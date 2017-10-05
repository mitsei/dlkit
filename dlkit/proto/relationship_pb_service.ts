// package: dlkit.proto.relationship
// file: dlkit/proto/relationship.proto

import * as dlkit_proto_relationship_pb from "../../dlkit/proto/relationship_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class RelationshipLookupSession {
  static serviceName = "dlkit.proto.relationship.RelationshipLookupSession";
}
export namespace RelationshipLookupSession {
  export class GetFamilyId {
    static readonly methodName = "GetFamilyId";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyIdRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyIdReply;
  }
  export class GetFamily {
    static readonly methodName = "GetFamily";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyReply;
  }
  export class CanLookupRelationships {
    static readonly methodName = "CanLookupRelationships";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanLookupRelationshipsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanLookupRelationshipsReply;
  }
  export class UseComparativeRelationshipView {
    static readonly methodName = "UseComparativeRelationshipView";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseComparativeRelationshipViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseComparativeRelationshipViewReply;
  }
  export class UsePlenaryRelationshipView {
    static readonly methodName = "UsePlenaryRelationshipView";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UsePlenaryRelationshipViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UsePlenaryRelationshipViewReply;
  }
  export class UseFederatedFamilyView {
    static readonly methodName = "UseFederatedFamilyView";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseFederatedFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseFederatedFamilyViewReply;
  }
  export class UseIsolatedFamilyView {
    static readonly methodName = "UseIsolatedFamilyView";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseIsolatedFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseIsolatedFamilyViewReply;
  }
  export class UseEffectiveRelationshipView {
    static readonly methodName = "UseEffectiveRelationshipView";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseEffectiveRelationshipViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseEffectiveRelationshipViewReply;
  }
  export class UseAnyEffectiveRelationshipView {
    static readonly methodName = "UseAnyEffectiveRelationshipView";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseAnyEffectiveRelationshipViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseAnyEffectiveRelationshipViewReply;
  }
  export class GetRelationship {
    static readonly methodName = "GetRelationship";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetRelationshipReply;
  }
  export class GetRelationshipsByIds {
    static readonly methodName = "GetRelationshipsByIds";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByIdsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusType {
    static readonly methodName = "GetRelationshipsByGenusType";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByParentGenusType {
    static readonly methodName = "GetRelationshipsByParentGenusType";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByRecordType {
    static readonly methodName = "GetRelationshipsByRecordType";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsOnDate {
    static readonly methodName = "GetRelationshipsOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsForSource {
    static readonly methodName = "GetRelationshipsForSource";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsForSourceRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsForSourceOnDate {
    static readonly methodName = "GetRelationshipsForSourceOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsForSourceOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusTypeForSource {
    static readonly methodName = "GetRelationshipsByGenusTypeForSource";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForSourceRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusTypeForSourceOnDate {
    static readonly methodName = "GetRelationshipsByGenusTypeForSourceOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForSourceOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsForDestination {
    static readonly methodName = "GetRelationshipsForDestination";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsForDestinationRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsForDestinationOnDate {
    static readonly methodName = "GetRelationshipsForDestinationOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsForDestinationOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusTypeForDestination {
    static readonly methodName = "GetRelationshipsByGenusTypeForDestination";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForDestinationRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusTypeForDestinationOnDate {
    static readonly methodName = "GetRelationshipsByGenusTypeForDestinationOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForDestinationOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsForPeers {
    static readonly methodName = "GetRelationshipsForPeers";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsForPeersRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsForPeersOnDate {
    static readonly methodName = "GetRelationshipsForPeersOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsForPeersOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusTypeForPeers {
    static readonly methodName = "GetRelationshipsByGenusTypeForPeers";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForPeersRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationshipsByGenusTypeForPeersOnDate {
    static readonly methodName = "GetRelationshipsByGenusTypeForPeersOnDate";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByGenusTypeForPeersOnDateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
  export class GetRelationships {
    static readonly methodName = "GetRelationships";
    static readonly service = RelationshipLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
}
export class RelationshipQuerySession {
  static serviceName = "dlkit.proto.relationship.RelationshipQuerySession";
}
export namespace RelationshipQuerySession {
  export class GetFamilyId {
    static readonly methodName = "GetFamilyId";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyIdRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyIdReply;
  }
  export class GetFamily {
    static readonly methodName = "GetFamily";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyReply;
  }
  export class UseFederatedFamilyView {
    static readonly methodName = "UseFederatedFamilyView";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseFederatedFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseFederatedFamilyViewReply;
  }
  export class UseIsolatedFamilyView {
    static readonly methodName = "UseIsolatedFamilyView";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseIsolatedFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseIsolatedFamilyViewReply;
  }
  export class CanSearchRelationships {
    static readonly methodName = "CanSearchRelationships";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanSearchRelationshipsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanSearchRelationshipsReply;
  }
  export class GetRelationshipQuery {
    static readonly methodName = "GetRelationshipQuery";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipQueryRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetRelationshipQueryReply;
  }
  export class GetRelationshipsByQuery {
    static readonly methodName = "GetRelationshipsByQuery";
    static readonly service = RelationshipQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipsByQueryRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Relationship;
  }
}
export class RelationshipAdminSession {
  static serviceName = "dlkit.proto.relationship.RelationshipAdminSession";
}
export namespace RelationshipAdminSession {
  export class GetFamilyId {
    static readonly methodName = "GetFamilyId";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyIdRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyIdReply;
  }
  export class GetFamily {
    static readonly methodName = "GetFamily";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyReply;
  }
  export class CanCreateRelationships {
    static readonly methodName = "CanCreateRelationships";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanCreateRelationshipsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanCreateRelationshipsReply;
  }
  export class CanCreateRelationshipWithRecordTypes {
    static readonly methodName = "CanCreateRelationshipWithRecordTypes";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanCreateRelationshipWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanCreateRelationshipWithRecordTypesReply;
  }
  export class GetRelationshipFormForCreate {
    static readonly methodName = "GetRelationshipFormForCreate";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipFormForCreateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetRelationshipFormForCreateReply;
  }
  export class CreateRelationship {
    static readonly methodName = "CreateRelationship";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CreateRelationshipRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CreateRelationshipReply;
  }
  export class CanUpdateRelationships {
    static readonly methodName = "CanUpdateRelationships";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanUpdateRelationshipsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanUpdateRelationshipsReply;
  }
  export class GetRelationshipFormForUpdate {
    static readonly methodName = "GetRelationshipFormForUpdate";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetRelationshipFormForUpdateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetRelationshipFormForUpdateReply;
  }
  export class UpdateRelationship {
    static readonly methodName = "UpdateRelationship";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UpdateRelationshipRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UpdateRelationshipReply;
  }
  export class CanDeleteRelationships {
    static readonly methodName = "CanDeleteRelationships";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanDeleteRelationshipsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanDeleteRelationshipsReply;
  }
  export class DeleteRelationship {
    static readonly methodName = "DeleteRelationship";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.DeleteRelationshipRequest;
    static readonly responseType = dlkit_proto_relationship_pb.DeleteRelationshipReply;
  }
  export class CanManageRelationshipAliases {
    static readonly methodName = "CanManageRelationshipAliases";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanManageRelationshipAliasesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanManageRelationshipAliasesReply;
  }
  export class AliasRelationship {
    static readonly methodName = "AliasRelationship";
    static readonly service = RelationshipAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.AliasRelationshipRequest;
    static readonly responseType = dlkit_proto_relationship_pb.AliasRelationshipReply;
  }
}
export class FamilyLookupSession {
  static serviceName = "dlkit.proto.relationship.FamilyLookupSession";
}
export namespace FamilyLookupSession {
  export class CanLookupFamilies {
    static readonly methodName = "CanLookupFamilies";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanLookupFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanLookupFamiliesReply;
  }
  export class UseComparativeFamilyView {
    static readonly methodName = "UseComparativeFamilyView";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseComparativeFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseComparativeFamilyViewReply;
  }
  export class UsePlenaryFamilyView {
    static readonly methodName = "UsePlenaryFamilyView";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UsePlenaryFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UsePlenaryFamilyViewReply;
  }
  export class GetFamily {
    static readonly methodName = "GetFamily";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyReply;
  }
  export class GetFamiliesByIds {
    static readonly methodName = "GetFamiliesByIds";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamiliesByIdsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class GetFamiliesByGenusType {
    static readonly methodName = "GetFamiliesByGenusType";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamiliesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class GetFamiliesByParentGenusType {
    static readonly methodName = "GetFamiliesByParentGenusType";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamiliesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class GetFamiliesByRecordType {
    static readonly methodName = "GetFamiliesByRecordType";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamiliesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class GetFamiliesByProvider {
    static readonly methodName = "GetFamiliesByProvider";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamiliesByProviderRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class GetFamilies {
    static readonly methodName = "GetFamilies";
    static readonly service = FamilyLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
}
export class FamilyAdminSession {
  static serviceName = "dlkit.proto.relationship.FamilyAdminSession";
}
export namespace FamilyAdminSession {
  export class CanCreateFamilies {
    static readonly methodName = "CanCreateFamilies";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanCreateFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanCreateFamiliesReply;
  }
  export class CanCreateFamilyWithRecordTypes {
    static readonly methodName = "CanCreateFamilyWithRecordTypes";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanCreateFamilyWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanCreateFamilyWithRecordTypesReply;
  }
  export class GetFamilyFormForCreate {
    static readonly methodName = "GetFamilyFormForCreate";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyFormForCreateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyFormForCreateReply;
  }
  export class CreateFamily {
    static readonly methodName = "CreateFamily";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CreateFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CreateFamilyReply;
  }
  export class CanUpdateFamilies {
    static readonly methodName = "CanUpdateFamilies";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanUpdateFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanUpdateFamiliesReply;
  }
  export class GetFamilyFormForUpdate {
    static readonly methodName = "GetFamilyFormForUpdate";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyFormForUpdateRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyFormForUpdateReply;
  }
  export class UpdateFamily {
    static readonly methodName = "UpdateFamily";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UpdateFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UpdateFamilyReply;
  }
  export class CanDeleteFamilies {
    static readonly methodName = "CanDeleteFamilies";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanDeleteFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanDeleteFamiliesReply;
  }
  export class DeleteFamily {
    static readonly methodName = "DeleteFamily";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.DeleteFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.DeleteFamilyReply;
  }
  export class CanManageFamilyAliases {
    static readonly methodName = "CanManageFamilyAliases";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanManageFamilyAliasesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanManageFamilyAliasesReply;
  }
  export class AliasFamily {
    static readonly methodName = "AliasFamily";
    static readonly service = FamilyAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.AliasFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.AliasFamilyReply;
  }
}
export class FamilyHierarchySession {
  static serviceName = "dlkit.proto.relationship.FamilyHierarchySession";
}
export namespace FamilyHierarchySession {
  export class GetFamilyHierarchyId {
    static readonly methodName = "GetFamilyHierarchyId";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyHierarchyIdRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyHierarchyIdReply;
  }
  export class GetFamilyHierarchy {
    static readonly methodName = "GetFamilyHierarchy";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyHierarchyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyHierarchyReply;
  }
  export class CanAccessFamilyHierarchy {
    static readonly methodName = "CanAccessFamilyHierarchy";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanAccessFamilyHierarchyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanAccessFamilyHierarchyReply;
  }
  export class UseComparativeFamilyView {
    static readonly methodName = "UseComparativeFamilyView";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UseComparativeFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UseComparativeFamilyViewReply;
  }
  export class UsePlenaryFamilyView {
    static readonly methodName = "UsePlenaryFamilyView";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.UsePlenaryFamilyViewRequest;
    static readonly responseType = dlkit_proto_relationship_pb.UsePlenaryFamilyViewReply;
  }
  export class GetRootFamilyIds {
    static readonly methodName = "GetRootFamilyIds";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRootFamilyIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootFamilies {
    static readonly methodName = "GetRootFamilies";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetRootFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class HasParentFamilies {
    static readonly methodName = "HasParentFamilies";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.HasParentFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.HasParentFamiliesReply;
  }
  export class IsParentOfFamily {
    static readonly methodName = "IsParentOfFamily";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.IsParentOfFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.IsParentOfFamilyReply;
  }
  export class GetParentFamilyIds {
    static readonly methodName = "GetParentFamilyIds";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetParentFamilyIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentFamilies {
    static readonly methodName = "GetParentFamilies";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetParentFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class IsAncestorOfFamily {
    static readonly methodName = "IsAncestorOfFamily";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.IsAncestorOfFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.IsAncestorOfFamilyReply;
  }
  export class HasChildFamilies {
    static readonly methodName = "HasChildFamilies";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.HasChildFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.HasChildFamiliesReply;
  }
  export class IsChildOfFamily {
    static readonly methodName = "IsChildOfFamily";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.IsChildOfFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.IsChildOfFamilyReply;
  }
  export class GetChildFamilyIds {
    static readonly methodName = "GetChildFamilyIds";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetChildFamilyIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildFamilies {
    static readonly methodName = "GetChildFamilies";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_relationship_pb.GetChildFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.Family;
  }
  export class IsDescendantOfFamily {
    static readonly methodName = "IsDescendantOfFamily";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.IsDescendantOfFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.IsDescendantOfFamilyReply;
  }
  export class GetFamilyNodeIds {
    static readonly methodName = "GetFamilyNodeIds";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyNodeIdsRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyNodeIdsReply;
  }
  export class GetFamilyNodes {
    static readonly methodName = "GetFamilyNodes";
    static readonly service = FamilyHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyNodesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyNodesReply;
  }
}
export class FamilyHierarchyDesignSession {
  static serviceName = "dlkit.proto.relationship.FamilyHierarchyDesignSession";
}
export namespace FamilyHierarchyDesignSession {
  export class GetFamilyHierarchyId {
    static readonly methodName = "GetFamilyHierarchyId";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyHierarchyIdRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyHierarchyIdReply;
  }
  export class GetFamilyHierarchy {
    static readonly methodName = "GetFamilyHierarchy";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.GetFamilyHierarchyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.GetFamilyHierarchyReply;
  }
  export class CanModifyFamilyHierarchy {
    static readonly methodName = "CanModifyFamilyHierarchy";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.CanModifyFamilyHierarchyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.CanModifyFamilyHierarchyReply;
  }
  export class AddRootFamily {
    static readonly methodName = "AddRootFamily";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.AddRootFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.AddRootFamilyReply;
  }
  export class RemoveRootFamily {
    static readonly methodName = "RemoveRootFamily";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.RemoveRootFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.RemoveRootFamilyReply;
  }
  export class AddChildFamily {
    static readonly methodName = "AddChildFamily";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.AddChildFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.AddChildFamilyReply;
  }
  export class RemoveChildFamily {
    static readonly methodName = "RemoveChildFamily";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.RemoveChildFamilyRequest;
    static readonly responseType = dlkit_proto_relationship_pb.RemoveChildFamilyReply;
  }
  export class RemoveChildFamilies {
    static readonly methodName = "RemoveChildFamilies";
    static readonly service = FamilyHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_relationship_pb.RemoveChildFamiliesRequest;
    static readonly responseType = dlkit_proto_relationship_pb.RemoveChildFamiliesReply;
  }
}
