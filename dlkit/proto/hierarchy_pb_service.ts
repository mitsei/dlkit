// package: dlkit.proto.hierarchy
// file: dlkit/proto/hierarchy.proto

import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
export class HierarchyTraversalSession {
  static serviceName = "dlkit.proto.hierarchy.HierarchyTraversalSession";
}
export namespace HierarchyTraversalSession {
  export class GetHierarchyId {
    static readonly methodName = "GetHierarchyId";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyIdRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyIdReply;
  }
  export class GetHierarchy {
    static readonly methodName = "GetHierarchy";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyReply;
  }
  export class CanAccessHierarchy {
    static readonly methodName = "CanAccessHierarchy";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanAccessHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanAccessHierarchyReply;
  }
  export class GetRoots {
    static readonly methodName = "GetRoots";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetRootsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class HasParents {
    static readonly methodName = "HasParents";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.HasParentsRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.HasParentsReply;
  }
  export class IsParent {
    static readonly methodName = "IsParent";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.IsParentRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.IsParentReply;
  }
  export class GetParents {
    static readonly methodName = "GetParents";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetParentsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class IsAncestor {
    static readonly methodName = "IsAncestor";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.IsAncestorRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.IsAncestorReply;
  }
  export class HasChildren {
    static readonly methodName = "HasChildren";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.HasChildrenRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.HasChildrenReply;
  }
  export class IsChild {
    static readonly methodName = "IsChild";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.IsChildRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.IsChildReply;
  }
  export class GetChildren {
    static readonly methodName = "GetChildren";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetChildrenRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class IsDescendant {
    static readonly methodName = "IsDescendant";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.IsDescendantRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.IsDescendantReply;
  }
  export class GetNodes {
    static readonly methodName = "GetNodes";
    static readonly service = HierarchyTraversalSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetNodesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetNodesReply;
  }
}
export class HierarchyDesignSession {
  static serviceName = "dlkit.proto.hierarchy.HierarchyDesignSession";
}
export namespace HierarchyDesignSession {
  export class GetHierarchyId {
    static readonly methodName = "GetHierarchyId";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyIdRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyIdReply;
  }
  export class GetHierarchy {
    static readonly methodName = "GetHierarchy";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyReply;
  }
  export class CanModifyHierarchy {
    static readonly methodName = "CanModifyHierarchy";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanModifyHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanModifyHierarchyReply;
  }
  export class AddRoot {
    static readonly methodName = "AddRoot";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.AddRootRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.AddRootReply;
  }
  export class AddChild {
    static readonly methodName = "AddChild";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.AddChildRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.AddChildReply;
  }
  export class RemoveRoot {
    static readonly methodName = "RemoveRoot";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.RemoveRootRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.RemoveRootReply;
  }
  export class RemoveChild {
    static readonly methodName = "RemoveChild";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.RemoveChildRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.RemoveChildReply;
  }
  export class RemoveChildren {
    static readonly methodName = "RemoveChildren";
    static readonly service = HierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.RemoveChildrenRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.RemoveChildrenReply;
  }
}
export class HierarchyLookupSession {
  static serviceName = "dlkit.proto.hierarchy.HierarchyLookupSession";
}
export namespace HierarchyLookupSession {
  export class CanLookupHierarchies {
    static readonly methodName = "CanLookupHierarchies";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanLookupHierarchiesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanLookupHierarchiesReply;
  }
  export class UseComparativeHierarchyView {
    static readonly methodName = "UseComparativeHierarchyView";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.UseComparativeHierarchyViewRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.UseComparativeHierarchyViewReply;
  }
  export class UsePlenaryHierarchyView {
    static readonly methodName = "UsePlenaryHierarchyView";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.UsePlenaryHierarchyViewRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.UsePlenaryHierarchyViewReply;
  }
  export class GetHierarchy {
    static readonly methodName = "GetHierarchy";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyReply;
  }
  export class GetHierarchiesByIds {
    static readonly methodName = "GetHierarchiesByIds";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchiesByIdsRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.Hierarchy;
  }
  export class GetHierarchiesByGenusType {
    static readonly methodName = "GetHierarchiesByGenusType";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchiesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.Hierarchy;
  }
  export class GetHierarchiesByParentGenusType {
    static readonly methodName = "GetHierarchiesByParentGenusType";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchiesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.Hierarchy;
  }
  export class GetHierarchiesByRecordType {
    static readonly methodName = "GetHierarchiesByRecordType";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchiesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.Hierarchy;
  }
  export class GetHierarchiesByProvider {
    static readonly methodName = "GetHierarchiesByProvider";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchiesByProviderRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.Hierarchy;
  }
  export class GetHierarchies {
    static readonly methodName = "GetHierarchies";
    static readonly service = HierarchyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchiesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.Hierarchy;
  }
}
export class HierarchyAdminSession {
  static serviceName = "dlkit.proto.hierarchy.HierarchyAdminSession";
}
export namespace HierarchyAdminSession {
  export class CanCreateHierarchies {
    static readonly methodName = "CanCreateHierarchies";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanCreateHierarchiesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanCreateHierarchiesReply;
  }
  export class CanCreateHierarchyWithRecordTypes {
    static readonly methodName = "CanCreateHierarchyWithRecordTypes";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanCreateHierarchyWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanCreateHierarchyWithRecordTypesReply;
  }
  export class GetHierarchyFormForCreate {
    static readonly methodName = "GetHierarchyFormForCreate";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyFormForCreateRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyFormForCreateReply;
  }
  export class CreateHierarchy {
    static readonly methodName = "CreateHierarchy";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CreateHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CreateHierarchyReply;
  }
  export class CanUpdateHierarchies {
    static readonly methodName = "CanUpdateHierarchies";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanUpdateHierarchiesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanUpdateHierarchiesReply;
  }
  export class GetHierarchyFormForUpdate {
    static readonly methodName = "GetHierarchyFormForUpdate";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.GetHierarchyFormForUpdateRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.GetHierarchyFormForUpdateReply;
  }
  export class UpdateHierarchy {
    static readonly methodName = "UpdateHierarchy";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.UpdateHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.UpdateHierarchyReply;
  }
  export class CanDeleteHierarchies {
    static readonly methodName = "CanDeleteHierarchies";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanDeleteHierarchiesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanDeleteHierarchiesReply;
  }
  export class DeleteHierarchy {
    static readonly methodName = "DeleteHierarchy";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.DeleteHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.DeleteHierarchyReply;
  }
  export class CanManageHierarchyAliases {
    static readonly methodName = "CanManageHierarchyAliases";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.CanManageHierarchyAliasesRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.CanManageHierarchyAliasesReply;
  }
  export class AliasHierarchy {
    static readonly methodName = "AliasHierarchy";
    static readonly service = HierarchyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_hierarchy_pb.AliasHierarchyRequest;
    static readonly responseType = dlkit_proto_hierarchy_pb.AliasHierarchyReply;
  }
}
