// package: dlkit.proto.authorization
// file: dlkit/proto/authorization.proto

import * as dlkit_proto_authorization_pb from "../../dlkit/proto/authorization_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class AuthorizationSession {
  static serviceName = "dlkit.proto.authorization.AuthorizationSession";
}
export namespace AuthorizationSession {
  export class GetVaultId {
    static readonly methodName = "GetVaultId";
    static readonly service = AuthorizationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultIdRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultIdReply;
  }
  export class GetVault {
    static readonly methodName = "GetVault";
    static readonly service = AuthorizationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultReply;
  }
  export class CanAccessAuthorizations {
    static readonly methodName = "CanAccessAuthorizations";
    static readonly service = AuthorizationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanAccessAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanAccessAuthorizationsReply;
  }
  export class IsAuthorized {
    static readonly methodName = "IsAuthorized";
    static readonly service = AuthorizationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.IsAuthorizedRequest;
    static readonly responseType = dlkit_proto_authorization_pb.IsAuthorizedReply;
  }
  export class GetAuthorizationCondition {
    static readonly methodName = "GetAuthorizationCondition";
    static readonly service = AuthorizationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationConditionRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationConditionReply;
  }
  export class IsAuthorizedOnCondition {
    static readonly methodName = "IsAuthorizedOnCondition";
    static readonly service = AuthorizationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.IsAuthorizedOnConditionRequest;
    static readonly responseType = dlkit_proto_authorization_pb.IsAuthorizedOnConditionReply;
  }
}
export class AuthorizationLookupSession {
  static serviceName = "dlkit.proto.authorization.AuthorizationLookupSession";
}
export namespace AuthorizationLookupSession {
  export class GetVaultId {
    static readonly methodName = "GetVaultId";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultIdRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultIdReply;
  }
  export class GetVault {
    static readonly methodName = "GetVault";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultReply;
  }
  export class CanLookupAuthorizations {
    static readonly methodName = "CanLookupAuthorizations";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanLookupAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanLookupAuthorizationsReply;
  }
  export class UseComparativeAuthorizationView {
    static readonly methodName = "UseComparativeAuthorizationView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseComparativeAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseComparativeAuthorizationViewReply;
  }
  export class UsePlenaryAuthorizationView {
    static readonly methodName = "UsePlenaryAuthorizationView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UsePlenaryAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UsePlenaryAuthorizationViewReply;
  }
  export class UseFederatedVaultView {
    static readonly methodName = "UseFederatedVaultView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseFederatedVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseFederatedVaultViewReply;
  }
  export class UseIsolatedVaultView {
    static readonly methodName = "UseIsolatedVaultView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseIsolatedVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseIsolatedVaultViewReply;
  }
  export class UseEffectiveAuthorizationView {
    static readonly methodName = "UseEffectiveAuthorizationView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseEffectiveAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseEffectiveAuthorizationViewReply;
  }
  export class UseAnyEffectiveAuthorizationView {
    static readonly methodName = "UseAnyEffectiveAuthorizationView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseAnyEffectiveAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseAnyEffectiveAuthorizationViewReply;
  }
  export class UseImplicitAuthorizationView {
    static readonly methodName = "UseImplicitAuthorizationView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseImplicitAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseImplicitAuthorizationViewReply;
  }
  export class UseExplicitAuthorizationView {
    static readonly methodName = "UseExplicitAuthorizationView";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseExplicitAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseExplicitAuthorizationViewReply;
  }
  export class GetAuthorization {
    static readonly methodName = "GetAuthorization";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationReply;
  }
  export class GetAuthorizationsByIds {
    static readonly methodName = "GetAuthorizationsByIds";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByIdsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsByGenusType {
    static readonly methodName = "GetAuthorizationsByGenusType";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsByParentGenusType {
    static readonly methodName = "GetAuthorizationsByParentGenusType";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsByRecordType {
    static readonly methodName = "GetAuthorizationsByRecordType";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsOnDate {
    static readonly methodName = "GetAuthorizationsOnDate";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsOnDateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForResource {
    static readonly methodName = "GetAuthorizationsForResource";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForResourceRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForResourceOnDate {
    static readonly methodName = "GetAuthorizationsForResourceOnDate";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForResourceOnDateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForAgent {
    static readonly methodName = "GetAuthorizationsForAgent";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForAgentRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForAgentOnDate {
    static readonly methodName = "GetAuthorizationsForAgentOnDate";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForAgentOnDateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForFunction {
    static readonly methodName = "GetAuthorizationsForFunction";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForFunctionRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForFunctionOnDate {
    static readonly methodName = "GetAuthorizationsForFunctionOnDate";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForFunctionOnDateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForResourceAndFunction {
    static readonly methodName = "GetAuthorizationsForResourceAndFunction";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForResourceAndFunctionRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForResourceAndFunctionOnDate {
    static readonly methodName = "GetAuthorizationsForResourceAndFunctionOnDate";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForResourceAndFunctionOnDateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForAgentAndFunction {
    static readonly methodName = "GetAuthorizationsForAgentAndFunction";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForAgentAndFunctionRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsForAgentAndFunctionOnDate {
    static readonly methodName = "GetAuthorizationsForAgentAndFunctionOnDate";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsForAgentAndFunctionOnDateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsByQualifier {
    static readonly methodName = "GetAuthorizationsByQualifier";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByQualifierRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetExplicitAuthorization {
    static readonly methodName = "GetExplicitAuthorization";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetExplicitAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetExplicitAuthorizationReply;
  }
  export class GetAuthorizations {
    static readonly methodName = "GetAuthorizations";
    static readonly service = AuthorizationLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
}
export class AuthorizationQuerySession {
  static serviceName = "dlkit.proto.authorization.AuthorizationQuerySession";
}
export namespace AuthorizationQuerySession {
  export class GetVaultId {
    static readonly methodName = "GetVaultId";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultIdRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultIdReply;
  }
  export class GetVault {
    static readonly methodName = "GetVault";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultReply;
  }
  export class CanSearchAuthorizations {
    static readonly methodName = "CanSearchAuthorizations";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanSearchAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanSearchAuthorizationsReply;
  }
  export class UseFederatedVaultView {
    static readonly methodName = "UseFederatedVaultView";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseFederatedVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseFederatedVaultViewReply;
  }
  export class UseIsolatedVaultView {
    static readonly methodName = "UseIsolatedVaultView";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseIsolatedVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseIsolatedVaultViewReply;
  }
  export class UseImplicitAuthorizationView {
    static readonly methodName = "UseImplicitAuthorizationView";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseImplicitAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseImplicitAuthorizationViewReply;
  }
  export class UseExplicitAuthorizationView {
    static readonly methodName = "UseExplicitAuthorizationView";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseExplicitAuthorizationViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseExplicitAuthorizationViewReply;
  }
  export class GetAuthorizationQuery {
    static readonly methodName = "GetAuthorizationQuery";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationQueryRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationQueryReply;
  }
  export class GetAuthorizationsByQuery {
    static readonly methodName = "GetAuthorizationsByQuery";
    static readonly service = AuthorizationQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByQueryRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
}
export class AuthorizationAdminSession {
  static serviceName = "dlkit.proto.authorization.AuthorizationAdminSession";
}
export namespace AuthorizationAdminSession {
  export class GetVaultId {
    static readonly methodName = "GetVaultId";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultIdRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultIdReply;
  }
  export class GetVault {
    static readonly methodName = "GetVault";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultReply;
  }
  export class CanCreateAuthorizations {
    static readonly methodName = "CanCreateAuthorizations";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanCreateAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanCreateAuthorizationsReply;
  }
  export class CanCreateAuthorizationWithRecordTypes {
    static readonly methodName = "CanCreateAuthorizationWithRecordTypes";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanCreateAuthorizationWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanCreateAuthorizationWithRecordTypesReply;
  }
  export class GetAuthorizationFormForCreateForAgent {
    static readonly methodName = "GetAuthorizationFormForCreateForAgent";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForAgentRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForAgentReply;
  }
  export class GetAuthorizationFormForCreateForResource {
    static readonly methodName = "GetAuthorizationFormForCreateForResource";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceReply;
  }
  export class GetAuthorizationFormForCreateForResourceAndTrust {
    static readonly methodName = "GetAuthorizationFormForCreateForResourceAndTrust";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceAndTrustRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceAndTrustReply;
  }
  export class CreateAuthorization {
    static readonly methodName = "CreateAuthorization";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CreateAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CreateAuthorizationReply;
  }
  export class CanUpdateAuthorizations {
    static readonly methodName = "CanUpdateAuthorizations";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanUpdateAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanUpdateAuthorizationsReply;
  }
  export class GetAuthorizationFormForUpdate {
    static readonly methodName = "GetAuthorizationFormForUpdate";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationFormForUpdateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetAuthorizationFormForUpdateReply;
  }
  export class UpdateAuthorization {
    static readonly methodName = "UpdateAuthorization";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UpdateAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UpdateAuthorizationReply;
  }
  export class CanDeleteAuthorizations {
    static readonly methodName = "CanDeleteAuthorizations";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanDeleteAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanDeleteAuthorizationsReply;
  }
  export class DeleteAuthorization {
    static readonly methodName = "DeleteAuthorization";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.DeleteAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.DeleteAuthorizationReply;
  }
  export class CanManageAuthorizationAliases {
    static readonly methodName = "CanManageAuthorizationAliases";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanManageAuthorizationAliasesRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanManageAuthorizationAliasesReply;
  }
  export class AliasAuthorization {
    static readonly methodName = "AliasAuthorization";
    static readonly service = AuthorizationAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.AliasAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.AliasAuthorizationReply;
  }
}
export class AuthorizationVaultSession {
  static serviceName = "dlkit.proto.authorization.AuthorizationVaultSession";
}
export namespace AuthorizationVaultSession {
  export class UseComparativeVaultView {
    static readonly methodName = "UseComparativeVaultView";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseComparativeVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseComparativeVaultViewReply;
  }
  export class UsePlenaryVaultView {
    static readonly methodName = "UsePlenaryVaultView";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UsePlenaryVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UsePlenaryVaultViewReply;
  }
  export class CanLookupAuthorizationVaultMappings {
    static readonly methodName = "CanLookupAuthorizationVaultMappings";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanLookupAuthorizationVaultMappingsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanLookupAuthorizationVaultMappingsReply;
  }
  export class GetAuthorizationIdsByVault {
    static readonly methodName = "GetAuthorizationIdsByVault";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationIdsByVaultRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAuthorizationsByVault {
    static readonly methodName = "GetAuthorizationsByVault";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsByVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Authorization;
  }
  export class GetAuthorizationsIdsByVault {
    static readonly methodName = "GetAuthorizationsIdsByVault";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAuthorizationsIdsByVaultRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetVaultIdsByAuthorization {
    static readonly methodName = "GetVaultIdsByAuthorization";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultIdsByAuthorizationRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetVaultByAuthorization {
    static readonly methodName = "GetVaultByAuthorization";
    static readonly service = AuthorizationVaultSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultByAuthorizationRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
}
export class AuthorizationVaultAssignmentSession {
  static serviceName = "dlkit.proto.authorization.AuthorizationVaultAssignmentSession";
}
export namespace AuthorizationVaultAssignmentSession {
  export class CanAssignAuthorizations {
    static readonly methodName = "CanAssignAuthorizations";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanAssignAuthorizationsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanAssignAuthorizationsReply;
  }
  export class CanAssignAuthorizationsToVault {
    static readonly methodName = "CanAssignAuthorizationsToVault";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanAssignAuthorizationsToVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanAssignAuthorizationsToVaultReply;
  }
  export class GetAssignableVaultIds {
    static readonly methodName = "GetAssignableVaultIds";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAssignableVaultIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableVaultIdsForAuthorization {
    static readonly methodName = "GetAssignableVaultIdsForAuthorization";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetAssignableVaultIdsForAuthorizationRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignAuthorizationToVault {
    static readonly methodName = "AssignAuthorizationToVault";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.AssignAuthorizationToVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.AssignAuthorizationToVaultReply;
  }
  export class UnassignAuthorizationFromVault {
    static readonly methodName = "UnassignAuthorizationFromVault";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UnassignAuthorizationFromVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UnassignAuthorizationFromVaultReply;
  }
  export class ReassignAuthorizationToVault {
    static readonly methodName = "ReassignAuthorizationToVault";
    static readonly service = AuthorizationVaultAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.ReassignAuthorizationToVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.ReassignAuthorizationToVaultReply;
  }
}
export class VaultLookupSession {
  static serviceName = "dlkit.proto.authorization.VaultLookupSession";
}
export namespace VaultLookupSession {
  export class CanLookupVaults {
    static readonly methodName = "CanLookupVaults";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanLookupVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanLookupVaultsReply;
  }
  export class UseComparativeVaultView {
    static readonly methodName = "UseComparativeVaultView";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseComparativeVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseComparativeVaultViewReply;
  }
  export class UsePlenaryVaultView {
    static readonly methodName = "UsePlenaryVaultView";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UsePlenaryVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UsePlenaryVaultViewReply;
  }
  export class GetVault {
    static readonly methodName = "GetVault";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultReply;
  }
  export class GetVaultsByIds {
    static readonly methodName = "GetVaultsByIds";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsByIdsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class GetVaultsByGenusType {
    static readonly methodName = "GetVaultsByGenusType";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class GetVaultsByParentGenusType {
    static readonly methodName = "GetVaultsByParentGenusType";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class GetVaultsByRecordType {
    static readonly methodName = "GetVaultsByRecordType";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class GetVaultsByProvider {
    static readonly methodName = "GetVaultsByProvider";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsByProviderRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class GetVaults {
    static readonly methodName = "GetVaults";
    static readonly service = VaultLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
}
export class VaultQuerySession {
  static serviceName = "dlkit.proto.authorization.VaultQuerySession";
}
export namespace VaultQuerySession {
  export class CanSearchVaults {
    static readonly methodName = "CanSearchVaults";
    static readonly service = VaultQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanSearchVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanSearchVaultsReply;
  }
  export class GetVaultQuery {
    static readonly methodName = "GetVaultQuery";
    static readonly service = VaultQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultQueryRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultQueryReply;
  }
  export class GetVaultsByQuery {
    static readonly methodName = "GetVaultsByQuery";
    static readonly service = VaultQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultsByQueryRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
}
export class VaultAdminSession {
  static serviceName = "dlkit.proto.authorization.VaultAdminSession";
}
export namespace VaultAdminSession {
  export class CanCreateVaults {
    static readonly methodName = "CanCreateVaults";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanCreateVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanCreateVaultsReply;
  }
  export class CanCreateVaultWithRecordTypes {
    static readonly methodName = "CanCreateVaultWithRecordTypes";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanCreateVaultWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanCreateVaultWithRecordTypesReply;
  }
  export class GetVaultFormForCreate {
    static readonly methodName = "GetVaultFormForCreate";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultFormForCreateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultFormForCreateReply;
  }
  export class CreateVault {
    static readonly methodName = "CreateVault";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CreateVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CreateVaultReply;
  }
  export class CanUpdateVaults {
    static readonly methodName = "CanUpdateVaults";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanUpdateVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanUpdateVaultsReply;
  }
  export class GetVaultFormForUpdate {
    static readonly methodName = "GetVaultFormForUpdate";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultFormForUpdateRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultFormForUpdateReply;
  }
  export class UpdateVault {
    static readonly methodName = "UpdateVault";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UpdateVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UpdateVaultReply;
  }
  export class CanDeleteVaults {
    static readonly methodName = "CanDeleteVaults";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanDeleteVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanDeleteVaultsReply;
  }
  export class DeleteVault {
    static readonly methodName = "DeleteVault";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.DeleteVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.DeleteVaultReply;
  }
  export class CanManageVaultAliases {
    static readonly methodName = "CanManageVaultAliases";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanManageVaultAliasesRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanManageVaultAliasesReply;
  }
  export class AliasVault {
    static readonly methodName = "AliasVault";
    static readonly service = VaultAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.AliasVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.AliasVaultReply;
  }
}
export class VaultHierarchySession {
  static serviceName = "dlkit.proto.authorization.VaultHierarchySession";
}
export namespace VaultHierarchySession {
  export class GetVaultHierarchyId {
    static readonly methodName = "GetVaultHierarchyId";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultHierarchyIdRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultHierarchyIdReply;
  }
  export class GetVaultHierarchy {
    static readonly methodName = "GetVaultHierarchy";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultHierarchyRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultHierarchyReply;
  }
  export class CanAccessVaultHierarchy {
    static readonly methodName = "CanAccessVaultHierarchy";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanAccessVaultHierarchyRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanAccessVaultHierarchyReply;
  }
  export class UseComparativeVaultView {
    static readonly methodName = "UseComparativeVaultView";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UseComparativeVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UseComparativeVaultViewReply;
  }
  export class UsePlenaryVaultView {
    static readonly methodName = "UsePlenaryVaultView";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.UsePlenaryVaultViewRequest;
    static readonly responseType = dlkit_proto_authorization_pb.UsePlenaryVaultViewReply;
  }
  export class GetRootVaultIds {
    static readonly methodName = "GetRootVaultIds";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetRootVaultIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootVaults {
    static readonly methodName = "GetRootVaults";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetRootVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class HasParentVaults {
    static readonly methodName = "HasParentVaults";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.HasParentVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.HasParentVaultsReply;
  }
  export class IsParentOfVault {
    static readonly methodName = "IsParentOfVault";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.IsParentOfVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.IsParentOfVaultReply;
  }
  export class GetParentVaultIds {
    static readonly methodName = "GetParentVaultIds";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetParentVaultIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentVaults {
    static readonly methodName = "GetParentVaults";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetParentVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class IsAncestorOfVault {
    static readonly methodName = "IsAncestorOfVault";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.IsAncestorOfVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.IsAncestorOfVaultReply;
  }
  export class HasChildVaults {
    static readonly methodName = "HasChildVaults";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.HasChildVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.HasChildVaultsReply;
  }
  export class IsChildOfVault {
    static readonly methodName = "IsChildOfVault";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.IsChildOfVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.IsChildOfVaultReply;
  }
  export class GetChildVaultIds {
    static readonly methodName = "GetChildVaultIds";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetChildVaultIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildVaults {
    static readonly methodName = "GetChildVaults";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authorization_pb.GetChildVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.Vault;
  }
  export class IsDescendantOfVault {
    static readonly methodName = "IsDescendantOfVault";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.IsDescendantOfVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.IsDescendantOfVaultReply;
  }
  export class GetVaultNodeIds {
    static readonly methodName = "GetVaultNodeIds";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultNodeIdsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultNodeIdsReply;
  }
  export class GetVaultNodes {
    static readonly methodName = "GetVaultNodes";
    static readonly service = VaultHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultNodesRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultNodesReply;
  }
}
export class VaultHierarchyDesignSession {
  static serviceName = "dlkit.proto.authorization.VaultHierarchyDesignSession";
}
export namespace VaultHierarchyDesignSession {
  export class GetVaultHierarchyId {
    static readonly methodName = "GetVaultHierarchyId";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultHierarchyIdRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultHierarchyIdReply;
  }
  export class GetVaultHierarchy {
    static readonly methodName = "GetVaultHierarchy";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.GetVaultHierarchyRequest;
    static readonly responseType = dlkit_proto_authorization_pb.GetVaultHierarchyReply;
  }
  export class CanModifyVaultHierarchy {
    static readonly methodName = "CanModifyVaultHierarchy";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.CanModifyVaultHierarchyRequest;
    static readonly responseType = dlkit_proto_authorization_pb.CanModifyVaultHierarchyReply;
  }
  export class AddRootVault {
    static readonly methodName = "AddRootVault";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.AddRootVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.AddRootVaultReply;
  }
  export class RemoveRootVault {
    static readonly methodName = "RemoveRootVault";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.RemoveRootVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.RemoveRootVaultReply;
  }
  export class AddChildVault {
    static readonly methodName = "AddChildVault";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.AddChildVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.AddChildVaultReply;
  }
  export class RemoveChildVault {
    static readonly methodName = "RemoveChildVault";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.RemoveChildVaultRequest;
    static readonly responseType = dlkit_proto_authorization_pb.RemoveChildVaultReply;
  }
  export class RemoveChildVaults {
    static readonly methodName = "RemoveChildVaults";
    static readonly service = VaultHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authorization_pb.RemoveChildVaultsRequest;
    static readonly responseType = dlkit_proto_authorization_pb.RemoveChildVaultsReply;
  }
}
