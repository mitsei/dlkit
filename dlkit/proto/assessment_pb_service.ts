// package: dlkit.proto.assessment
// file: dlkit/proto/assessment.proto

import * as dlkit_proto_assessment_pb from "../../dlkit/proto/assessment_pb";
import * as dlkit_primordium_calendaring_primitives_pb from "../../dlkit/primordium/calendaring/primitives_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_grading_pb from "../../dlkit/proto/grading_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class AssessmentSession {
  static serviceName = "dlkit.proto.assessment.AssessmentSession";
}
export namespace AssessmentSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanTakeAssessments {
    static readonly methodName = "CanTakeAssessments";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanTakeAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanTakeAssessmentsReply;
  }
  export class HasAssessmentBegun {
    static readonly methodName = "HasAssessmentBegun";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasAssessmentBegunRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasAssessmentBegunReply;
  }
  export class IsAssessmentOver {
    static readonly methodName = "IsAssessmentOver";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsAssessmentOverRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsAssessmentOverReply;
  }
  export class RequiresSynchronousSections {
    static readonly methodName = "RequiresSynchronousSections";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RequiresSynchronousSectionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RequiresSynchronousSectionsReply;
  }
  export class GetFirstAssessmentSection {
    static readonly methodName = "GetFirstAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetFirstAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetFirstAssessmentSectionReply;
  }
  export class HasNextAssessmentSection {
    static readonly methodName = "HasNextAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasNextAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasNextAssessmentSectionReply;
  }
  export class GetNextAssessmentSection {
    static readonly methodName = "GetNextAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetNextAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetNextAssessmentSectionReply;
  }
  export class HasPreviousAssessmentSection {
    static readonly methodName = "HasPreviousAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasPreviousAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasPreviousAssessmentSectionReply;
  }
  export class GetPreviousAssessmentSection {
    static readonly methodName = "GetPreviousAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetPreviousAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetPreviousAssessmentSectionReply;
  }
  export class GetAssessmentSection {
    static readonly methodName = "GetAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentSectionReply;
  }
  export class GetAssessmentSections {
    static readonly methodName = "GetAssessmentSections";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentSectionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentSection;
  }
  export class IsAssessmentSectionComplete {
    static readonly methodName = "IsAssessmentSectionComplete";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsAssessmentSectionCompleteRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsAssessmentSectionCompleteReply;
  }
  export class GetIncompleteAssessmentSections {
    static readonly methodName = "GetIncompleteAssessmentSections";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetIncompleteAssessmentSectionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentSection;
  }
  export class HasAssessmentSectionBegun {
    static readonly methodName = "HasAssessmentSectionBegun";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasAssessmentSectionBegunRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasAssessmentSectionBegunReply;
  }
  export class IsAssessmentSectionOver {
    static readonly methodName = "IsAssessmentSectionOver";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsAssessmentSectionOverRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsAssessmentSectionOverReply;
  }
  export class RequiresSynchronousResponses {
    static readonly methodName = "RequiresSynchronousResponses";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RequiresSynchronousResponsesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RequiresSynchronousResponsesReply;
  }
  export class GetFirstQuestion {
    static readonly methodName = "GetFirstQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetFirstQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetFirstQuestionReply;
  }
  export class HasNextQuestion {
    static readonly methodName = "HasNextQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasNextQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasNextQuestionReply;
  }
  export class GetNextQuestion {
    static readonly methodName = "GetNextQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetNextQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetNextQuestionReply;
  }
  export class HasPreviousQuestion {
    static readonly methodName = "HasPreviousQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasPreviousQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasPreviousQuestionReply;
  }
  export class GetPreviousQuestion {
    static readonly methodName = "GetPreviousQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetPreviousQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetPreviousQuestionReply;
  }
  export class GetQuestion {
    static readonly methodName = "GetQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetQuestionReply;
  }
  export class GetQuestions {
    static readonly methodName = "GetQuestions";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetQuestionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Question;
  }
  export class GetResponseForm {
    static readonly methodName = "GetResponseForm";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetResponseFormRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetResponseFormReply;
  }
  export class SubmitResponse {
    static readonly methodName = "SubmitResponse";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.SubmitResponseRequest;
    static readonly responseType = dlkit_proto_assessment_pb.SubmitResponseReply;
  }
  export class SkipItem {
    static readonly methodName = "SkipItem";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.SkipItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.SkipItemReply;
  }
  export class IsQuestionAnswered {
    static readonly methodName = "IsQuestionAnswered";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsQuestionAnsweredRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsQuestionAnsweredReply;
  }
  export class GetUnansweredQuestions {
    static readonly methodName = "GetUnansweredQuestions";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetUnansweredQuestionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Question;
  }
  export class HasUnansweredQuestions {
    static readonly methodName = "HasUnansweredQuestions";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasUnansweredQuestionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasUnansweredQuestionsReply;
  }
  export class GetFirstUnansweredQuestion {
    static readonly methodName = "GetFirstUnansweredQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetFirstUnansweredQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetFirstUnansweredQuestionReply;
  }
  export class HasNextUnansweredQuestion {
    static readonly methodName = "HasNextUnansweredQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasNextUnansweredQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasNextUnansweredQuestionReply;
  }
  export class GetNextUnansweredQuestion {
    static readonly methodName = "GetNextUnansweredQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetNextUnansweredQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetNextUnansweredQuestionReply;
  }
  export class HasPreviousUnansweredQuestion {
    static readonly methodName = "HasPreviousUnansweredQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasPreviousUnansweredQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasPreviousUnansweredQuestionReply;
  }
  export class GetPreviousUnansweredQuestion {
    static readonly methodName = "GetPreviousUnansweredQuestion";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetPreviousUnansweredQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetPreviousUnansweredQuestionReply;
  }
  export class GetResponse {
    static readonly methodName = "GetResponse";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetResponseRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetResponseReply;
  }
  export class GetResponses {
    static readonly methodName = "GetResponses";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetResponsesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Response;
  }
  export class ClearResponse {
    static readonly methodName = "ClearResponse";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.ClearResponseRequest;
    static readonly responseType = dlkit_proto_assessment_pb.ClearResponseReply;
  }
  export class FinishAssessmentSection {
    static readonly methodName = "FinishAssessmentSection";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.FinishAssessmentSectionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.FinishAssessmentSectionReply;
  }
  export class IsAnswerAvailable {
    static readonly methodName = "IsAnswerAvailable";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsAnswerAvailableRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsAnswerAvailableReply;
  }
  export class GetAnswers {
    static readonly methodName = "GetAnswers";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAnswersRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Answer;
  }
  export class FinishAssessment {
    static readonly methodName = "FinishAssessment";
    static readonly service = AssessmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.FinishAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.FinishAssessmentReply;
  }
}
export class AssessmentResultsSession {
  static serviceName = "dlkit.proto.assessment.AssessmentResultsSession";
}
export namespace AssessmentResultsSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanAccessAssessmentResults {
    static readonly methodName = "CanAccessAssessmentResults";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAccessAssessmentResultsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAccessAssessmentResultsReply;
  }
  export class GetItems {
    static readonly methodName = "GetItems";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetResponses {
    static readonly methodName = "GetResponses";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetResponsesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Response;
  }
  export class AreResultsAvailable {
    static readonly methodName = "AreResultsAvailable";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AreResultsAvailableRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AreResultsAvailableReply;
  }
  export class GetGradeEntries {
    static readonly methodName = "GetGradeEntries";
    static readonly service = AssessmentResultsSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
}
export class ItemLookupSession {
  static serviceName = "dlkit.proto.assessment.ItemLookupSession";
}
export namespace ItemLookupSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanLookupItems {
    static readonly methodName = "CanLookupItems";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupItemsReply;
  }
  export class UseComparativeItemView {
    static readonly methodName = "UseComparativeItemView";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeItemViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeItemViewReply;
  }
  export class UsePlenaryItemView {
    static readonly methodName = "UsePlenaryItemView";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryItemViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryItemViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetItem {
    static readonly methodName = "GetItem";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemReply;
  }
  export class GetItemsByIds {
    static readonly methodName = "GetItemsByIds";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByGenusType {
    static readonly methodName = "GetItemsByGenusType";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByParentGenusType {
    static readonly methodName = "GetItemsByParentGenusType";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByRecordType {
    static readonly methodName = "GetItemsByRecordType";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByQuestion {
    static readonly methodName = "GetItemsByQuestion";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByAnswer {
    static readonly methodName = "GetItemsByAnswer";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByAnswerRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByLearningObjective {
    static readonly methodName = "GetItemsByLearningObjective";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByLearningObjectiveRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemsByLearningObjectives {
    static readonly methodName = "GetItemsByLearningObjectives";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByLearningObjectivesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItems {
    static readonly methodName = "GetItems";
    static readonly service = ItemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
}
export class ItemQuerySession {
  static serviceName = "dlkit.proto.assessment.ItemQuerySession";
}
export namespace ItemQuerySession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanSearchItems {
    static readonly methodName = "CanSearchItems";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanSearchItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanSearchItemsReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetItemQuery {
    static readonly methodName = "GetItemQuery";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemQueryReply;
  }
  export class GetItemsByQuery {
    static readonly methodName = "GetItemsByQuery";
    static readonly service = ItemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
}
export class ItemSearchSession {
  static serviceName = "dlkit.proto.assessment.ItemSearchSession";
}
export namespace ItemSearchSession {
  export class GetItemSearch {
    static readonly methodName = "GetItemSearch";
    static readonly service = ItemSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemSearchRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemSearchReply;
  }
  export class GetItemSearchOrder {
    static readonly methodName = "GetItemSearchOrder";
    static readonly service = ItemSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemSearchOrderRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemSearchOrderReply;
  }
  export class GetItemsBySearch {
    static readonly methodName = "GetItemsBySearch";
    static readonly service = ItemSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsBySearchRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemsBySearchReply;
  }
  export class GetItemQueryFromInspector {
    static readonly methodName = "GetItemQueryFromInspector";
    static readonly service = ItemSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemQueryFromInspectorRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemQueryFromInspectorReply;
  }
}
export class ItemAdminSession {
  static serviceName = "dlkit.proto.assessment.ItemAdminSession";
}
export namespace ItemAdminSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanCreateItems {
    static readonly methodName = "CanCreateItems";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateItemsReply;
  }
  export class CanCreateItemWithRecordTypes {
    static readonly methodName = "CanCreateItemWithRecordTypes";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateItemWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateItemWithRecordTypesReply;
  }
  export class GetItemFormForCreate {
    static readonly methodName = "GetItemFormForCreate";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemFormForCreateReply;
  }
  export class CreateItem {
    static readonly methodName = "CreateItem";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateItemReply;
  }
  export class CanUpdateItems {
    static readonly methodName = "CanUpdateItems";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateItemsReply;
  }
  export class GetItemFormForUpdate {
    static readonly methodName = "GetItemFormForUpdate";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetItemFormForUpdateReply;
  }
  export class UpdateItem {
    static readonly methodName = "UpdateItem";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateItemReply;
  }
  export class CanDeleteItems {
    static readonly methodName = "CanDeleteItems";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteItemsReply;
  }
  export class DeleteItem {
    static readonly methodName = "DeleteItem";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteItemReply;
  }
  export class CanManageItemAliases {
    static readonly methodName = "CanManageItemAliases";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanManageItemAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanManageItemAliasesReply;
  }
  export class AliasItem {
    static readonly methodName = "AliasItem";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AliasItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AliasItemReply;
  }
  export class CanCreateQuestions {
    static readonly methodName = "CanCreateQuestions";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateQuestionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateQuestionsReply;
  }
  export class CanCreateQuestionWithRecordTypes {
    static readonly methodName = "CanCreateQuestionWithRecordTypes";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateQuestionWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateQuestionWithRecordTypesReply;
  }
  export class GetQuestionFormForCreate {
    static readonly methodName = "GetQuestionFormForCreate";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetQuestionFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetQuestionFormForCreateReply;
  }
  export class CreateQuestion {
    static readonly methodName = "CreateQuestion";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateQuestionReply;
  }
  export class CanUpdateQuestions {
    static readonly methodName = "CanUpdateQuestions";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateQuestionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateQuestionsReply;
  }
  export class GetQuestionFormForUpdate {
    static readonly methodName = "GetQuestionFormForUpdate";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetQuestionFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetQuestionFormForUpdateReply;
  }
  export class UpdateQuestion {
    static readonly methodName = "UpdateQuestion";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateQuestionReply;
  }
  export class CanDeleteQuestions {
    static readonly methodName = "CanDeleteQuestions";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteQuestionsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteQuestionsReply;
  }
  export class DeleteQuestion {
    static readonly methodName = "DeleteQuestion";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteQuestionRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteQuestionReply;
  }
  export class CanCreateAnswers {
    static readonly methodName = "CanCreateAnswers";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAnswersRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAnswersReply;
  }
  export class CanCreateAnswersWithRecordTypes {
    static readonly methodName = "CanCreateAnswersWithRecordTypes";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAnswersWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAnswersWithRecordTypesReply;
  }
  export class GetAnswerFormForCreate {
    static readonly methodName = "GetAnswerFormForCreate";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAnswerFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAnswerFormForCreateReply;
  }
  export class CreateAnswer {
    static readonly methodName = "CreateAnswer";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateAnswerRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateAnswerReply;
  }
  export class CanUpdateAnswers {
    static readonly methodName = "CanUpdateAnswers";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateAnswersRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateAnswersReply;
  }
  export class GetAnswerFormForUpdate {
    static readonly methodName = "GetAnswerFormForUpdate";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAnswerFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAnswerFormForUpdateReply;
  }
  export class UpdateAnswer {
    static readonly methodName = "UpdateAnswer";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateAnswerRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateAnswerReply;
  }
  export class CanDeleteAnswers {
    static readonly methodName = "CanDeleteAnswers";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteAnswersRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteAnswersReply;
  }
  export class DeleteAnswer {
    static readonly methodName = "DeleteAnswer";
    static readonly service = ItemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteAnswerRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteAnswerReply;
  }
}
export class ItemNotificationSession {
  static serviceName = "dlkit.proto.assessment.ItemNotificationSession";
}
export namespace ItemNotificationSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanRegisterForItemNotifications {
    static readonly methodName = "CanRegisterForItemNotifications";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanRegisterForItemNotificationsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanRegisterForItemNotificationsReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class ReliableItemNotifications {
    static readonly methodName = "ReliableItemNotifications";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.ReliableItemNotificationsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.ReliableItemNotificationsReply;
  }
  export class UnreliableItemNotifications {
    static readonly methodName = "UnreliableItemNotifications";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UnreliableItemNotificationsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UnreliableItemNotificationsReply;
  }
  export class AcknowledgeItemNotification {
    static readonly methodName = "AcknowledgeItemNotification";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AcknowledgeItemNotificationRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AcknowledgeItemNotificationReply;
  }
  export class RegisterForNewItems {
    static readonly methodName = "RegisterForNewItems";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RegisterForNewItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RegisterForNewItemsReply;
  }
  export class RegisterForChangedItems {
    static readonly methodName = "RegisterForChangedItems";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RegisterForChangedItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RegisterForChangedItemsReply;
  }
  export class RegisterForChangedItem {
    static readonly methodName = "RegisterForChangedItem";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RegisterForChangedItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RegisterForChangedItemReply;
  }
  export class RegisterForDeletedItems {
    static readonly methodName = "RegisterForDeletedItems";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RegisterForDeletedItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RegisterForDeletedItemsReply;
  }
  export class RegisterForDeletedItem {
    static readonly methodName = "RegisterForDeletedItem";
    static readonly service = ItemNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RegisterForDeletedItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RegisterForDeletedItemReply;
  }
}
export class ItemBankSession {
  static serviceName = "dlkit.proto.assessment.ItemBankSession";
}
export namespace ItemBankSession {
  export class CanLookupItemBankMappings {
    static readonly methodName = "CanLookupItemBankMappings";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupItemBankMappingsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupItemBankMappingsReply;
  }
  export class UseComparativeBankView {
    static readonly methodName = "UseComparativeBankView";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeBankViewReply;
  }
  export class UsePlenaryBankView {
    static readonly methodName = "UsePlenaryBankView";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryBankViewReply;
  }
  export class GetItemIdsByBank {
    static readonly methodName = "GetItemIdsByBank";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemIdsByBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetItemsByBank {
    static readonly methodName = "GetItemsByBank";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetItemIdsByBanks {
    static readonly methodName = "GetItemIdsByBanks";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemIdsByBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetItemsByBanks {
    static readonly methodName = "GetItemsByBanks";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsByBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetBankIdsByItem {
    static readonly methodName = "GetBankIdsByItem";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdsByItemRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBanksByItem {
    static readonly methodName = "GetBanksByItem";
    static readonly service = ItemBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class ItemBankAssignmentSession {
  static serviceName = "dlkit.proto.assessment.ItemBankAssignmentSession";
}
export namespace ItemBankAssignmentSession {
  export class CanAssignItems {
    static readonly methodName = "CanAssignItems";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignItemsReply;
  }
  export class CanAssignItemsToBank {
    static readonly methodName = "CanAssignItemsToBank";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignItemsToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignItemsToBankReply;
  }
  export class GetAssignableBankIds {
    static readonly methodName = "GetAssignableBankIds";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBankIdsForItem {
    static readonly methodName = "GetAssignableBankIdsForItem";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsForItemRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignItemToBank {
    static readonly methodName = "AssignItemToBank";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AssignItemToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssignItemToBankReply;
  }
  export class UnassignItemFromBank {
    static readonly methodName = "UnassignItemFromBank";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UnassignItemFromBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UnassignItemFromBankReply;
  }
  export class ReassignItemToBilling {
    static readonly methodName = "ReassignItemToBilling";
    static readonly service = ItemBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.ReassignItemToBillingRequest;
    static readonly responseType = dlkit_proto_assessment_pb.ReassignItemToBillingReply;
  }
}
export class AssessmentLookupSession {
  static serviceName = "dlkit.proto.assessment.AssessmentLookupSession";
}
export namespace AssessmentLookupSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanLookupAssessments {
    static readonly methodName = "CanLookupAssessments";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupAssessmentsReply;
  }
  export class UseComparativeAssessmentView {
    static readonly methodName = "UseComparativeAssessmentView";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeAssessmentViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeAssessmentViewReply;
  }
  export class UsePlenaryAssessmentView {
    static readonly methodName = "UsePlenaryAssessmentView";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryAssessmentViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryAssessmentViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessment {
    static readonly methodName = "GetAssessment";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentReply;
  }
  export class GetAssessmentsByIds {
    static readonly methodName = "GetAssessmentsByIds";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
  export class GetAssessmentsByGenusType {
    static readonly methodName = "GetAssessmentsByGenusType";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
  export class GetAssessmentsByParentGenusType {
    static readonly methodName = "GetAssessmentsByParentGenusType";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
  export class GetAssessmentsByRecordType {
    static readonly methodName = "GetAssessmentsByRecordType";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
  export class GetAssessments {
    static readonly methodName = "GetAssessments";
    static readonly service = AssessmentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
}
export class AssessmentQuerySession {
  static serviceName = "dlkit.proto.assessment.AssessmentQuerySession";
}
export namespace AssessmentQuerySession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanSearchAssessments {
    static readonly methodName = "CanSearchAssessments";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanSearchAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanSearchAssessmentsReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessmentQuery {
    static readonly methodName = "GetAssessmentQuery";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentQueryReply;
  }
  export class GetAssessmentsByQuery {
    static readonly methodName = "GetAssessmentsByQuery";
    static readonly service = AssessmentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
}
export class AssessmentAdminSession {
  static serviceName = "dlkit.proto.assessment.AssessmentAdminSession";
}
export namespace AssessmentAdminSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanCreateAssessments {
    static readonly methodName = "CanCreateAssessments";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAssessmentsReply;
  }
  export class CanCreateAssessmentWithRecordTypes {
    static readonly methodName = "CanCreateAssessmentWithRecordTypes";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAssessmentWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAssessmentWithRecordTypesReply;
  }
  export class GetAssessmentFormForCreate {
    static readonly methodName = "GetAssessmentFormForCreate";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentFormForCreateReply;
  }
  export class CreateAssessment {
    static readonly methodName = "CreateAssessment";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateAssessmentReply;
  }
  export class CanUpdateAssessments {
    static readonly methodName = "CanUpdateAssessments";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateAssessmentsReply;
  }
  export class GetAssessmentFormForUpdate {
    static readonly methodName = "GetAssessmentFormForUpdate";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentFormForUpdateReply;
  }
  export class UpdateAssessment {
    static readonly methodName = "UpdateAssessment";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateAssessmentReply;
  }
  export class CanDeleteAssessments {
    static readonly methodName = "CanDeleteAssessments";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteAssessmentsReply;
  }
  export class DeleteAssessment {
    static readonly methodName = "DeleteAssessment";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteAssessmentReply;
  }
  export class CanManageAssessmentAliases {
    static readonly methodName = "CanManageAssessmentAliases";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanManageAssessmentAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanManageAssessmentAliasesReply;
  }
  export class AliasAssessment {
    static readonly methodName = "AliasAssessment";
    static readonly service = AssessmentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AliasAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AliasAssessmentReply;
  }
}
export class AssessmentBankSession {
  static serviceName = "dlkit.proto.assessment.AssessmentBankSession";
}
export namespace AssessmentBankSession {
  export class CanLookupAssessmentBankMappings {
    static readonly methodName = "CanLookupAssessmentBankMappings";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupAssessmentBankMappingsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupAssessmentBankMappingsReply;
  }
  export class UseComparativeBankView {
    static readonly methodName = "UseComparativeBankView";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeBankViewReply;
  }
  export class UsePlenaryBankView {
    static readonly methodName = "UsePlenaryBankView";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryBankViewReply;
  }
  export class GetAssessmentIdsByBank {
    static readonly methodName = "GetAssessmentIdsByBank";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentIdsByBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentsByBank {
    static readonly methodName = "GetAssessmentsByBank";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
  export class GetAssessmentIdsByBanks {
    static readonly methodName = "GetAssessmentIdsByBanks";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentIdsByBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentsByBanks {
    static readonly methodName = "GetAssessmentsByBanks";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsByBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Assessment;
  }
  export class GetBankIdsByAssessment {
    static readonly methodName = "GetBankIdsByAssessment";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdsByAssessmentRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBanksByAssessment {
    static readonly methodName = "GetBanksByAssessment";
    static readonly service = AssessmentBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class AssessmentBankAssignmentSession {
  static serviceName = "dlkit.proto.assessment.AssessmentBankAssignmentSession";
}
export namespace AssessmentBankAssignmentSession {
  export class CanAssignAssessments {
    static readonly methodName = "CanAssignAssessments";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignAssessmentsReply;
  }
  export class CanAssignAssessmentsToBank {
    static readonly methodName = "CanAssignAssessmentsToBank";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignAssessmentsToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignAssessmentsToBankReply;
  }
  export class GetAssignableBankIds {
    static readonly methodName = "GetAssignableBankIds";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBankIdsForAssessment {
    static readonly methodName = "GetAssignableBankIdsForAssessment";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsForAssessmentRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignAssessmentToBank {
    static readonly methodName = "AssignAssessmentToBank";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AssignAssessmentToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssignAssessmentToBankReply;
  }
  export class UnassignAssessmentFromBank {
    static readonly methodName = "UnassignAssessmentFromBank";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UnassignAssessmentFromBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UnassignAssessmentFromBankReply;
  }
  export class ReassignAssessmentToBilling {
    static readonly methodName = "ReassignAssessmentToBilling";
    static readonly service = AssessmentBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.ReassignAssessmentToBillingRequest;
    static readonly responseType = dlkit_proto_assessment_pb.ReassignAssessmentToBillingReply;
  }
}
export class AssessmentBasicAuthoringSession {
  static serviceName = "dlkit.proto.assessment.AssessmentBasicAuthoringSession";
}
export namespace AssessmentBasicAuthoringSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanAuthorAssessments {
    static readonly methodName = "CanAuthorAssessments";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAuthorAssessmentsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAuthorAssessmentsReply;
  }
  export class GetItems {
    static readonly methodName = "GetItems";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class AddItem {
    static readonly methodName = "AddItem";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AddItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AddItemReply;
  }
  export class RemoveItem {
    static readonly methodName = "RemoveItem";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RemoveItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RemoveItemReply;
  }
  export class MoveItem {
    static readonly methodName = "MoveItem";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.MoveItemRequest;
    static readonly responseType = dlkit_proto_assessment_pb.MoveItemReply;
  }
  export class OrderItems {
    static readonly methodName = "OrderItems";
    static readonly service = AssessmentBasicAuthoringSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.OrderItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.OrderItemsReply;
  }
}
export class AssessmentOfferedLookupSession {
  static serviceName = "dlkit.proto.assessment.AssessmentOfferedLookupSession";
}
export namespace AssessmentOfferedLookupSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanLookupAssessmentsOffered {
    static readonly methodName = "CanLookupAssessmentsOffered";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupAssessmentsOfferedReply;
  }
  export class UseComparativeAssessmentOfferedView {
    static readonly methodName = "UseComparativeAssessmentOfferedView";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeAssessmentOfferedViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeAssessmentOfferedViewReply;
  }
  export class UsePlenaryAssessmentOfferedView {
    static readonly methodName = "UsePlenaryAssessmentOfferedView";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryAssessmentOfferedViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryAssessmentOfferedViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessmentOffered {
    static readonly methodName = "GetAssessmentOffered";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentOfferedReply;
  }
  export class GetAssessmentsOfferedByIds {
    static readonly methodName = "GetAssessmentsOfferedByIds";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentsOfferedByGenusType {
    static readonly methodName = "GetAssessmentsOfferedByGenusType";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentsOfferedByParentGenusType {
    static readonly methodName = "GetAssessmentsOfferedByParentGenusType";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentsOfferedByRecordType {
    static readonly methodName = "GetAssessmentsOfferedByRecordType";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentsOfferedByDate {
    static readonly methodName = "GetAssessmentsOfferedByDate";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByDateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentsOfferedForAssessment {
    static readonly methodName = "GetAssessmentsOfferedForAssessment";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentsOffered {
    static readonly methodName = "GetAssessmentsOffered";
    static readonly service = AssessmentOfferedLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
}
export class AssessmentOfferedQuerySession {
  static serviceName = "dlkit.proto.assessment.AssessmentOfferedQuerySession";
}
export namespace AssessmentOfferedQuerySession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanSearchAssessmentsOffered {
    static readonly methodName = "CanSearchAssessmentsOffered";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanSearchAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanSearchAssessmentsOfferedReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessmentOfferedQuery {
    static readonly methodName = "GetAssessmentOfferedQuery";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentOfferedQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentOfferedQueryReply;
  }
  export class GetAssessmentsOfferedByQuery {
    static readonly methodName = "GetAssessmentsOfferedByQuery";
    static readonly service = AssessmentOfferedQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
}
export class AssessmentOfferedAdminSession {
  static serviceName = "dlkit.proto.assessment.AssessmentOfferedAdminSession";
}
export namespace AssessmentOfferedAdminSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanCreateAssessmentsOffered {
    static readonly methodName = "CanCreateAssessmentsOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAssessmentsOfferedReply;
  }
  export class CanCreateAssessmentOfferedWithRecordTypes {
    static readonly methodName = "CanCreateAssessmentOfferedWithRecordTypes";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAssessmentOfferedWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAssessmentOfferedWithRecordTypesReply;
  }
  export class GetAssessmentOfferedFormForCreate {
    static readonly methodName = "GetAssessmentOfferedFormForCreate";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentOfferedFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentOfferedFormForCreateReply;
  }
  export class CreateAssessmentOffered {
    static readonly methodName = "CreateAssessmentOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateAssessmentOfferedReply;
  }
  export class CanUpdateAssessmentsOffered {
    static readonly methodName = "CanUpdateAssessmentsOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateAssessmentsOfferedReply;
  }
  export class GetAssessmentOfferedFormForUpdate {
    static readonly methodName = "GetAssessmentOfferedFormForUpdate";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentOfferedFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentOfferedFormForUpdateReply;
  }
  export class UpdateAssessmentOffered {
    static readonly methodName = "UpdateAssessmentOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateAssessmentOfferedReply;
  }
  export class CanDeleteAssessmentsOffered {
    static readonly methodName = "CanDeleteAssessmentsOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteAssessmentsOfferedReply;
  }
  export class DeleteAssessmentOffered {
    static readonly methodName = "DeleteAssessmentOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteAssessmentOfferedReply;
  }
  export class CanManageAssessmentOfferedAliases {
    static readonly methodName = "CanManageAssessmentOfferedAliases";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanManageAssessmentOfferedAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanManageAssessmentOfferedAliasesReply;
  }
  export class AliasAssessmentOffered {
    static readonly methodName = "AliasAssessmentOffered";
    static readonly service = AssessmentOfferedAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AliasAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AliasAssessmentOfferedReply;
  }
}
export class AssessmentOfferedBankSession {
  static serviceName = "dlkit.proto.assessment.AssessmentOfferedBankSession";
}
export namespace AssessmentOfferedBankSession {
  export class CanLookupAssessmentOfferedBankMappings {
    static readonly methodName = "CanLookupAssessmentOfferedBankMappings";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupAssessmentOfferedBankMappingsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupAssessmentOfferedBankMappingsReply;
  }
  export class UseComparativeBankView {
    static readonly methodName = "UseComparativeBankView";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeBankViewReply;
  }
  export class UsePlenaryBankView {
    static readonly methodName = "UsePlenaryBankView";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryBankViewReply;
  }
  export class GetAssessmentOfferedIdsByBank {
    static readonly methodName = "GetAssessmentOfferedIdsByBank";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentOfferedIdsByBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentsOfferedByBank {
    static readonly methodName = "GetAssessmentsOfferedByBank";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetAssessmentOfferedIdsByBanks {
    static readonly methodName = "GetAssessmentOfferedIdsByBanks";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentOfferedIdsByBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentsOfferedByBanks {
    static readonly methodName = "GetAssessmentsOfferedByBanks";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsOfferedByBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentOffered;
  }
  export class GetBankIdsByAssessmentOffered {
    static readonly methodName = "GetBankIdsByAssessmentOffered";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdsByAssessmentOfferedRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBanksByAssessmentOffered {
    static readonly methodName = "GetBanksByAssessmentOffered";
    static readonly service = AssessmentOfferedBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class AssessmentOfferedBankAssignmentSession {
  static serviceName = "dlkit.proto.assessment.AssessmentOfferedBankAssignmentSession";
}
export namespace AssessmentOfferedBankAssignmentSession {
  export class CanAssignAssessmentsOffered {
    static readonly methodName = "CanAssignAssessmentsOffered";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedReply;
  }
  export class CanAssignAssessmentsOfferedToBank {
    static readonly methodName = "CanAssignAssessmentsOfferedToBank";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedToBankReply;
  }
  export class GetAssignableBankIds {
    static readonly methodName = "GetAssignableBankIds";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBankIdsForAssessmentOffered {
    static readonly methodName = "GetAssignableBankIdsForAssessmentOffered";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsForAssessmentOfferedRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignAssessmentOfferedToBank {
    static readonly methodName = "AssignAssessmentOfferedToBank";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AssignAssessmentOfferedToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssignAssessmentOfferedToBankReply;
  }
  export class UnassignAssessmentOfferedFromBank {
    static readonly methodName = "UnassignAssessmentOfferedFromBank";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UnassignAssessmentOfferedFromBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UnassignAssessmentOfferedFromBankReply;
  }
  export class ReassignAssessmentOfferedToBilling {
    static readonly methodName = "ReassignAssessmentOfferedToBilling";
    static readonly service = AssessmentOfferedBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.ReassignAssessmentOfferedToBillingRequest;
    static readonly responseType = dlkit_proto_assessment_pb.ReassignAssessmentOfferedToBillingReply;
  }
}
export class AssessmentTakenLookupSession {
  static serviceName = "dlkit.proto.assessment.AssessmentTakenLookupSession";
}
export namespace AssessmentTakenLookupSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanLookupAssessmentsTaken {
    static readonly methodName = "CanLookupAssessmentsTaken";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupAssessmentsTakenReply;
  }
  export class UseComparativeAssessmentTakenView {
    static readonly methodName = "UseComparativeAssessmentTakenView";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeAssessmentTakenViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeAssessmentTakenViewReply;
  }
  export class UsePlenaryAssessmentTakenView {
    static readonly methodName = "UsePlenaryAssessmentTakenView";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryAssessmentTakenViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryAssessmentTakenViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessmentTaken {
    static readonly methodName = "GetAssessmentTaken";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentTakenReply;
  }
  export class GetAssessmentsTakenByIds {
    static readonly methodName = "GetAssessmentsTakenByIds";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByGenusType {
    static readonly methodName = "GetAssessmentsTakenByGenusType";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByParentGenusType {
    static readonly methodName = "GetAssessmentsTakenByParentGenusType";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByRecordType {
    static readonly methodName = "GetAssessmentsTakenByRecordType";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByDate {
    static readonly methodName = "GetAssessmentsTakenByDate";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByDateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenForTaker {
    static readonly methodName = "GetAssessmentsTakenForTaker";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenForTakerRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByDateForTaker {
    static readonly methodName = "GetAssessmentsTakenByDateForTaker";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForTakerRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenForAssessment {
    static readonly methodName = "GetAssessmentsTakenForAssessment";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByDateForAssessment {
    static readonly methodName = "GetAssessmentsTakenByDateForAssessment";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenForTakerAndAssessment {
    static readonly methodName = "GetAssessmentsTakenForTakerAndAssessment";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenForTakerAndAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByDateForTakerAndAssessment {
    static readonly methodName = "GetAssessmentsTakenByDateForTakerAndAssessment";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForTakerAndAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenForAssessmentOffered {
    static readonly methodName = "GetAssessmentsTakenForAssessmentOffered";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenForAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByDateForAssessmentOffered {
    static readonly methodName = "GetAssessmentsTakenByDateForAssessmentOffered";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenForTakerAndAssessmentOffered {
    static readonly methodName = "GetAssessmentsTakenForTakerAndAssessmentOffered";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenForTakerAndAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTakenByDateForTakerAndAssessmentOffered {
    static readonly methodName = "GetAssessmentsTakenByDateForTakerAndAssessmentOffered";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentsTaken {
    static readonly methodName = "GetAssessmentsTaken";
    static readonly service = AssessmentTakenLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
}
export class AssessmentTakenQuerySession {
  static serviceName = "dlkit.proto.assessment.AssessmentTakenQuerySession";
}
export namespace AssessmentTakenQuerySession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanSearchAssessmentsTaken {
    static readonly methodName = "CanSearchAssessmentsTaken";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanSearchAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanSearchAssessmentsTakenReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessmentTakenQuery {
    static readonly methodName = "GetAssessmentTakenQuery";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentTakenQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentTakenQueryReply;
  }
  export class GetAssessmentsTakenByQuery {
    static readonly methodName = "GetAssessmentsTakenByQuery";
    static readonly service = AssessmentTakenQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
}
export class AssessmentTakenAdminSession {
  static serviceName = "dlkit.proto.assessment.AssessmentTakenAdminSession";
}
export namespace AssessmentTakenAdminSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class CanCreateAssessmentsTaken {
    static readonly methodName = "CanCreateAssessmentsTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAssessmentsTakenReply;
  }
  export class CanCreateAssessmentTakenWithRecordTypes {
    static readonly methodName = "CanCreateAssessmentTakenWithRecordTypes";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateAssessmentTakenWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateAssessmentTakenWithRecordTypesReply;
  }
  export class GetAssessmentTakenFormForCreate {
    static readonly methodName = "GetAssessmentTakenFormForCreate";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentTakenFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentTakenFormForCreateReply;
  }
  export class CreateAssessmentTaken {
    static readonly methodName = "CreateAssessmentTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateAssessmentTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateAssessmentTakenReply;
  }
  export class CanUpdateAssessmentsTaken {
    static readonly methodName = "CanUpdateAssessmentsTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateAssessmentsTakenReply;
  }
  export class GetAssessmentTakenFormForUpdate {
    static readonly methodName = "GetAssessmentTakenFormForUpdate";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentTakenFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetAssessmentTakenFormForUpdateReply;
  }
  export class UpdateAssessmentTaken {
    static readonly methodName = "UpdateAssessmentTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateAssessmentTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateAssessmentTakenReply;
  }
  export class CanDeleteAssessmentsTaken {
    static readonly methodName = "CanDeleteAssessmentsTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteAssessmentsTakenReply;
  }
  export class DeleteAssessmentTaken {
    static readonly methodName = "DeleteAssessmentTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteAssessmentTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteAssessmentTakenReply;
  }
  export class CanManageAssessmentTakenAliases {
    static readonly methodName = "CanManageAssessmentTakenAliases";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanManageAssessmentTakenAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanManageAssessmentTakenAliasesReply;
  }
  export class AliasAssessmentTaken {
    static readonly methodName = "AliasAssessmentTaken";
    static readonly service = AssessmentTakenAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AliasAssessmentTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AliasAssessmentTakenReply;
  }
}
export class AssessmentTakenBankSession {
  static serviceName = "dlkit.proto.assessment.AssessmentTakenBankSession";
}
export namespace AssessmentTakenBankSession {
  export class CanLookupAssessmentTakenBankMappings {
    static readonly methodName = "CanLookupAssessmentTakenBankMappings";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupAssessmentTakenBankMappingsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupAssessmentTakenBankMappingsReply;
  }
  export class UseComparativeBankView {
    static readonly methodName = "UseComparativeBankView";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeBankViewReply;
  }
  export class UsePlenaryBankView {
    static readonly methodName = "UsePlenaryBankView";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryBankViewReply;
  }
  export class GetAssessmentTakenIdsByBank {
    static readonly methodName = "GetAssessmentTakenIdsByBank";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentTakenIdsByBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentsTakenByBank {
    static readonly methodName = "GetAssessmentsTakenByBank";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetAssessmentTakenIdsByBanks {
    static readonly methodName = "GetAssessmentTakenIdsByBanks";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentTakenIdsByBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentsTakenByBanks {
    static readonly methodName = "GetAssessmentsTakenByBanks";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssessmentsTakenByBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssessmentTaken;
  }
  export class GetBankIdsByAssessmentTaken {
    static readonly methodName = "GetBankIdsByAssessmentTaken";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankIdsByAssessmentTakenRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBanksByAssessmentTaken {
    static readonly methodName = "GetBanksByAssessmentTaken";
    static readonly service = AssessmentTakenBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByAssessmentTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class AssessmentTakenBankAssignmentSession {
  static serviceName = "dlkit.proto.assessment.AssessmentTakenBankAssignmentSession";
}
export namespace AssessmentTakenBankAssignmentSession {
  export class CanAssignAssessmentsTaken {
    static readonly methodName = "CanAssignAssessmentsTaken";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignAssessmentsTakenRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignAssessmentsTakenReply;
  }
  export class CanAssignAssessmentsTakenToBank {
    static readonly methodName = "CanAssignAssessmentsTakenToBank";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAssignAssessmentsTakenToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAssignAssessmentsTakenToBankReply;
  }
  export class GetAssignableBankIds {
    static readonly methodName = "GetAssignableBankIds";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBankIdsForAssessmentTaken {
    static readonly methodName = "GetAssignableBankIdsForAssessmentTaken";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetAssignableBankIdsForAssessmentTakenRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignAssessmentTakenToBank {
    static readonly methodName = "AssignAssessmentTakenToBank";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AssignAssessmentTakenToBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AssignAssessmentTakenToBankReply;
  }
  export class UnassignAssessmentTakenFromBank {
    static readonly methodName = "UnassignAssessmentTakenFromBank";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UnassignAssessmentTakenFromBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UnassignAssessmentTakenFromBankReply;
  }
  export class ReassignAssessmentTakenToBilling {
    static readonly methodName = "ReassignAssessmentTakenToBilling";
    static readonly service = AssessmentTakenBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.ReassignAssessmentTakenToBillingRequest;
    static readonly responseType = dlkit_proto_assessment_pb.ReassignAssessmentTakenToBillingReply;
  }
}
export class BankLookupSession {
  static serviceName = "dlkit.proto.assessment.BankLookupSession";
}
export namespace BankLookupSession {
  export class CanLookupBanks {
    static readonly methodName = "CanLookupBanks";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanLookupBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanLookupBanksReply;
  }
  export class UseComparativeBankView {
    static readonly methodName = "UseComparativeBankView";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeBankViewReply;
  }
  export class UsePlenaryBankView {
    static readonly methodName = "UsePlenaryBankView";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryBankViewReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankReply;
  }
  export class GetBanksByIds {
    static readonly methodName = "GetBanksByIds";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class GetBanksByGenusType {
    static readonly methodName = "GetBanksByGenusType";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class GetBanksByParentGenusType {
    static readonly methodName = "GetBanksByParentGenusType";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class GetBanksByRecordType {
    static readonly methodName = "GetBanksByRecordType";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class GetBanksByProvider {
    static readonly methodName = "GetBanksByProvider";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByProviderRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class GetBanks {
    static readonly methodName = "GetBanks";
    static readonly service = BankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class BankQuerySession {
  static serviceName = "dlkit.proto.assessment.BankQuerySession";
}
export namespace BankQuerySession {
  export class CanSearchBanks {
    static readonly methodName = "CanSearchBanks";
    static readonly service = BankQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanSearchBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanSearchBanksReply;
  }
  export class GetBankQuery {
    static readonly methodName = "GetBankQuery";
    static readonly service = BankQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankQueryReply;
  }
  export class GetBanksByQuery {
    static readonly methodName = "GetBanksByQuery";
    static readonly service = BankQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetBanksByQueryRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class BankAdminSession {
  static serviceName = "dlkit.proto.assessment.BankAdminSession";
}
export namespace BankAdminSession {
  export class CanCreateBanks {
    static readonly methodName = "CanCreateBanks";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateBanksReply;
  }
  export class CanCreateBankWithRecordTypes {
    static readonly methodName = "CanCreateBankWithRecordTypes";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanCreateBankWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanCreateBankWithRecordTypesReply;
  }
  export class GetBankFormForCreate {
    static readonly methodName = "GetBankFormForCreate";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankFormForCreateReply;
  }
  export class CreateBank {
    static readonly methodName = "CreateBank";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CreateBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CreateBankReply;
  }
  export class CanUpdateBanks {
    static readonly methodName = "CanUpdateBanks";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanUpdateBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanUpdateBanksReply;
  }
  export class GetBankFormForUpdate {
    static readonly methodName = "GetBankFormForUpdate";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankFormForUpdateReply;
  }
  export class UpdateBank {
    static readonly methodName = "UpdateBank";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UpdateBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UpdateBankReply;
  }
  export class CanDeleteBanks {
    static readonly methodName = "CanDeleteBanks";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanDeleteBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanDeleteBanksReply;
  }
  export class DeleteBank {
    static readonly methodName = "DeleteBank";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.DeleteBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.DeleteBankReply;
  }
  export class CanManageBankAliases {
    static readonly methodName = "CanManageBankAliases";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanManageBankAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanManageBankAliasesReply;
  }
  export class AliasBank {
    static readonly methodName = "AliasBank";
    static readonly service = BankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AliasBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AliasBankReply;
  }
}
export class BankHierarchySession {
  static serviceName = "dlkit.proto.assessment.BankHierarchySession";
}
export namespace BankHierarchySession {
  export class GetBankHierarchyId {
    static readonly methodName = "GetBankHierarchyId";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankHierarchyIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankHierarchyIdReply;
  }
  export class GetBankHierarchy {
    static readonly methodName = "GetBankHierarchy";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankHierarchyRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankHierarchyReply;
  }
  export class CanAccessBankHierarchy {
    static readonly methodName = "CanAccessBankHierarchy";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanAccessBankHierarchyRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanAccessBankHierarchyReply;
  }
  export class UseComparativeBankView {
    static readonly methodName = "UseComparativeBankView";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UseComparativeBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UseComparativeBankViewReply;
  }
  export class UsePlenaryBankView {
    static readonly methodName = "UsePlenaryBankView";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.UsePlenaryBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_pb.UsePlenaryBankViewReply;
  }
  export class GetRootBankIds {
    static readonly methodName = "GetRootBankIds";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetRootBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootBanks {
    static readonly methodName = "GetRootBanks";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetRootBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class HasParentBanks {
    static readonly methodName = "HasParentBanks";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasParentBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasParentBanksReply;
  }
  export class IsParentOfBank {
    static readonly methodName = "IsParentOfBank";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsParentOfBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsParentOfBankReply;
  }
  export class GetParentBankIds {
    static readonly methodName = "GetParentBankIds";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetParentBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentBanks {
    static readonly methodName = "GetParentBanks";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetParentBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class IsAncestorOfBank {
    static readonly methodName = "IsAncestorOfBank";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsAncestorOfBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsAncestorOfBankReply;
  }
  export class HasChildBanks {
    static readonly methodName = "HasChildBanks";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.HasChildBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.HasChildBanksReply;
  }
  export class IsChildOfBank {
    static readonly methodName = "IsChildOfBank";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsChildOfBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsChildOfBankReply;
  }
  export class GetChildBankIds {
    static readonly methodName = "GetChildBankIds";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetChildBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildBanks {
    static readonly methodName = "GetChildBanks";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_pb.GetChildBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
  export class IsDescendantOfBank {
    static readonly methodName = "IsDescendantOfBank";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.IsDescendantOfBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.IsDescendantOfBankReply;
  }
  export class GetBankNodeIds {
    static readonly methodName = "GetBankNodeIds";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankNodeIdsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankNodeIdsReply;
  }
  export class GetBankNodes {
    static readonly methodName = "GetBankNodes";
    static readonly service = BankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankNodesRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankNodesReply;
  }
}
export class BankHierarchyDesignSession {
  static serviceName = "dlkit.proto.assessment.BankHierarchyDesignSession";
}
export namespace BankHierarchyDesignSession {
  export class GetBankHierarchyId {
    static readonly methodName = "GetBankHierarchyId";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankHierarchyIdRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankHierarchyIdReply;
  }
  export class GetBankHierarchy {
    static readonly methodName = "GetBankHierarchy";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.GetBankHierarchyRequest;
    static readonly responseType = dlkit_proto_assessment_pb.GetBankHierarchyReply;
  }
  export class CanModifyBankHierarchy {
    static readonly methodName = "CanModifyBankHierarchy";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.CanModifyBankHierarchyRequest;
    static readonly responseType = dlkit_proto_assessment_pb.CanModifyBankHierarchyReply;
  }
  export class AddRootBank {
    static readonly methodName = "AddRootBank";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AddRootBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AddRootBankReply;
  }
  export class RemoveRootBank {
    static readonly methodName = "RemoveRootBank";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RemoveRootBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RemoveRootBankReply;
  }
  export class AddChildBank {
    static readonly methodName = "AddChildBank";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.AddChildBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.AddChildBankReply;
  }
  export class RemoveChildBank {
    static readonly methodName = "RemoveChildBank";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RemoveChildBankRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RemoveChildBankReply;
  }
  export class RemoveChildBanks {
    static readonly methodName = "RemoveChildBanks";
    static readonly service = BankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_pb.RemoveChildBanksRequest;
    static readonly responseType = dlkit_proto_assessment_pb.RemoveChildBanksReply;
  }
}
