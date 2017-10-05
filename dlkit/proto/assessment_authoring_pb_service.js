// package: dlkit.proto.assessment_authoring
// file: dlkit/proto/assessment_authoring.proto

var jspb = require("google-protobuf");
var dlkit_proto_assessment_authoring_pb = require("../../dlkit/proto/assessment_authoring_pb");
var dlkit_primordium_calendaring_primitives_pb = require("../../dlkit/primordium/calendaring/primitives_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_assessment_pb = require("../../dlkit/proto/assessment_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var AssessmentPartLookupSession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartLookupSession"
};
AssessmentPartLookupSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
AssessmentPartLookupSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
AssessmentPartLookupSession.CanLookupAssessmentParts = {
  methodName: "CanLookupAssessmentParts",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartsReply
};
AssessmentPartLookupSession.UseComparativeAssessmentPartView = {
  methodName: "UseComparativeAssessmentPartView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartViewReply
};
AssessmentPartLookupSession.UsePlenaryAssessmentPartView = {
  methodName: "UsePlenaryAssessmentPartView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartViewReply
};
AssessmentPartLookupSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply
};
AssessmentPartLookupSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply
};
AssessmentPartLookupSession.UseActiveAssessmentPartView = {
  methodName: "UseActiveAssessmentPartView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseActiveAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseActiveAssessmentPartViewReply
};
AssessmentPartLookupSession.UseAnyStatusAssessmentPartView = {
  methodName: "UseAnyStatusAssessmentPartView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseAnyStatusAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseAnyStatusAssessmentPartViewReply
};
AssessmentPartLookupSession.UseSequesteredAssessmentPartView = {
  methodName: "UseSequesteredAssessmentPartView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewReply
};
AssessmentPartLookupSession.UseUnsequesteredAssessmentPartView = {
  methodName: "UseUnsequesteredAssessmentPartView",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewReply
};
AssessmentPartLookupSession.GetAssessmentPart = {
  methodName: "GetAssessmentPart",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartReply
};
AssessmentPartLookupSession.GetAssessmentPartsByIds = {
  methodName: "GetAssessmentPartsByIds",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByIdsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartLookupSession.GetAssessmentPartsByGenusType = {
  methodName: "GetAssessmentPartsByGenusType",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByGenusTypeRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartLookupSession.GetAssessmentPartsByParentGenusType = {
  methodName: "GetAssessmentPartsByParentGenusType",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartLookupSession.GetAssessmentPartsByRecordType = {
  methodName: "GetAssessmentPartsByRecordType",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByRecordTypeRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartLookupSession.GetAssessmentPartsForAssessment = {
  methodName: "GetAssessmentPartsForAssessment",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsForAssessmentRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartLookupSession.GetAssessmentParts = {
  methodName: "GetAssessmentParts",
  service: AssessmentPartLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
var AssessmentPartQuerySession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartQuerySession"
};
AssessmentPartQuerySession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
AssessmentPartQuerySession.GetBank = {
  methodName: "GetBank",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
AssessmentPartQuerySession.CanSearchAssessmentParts = {
  methodName: "CanSearchAssessmentParts",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanSearchAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanSearchAssessmentPartsReply
};
AssessmentPartQuerySession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply
};
AssessmentPartQuerySession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply
};
AssessmentPartQuerySession.UseSequesteredAssessmentPartView = {
  methodName: "UseSequesteredAssessmentPartView",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewReply
};
AssessmentPartQuerySession.UseUnsequesteredAssessmentPartView = {
  methodName: "UseUnsequesteredAssessmentPartView",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewReply
};
AssessmentPartQuerySession.GetAssessmentPartQuery = {
  methodName: "GetAssessmentPartQuery",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartQueryRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartQueryReply
};
AssessmentPartQuerySession.GetAssessmentPartsByQuery = {
  methodName: "GetAssessmentPartsByQuery",
  service: AssessmentPartQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByQueryRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
var AssessmentPartAdminSession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartAdminSession"
};
AssessmentPartAdminSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
AssessmentPartAdminSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
AssessmentPartAdminSession.CanCreateAssessmentParts = {
  methodName: "CanCreateAssessmentParts",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartsReply
};
AssessmentPartAdminSession.CanCreateAssessmentPartWithRecordTypes = {
  methodName: "CanCreateAssessmentPartWithRecordTypes",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartWithRecordTypesReply
};
AssessmentPartAdminSession.GetAssessmentPartFormForCreateForAssessment = {
  methodName: "GetAssessmentPartFormForCreateForAssessment",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentReply
};
AssessmentPartAdminSession.CreateAssessmentPartForAssessment = {
  methodName: "CreateAssessmentPartForAssessment",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentReply
};
AssessmentPartAdminSession.GetAssessmentPartFormForCreateForAssessmentPart = {
  methodName: "GetAssessmentPartFormForCreateForAssessmentPart",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentPartReply
};
AssessmentPartAdminSession.CreateAssessmentPartForAssessmentPart = {
  methodName: "CreateAssessmentPartForAssessmentPart",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentPartReply
};
AssessmentPartAdminSession.CanUpdateAssessmentParts = {
  methodName: "CanUpdateAssessmentParts",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanUpdateAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanUpdateAssessmentPartsReply
};
AssessmentPartAdminSession.GetAssessmentPartFormForUpdate = {
  methodName: "GetAssessmentPartFormForUpdate",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForUpdateRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForUpdateReply
};
AssessmentPartAdminSession.UpdateAssessmentPart = {
  methodName: "UpdateAssessmentPart",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UpdateAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UpdateAssessmentPartReply
};
AssessmentPartAdminSession.CanDeleteAssessmentParts = {
  methodName: "CanDeleteAssessmentParts",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanDeleteAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanDeleteAssessmentPartsReply
};
AssessmentPartAdminSession.DeleteAssessmentPart = {
  methodName: "DeleteAssessmentPart",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.DeleteAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.DeleteAssessmentPartReply
};
AssessmentPartAdminSession.CanManageAssessmentPartAliases = {
  methodName: "CanManageAssessmentPartAliases",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanManageAssessmentPartAliasesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanManageAssessmentPartAliasesReply
};
AssessmentPartAdminSession.AliasAssessmentPart = {
  methodName: "AliasAssessmentPart",
  service: AssessmentPartAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.AliasAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AliasAssessmentPartReply
};
var AssessmentPartBankSession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartBankSession"
};
AssessmentPartBankSession.CanLookupAssessmentPartBankMappings = {
  methodName: "CanLookupAssessmentPartBankMappings",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartBankMappingsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartBankMappingsReply
};
AssessmentPartBankSession.UseComparativeAssessmentPartBankView = {
  methodName: "UseComparativeAssessmentPartBankView",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartBankViewReply
};
AssessmentPartBankSession.UsePlenaryAssessmentPartBankView = {
  methodName: "UsePlenaryAssessmentPartBankView",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartBankViewReply
};
AssessmentPartBankSession.GetAssessmentPartIdsByBank = {
  methodName: "GetAssessmentPartIdsByBank",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartIdsByBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentPartBankSession.GetAssessmentPartsByBank = {
  methodName: "GetAssessmentPartsByBank",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartBankSession.GetAssessmentPartIdsByBanks = {
  methodName: "GetAssessmentPartIdsByBanks",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartIdsByBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentPartBankSession.GetAssessmentPartsByBanks = {
  methodName: "GetAssessmentPartsByBanks",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByBanksRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
AssessmentPartBankSession.GetBankIdsByAssessmentPart = {
  methodName: "GetBankIdsByAssessmentPart",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdsByAssessmentPartRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentPartBankSession.GetBanksByAssessmentPart = {
  methodName: "GetBanksByAssessmentPart",
  service: AssessmentPartBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetBanksByAssessmentPartRequest,
  responseType: dlkit_proto_assessment_pb.Bank
};
var AssessmentPartBankAssignmentSession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartBankAssignmentSession"
};
AssessmentPartBankAssignmentSession.CanAssignAssessmentParts = {
  methodName: "CanAssignAssessmentParts",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsReply
};
AssessmentPartBankAssignmentSession.CanAssignAssessmentPartsToBank = {
  methodName: "CanAssignAssessmentPartsToBank",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsToBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsToBankReply
};
AssessmentPartBankAssignmentSession.GetAssignableBankIds = {
  methodName: "GetAssignableBankIds",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssignableBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentPartBankAssignmentSession.GetAssignableBankIdsForAssessmentPart = {
  methodName: "GetAssignableBankIdsForAssessmentPart",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssignableBankIdsForAssessmentPartRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssessmentPartBankAssignmentSession.AssignAssessmentPartToBank = {
  methodName: "AssignAssessmentPartToBank",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.AssignAssessmentPartToBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssignAssessmentPartToBankReply
};
AssessmentPartBankAssignmentSession.UnassignAssessmentPartFromBank = {
  methodName: "UnassignAssessmentPartFromBank",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UnassignAssessmentPartFromBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UnassignAssessmentPartFromBankReply
};
AssessmentPartBankAssignmentSession.ReassignAssessmentPartToBank = {
  methodName: "ReassignAssessmentPartToBank",
  service: AssessmentPartBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.ReassignAssessmentPartToBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.ReassignAssessmentPartToBankReply
};
var AssessmentPartItemSession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartItemSession"
};
AssessmentPartItemSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
AssessmentPartItemSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
AssessmentPartItemSession.CanAccessAssessmentPartItems = {
  methodName: "CanAccessAssessmentPartItems",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanAccessAssessmentPartItemsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanAccessAssessmentPartItemsReply
};
AssessmentPartItemSession.UseComparativeAsseessmentPartItemView = {
  methodName: "UseComparativeAsseessmentPartItemView",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseComparativeAsseessmentPartItemViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseComparativeAsseessmentPartItemViewReply
};
AssessmentPartItemSession.UsePlenaryAssessmentPartItemView = {
  methodName: "UsePlenaryAssessmentPartItemView",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartItemViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartItemViewReply
};
AssessmentPartItemSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply
};
AssessmentPartItemSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply
};
AssessmentPartItemSession.GetAssessmentPartItems = {
  methodName: "GetAssessmentPartItems",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartItemsRequest,
  responseType: dlkit_proto_assessment_pb.Item
};
AssessmentPartItemSession.GetAssessmentPartsByItem = {
  methodName: "GetAssessmentPartsByItem",
  service: AssessmentPartItemSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByItemRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AssessmentPart
};
var AssessmentPartItemDesignSession = {
  serviceName: "dlkit.proto.assessment_authoring.AssessmentPartItemDesignSession"
};
AssessmentPartItemDesignSession.GetBankId = {
  methodName: "GetBankId",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
AssessmentPartItemDesignSession.GetBank = {
  methodName: "GetBank",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
AssessmentPartItemDesignSession.CanDesignAssessmentParts = {
  methodName: "CanDesignAssessmentParts",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanDesignAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanDesignAssessmentPartsReply
};
AssessmentPartItemDesignSession.AddItem = {
  methodName: "AddItem",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.AddItemRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AddItemReply
};
AssessmentPartItemDesignSession.MoveItemAhead = {
  methodName: "MoveItemAhead",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.MoveItemAheadRequest,
  responseType: dlkit_proto_assessment_authoring_pb.MoveItemAheadReply
};
AssessmentPartItemDesignSession.MoveItemBehind = {
  methodName: "MoveItemBehind",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.MoveItemBehindRequest,
  responseType: dlkit_proto_assessment_authoring_pb.MoveItemBehindReply
};
AssessmentPartItemDesignSession.OrderItems = {
  methodName: "OrderItems",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.OrderItemsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.OrderItemsReply
};
AssessmentPartItemDesignSession.RemoveItem = {
  methodName: "RemoveItem",
  service: AssessmentPartItemDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.RemoveItemRequest,
  responseType: dlkit_proto_assessment_authoring_pb.RemoveItemReply
};
var SequenceRuleLookupSession = {
  serviceName: "dlkit.proto.assessment_authoring.SequenceRuleLookupSession"
};
SequenceRuleLookupSession.GetBankId = {
  methodName: "GetBankId",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
SequenceRuleLookupSession.GetBank = {
  methodName: "GetBank",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
SequenceRuleLookupSession.CanLookupSequenceRules = {
  methodName: "CanLookupSequenceRules",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanLookupSequenceRulesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanLookupSequenceRulesReply
};
SequenceRuleLookupSession.UseComparativeSequenceRuleView = {
  methodName: "UseComparativeSequenceRuleView",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseComparativeSequenceRuleViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseComparativeSequenceRuleViewReply
};
SequenceRuleLookupSession.UsePlenarySequenceRuleView = {
  methodName: "UsePlenarySequenceRuleView",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UsePlenarySequenceRuleViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UsePlenarySequenceRuleViewReply
};
SequenceRuleLookupSession.UseFederatedBankView = {
  methodName: "UseFederatedBankView",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply
};
SequenceRuleLookupSession.UseIsolatedBankView = {
  methodName: "UseIsolatedBankView",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply
};
SequenceRuleLookupSession.UseActiveSequenceRuleView = {
  methodName: "UseActiveSequenceRuleView",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseActiveSequenceRuleViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseActiveSequenceRuleViewReply
};
SequenceRuleLookupSession.UseAnyStatusSequenceRuleView = {
  methodName: "UseAnyStatusSequenceRuleView",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UseAnyStatusSequenceRuleViewRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UseAnyStatusSequenceRuleViewReply
};
SequenceRuleLookupSession.GetSequenceRule = {
  methodName: "GetSequenceRule",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRuleRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetSequenceRuleReply
};
SequenceRuleLookupSession.GetSequenceRulesByIds = {
  methodName: "GetSequenceRulesByIds",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesByIdsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesByGenusType = {
  methodName: "GetSequenceRulesByGenusType",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesByGenusTypeRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesByParentGenusType = {
  methodName: "GetSequenceRulesByParentGenusType",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesByParentGenusTypeRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesByRecordType = {
  methodName: "GetSequenceRulesByRecordType",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesByRecordTypeRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesForAssessmentPart = {
  methodName: "GetSequenceRulesForAssessmentPart",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesForAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesForNextAssessmentPart = {
  methodName: "GetSequenceRulesForNextAssessmentPart",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesForNextAssessmentPartRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesForAssessmentParts = {
  methodName: "GetSequenceRulesForAssessmentParts",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesForAssessmentPartsRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRulesForAssessment = {
  methodName: "GetSequenceRulesForAssessment",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesForAssessmentRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
SequenceRuleLookupSession.GetSequenceRules = {
  methodName: "GetSequenceRules",
  service: SequenceRuleLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRulesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.SequenceRule
};
var SequenceRuleAdminSession = {
  serviceName: "dlkit.proto.assessment_authoring.SequenceRuleAdminSession"
};
SequenceRuleAdminSession.GetBankId = {
  methodName: "GetBankId",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankIdRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankIdReply
};
SequenceRuleAdminSession.GetBank = {
  methodName: "GetBank",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetBankRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetBankReply
};
SequenceRuleAdminSession.CanCreateSequenceRule = {
  methodName: "CanCreateSequenceRule",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleReply
};
SequenceRuleAdminSession.CanCreateSequenceRuleWithRecordTypes = {
  methodName: "CanCreateSequenceRuleWithRecordTypes",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleWithRecordTypesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleWithRecordTypesReply
};
SequenceRuleAdminSession.GetSequenceRuleFormForCreate = {
  methodName: "GetSequenceRuleFormForCreate",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForCreateRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForCreateReply
};
SequenceRuleAdminSession.CreateSequenceRule = {
  methodName: "CreateSequenceRule",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CreateSequenceRuleRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CreateSequenceRuleReply
};
SequenceRuleAdminSession.CanUpdateSequenceRules = {
  methodName: "CanUpdateSequenceRules",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanUpdateSequenceRulesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanUpdateSequenceRulesReply
};
SequenceRuleAdminSession.GetSequenceRuleFormForUpdate = {
  methodName: "GetSequenceRuleFormForUpdate",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForUpdateRequest,
  responseType: dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForUpdateReply
};
SequenceRuleAdminSession.UpdateSequenceRule = {
  methodName: "UpdateSequenceRule",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.UpdateSequenceRuleRequest,
  responseType: dlkit_proto_assessment_authoring_pb.UpdateSequenceRuleReply
};
SequenceRuleAdminSession.CanDeleteSequenceRules = {
  methodName: "CanDeleteSequenceRules",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanDeleteSequenceRulesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanDeleteSequenceRulesReply
};
SequenceRuleAdminSession.DeleteSequenceRule = {
  methodName: "DeleteSequenceRule",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.DeleteSequenceRuleRequest,
  responseType: dlkit_proto_assessment_authoring_pb.DeleteSequenceRuleReply
};
SequenceRuleAdminSession.CanManageSequenceRuleAliases = {
  methodName: "CanManageSequenceRuleAliases",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanManageSequenceRuleAliasesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanManageSequenceRuleAliasesReply
};
SequenceRuleAdminSession.AliasSequenceRule = {
  methodName: "AliasSequenceRule",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.AliasSequenceRuleRequest,
  responseType: dlkit_proto_assessment_authoring_pb.AliasSequenceRuleReply
};
SequenceRuleAdminSession.CanSequenceSequenceRules = {
  methodName: "CanSequenceSequenceRules",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.CanSequenceSequenceRulesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.CanSequenceSequenceRulesReply
};
SequenceRuleAdminSession.MoveSequenceRuleAhead = {
  methodName: "MoveSequenceRuleAhead",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.MoveSequenceRuleAheadRequest,
  responseType: dlkit_proto_assessment_authoring_pb.MoveSequenceRuleAheadReply
};
SequenceRuleAdminSession.MoveSequenceRuleBehind = {
  methodName: "MoveSequenceRuleBehind",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.MoveSequenceRuleBehindRequest,
  responseType: dlkit_proto_assessment_authoring_pb.MoveSequenceRuleBehindReply
};
SequenceRuleAdminSession.OrderSequenceRules = {
  methodName: "OrderSequenceRules",
  service: SequenceRuleAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_assessment_authoring_pb.OrderSequenceRulesRequest,
  responseType: dlkit_proto_assessment_authoring_pb.OrderSequenceRulesReply
};
module.exports = {
  AssessmentPartLookupSession: AssessmentPartLookupSession,
  AssessmentPartQuerySession: AssessmentPartQuerySession,
  AssessmentPartAdminSession: AssessmentPartAdminSession,
  AssessmentPartBankSession: AssessmentPartBankSession,
  AssessmentPartBankAssignmentSession: AssessmentPartBankAssignmentSession,
  AssessmentPartItemSession: AssessmentPartItemSession,
  AssessmentPartItemDesignSession: AssessmentPartItemDesignSession,
  SequenceRuleLookupSession: SequenceRuleLookupSession,
  SequenceRuleAdminSession: SequenceRuleAdminSession,
};

