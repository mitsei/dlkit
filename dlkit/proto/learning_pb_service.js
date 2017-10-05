// package: dlkit.proto.learning
// file: dlkit/proto/learning.proto

var jspb = require("google-protobuf");
var dlkit_proto_learning_pb = require("../../dlkit/proto/learning_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var ObjectiveLookupSession = {
  serviceName: "dlkit.proto.learning.ObjectiveLookupSession"
};
ObjectiveLookupSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ObjectiveLookupSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ObjectiveLookupSession.CanLookupObjectives = {
  methodName: "CanLookupObjectives",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanLookupObjectivesReply
};
ObjectiveLookupSession.UseComparativeObjectiveView = {
  methodName: "UseComparativeObjectiveView",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveViewReply
};
ObjectiveLookupSession.UsePlenaryObjectiveView = {
  methodName: "UsePlenaryObjectiveView",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveViewReply
};
ObjectiveLookupSession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ObjectiveLookupSession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ObjectiveLookupSession.GetObjective = {
  methodName: "GetObjective",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveReply
};
ObjectiveLookupSession.GetObjectivesByIds = {
  methodName: "GetObjectivesByIds",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByIdsRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveLookupSession.GetObjectivesByGenusType = {
  methodName: "GetObjectivesByGenusType",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveLookupSession.GetObjectivesByParentGenusType = {
  methodName: "GetObjectivesByParentGenusType",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByParentGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveLookupSession.GetObjectivesByRecordType = {
  methodName: "GetObjectivesByRecordType",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByRecordTypeRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveLookupSession.GetObjectives = {
  methodName: "GetObjectives",
  service: ObjectiveLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
var ObjectiveQuerySession = {
  serviceName: "dlkit.proto.learning.ObjectiveQuerySession"
};
ObjectiveQuerySession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ObjectiveQuerySession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ObjectiveQuerySession.CanSearchObjectives = {
  methodName: "CanSearchObjectives",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanSearchObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanSearchObjectivesReply
};
ObjectiveQuerySession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ObjectiveQuerySession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ObjectiveQuerySession.GetObjectiveQuery = {
  methodName: "GetObjectiveQuery",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveQueryRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveQueryReply
};
ObjectiveQuerySession.GetObjectivesByQuery = {
  methodName: "GetObjectivesByQuery",
  service: ObjectiveQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByQueryRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
var ObjectiveAdminSession = {
  serviceName: "dlkit.proto.learning.ObjectiveAdminSession"
};
ObjectiveAdminSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ObjectiveAdminSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ObjectiveAdminSession.CanCreateObjectives = {
  methodName: "CanCreateObjectives",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateObjectivesReply
};
ObjectiveAdminSession.CanCreateObjectiveWithRecordTypes = {
  methodName: "CanCreateObjectiveWithRecordTypes",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateObjectiveWithRecordTypesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateObjectiveWithRecordTypesReply
};
ObjectiveAdminSession.GetObjectiveFormForCreate = {
  methodName: "GetObjectiveFormForCreate",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveFormForCreateRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveFormForCreateReply
};
ObjectiveAdminSession.CreateObjective = {
  methodName: "CreateObjective",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CreateObjectiveRequest,
  responseType: dlkit_proto_learning_pb.CreateObjectiveReply
};
ObjectiveAdminSession.CanUpdateObjectives = {
  methodName: "CanUpdateObjectives",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanUpdateObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanUpdateObjectivesReply
};
ObjectiveAdminSession.GetObjectiveFormForUpdate = {
  methodName: "GetObjectiveFormForUpdate",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveFormForUpdateRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveFormForUpdateReply
};
ObjectiveAdminSession.UpdateObjective = {
  methodName: "UpdateObjective",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UpdateObjectiveRequest,
  responseType: dlkit_proto_learning_pb.UpdateObjectiveReply
};
ObjectiveAdminSession.CanDeleteObjectives = {
  methodName: "CanDeleteObjectives",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanDeleteObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanDeleteObjectivesReply
};
ObjectiveAdminSession.DeleteObjective = {
  methodName: "DeleteObjective",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.DeleteObjectiveRequest,
  responseType: dlkit_proto_learning_pb.DeleteObjectiveReply
};
ObjectiveAdminSession.CanManageObjectiveAliases = {
  methodName: "CanManageObjectiveAliases",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanManageObjectiveAliasesRequest,
  responseType: dlkit_proto_learning_pb.CanManageObjectiveAliasesReply
};
ObjectiveAdminSession.AliasObjective = {
  methodName: "AliasObjective",
  service: ObjectiveAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AliasObjectiveRequest,
  responseType: dlkit_proto_learning_pb.AliasObjectiveReply
};
var ObjectiveHierarchySession = {
  serviceName: "dlkit.proto.learning.ObjectiveHierarchySession"
};
ObjectiveHierarchySession.GetObjectiveHierarchyId = {
  methodName: "GetObjectiveHierarchyId",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveHierarchyIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveHierarchyIdReply
};
ObjectiveHierarchySession.GetObjectiveHierarchy = {
  methodName: "GetObjectiveHierarchy",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveHierarchyRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveHierarchyReply
};
ObjectiveHierarchySession.CanAccessObjectiveHierarchy = {
  methodName: "CanAccessObjectiveHierarchy",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAccessObjectiveHierarchyRequest,
  responseType: dlkit_proto_learning_pb.CanAccessObjectiveHierarchyReply
};
ObjectiveHierarchySession.UseComparativeObjectiveView = {
  methodName: "UseComparativeObjectiveView",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveViewReply
};
ObjectiveHierarchySession.UsePlenaryObjectiveView = {
  methodName: "UsePlenaryObjectiveView",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveViewReply
};
ObjectiveHierarchySession.GetRootObjectiveIds = {
  methodName: "GetRootObjectiveIds",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetRootObjectiveIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveHierarchySession.GetRootObjectives = {
  methodName: "GetRootObjectives",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetRootObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveHierarchySession.HasParentObjectives = {
  methodName: "HasParentObjectives",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.HasParentObjectivesRequest,
  responseType: dlkit_proto_learning_pb.HasParentObjectivesReply
};
ObjectiveHierarchySession.IsParentOfObjective = {
  methodName: "IsParentOfObjective",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsParentOfObjectiveRequest,
  responseType: dlkit_proto_learning_pb.IsParentOfObjectiveReply
};
ObjectiveHierarchySession.GetParentObjectiveIds = {
  methodName: "GetParentObjectiveIds",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetParentObjectiveIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveHierarchySession.GetParentObjectives = {
  methodName: "GetParentObjectives",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetParentObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveHierarchySession.IsAncestorOfObjective = {
  methodName: "IsAncestorOfObjective",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsAncestorOfObjectiveRequest,
  responseType: dlkit_proto_learning_pb.IsAncestorOfObjectiveReply
};
ObjectiveHierarchySession.HasChildObjectives = {
  methodName: "HasChildObjectives",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.HasChildObjectivesRequest,
  responseType: dlkit_proto_learning_pb.HasChildObjectivesReply
};
ObjectiveHierarchySession.IsChildOfObjective = {
  methodName: "IsChildOfObjective",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsChildOfObjectiveRequest,
  responseType: dlkit_proto_learning_pb.IsChildOfObjectiveReply
};
ObjectiveHierarchySession.GetChildObjectiveIds = {
  methodName: "GetChildObjectiveIds",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetChildObjectiveIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveHierarchySession.GetChildObjectives = {
  methodName: "GetChildObjectives",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetChildObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveHierarchySession.IsDescendantOfObjective = {
  methodName: "IsDescendantOfObjective",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsDescendantOfObjectiveRequest,
  responseType: dlkit_proto_learning_pb.IsDescendantOfObjectiveReply
};
ObjectiveHierarchySession.GetObjectiveNodeIds = {
  methodName: "GetObjectiveNodeIds",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveNodeIdsRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveNodeIdsReply
};
ObjectiveHierarchySession.GetObjectiveNodes = {
  methodName: "GetObjectiveNodes",
  service: ObjectiveHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveNodesRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveNodesReply
};
var ObjectiveHierarchyDesignSession = {
  serviceName: "dlkit.proto.learning.ObjectiveHierarchyDesignSession"
};
ObjectiveHierarchyDesignSession.GetObjectiveHierarchyId = {
  methodName: "GetObjectiveHierarchyId",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveHierarchyIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveHierarchyIdReply
};
ObjectiveHierarchyDesignSession.GetObjectiveHierarchy = {
  methodName: "GetObjectiveHierarchy",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveHierarchyRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveHierarchyReply
};
ObjectiveHierarchyDesignSession.CanModifyObjectiveHierarchy = {
  methodName: "CanModifyObjectiveHierarchy",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanModifyObjectiveHierarchyRequest,
  responseType: dlkit_proto_learning_pb.CanModifyObjectiveHierarchyReply
};
ObjectiveHierarchyDesignSession.AddRootObjective = {
  methodName: "AddRootObjective",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AddRootObjectiveRequest,
  responseType: dlkit_proto_learning_pb.AddRootObjectiveReply
};
ObjectiveHierarchyDesignSession.RemoveRootObjective = {
  methodName: "RemoveRootObjective",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.RemoveRootObjectiveRequest,
  responseType: dlkit_proto_learning_pb.RemoveRootObjectiveReply
};
ObjectiveHierarchyDesignSession.AddChildObjective = {
  methodName: "AddChildObjective",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AddChildObjectiveRequest,
  responseType: dlkit_proto_learning_pb.AddChildObjectiveReply
};
ObjectiveHierarchyDesignSession.RemoveChildObjective = {
  methodName: "RemoveChildObjective",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.RemoveChildObjectiveRequest,
  responseType: dlkit_proto_learning_pb.RemoveChildObjectiveReply
};
ObjectiveHierarchyDesignSession.RemoveChildObjectives = {
  methodName: "RemoveChildObjectives",
  service: ObjectiveHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.RemoveChildObjectivesRequest,
  responseType: dlkit_proto_learning_pb.RemoveChildObjectivesReply
};
var ObjectiveSequencingSession = {
  serviceName: "dlkit.proto.learning.ObjectiveSequencingSession"
};
ObjectiveSequencingSession.GetObjectiveHierarchyId = {
  methodName: "GetObjectiveHierarchyId",
  service: ObjectiveSequencingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveHierarchyIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveHierarchyIdReply
};
ObjectiveSequencingSession.GetObjectiveHierarchy = {
  methodName: "GetObjectiveHierarchy",
  service: ObjectiveSequencingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveHierarchyRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveHierarchyReply
};
ObjectiveSequencingSession.CanSequenceObjectives = {
  methodName: "CanSequenceObjectives",
  service: ObjectiveSequencingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanSequenceObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanSequenceObjectivesReply
};
ObjectiveSequencingSession.MoveObjectiveAhead = {
  methodName: "MoveObjectiveAhead",
  service: ObjectiveSequencingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.MoveObjectiveAheadRequest,
  responseType: dlkit_proto_learning_pb.MoveObjectiveAheadReply
};
ObjectiveSequencingSession.MoveObjectiveBehind = {
  methodName: "MoveObjectiveBehind",
  service: ObjectiveSequencingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.MoveObjectiveBehindRequest,
  responseType: dlkit_proto_learning_pb.MoveObjectiveBehindReply
};
ObjectiveSequencingSession.SequenceObjectives = {
  methodName: "SequenceObjectives",
  service: ObjectiveSequencingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.SequenceObjectivesRequest,
  responseType: dlkit_proto_learning_pb.SequenceObjectivesReply
};
var ObjectiveObjectiveBankSession = {
  serviceName: "dlkit.proto.learning.ObjectiveObjectiveBankSession"
};
ObjectiveObjectiveBankSession.CanLookupObjectiveObjectiveBankMappings = {
  methodName: "CanLookupObjectiveObjectiveBankMappings",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupObjectiveObjectiveBankMappingsRequest,
  responseType: dlkit_proto_learning_pb.CanLookupObjectiveObjectiveBankMappingsReply
};
ObjectiveObjectiveBankSession.UseComparativeObjectiveBankView = {
  methodName: "UseComparativeObjectiveBankView",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply
};
ObjectiveObjectiveBankSession.UsePlenaryObjectiveBankView = {
  methodName: "UsePlenaryObjectiveBankView",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply
};
ObjectiveObjectiveBankSession.GetObjectiveIdsByObjectiveBank = {
  methodName: "GetObjectiveIdsByObjectiveBank",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveIdsByObjectiveBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveObjectiveBankSession.GetObjectivesByObjectiveBank = {
  methodName: "GetObjectivesByObjectiveBank",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveObjectiveBankSession.GetObjectiveIdsByObjectiveBanks = {
  methodName: "GetObjectiveIdsByObjectiveBanks",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveIdsByObjectiveBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveObjectiveBankSession.GetObjectivesByObjectiveBanks = {
  methodName: "GetObjectivesByObjectiveBanks",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectivesByObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveObjectiveBankSession.GetObjectiveBankIdsByObjective = {
  methodName: "GetObjectiveBankIdsByObjective",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdsByObjectiveRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveObjectiveBankSession.GetObjectiveBanksByObjective = {
  methodName: "GetObjectiveBanksByObjective",
  service: ObjectiveObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByObjectiveRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
var ObjectiveObjectiveBankAssignmentSession = {
  serviceName: "dlkit.proto.learning.ObjectiveObjectiveBankAssignmentSession"
};
ObjectiveObjectiveBankAssignmentSession.CanAssignObjectives = {
  methodName: "CanAssignObjectives",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignObjectivesRequest,
  responseType: dlkit_proto_learning_pb.CanAssignObjectivesReply
};
ObjectiveObjectiveBankAssignmentSession.CanAssignObjectivesToObjectiveBank = {
  methodName: "CanAssignObjectivesToObjectiveBank",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignObjectivesToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.CanAssignObjectivesToObjectiveBankReply
};
ObjectiveObjectiveBankAssignmentSession.GetAssignableObjectiveBankIds = {
  methodName: "GetAssignableObjectiveBankIds",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveObjectiveBankAssignmentSession.GetAssignableObjectiveBankIdsForObjective = {
  methodName: "GetAssignableObjectiveBankIdsForObjective",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsForObjectiveRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveObjectiveBankAssignmentSession.AssignObjectiveToObjectiveBank = {
  methodName: "AssignObjectiveToObjectiveBank",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AssignObjectiveToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.AssignObjectiveToObjectiveBankReply
};
ObjectiveObjectiveBankAssignmentSession.UnassignObjectiveFromObjectiveBank = {
  methodName: "UnassignObjectiveFromObjectiveBank",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UnassignObjectiveFromObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.UnassignObjectiveFromObjectiveBankReply
};
ObjectiveObjectiveBankAssignmentSession.ReassignProficiencyToObjectiveBank = {
  methodName: "ReassignProficiencyToObjectiveBank",
  service: ObjectiveObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankReply
};
var ObjectiveRequisiteSession = {
  serviceName: "dlkit.proto.learning.ObjectiveRequisiteSession"
};
ObjectiveRequisiteSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ObjectiveRequisiteSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ObjectiveRequisiteSession.CanLookupObjectivePrerequisites = {
  methodName: "CanLookupObjectivePrerequisites",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupObjectivePrerequisitesRequest,
  responseType: dlkit_proto_learning_pb.CanLookupObjectivePrerequisitesReply
};
ObjectiveRequisiteSession.UseComparativeObjectiveView = {
  methodName: "UseComparativeObjectiveView",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveViewReply
};
ObjectiveRequisiteSession.UsePlenaryObjectiveView = {
  methodName: "UsePlenaryObjectiveView",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveViewReply
};
ObjectiveRequisiteSession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ObjectiveRequisiteSession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ObjectiveRequisiteSession.GetRequisiteObjectives = {
  methodName: "GetRequisiteObjectives",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetRequisiteObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveRequisiteSession.GetAllRequisiteObjectives = {
  methodName: "GetAllRequisiteObjectives",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAllRequisiteObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveRequisiteSession.GetDependentObjectives = {
  methodName: "GetDependentObjectives",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetDependentObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
ObjectiveRequisiteSession.IsObjectiveRequired = {
  methodName: "IsObjectiveRequired",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsObjectiveRequiredRequest,
  responseType: dlkit_proto_learning_pb.IsObjectiveRequiredReply
};
ObjectiveRequisiteSession.GetEquivalentObjectives = {
  methodName: "GetEquivalentObjectives",
  service: ObjectiveRequisiteSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetEquivalentObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Objective
};
var ObjectiveRequisiteAssignmentSession = {
  serviceName: "dlkit.proto.learning.ObjectiveRequisiteAssignmentSession"
};
ObjectiveRequisiteAssignmentSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ObjectiveRequisiteAssignmentSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ObjectiveRequisiteAssignmentSession.CanAssignRequisites = {
  methodName: "CanAssignRequisites",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignRequisitesRequest,
  responseType: dlkit_proto_learning_pb.CanAssignRequisitesReply
};
ObjectiveRequisiteAssignmentSession.AssignObjectiveRequisite = {
  methodName: "AssignObjectiveRequisite",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AssignObjectiveRequisiteRequest,
  responseType: dlkit_proto_learning_pb.AssignObjectiveRequisiteReply
};
ObjectiveRequisiteAssignmentSession.UnassignObjectiveRequisite = {
  methodName: "UnassignObjectiveRequisite",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UnassignObjectiveRequisiteRequest,
  responseType: dlkit_proto_learning_pb.UnassignObjectiveRequisiteReply
};
ObjectiveRequisiteAssignmentSession.AssignEquivalentObjective = {
  methodName: "AssignEquivalentObjective",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AssignEquivalentObjectiveRequest,
  responseType: dlkit_proto_learning_pb.AssignEquivalentObjectiveReply
};
ObjectiveRequisiteAssignmentSession.UnassignEquivalentObjective = {
  methodName: "UnassignEquivalentObjective",
  service: ObjectiveRequisiteAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UnassignEquivalentObjectiveRequest,
  responseType: dlkit_proto_learning_pb.UnassignEquivalentObjectiveReply
};
var ActivityLookupSession = {
  serviceName: "dlkit.proto.learning.ActivityLookupSession"
};
ActivityLookupSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ActivityLookupSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ActivityLookupSession.CanLookupActivities = {
  methodName: "CanLookupActivities",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupActivitiesRequest,
  responseType: dlkit_proto_learning_pb.CanLookupActivitiesReply
};
ActivityLookupSession.UseComparativeActivityView = {
  methodName: "UseComparativeActivityView",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeActivityViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeActivityViewReply
};
ActivityLookupSession.UsePlenaryActivityView = {
  methodName: "UsePlenaryActivityView",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryActivityViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryActivityViewReply
};
ActivityLookupSession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ActivityLookupSession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ActivityLookupSession.GetActivity = {
  methodName: "GetActivity",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetActivityRequest,
  responseType: dlkit_proto_learning_pb.GetActivityReply
};
ActivityLookupSession.GetActivitiesByIds = {
  methodName: "GetActivitiesByIds",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByIdsRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesByGenusType = {
  methodName: "GetActivitiesByGenusType",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesByParentGenusType = {
  methodName: "GetActivitiesByParentGenusType",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByParentGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesByRecordType = {
  methodName: "GetActivitiesByRecordType",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByRecordTypeRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesForObjective = {
  methodName: "GetActivitiesForObjective",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesForObjectiveRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesForObjectives = {
  methodName: "GetActivitiesForObjectives",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesForObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesByAsset = {
  methodName: "GetActivitiesByAsset",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByAssetRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivitiesByAssets = {
  methodName: "GetActivitiesByAssets",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByAssetsRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityLookupSession.GetActivities = {
  methodName: "GetActivities",
  service: ActivityLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
var ActivityQuerySession = {
  serviceName: "dlkit.proto.learning.ActivityQuerySession"
};
ActivityQuerySession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ActivityQuerySession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ActivityQuerySession.CanSearchActivities = {
  methodName: "CanSearchActivities",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanSearchActivitiesRequest,
  responseType: dlkit_proto_learning_pb.CanSearchActivitiesReply
};
ActivityQuerySession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ActivityQuerySession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ActivityQuerySession.GetActivityQuery = {
  methodName: "GetActivityQuery",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetActivityQueryRequest,
  responseType: dlkit_proto_learning_pb.GetActivityQueryReply
};
ActivityQuerySession.GetActivitiesByQuery = {
  methodName: "GetActivitiesByQuery",
  service: ActivityQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByQueryRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
var ActivityAdminSession = {
  serviceName: "dlkit.proto.learning.ActivityAdminSession"
};
ActivityAdminSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ActivityAdminSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ActivityAdminSession.CanCreateActivities = {
  methodName: "CanCreateActivities",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateActivitiesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateActivitiesReply
};
ActivityAdminSession.CanCreateActivityWithRecordTypes = {
  methodName: "CanCreateActivityWithRecordTypes",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateActivityWithRecordTypesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateActivityWithRecordTypesReply
};
ActivityAdminSession.GetActivityFormForCreate = {
  methodName: "GetActivityFormForCreate",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetActivityFormForCreateRequest,
  responseType: dlkit_proto_learning_pb.GetActivityFormForCreateReply
};
ActivityAdminSession.CreateActivity = {
  methodName: "CreateActivity",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CreateActivityRequest,
  responseType: dlkit_proto_learning_pb.CreateActivityReply
};
ActivityAdminSession.CanUpdateActivities = {
  methodName: "CanUpdateActivities",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanUpdateActivitiesRequest,
  responseType: dlkit_proto_learning_pb.CanUpdateActivitiesReply
};
ActivityAdminSession.GetActivityFormForUpdate = {
  methodName: "GetActivityFormForUpdate",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetActivityFormForUpdateRequest,
  responseType: dlkit_proto_learning_pb.GetActivityFormForUpdateReply
};
ActivityAdminSession.UpdateActivity = {
  methodName: "UpdateActivity",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UpdateActivityRequest,
  responseType: dlkit_proto_learning_pb.UpdateActivityReply
};
ActivityAdminSession.CanDeleteActivities = {
  methodName: "CanDeleteActivities",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanDeleteActivitiesRequest,
  responseType: dlkit_proto_learning_pb.CanDeleteActivitiesReply
};
ActivityAdminSession.DeleteActivity = {
  methodName: "DeleteActivity",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.DeleteActivityRequest,
  responseType: dlkit_proto_learning_pb.DeleteActivityReply
};
ActivityAdminSession.CanManageActivityAliases = {
  methodName: "CanManageActivityAliases",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanManageActivityAliasesRequest,
  responseType: dlkit_proto_learning_pb.CanManageActivityAliasesReply
};
ActivityAdminSession.AliasActivity = {
  methodName: "AliasActivity",
  service: ActivityAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AliasActivityRequest,
  responseType: dlkit_proto_learning_pb.AliasActivityReply
};
var ActivityObjectiveBankSession = {
  serviceName: "dlkit.proto.learning.ActivityObjectiveBankSession"
};
ActivityObjectiveBankSession.CanLookupActivityObjectiveBankMappings = {
  methodName: "CanLookupActivityObjectiveBankMappings",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupActivityObjectiveBankMappingsRequest,
  responseType: dlkit_proto_learning_pb.CanLookupActivityObjectiveBankMappingsReply
};
ActivityObjectiveBankSession.UseComparativeObjectiveBankView = {
  methodName: "UseComparativeObjectiveBankView",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply
};
ActivityObjectiveBankSession.UsePlenaryObjectiveBankView = {
  methodName: "UsePlenaryObjectiveBankView",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply
};
ActivityObjectiveBankSession.GetActivityIdsByObjectiveBank = {
  methodName: "GetActivityIdsByObjectiveBank",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivityIdsByObjectiveBankRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ActivityObjectiveBankSession.GetActivitiesByObjectiveBank = {
  methodName: "GetActivitiesByObjectiveBank",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityObjectiveBankSession.GetActivityIdsByObjectiveBanks = {
  methodName: "GetActivityIdsByObjectiveBanks",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivityIdsByObjectiveBanksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ActivityObjectiveBankSession.GetActivitiesByObjectiveBanks = {
  methodName: "GetActivitiesByObjectiveBanks",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetActivitiesByObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.Activity
};
ActivityObjectiveBankSession.GetObjectiveBankIdsByActivity = {
  methodName: "GetObjectiveBankIdsByActivity",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdsByActivityRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ActivityObjectiveBankSession.GetObjectiveBanksByActivity = {
  methodName: "GetObjectiveBanksByActivity",
  service: ActivityObjectiveBankSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByActivityRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
var ActivityObjectiveBankAssignmentSession = {
  serviceName: "dlkit.proto.learning.ActivityObjectiveBankAssignmentSession"
};
ActivityObjectiveBankAssignmentSession.CanAssignActivities = {
  methodName: "CanAssignActivities",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignActivitiesRequest,
  responseType: dlkit_proto_learning_pb.CanAssignActivitiesReply
};
ActivityObjectiveBankAssignmentSession.CanAssignActivitiesToObjectiveBank = {
  methodName: "CanAssignActivitiesToObjectiveBank",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignActivitiesToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.CanAssignActivitiesToObjectiveBankReply
};
ActivityObjectiveBankAssignmentSession.GetAssignableObjectiveBankIds = {
  methodName: "GetAssignableObjectiveBankIds",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ActivityObjectiveBankAssignmentSession.GetAssignableObjectiveBankIdsForActivity = {
  methodName: "GetAssignableObjectiveBankIdsForActivity",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsForActivityRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ActivityObjectiveBankAssignmentSession.AssignActivityToObjectiveBank = {
  methodName: "AssignActivityToObjectiveBank",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AssignActivityToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.AssignActivityToObjectiveBankReply
};
ActivityObjectiveBankAssignmentSession.UnassignActivityFromObjectiveBank = {
  methodName: "UnassignActivityFromObjectiveBank",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UnassignActivityFromObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.UnassignActivityFromObjectiveBankReply
};
ActivityObjectiveBankAssignmentSession.ReassignActivityToObjectiveBank = {
  methodName: "ReassignActivityToObjectiveBank",
  service: ActivityObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.ReassignActivityToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.ReassignActivityToObjectiveBankReply
};
var ProficiencyLookupSession = {
  serviceName: "dlkit.proto.learning.ProficiencyLookupSession"
};
ProficiencyLookupSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ProficiencyLookupSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ProficiencyLookupSession.CanLookupProficiencies = {
  methodName: "CanLookupProficiencies",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupProficienciesRequest,
  responseType: dlkit_proto_learning_pb.CanLookupProficienciesReply
};
ProficiencyLookupSession.UseComparativeProficiencyView = {
  methodName: "UseComparativeProficiencyView",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeProficiencyViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeProficiencyViewReply
};
ProficiencyLookupSession.UsePlenaryProficiencyView = {
  methodName: "UsePlenaryProficiencyView",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryProficiencyViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryProficiencyViewReply
};
ProficiencyLookupSession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ProficiencyLookupSession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ProficiencyLookupSession.UseEffectiveProficiencyView = {
  methodName: "UseEffectiveProficiencyView",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseEffectiveProficiencyViewRequest,
  responseType: dlkit_proto_learning_pb.UseEffectiveProficiencyViewReply
};
ProficiencyLookupSession.UseAnyEffectiveProficiencyView = {
  methodName: "UseAnyEffectiveProficiencyView",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseAnyEffectiveProficiencyViewRequest,
  responseType: dlkit_proto_learning_pb.UseAnyEffectiveProficiencyViewReply
};
ProficiencyLookupSession.GetProficiency = {
  methodName: "GetProficiency",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetProficiencyRequest,
  responseType: dlkit_proto_learning_pb.GetProficiencyReply
};
ProficiencyLookupSession.GetProficienciesByIds = {
  methodName: "GetProficienciesByIds",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByIdsRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusType = {
  methodName: "GetProficienciesByGenusType",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByParentGenusType = {
  methodName: "GetProficienciesByParentGenusType",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByParentGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByRecordType = {
  methodName: "GetProficienciesByRecordType",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByRecordTypeRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesOnDate = {
  methodName: "GetProficienciesOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeOnDate = {
  methodName: "GetProficienciesByGenusTypeOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForObjective = {
  methodName: "GetProficienciesForObjective",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForObjectiveRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForObjectiveOnDate = {
  methodName: "GetProficienciesForObjectiveOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForObjectiveOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeForObjective = {
  methodName: "GetProficienciesByGenusTypeForObjective",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeForObjectiveOnDate = {
  methodName: "GetProficienciesByGenusTypeForObjectiveOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForObjectives = {
  methodName: "GetProficienciesForObjectives",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForObjectivesRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForResource = {
  methodName: "GetProficienciesForResource",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForResourceRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForResourceOnDate = {
  methodName: "GetProficienciesForResourceOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForResourceOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeForResource = {
  methodName: "GetProficienciesByGenusTypeForResource",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeForResourceRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeForResourceOnDate = {
  methodName: "GetProficienciesByGenusTypeForResourceOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeForResourceOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForResources = {
  methodName: "GetProficienciesForResources",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForResourcesRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForObjectiveAndResource = {
  methodName: "GetProficienciesForObjectiveAndResource",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForObjectiveAndResourceRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesForObjectiveAndResourceOnDate = {
  methodName: "GetProficienciesForObjectiveAndResourceOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesForObjectiveAndResourceOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeForObjectiveAndResource = {
  methodName: "GetProficienciesByGenusTypeForObjectiveAndResource",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveAndResourceRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficienciesByGenusTypeForObjectiveAndResourceOnDate = {
  methodName: "GetProficienciesByGenusTypeForObjectiveAndResourceOnDate",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
ProficiencyLookupSession.GetProficiencies = {
  methodName: "GetProficiencies",
  service: ProficiencyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
var ProficiencyQuerySession = {
  serviceName: "dlkit.proto.learning.ProficiencyQuerySession"
};
ProficiencyQuerySession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ProficiencyQuerySession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ProficiencyQuerySession.CanSearchProficiencies = {
  methodName: "CanSearchProficiencies",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanSearchProficienciesRequest,
  responseType: dlkit_proto_learning_pb.CanSearchProficienciesReply
};
ProficiencyQuerySession.UseFederatedObjectiveBankView = {
  methodName: "UseFederatedObjectiveBankView",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply
};
ProficiencyQuerySession.UseIsolatedObjectiveBankView = {
  methodName: "UseIsolatedObjectiveBankView",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply
};
ProficiencyQuerySession.GetProficiencyQuery = {
  methodName: "GetProficiencyQuery",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetProficiencyQueryRequest,
  responseType: dlkit_proto_learning_pb.GetProficiencyQueryReply
};
ProficiencyQuerySession.GetProficienciesByQuery = {
  methodName: "GetProficienciesByQuery",
  service: ProficiencyQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetProficienciesByQueryRequest,
  responseType: dlkit_proto_learning_pb.Proficiency
};
var ProficiencyAdminSession = {
  serviceName: "dlkit.proto.learning.ProficiencyAdminSession"
};
ProficiencyAdminSession.GetObjectiveBankId = {
  methodName: "GetObjectiveBankId",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankIdReply
};
ProficiencyAdminSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ProficiencyAdminSession.CanCreateProficiencies = {
  methodName: "CanCreateProficiencies",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateProficienciesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateProficienciesReply
};
ProficiencyAdminSession.CanCreateProficiencyWithRecordTypes = {
  methodName: "CanCreateProficiencyWithRecordTypes",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateProficiencyWithRecordTypesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateProficiencyWithRecordTypesReply
};
ProficiencyAdminSession.GetProficiencyFormForCreate = {
  methodName: "GetProficiencyFormForCreate",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetProficiencyFormForCreateRequest,
  responseType: dlkit_proto_learning_pb.GetProficiencyFormForCreateReply
};
ProficiencyAdminSession.CreateProficiency = {
  methodName: "CreateProficiency",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CreateProficiencyRequest,
  responseType: dlkit_proto_learning_pb.CreateProficiencyReply
};
ProficiencyAdminSession.CanUpdateProficiencies = {
  methodName: "CanUpdateProficiencies",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanUpdateProficienciesRequest,
  responseType: dlkit_proto_learning_pb.CanUpdateProficienciesReply
};
ProficiencyAdminSession.GetProficiencyFormForUpdate = {
  methodName: "GetProficiencyFormForUpdate",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetProficiencyFormForUpdateRequest,
  responseType: dlkit_proto_learning_pb.GetProficiencyFormForUpdateReply
};
ProficiencyAdminSession.UpdateProficiency = {
  methodName: "UpdateProficiency",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UpdateProficiencyRequest,
  responseType: dlkit_proto_learning_pb.UpdateProficiencyReply
};
ProficiencyAdminSession.CanDeleteProficiencies = {
  methodName: "CanDeleteProficiencies",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanDeleteProficienciesRequest,
  responseType: dlkit_proto_learning_pb.CanDeleteProficienciesReply
};
ProficiencyAdminSession.DeleteProficiency = {
  methodName: "DeleteProficiency",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.DeleteProficiencyRequest,
  responseType: dlkit_proto_learning_pb.DeleteProficiencyReply
};
ProficiencyAdminSession.DeleteProficiencies = {
  methodName: "DeleteProficiencies",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.DeleteProficienciesRequest,
  responseType: dlkit_proto_learning_pb.DeleteProficienciesReply
};
ProficiencyAdminSession.CanManageProficiencyAliases = {
  methodName: "CanManageProficiencyAliases",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanManageProficiencyAliasesRequest,
  responseType: dlkit_proto_learning_pb.CanManageProficiencyAliasesReply
};
ProficiencyAdminSession.AliasProficiency = {
  methodName: "AliasProficiency",
  service: ProficiencyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AliasProficiencyRequest,
  responseType: dlkit_proto_learning_pb.AliasProficiencyReply
};
var ProficiencyObjectiveBankAssignmentSession = {
  serviceName: "dlkit.proto.learning.ProficiencyObjectiveBankAssignmentSession"
};
ProficiencyObjectiveBankAssignmentSession.CanAssignProficiencies = {
  methodName: "CanAssignProficiencies",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignProficienciesRequest,
  responseType: dlkit_proto_learning_pb.CanAssignProficienciesReply
};
ProficiencyObjectiveBankAssignmentSession.CanAssignProficienciesToObjectiveBank = {
  methodName: "CanAssignProficienciesToObjectiveBank",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAssignProficienciesToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.CanAssignProficienciesToObjectiveBankReply
};
ProficiencyObjectiveBankAssignmentSession.GetAssignableObjectiveBankIds = {
  methodName: "GetAssignableObjectiveBankIds",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ProficiencyObjectiveBankAssignmentSession.GetAssignableObjectiveBankIdsForProficiency = {
  methodName: "GetAssignableObjectiveBankIdsForProficiency",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsForProficiencyRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ProficiencyObjectiveBankAssignmentSession.AssignProficiencyToObjectiveBank = {
  methodName: "AssignProficiencyToObjectiveBank",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AssignProficiencyToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.AssignProficiencyToObjectiveBankReply
};
ProficiencyObjectiveBankAssignmentSession.UnassignProficiencyFromObjectiveBank = {
  methodName: "UnassignProficiencyFromObjectiveBank",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UnassignProficiencyFromObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.UnassignProficiencyFromObjectiveBankReply
};
ProficiencyObjectiveBankAssignmentSession.ReassignProficiencyToObjectiveBank = {
  methodName: "ReassignProficiencyToObjectiveBank",
  service: ProficiencyObjectiveBankAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankReply
};
var ObjectiveBankLookupSession = {
  serviceName: "dlkit.proto.learning.ObjectiveBankLookupSession"
};
ObjectiveBankLookupSession.CanLookupObjectiveBanks = {
  methodName: "CanLookupObjectiveBanks",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanLookupObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.CanLookupObjectiveBanksReply
};
ObjectiveBankLookupSession.UseComparativeObjectiveBankView = {
  methodName: "UseComparativeObjectiveBankView",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply
};
ObjectiveBankLookupSession.UsePlenaryObjectiveBankView = {
  methodName: "UsePlenaryObjectiveBankView",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply
};
ObjectiveBankLookupSession.GetObjectiveBank = {
  methodName: "GetObjectiveBank",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankReply
};
ObjectiveBankLookupSession.GetObjectiveBanksByIds = {
  methodName: "GetObjectiveBanksByIds",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByIdsRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankLookupSession.GetObjectiveBanksByGenusType = {
  methodName: "GetObjectiveBanksByGenusType",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankLookupSession.GetObjectiveBanksByParentGenusType = {
  methodName: "GetObjectiveBanksByParentGenusType",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByParentGenusTypeRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankLookupSession.GetObjectiveBanksByRecordType = {
  methodName: "GetObjectiveBanksByRecordType",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByRecordTypeRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankLookupSession.GetObjectiveBanksByProvider = {
  methodName: "GetObjectiveBanksByProvider",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksByProviderRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankLookupSession.GetObjectiveBanks = {
  methodName: "GetObjectiveBanks",
  service: ObjectiveBankLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
var ObjectiveBankAdminSession = {
  serviceName: "dlkit.proto.learning.ObjectiveBankAdminSession"
};
ObjectiveBankAdminSession.CanCreateObjectiveBanks = {
  methodName: "CanCreateObjectiveBanks",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.CanCreateObjectiveBanksReply
};
ObjectiveBankAdminSession.CanCreateObjectiveBankWithRecordTypes = {
  methodName: "CanCreateObjectiveBankWithRecordTypes",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanCreateObjectiveBankWithRecordTypesRequest,
  responseType: dlkit_proto_learning_pb.CanCreateObjectiveBankWithRecordTypesReply
};
ObjectiveBankAdminSession.GetObjectiveBankFormForCreate = {
  methodName: "GetObjectiveBankFormForCreate",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankFormForCreateRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankFormForCreateReply
};
ObjectiveBankAdminSession.CreateObjectiveBank = {
  methodName: "CreateObjectiveBank",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CreateObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.CreateObjectiveBankReply
};
ObjectiveBankAdminSession.CanUpdateObjectiveBanks = {
  methodName: "CanUpdateObjectiveBanks",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanUpdateObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.CanUpdateObjectiveBanksReply
};
ObjectiveBankAdminSession.GetObjectiveBankFormForUpdate = {
  methodName: "GetObjectiveBankFormForUpdate",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankFormForUpdateRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankFormForUpdateReply
};
ObjectiveBankAdminSession.UpdateObjectiveBank = {
  methodName: "UpdateObjectiveBank",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UpdateObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.UpdateObjectiveBankReply
};
ObjectiveBankAdminSession.CanDeleteObjectiveBanks = {
  methodName: "CanDeleteObjectiveBanks",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanDeleteObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.CanDeleteObjectiveBanksReply
};
ObjectiveBankAdminSession.DeleteObjectiveBank = {
  methodName: "DeleteObjectiveBank",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.DeleteObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.DeleteObjectiveBankReply
};
ObjectiveBankAdminSession.CanManageObjectiveBankAliases = {
  methodName: "CanManageObjectiveBankAliases",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanManageObjectiveBankAliasesRequest,
  responseType: dlkit_proto_learning_pb.CanManageObjectiveBankAliasesReply
};
ObjectiveBankAdminSession.AliasObjectiveBank = {
  methodName: "AliasObjectiveBank",
  service: ObjectiveBankAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AliasObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.AliasObjectiveBankReply
};
var ObjectiveBankHierarchySession = {
  serviceName: "dlkit.proto.learning.ObjectiveBankHierarchySession"
};
ObjectiveBankHierarchySession.GetObjectiveBankHierarchyId = {
  methodName: "GetObjectiveBankHierarchyId",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdReply
};
ObjectiveBankHierarchySession.GetObjectiveBankHierarchy = {
  methodName: "GetObjectiveBankHierarchy",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyReply
};
ObjectiveBankHierarchySession.CanAccessObjectiveBankHierarchy = {
  methodName: "CanAccessObjectiveBankHierarchy",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanAccessObjectiveBankHierarchyRequest,
  responseType: dlkit_proto_learning_pb.CanAccessObjectiveBankHierarchyReply
};
ObjectiveBankHierarchySession.UseComparativeObjectiveBankView = {
  methodName: "UseComparativeObjectiveBankView",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply
};
ObjectiveBankHierarchySession.UsePlenaryObjectiveBankView = {
  methodName: "UsePlenaryObjectiveBankView",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest,
  responseType: dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply
};
ObjectiveBankHierarchySession.GetRootObjectiveBankIds = {
  methodName: "GetRootObjectiveBankIds",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetRootObjectiveBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveBankHierarchySession.GetRootObjectiveBanks = {
  methodName: "GetRootObjectiveBanks",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetRootObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankHierarchySession.HasParentObjectiveBanks = {
  methodName: "HasParentObjectiveBanks",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.HasParentObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.HasParentObjectiveBanksReply
};
ObjectiveBankHierarchySession.IsParentOfObjectiveBank = {
  methodName: "IsParentOfObjectiveBank",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsParentOfObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.IsParentOfObjectiveBankReply
};
ObjectiveBankHierarchySession.GetParentObjectiveBankIds = {
  methodName: "GetParentObjectiveBankIds",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetParentObjectiveBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveBankHierarchySession.GetParentObjectiveBanks = {
  methodName: "GetParentObjectiveBanks",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetParentObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankHierarchySession.IsAncestorOfObjectiveBank = {
  methodName: "IsAncestorOfObjectiveBank",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsAncestorOfObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.IsAncestorOfObjectiveBankReply
};
ObjectiveBankHierarchySession.HasChildObjectiveBanks = {
  methodName: "HasChildObjectiveBanks",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.HasChildObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.HasChildObjectiveBanksReply
};
ObjectiveBankHierarchySession.IsChildOfObjectiveBank = {
  methodName: "IsChildOfObjectiveBank",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsChildOfObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.IsChildOfObjectiveBankReply
};
ObjectiveBankHierarchySession.GetChildObjectiveBankIds = {
  methodName: "GetChildObjectiveBankIds",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetChildObjectiveBankIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ObjectiveBankHierarchySession.GetChildObjectiveBanks = {
  methodName: "GetChildObjectiveBanks",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_learning_pb.GetChildObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.ObjectiveBank
};
ObjectiveBankHierarchySession.IsDescendantOfObjectiveBank = {
  methodName: "IsDescendantOfObjectiveBank",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.IsDescendantOfObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.IsDescendantOfObjectiveBankReply
};
ObjectiveBankHierarchySession.GetObjectiveBankNodeIds = {
  methodName: "GetObjectiveBankNodeIds",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankNodeIdsRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankNodeIdsReply
};
ObjectiveBankHierarchySession.GetObjectiveBankNodes = {
  methodName: "GetObjectiveBankNodes",
  service: ObjectiveBankHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankNodesRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankNodesReply
};
var ObjectiveBankHierarchyDesignSession = {
  serviceName: "dlkit.proto.learning.ObjectiveBankHierarchyDesignSession"
};
ObjectiveBankHierarchyDesignSession.GetObjectiveBankHierarchyId = {
  methodName: "GetObjectiveBankHierarchyId",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdReply
};
ObjectiveBankHierarchyDesignSession.GetObjectiveBankHierarchy = {
  methodName: "GetObjectiveBankHierarchy",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyRequest,
  responseType: dlkit_proto_learning_pb.GetObjectiveBankHierarchyReply
};
ObjectiveBankHierarchyDesignSession.CanModifyObjectiveBankHierarchy = {
  methodName: "CanModifyObjectiveBankHierarchy",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.CanModifyObjectiveBankHierarchyRequest,
  responseType: dlkit_proto_learning_pb.CanModifyObjectiveBankHierarchyReply
};
ObjectiveBankHierarchyDesignSession.AddRootObjectiveBank = {
  methodName: "AddRootObjectiveBank",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AddRootObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.AddRootObjectiveBankReply
};
ObjectiveBankHierarchyDesignSession.RemoveRootObjectiveBank = {
  methodName: "RemoveRootObjectiveBank",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.RemoveRootObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.RemoveRootObjectiveBankReply
};
ObjectiveBankHierarchyDesignSession.AddChildObjectiveBank = {
  methodName: "AddChildObjectiveBank",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.AddChildObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.AddChildObjectiveBankReply
};
ObjectiveBankHierarchyDesignSession.RemoveChildObjectiveBank = {
  methodName: "RemoveChildObjectiveBank",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.RemoveChildObjectiveBankRequest,
  responseType: dlkit_proto_learning_pb.RemoveChildObjectiveBankReply
};
ObjectiveBankHierarchyDesignSession.RemoveChildObjectiveBanks = {
  methodName: "RemoveChildObjectiveBanks",
  service: ObjectiveBankHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_learning_pb.RemoveChildObjectiveBanksRequest,
  responseType: dlkit_proto_learning_pb.RemoveChildObjectiveBanksReply
};
module.exports = {
  ObjectiveLookupSession: ObjectiveLookupSession,
  ObjectiveQuerySession: ObjectiveQuerySession,
  ObjectiveAdminSession: ObjectiveAdminSession,
  ObjectiveHierarchySession: ObjectiveHierarchySession,
  ObjectiveHierarchyDesignSession: ObjectiveHierarchyDesignSession,
  ObjectiveSequencingSession: ObjectiveSequencingSession,
  ObjectiveObjectiveBankSession: ObjectiveObjectiveBankSession,
  ObjectiveObjectiveBankAssignmentSession: ObjectiveObjectiveBankAssignmentSession,
  ObjectiveRequisiteSession: ObjectiveRequisiteSession,
  ObjectiveRequisiteAssignmentSession: ObjectiveRequisiteAssignmentSession,
  ActivityLookupSession: ActivityLookupSession,
  ActivityQuerySession: ActivityQuerySession,
  ActivityAdminSession: ActivityAdminSession,
  ActivityObjectiveBankSession: ActivityObjectiveBankSession,
  ActivityObjectiveBankAssignmentSession: ActivityObjectiveBankAssignmentSession,
  ProficiencyLookupSession: ProficiencyLookupSession,
  ProficiencyQuerySession: ProficiencyQuerySession,
  ProficiencyAdminSession: ProficiencyAdminSession,
  ProficiencyObjectiveBankAssignmentSession: ProficiencyObjectiveBankAssignmentSession,
  ObjectiveBankLookupSession: ObjectiveBankLookupSession,
  ObjectiveBankAdminSession: ObjectiveBankAdminSession,
  ObjectiveBankHierarchySession: ObjectiveBankHierarchySession,
  ObjectiveBankHierarchyDesignSession: ObjectiveBankHierarchyDesignSession,
};

