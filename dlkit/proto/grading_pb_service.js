// package: dlkit.proto.grading
// file: dlkit/proto/grading.proto

var jspb = require("google-protobuf");
var dlkit_proto_grading_pb = require("../../dlkit/proto/grading_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var GradeSystemLookupSession = {
  serviceName: "dlkit.proto.grading.GradeSystemLookupSession"
};
GradeSystemLookupSession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradeSystemLookupSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradeSystemLookupSession.CanLookupGradeSystems = {
  methodName: "CanLookupGradeSystems",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanLookupGradeSystemsRequest,
  responseType: dlkit_proto_grading_pb.CanLookupGradeSystemsReply
};
GradeSystemLookupSession.UseComparativeGradeSystemView = {
  methodName: "UseComparativeGradeSystemView",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradeSystemViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradeSystemViewReply
};
GradeSystemLookupSession.UsePlenaryGradeSystemView = {
  methodName: "UsePlenaryGradeSystemView",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradeSystemViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradeSystemViewReply
};
GradeSystemLookupSession.UseFederatedGradebookView = {
  methodName: "UseFederatedGradebookView",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseFederatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseFederatedGradebookViewReply
};
GradeSystemLookupSession.UseIsolatedGradebookView = {
  methodName: "UseIsolatedGradebookView",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseIsolatedGradebookViewReply
};
GradeSystemLookupSession.GetGradeSystem = {
  methodName: "GetGradeSystem",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.GetGradeSystemReply
};
GradeSystemLookupSession.GetGradeSystemByGrade = {
  methodName: "GetGradeSystemByGrade",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeSystemByGradeRequest,
  responseType: dlkit_proto_grading_pb.GetGradeSystemByGradeReply
};
GradeSystemLookupSession.GetGradeSystemsByIds = {
  methodName: "GetGradeSystemsByIds",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByIdsRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
GradeSystemLookupSession.GetGradeSystemsByGenusType = {
  methodName: "GetGradeSystemsByGenusType",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
GradeSystemLookupSession.GetGradeSystemsByParentGenusType = {
  methodName: "GetGradeSystemsByParentGenusType",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByParentGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
GradeSystemLookupSession.GetGradeSystemsByRecordType = {
  methodName: "GetGradeSystemsByRecordType",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByRecordTypeRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
GradeSystemLookupSession.GetGradeSystems = {
  methodName: "GetGradeSystems",
  service: GradeSystemLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
var GradeSystemQuerySession = {
  serviceName: "dlkit.proto.grading.GradeSystemQuerySession"
};
GradeSystemQuerySession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradeSystemQuerySession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradeSystemQuerySession.CanSearchGradeSystems = {
  methodName: "CanSearchGradeSystems",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanSearchGradeSystemsRequest,
  responseType: dlkit_proto_grading_pb.CanSearchGradeSystemsReply
};
GradeSystemQuerySession.UseFederatedGradebookView = {
  methodName: "UseFederatedGradebookView",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseFederatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseFederatedGradebookViewReply
};
GradeSystemQuerySession.UseIsolatedGradebookView = {
  methodName: "UseIsolatedGradebookView",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseIsolatedGradebookViewReply
};
GradeSystemQuerySession.GetGradeSystemQuery = {
  methodName: "GetGradeSystemQuery",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeSystemQueryRequest,
  responseType: dlkit_proto_grading_pb.GetGradeSystemQueryReply
};
GradeSystemQuerySession.GetGradeSystemsByQuery = {
  methodName: "GetGradeSystemsByQuery",
  service: GradeSystemQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByQueryRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
var GradeSystemAdminSession = {
  serviceName: "dlkit.proto.grading.GradeSystemAdminSession"
};
GradeSystemAdminSession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradeSystemAdminSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradeSystemAdminSession.CanCreateGradeSystems = {
  methodName: "CanCreateGradeSystems",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradeSystemsRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradeSystemsReply
};
GradeSystemAdminSession.CanCreateGradeSystemWithRecordTypes = {
  methodName: "CanCreateGradeSystemWithRecordTypes",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradeSystemWithRecordTypesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradeSystemWithRecordTypesReply
};
GradeSystemAdminSession.GetGradeSystemFormForCreate = {
  methodName: "GetGradeSystemFormForCreate",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeSystemFormForCreateRequest,
  responseType: dlkit_proto_grading_pb.GetGradeSystemFormForCreateReply
};
GradeSystemAdminSession.CreateGradeSystem = {
  methodName: "CreateGradeSystem",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CreateGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.CreateGradeSystemReply
};
GradeSystemAdminSession.CanUpdateGradeSystems = {
  methodName: "CanUpdateGradeSystems",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanUpdateGradeSystemsRequest,
  responseType: dlkit_proto_grading_pb.CanUpdateGradeSystemsReply
};
GradeSystemAdminSession.GetGradeSystemFormForUpdate = {
  methodName: "GetGradeSystemFormForUpdate",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeSystemFormForUpdateRequest,
  responseType: dlkit_proto_grading_pb.GetGradeSystemFormForUpdateReply
};
GradeSystemAdminSession.UpdateGradeSystem = {
  methodName: "UpdateGradeSystem",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UpdateGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.UpdateGradeSystemReply
};
GradeSystemAdminSession.CanDeleteGradeSystems = {
  methodName: "CanDeleteGradeSystems",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanDeleteGradeSystemsRequest,
  responseType: dlkit_proto_grading_pb.CanDeleteGradeSystemsReply
};
GradeSystemAdminSession.DeleteGradeSystem = {
  methodName: "DeleteGradeSystem",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.DeleteGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.DeleteGradeSystemReply
};
GradeSystemAdminSession.CanManageGradeSystemAliases = {
  methodName: "CanManageGradeSystemAliases",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanManageGradeSystemAliasesRequest,
  responseType: dlkit_proto_grading_pb.CanManageGradeSystemAliasesReply
};
GradeSystemAdminSession.AliasGradeSystem = {
  methodName: "AliasGradeSystem",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AliasGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.AliasGradeSystemReply
};
GradeSystemAdminSession.CanCreateGrades = {
  methodName: "CanCreateGrades",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradesReply
};
GradeSystemAdminSession.CanCreateGradeWithRecordTypes = {
  methodName: "CanCreateGradeWithRecordTypes",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradeWithRecordTypesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradeWithRecordTypesReply
};
GradeSystemAdminSession.GetGradeFormForCreate = {
  methodName: "GetGradeFormForCreate",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeFormForCreateRequest,
  responseType: dlkit_proto_grading_pb.GetGradeFormForCreateReply
};
GradeSystemAdminSession.CreateGrade = {
  methodName: "CreateGrade",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CreateGradeRequest,
  responseType: dlkit_proto_grading_pb.CreateGradeReply
};
GradeSystemAdminSession.CanUpdateGrades = {
  methodName: "CanUpdateGrades",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanUpdateGradesRequest,
  responseType: dlkit_proto_grading_pb.CanUpdateGradesReply
};
GradeSystemAdminSession.GetGradeFormForUpdate = {
  methodName: "GetGradeFormForUpdate",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeFormForUpdateRequest,
  responseType: dlkit_proto_grading_pb.GetGradeFormForUpdateReply
};
GradeSystemAdminSession.UpdateGrade = {
  methodName: "UpdateGrade",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UpdateGradeRequest,
  responseType: dlkit_proto_grading_pb.UpdateGradeReply
};
GradeSystemAdminSession.CanDeleteGrades = {
  methodName: "CanDeleteGrades",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanDeleteGradesRequest,
  responseType: dlkit_proto_grading_pb.CanDeleteGradesReply
};
GradeSystemAdminSession.DeleteGrade = {
  methodName: "DeleteGrade",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.DeleteGradeRequest,
  responseType: dlkit_proto_grading_pb.DeleteGradeReply
};
GradeSystemAdminSession.CanManageGradeAliases = {
  methodName: "CanManageGradeAliases",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanManageGradeAliasesRequest,
  responseType: dlkit_proto_grading_pb.CanManageGradeAliasesReply
};
GradeSystemAdminSession.AliasGrade = {
  methodName: "AliasGrade",
  service: GradeSystemAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AliasGradeRequest,
  responseType: dlkit_proto_grading_pb.AliasGradeReply
};
var GradeSystemGradebookSession = {
  serviceName: "dlkit.proto.grading.GradeSystemGradebookSession"
};
GradeSystemGradebookSession.UseComparativeGradebookView = {
  methodName: "UseComparativeGradebookView",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradebookViewReply
};
GradeSystemGradebookSession.UsePlenaryGradebookView = {
  methodName: "UsePlenaryGradebookView",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradebookViewReply
};
GradeSystemGradebookSession.CanLookupGradeSystemGradebookMappings = {
  methodName: "CanLookupGradeSystemGradebookMappings",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanLookupGradeSystemGradebookMappingsRequest,
  responseType: dlkit_proto_grading_pb.CanLookupGradeSystemGradebookMappingsReply
};
GradeSystemGradebookSession.GetGradeSystemIdsByGradebook = {
  methodName: "GetGradeSystemIdsByGradebook",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemIdsByGradebookRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradeSystemGradebookSession.GetGradeSystemsByGradebook = {
  methodName: "GetGradeSystemsByGradebook",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByGradebookRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
GradeSystemGradebookSession.GetGradeSystemIdsByGradebooks = {
  methodName: "GetGradeSystemIdsByGradebooks",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemIdsByGradebooksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradeSystemGradebookSession.GetGradeSystemsByGradebooks = {
  methodName: "GetGradeSystemsByGradebooks",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeSystemsByGradebooksRequest,
  responseType: dlkit_proto_grading_pb.GradeSystem
};
GradeSystemGradebookSession.GetGradebookIdsByGradeSystem = {
  methodName: "GetGradebookIdsByGradeSystem",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookIdsByGradeSystemRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradeSystemGradebookSession.GetGradebooksByGradeSystem = {
  methodName: "GetGradebooksByGradeSystem",
  service: GradeSystemGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
var GradeSystemGradebookAssignmentSession = {
  serviceName: "dlkit.proto.grading.GradeSystemGradebookAssignmentSession"
};
GradeSystemGradebookAssignmentSession.CanAssignGradeSystem = {
  methodName: "CanAssignGradeSystem",
  service: GradeSystemGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanAssignGradeSystemRequest,
  responseType: dlkit_proto_grading_pb.CanAssignGradeSystemReply
};
GradeSystemGradebookAssignmentSession.CanAssignGradeSystemsToGradebook = {
  methodName: "CanAssignGradeSystemsToGradebook",
  service: GradeSystemGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanAssignGradeSystemsToGradebookRequest,
  responseType: dlkit_proto_grading_pb.CanAssignGradeSystemsToGradebookReply
};
GradeSystemGradebookAssignmentSession.GetAssignableGradebookIds = {
  methodName: "GetAssignableGradebookIds",
  service: GradeSystemGradebookAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetAssignableGradebookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradeSystemGradebookAssignmentSession.GetAssignableGradebookIdsForGradeSystem = {
  methodName: "GetAssignableGradebookIdsForGradeSystem",
  service: GradeSystemGradebookAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetAssignableGradebookIdsForGradeSystemRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradeSystemGradebookAssignmentSession.AssignGradeSystemToGradebook = {
  methodName: "AssignGradeSystemToGradebook",
  service: GradeSystemGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AssignGradeSystemToGradebookRequest,
  responseType: dlkit_proto_grading_pb.AssignGradeSystemToGradebookReply
};
GradeSystemGradebookAssignmentSession.UnassignGradeSystemFromGradebook = {
  methodName: "UnassignGradeSystemFromGradebook",
  service: GradeSystemGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UnassignGradeSystemFromGradebookRequest,
  responseType: dlkit_proto_grading_pb.UnassignGradeSystemFromGradebookReply
};
var GradeEntryLookupSession = {
  serviceName: "dlkit.proto.grading.GradeEntryLookupSession"
};
GradeEntryLookupSession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradeEntryLookupSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradeEntryLookupSession.CanLookupGradeEntries = {
  methodName: "CanLookupGradeEntries",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanLookupGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.CanLookupGradeEntriesReply
};
GradeEntryLookupSession.UseComparativeGradeEntryView = {
  methodName: "UseComparativeGradeEntryView",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradeEntryViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradeEntryViewReply
};
GradeEntryLookupSession.UsePlenaryGradeEntryView = {
  methodName: "UsePlenaryGradeEntryView",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradeEntryViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradeEntryViewReply
};
GradeEntryLookupSession.UseFederatedGradebookView = {
  methodName: "UseFederatedGradebookView",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseFederatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseFederatedGradebookViewReply
};
GradeEntryLookupSession.UseIsolatedGradebookView = {
  methodName: "UseIsolatedGradebookView",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseIsolatedGradebookViewReply
};
GradeEntryLookupSession.UseEffectiveGradeEntryView = {
  methodName: "UseEffectiveGradeEntryView",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseEffectiveGradeEntryViewRequest,
  responseType: dlkit_proto_grading_pb.UseEffectiveGradeEntryViewReply
};
GradeEntryLookupSession.UseAnyEffectiveGradeEntryView = {
  methodName: "UseAnyEffectiveGradeEntryView",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseAnyEffectiveGradeEntryViewRequest,
  responseType: dlkit_proto_grading_pb.UseAnyEffectiveGradeEntryViewReply
};
GradeEntryLookupSession.GetGradeEntry = {
  methodName: "GetGradeEntry",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeEntryRequest,
  responseType: dlkit_proto_grading_pb.GetGradeEntryReply
};
GradeEntryLookupSession.GetGradeEntriesByIds = {
  methodName: "GetGradeEntriesByIds",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesByIdsRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesByGenusType = {
  methodName: "GetGradeEntriesByGenusType",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesByGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesByParentGenusType = {
  methodName: "GetGradeEntriesByParentGenusType",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesByParentGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesByRecordType = {
  methodName: "GetGradeEntriesByRecordType",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesByRecordTypeRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesOnDate = {
  methodName: "GetGradeEntriesOnDate",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesOnDateRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesForGradebookColumn = {
  methodName: "GetGradeEntriesForGradebookColumn",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesForGradebookColumnOnDate = {
  methodName: "GetGradeEntriesForGradebookColumnOnDate",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnOnDateRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesForResource = {
  methodName: "GetGradeEntriesForResource",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesForResourceRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesForResourceOnDate = {
  methodName: "GetGradeEntriesForResourceOnDate",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesForResourceOnDateRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesForGradebookColumnAndResource = {
  methodName: "GetGradeEntriesForGradebookColumnAndResource",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnAndResourceRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesForGradebookColumnAndResourceOnDate = {
  methodName: "GetGradeEntriesForGradebookColumnAndResourceOnDate",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnAndResourceOnDateRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntriesByGrader = {
  methodName: "GetGradeEntriesByGrader",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesByGraderRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
GradeEntryLookupSession.GetGradeEntries = {
  methodName: "GetGradeEntries",
  service: GradeEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
var GradeEntryQuerySession = {
  serviceName: "dlkit.proto.grading.GradeEntryQuerySession"
};
GradeEntryQuerySession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradeEntryQuerySession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradeEntryQuerySession.CanSearchGradeEntries = {
  methodName: "CanSearchGradeEntries",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanSearchGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.CanSearchGradeEntriesReply
};
GradeEntryQuerySession.UseFederatedGradebookView = {
  methodName: "UseFederatedGradebookView",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseFederatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseFederatedGradebookViewReply
};
GradeEntryQuerySession.UseIsolatedGradebookView = {
  methodName: "UseIsolatedGradebookView",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseIsolatedGradebookViewReply
};
GradeEntryQuerySession.GetGradeEntryQuery = {
  methodName: "GetGradeEntryQuery",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeEntryQueryRequest,
  responseType: dlkit_proto_grading_pb.GetGradeEntryQueryReply
};
GradeEntryQuerySession.GetGradeEntriesByQuery = {
  methodName: "GetGradeEntriesByQuery",
  service: GradeEntryQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradeEntriesByQueryRequest,
  responseType: dlkit_proto_grading_pb.GradeEntry
};
var GradeEntryAdminSession = {
  serviceName: "dlkit.proto.grading.GradeEntryAdminSession"
};
GradeEntryAdminSession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradeEntryAdminSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradeEntryAdminSession.CanCreateGradeEntries = {
  methodName: "CanCreateGradeEntries",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradeEntriesReply
};
GradeEntryAdminSession.CanCreateGradeEntryWithRecordTypes = {
  methodName: "CanCreateGradeEntryWithRecordTypes",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradeEntryWithRecordTypesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradeEntryWithRecordTypesReply
};
GradeEntryAdminSession.GetGradeEntryFormForCreate = {
  methodName: "GetGradeEntryFormForCreate",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeEntryFormForCreateRequest,
  responseType: dlkit_proto_grading_pb.GetGradeEntryFormForCreateReply
};
GradeEntryAdminSession.CreateGradeEntry = {
  methodName: "CreateGradeEntry",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CreateGradeEntryRequest,
  responseType: dlkit_proto_grading_pb.CreateGradeEntryReply
};
GradeEntryAdminSession.CanOverridecalculatedGradeEntries = {
  methodName: "CanOverridecalculatedGradeEntries",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanOverridecalculatedGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.CanOverridecalculatedGradeEntriesReply
};
GradeEntryAdminSession.GetGradeEntryFormForOverride = {
  methodName: "GetGradeEntryFormForOverride",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeEntryFormForOverrideRequest,
  responseType: dlkit_proto_grading_pb.GetGradeEntryFormForOverrideReply
};
GradeEntryAdminSession.OverrideCalculatedGradeEntry = {
  methodName: "OverrideCalculatedGradeEntry",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.OverrideCalculatedGradeEntryRequest,
  responseType: dlkit_proto_grading_pb.OverrideCalculatedGradeEntryReply
};
GradeEntryAdminSession.CanUpdateGradeEntries = {
  methodName: "CanUpdateGradeEntries",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanUpdateGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.CanUpdateGradeEntriesReply
};
GradeEntryAdminSession.GetGradeEntryFormForUpdate = {
  methodName: "GetGradeEntryFormForUpdate",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradeEntryFormForUpdateRequest,
  responseType: dlkit_proto_grading_pb.GetGradeEntryFormForUpdateReply
};
GradeEntryAdminSession.UpdateGradeEntry = {
  methodName: "UpdateGradeEntry",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UpdateGradeEntryRequest,
  responseType: dlkit_proto_grading_pb.UpdateGradeEntryReply
};
GradeEntryAdminSession.CanDeleteGradeEntries = {
  methodName: "CanDeleteGradeEntries",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanDeleteGradeEntriesRequest,
  responseType: dlkit_proto_grading_pb.CanDeleteGradeEntriesReply
};
GradeEntryAdminSession.DeleteGradeEntry = {
  methodName: "DeleteGradeEntry",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.DeleteGradeEntryRequest,
  responseType: dlkit_proto_grading_pb.DeleteGradeEntryReply
};
GradeEntryAdminSession.CanManageGradeEntryAliases = {
  methodName: "CanManageGradeEntryAliases",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanManageGradeEntryAliasesRequest,
  responseType: dlkit_proto_grading_pb.CanManageGradeEntryAliasesReply
};
GradeEntryAdminSession.AliasGradeEntry = {
  methodName: "AliasGradeEntry",
  service: GradeEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AliasGradeEntryRequest,
  responseType: dlkit_proto_grading_pb.AliasGradeEntryReply
};
var GradebookColumnLookupSession = {
  serviceName: "dlkit.proto.grading.GradebookColumnLookupSession"
};
GradebookColumnLookupSession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradebookColumnLookupSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradebookColumnLookupSession.CanLookupGradebookColumns = {
  methodName: "CanLookupGradebookColumns",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanLookupGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.CanLookupGradebookColumnsReply
};
GradebookColumnLookupSession.UseComparativeGradebookColumnView = {
  methodName: "UseComparativeGradebookColumnView",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradebookColumnViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradebookColumnViewReply
};
GradebookColumnLookupSession.UsePlenaryGradebookColumnView = {
  methodName: "UsePlenaryGradebookColumnView",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradebookColumnViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradebookColumnViewReply
};
GradebookColumnLookupSession.UseFederatedGradebookView = {
  methodName: "UseFederatedGradebookView",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseFederatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseFederatedGradebookViewReply
};
GradebookColumnLookupSession.UseIsolatedGradebookView = {
  methodName: "UseIsolatedGradebookView",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseIsolatedGradebookViewReply
};
GradebookColumnLookupSession.GetGradebookColumn = {
  methodName: "GetGradebookColumn",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookColumnReply
};
GradebookColumnLookupSession.GetGradebookColumnsByIds = {
  methodName: "GetGradebookColumnsByIds",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByIdsRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnLookupSession.GetGradebookColumnsByGenusType = {
  methodName: "GetGradebookColumnsByGenusType",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnLookupSession.GetGradebookColumnsByParentGenusType = {
  methodName: "GetGradebookColumnsByParentGenusType",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByParentGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnLookupSession.GetGradebookColumnsByRecordType = {
  methodName: "GetGradebookColumnsByRecordType",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByRecordTypeRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnLookupSession.GetGradebookColumns = {
  methodName: "GetGradebookColumns",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnLookupSession.SupportsSummary = {
  methodName: "SupportsSummary",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.SupportsSummaryRequest,
  responseType: dlkit_proto_grading_pb.SupportsSummaryReply
};
GradebookColumnLookupSession.GetGradebookColumnSummary = {
  methodName: "GetGradebookColumnSummary",
  service: GradebookColumnLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnSummaryRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookColumnSummaryReply
};
var GradebookColumnQuerySession = {
  serviceName: "dlkit.proto.grading.GradebookColumnQuerySession"
};
GradebookColumnQuerySession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradebookColumnQuerySession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradebookColumnQuerySession.CanSearchGradebookColumns = {
  methodName: "CanSearchGradebookColumns",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanSearchGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.CanSearchGradebookColumnsReply
};
GradebookColumnQuerySession.UseFederatedGradebookView = {
  methodName: "UseFederatedGradebookView",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseFederatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseFederatedGradebookViewReply
};
GradebookColumnQuerySession.UseIsolatedGradebookView = {
  methodName: "UseIsolatedGradebookView",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseIsolatedGradebookViewReply
};
GradebookColumnQuerySession.GetGradebookColumnQuery = {
  methodName: "GetGradebookColumnQuery",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnQueryRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookColumnQueryReply
};
GradebookColumnQuerySession.GetGradebookColumnsByQuery = {
  methodName: "GetGradebookColumnsByQuery",
  service: GradebookColumnQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByQueryRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
var GradebookColumnAdminSession = {
  serviceName: "dlkit.proto.grading.GradebookColumnAdminSession"
};
GradebookColumnAdminSession.GetGradebookId = {
  methodName: "GetGradebookId",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookIdReply
};
GradebookColumnAdminSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradebookColumnAdminSession.CanCreateGradebookColumns = {
  methodName: "CanCreateGradebookColumns",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradebookColumnsReply
};
GradebookColumnAdminSession.CanCreateGradebookColumnWithRecordTypes = {
  methodName: "CanCreateGradebookColumnWithRecordTypes",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradebookColumnWithRecordTypesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradebookColumnWithRecordTypesReply
};
GradebookColumnAdminSession.GetGradebookColumnFormForCreate = {
  methodName: "GetGradebookColumnFormForCreate",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnFormForCreateRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookColumnFormForCreateReply
};
GradebookColumnAdminSession.CreateGradebookColumn = {
  methodName: "CreateGradebookColumn",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CreateGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.CreateGradebookColumnReply
};
GradebookColumnAdminSession.CanUpdateGradebookColumns = {
  methodName: "CanUpdateGradebookColumns",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanUpdateGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.CanUpdateGradebookColumnsReply
};
GradebookColumnAdminSession.GetGradebookColumnFormForUpdate = {
  methodName: "GetGradebookColumnFormForUpdate",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnFormForUpdateRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookColumnFormForUpdateReply
};
GradebookColumnAdminSession.UpdateGradebookColumn = {
  methodName: "UpdateGradebookColumn",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UpdateGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.UpdateGradebookColumnReply
};
GradebookColumnAdminSession.SequenceGradebookColumns = {
  methodName: "SequenceGradebookColumns",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.SequenceGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.SequenceGradebookColumnsReply
};
GradebookColumnAdminSession.MoveGradebookColumn = {
  methodName: "MoveGradebookColumn",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.MoveGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.MoveGradebookColumnReply
};
GradebookColumnAdminSession.CopyGradebookColumnEntries = {
  methodName: "CopyGradebookColumnEntries",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CopyGradebookColumnEntriesRequest,
  responseType: dlkit_proto_grading_pb.CopyGradebookColumnEntriesReply
};
GradebookColumnAdminSession.CanDeleteGradebookColumns = {
  methodName: "CanDeleteGradebookColumns",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanDeleteGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.CanDeleteGradebookColumnsReply
};
GradebookColumnAdminSession.DeleteGradebookColumn = {
  methodName: "DeleteGradebookColumn",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.DeleteGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.DeleteGradebookColumnReply
};
GradebookColumnAdminSession.CanManageGradebookColumnAliases = {
  methodName: "CanManageGradebookColumnAliases",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanManageGradebookColumnAliasesRequest,
  responseType: dlkit_proto_grading_pb.CanManageGradebookColumnAliasesReply
};
GradebookColumnAdminSession.AliasGradebookColumn = {
  methodName: "AliasGradebookColumn",
  service: GradebookColumnAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AliasGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.AliasGradebookColumnReply
};
var GradebookColumnGradebookSession = {
  serviceName: "dlkit.proto.grading.GradebookColumnGradebookSession"
};
GradebookColumnGradebookSession.UseComparativeGradebookView = {
  methodName: "UseComparativeGradebookView",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradebookViewReply
};
GradebookColumnGradebookSession.UsePlenaryGradebookView = {
  methodName: "UsePlenaryGradebookView",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradebookViewReply
};
GradebookColumnGradebookSession.CanLookupGradebookColumnGradebookMappings = {
  methodName: "CanLookupGradebookColumnGradebookMappings",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanLookupGradebookColumnGradebookMappingsRequest,
  responseType: dlkit_proto_grading_pb.CanLookupGradebookColumnGradebookMappingsReply
};
GradebookColumnGradebookSession.GetGradebookColumnIdsByGradebook = {
  methodName: "GetGradebookColumnIdsByGradebook",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnIdsByGradebookRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookColumnGradebookSession.GetGradebookColumnsByGradebook = {
  methodName: "GetGradebookColumnsByGradebook",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByGradebookRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnGradebookSession.GetGradebookColumnIdsByGradebooks = {
  methodName: "GetGradebookColumnIdsByGradebooks",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnIdsByGradebooksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookColumnGradebookSession.GetGradebookColumnsByGradebooks = {
  methodName: "GetGradebookColumnsByGradebooks",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookColumnsByGradebooksRequest,
  responseType: dlkit_proto_grading_pb.GradebookColumn
};
GradebookColumnGradebookSession.GetGradebookIdsByGradebookColumn = {
  methodName: "GetGradebookIdsByGradebookColumn",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebookIdsByGradebookColumnRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookColumnGradebookSession.GetGradebooksByGradebookColumn = {
  methodName: "GetGradebooksByGradebookColumn",
  service: GradebookColumnGradebookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByGradebookColumnRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
var GradebookColumnGradebookAssignmentSession = {
  serviceName: "dlkit.proto.grading.GradebookColumnGradebookAssignmentSession"
};
GradebookColumnGradebookAssignmentSession.CanAssignGradebookColumns = {
  methodName: "CanAssignGradebookColumns",
  service: GradebookColumnGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanAssignGradebookColumnsRequest,
  responseType: dlkit_proto_grading_pb.CanAssignGradebookColumnsReply
};
GradebookColumnGradebookAssignmentSession.CanAssignGradebookColumnsToGradebook = {
  methodName: "CanAssignGradebookColumnsToGradebook",
  service: GradebookColumnGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanAssignGradebookColumnsToGradebookRequest,
  responseType: dlkit_proto_grading_pb.CanAssignGradebookColumnsToGradebookReply
};
GradebookColumnGradebookAssignmentSession.GetAssignableGradebookIds = {
  methodName: "GetAssignableGradebookIds",
  service: GradebookColumnGradebookAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetAssignableGradebookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookColumnGradebookAssignmentSession.GetAssignableGradebookIdsForGradebookColumn = {
  methodName: "GetAssignableGradebookIdsForGradebookColumn",
  service: GradebookColumnGradebookAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetAssignableGradebookIdsForGradebookColumnRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookColumnGradebookAssignmentSession.AssignGradebookColumnToGradebook = {
  methodName: "AssignGradebookColumnToGradebook",
  service: GradebookColumnGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AssignGradebookColumnToGradebookRequest,
  responseType: dlkit_proto_grading_pb.AssignGradebookColumnToGradebookReply
};
GradebookColumnGradebookAssignmentSession.UnassignGradebookColumnFromGradebook = {
  methodName: "UnassignGradebookColumnFromGradebook",
  service: GradebookColumnGradebookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UnassignGradebookColumnFromGradebookRequest,
  responseType: dlkit_proto_grading_pb.UnassignGradebookColumnFromGradebookReply
};
var GradebookLookupSession = {
  serviceName: "dlkit.proto.grading.GradebookLookupSession"
};
GradebookLookupSession.CanLookupGradebooks = {
  methodName: "CanLookupGradebooks",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanLookupGradebooksRequest,
  responseType: dlkit_proto_grading_pb.CanLookupGradebooksReply
};
GradebookLookupSession.UseComparativeGradebookView = {
  methodName: "UseComparativeGradebookView",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradebookViewReply
};
GradebookLookupSession.UsePlenaryGradebookView = {
  methodName: "UsePlenaryGradebookView",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradebookViewReply
};
GradebookLookupSession.GetGradebook = {
  methodName: "GetGradebook",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookReply
};
GradebookLookupSession.GetGradebooksByIds = {
  methodName: "GetGradebooksByIds",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByIdsRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookLookupSession.GetGradebooksByGenusType = {
  methodName: "GetGradebooksByGenusType",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookLookupSession.GetGradebooksByParentGenusType = {
  methodName: "GetGradebooksByParentGenusType",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByParentGenusTypeRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookLookupSession.GetGradebooksByRecordType = {
  methodName: "GetGradebooksByRecordType",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByRecordTypeRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookLookupSession.GetGradebooksByProvider = {
  methodName: "GetGradebooksByProvider",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksByProviderRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookLookupSession.GetGradebooks = {
  methodName: "GetGradebooks",
  service: GradebookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetGradebooksRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
var GradebookAdminSession = {
  serviceName: "dlkit.proto.grading.GradebookAdminSession"
};
GradebookAdminSession.CanCreateGradebooks = {
  methodName: "CanCreateGradebooks",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradebooksRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradebooksReply
};
GradebookAdminSession.CanCreateGradebookWithRecordTypes = {
  methodName: "CanCreateGradebookWithRecordTypes",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanCreateGradebookWithRecordTypesRequest,
  responseType: dlkit_proto_grading_pb.CanCreateGradebookWithRecordTypesReply
};
GradebookAdminSession.GetGradebookFormForCreate = {
  methodName: "GetGradebookFormForCreate",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookFormForCreateRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookFormForCreateReply
};
GradebookAdminSession.CreateGradebook = {
  methodName: "CreateGradebook",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CreateGradebookRequest,
  responseType: dlkit_proto_grading_pb.CreateGradebookReply
};
GradebookAdminSession.CanUpdateGradebooks = {
  methodName: "CanUpdateGradebooks",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanUpdateGradebooksRequest,
  responseType: dlkit_proto_grading_pb.CanUpdateGradebooksReply
};
GradebookAdminSession.GetGradebookFormForUpdate = {
  methodName: "GetGradebookFormForUpdate",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookFormForUpdateRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookFormForUpdateReply
};
GradebookAdminSession.UpdateGradebook = {
  methodName: "UpdateGradebook",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UpdateGradebookRequest,
  responseType: dlkit_proto_grading_pb.UpdateGradebookReply
};
GradebookAdminSession.CanDeleteGradebooks = {
  methodName: "CanDeleteGradebooks",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanDeleteGradebooksRequest,
  responseType: dlkit_proto_grading_pb.CanDeleteGradebooksReply
};
GradebookAdminSession.DeleteGradebook = {
  methodName: "DeleteGradebook",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.DeleteGradebookRequest,
  responseType: dlkit_proto_grading_pb.DeleteGradebookReply
};
GradebookAdminSession.CanManageGradebookAliases = {
  methodName: "CanManageGradebookAliases",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanManageGradebookAliasesRequest,
  responseType: dlkit_proto_grading_pb.CanManageGradebookAliasesReply
};
GradebookAdminSession.AliasGradebook = {
  methodName: "AliasGradebook",
  service: GradebookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AliasGradebookRequest,
  responseType: dlkit_proto_grading_pb.AliasGradebookReply
};
var GradebookHierarchySession = {
  serviceName: "dlkit.proto.grading.GradebookHierarchySession"
};
GradebookHierarchySession.GetGradebookHierarchyId = {
  methodName: "GetGradebookHierarchyId",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookHierarchyIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookHierarchyIdReply
};
GradebookHierarchySession.GetGradebookHierarchy = {
  methodName: "GetGradebookHierarchy",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookHierarchyRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookHierarchyReply
};
GradebookHierarchySession.CanAccessGradebookHierarchy = {
  methodName: "CanAccessGradebookHierarchy",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanAccessGradebookHierarchyRequest,
  responseType: dlkit_proto_grading_pb.CanAccessGradebookHierarchyReply
};
GradebookHierarchySession.UseComparativeGradebookView = {
  methodName: "UseComparativeGradebookView",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UseComparativeGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UseComparativeGradebookViewReply
};
GradebookHierarchySession.UsePlenaryGradebookView = {
  methodName: "UsePlenaryGradebookView",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest,
  responseType: dlkit_proto_grading_pb.UsePlenaryGradebookViewReply
};
GradebookHierarchySession.GetRootGradebookIds = {
  methodName: "GetRootGradebookIds",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetRootGradebookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookHierarchySession.GetRootGradebooks = {
  methodName: "GetRootGradebooks",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetRootGradebooksRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookHierarchySession.HasParentGradebooks = {
  methodName: "HasParentGradebooks",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.HasParentGradebooksRequest,
  responseType: dlkit_proto_grading_pb.HasParentGradebooksReply
};
GradebookHierarchySession.IsParentOfGradebook = {
  methodName: "IsParentOfGradebook",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.IsParentOfGradebookRequest,
  responseType: dlkit_proto_grading_pb.IsParentOfGradebookReply
};
GradebookHierarchySession.GetParentGradebookIds = {
  methodName: "GetParentGradebookIds",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetParentGradebookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookHierarchySession.GetParentGradebooks = {
  methodName: "GetParentGradebooks",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetParentGradebooksRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookHierarchySession.IsAncestorOfGradebook = {
  methodName: "IsAncestorOfGradebook",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.IsAncestorOfGradebookRequest,
  responseType: dlkit_proto_grading_pb.IsAncestorOfGradebookReply
};
GradebookHierarchySession.HasChildGradebooks = {
  methodName: "HasChildGradebooks",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.HasChildGradebooksRequest,
  responseType: dlkit_proto_grading_pb.HasChildGradebooksReply
};
GradebookHierarchySession.IsChildOfGradebook = {
  methodName: "IsChildOfGradebook",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.IsChildOfGradebookRequest,
  responseType: dlkit_proto_grading_pb.IsChildOfGradebookReply
};
GradebookHierarchySession.GetChildGradebookIds = {
  methodName: "GetChildGradebookIds",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetChildGradebookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
GradebookHierarchySession.GetChildGradebooks = {
  methodName: "GetChildGradebooks",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_grading_pb.GetChildGradebooksRequest,
  responseType: dlkit_proto_grading_pb.Gradebook
};
GradebookHierarchySession.IsDescendantOfGradebook = {
  methodName: "IsDescendantOfGradebook",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.IsDescendantOfGradebookRequest,
  responseType: dlkit_proto_grading_pb.IsDescendantOfGradebookReply
};
GradebookHierarchySession.GetGradebookNodeIds = {
  methodName: "GetGradebookNodeIds",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookNodeIdsRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookNodeIdsReply
};
GradebookHierarchySession.GetGradebookNodes = {
  methodName: "GetGradebookNodes",
  service: GradebookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookNodesRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookNodesReply
};
var GradebookHierarchyDesignSession = {
  serviceName: "dlkit.proto.grading.GradebookHierarchyDesignSession"
};
GradebookHierarchyDesignSession.GetGradebookHierarchyId = {
  methodName: "GetGradebookHierarchyId",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookHierarchyIdRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookHierarchyIdReply
};
GradebookHierarchyDesignSession.GetGradebookHierarchy = {
  methodName: "GetGradebookHierarchy",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.GetGradebookHierarchyRequest,
  responseType: dlkit_proto_grading_pb.GetGradebookHierarchyReply
};
GradebookHierarchyDesignSession.CanModifyGradebookHierarchy = {
  methodName: "CanModifyGradebookHierarchy",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.CanModifyGradebookHierarchyRequest,
  responseType: dlkit_proto_grading_pb.CanModifyGradebookHierarchyReply
};
GradebookHierarchyDesignSession.AddRootGradebook = {
  methodName: "AddRootGradebook",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AddRootGradebookRequest,
  responseType: dlkit_proto_grading_pb.AddRootGradebookReply
};
GradebookHierarchyDesignSession.RemoveRootGradebook = {
  methodName: "RemoveRootGradebook",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.RemoveRootGradebookRequest,
  responseType: dlkit_proto_grading_pb.RemoveRootGradebookReply
};
GradebookHierarchyDesignSession.AddChildGradebook = {
  methodName: "AddChildGradebook",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.AddChildGradebookRequest,
  responseType: dlkit_proto_grading_pb.AddChildGradebookReply
};
GradebookHierarchyDesignSession.RemoveChildGradebook = {
  methodName: "RemoveChildGradebook",
  service: GradebookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_grading_pb.RemoveChildGradebookRequest,
  responseType: dlkit_proto_grading_pb.RemoveChildGradebookReply
};
module.exports = {
  GradeSystemLookupSession: GradeSystemLookupSession,
  GradeSystemQuerySession: GradeSystemQuerySession,
  GradeSystemAdminSession: GradeSystemAdminSession,
  GradeSystemGradebookSession: GradeSystemGradebookSession,
  GradeSystemGradebookAssignmentSession: GradeSystemGradebookAssignmentSession,
  GradeEntryLookupSession: GradeEntryLookupSession,
  GradeEntryQuerySession: GradeEntryQuerySession,
  GradeEntryAdminSession: GradeEntryAdminSession,
  GradebookColumnLookupSession: GradebookColumnLookupSession,
  GradebookColumnQuerySession: GradebookColumnQuerySession,
  GradebookColumnAdminSession: GradebookColumnAdminSession,
  GradebookColumnGradebookSession: GradebookColumnGradebookSession,
  GradebookColumnGradebookAssignmentSession: GradebookColumnGradebookAssignmentSession,
  GradebookLookupSession: GradebookLookupSession,
  GradebookAdminSession: GradebookAdminSession,
  GradebookHierarchySession: GradebookHierarchySession,
  GradebookHierarchyDesignSession: GradebookHierarchyDesignSession,
};

