// package: dlkit.proto.hierarchy
// file: dlkit/proto/hierarchy.proto

var jspb = require("google-protobuf");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var HierarchyTraversalSession = {
  serviceName: "dlkit.proto.hierarchy.HierarchyTraversalSession"
};
HierarchyTraversalSession.GetHierarchyId = {
  methodName: "GetHierarchyId",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyIdRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyIdReply
};
HierarchyTraversalSession.GetHierarchy = {
  methodName: "GetHierarchy",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyReply
};
HierarchyTraversalSession.CanAccessHierarchy = {
  methodName: "CanAccessHierarchy",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanAccessHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.CanAccessHierarchyReply
};
HierarchyTraversalSession.GetRoots = {
  methodName: "GetRoots",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetRootsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
HierarchyTraversalSession.HasParents = {
  methodName: "HasParents",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.HasParentsRequest,
  responseType: dlkit_proto_hierarchy_pb.HasParentsReply
};
HierarchyTraversalSession.IsParent = {
  methodName: "IsParent",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.IsParentRequest,
  responseType: dlkit_proto_hierarchy_pb.IsParentReply
};
HierarchyTraversalSession.GetParents = {
  methodName: "GetParents",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetParentsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
HierarchyTraversalSession.IsAncestor = {
  methodName: "IsAncestor",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.IsAncestorRequest,
  responseType: dlkit_proto_hierarchy_pb.IsAncestorReply
};
HierarchyTraversalSession.HasChildren = {
  methodName: "HasChildren",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.HasChildrenRequest,
  responseType: dlkit_proto_hierarchy_pb.HasChildrenReply
};
HierarchyTraversalSession.IsChild = {
  methodName: "IsChild",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.IsChildRequest,
  responseType: dlkit_proto_hierarchy_pb.IsChildReply
};
HierarchyTraversalSession.GetChildren = {
  methodName: "GetChildren",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetChildrenRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
HierarchyTraversalSession.IsDescendant = {
  methodName: "IsDescendant",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.IsDescendantRequest,
  responseType: dlkit_proto_hierarchy_pb.IsDescendantReply
};
HierarchyTraversalSession.GetNodes = {
  methodName: "GetNodes",
  service: HierarchyTraversalSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetNodesRequest,
  responseType: dlkit_proto_hierarchy_pb.GetNodesReply
};
var HierarchyDesignSession = {
  serviceName: "dlkit.proto.hierarchy.HierarchyDesignSession"
};
HierarchyDesignSession.GetHierarchyId = {
  methodName: "GetHierarchyId",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyIdRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyIdReply
};
HierarchyDesignSession.GetHierarchy = {
  methodName: "GetHierarchy",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyReply
};
HierarchyDesignSession.CanModifyHierarchy = {
  methodName: "CanModifyHierarchy",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanModifyHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.CanModifyHierarchyReply
};
HierarchyDesignSession.AddRoot = {
  methodName: "AddRoot",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.AddRootRequest,
  responseType: dlkit_proto_hierarchy_pb.AddRootReply
};
HierarchyDesignSession.AddChild = {
  methodName: "AddChild",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.AddChildRequest,
  responseType: dlkit_proto_hierarchy_pb.AddChildReply
};
HierarchyDesignSession.RemoveRoot = {
  methodName: "RemoveRoot",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.RemoveRootRequest,
  responseType: dlkit_proto_hierarchy_pb.RemoveRootReply
};
HierarchyDesignSession.RemoveChild = {
  methodName: "RemoveChild",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.RemoveChildRequest,
  responseType: dlkit_proto_hierarchy_pb.RemoveChildReply
};
HierarchyDesignSession.RemoveChildren = {
  methodName: "RemoveChildren",
  service: HierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.RemoveChildrenRequest,
  responseType: dlkit_proto_hierarchy_pb.RemoveChildrenReply
};
var HierarchyLookupSession = {
  serviceName: "dlkit.proto.hierarchy.HierarchyLookupSession"
};
HierarchyLookupSession.CanLookupHierarchies = {
  methodName: "CanLookupHierarchies",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanLookupHierarchiesRequest,
  responseType: dlkit_proto_hierarchy_pb.CanLookupHierarchiesReply
};
HierarchyLookupSession.UseComparativeHierarchyView = {
  methodName: "UseComparativeHierarchyView",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.UseComparativeHierarchyViewRequest,
  responseType: dlkit_proto_hierarchy_pb.UseComparativeHierarchyViewReply
};
HierarchyLookupSession.UsePlenaryHierarchyView = {
  methodName: "UsePlenaryHierarchyView",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.UsePlenaryHierarchyViewRequest,
  responseType: dlkit_proto_hierarchy_pb.UsePlenaryHierarchyViewReply
};
HierarchyLookupSession.GetHierarchy = {
  methodName: "GetHierarchy",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyReply
};
HierarchyLookupSession.GetHierarchiesByIds = {
  methodName: "GetHierarchiesByIds",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchiesByIdsRequest,
  responseType: dlkit_proto_hierarchy_pb.Hierarchy
};
HierarchyLookupSession.GetHierarchiesByGenusType = {
  methodName: "GetHierarchiesByGenusType",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchiesByGenusTypeRequest,
  responseType: dlkit_proto_hierarchy_pb.Hierarchy
};
HierarchyLookupSession.GetHierarchiesByParentGenusType = {
  methodName: "GetHierarchiesByParentGenusType",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchiesByParentGenusTypeRequest,
  responseType: dlkit_proto_hierarchy_pb.Hierarchy
};
HierarchyLookupSession.GetHierarchiesByRecordType = {
  methodName: "GetHierarchiesByRecordType",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchiesByRecordTypeRequest,
  responseType: dlkit_proto_hierarchy_pb.Hierarchy
};
HierarchyLookupSession.GetHierarchiesByProvider = {
  methodName: "GetHierarchiesByProvider",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchiesByProviderRequest,
  responseType: dlkit_proto_hierarchy_pb.Hierarchy
};
HierarchyLookupSession.GetHierarchies = {
  methodName: "GetHierarchies",
  service: HierarchyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchiesRequest,
  responseType: dlkit_proto_hierarchy_pb.Hierarchy
};
var HierarchyAdminSession = {
  serviceName: "dlkit.proto.hierarchy.HierarchyAdminSession"
};
HierarchyAdminSession.CanCreateHierarchies = {
  methodName: "CanCreateHierarchies",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanCreateHierarchiesRequest,
  responseType: dlkit_proto_hierarchy_pb.CanCreateHierarchiesReply
};
HierarchyAdminSession.CanCreateHierarchyWithRecordTypes = {
  methodName: "CanCreateHierarchyWithRecordTypes",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanCreateHierarchyWithRecordTypesRequest,
  responseType: dlkit_proto_hierarchy_pb.CanCreateHierarchyWithRecordTypesReply
};
HierarchyAdminSession.GetHierarchyFormForCreate = {
  methodName: "GetHierarchyFormForCreate",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyFormForCreateRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyFormForCreateReply
};
HierarchyAdminSession.CreateHierarchy = {
  methodName: "CreateHierarchy",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CreateHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.CreateHierarchyReply
};
HierarchyAdminSession.CanUpdateHierarchies = {
  methodName: "CanUpdateHierarchies",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanUpdateHierarchiesRequest,
  responseType: dlkit_proto_hierarchy_pb.CanUpdateHierarchiesReply
};
HierarchyAdminSession.GetHierarchyFormForUpdate = {
  methodName: "GetHierarchyFormForUpdate",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.GetHierarchyFormForUpdateRequest,
  responseType: dlkit_proto_hierarchy_pb.GetHierarchyFormForUpdateReply
};
HierarchyAdminSession.UpdateHierarchy = {
  methodName: "UpdateHierarchy",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.UpdateHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.UpdateHierarchyReply
};
HierarchyAdminSession.CanDeleteHierarchies = {
  methodName: "CanDeleteHierarchies",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanDeleteHierarchiesRequest,
  responseType: dlkit_proto_hierarchy_pb.CanDeleteHierarchiesReply
};
HierarchyAdminSession.DeleteHierarchy = {
  methodName: "DeleteHierarchy",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.DeleteHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.DeleteHierarchyReply
};
HierarchyAdminSession.CanManageHierarchyAliases = {
  methodName: "CanManageHierarchyAliases",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.CanManageHierarchyAliasesRequest,
  responseType: dlkit_proto_hierarchy_pb.CanManageHierarchyAliasesReply
};
HierarchyAdminSession.AliasHierarchy = {
  methodName: "AliasHierarchy",
  service: HierarchyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_hierarchy_pb.AliasHierarchyRequest,
  responseType: dlkit_proto_hierarchy_pb.AliasHierarchyReply
};
module.exports = {
  HierarchyTraversalSession: HierarchyTraversalSession,
  HierarchyDesignSession: HierarchyDesignSession,
  HierarchyLookupSession: HierarchyLookupSession,
  HierarchyAdminSession: HierarchyAdminSession,
};

