// package: dlkit.proto.relationship
// file: dlkit/proto/relationship.proto

var jspb = require("google-protobuf");
var dlkit_proto_relationship_pb = require("../../dlkit/proto/relationship_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var RelationshipLookupSession = {
  serviceName: "dlkit.proto.relationship.RelationshipLookupSession"
};
RelationshipLookupSession.GetFamilyId = {
  methodName: "GetFamilyId",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyIdRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyIdReply
};
RelationshipLookupSession.GetFamily = {
  methodName: "GetFamily",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyReply
};
RelationshipLookupSession.CanLookupRelationships = {
  methodName: "CanLookupRelationships",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanLookupRelationshipsRequest,
  responseType: dlkit_proto_relationship_pb.CanLookupRelationshipsReply
};
RelationshipLookupSession.UseComparativeRelationshipView = {
  methodName: "UseComparativeRelationshipView",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseComparativeRelationshipViewRequest,
  responseType: dlkit_proto_relationship_pb.UseComparativeRelationshipViewReply
};
RelationshipLookupSession.UsePlenaryRelationshipView = {
  methodName: "UsePlenaryRelationshipView",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UsePlenaryRelationshipViewRequest,
  responseType: dlkit_proto_relationship_pb.UsePlenaryRelationshipViewReply
};
RelationshipLookupSession.UseFederatedFamilyView = {
  methodName: "UseFederatedFamilyView",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseFederatedFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UseFederatedFamilyViewReply
};
RelationshipLookupSession.UseIsolatedFamilyView = {
  methodName: "UseIsolatedFamilyView",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseIsolatedFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UseIsolatedFamilyViewReply
};
RelationshipLookupSession.UseEffectiveRelationshipView = {
  methodName: "UseEffectiveRelationshipView",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseEffectiveRelationshipViewRequest,
  responseType: dlkit_proto_relationship_pb.UseEffectiveRelationshipViewReply
};
RelationshipLookupSession.UseAnyEffectiveRelationshipView = {
  methodName: "UseAnyEffectiveRelationshipView",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseAnyEffectiveRelationshipViewRequest,
  responseType: dlkit_proto_relationship_pb.UseAnyEffectiveRelationshipViewReply
};
RelationshipLookupSession.GetRelationship = {
  methodName: "GetRelationship",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetRelationshipRequest,
  responseType: dlkit_proto_relationship_pb.GetRelationshipReply
};
RelationshipLookupSession.GetRelationshipsByIds = {
  methodName: "GetRelationshipsByIds",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByIdsRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusType = {
  methodName: "GetRelationshipsByGenusType",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByParentGenusType = {
  methodName: "GetRelationshipsByParentGenusType",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByParentGenusTypeRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByRecordType = {
  methodName: "GetRelationshipsByRecordType",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByRecordTypeRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsOnDate = {
  methodName: "GetRelationshipsOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsForSource = {
  methodName: "GetRelationshipsForSource",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsForSourceRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsForSourceOnDate = {
  methodName: "GetRelationshipsForSourceOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsForSourceOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusTypeForSource = {
  methodName: "GetRelationshipsByGenusTypeForSource",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForSourceRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusTypeForSourceOnDate = {
  methodName: "GetRelationshipsByGenusTypeForSourceOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForSourceOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsForDestination = {
  methodName: "GetRelationshipsForDestination",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsForDestinationRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsForDestinationOnDate = {
  methodName: "GetRelationshipsForDestinationOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsForDestinationOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusTypeForDestination = {
  methodName: "GetRelationshipsByGenusTypeForDestination",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForDestinationRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusTypeForDestinationOnDate = {
  methodName: "GetRelationshipsByGenusTypeForDestinationOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForDestinationOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsForPeers = {
  methodName: "GetRelationshipsForPeers",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsForPeersRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsForPeersOnDate = {
  methodName: "GetRelationshipsForPeersOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsForPeersOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusTypeForPeers = {
  methodName: "GetRelationshipsByGenusTypeForPeers",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForPeersRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationshipsByGenusTypeForPeersOnDate = {
  methodName: "GetRelationshipsByGenusTypeForPeersOnDate",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForPeersOnDateRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
RelationshipLookupSession.GetRelationships = {
  methodName: "GetRelationships",
  service: RelationshipLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
var RelationshipQuerySession = {
  serviceName: "dlkit.proto.relationship.RelationshipQuerySession"
};
RelationshipQuerySession.GetFamilyId = {
  methodName: "GetFamilyId",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyIdRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyIdReply
};
RelationshipQuerySession.GetFamily = {
  methodName: "GetFamily",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyReply
};
RelationshipQuerySession.UseFederatedFamilyView = {
  methodName: "UseFederatedFamilyView",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseFederatedFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UseFederatedFamilyViewReply
};
RelationshipQuerySession.UseIsolatedFamilyView = {
  methodName: "UseIsolatedFamilyView",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseIsolatedFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UseIsolatedFamilyViewReply
};
RelationshipQuerySession.CanSearchRelationships = {
  methodName: "CanSearchRelationships",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanSearchRelationshipsRequest,
  responseType: dlkit_proto_relationship_pb.CanSearchRelationshipsReply
};
RelationshipQuerySession.GetRelationshipQuery = {
  methodName: "GetRelationshipQuery",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetRelationshipQueryRequest,
  responseType: dlkit_proto_relationship_pb.GetRelationshipQueryReply
};
RelationshipQuerySession.GetRelationshipsByQuery = {
  methodName: "GetRelationshipsByQuery",
  service: RelationshipQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRelationshipsByQueryRequest,
  responseType: dlkit_proto_relationship_pb.Relationship
};
var RelationshipAdminSession = {
  serviceName: "dlkit.proto.relationship.RelationshipAdminSession"
};
RelationshipAdminSession.GetFamilyId = {
  methodName: "GetFamilyId",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyIdRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyIdReply
};
RelationshipAdminSession.GetFamily = {
  methodName: "GetFamily",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyReply
};
RelationshipAdminSession.CanCreateRelationships = {
  methodName: "CanCreateRelationships",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanCreateRelationshipsRequest,
  responseType: dlkit_proto_relationship_pb.CanCreateRelationshipsReply
};
RelationshipAdminSession.CanCreateRelationshipWithRecordTypes = {
  methodName: "CanCreateRelationshipWithRecordTypes",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanCreateRelationshipWithRecordTypesRequest,
  responseType: dlkit_proto_relationship_pb.CanCreateRelationshipWithRecordTypesReply
};
RelationshipAdminSession.GetRelationshipFormForCreate = {
  methodName: "GetRelationshipFormForCreate",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetRelationshipFormForCreateRequest,
  responseType: dlkit_proto_relationship_pb.GetRelationshipFormForCreateReply
};
RelationshipAdminSession.CreateRelationship = {
  methodName: "CreateRelationship",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CreateRelationshipRequest,
  responseType: dlkit_proto_relationship_pb.CreateRelationshipReply
};
RelationshipAdminSession.CanUpdateRelationships = {
  methodName: "CanUpdateRelationships",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanUpdateRelationshipsRequest,
  responseType: dlkit_proto_relationship_pb.CanUpdateRelationshipsReply
};
RelationshipAdminSession.GetRelationshipFormForUpdate = {
  methodName: "GetRelationshipFormForUpdate",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetRelationshipFormForUpdateRequest,
  responseType: dlkit_proto_relationship_pb.GetRelationshipFormForUpdateReply
};
RelationshipAdminSession.UpdateRelationship = {
  methodName: "UpdateRelationship",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UpdateRelationshipRequest,
  responseType: dlkit_proto_relationship_pb.UpdateRelationshipReply
};
RelationshipAdminSession.CanDeleteRelationships = {
  methodName: "CanDeleteRelationships",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanDeleteRelationshipsRequest,
  responseType: dlkit_proto_relationship_pb.CanDeleteRelationshipsReply
};
RelationshipAdminSession.DeleteRelationship = {
  methodName: "DeleteRelationship",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.DeleteRelationshipRequest,
  responseType: dlkit_proto_relationship_pb.DeleteRelationshipReply
};
RelationshipAdminSession.CanManageRelationshipAliases = {
  methodName: "CanManageRelationshipAliases",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanManageRelationshipAliasesRequest,
  responseType: dlkit_proto_relationship_pb.CanManageRelationshipAliasesReply
};
RelationshipAdminSession.AliasRelationship = {
  methodName: "AliasRelationship",
  service: RelationshipAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.AliasRelationshipRequest,
  responseType: dlkit_proto_relationship_pb.AliasRelationshipReply
};
var FamilyLookupSession = {
  serviceName: "dlkit.proto.relationship.FamilyLookupSession"
};
FamilyLookupSession.CanLookupFamilies = {
  methodName: "CanLookupFamilies",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanLookupFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.CanLookupFamiliesReply
};
FamilyLookupSession.UseComparativeFamilyView = {
  methodName: "UseComparativeFamilyView",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseComparativeFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UseComparativeFamilyViewReply
};
FamilyLookupSession.UsePlenaryFamilyView = {
  methodName: "UsePlenaryFamilyView",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UsePlenaryFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UsePlenaryFamilyViewReply
};
FamilyLookupSession.GetFamily = {
  methodName: "GetFamily",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyReply
};
FamilyLookupSession.GetFamiliesByIds = {
  methodName: "GetFamiliesByIds",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetFamiliesByIdsRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyLookupSession.GetFamiliesByGenusType = {
  methodName: "GetFamiliesByGenusType",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetFamiliesByGenusTypeRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyLookupSession.GetFamiliesByParentGenusType = {
  methodName: "GetFamiliesByParentGenusType",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetFamiliesByParentGenusTypeRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyLookupSession.GetFamiliesByRecordType = {
  methodName: "GetFamiliesByRecordType",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetFamiliesByRecordTypeRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyLookupSession.GetFamiliesByProvider = {
  methodName: "GetFamiliesByProvider",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetFamiliesByProviderRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyLookupSession.GetFamilies = {
  methodName: "GetFamilies",
  service: FamilyLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
var FamilyAdminSession = {
  serviceName: "dlkit.proto.relationship.FamilyAdminSession"
};
FamilyAdminSession.CanCreateFamilies = {
  methodName: "CanCreateFamilies",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanCreateFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.CanCreateFamiliesReply
};
FamilyAdminSession.CanCreateFamilyWithRecordTypes = {
  methodName: "CanCreateFamilyWithRecordTypes",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanCreateFamilyWithRecordTypesRequest,
  responseType: dlkit_proto_relationship_pb.CanCreateFamilyWithRecordTypesReply
};
FamilyAdminSession.GetFamilyFormForCreate = {
  methodName: "GetFamilyFormForCreate",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyFormForCreateRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyFormForCreateReply
};
FamilyAdminSession.CreateFamily = {
  methodName: "CreateFamily",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CreateFamilyRequest,
  responseType: dlkit_proto_relationship_pb.CreateFamilyReply
};
FamilyAdminSession.CanUpdateFamilies = {
  methodName: "CanUpdateFamilies",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanUpdateFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.CanUpdateFamiliesReply
};
FamilyAdminSession.GetFamilyFormForUpdate = {
  methodName: "GetFamilyFormForUpdate",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyFormForUpdateRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyFormForUpdateReply
};
FamilyAdminSession.UpdateFamily = {
  methodName: "UpdateFamily",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UpdateFamilyRequest,
  responseType: dlkit_proto_relationship_pb.UpdateFamilyReply
};
FamilyAdminSession.CanDeleteFamilies = {
  methodName: "CanDeleteFamilies",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanDeleteFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.CanDeleteFamiliesReply
};
FamilyAdminSession.DeleteFamily = {
  methodName: "DeleteFamily",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.DeleteFamilyRequest,
  responseType: dlkit_proto_relationship_pb.DeleteFamilyReply
};
FamilyAdminSession.CanManageFamilyAliases = {
  methodName: "CanManageFamilyAliases",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanManageFamilyAliasesRequest,
  responseType: dlkit_proto_relationship_pb.CanManageFamilyAliasesReply
};
FamilyAdminSession.AliasFamily = {
  methodName: "AliasFamily",
  service: FamilyAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.AliasFamilyRequest,
  responseType: dlkit_proto_relationship_pb.AliasFamilyReply
};
var FamilyHierarchySession = {
  serviceName: "dlkit.proto.relationship.FamilyHierarchySession"
};
FamilyHierarchySession.GetFamilyHierarchyId = {
  methodName: "GetFamilyHierarchyId",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyHierarchyIdRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyHierarchyIdReply
};
FamilyHierarchySession.GetFamilyHierarchy = {
  methodName: "GetFamilyHierarchy",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyHierarchyRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyHierarchyReply
};
FamilyHierarchySession.CanAccessFamilyHierarchy = {
  methodName: "CanAccessFamilyHierarchy",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanAccessFamilyHierarchyRequest,
  responseType: dlkit_proto_relationship_pb.CanAccessFamilyHierarchyReply
};
FamilyHierarchySession.UseComparativeFamilyView = {
  methodName: "UseComparativeFamilyView",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UseComparativeFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UseComparativeFamilyViewReply
};
FamilyHierarchySession.UsePlenaryFamilyView = {
  methodName: "UsePlenaryFamilyView",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.UsePlenaryFamilyViewRequest,
  responseType: dlkit_proto_relationship_pb.UsePlenaryFamilyViewReply
};
FamilyHierarchySession.GetRootFamilyIds = {
  methodName: "GetRootFamilyIds",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRootFamilyIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
FamilyHierarchySession.GetRootFamilies = {
  methodName: "GetRootFamilies",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetRootFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyHierarchySession.HasParentFamilies = {
  methodName: "HasParentFamilies",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.HasParentFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.HasParentFamiliesReply
};
FamilyHierarchySession.IsParentOfFamily = {
  methodName: "IsParentOfFamily",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.IsParentOfFamilyRequest,
  responseType: dlkit_proto_relationship_pb.IsParentOfFamilyReply
};
FamilyHierarchySession.GetParentFamilyIds = {
  methodName: "GetParentFamilyIds",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetParentFamilyIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
FamilyHierarchySession.GetParentFamilies = {
  methodName: "GetParentFamilies",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetParentFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyHierarchySession.IsAncestorOfFamily = {
  methodName: "IsAncestorOfFamily",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.IsAncestorOfFamilyRequest,
  responseType: dlkit_proto_relationship_pb.IsAncestorOfFamilyReply
};
FamilyHierarchySession.HasChildFamilies = {
  methodName: "HasChildFamilies",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.HasChildFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.HasChildFamiliesReply
};
FamilyHierarchySession.IsChildOfFamily = {
  methodName: "IsChildOfFamily",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.IsChildOfFamilyRequest,
  responseType: dlkit_proto_relationship_pb.IsChildOfFamilyReply
};
FamilyHierarchySession.GetChildFamilyIds = {
  methodName: "GetChildFamilyIds",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetChildFamilyIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
FamilyHierarchySession.GetChildFamilies = {
  methodName: "GetChildFamilies",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_relationship_pb.GetChildFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.Family
};
FamilyHierarchySession.IsDescendantOfFamily = {
  methodName: "IsDescendantOfFamily",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.IsDescendantOfFamilyRequest,
  responseType: dlkit_proto_relationship_pb.IsDescendantOfFamilyReply
};
FamilyHierarchySession.GetFamilyNodeIds = {
  methodName: "GetFamilyNodeIds",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyNodeIdsRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyNodeIdsReply
};
FamilyHierarchySession.GetFamilyNodes = {
  methodName: "GetFamilyNodes",
  service: FamilyHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyNodesRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyNodesReply
};
var FamilyHierarchyDesignSession = {
  serviceName: "dlkit.proto.relationship.FamilyHierarchyDesignSession"
};
FamilyHierarchyDesignSession.GetFamilyHierarchyId = {
  methodName: "GetFamilyHierarchyId",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyHierarchyIdRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyHierarchyIdReply
};
FamilyHierarchyDesignSession.GetFamilyHierarchy = {
  methodName: "GetFamilyHierarchy",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.GetFamilyHierarchyRequest,
  responseType: dlkit_proto_relationship_pb.GetFamilyHierarchyReply
};
FamilyHierarchyDesignSession.CanModifyFamilyHierarchy = {
  methodName: "CanModifyFamilyHierarchy",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.CanModifyFamilyHierarchyRequest,
  responseType: dlkit_proto_relationship_pb.CanModifyFamilyHierarchyReply
};
FamilyHierarchyDesignSession.AddRootFamily = {
  methodName: "AddRootFamily",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.AddRootFamilyRequest,
  responseType: dlkit_proto_relationship_pb.AddRootFamilyReply
};
FamilyHierarchyDesignSession.RemoveRootFamily = {
  methodName: "RemoveRootFamily",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.RemoveRootFamilyRequest,
  responseType: dlkit_proto_relationship_pb.RemoveRootFamilyReply
};
FamilyHierarchyDesignSession.AddChildFamily = {
  methodName: "AddChildFamily",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.AddChildFamilyRequest,
  responseType: dlkit_proto_relationship_pb.AddChildFamilyReply
};
FamilyHierarchyDesignSession.RemoveChildFamily = {
  methodName: "RemoveChildFamily",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.RemoveChildFamilyRequest,
  responseType: dlkit_proto_relationship_pb.RemoveChildFamilyReply
};
FamilyHierarchyDesignSession.RemoveChildFamilies = {
  methodName: "RemoveChildFamilies",
  service: FamilyHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_relationship_pb.RemoveChildFamiliesRequest,
  responseType: dlkit_proto_relationship_pb.RemoveChildFamiliesReply
};
module.exports = {
  RelationshipLookupSession: RelationshipLookupSession,
  RelationshipQuerySession: RelationshipQuerySession,
  RelationshipAdminSession: RelationshipAdminSession,
  FamilyLookupSession: FamilyLookupSession,
  FamilyAdminSession: FamilyAdminSession,
  FamilyHierarchySession: FamilyHierarchySession,
  FamilyHierarchyDesignSession: FamilyHierarchyDesignSession,
};

