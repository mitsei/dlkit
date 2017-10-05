// package: dlkit.proto.learning
// file: dlkit/proto/learning.proto

import * as dlkit_proto_learning_pb from "../../dlkit/proto/learning_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class ObjectiveLookupSession {
  static serviceName = "dlkit.proto.learning.ObjectiveLookupSession";
}
export namespace ObjectiveLookupSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanLookupObjectives {
    static readonly methodName = "CanLookupObjectives";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupObjectivesReply;
  }
  export class UseComparativeObjectiveView {
    static readonly methodName = "UseComparativeObjectiveView";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveViewReply;
  }
  export class UsePlenaryObjectiveView {
    static readonly methodName = "UsePlenaryObjectiveView";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveViewReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class GetObjective {
    static readonly methodName = "GetObjective";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveReply;
  }
  export class GetObjectivesByIds {
    static readonly methodName = "GetObjectivesByIds";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByIdsRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetObjectivesByGenusType {
    static readonly methodName = "GetObjectivesByGenusType";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetObjectivesByParentGenusType {
    static readonly methodName = "GetObjectivesByParentGenusType";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetObjectivesByRecordType {
    static readonly methodName = "GetObjectivesByRecordType";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetObjectives {
    static readonly methodName = "GetObjectives";
    static readonly service = ObjectiveLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
}
export class ObjectiveQuerySession {
  static serviceName = "dlkit.proto.learning.ObjectiveQuerySession";
}
export namespace ObjectiveQuerySession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanSearchObjectives {
    static readonly methodName = "CanSearchObjectives";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanSearchObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanSearchObjectivesReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class GetObjectiveQuery {
    static readonly methodName = "GetObjectiveQuery";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveQueryRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveQueryReply;
  }
  export class GetObjectivesByQuery {
    static readonly methodName = "GetObjectivesByQuery";
    static readonly service = ObjectiveQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByQueryRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
}
export class ObjectiveAdminSession {
  static serviceName = "dlkit.proto.learning.ObjectiveAdminSession";
}
export namespace ObjectiveAdminSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanCreateObjectives {
    static readonly methodName = "CanCreateObjectives";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateObjectivesReply;
  }
  export class CanCreateObjectiveWithRecordTypes {
    static readonly methodName = "CanCreateObjectiveWithRecordTypes";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateObjectiveWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateObjectiveWithRecordTypesReply;
  }
  export class GetObjectiveFormForCreate {
    static readonly methodName = "GetObjectiveFormForCreate";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveFormForCreateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveFormForCreateReply;
  }
  export class CreateObjective {
    static readonly methodName = "CreateObjective";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CreateObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.CreateObjectiveReply;
  }
  export class CanUpdateObjectives {
    static readonly methodName = "CanUpdateObjectives";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanUpdateObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanUpdateObjectivesReply;
  }
  export class GetObjectiveFormForUpdate {
    static readonly methodName = "GetObjectiveFormForUpdate";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveFormForUpdateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveFormForUpdateReply;
  }
  export class UpdateObjective {
    static readonly methodName = "UpdateObjective";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UpdateObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.UpdateObjectiveReply;
  }
  export class CanDeleteObjectives {
    static readonly methodName = "CanDeleteObjectives";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanDeleteObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanDeleteObjectivesReply;
  }
  export class DeleteObjective {
    static readonly methodName = "DeleteObjective";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.DeleteObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.DeleteObjectiveReply;
  }
  export class CanManageObjectiveAliases {
    static readonly methodName = "CanManageObjectiveAliases";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanManageObjectiveAliasesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanManageObjectiveAliasesReply;
  }
  export class AliasObjective {
    static readonly methodName = "AliasObjective";
    static readonly service = ObjectiveAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AliasObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.AliasObjectiveReply;
  }
}
export class ObjectiveHierarchySession {
  static serviceName = "dlkit.proto.learning.ObjectiveHierarchySession";
}
export namespace ObjectiveHierarchySession {
  export class GetObjectiveHierarchyId {
    static readonly methodName = "GetObjectiveHierarchyId";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveHierarchyIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveHierarchyIdReply;
  }
  export class GetObjectiveHierarchy {
    static readonly methodName = "GetObjectiveHierarchy";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveHierarchyReply;
  }
  export class CanAccessObjectiveHierarchy {
    static readonly methodName = "CanAccessObjectiveHierarchy";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAccessObjectiveHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAccessObjectiveHierarchyReply;
  }
  export class UseComparativeObjectiveView {
    static readonly methodName = "UseComparativeObjectiveView";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveViewReply;
  }
  export class UsePlenaryObjectiveView {
    static readonly methodName = "UsePlenaryObjectiveView";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveViewReply;
  }
  export class GetRootObjectiveIds {
    static readonly methodName = "GetRootObjectiveIds";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetRootObjectiveIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootObjectives {
    static readonly methodName = "GetRootObjectives";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetRootObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class HasParentObjectives {
    static readonly methodName = "HasParentObjectives";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.HasParentObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.HasParentObjectivesReply;
  }
  export class IsParentOfObjective {
    static readonly methodName = "IsParentOfObjective";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsParentOfObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsParentOfObjectiveReply;
  }
  export class GetParentObjectiveIds {
    static readonly methodName = "GetParentObjectiveIds";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetParentObjectiveIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentObjectives {
    static readonly methodName = "GetParentObjectives";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetParentObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class IsAncestorOfObjective {
    static readonly methodName = "IsAncestorOfObjective";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsAncestorOfObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsAncestorOfObjectiveReply;
  }
  export class HasChildObjectives {
    static readonly methodName = "HasChildObjectives";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.HasChildObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.HasChildObjectivesReply;
  }
  export class IsChildOfObjective {
    static readonly methodName = "IsChildOfObjective";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsChildOfObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsChildOfObjectiveReply;
  }
  export class GetChildObjectiveIds {
    static readonly methodName = "GetChildObjectiveIds";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetChildObjectiveIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildObjectives {
    static readonly methodName = "GetChildObjectives";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetChildObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class IsDescendantOfObjective {
    static readonly methodName = "IsDescendantOfObjective";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsDescendantOfObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsDescendantOfObjectiveReply;
  }
  export class GetObjectiveNodeIds {
    static readonly methodName = "GetObjectiveNodeIds";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveNodeIdsRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveNodeIdsReply;
  }
  export class GetObjectiveNodes {
    static readonly methodName = "GetObjectiveNodes";
    static readonly service = ObjectiveHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveNodesRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveNodesReply;
  }
}
export class ObjectiveHierarchyDesignSession {
  static serviceName = "dlkit.proto.learning.ObjectiveHierarchyDesignSession";
}
export namespace ObjectiveHierarchyDesignSession {
  export class GetObjectiveHierarchyId {
    static readonly methodName = "GetObjectiveHierarchyId";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveHierarchyIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveHierarchyIdReply;
  }
  export class GetObjectiveHierarchy {
    static readonly methodName = "GetObjectiveHierarchy";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveHierarchyReply;
  }
  export class CanModifyObjectiveHierarchy {
    static readonly methodName = "CanModifyObjectiveHierarchy";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanModifyObjectiveHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanModifyObjectiveHierarchyReply;
  }
  export class AddRootObjective {
    static readonly methodName = "AddRootObjective";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AddRootObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.AddRootObjectiveReply;
  }
  export class RemoveRootObjective {
    static readonly methodName = "RemoveRootObjective";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.RemoveRootObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.RemoveRootObjectiveReply;
  }
  export class AddChildObjective {
    static readonly methodName = "AddChildObjective";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AddChildObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.AddChildObjectiveReply;
  }
  export class RemoveChildObjective {
    static readonly methodName = "RemoveChildObjective";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.RemoveChildObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.RemoveChildObjectiveReply;
  }
  export class RemoveChildObjectives {
    static readonly methodName = "RemoveChildObjectives";
    static readonly service = ObjectiveHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.RemoveChildObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.RemoveChildObjectivesReply;
  }
}
export class ObjectiveSequencingSession {
  static serviceName = "dlkit.proto.learning.ObjectiveSequencingSession";
}
export namespace ObjectiveSequencingSession {
  export class GetObjectiveHierarchyId {
    static readonly methodName = "GetObjectiveHierarchyId";
    static readonly service = ObjectiveSequencingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveHierarchyIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveHierarchyIdReply;
  }
  export class GetObjectiveHierarchy {
    static readonly methodName = "GetObjectiveHierarchy";
    static readonly service = ObjectiveSequencingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveHierarchyReply;
  }
  export class CanSequenceObjectives {
    static readonly methodName = "CanSequenceObjectives";
    static readonly service = ObjectiveSequencingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanSequenceObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanSequenceObjectivesReply;
  }
  export class MoveObjectiveAhead {
    static readonly methodName = "MoveObjectiveAhead";
    static readonly service = ObjectiveSequencingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.MoveObjectiveAheadRequest;
    static readonly responseType = dlkit_proto_learning_pb.MoveObjectiveAheadReply;
  }
  export class MoveObjectiveBehind {
    static readonly methodName = "MoveObjectiveBehind";
    static readonly service = ObjectiveSequencingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.MoveObjectiveBehindRequest;
    static readonly responseType = dlkit_proto_learning_pb.MoveObjectiveBehindReply;
  }
  export class SequenceObjectives {
    static readonly methodName = "SequenceObjectives";
    static readonly service = ObjectiveSequencingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.SequenceObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.SequenceObjectivesReply;
  }
}
export class ObjectiveObjectiveBankSession {
  static serviceName = "dlkit.proto.learning.ObjectiveObjectiveBankSession";
}
export namespace ObjectiveObjectiveBankSession {
  export class CanLookupObjectiveObjectiveBankMappings {
    static readonly methodName = "CanLookupObjectiveObjectiveBankMappings";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupObjectiveObjectiveBankMappingsRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupObjectiveObjectiveBankMappingsReply;
  }
  export class UseComparativeObjectiveBankView {
    static readonly methodName = "UseComparativeObjectiveBankView";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply;
  }
  export class UsePlenaryObjectiveBankView {
    static readonly methodName = "UsePlenaryObjectiveBankView";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply;
  }
  export class GetObjectiveIdsByObjectiveBank {
    static readonly methodName = "GetObjectiveIdsByObjectiveBank";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveIdsByObjectiveBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetObjectivesByObjectiveBank {
    static readonly methodName = "GetObjectivesByObjectiveBank";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetObjectiveIdsByObjectiveBanks {
    static readonly methodName = "GetObjectiveIdsByObjectiveBanks";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveIdsByObjectiveBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetObjectivesByObjectiveBanks {
    static readonly methodName = "GetObjectivesByObjectiveBanks";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectivesByObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetObjectiveBankIdsByObjective {
    static readonly methodName = "GetObjectiveBankIdsByObjective";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdsByObjectiveRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetObjectiveBanksByObjective {
    static readonly methodName = "GetObjectiveBanksByObjective";
    static readonly service = ObjectiveObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
}
export class ObjectiveObjectiveBankAssignmentSession {
  static serviceName = "dlkit.proto.learning.ObjectiveObjectiveBankAssignmentSession";
}
export namespace ObjectiveObjectiveBankAssignmentSession {
  export class CanAssignObjectives {
    static readonly methodName = "CanAssignObjectives";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignObjectivesReply;
  }
  export class CanAssignObjectivesToObjectiveBank {
    static readonly methodName = "CanAssignObjectivesToObjectiveBank";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignObjectivesToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignObjectivesToObjectiveBankReply;
  }
  export class GetAssignableObjectiveBankIds {
    static readonly methodName = "GetAssignableObjectiveBankIds";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableObjectiveBankIdsForObjective {
    static readonly methodName = "GetAssignableObjectiveBankIdsForObjective";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsForObjectiveRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignObjectiveToObjectiveBank {
    static readonly methodName = "AssignObjectiveToObjectiveBank";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AssignObjectiveToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.AssignObjectiveToObjectiveBankReply;
  }
  export class UnassignObjectiveFromObjectiveBank {
    static readonly methodName = "UnassignObjectiveFromObjectiveBank";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UnassignObjectiveFromObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.UnassignObjectiveFromObjectiveBankReply;
  }
  export class ReassignProficiencyToObjectiveBank {
    static readonly methodName = "ReassignProficiencyToObjectiveBank";
    static readonly service = ObjectiveObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankReply;
  }
}
export class ObjectiveRequisiteSession {
  static serviceName = "dlkit.proto.learning.ObjectiveRequisiteSession";
}
export namespace ObjectiveRequisiteSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanLookupObjectivePrerequisites {
    static readonly methodName = "CanLookupObjectivePrerequisites";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupObjectivePrerequisitesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupObjectivePrerequisitesReply;
  }
  export class UseComparativeObjectiveView {
    static readonly methodName = "UseComparativeObjectiveView";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveViewReply;
  }
  export class UsePlenaryObjectiveView {
    static readonly methodName = "UsePlenaryObjectiveView";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveViewReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class GetRequisiteObjectives {
    static readonly methodName = "GetRequisiteObjectives";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetRequisiteObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetAllRequisiteObjectives {
    static readonly methodName = "GetAllRequisiteObjectives";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAllRequisiteObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class GetDependentObjectives {
    static readonly methodName = "GetDependentObjectives";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetDependentObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
  export class IsObjectiveRequired {
    static readonly methodName = "IsObjectiveRequired";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsObjectiveRequiredRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsObjectiveRequiredReply;
  }
  export class GetEquivalentObjectives {
    static readonly methodName = "GetEquivalentObjectives";
    static readonly service = ObjectiveRequisiteSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetEquivalentObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Objective;
  }
}
export class ObjectiveRequisiteAssignmentSession {
  static serviceName = "dlkit.proto.learning.ObjectiveRequisiteAssignmentSession";
}
export namespace ObjectiveRequisiteAssignmentSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanAssignRequisites {
    static readonly methodName = "CanAssignRequisites";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignRequisitesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignRequisitesReply;
  }
  export class AssignObjectiveRequisite {
    static readonly methodName = "AssignObjectiveRequisite";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AssignObjectiveRequisiteRequest;
    static readonly responseType = dlkit_proto_learning_pb.AssignObjectiveRequisiteReply;
  }
  export class UnassignObjectiveRequisite {
    static readonly methodName = "UnassignObjectiveRequisite";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UnassignObjectiveRequisiteRequest;
    static readonly responseType = dlkit_proto_learning_pb.UnassignObjectiveRequisiteReply;
  }
  export class AssignEquivalentObjective {
    static readonly methodName = "AssignEquivalentObjective";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AssignEquivalentObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.AssignEquivalentObjectiveReply;
  }
  export class UnassignEquivalentObjective {
    static readonly methodName = "UnassignEquivalentObjective";
    static readonly service = ObjectiveRequisiteAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UnassignEquivalentObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.UnassignEquivalentObjectiveReply;
  }
}
export class ActivityLookupSession {
  static serviceName = "dlkit.proto.learning.ActivityLookupSession";
}
export namespace ActivityLookupSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanLookupActivities {
    static readonly methodName = "CanLookupActivities";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupActivitiesReply;
  }
  export class UseComparativeActivityView {
    static readonly methodName = "UseComparativeActivityView";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeActivityViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeActivityViewReply;
  }
  export class UsePlenaryActivityView {
    static readonly methodName = "UsePlenaryActivityView";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryActivityViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryActivityViewReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class GetActivity {
    static readonly methodName = "GetActivity";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetActivityRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetActivityReply;
  }
  export class GetActivitiesByIds {
    static readonly methodName = "GetActivitiesByIds";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByIdsRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesByGenusType {
    static readonly methodName = "GetActivitiesByGenusType";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesByParentGenusType {
    static readonly methodName = "GetActivitiesByParentGenusType";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesByRecordType {
    static readonly methodName = "GetActivitiesByRecordType";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesForObjective {
    static readonly methodName = "GetActivitiesForObjective";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesForObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesForObjectives {
    static readonly methodName = "GetActivitiesForObjectives";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesForObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesByAsset {
    static readonly methodName = "GetActivitiesByAsset";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByAssetRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivitiesByAssets {
    static readonly methodName = "GetActivitiesByAssets";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByAssetsRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivities {
    static readonly methodName = "GetActivities";
    static readonly service = ActivityLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
}
export class ActivityQuerySession {
  static serviceName = "dlkit.proto.learning.ActivityQuerySession";
}
export namespace ActivityQuerySession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanSearchActivities {
    static readonly methodName = "CanSearchActivities";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanSearchActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanSearchActivitiesReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class GetActivityQuery {
    static readonly methodName = "GetActivityQuery";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetActivityQueryRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetActivityQueryReply;
  }
  export class GetActivitiesByQuery {
    static readonly methodName = "GetActivitiesByQuery";
    static readonly service = ActivityQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByQueryRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
}
export class ActivityAdminSession {
  static serviceName = "dlkit.proto.learning.ActivityAdminSession";
}
export namespace ActivityAdminSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanCreateActivities {
    static readonly methodName = "CanCreateActivities";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateActivitiesReply;
  }
  export class CanCreateActivityWithRecordTypes {
    static readonly methodName = "CanCreateActivityWithRecordTypes";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateActivityWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateActivityWithRecordTypesReply;
  }
  export class GetActivityFormForCreate {
    static readonly methodName = "GetActivityFormForCreate";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetActivityFormForCreateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetActivityFormForCreateReply;
  }
  export class CreateActivity {
    static readonly methodName = "CreateActivity";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CreateActivityRequest;
    static readonly responseType = dlkit_proto_learning_pb.CreateActivityReply;
  }
  export class CanUpdateActivities {
    static readonly methodName = "CanUpdateActivities";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanUpdateActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanUpdateActivitiesReply;
  }
  export class GetActivityFormForUpdate {
    static readonly methodName = "GetActivityFormForUpdate";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetActivityFormForUpdateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetActivityFormForUpdateReply;
  }
  export class UpdateActivity {
    static readonly methodName = "UpdateActivity";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UpdateActivityRequest;
    static readonly responseType = dlkit_proto_learning_pb.UpdateActivityReply;
  }
  export class CanDeleteActivities {
    static readonly methodName = "CanDeleteActivities";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanDeleteActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanDeleteActivitiesReply;
  }
  export class DeleteActivity {
    static readonly methodName = "DeleteActivity";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.DeleteActivityRequest;
    static readonly responseType = dlkit_proto_learning_pb.DeleteActivityReply;
  }
  export class CanManageActivityAliases {
    static readonly methodName = "CanManageActivityAliases";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanManageActivityAliasesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanManageActivityAliasesReply;
  }
  export class AliasActivity {
    static readonly methodName = "AliasActivity";
    static readonly service = ActivityAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AliasActivityRequest;
    static readonly responseType = dlkit_proto_learning_pb.AliasActivityReply;
  }
}
export class ActivityObjectiveBankSession {
  static serviceName = "dlkit.proto.learning.ActivityObjectiveBankSession";
}
export namespace ActivityObjectiveBankSession {
  export class CanLookupActivityObjectiveBankMappings {
    static readonly methodName = "CanLookupActivityObjectiveBankMappings";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupActivityObjectiveBankMappingsRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupActivityObjectiveBankMappingsReply;
  }
  export class UseComparativeObjectiveBankView {
    static readonly methodName = "UseComparativeObjectiveBankView";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply;
  }
  export class UsePlenaryObjectiveBankView {
    static readonly methodName = "UsePlenaryObjectiveBankView";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply;
  }
  export class GetActivityIdsByObjectiveBank {
    static readonly methodName = "GetActivityIdsByObjectiveBank";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivityIdsByObjectiveBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetActivitiesByObjectiveBank {
    static readonly methodName = "GetActivitiesByObjectiveBank";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetActivityIdsByObjectiveBanks {
    static readonly methodName = "GetActivityIdsByObjectiveBanks";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivityIdsByObjectiveBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetActivitiesByObjectiveBanks {
    static readonly methodName = "GetActivitiesByObjectiveBanks";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetActivitiesByObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.Activity;
  }
  export class GetObjectiveBankIdsByActivity {
    static readonly methodName = "GetObjectiveBankIdsByActivity";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdsByActivityRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetObjectiveBanksByActivity {
    static readonly methodName = "GetObjectiveBanksByActivity";
    static readonly service = ActivityObjectiveBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByActivityRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
}
export class ActivityObjectiveBankAssignmentSession {
  static serviceName = "dlkit.proto.learning.ActivityObjectiveBankAssignmentSession";
}
export namespace ActivityObjectiveBankAssignmentSession {
  export class CanAssignActivities {
    static readonly methodName = "CanAssignActivities";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignActivitiesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignActivitiesReply;
  }
  export class CanAssignActivitiesToObjectiveBank {
    static readonly methodName = "CanAssignActivitiesToObjectiveBank";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignActivitiesToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignActivitiesToObjectiveBankReply;
  }
  export class GetAssignableObjectiveBankIds {
    static readonly methodName = "GetAssignableObjectiveBankIds";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableObjectiveBankIdsForActivity {
    static readonly methodName = "GetAssignableObjectiveBankIdsForActivity";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsForActivityRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignActivityToObjectiveBank {
    static readonly methodName = "AssignActivityToObjectiveBank";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AssignActivityToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.AssignActivityToObjectiveBankReply;
  }
  export class UnassignActivityFromObjectiveBank {
    static readonly methodName = "UnassignActivityFromObjectiveBank";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UnassignActivityFromObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.UnassignActivityFromObjectiveBankReply;
  }
  export class ReassignActivityToObjectiveBank {
    static readonly methodName = "ReassignActivityToObjectiveBank";
    static readonly service = ActivityObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.ReassignActivityToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.ReassignActivityToObjectiveBankReply;
  }
}
export class ProficiencyLookupSession {
  static serviceName = "dlkit.proto.learning.ProficiencyLookupSession";
}
export namespace ProficiencyLookupSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanLookupProficiencies {
    static readonly methodName = "CanLookupProficiencies";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupProficienciesReply;
  }
  export class UseComparativeProficiencyView {
    static readonly methodName = "UseComparativeProficiencyView";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeProficiencyViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeProficiencyViewReply;
  }
  export class UsePlenaryProficiencyView {
    static readonly methodName = "UsePlenaryProficiencyView";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryProficiencyViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryProficiencyViewReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class UseEffectiveProficiencyView {
    static readonly methodName = "UseEffectiveProficiencyView";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseEffectiveProficiencyViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseEffectiveProficiencyViewReply;
  }
  export class UseAnyEffectiveProficiencyView {
    static readonly methodName = "UseAnyEffectiveProficiencyView";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseAnyEffectiveProficiencyViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseAnyEffectiveProficiencyViewReply;
  }
  export class GetProficiency {
    static readonly methodName = "GetProficiency";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetProficiencyRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetProficiencyReply;
  }
  export class GetProficienciesByIds {
    static readonly methodName = "GetProficienciesByIds";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByIdsRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusType {
    static readonly methodName = "GetProficienciesByGenusType";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByParentGenusType {
    static readonly methodName = "GetProficienciesByParentGenusType";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByRecordType {
    static readonly methodName = "GetProficienciesByRecordType";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesOnDate {
    static readonly methodName = "GetProficienciesOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeOnDate {
    static readonly methodName = "GetProficienciesByGenusTypeOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForObjective {
    static readonly methodName = "GetProficienciesForObjective";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForObjectiveOnDate {
    static readonly methodName = "GetProficienciesForObjectiveOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForObjectiveOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeForObjective {
    static readonly methodName = "GetProficienciesByGenusTypeForObjective";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeForObjectiveOnDate {
    static readonly methodName = "GetProficienciesByGenusTypeForObjectiveOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForObjectives {
    static readonly methodName = "GetProficienciesForObjectives";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForObjectivesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForResource {
    static readonly methodName = "GetProficienciesForResource";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForResourceRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForResourceOnDate {
    static readonly methodName = "GetProficienciesForResourceOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForResourceOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeForResource {
    static readonly methodName = "GetProficienciesByGenusTypeForResource";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeForResourceRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeForResourceOnDate {
    static readonly methodName = "GetProficienciesByGenusTypeForResourceOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeForResourceOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForResources {
    static readonly methodName = "GetProficienciesForResources";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForResourcesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForObjectiveAndResource {
    static readonly methodName = "GetProficienciesForObjectiveAndResource";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForObjectiveAndResourceRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesForObjectiveAndResourceOnDate {
    static readonly methodName = "GetProficienciesForObjectiveAndResourceOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesForObjectiveAndResourceOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeForObjectiveAndResource {
    static readonly methodName = "GetProficienciesByGenusTypeForObjectiveAndResource";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveAndResourceRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficienciesByGenusTypeForObjectiveAndResourceOnDate {
    static readonly methodName = "GetProficienciesByGenusTypeForObjectiveAndResourceOnDate";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
  export class GetProficiencies {
    static readonly methodName = "GetProficiencies";
    static readonly service = ProficiencyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
}
export class ProficiencyQuerySession {
  static serviceName = "dlkit.proto.learning.ProficiencyQuerySession";
}
export namespace ProficiencyQuerySession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanSearchProficiencies {
    static readonly methodName = "CanSearchProficiencies";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanSearchProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanSearchProficienciesReply;
  }
  export class UseFederatedObjectiveBankView {
    static readonly methodName = "UseFederatedObjectiveBankView";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseFederatedObjectiveBankViewReply;
  }
  export class UseIsolatedObjectiveBankView {
    static readonly methodName = "UseIsolatedObjectiveBankView";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseIsolatedObjectiveBankViewReply;
  }
  export class GetProficiencyQuery {
    static readonly methodName = "GetProficiencyQuery";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetProficiencyQueryRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetProficiencyQueryReply;
  }
  export class GetProficienciesByQuery {
    static readonly methodName = "GetProficienciesByQuery";
    static readonly service = ProficiencyQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetProficienciesByQueryRequest;
    static readonly responseType = dlkit_proto_learning_pb.Proficiency;
  }
}
export class ProficiencyAdminSession {
  static serviceName = "dlkit.proto.learning.ProficiencyAdminSession";
}
export namespace ProficiencyAdminSession {
  export class GetObjectiveBankId {
    static readonly methodName = "GetObjectiveBankId";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankIdReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class CanCreateProficiencies {
    static readonly methodName = "CanCreateProficiencies";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateProficienciesReply;
  }
  export class CanCreateProficiencyWithRecordTypes {
    static readonly methodName = "CanCreateProficiencyWithRecordTypes";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateProficiencyWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateProficiencyWithRecordTypesReply;
  }
  export class GetProficiencyFormForCreate {
    static readonly methodName = "GetProficiencyFormForCreate";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetProficiencyFormForCreateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetProficiencyFormForCreateReply;
  }
  export class CreateProficiency {
    static readonly methodName = "CreateProficiency";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CreateProficiencyRequest;
    static readonly responseType = dlkit_proto_learning_pb.CreateProficiencyReply;
  }
  export class CanUpdateProficiencies {
    static readonly methodName = "CanUpdateProficiencies";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanUpdateProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanUpdateProficienciesReply;
  }
  export class GetProficiencyFormForUpdate {
    static readonly methodName = "GetProficiencyFormForUpdate";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetProficiencyFormForUpdateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetProficiencyFormForUpdateReply;
  }
  export class UpdateProficiency {
    static readonly methodName = "UpdateProficiency";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UpdateProficiencyRequest;
    static readonly responseType = dlkit_proto_learning_pb.UpdateProficiencyReply;
  }
  export class CanDeleteProficiencies {
    static readonly methodName = "CanDeleteProficiencies";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanDeleteProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanDeleteProficienciesReply;
  }
  export class DeleteProficiency {
    static readonly methodName = "DeleteProficiency";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.DeleteProficiencyRequest;
    static readonly responseType = dlkit_proto_learning_pb.DeleteProficiencyReply;
  }
  export class DeleteProficiencies {
    static readonly methodName = "DeleteProficiencies";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.DeleteProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.DeleteProficienciesReply;
  }
  export class CanManageProficiencyAliases {
    static readonly methodName = "CanManageProficiencyAliases";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanManageProficiencyAliasesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanManageProficiencyAliasesReply;
  }
  export class AliasProficiency {
    static readonly methodName = "AliasProficiency";
    static readonly service = ProficiencyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AliasProficiencyRequest;
    static readonly responseType = dlkit_proto_learning_pb.AliasProficiencyReply;
  }
}
export class ProficiencyObjectiveBankAssignmentSession {
  static serviceName = "dlkit.proto.learning.ProficiencyObjectiveBankAssignmentSession";
}
export namespace ProficiencyObjectiveBankAssignmentSession {
  export class CanAssignProficiencies {
    static readonly methodName = "CanAssignProficiencies";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignProficienciesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignProficienciesReply;
  }
  export class CanAssignProficienciesToObjectiveBank {
    static readonly methodName = "CanAssignProficienciesToObjectiveBank";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAssignProficienciesToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAssignProficienciesToObjectiveBankReply;
  }
  export class GetAssignableObjectiveBankIds {
    static readonly methodName = "GetAssignableObjectiveBankIds";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableObjectiveBankIdsForProficiency {
    static readonly methodName = "GetAssignableObjectiveBankIdsForProficiency";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetAssignableObjectiveBankIdsForProficiencyRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignProficiencyToObjectiveBank {
    static readonly methodName = "AssignProficiencyToObjectiveBank";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AssignProficiencyToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.AssignProficiencyToObjectiveBankReply;
  }
  export class UnassignProficiencyFromObjectiveBank {
    static readonly methodName = "UnassignProficiencyFromObjectiveBank";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UnassignProficiencyFromObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.UnassignProficiencyFromObjectiveBankReply;
  }
  export class ReassignProficiencyToObjectiveBank {
    static readonly methodName = "ReassignProficiencyToObjectiveBank";
    static readonly service = ProficiencyObjectiveBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.ReassignProficiencyToObjectiveBankReply;
  }
}
export class ObjectiveBankLookupSession {
  static serviceName = "dlkit.proto.learning.ObjectiveBankLookupSession";
}
export namespace ObjectiveBankLookupSession {
  export class CanLookupObjectiveBanks {
    static readonly methodName = "CanLookupObjectiveBanks";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanLookupObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanLookupObjectiveBanksReply;
  }
  export class UseComparativeObjectiveBankView {
    static readonly methodName = "UseComparativeObjectiveBankView";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply;
  }
  export class UsePlenaryObjectiveBankView {
    static readonly methodName = "UsePlenaryObjectiveBankView";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply;
  }
  export class GetObjectiveBank {
    static readonly methodName = "GetObjectiveBank";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankReply;
  }
  export class GetObjectiveBanksByIds {
    static readonly methodName = "GetObjectiveBanksByIds";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByIdsRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class GetObjectiveBanksByGenusType {
    static readonly methodName = "GetObjectiveBanksByGenusType";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class GetObjectiveBanksByParentGenusType {
    static readonly methodName = "GetObjectiveBanksByParentGenusType";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class GetObjectiveBanksByRecordType {
    static readonly methodName = "GetObjectiveBanksByRecordType";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByRecordTypeRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class GetObjectiveBanksByProvider {
    static readonly methodName = "GetObjectiveBanksByProvider";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksByProviderRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class GetObjectiveBanks {
    static readonly methodName = "GetObjectiveBanks";
    static readonly service = ObjectiveBankLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
}
export class ObjectiveBankAdminSession {
  static serviceName = "dlkit.proto.learning.ObjectiveBankAdminSession";
}
export namespace ObjectiveBankAdminSession {
  export class CanCreateObjectiveBanks {
    static readonly methodName = "CanCreateObjectiveBanks";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateObjectiveBanksReply;
  }
  export class CanCreateObjectiveBankWithRecordTypes {
    static readonly methodName = "CanCreateObjectiveBankWithRecordTypes";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanCreateObjectiveBankWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanCreateObjectiveBankWithRecordTypesReply;
  }
  export class GetObjectiveBankFormForCreate {
    static readonly methodName = "GetObjectiveBankFormForCreate";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankFormForCreateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankFormForCreateReply;
  }
  export class CreateObjectiveBank {
    static readonly methodName = "CreateObjectiveBank";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CreateObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.CreateObjectiveBankReply;
  }
  export class CanUpdateObjectiveBanks {
    static readonly methodName = "CanUpdateObjectiveBanks";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanUpdateObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanUpdateObjectiveBanksReply;
  }
  export class GetObjectiveBankFormForUpdate {
    static readonly methodName = "GetObjectiveBankFormForUpdate";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankFormForUpdateRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankFormForUpdateReply;
  }
  export class UpdateObjectiveBank {
    static readonly methodName = "UpdateObjectiveBank";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UpdateObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.UpdateObjectiveBankReply;
  }
  export class CanDeleteObjectiveBanks {
    static readonly methodName = "CanDeleteObjectiveBanks";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanDeleteObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanDeleteObjectiveBanksReply;
  }
  export class DeleteObjectiveBank {
    static readonly methodName = "DeleteObjectiveBank";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.DeleteObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.DeleteObjectiveBankReply;
  }
  export class CanManageObjectiveBankAliases {
    static readonly methodName = "CanManageObjectiveBankAliases";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanManageObjectiveBankAliasesRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanManageObjectiveBankAliasesReply;
  }
  export class AliasObjectiveBank {
    static readonly methodName = "AliasObjectiveBank";
    static readonly service = ObjectiveBankAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AliasObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.AliasObjectiveBankReply;
  }
}
export class ObjectiveBankHierarchySession {
  static serviceName = "dlkit.proto.learning.ObjectiveBankHierarchySession";
}
export namespace ObjectiveBankHierarchySession {
  export class GetObjectiveBankHierarchyId {
    static readonly methodName = "GetObjectiveBankHierarchyId";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdReply;
  }
  export class GetObjectiveBankHierarchy {
    static readonly methodName = "GetObjectiveBankHierarchy";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyReply;
  }
  export class CanAccessObjectiveBankHierarchy {
    static readonly methodName = "CanAccessObjectiveBankHierarchy";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanAccessObjectiveBankHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanAccessObjectiveBankHierarchyReply;
  }
  export class UseComparativeObjectiveBankView {
    static readonly methodName = "UseComparativeObjectiveBankView";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UseComparativeObjectiveBankViewReply;
  }
  export class UsePlenaryObjectiveBankView {
    static readonly methodName = "UsePlenaryObjectiveBankView";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewRequest;
    static readonly responseType = dlkit_proto_learning_pb.UsePlenaryObjectiveBankViewReply;
  }
  export class GetRootObjectiveBankIds {
    static readonly methodName = "GetRootObjectiveBankIds";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetRootObjectiveBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootObjectiveBanks {
    static readonly methodName = "GetRootObjectiveBanks";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetRootObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class HasParentObjectiveBanks {
    static readonly methodName = "HasParentObjectiveBanks";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.HasParentObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.HasParentObjectiveBanksReply;
  }
  export class IsParentOfObjectiveBank {
    static readonly methodName = "IsParentOfObjectiveBank";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsParentOfObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsParentOfObjectiveBankReply;
  }
  export class GetParentObjectiveBankIds {
    static readonly methodName = "GetParentObjectiveBankIds";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetParentObjectiveBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentObjectiveBanks {
    static readonly methodName = "GetParentObjectiveBanks";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetParentObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class IsAncestorOfObjectiveBank {
    static readonly methodName = "IsAncestorOfObjectiveBank";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsAncestorOfObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsAncestorOfObjectiveBankReply;
  }
  export class HasChildObjectiveBanks {
    static readonly methodName = "HasChildObjectiveBanks";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.HasChildObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.HasChildObjectiveBanksReply;
  }
  export class IsChildOfObjectiveBank {
    static readonly methodName = "IsChildOfObjectiveBank";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsChildOfObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsChildOfObjectiveBankReply;
  }
  export class GetChildObjectiveBankIds {
    static readonly methodName = "GetChildObjectiveBankIds";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetChildObjectiveBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildObjectiveBanks {
    static readonly methodName = "GetChildObjectiveBanks";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_learning_pb.GetChildObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.ObjectiveBank;
  }
  export class IsDescendantOfObjectiveBank {
    static readonly methodName = "IsDescendantOfObjectiveBank";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.IsDescendantOfObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.IsDescendantOfObjectiveBankReply;
  }
  export class GetObjectiveBankNodeIds {
    static readonly methodName = "GetObjectiveBankNodeIds";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankNodeIdsRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankNodeIdsReply;
  }
  export class GetObjectiveBankNodes {
    static readonly methodName = "GetObjectiveBankNodes";
    static readonly service = ObjectiveBankHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankNodesRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankNodesReply;
  }
}
export class ObjectiveBankHierarchyDesignSession {
  static serviceName = "dlkit.proto.learning.ObjectiveBankHierarchyDesignSession";
}
export namespace ObjectiveBankHierarchyDesignSession {
  export class GetObjectiveBankHierarchyId {
    static readonly methodName = "GetObjectiveBankHierarchyId";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyIdReply;
  }
  export class GetObjectiveBankHierarchy {
    static readonly methodName = "GetObjectiveBankHierarchy";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.GetObjectiveBankHierarchyReply;
  }
  export class CanModifyObjectiveBankHierarchy {
    static readonly methodName = "CanModifyObjectiveBankHierarchy";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.CanModifyObjectiveBankHierarchyRequest;
    static readonly responseType = dlkit_proto_learning_pb.CanModifyObjectiveBankHierarchyReply;
  }
  export class AddRootObjectiveBank {
    static readonly methodName = "AddRootObjectiveBank";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AddRootObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.AddRootObjectiveBankReply;
  }
  export class RemoveRootObjectiveBank {
    static readonly methodName = "RemoveRootObjectiveBank";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.RemoveRootObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.RemoveRootObjectiveBankReply;
  }
  export class AddChildObjectiveBank {
    static readonly methodName = "AddChildObjectiveBank";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.AddChildObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.AddChildObjectiveBankReply;
  }
  export class RemoveChildObjectiveBank {
    static readonly methodName = "RemoveChildObjectiveBank";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.RemoveChildObjectiveBankRequest;
    static readonly responseType = dlkit_proto_learning_pb.RemoveChildObjectiveBankReply;
  }
  export class RemoveChildObjectiveBanks {
    static readonly methodName = "RemoveChildObjectiveBanks";
    static readonly service = ObjectiveBankHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_learning_pb.RemoveChildObjectiveBanksRequest;
    static readonly responseType = dlkit_proto_learning_pb.RemoveChildObjectiveBanksReply;
  }
}
