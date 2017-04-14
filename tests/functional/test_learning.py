import datetime

from decimal import Decimal

from dlkit.runtime.primordium import DateTime, Id, Type

from .utilities.testing import DLKitTestCase, serialize_date


class ProficiencyTests(DLKitTestCase):
    def create_objective(self):
        form = self._bank.get_objective_form_for_create([])
        form.display_name = 'test objective'
        form.set_genus_type(
            Type('learning.Objective%3Amc3.learning.generic.outcome%40ODL.MIT.EDU'))
        return self._bank.create_objective(form)

    def create_proficiency(self):
        form = self._bank.get_proficiency_form_for_create(self._test_obj_id,
                                                          self._test_kerb,
                                                          [])
        form.set_completion(Decimal('50.0'))
        return self._bank.create_proficiency(form)

    def setUp(self):
        super(ProficiencyTests, self).setUp()

        self._bank = self._get_test_objective_bank()
        self._test_obj = self.create_objective()
        self._test_obj_id = self._test_obj.ident
        self._test_kerb = Id('fake%3Adlkit%2540mit.edu%40bazzim.MIT.EDU')

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(ProficiencyTests, self).tearDown()

    def test_can_set_proficiency_with_kerberos(self):
        form = self._bank.get_proficiency_form_for_create(self._test_obj_id,
                                                          self._test_kerb,
                                                          [])
        form.set_completion(Decimal('50.0'))
        proficiency = self._bank.create_proficiency(form)
        proficiency_map = proficiency.object_map
        self.assertEqual(
            proficiency_map['resourceId'],
            str(self._test_kerb)
        )
        self.assertEqual(
            proficiency_map['objectiveId'],
            str(self._test_obj_id)
        )
        self.assertEqual(
            proficiency_map['completion'],
            50.0
        )

    def test_can_get_proficiency(self):
        proficiency = self.create_proficiency()
        refreshed = self._bank.get_proficiency(proficiency.ident)
        proficiency_map = refreshed.object_map
        self.assertEqual(
            proficiency_map['resourceId'],
            str(self._test_kerb)
        )
        self.assertEqual(
            proficiency_map['objectiveId'],
            str(self._test_obj_id)
        )
        self.assertEqual(
            proficiency_map['completion'],
            50.0
        )

    def test_can_get_proficiency_objective(self):
        proficiency = self.create_proficiency()
        obj = proficiency.get_objective()
        self.assertEqual(
            str(obj.ident),
            str(self._test_obj_id)
        )
        self.assertEqual(
            obj.object_map['genusTypeId'],
            'learning.Objective%3Amc3.learning.generic.outcome%40ODL.MIT.EDU'
        )

    def test_can_get_proficiencies_by_kerberos(self):
        proficiency = self.create_proficiency()
        proficiencies = self._bank.get_proficiencies_for_resource(self._test_kerb)
        self.assertEqual(
            proficiencies.available(),
            1
        )
        self.assertEqual(
            str(proficiencies.next().ident),
            str(proficiency.ident)
        )

    def test_can_get_proficiencies_by_kerberos_in_date_range(self):
        proficiency = self.create_proficiency()
        today = datetime.datetime.utcnow()
        yesterday = today - datetime.timedelta(days=1)

        start_date = DateTime(**serialize_date(yesterday))
        end_date = DateTime(**serialize_date(today))

        proficiencies = self._bank.get_proficiencies_for_resource_on_date(self._test_kerb,
                                                                          start_date,
                                                                          end_date)
        self.assertEqual(
            proficiencies.available(),
            1
        )
        self.assertEqual(
            str(proficiencies.next().ident),
            str(proficiency.ident)
        )

    def test_no_proficiencies_returned_when_out_of_date_range_but_matching_kerberos(self):
        today = datetime.datetime.utcnow()
        yesterday = today - datetime.timedelta(days=1)
        two_days_ago = yesterday - datetime.timedelta(days=2)

        proficiency = self.create_proficiency()

        start_date = DateTime(**serialize_date(two_days_ago))
        end_date = DateTime(**serialize_date(yesterday))

        proficiencies = self._bank.get_proficiencies_for_resource_on_date(self._test_kerb,
                                                                          start_date,
                                                                          end_date)
        self.assertEqual(
            proficiencies.available(),
            0
        )

    def test_no_proficiencies_returned_when_no_kerberos_match(self):
        proficiency = self.create_proficiency()
        today = datetime.datetime.utcnow()
        yesterday = today - datetime.timedelta(days=1)

        start_date = DateTime(**serialize_date(yesterday))
        end_date = DateTime(**serialize_date(today))

        proficiencies = self._bank.get_proficiencies_for_resource_on_date('foo',
                                                                          start_date,
                                                                          end_date)
        self.assertEqual(
            proficiencies.available(),
            0
        )

    def test_no_proficiencies_returned_when_out_of_date_range_and_no_matching_kerberos(self):
        today = datetime.datetime.utcnow()
        yesterday = today - datetime.timedelta(days=1)
        two_days_ago = yesterday - datetime.timedelta(days=2)

        proficiency = self.create_proficiency()

        start_date = DateTime(**serialize_date(two_days_ago))
        end_date = DateTime(**serialize_date(yesterday))

        proficiencies = self._bank.get_proficiencies_for_resource_on_date('foo',
                                                                          start_date,
                                                                          end_date)
        self.assertEqual(
            proficiencies.available(),
            0
        )
