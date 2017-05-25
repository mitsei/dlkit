"""Mixins for use by assessment package implementations"""
from bson import ObjectId

from collections import OrderedDict

import dlkit.abstract_osid.osid.errors as errors
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.calendaring.primitives import DateTime
from .objects import AssessmentSection, NULL_RESPONSE, UNANSWERED, QuestionList, Response, ResponseList,\
    ASSESSMENT_AUTHORITY
from .assessment_utilities import get_level_delta_for_parts, get_provider_manager, get_default_part_map,\
    get_default_question_map, get_assessment_part_lookup_session, get_item_lookup_session
from .objects import AssessmentSection
from ..utilities import JSONClientValidated


class PartSequenceSection(object):
    """Adds records to support AssessmentPart Sequencing."""

    def __init__(self, *args, **kwargs):
        super(PartSequenceSection, self).__init__(*args, **kwargs)

    def get_next_part_for_part(self, part, level=0, children_checked=False):
        check_parent = True
        rule = self._get_first_successful_sequence_rule_for_part(part)
        part_id = part.get_id()
        if rule is not None:  # A SequenceRule trumps everything.
            next_part = rule.get_next_assessment_part()
            level = level + get_level_delta_for_parts(part, next_part)
            check_parent = False
        elif part.has_children() and not children_checked:
            try:
                child_id = part.get_child_ids().next()
                # apls = get_assessment_part_lookup_session(part._runtime, part._proxy, self)
                # apls.use_unsequestered_assessment_part_view()
                # apls.use_federated_bank_view()
                # next_part = apls.get_assessment_part(child_id)
                next_part = self._get_assessment_part(child_id)
                level += 1
                check_parent = False
            except StopIteration:
                pass
        else:  # check to see if this part has a sibling that could be next
            sibling_ids = []
            if part.has_parent_part():
                parent = part.get_assessment_part()
                if parent.has_children():
                    sibling_ids = [str(ci) for ci in parent.get_child_ids()]
                if sibling_ids:
                    try:
                        next_part_id = Id(sibling_ids[sibling_ids.index(str(part_id)) + 1])
                        # apls = get_assessment_part_lookup_session(part._runtime, part._proxy, self)
                        # apls.use_unsequestered_assessment_part_view()
                        # apls.use_federated_bank_view()
                        # next_part = apls.get_assessment_part(next_part_id)
                        next_part = self._get_assessment_part(next_part_id)
                    except (ValueError, IndexError):
                        children_checked = True
                    else:
                        check_parent = False

        if check_parent and part.has_parent_part():  # We are at a lowest leaf and need to check parent
            next_part = self.get_next_part_for_part(
                part.get_assessment_part(),
                level - 1,
                children_checked)
        elif check_parent:
            raise errors.IllegalState()
        next_part._level_in_section = level
        return next_part

    def _get_first_successful_sequence_rule_for_part(self, part):
        mgr = get_provider_manager('ASSESSMENT_AUTHORING', runtime=self._runtime, proxy=self._proxy)
        rule_lookup_session = mgr.get_sequence_rule_lookup_session(proxy=self._proxy)
        rule_lookup_session.use_federated_bank_view()
        for rule in rule_lookup_session.get_sequence_rules_for_assessment_part(part.get_id()):
            if rule._evaluates_true():  # Or wherever this wants to be evaluated
                return rule
        return None


