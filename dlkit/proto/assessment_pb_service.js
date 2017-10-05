// package: dlkit.proto.assessment
// file: dlkit/proto/assessment.proto

var jspb = require("google-protobuf");
var dlkit_proto_assessment_pb = require("../../dlkit/proto/assessment_pb");
var dlkit_primordium_calendaring_primitives_pb = require("../../dlkit/primordium/calendaring/primitives_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_grading_pb = require("../../dlkit/proto/grading_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var AssessmentSession = {
  serviceName: "dlkit.proto.assessment.AssessmentSession"
};
AssessmentSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentSession.CanTakeAssessments = {
  methodName: "CanTakeAssessments",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanTakeAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanTakeAssessmentsReply
};
AssessmentSession.HasAssessmentBegun = {
  methodName: "HasAssessmentBegun",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasAssessmentBegunRequest,
  responseType: dlkit_proto_assessment_pb.HasAssessmentBegunReply
};
AssessmentSession.IsAssessmentOver = {
  methodName: "IsAssessmentOver",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsAssessmentOverRequest,
  responseType: dlkit_proto_assessment_pb.IsAssessmentOverReply
};
AssessmentSession.RequiresSynchronousSections = {
  methodName: "RequiresSynchronousSections",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RequiresSynchronousSectionsRequest,
  responseType: dlkit_proto_assessment_pb.RequiresSynchronousSectionsReply
};
AssessmentSession.GetFirstAssessmentSection = {
  methodName: "GetFirstAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetFirstAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.GetFirstAssessmentSectionReply
};
AssessmentSession.HasNextAssessmentSection = {
  methodName: "HasNextAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasNextAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.HasNextAssessmentSectionReply
};
AssessmentSession.GetNextAssessmentSection = {
  methodName: "GetNextAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetNextAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.GetNextAssessmentSectionReply
};
AssessmentSession.HasPreviousAssessmentSection = {
  methodName: "HasPreviousAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasPreviousAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.HasPreviousAssessmentSectionReply
};
AssessmentSession.GetPreviousAssessmentSection = {
  methodName: "GetPreviousAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetPreviousAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.GetPreviousAssessmentSectionReply
};
AssessmentSession.GetAssessmentSection = {
  methodName: "GetAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentSectionReply
};
AssessmentSession.GetAssessmentSections = {
  methodName: "GetAssessmentSections",
  service: AssessmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentSectionsRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentSection
};
AssessmentSession.IsAssessmentSectionComplete = {
  methodName: "IsAssessmentSectionComplete",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsAssessmentSectionCompleteRequest,
  responseType: dlkit_proto_assessment_pb.IsAssessmentSectionCompleteReply
};
AssessmentSession.GetIncompleteAssessmentSections = {
  methodName: "GetIncompleteAssessmentSections",
  service: AssessmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetIncompleteAssessmentSectionsRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentSection
};
AssessmentSession.HasAssessmentSectionBegun = {
  methodName: "HasAssessmentSectionBegun",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasAssessmentSectionBegunRequest,
  responseType: dlkit_proto_assessment_pb.HasAssessmentSectionBegunReply
};
AssessmentSession.IsAssessmentSectionOver = {
  methodName: "IsAssessmentSectionOver",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsAssessmentSectionOverRequest,
  responseType: dlkit_proto_assessment_pb.IsAssessmentSectionOverReply
};
AssessmentSession.RequiresSynchronousResponses = {
  methodName: "RequiresSynchronousResponses",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RequiresSynchronousResponsesRequest,
  responseType: dlkit_proto_assessment_pb.RequiresSynchronousResponsesReply
};
AssessmentSession.GetFirstQuestion = {
  methodName: "GetFirstQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetFirstQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetFirstQuestionReply
};
AssessmentSession.HasNextQuestion = {
  methodName: "HasNextQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasNextQuestionRequest,
  responseType: dlkit_proto_assessment_pb.HasNextQuestionReply
};
AssessmentSession.GetNextQuestion = {
  methodName: "GetNextQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetNextQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetNextQuestionReply
};
AssessmentSession.HasPreviousQuestion = {
  methodName: "HasPreviousQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasPreviousQuestionRequest,
  responseType: dlkit_proto_assessment_pb.HasPreviousQuestionReply
};
AssessmentSession.GetPreviousQuestion = {
  methodName: "GetPreviousQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetPreviousQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetPreviousQuestionReply
};
AssessmentSession.GetQuestion = {
  methodName: "GetQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetQuestionReply
};
AssessmentSession.GetQuestions = {
  methodName: "GetQuestions",
  service: AssessmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetQuestionsRequest,
  responseType: dlkit_proto_assessment_pb.Question
};
AssessmentSession.GetResponseForm = {
  methodName: "GetResponseForm",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetResponseFormRequest,
  responseType: dlkit_proto_assessment_pb.GetResponseFormReply
};
AssessmentSession.SubmitResponse = {
  methodName: "SubmitResponse",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.SubmitResponseRequest,
  responseType: dlkit_proto_assessment_pb.SubmitResponseReply
};
AssessmentSession.SkipItem = {
  methodName: "SkipItem",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.SkipItemRequest,
  responseType: dlkit_proto_assessment_pb.SkipItemReply
};
AssessmentSession.IsQuestionAnswered = {
  methodName: "IsQuestionAnswered",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsQuestionAnsweredRequest,
  responseType: dlkit_proto_assessment_pb.IsQuestionAnsweredReply
};
AssessmentSession.GetUnansweredQuestions = {
  methodName: "GetUnansweredQuestions",
  service: AssessmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetUnansweredQuestionsRequest,
  responseType: dlkit_proto_assessment_pb.Question
};
AssessmentSession.HasUnansweredQuestions = {
  methodName: "HasUnansweredQuestions",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasUnansweredQuestionsRequest,
  responseType: dlkit_proto_assessment_pb.HasUnansweredQuestionsReply
};
AssessmentSession.GetFirstUnansweredQuestion = {
  methodName: "GetFirstUnansweredQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetFirstUnansweredQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetFirstUnansweredQuestionReply
};
AssessmentSession.HasNextUnansweredQuestion = {
  methodName: "HasNextUnansweredQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasNextUnansweredQuestionRequest,
  responseType: dlkit_proto_assessment_pb.HasNextUnansweredQuestionReply
};
AssessmentSession.GetNextUnansweredQuestion = {
  methodName: "GetNextUnansweredQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetNextUnansweredQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetNextUnansweredQuestionReply
};
AssessmentSession.HasPreviousUnansweredQuestion = {
  methodName: "HasPreviousUnansweredQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasPreviousUnansweredQuestionRequest,
  responseType: dlkit_proto_assessment_pb.HasPreviousUnansweredQuestionReply
};
AssessmentSession.GetPreviousUnansweredQuestion = {
  methodName: "GetPreviousUnansweredQuestion",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetPreviousUnansweredQuestionRequest,
  responseType: dlkit_proto_assessment_pb.GetPreviousUnansweredQuestionReply
};
AssessmentSession.GetResponse = {
  methodName: "GetResponse",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetResponseRequest,
  responseType: dlkit_proto_assessment_pb.GetResponseReply
};
AssessmentSession.GetResponses = {
  methodName: "GetResponses",
  service: AssessmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetResponsesRequest,
  responseType: dlkit_proto_assessment_pb.Response
};
AssessmentSession.ClearResponse = {
  methodName: "ClearResponse",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.ClearResponseRequest,
  responseType: dlkit_proto_assessment_pb.ClearResponseReply
};
AssessmentSession.FinishAssessmentSection = {
  methodName: "FinishAssessmentSection",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.FinishAssessmentSectionRequest,
  responseType: dlkit_proto_assessment_pb.FinishAssessmentSectionReply
};
AssessmentSession.IsAnswerAvailable = {
  methodName: "IsAnswerAvailable",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsAnswerAvailableRequest,
  responseType: dlkit_proto_assessment_pb.IsAnswerAvailableReply
};
AssessmentSession.GetAnswers = {
  methodName: "GetAnswers",
  service: AssessmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAnswersRequest,
  responseType: dlkit_proto_assessment_pb.Answer
};
AssessmentSession.FinishAssessment = {
  methodName: "FinishAssessment",
  service: AssessmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.FinishAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.FinishAssessmentReply
};
var AssessmentResultsSession = {
  serviceName: "dlkit.proto.assessment.AssessmentResultsSession"
};
AssessmentResultsSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentResultsSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentResultsSession.CanAccessAssessmentResults = {
  methodName: "CanAccessAssessmentResults",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAccessAssessmentResultsRequest,
  responseType: dlkit_proto_assessment_pb.CanAccessAssessmentResultsReply
};
AssessmentResultsSession.GetItems = {
  methodName: "GetItems",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
AssessmentResultsSession.GetResponses = {
  methodName: "GetResponses",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetResponsesRequest,
  responseType: dlkit_proto_assessment_pb.Response
};
AssessmentResultsSession.AreResultsAvailable = {
  methodName: "AreResultsAvailable",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AreResultsAvailableRequest,
  responseType: dlkit_proto_assessment_pb.AreResultsAvailableReply
};
AssessmentResultsSession.GetGradeEntries = {
  methodName: "GetGradeEntries",
  service: AssessmentResultsSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
var ItemLookupSession = {
  serviceName: "dlkit.proto.assessment.ItemLookupSession"
};
ItemLookupSession.GetBankId = {
  methodName: "GetBankId",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
ItemLookupSession.GetBank = {
  methodName: "GetBank",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
ItemLookupSession.CanLookupItems = {
  methodName: "CanLookupItems",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupItemsRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupItemsReply
};
ItemLookupSession.UseComparativeItemView = {
  methodName: "UseComparativeItemView",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeItemViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeItemViewReply
};
ItemLookupSession.UsePlenaryItemView = {
  methodName: "UsePlenaryItemView",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryItemViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryItemViewReply
};
ItemLookupSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
ItemLookupSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
ItemLookupSession.GetItem = {
  methodName: "GetItem",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemRequest,
  responseType: dlkit_proto_assessment_pb.GetItemReply
};
ItemLookupSession.GetItemsByIds = {
  methodName: "GetItemsByIds",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByIdsRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByGenusType = {
  methodName: "GetItemsByGenusType",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByParentGenusType = {
  methodName: "GetItemsByParentGenusType",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByRecordType = {
  methodName: "GetItemsByRecordType",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByRecordTypeRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByQuestion = {
  methodName: "GetItemsByQuestion",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByQuestionRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByAnswer = {
  methodName: "GetItemsByAnswer",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByAnswerRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByLearningObjective = {
  methodName: "GetItemsByLearningObjective",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByLearningObjectiveRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItemsByLearningObjectives = {
  methodName: "GetItemsByLearningObjectives",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByLearningObjectivesRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemLookupSession.GetItems = {
  methodName: "GetItems",
  service: ItemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
var ItemQuerySession = {
  serviceName: "dlkit.proto.assessment.ItemQuerySession"
};
ItemQuerySession.GetBankId = {
  methodName: "GetBankId",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
ItemQuerySession.GetBank = {
  methodName: "GetBank",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
ItemQuerySession.CanSearchItems = {
  methodName: "CanSearchItems",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanSearchItemsRequest,
  responseType: dlkit_proto_assessment_pb.CanSearchItemsReply
};
ItemQuerySession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
ItemQuerySession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
ItemQuerySession.GetItemQuery = {
  methodName: "GetItemQuery",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemQueryRequest,
  responseType: dlkit_proto_assessment_pb.GetItemQueryReply
};
ItemQuerySession.GetItemsByQuery = {
  methodName: "GetItemsByQuery",
  service: ItemQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByQueryRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
var ItemSearchSession = {
  serviceName: "dlkit.proto.assessment.ItemSearchSession"
};
ItemSearchSession.GetItemSearch = {
  methodName: "GetItemSearch",
  service: ItemSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemSearchRequest,
  responseType: dlkit_proto_assessment_pb.GetItemSearchReply
};
ItemSearchSession.GetItemSearchOrder = {
  methodName: "GetItemSearchOrder",
  service: ItemSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemSearchOrderRequest,
  responseType: dlkit_proto_assessment_pb.GetItemSearchOrderReply
};
ItemSearchSession.GetItemsBySearch = {
  methodName: "GetItemsBySearch",
  service: ItemSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemsBySearchRequest,
  responseType: dlkit_proto_assessment_pb.GetItemsBySearchReply
};
ItemSearchSession.GetItemQueryFromInspector = {
  methodName: "GetItemQueryFromInspector",
  service: ItemSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemQueryFromInspectorRequest,
  responseType: dlkit_proto_assessment_pb.GetItemQueryFromInspectorReply
};
var ItemAdminSession = {
  serviceName: "dlkit.proto.assessment.ItemAdminSession"
};
ItemAdminSession.GetBankId = {
  methodName: "GetBankId",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
ItemAdminSession.GetBank = {
  methodName: "GetBank",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
ItemAdminSession.CanCreateItems = {
  methodName: "CanCreateItems",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateItemsRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateItemsReply
};
ItemAdminSession.CanCreateItemWithRecordTypes = {
  methodName: "CanCreateItemWithRecordTypes",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateItemWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateItemWithRecordTypesReply
};
ItemAdminSession.GetItemFormForCreate = {
  methodName: "GetItemFormForCreate",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetItemFormForCreateReply
};
ItemAdminSession.CreateItem = {
  methodName: "CreateItem",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateItemRequest,
  responseType: dlkit_proto_assessment_pb.CreateItemReply
};
ItemAdminSession.CanUpdateItems = {
  methodName: "CanUpdateItems",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateItemsRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateItemsReply
};
ItemAdminSession.GetItemFormForUpdate = {
  methodName: "GetItemFormForUpdate",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetItemFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetItemFormForUpdateReply
};
ItemAdminSession.UpdateItem = {
  methodName: "UpdateItem",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateItemRequest,
  responseType: dlkit_proto_assessment_pb.UpdateItemReply
};
ItemAdminSession.CanDeleteItems = {
  methodName: "CanDeleteItems",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteItemsRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteItemsReply
};
ItemAdminSession.DeleteItem = {
  methodName: "DeleteItem",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteItemRequest,
  responseType: dlkit_proto_assessment_pb.DeleteItemReply
};
ItemAdminSession.CanManageItemAliases = {
  methodName: "CanManageItemAliases",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanManageItemAliasesRequest,
  responseType: dlkit_proto_assessment_pb.CanManageItemAliasesReply
};
ItemAdminSession.AliasItem = {
  methodName: "AliasItem",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AliasItemRequest,
  responseType: dlkit_proto_assessment_pb.AliasItemReply
};
ItemAdminSession.CanCreateQuestions = {
  methodName: "CanCreateQuestions",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateQuestionsRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateQuestionsReply
};
ItemAdminSession.CanCreateQuestionWithRecordTypes = {
  methodName: "CanCreateQuestionWithRecordTypes",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateQuestionWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateQuestionWithRecordTypesReply
};
ItemAdminSession.GetQuestionFormForCreate = {
  methodName: "GetQuestionFormForCreate",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetQuestionFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetQuestionFormForCreateReply
};
ItemAdminSession.CreateQuestion = {
  methodName: "CreateQuestion",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateQuestionRequest,
  responseType: dlkit_proto_assessment_pb.CreateQuestionReply
};
ItemAdminSession.CanUpdateQuestions = {
  methodName: "CanUpdateQuestions",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateQuestionsRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateQuestionsReply
};
ItemAdminSession.GetQuestionFormForUpdate = {
  methodName: "GetQuestionFormForUpdate",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetQuestionFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetQuestionFormForUpdateReply
};
ItemAdminSession.UpdateQuestion = {
  methodName: "UpdateQuestion",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateQuestionRequest,
  responseType: dlkit_proto_assessment_pb.UpdateQuestionReply
};
ItemAdminSession.CanDeleteQuestions = {
  methodName: "CanDeleteQuestions",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteQuestionsRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteQuestionsReply
};
ItemAdminSession.DeleteQuestion = {
  methodName: "DeleteQuestion",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteQuestionRequest,
  responseType: dlkit_proto_assessment_pb.DeleteQuestionReply
};
ItemAdminSession.CanCreateAnswers = {
  methodName: "CanCreateAnswers",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAnswersRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAnswersReply
};
ItemAdminSession.CanCreateAnswersWithRecordTypes = {
  methodName: "CanCreateAnswersWithRecordTypes",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAnswersWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAnswersWithRecordTypesReply
};
ItemAdminSession.GetAnswerFormForCreate = {
  methodName: "GetAnswerFormForCreate",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAnswerFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetAnswerFormForCreateReply
};
ItemAdminSession.CreateAnswer = {
  methodName: "CreateAnswer",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateAnswerRequest,
  responseType: dlkit_proto_assessment_pb.CreateAnswerReply
};
ItemAdminSession.CanUpdateAnswers = {
  methodName: "CanUpdateAnswers",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateAnswersRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateAnswersReply
};
ItemAdminSession.GetAnswerFormForUpdate = {
  methodName: "GetAnswerFormForUpdate",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAnswerFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetAnswerFormForUpdateReply
};
ItemAdminSession.UpdateAnswer = {
  methodName: "UpdateAnswer",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateAnswerRequest,
  responseType: dlkit_proto_assessment_pb.UpdateAnswerReply
};
ItemAdminSession.CanDeleteAnswers = {
  methodName: "CanDeleteAnswers",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteAnswersRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteAnswersReply
};
ItemAdminSession.DeleteAnswer = {
  methodName: "DeleteAnswer",
  service: ItemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteAnswerRequest,
  responseType: dlkit_proto_assessment_pb.DeleteAnswerReply
};
var ItemNotificationSession = {
  serviceName: "dlkit.proto.assessment.ItemNotificationSession"
};
ItemNotificationSession.GetBankId = {
  methodName: "GetBankId",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
ItemNotificationSession.GetBank = {
  methodName: "GetBank",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
ItemNotificationSession.CanRegisterForItemNotifications = {
  methodName: "CanRegisterForItemNotifications",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanRegisterForItemNotificationsRequest,
  responseType: dlkit_proto_assessment_pb.CanRegisterForItemNotificationsReply
};
ItemNotificationSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
ItemNotificationSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
ItemNotificationSession.ReliableItemNotifications = {
  methodName: "ReliableItemNotifications",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.ReliableItemNotificationsRequest,
  responseType: dlkit_proto_assessment_pb.ReliableItemNotificationsReply
};
ItemNotificationSession.UnreliableItemNotifications = {
  methodName: "UnreliableItemNotifications",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UnreliableItemNotificationsRequest,
  responseType: dlkit_proto_assessment_pb.UnreliableItemNotificationsReply
};
ItemNotificationSession.AcknowledgeItemNotification = {
  methodName: "AcknowledgeItemNotification",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AcknowledgeItemNotificationRequest,
  responseType: dlkit_proto_assessment_pb.AcknowledgeItemNotificationReply
};
ItemNotificationSession.RegisterForNewItems = {
  methodName: "RegisterForNewItems",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RegisterForNewItemsRequest,
  responseType: dlkit_proto_assessment_pb.RegisterForNewItemsReply
};
ItemNotificationSession.RegisterForChangedItems = {
  methodName: "RegisterForChangedItems",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RegisterForChangedItemsRequest,
  responseType: dlkit_proto_assessment_pb.RegisterForChangedItemsReply
};
ItemNotificationSession.RegisterForChangedItem = {
  methodName: "RegisterForChangedItem",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RegisterForChangedItemRequest,
  responseType: dlkit_proto_assessment_pb.RegisterForChangedItemReply
};
ItemNotificationSession.RegisterForDeletedItems = {
  methodName: "RegisterForDeletedItems",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RegisterForDeletedItemsRequest,
  responseType: dlkit_proto_assessment_pb.RegisterForDeletedItemsReply
};
ItemNotificationSession.RegisterForDeletedItem = {
  methodName: "RegisterForDeletedItem",
  service: ItemNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RegisterForDeletedItemRequest,
  responseType: dlkit_proto_assessment_pb.RegisterForDeletedItemReply
};
var ItemBankSession = {
  serviceName: "dlkit.proto.assessment.ItemBankSession"
};
ItemBankSession.CanLookupItemBankMappings = {
  methodName: "CanLookupItemBankMappings",
  service: ItemBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupItemBankMappingsRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupItemBankMappingsReply
};
ItemBankSession.UseComparativeBankView = {
  methodName: "UseComparativeBankView",
  service: ItemBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeBankViewReply
};
ItemBankSession.UsePlenaryBankView = {
  methodName: "UsePlenaryBankView",
  service: ItemBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryBankViewReply
};
ItemBankSession.GetItemIdsByBank = {
  methodName: "GetItemIdsByBank",
  service: ItemBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemIdsByBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ItemBankSession.GetItemsByBank = {
  methodName: "GetItemsByBank",
  service: ItemBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByBankRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemBankSession.GetItemIdsByBanks = {
  methodName: "GetItemIdsByBanks",
  service: ItemBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemIdsByBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ItemBankSession.GetItemsByBanks = {
  methodName: "GetItemsByBanks",
  service: ItemBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsByBanksRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
ItemBankSession.GetBankIdsByItem = {
  methodName: "GetBankIdsByItem",
  service: ItemBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBankIdsByItemRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ItemBankSession.GetBanksByItem = {
  methodName: "GetBanksByItem",
  service: ItemBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByItemRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var ItemBankAssignmentSession = {
  serviceName: "dlkit.proto.assessment.ItemBankAssignmentSession"
};
ItemBankAssignmentSession.CanAssignItems = {
  methodName: "CanAssignItems",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignItemsRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignItemsReply
};
ItemBankAssignmentSession.CanAssignItemsToBank = {
  methodName: "CanAssignItemsToBank",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignItemsToBankRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignItemsToBankReply
};
ItemBankAssignmentSession.GetAssignableBankIds = {
  methodName: "GetAssignableBankIds",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ItemBankAssignmentSession.GetAssignableBankIdsForItem = {
  methodName: "GetAssignableBankIdsForItem",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsForItemRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ItemBankAssignmentSession.AssignItemToBank = {
  methodName: "AssignItemToBank",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AssignItemToBankRequest,
  responseType: dlkit_proto_assessment_pb.AssignItemToBankReply
};
ItemBankAssignmentSession.UnassignItemFromBank = {
  methodName: "UnassignItemFromBank",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UnassignItemFromBankRequest,
  responseType: dlkit_proto_assessment_pb.UnassignItemFromBankReply
};
ItemBankAssignmentSession.ReassignItemToBilling = {
  methodName: "ReassignItemToBilling",
  service: ItemBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.ReassignItemToBillingRequest,
  responseType: dlkit_proto_assessment_pb.ReassignItemToBillingReply
};
var AssessmentLookupSession = {
  serviceName: "dlkit.proto.assessment.AssessmentLookupSession"
};
AssessmentLookupSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentLookupSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentLookupSession.CanLookupAssessments = {
  methodName: "CanLookupAssessments",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupAssessmentsReply
};
AssessmentLookupSession.UseComparativeAssessmentView = {
  methodName: "UseComparativeAssessmentView",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeAssessmentViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeAssessmentViewReply
};
AssessmentLookupSession.UsePlenaryAssessmentView = {
  methodName: "UsePlenaryAssessmentView",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryAssessmentViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryAssessmentViewReply
};
AssessmentLookupSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
AssessmentLookupSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
AssessmentLookupSession.GetAssessment = {
  methodName: "GetAssessment",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentReply
};
AssessmentLookupSession.GetAssessmentsByIds = {
  methodName: "GetAssessmentsByIds",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByIdsRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
AssessmentLookupSession.GetAssessmentsByGenusType = {
  methodName: "GetAssessmentsByGenusType",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
AssessmentLookupSession.GetAssessmentsByParentGenusType = {
  methodName: "GetAssessmentsByParentGenusType",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
AssessmentLookupSession.GetAssessmentsByRecordType = {
  methodName: "GetAssessmentsByRecordType",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByRecordTypeRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
AssessmentLookupSession.GetAssessments = {
  methodName: "GetAssessments",
  service: AssessmentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
var AssessmentQuerySession = {
  serviceName: "dlkit.proto.assessment.AssessmentQuerySession"
};
AssessmentQuerySession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentQuerySession.GetBank = {
  methodName: "GetBank",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentQuerySession.CanSearchAssessments = {
  methodName: "CanSearchAssessments",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanSearchAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanSearchAssessmentsReply
};
AssessmentQuerySession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
AssessmentQuerySession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
AssessmentQuerySession.GetAssessmentQuery = {
  methodName: "GetAssessmentQuery",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentQueryRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentQueryReply
};
AssessmentQuerySession.GetAssessmentsByQuery = {
  methodName: "GetAssessmentsByQuery",
  service: AssessmentQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByQueryRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
var AssessmentAdminSession = {
  serviceName: "dlkit.proto.assessment.AssessmentAdminSession"
};
AssessmentAdminSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentAdminSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentAdminSession.CanCreateAssessments = {
  methodName: "CanCreateAssessments",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAssessmentsReply
};
AssessmentAdminSession.CanCreateAssessmentWithRecordTypes = {
  methodName: "CanCreateAssessmentWithRecordTypes",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAssessmentWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAssessmentWithRecordTypesReply
};
AssessmentAdminSession.GetAssessmentFormForCreate = {
  methodName: "GetAssessmentFormForCreate",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentFormForCreateReply
};
AssessmentAdminSession.CreateAssessment = {
  methodName: "CreateAssessment",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.CreateAssessmentReply
};
AssessmentAdminSession.CanUpdateAssessments = {
  methodName: "CanUpdateAssessments",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateAssessmentsReply
};
AssessmentAdminSession.GetAssessmentFormForUpdate = {
  methodName: "GetAssessmentFormForUpdate",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentFormForUpdateReply
};
AssessmentAdminSession.UpdateAssessment = {
  methodName: "UpdateAssessment",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.UpdateAssessmentReply
};
AssessmentAdminSession.CanDeleteAssessments = {
  methodName: "CanDeleteAssessments",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteAssessmentsReply
};
AssessmentAdminSession.DeleteAssessment = {
  methodName: "DeleteAssessment",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.DeleteAssessmentReply
};
AssessmentAdminSession.CanManageAssessmentAliases = {
  methodName: "CanManageAssessmentAliases",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanManageAssessmentAliasesRequest,
  responseType: dlkit_proto_assessment_pb.CanManageAssessmentAliasesReply
};
AssessmentAdminSession.AliasAssessment = {
  methodName: "AliasAssessment",
  service: AssessmentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AliasAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.AliasAssessmentReply
};
var AssessmentBankSession = {
  serviceName: "dlkit.proto.assessment.AssessmentBankSession"
};
AssessmentBankSession.CanLookupAssessmentBankMappings = {
  methodName: "CanLookupAssessmentBankMappings",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupAssessmentBankMappingsRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupAssessmentBankMappingsReply
};
AssessmentBankSession.UseComparativeBankView = {
  methodName: "UseComparativeBankView",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeBankViewReply
};
AssessmentBankSession.UsePlenaryBankView = {
  methodName: "UsePlenaryBankView",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryBankViewReply
};
AssessmentBankSession.GetAssessmentIdsByBank = {
  methodName: "GetAssessmentIdsByBank",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentIdsByBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentBankSession.GetAssessmentsByBank = {
  methodName: "GetAssessmentsByBank",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByBankRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
AssessmentBankSession.GetAssessmentIdsByBanks = {
  methodName: "GetAssessmentIdsByBanks",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentIdsByBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentBankSession.GetAssessmentsByBanks = {
  methodName: "GetAssessmentsByBanks",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsByBanksRequest,
  responseType: dlkit_proto_assessment_pb.Assessment
};
AssessmentBankSession.GetBankIdsByAssessment = {
  methodName: "GetBankIdsByAssessment",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBankIdsByAssessmentRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentBankSession.GetBanksByAssessment = {
  methodName: "GetBanksByAssessment",
  service: AssessmentBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var AssessmentBankAssignmentSession = {
  serviceName: "dlkit.proto.assessment.AssessmentBankAssignmentSession"
};
AssessmentBankAssignmentSession.CanAssignAssessments = {
  methodName: "CanAssignAssessments",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignAssessmentsReply
};
AssessmentBankAssignmentSession.CanAssignAssessmentsToBank = {
  methodName: "CanAssignAssessmentsToBank",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignAssessmentsToBankRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignAssessmentsToBankReply
};
AssessmentBankAssignmentSession.GetAssignableBankIds = {
  methodName: "GetAssignableBankIds",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentBankAssignmentSession.GetAssignableBankIdsForAssessment = {
  methodName: "GetAssignableBankIdsForAssessment",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsForAssessmentRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentBankAssignmentSession.AssignAssessmentToBank = {
  methodName: "AssignAssessmentToBank",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AssignAssessmentToBankRequest,
  responseType: dlkit_proto_assessment_pb.AssignAssessmentToBankReply
};
AssessmentBankAssignmentSession.UnassignAssessmentFromBank = {
  methodName: "UnassignAssessmentFromBank",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UnassignAssessmentFromBankRequest,
  responseType: dlkit_proto_assessment_pb.UnassignAssessmentFromBankReply
};
AssessmentBankAssignmentSession.ReassignAssessmentToBilling = {
  methodName: "ReassignAssessmentToBilling",
  service: AssessmentBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.ReassignAssessmentToBillingRequest,
  responseType: dlkit_proto_assessment_pb.ReassignAssessmentToBillingReply
};
var AssessmentBasicAuthoringSession = {
  serviceName: "dlkit.proto.assessment.AssessmentBasicAuthoringSession"
};
AssessmentBasicAuthoringSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentBasicAuthoringSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentBasicAuthoringSession.CanAuthorAssessments = {
  methodName: "CanAuthorAssessments",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAuthorAssessmentsRequest,
  responseType: dlkit_proto_assessment_pb.CanAuthorAssessmentsReply
};
AssessmentBasicAuthoringSession.GetItems = {
  methodName: "GetItems",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetItemsRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
AssessmentBasicAuthoringSession.AddItem = {
  methodName: "AddItem",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AddItemRequest,
  responseType: dlkit_proto_assessment_pb.AddItemReply
};
AssessmentBasicAuthoringSession.RemoveItem = {
  methodName: "RemoveItem",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RemoveItemRequest,
  responseType: dlkit_proto_assessment_pb.RemoveItemReply
};
AssessmentBasicAuthoringSession.MoveItem = {
  methodName: "MoveItem",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.MoveItemRequest,
  responseType: dlkit_proto_assessment_pb.MoveItemReply
};
AssessmentBasicAuthoringSession.OrderItems = {
  methodName: "OrderItems",
  service: AssessmentBasicAuthoringSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.OrderItemsRequest,
  responseType: dlkit_proto_assessment_pb.OrderItemsReply
};
var AssessmentOfferedLookupSession = {
  serviceName: "dlkit.proto.assessment.AssessmentOfferedLookupSession"
};
AssessmentOfferedLookupSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentOfferedLookupSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentOfferedLookupSession.CanLookupAssessmentsOffered = {
  methodName: "CanLookupAssessmentsOffered",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupAssessmentsOfferedReply
};
AssessmentOfferedLookupSession.UseComparativeAssessmentOfferedView = {
  methodName: "UseComparativeAssessmentOfferedView",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeAssessmentOfferedViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeAssessmentOfferedViewReply
};
AssessmentOfferedLookupSession.UsePlenaryAssessmentOfferedView = {
  methodName: "UsePlenaryAssessmentOfferedView",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryAssessmentOfferedViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryAssessmentOfferedViewReply
};
AssessmentOfferedLookupSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
AssessmentOfferedLookupSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
AssessmentOfferedLookupSession.GetAssessmentOffered = {
  methodName: "GetAssessmentOffered",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentOfferedReply
};
AssessmentOfferedLookupSession.GetAssessmentsOfferedByIds = {
  methodName: "GetAssessmentsOfferedByIds",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByIdsRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedLookupSession.GetAssessmentsOfferedByGenusType = {
  methodName: "GetAssessmentsOfferedByGenusType",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedLookupSession.GetAssessmentsOfferedByParentGenusType = {
  methodName: "GetAssessmentsOfferedByParentGenusType",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedLookupSession.GetAssessmentsOfferedByRecordType = {
  methodName: "GetAssessmentsOfferedByRecordType",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByRecordTypeRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedLookupSession.GetAssessmentsOfferedByDate = {
  methodName: "GetAssessmentsOfferedByDate",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByDateRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedLookupSession.GetAssessmentsOfferedForAssessment = {
  methodName: "GetAssessmentsOfferedForAssessment",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedForAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedLookupSession.GetAssessmentsOffered = {
  methodName: "GetAssessmentsOffered",
  service: AssessmentOfferedLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
var AssessmentOfferedQuerySession = {
  serviceName: "dlkit.proto.assessment.AssessmentOfferedQuerySession"
};
AssessmentOfferedQuerySession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentOfferedQuerySession.GetBank = {
  methodName: "GetBank",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentOfferedQuerySession.CanSearchAssessmentsOffered = {
  methodName: "CanSearchAssessmentsOffered",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanSearchAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CanSearchAssessmentsOfferedReply
};
AssessmentOfferedQuerySession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
AssessmentOfferedQuerySession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
AssessmentOfferedQuerySession.GetAssessmentOfferedQuery = {
  methodName: "GetAssessmentOfferedQuery",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentOfferedQueryRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentOfferedQueryReply
};
AssessmentOfferedQuerySession.GetAssessmentsOfferedByQuery = {
  methodName: "GetAssessmentsOfferedByQuery",
  service: AssessmentOfferedQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByQueryRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
var AssessmentOfferedAdminSession = {
  serviceName: "dlkit.proto.assessment.AssessmentOfferedAdminSession"
};
AssessmentOfferedAdminSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentOfferedAdminSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentOfferedAdminSession.CanCreateAssessmentsOffered = {
  methodName: "CanCreateAssessmentsOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAssessmentsOfferedReply
};
AssessmentOfferedAdminSession.CanCreateAssessmentOfferedWithRecordTypes = {
  methodName: "CanCreateAssessmentOfferedWithRecordTypes",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAssessmentOfferedWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAssessmentOfferedWithRecordTypesReply
};
AssessmentOfferedAdminSession.GetAssessmentOfferedFormForCreate = {
  methodName: "GetAssessmentOfferedFormForCreate",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentOfferedFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentOfferedFormForCreateReply
};
AssessmentOfferedAdminSession.CreateAssessmentOffered = {
  methodName: "CreateAssessmentOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CreateAssessmentOfferedReply
};
AssessmentOfferedAdminSession.CanUpdateAssessmentsOffered = {
  methodName: "CanUpdateAssessmentsOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateAssessmentsOfferedReply
};
AssessmentOfferedAdminSession.GetAssessmentOfferedFormForUpdate = {
  methodName: "GetAssessmentOfferedFormForUpdate",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentOfferedFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentOfferedFormForUpdateReply
};
AssessmentOfferedAdminSession.UpdateAssessmentOffered = {
  methodName: "UpdateAssessmentOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.UpdateAssessmentOfferedReply
};
AssessmentOfferedAdminSession.CanDeleteAssessmentsOffered = {
  methodName: "CanDeleteAssessmentsOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteAssessmentsOfferedReply
};
AssessmentOfferedAdminSession.DeleteAssessmentOffered = {
  methodName: "DeleteAssessmentOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.DeleteAssessmentOfferedReply
};
AssessmentOfferedAdminSession.CanManageAssessmentOfferedAliases = {
  methodName: "CanManageAssessmentOfferedAliases",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanManageAssessmentOfferedAliasesRequest,
  responseType: dlkit_proto_assessment_pb.CanManageAssessmentOfferedAliasesReply
};
AssessmentOfferedAdminSession.AliasAssessmentOffered = {
  methodName: "AliasAssessmentOffered",
  service: AssessmentOfferedAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AliasAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.AliasAssessmentOfferedReply
};
var AssessmentOfferedBankSession = {
  serviceName: "dlkit.proto.assessment.AssessmentOfferedBankSession"
};
AssessmentOfferedBankSession.CanLookupAssessmentOfferedBankMappings = {
  methodName: "CanLookupAssessmentOfferedBankMappings",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupAssessmentOfferedBankMappingsRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupAssessmentOfferedBankMappingsReply
};
AssessmentOfferedBankSession.UseComparativeBankView = {
  methodName: "UseComparativeBankView",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeBankViewReply
};
AssessmentOfferedBankSession.UsePlenaryBankView = {
  methodName: "UsePlenaryBankView",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryBankViewReply
};
AssessmentOfferedBankSession.GetAssessmentOfferedIdsByBank = {
  methodName: "GetAssessmentOfferedIdsByBank",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentOfferedIdsByBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentOfferedBankSession.GetAssessmentsOfferedByBank = {
  methodName: "GetAssessmentsOfferedByBank",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByBankRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedBankSession.GetAssessmentOfferedIdsByBanks = {
  methodName: "GetAssessmentOfferedIdsByBanks",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentOfferedIdsByBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentOfferedBankSession.GetAssessmentsOfferedByBanks = {
  methodName: "GetAssessmentsOfferedByBanks",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsOfferedByBanksRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentOffered
};
AssessmentOfferedBankSession.GetBankIdsByAssessmentOffered = {
  methodName: "GetBankIdsByAssessmentOffered",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBankIdsByAssessmentOfferedRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentOfferedBankSession.GetBanksByAssessmentOffered = {
  methodName: "GetBanksByAssessmentOffered",
  service: AssessmentOfferedBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var AssessmentOfferedBankAssignmentSession = {
  serviceName: "dlkit.proto.assessment.AssessmentOfferedBankAssignmentSession"
};
AssessmentOfferedBankAssignmentSession.CanAssignAssessmentsOffered = {
  methodName: "CanAssignAssessmentsOffered",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedReply
};
AssessmentOfferedBankAssignmentSession.CanAssignAssessmentsOfferedToBank = {
  methodName: "CanAssignAssessmentsOfferedToBank",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedToBankRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignAssessmentsOfferedToBankReply
};
AssessmentOfferedBankAssignmentSession.GetAssignableBankIds = {
  methodName: "GetAssignableBankIds",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentOfferedBankAssignmentSession.GetAssignableBankIdsForAssessmentOffered = {
  methodName: "GetAssignableBankIdsForAssessmentOffered",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsForAssessmentOfferedRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentOfferedBankAssignmentSession.AssignAssessmentOfferedToBank = {
  methodName: "AssignAssessmentOfferedToBank",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AssignAssessmentOfferedToBankRequest,
  responseType: dlkit_proto_assessment_pb.AssignAssessmentOfferedToBankReply
};
AssessmentOfferedBankAssignmentSession.UnassignAssessmentOfferedFromBank = {
  methodName: "UnassignAssessmentOfferedFromBank",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UnassignAssessmentOfferedFromBankRequest,
  responseType: dlkit_proto_assessment_pb.UnassignAssessmentOfferedFromBankReply
};
AssessmentOfferedBankAssignmentSession.ReassignAssessmentOfferedToBilling = {
  methodName: "ReassignAssessmentOfferedToBilling",
  service: AssessmentOfferedBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.ReassignAssessmentOfferedToBillingRequest,
  responseType: dlkit_proto_assessment_pb.ReassignAssessmentOfferedToBillingReply
};
var AssessmentTakenLookupSession = {
  serviceName: "dlkit.proto.assessment.AssessmentTakenLookupSession"
};
AssessmentTakenLookupSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentTakenLookupSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentTakenLookupSession.CanLookupAssessmentsTaken = {
  methodName: "CanLookupAssessmentsTaken",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupAssessmentsTakenReply
};
AssessmentTakenLookupSession.UseComparativeAssessmentTakenView = {
  methodName: "UseComparativeAssessmentTakenView",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeAssessmentTakenViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeAssessmentTakenViewReply
};
AssessmentTakenLookupSession.UsePlenaryAssessmentTakenView = {
  methodName: "UsePlenaryAssessmentTakenView",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryAssessmentTakenViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryAssessmentTakenViewReply
};
AssessmentTakenLookupSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
AssessmentTakenLookupSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
AssessmentTakenLookupSession.GetAssessmentTaken = {
  methodName: "GetAssessmentTaken",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentTakenRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentTakenReply
};
AssessmentTakenLookupSession.GetAssessmentsTakenByIds = {
  methodName: "GetAssessmentsTakenByIds",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByIdsRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByGenusType = {
  methodName: "GetAssessmentsTakenByGenusType",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByParentGenusType = {
  methodName: "GetAssessmentsTakenByParentGenusType",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByRecordType = {
  methodName: "GetAssessmentsTakenByRecordType",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByRecordTypeRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByDate = {
  methodName: "GetAssessmentsTakenByDate",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByDateRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenForTaker = {
  methodName: "GetAssessmentsTakenForTaker",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenForTakerRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByDateForTaker = {
  methodName: "GetAssessmentsTakenByDateForTaker",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForTakerRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenForAssessment = {
  methodName: "GetAssessmentsTakenForAssessment",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenForAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByDateForAssessment = {
  methodName: "GetAssessmentsTakenByDateForAssessment",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenForTakerAndAssessment = {
  methodName: "GetAssessmentsTakenForTakerAndAssessment",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenForTakerAndAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByDateForTakerAndAssessment = {
  methodName: "GetAssessmentsTakenByDateForTakerAndAssessment",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForTakerAndAssessmentRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenForAssessmentOffered = {
  methodName: "GetAssessmentsTakenForAssessmentOffered",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenForAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByDateForAssessmentOffered = {
  methodName: "GetAssessmentsTakenByDateForAssessmentOffered",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenForTakerAndAssessmentOffered = {
  methodName: "GetAssessmentsTakenForTakerAndAssessmentOffered",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenForTakerAndAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTakenByDateForTakerAndAssessmentOffered = {
  methodName: "GetAssessmentsTakenByDateForTakerAndAssessmentOffered",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenLookupSession.GetAssessmentsTaken = {
  methodName: "GetAssessmentsTaken",
  service: AssessmentTakenLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
var AssessmentTakenQuerySession = {
  serviceName: "dlkit.proto.assessment.AssessmentTakenQuerySession"
};
AssessmentTakenQuerySession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentTakenQuerySession.GetBank = {
  methodName: "GetBank",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentTakenQuerySession.CanSearchAssessmentsTaken = {
  methodName: "CanSearchAssessmentsTaken",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanSearchAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.CanSearchAssessmentsTakenReply
};
AssessmentTakenQuerySession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseFederatedBankViewReply
};
AssessmentTakenQuerySession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseIsolatedBankViewReply
};
AssessmentTakenQuerySession.GetAssessmentTakenQuery = {
  methodName: "GetAssessmentTakenQuery",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentTakenQueryRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentTakenQueryReply
};
AssessmentTakenQuerySession.GetAssessmentsTakenByQuery = {
  methodName: "GetAssessmentsTakenByQuery",
  service: AssessmentTakenQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByQueryRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
var AssessmentTakenAdminSession = {
  serviceName: "dlkit.proto.assessment.AssessmentTakenAdminSession"
};
AssessmentTakenAdminSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankIdReply
};
AssessmentTakenAdminSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
AssessmentTakenAdminSession.CanCreateAssessmentsTaken = {
  methodName: "CanCreateAssessmentsTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAssessmentsTakenReply
};
AssessmentTakenAdminSession.CanCreateAssessmentTakenWithRecordTypes = {
  methodName: "CanCreateAssessmentTakenWithRecordTypes",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateAssessmentTakenWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateAssessmentTakenWithRecordTypesReply
};
AssessmentTakenAdminSession.GetAssessmentTakenFormForCreate = {
  methodName: "GetAssessmentTakenFormForCreate",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentTakenFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentTakenFormForCreateReply
};
AssessmentTakenAdminSession.CreateAssessmentTaken = {
  methodName: "CreateAssessmentTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateAssessmentTakenRequest,
  responseType: dlkit_proto_assessment_pb.CreateAssessmentTakenReply
};
AssessmentTakenAdminSession.CanUpdateAssessmentsTaken = {
  methodName: "CanUpdateAssessmentsTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateAssessmentsTakenReply
};
AssessmentTakenAdminSession.GetAssessmentTakenFormForUpdate = {
  methodName: "GetAssessmentTakenFormForUpdate",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetAssessmentTakenFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetAssessmentTakenFormForUpdateReply
};
AssessmentTakenAdminSession.UpdateAssessmentTaken = {
  methodName: "UpdateAssessmentTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateAssessmentTakenRequest,
  responseType: dlkit_proto_assessment_pb.UpdateAssessmentTakenReply
};
AssessmentTakenAdminSession.CanDeleteAssessmentsTaken = {
  methodName: "CanDeleteAssessmentsTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteAssessmentsTakenReply
};
AssessmentTakenAdminSession.DeleteAssessmentTaken = {
  methodName: "DeleteAssessmentTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteAssessmentTakenRequest,
  responseType: dlkit_proto_assessment_pb.DeleteAssessmentTakenReply
};
AssessmentTakenAdminSession.CanManageAssessmentTakenAliases = {
  methodName: "CanManageAssessmentTakenAliases",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanManageAssessmentTakenAliasesRequest,
  responseType: dlkit_proto_assessment_pb.CanManageAssessmentTakenAliasesReply
};
AssessmentTakenAdminSession.AliasAssessmentTaken = {
  methodName: "AliasAssessmentTaken",
  service: AssessmentTakenAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AliasAssessmentTakenRequest,
  responseType: dlkit_proto_assessment_pb.AliasAssessmentTakenReply
};
var AssessmentTakenBankSession = {
  serviceName: "dlkit.proto.assessment.AssessmentTakenBankSession"
};
AssessmentTakenBankSession.CanLookupAssessmentTakenBankMappings = {
  methodName: "CanLookupAssessmentTakenBankMappings",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupAssessmentTakenBankMappingsRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupAssessmentTakenBankMappingsReply
};
AssessmentTakenBankSession.UseComparativeBankView = {
  methodName: "UseComparativeBankView",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeBankViewReply
};
AssessmentTakenBankSession.UsePlenaryBankView = {
  methodName: "UsePlenaryBankView",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryBankViewReply
};
AssessmentTakenBankSession.GetAssessmentTakenIdsByBank = {
  methodName: "GetAssessmentTakenIdsByBank",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentTakenIdsByBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentTakenBankSession.GetAssessmentsTakenByBank = {
  methodName: "GetAssessmentsTakenByBank",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByBankRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenBankSession.GetAssessmentTakenIdsByBanks = {
  methodName: "GetAssessmentTakenIdsByBanks",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentTakenIdsByBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentTakenBankSession.GetAssessmentsTakenByBanks = {
  methodName: "GetAssessmentsTakenByBanks",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssessmentsTakenByBanksRequest,
  responseType: dlkit_proto_assessment_pb.AssessmentTaken
};
AssessmentTakenBankSession.GetBankIdsByAssessmentTaken = {
  methodName: "GetBankIdsByAssessmentTaken",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBankIdsByAssessmentTakenRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentTakenBankSession.GetBanksByAssessmentTaken = {
  methodName: "GetBanksByAssessmentTaken",
  service: AssessmentTakenBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByAssessmentTakenRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var AssessmentTakenBankAssignmentSession = {
  serviceName: "dlkit.proto.assessment.AssessmentTakenBankAssignmentSession"
};
AssessmentTakenBankAssignmentSession.CanAssignAssessmentsTaken = {
  methodName: "CanAssignAssessmentsTaken",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignAssessmentsTakenRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignAssessmentsTakenReply
};
AssessmentTakenBankAssignmentSession.CanAssignAssessmentsTakenToBank = {
  methodName: "CanAssignAssessmentsTakenToBank",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAssignAssessmentsTakenToBankRequest,
  responseType: dlkit_proto_assessment_pb.CanAssignAssessmentsTakenToBankReply
};
AssessmentTakenBankAssignmentSession.GetAssignableBankIds = {
  methodName: "GetAssignableBankIds",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentTakenBankAssignmentSession.GetAssignableBankIdsForAssessmentTaken = {
  methodName: "GetAssignableBankIdsForAssessmentTaken",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetAssignableBankIdsForAssessmentTakenRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentTakenBankAssignmentSession.AssignAssessmentTakenToBank = {
  methodName: "AssignAssessmentTakenToBank",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AssignAssessmentTakenToBankRequest,
  responseType: dlkit_proto_assessment_pb.AssignAssessmentTakenToBankReply
};
AssessmentTakenBankAssignmentSession.UnassignAssessmentTakenFromBank = {
  methodName: "UnassignAssessmentTakenFromBank",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UnassignAssessmentTakenFromBankRequest,
  responseType: dlkit_proto_assessment_pb.UnassignAssessmentTakenFromBankReply
};
AssessmentTakenBankAssignmentSession.ReassignAssessmentTakenToBilling = {
  methodName: "ReassignAssessmentTakenToBilling",
  service: AssessmentTakenBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.ReassignAssessmentTakenToBillingRequest,
  responseType: dlkit_proto_assessment_pb.ReassignAssessmentTakenToBillingReply
};
var BankLookupSession = {
  serviceName: "dlkit.proto.assessment.BankLookupSession"
};
BankLookupSession.CanLookupBanks = {
  methodName: "CanLookupBanks",
  service: BankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanLookupBanksRequest,
  responseType: dlkit_proto_assessment_pb.CanLookupBanksReply
};
BankLookupSession.UseComparativeBankView = {
  methodName: "UseComparativeBankView",
  service: BankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeBankViewReply
};
BankLookupSession.UsePlenaryBankView = {
  methodName: "UsePlenaryBankView",
  service: BankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryBankViewReply
};
BankLookupSession.GetBank = {
  methodName: "GetBank",
  service: BankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_pb.GetBankReply
};
BankLookupSession.GetBanksByIds = {
  methodName: "GetBanksByIds",
  service: BankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByIdsRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankLookupSession.GetBanksByGenusType = {
  methodName: "GetBanksByGenusType",
  service: BankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankLookupSession.GetBanksByParentGenusType = {
  methodName: "GetBanksByParentGenusType",
  service: BankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankLookupSession.GetBanksByRecordType = {
  methodName: "GetBanksByRecordType",
  service: BankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByRecordTypeRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankLookupSession.GetBanksByProvider = {
  methodName: "GetBanksByProvider",
  service: BankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByProviderRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankLookupSession.GetBanks = {
  methodName: "GetBanks",
  service: BankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var BankQuerySession = {
  serviceName: "dlkit.proto.assessment.BankQuerySession"
};
BankQuerySession.CanSearchBanks = {
  methodName: "CanSearchBanks",
  service: BankQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanSearchBanksRequest,
  responseType: dlkit_proto_assessment_pb.CanSearchBanksReply
};
BankQuerySession.GetBankQuery = {
  methodName: "GetBankQuery",
  service: BankQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankQueryRequest,
  responseType: dlkit_proto_assessment_pb.GetBankQueryReply
};
BankQuerySession.GetBanksByQuery = {
  methodName: "GetBanksByQuery",
  service: BankQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetBanksByQueryRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var BankAdminSession = {
  serviceName: "dlkit.proto.assessment.BankAdminSession"
};
BankAdminSession.CanCreateBanks = {
  methodName: "CanCreateBanks",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateBanksRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateBanksReply
};
BankAdminSession.CanCreateBankWithRecordTypes = {
  methodName: "CanCreateBankWithRecordTypes",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanCreateBankWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_pb.CanCreateBankWithRecordTypesReply
};
BankAdminSession.GetBankFormForCreate = {
  methodName: "GetBankFormForCreate",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankFormForCreateRequest,
  responseType: dlkit_proto_assessment_pb.GetBankFormForCreateReply
};
BankAdminSession.CreateBank = {
  methodName: "CreateBank",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CreateBankRequest,
  responseType: dlkit_proto_assessment_pb.CreateBankReply
};
BankAdminSession.CanUpdateBanks = {
  methodName: "CanUpdateBanks",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanUpdateBanksRequest,
  responseType: dlkit_proto_assessment_pb.CanUpdateBanksReply
};
BankAdminSession.GetBankFormForUpdate = {
  methodName: "GetBankFormForUpdate",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankFormForUpdateRequest,
  responseType: dlkit_proto_assessment_pb.GetBankFormForUpdateReply
};
BankAdminSession.UpdateBank = {
  methodName: "UpdateBank",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UpdateBankRequest,
  responseType: dlkit_proto_assessment_pb.UpdateBankReply
};
BankAdminSession.CanDeleteBanks = {
  methodName: "CanDeleteBanks",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanDeleteBanksRequest,
  responseType: dlkit_proto_assessment_pb.CanDeleteBanksReply
};
BankAdminSession.DeleteBank = {
  methodName: "DeleteBank",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.DeleteBankRequest,
  responseType: dlkit_proto_assessment_pb.DeleteBankReply
};
BankAdminSession.CanManageBankAliases = {
  methodName: "CanManageBankAliases",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanManageBankAliasesRequest,
  responseType: dlkit_proto_assessment_pb.CanManageBankAliasesReply
};
BankAdminSession.AliasBank = {
  methodName: "AliasBank",
  service: BankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AliasBankRequest,
  responseType: dlkit_proto_assessment_pb.AliasBankReply
};
var BankHierarchySession = {
  serviceName: "dlkit.proto.assessment.BankHierarchySession"
};
BankHierarchySession.GetBankHierarchyId = {
  methodName: "GetBankHierarchyId",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankHierarchyIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankHierarchyIdReply
};
BankHierarchySession.GetBankHierarchy = {
  methodName: "GetBankHierarchy",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankHierarchyRequest,
  responseType: dlkit_proto_assessment_pb.GetBankHierarchyReply
};
BankHierarchySession.CanAccessBankHierarchy = {
  methodName: "CanAccessBankHierarchy",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanAccessBankHierarchyRequest,
  responseType: dlkit_proto_assessment_pb.CanAccessBankHierarchyReply
};
BankHierarchySession.UseComparativeBankView = {
  methodName: "UseComparativeBankView",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UseComparativeBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UseComparativeBankViewReply
};
BankHierarchySession.UsePlenaryBankView = {
  methodName: "UsePlenaryBankView",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.UsePlenaryBankViewRequest,
  responseType: dlkit_proto_assessment_pb.UsePlenaryBankViewReply
};
BankHierarchySession.GetRootBankIds = {
  methodName: "GetRootBankIds",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetRootBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BankHierarchySession.GetRootBanks = {
  methodName: "GetRootBanks",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetRootBanksRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankHierarchySession.HasParentBanks = {
  methodName: "HasParentBanks",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasParentBanksRequest,
  responseType: dlkit_proto_assessment_pb.HasParentBanksReply
};
BankHierarchySession.IsParentOfBank = {
  methodName: "IsParentOfBank",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsParentOfBankRequest,
  responseType: dlkit_proto_assessment_pb.IsParentOfBankReply
};
BankHierarchySession.GetParentBankIds = {
  methodName: "GetParentBankIds",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetParentBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BankHierarchySession.GetParentBanks = {
  methodName: "GetParentBanks",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetParentBanksRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankHierarchySession.IsAncestorOfBank = {
  methodName: "IsAncestorOfBank",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsAncestorOfBankRequest,
  responseType: dlkit_proto_assessment_pb.IsAncestorOfBankReply
};
BankHierarchySession.HasChildBanks = {
  methodName: "HasChildBanks",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.HasChildBanksRequest,
  responseType: dlkit_proto_assessment_pb.HasChildBanksReply
};
BankHierarchySession.IsChildOfBank = {
  methodName: "IsChildOfBank",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsChildOfBankRequest,
  responseType: dlkit_proto_assessment_pb.IsChildOfBankReply
};
BankHierarchySession.GetChildBankIds = {
  methodName: "GetChildBankIds",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetChildBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BankHierarchySession.GetChildBanks = {
  methodName: "GetChildBanks",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_pb.GetChildBanksRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
BankHierarchySession.IsDescendantOfBank = {
  methodName: "IsDescendantOfBank",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.IsDescendantOfBankRequest,
  responseType: dlkit_proto_assessment_pb.IsDescendantOfBankReply
};
BankHierarchySession.GetBankNodeIds = {
  methodName: "GetBankNodeIds",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankNodeIdsRequest,
  responseType: dlkit_proto_assessment_pb.GetBankNodeIdsReply
};
BankHierarchySession.GetBankNodes = {
  methodName: "GetBankNodes",
  service: BankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankNodesRequest,
  responseType: dlkit_proto_assessment_pb.GetBankNodesReply
};
var BankHierarchyDesignSession = {
  serviceName: "dlkit.proto.assessment.BankHierarchyDesignSession"
};
BankHierarchyDesignSession.GetBankHierarchyId = {
  methodName: "GetBankHierarchyId",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankHierarchyIdRequest,
  responseType: dlkit_proto_assessment_pb.GetBankHierarchyIdReply
};
BankHierarchyDesignSession.GetBankHierarchy = {
  methodName: "GetBankHierarchy",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.GetBankHierarchyRequest,
  responseType: dlkit_proto_assessment_pb.GetBankHierarchyReply
};
BankHierarchyDesignSession.CanModifyBankHierarchy = {
  methodName: "CanModifyBankHierarchy",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.CanModifyBankHierarchyRequest,
  responseType: dlkit_proto_assessment_pb.CanModifyBankHierarchyReply
};
BankHierarchyDesignSession.AddRootBank = {
  methodName: "AddRootBank",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AddRootBankRequest,
  responseType: dlkit_proto_assessment_pb.AddRootBankReply
};
BankHierarchyDesignSession.RemoveRootBank = {
  methodName: "RemoveRootBank",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RemoveRootBankRequest,
  responseType: dlkit_proto_assessment_pb.RemoveRootBankReply
};
BankHierarchyDesignSession.AddChildBank = {
  methodName: "AddChildBank",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.AddChildBankRequest,
  responseType: dlkit_proto_assessment_pb.AddChildBankReply
};
BankHierarchyDesignSession.RemoveChildBank = {
  methodName: "RemoveChildBank",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RemoveChildBankRequest,
  responseType: dlkit_proto_assessment_pb.RemoveChildBankReply
};
BankHierarchyDesignSession.RemoveChildBanks = {
  methodName: "RemoveChildBanks",
  service: BankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_pb.RemoveChildBanksRequest,
  responseType: dlkit_proto_assessment_pb.RemoveChildBanksReply
};
module.exports = {
  AssessmentSession: AssessmentSession,
  AssessmentResultsSession: AssessmentResultsSession,
  ItemLookupSession: ItemLookupSession,
  ItemQuerySession: ItemQuerySession,
  ItemSearchSession: ItemSearchSession,
  ItemAdminSession: ItemAdminSession,
  ItemNotificationSession: ItemNotificationSession,
  ItemBankSession: ItemBankSession,
  ItemBankAssignmentSession: ItemBankAssignmentSession,
  AssessmentLookupSession: AssessmentLookupSession,
  AssessmentQuerySession: AssessmentQuerySession,
  AssessmentAdminSession: AssessmentAdminSession,
  AssessmentBankSession: AssessmentBankSession,
  AssessmentBankAssignmentSession: AssessmentBankAssignmentSession,
  AssessmentBasicAuthoringSession: AssessmentBasicAuthoringSession,
  AssessmentOfferedLookupSession: AssessmentOfferedLookupSession,
  AssessmentOfferedQuerySession: AssessmentOfferedQuerySession,
  AssessmentOfferedAdminSession: AssessmentOfferedAdminSession,
  AssessmentOfferedBankSession: AssessmentOfferedBankSession,
  AssessmentOfferedBankAssignmentSession: AssessmentOfferedBankAssignmentSession,
  AssessmentTakenLookupSession: AssessmentTakenLookupSession,
  AssessmentTakenQuerySession: AssessmentTakenQuerySession,
  AssessmentTakenAdminSession: AssessmentTakenAdminSession,
  AssessmentTakenBankSession: AssessmentTakenBankSession,
  AssessmentTakenBankAssignmentSession: AssessmentTakenBankAssignmentSession,
  BankLookupSession: BankLookupSession,
  BankQuerySession: BankQuerySession,
  BankAdminSession: BankAdminSession,
  BankHierarchySession: BankHierarchySession,
  BankHierarchyDesignSession: BankHierarchyDesignSession,
};