class AssessmentSessionSection(object):
    """Adds records to support AssessmentSession functionality."""

    def __init__(self, *args, **kwargs):
        super(AssessmentSessionSection, self).__init__(*args, **kwargs)
        self._assessment_parts = dict()
        self._item_lookup_session = None
        self._assessment_part_lookup_session = None
        self._item_id_list = []
        if 'actualStartTime' not in self._my_map:
            self._my_map['actualStartTime'] = None
        if '_id' not in self._my_map:
            # could happen if not created with items -- then self._initialize_part_map()
            # will not call self._save(). But we need to assign it an ID
            # this has to happen before _initialize_part_map(),
            # otherwise Parts won't be able to work...
            self._save()
        if 'questions' not in self._my_map:  # This is the first instantiation
            self._initialize_part_map()

    def _initialize_part_map(self):
        """Sets up assessmentPartMap with as much information as is initially available."""
        self._my_map['assessmentParts'] = []
        self._my_map['questions'] = []
        item_ids = self._assessment_part.get_item_ids()
        if item_ids.available():
            # This is a simple section:
            self._load_simple_section_questions(item_ids)
        else:
            # This goes down the winding path...
            # let's not call this...seems redundant, and per Jeff, this might
            # save us time.
            # self._update_questions()
            pass

    def _get_part_map(self, part_id):
        """ from self._my_map['assessmentParts'], return the one part map
        with ID that matches the one passed in"""
        return [p for p in self._my_map['assessmentParts']
                if p['assessmentPartId'] == str(part_id)][0]

    def _insert_part_map(self, part_map, index=-1):
        """ add a part map to self._my_map['assessmentParts']"""
        if index == -1:
            self._my_map['assessmentParts'].append(part_map)
        else:
            self._my_map['assessmentParts'].insert(index, part_map)

    def _part_ids(self):
        """private convenience method to return a list of the part Ids in this section"""
        return [p['assessmentPartId'] for p in self._my_map['assessmentParts']]

    def _load_simple_section_questions(self, item_ids):
        """For loading the simple section case (common)

        just load the questions for the section, and insert the one part
        into assessment part map.

        """
        self._insert_part_map(
            get_default_part_map(self._assessment_part_id,
                                 0,
                                 self._assessment_part.are_items_sequential()))
        lookup_session = self._get_item_lookup_session()
        items = lookup_session.get_items_by_ids(item_ids)
        display_num = 1
        for item in items:
            question_id = item.get_question().get_id()
            self._my_map['questions'].append(get_default_question_map(
                item.get_id(),
                question_id,
                self._assessment_part_id,
                [display_num]))
            display_num += 1
        self._save()

    def _save(self):
        """Saves the current state of this AssessmentSection to database.

        Should be called every time the question map changes.

        """
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentSection',
                                         runtime=self._runtime)
        if '_id' in self._my_map:  # This is the first time:
            collection.save(self._my_map)
        else:
            insert_result = collection.insert_one(self._my_map)
            self._my_map = collection.find_one({'_id': insert_result.inserted_id})  # To get the _id

    def _delete(self):
        """Deletes this AssessmentSection from database.

        Will be called by AssessmentTaken._delete() for clean-up purposes.

        """
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentSection',
                                         runtime=self._runtime)
        collection.delete_one({'_id': ObjectId(self.get_id().get_identifier())})

    # Model for question map to be constructed through taking an assessment section:
    #
    #   'questions': [{
    #       '_id': <a unique ObjectId()>,
    #       'questionId: <idstr of question>,
    #       'itemId': <idstr of question's item>,
    #       'partId': <idstr of the part this question came from>,
    #       'labelElements': <list for constructing label, based on part levels, like [3, 1, 2]
    #       'responses: [<dict of the student's Answer>,
    #                    <or {'missingResponse': NULL_RESPONSE} if response is skipped or cleared>,
    #                    <or {'missingResponse': UNANSWERED} if no attempts have yet been made on question>,
    #                    <etc for additional attempts>...]
    #       }, <etc for additional questions>...]

    def is_simple_section(self):
        """Tests if this section is simple (ie, items assigned directly to Section Part)."""
        item_ids = self._get_assessment_part(self._assessment_part_id).get_item_ids()
        if item_ids.available():
            return True
        return False

    def _get_assessment_part(self, part_id=None):
        """Gets an AssessmentPart given a part_id.

        Returns this Section's own part if part_id is None.

        Make this a private part, so that it doesn't collide with the AssessmentPart.get_assessment_part
        method, which does not expect any arguments...

        """
        if part_id is None:
            return self._assessment_part
        if part_id not in self._assessment_parts:
            lookup_session = self._get_assessment_part_lookup_session()
            self._assessment_parts[part_id] = lookup_session.get_assessment_part(part_id)
        return self._assessment_parts[part_id]

    def _update_from_database(self):
        """Updates map to latest state in database.

        Should be called prior to major object events to assure that an
        assessment being taken on multiple devices are reasonably synchronized.

        """
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentSection',
                                         runtime=self._runtime)
        self._my_map = collection.find_one({'_id': self._my_map['_id']})

    def _update_questions(self):
        """Updates questions known to this Section"""
        if self.is_simple_section():
            return  # we don't need to go through any this for simple sections
        # ideally, we would update the parts map and questions list
        # at the same time as _get_parts(), to not run into the
        # issue where magic parts are initialized (with items)
        # ignorant of their "sibling" magic part items...
        # because the section hasn't been updated or saved to database
        part_list = self._get_parts()
        if len(part_list) > len(self._my_map['assessmentParts']):
            self._update_assessment_parts_map(part_list)
            self._update_questions_list(part_list)
            self._save()

    def _get_parts(self):
        parts = list()
        part = self._assessment_part
        part._level_in_section = 0
        finished = False
        while not finished:

            try:
                magic_parts = part.get_parts(reference_level=part._level_in_section)
            except AttributeError:
                pass
            else:
                # First make sure all these magic parts are cached
                for part in list(magic_parts):
                    part_id = part.get_id()
                    if part_id not in self._assessment_parts:
                        self._assessment_parts[part_id] = part
                parts += magic_parts

            # Now get the next part through normal means:
            try:
                part = self.get_next_part_for_part(part, level=part._level_in_section)
            except errors.IllegalState:
                finished = True
            else:
                if part.has_items():
                    # THIS is a hack -- to get around repeated items within the same
                    # section....
                    for item_id in part.get_item_ids():
                        if str(item_id) not in self._item_id_list:
                            self._item_id_list.append(str(item_id))
                    parts.append(part)
        return parts

    def _update_assessment_parts_map(self, part_list):
        """Updates the part map.

        Called before question list gets updated if it is determined that the
        sections assessmentPart map is out of date with the current part list.

        """
        for part in part_list:
            # perhaps look for a "level offset"?
            level = part._level_in_section  # plus or minus "level offset"?
            if str(part.get_id()) not in self._part_ids():
                self._insert_part_map(get_default_part_map(
                    part.get_id(), level, part.are_items_sequential()),
                    index=part_list.index(part))

    def _update_questions_list(self, part_list):

        def get_question_display_elements(question_part_map):
            """Get the parts only in this route.

            Go backwards until you find a part with level 1?
            stop there, so that you don't get shifted to the previous part
            i.e. [level 1, level 2, level 1, level 2]
                 when running this on the last question, you want to get
                 the indices relative to the second level 1, not including
                 the first two parts

            self._my_map['assessmentParts'] = [
                {'assessmentPartId': <idstr of a part. Might be a 'magic' id>,
                 'level': 1,
                 'requiresSequentialItems': False},
                {'assessmentPartId': <idstr of a part. Might be a 'magic' id>,
                 'level': 2,
                 'requiresSequentialItems': True},
                {'assessmentPartId': <idstr of a part. Might be a 'magic' id>,
                 'level': 1
                 'requiresSequentialItems': False},
                <etc, for additional assessment parts>,
            ]
            """
            my_display_elements = []
            parts_in_same_route = {}

            original_question_level = question_part_map['level']
            if question_part_map['level'] > 1:
                question_map = question_part_map
                search_index = part_list.index(part)
                level_1_part = {}
                found_target_question = False
                while not found_target_question:
                    if question_map['level'] <= original_question_level:
                        if question_map['level'] not in parts_in_same_route:
                            parts_in_same_route[question_map['level']] = []
                        parts_in_same_route[question_map['level']].insert(0, question_map)
                    search_index -= 1
                    question_map = self._get_part_map(part_list[search_index].get_id())
                    level = question_map['level']
                    if level == 1:
                        level_1_part = question_map  # let's preserve this for later
                        found_target_question = True
            else:
                level_1_part = question_part_map

            # get all level 1 parts to get the first index
            all_level_1_parts = [p
                                 for p in self._my_map['assessmentParts']
                                 if p['level'] == 1]
            my_display_elements.append(all_level_1_parts.index(level_1_part) + 1)

            # With Python 3, need to sort parts_in_same_route so that
            # the lowest level is first
            parts_in_same_route = OrderedDict(sorted(parts_in_same_route.items(), key=lambda k: k[0]))
            for level, waypoints in parts_in_same_route.items():
                # for each part in the route at a given level, sum up the number of questions
                # that have appeared in that part
                # start the last level at 1, because the "current" question being injected
                # doesn't exist in self._my_map yet
                if level == question_part_map['level']:
                    count = 1
                else:
                    count = 0

                for waypoint in waypoints:
                    waypoint_questions = [q
                                          for q in self._my_map['questions']
                                          if q['assessmentPartId'] == waypoint['assessmentPartId']]
                    count += len(waypoint_questions)
                my_display_elements.append(count)

            return my_display_elements

        index = 0
        for part in part_list:
            if (len(self._my_map['questions']) == index or
                    self._my_map['questions'][index]['assessmentPartId'] != str(part.get_id())):
                part_id = part.get_id()
                part_map = self._get_part_map(part_id)
                for item in self._get_assessment_part_lookup_session().get_assessment_part(part_id).get_items():
                    # need to update the display elements for the question
                    # kind of convoluted, but the first part of the display elements
                    # is the "part_index" of the previous level 1 question (if parts were organized
                    # by level) ... let's re-organize the parts.
                    display_elements = get_question_display_elements(part_map)
                    self._my_map['questions'].insert(index, get_default_question_map(
                        item.get_id(),
                        item.get_question().get_id(),
                        part_id,
                        display_elements))
                    index += 1

            else:  # skip through all remaining questions for this part
                part_id = part.get_id()
                part_map = self._get_part_map(part_id)
                while (len(self._my_map['questions']) > index and
                       self._my_map['questions'][index]['assessmentPartId'] == part_map['assessmentPartId']):
                    index += 1

    def _get_assessment_part_lookup_session(self):  # get_assessment_part_lookup_session should be mixed in
        if self._assessment_part_lookup_session is None:
            session = get_assessment_part_lookup_session(self._runtime,
                                                         self._proxy,
                                                         self)
            session.use_unsequestered_assessment_part_view()
            session.use_federated_bank_view()
            self._assessment_part_lookup_session = session
        try:
            self._assessment_part_lookup_session.update_section(self)
        except AttributeError:
            pass
        return self._assessment_part_lookup_session

    def _get_item_lookup_session(self):  # get_item_lookup_session should be mixed in
        if self._item_lookup_session is None:
            session = get_item_lookup_session(self._runtime, self._proxy)
            session.use_federated_bank_view()
            self._item_lookup_session = session
        return self._item_lookup_session

    def _get_question_map(self, question_id):
        """get question map from questions matching question_id

        This can make sense of both Section assigned Ids or normal Question/Item Ids

        """
        if question_id.get_authority() == ASSESSMENT_AUTHORITY:
            key = '_id'
            match_value = ObjectId(question_id.get_identifier())
        else:
            key = 'questionId'
            match_value = str(question_id)
        for question_map in self._my_map['questions']:
            if question_map[key] == match_value:
                return question_map
        raise errors.NotFound()

    def get_question_ids_for_assessment_part(self, assessment_part_id):
        """convenience method returns unique question ids associated with an assessment_part_id"""
        question_ids = []
        for question_map in self._my_map['questions']:
            if question_map['assessmentPartId'] == str(assessment_part_id):
                question_ids.append(self.get_question(question_map=question_map).get_id())
        return question_ids

    def get_item_ids_for_assessment_part(self, assessment_part_id):
        """convenience method returns item ids associated with an assessment_part_id"""
        item_ids = []
        for question_map in self._my_map['questions']:
            if question_map['assessmentPartId'] == str(assessment_part_id):
                item_ids.append(Id(question_map['itemId']))
        return item_ids

    def _is_question_sequential(self, question_map):
        """determine if sequential rules apply to question for getting next question

        Currently only checks the assessment part's items sequential

        """
        return [pm['requiresSequentialItems'] for
                pm in self._my_map['assessmentParts'] if
                pm['assessmentPartId'] == question_map['assessmentPartId']][0]

    def _get_item(self, question_id):
        """we need a middle-man method to convert the unique "assessment-session"
            authority question_ids into "real" itemIds
        BUT this also has to return the "magic" item, so we can't rely
        on
                question = self.get_question(question_id)
                ils = self._get_item_lookup_session()
                return ils.get_item(Id(question._my_map['itemId']))
        """
        question_map = self._get_question_map(question_id)  # Throws NotFound()
        real_question_id = Id(question_map['questionId'])
        return self._get_item_lookup_session().get_item(real_question_id)

    def has_started(self):
        """Checks if the taker has started taking this Section

        Meaning that the taker has retrieved the first question or all questions
        for the first time

        """
        if self._my_map['actualStartTime'] is None:
            return False
        return True

    def get_actual_start_time(self):
        """The DateTime the taker first retrieved question or questions from this Section"""
        if self._my_map['actualStartTime'] is None:
            raise errors.IllegalState()
        return self._my_map['actualStartTime']

    def get_questions(self, answered=None, honor_sequential=True, update=True):
        """gets all available questions for this section

        if answered == False: only return next unanswered question
        if answered == True: only return next answered question
        if answered in None: return next question whether answered or not
        if honor_sequential == True: only return questions if section or part
                                     is set to sequential items

        """

        def update_question_list():
            """Supportive function to aid readability of _get_questions."""
            latest_question_response = question_map['responses'][0]
            question_answered = False
            # take missingResponse == UNANSWERED or NULL_RESPONSE as an unanswered question
            if 'missingResponse' not in latest_question_response:
                question_answered = True

            if answered is None or answered == question_answered:
                question_list.append(self.get_question(question_map=question_map))
            return question_answered

        prev_question_answered = True
        question_list = []
        if update:
            self._update_questions()  # Make sure questions list is current
        for question_map in self._my_map['questions']:
            if self._is_question_sequential(question_map) and honor_sequential:
                if prev_question_answered:
                    prev_question_answered = update_question_list()
            else:
                update_question_list()
        if self._my_map['actualStartTime'] is None:
            self._my_map['actualStartTime'] = DateTime.utcnow()
        return QuestionList(question_list, runtime=self._runtime, proxy=self._proxy)

    def get_question(self, question_id=None, question_map=None):
        if question_id is not None:
            question_map = self._get_question_map(question_id)  # Throws NotFound()
        real_question_id = Id(question_map['questionId'])
        display_elements = question_map['displayElements']
        item = self._get_item_lookup_session().get_item(real_question_id)
        question = item.get_question()

        # Try to set a new display name and label
        try:
            if len(display_elements) > 0:
                new_display_name = [str(e) for e in display_elements]
                question.set_display_label('.'.join(new_display_name))
        except AttributeError:
            pass

        # Claim authority over this question:
        question._authority = ASSESSMENT_AUTHORITY

        # Override Item Id of this question (this is the Id that Questions report)
        question._item_id = Id(namespace='assessment.Item',
                               identifier=str(question_map['_id']),
                               authority=ASSESSMENT_AUTHORITY)
        return question

    def get_answers(self, question_id):
        # don't use the self._get_item() convenience method here
        # because we need to preserve the magic params (if any) present
        # in the questionId
        question_map = self._get_question_map(question_id)  # will raise NotFound()
        ils = self._get_item_lookup_session()
        item = ils.get_item(Id(question_map['questionId']))
        answers = list(item.get_answers())
        try:
            answers += list(item.get_wrong_answers())
        except AttributeError:
            pass
        return answers  # Should this return and AnswerList?

    def get_first_question(self):
        if self._my_map['actualStartTime'] is None:
            self._my_map['actualStartTime'] = DateTime.utcnow()
        return self.get_question(question_map=self._my_map['questions'][0])

    def get_next_question(self, question_id, answered=None, reverse=False, honor_sequential=True):
        """Inspects question map to return the next available question.

        if answered == False: only return next unanswered question
        if answered == True: only return next answered question
        if answered in None: return next question whether answered or not
        if reverse == True: go backwards - effectively get_previous_question
        if honor_sequential == True: only return questions if section or part
                                     is set to sequential items

        """
        self._update_questions()  # Make sure questions list is current
        question_map = self._get_question_map(question_id)  # will raise NotFound()
        questions = list(self._my_map['questions'])
        if reverse:
            questions = questions[::-1]
            error_text = ' previous '
        else:
            if 'missingResponse' in question_map:
                if self._is_question_sequential(question_map) and honor_sequential:
                    raise errors.IllegalState('Next question is not yet available')
            error_text = ' next '
        if questions[-1] == question_map:
            raise errors.IllegalState('No ' + error_text + ' questions available')
        index = questions.index(question_map) + 1
        for question_map in questions[index:]:
            latest_question_response = question_map['responses'][0]
            question_answered = False
            # take missingResponse == UNANSWERED or NULL_RESPONSE as an unanswered question
            if 'missingResponse' not in latest_question_response:
                question_answered = True
            if answered is None or question_answered == answered:
                return self.get_question(question_map=question_map)
        raise errors.IllegalState('No ' + error_text + ' question matching parameters was found')

    def submit_response(self, question_id, answer_form=None):
        """Updates assessmentParts map to insert an item response.

        answer_form is None indicates that the current response is to be cleared

        """
        if answer_form is None:
            response = {'missingResponse': NULL_RESPONSE,
                        'itemId': str(question_id)}
        else:
            response = dict(answer_form._my_map)
            response['submissionTime'] = DateTime.utcnow()
            try:
                response['isCorrect'] = self._get_item(question_id).is_response_correct(
                    Response(osid_object_map=response, runtime=self._runtime, proxy=self._proxy))
            except (errors.IllegalState, errors.NotFound):
                response['isCorrect'] = None
        response['submissionTime'] = DateTime.utcnow()

        question_map = self._get_question_map(question_id)  # will raise NotFound()
        if ('missingResponse' in question_map['responses'][0] and
                question_map['responses'][0]['missingResponse'] == UNANSWERED):
            question_map['responses'] = []  # clear unanswered response
        question_map['responses'].insert(0, response)
        self._save()

    def get_response(self, question_id):
        """Gets the response for question_id"""
        question_map = self._get_question_map(question_id)  # will raise NotFound()
        return self._get_response_from_question_map(question_map)

    def get_responses(self):
        """Gets list of the latest responses"""
        response_list = []
        for question_map in self._my_map['questions']:
            response_list.append(self._get_response_from_question_map(question_map))
        return ResponseList(response_list)

    def _get_response_from_question_map(self, question_map):
        """Gets the a Response from the provided question_map"""
        return self._get_response_from_response_map(question_map['responses'][0],
                                                    question_map['responses'][1:])

    def _get_response_from_response_map(self, response_map, additional_attempts=None):
        return Response(osid_object_map=response_map,
                        additional_attempts=additional_attempts,
                        runtime=self._runtime,
                        proxy=self._proxy,
                        section=self)

    def is_question_answered(self, question_id):
        """has the question matching item_id been answered and not skipped"""
        question_map = self._get_question_map(question_id)  # will raise NotFound()
        if 'missingResponse' in question_map['responses'][0]:
            return False
        else:
            return True

    def is_feedback_available(self, question_id):
        """is feedback available for item"""
        response = self.get_response(question_id)
        item = self._get_item(question_id)
        if response.is_answered():
            return item.is_feedback_available_for_response(response)
        return item.is_feedback_available()

    def get_feedback(self, question_id):
        """get feedback for item"""
        response = self.get_response(question_id)
        item = self._get_item(response.get_item_id())
        if response.is_answered():
            try:
                return item.get_feedback_for_response(response)
            except errors.IllegalState:
                pass
        else:
            return item.get_feedback()  # raises IllegalState

    def get_confused_learning_objective_ids(self, question_id):
        """get confused objective ids available for the question"""
        response = self.get_response(question_id)
        if response.is_answered():
            item = self._get_item(response.get_item_id())
            return item.get_confused_learning_objective_ids_for_response(response)
        raise errors.IllegalState()

    def is_correctness_available(self, question_id):
        """is a measure of correctness available for the question"""
        response = self.get_response(question_id)
        if response.is_answered():
            item = self._get_item(response.get_item_id())
            return item.is_correctness_available_for_response(response)
        return False

    def is_correct(self, question_id):
        """is the question answered correctly"""
        response = self.get_response(question_id=question_id)
        if response.is_answered():
            item = self._get_item(response.get_item_id())
            return item.is_response_correct(response)
        raise errors.IllegalState()

    def get_correctness(self, question_id):
        """get measure of correctness for the question"""
        response = self.get_response(question_id)
        if response.is_answered():
            item = self._get_item(response.get_item_id())
            return item.get_correctness_for_response(response)
        raise errors.IllegalState()

    def finish(self):
        """Declare this section finished"""
        self._my_map['over'] = True  # finished == over?
        self._my_map['completionTime'] = DateTime.utcnow()
        self._save()

    def is_over(self):
        """Check if this section is over"""
        if 'over' in self._my_map and self._my_map['over']:
            return True
        return False

    def is_complete(self):
        """Check all Questions for completeness

        For now, completeness simply means that all questions have been
        responded to and not skipped or cleared.

        """
        self._update_questions()  # Make sure questions list is current
        for question_map in self._my_map['questions']:
            if 'missingResponse' in question_map['responses'][0]:
                return False
        return True

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['actualStartTime'] is not None:
            actual_start_time = obj_map['actualStartTime']
            obj_map['actualStartTime'] = dict()
            obj_map['actualStartTime']['year'] = actual_start_time.year
            obj_map['actualStartTime']['month'] = actual_start_time.month
            obj_map['actualStartTime']['day'] = actual_start_time.day
            obj_map['actualStartTime']['hour'] = actual_start_time.hour
            obj_map['actualStartTime']['minute'] = actual_start_time.minute
            obj_map['actualStartTime']['second'] = actual_start_time.second
            obj_map['actualStartTime']['microsecond'] = actual_start_time.microsecond
        obj_map = AssessmentSection.get_object_map(self, obj_map)
        return obj_map


class LoadedSection(PartSequenceSection, AssessmentSessionSection, AssessmentSection):
    pass
