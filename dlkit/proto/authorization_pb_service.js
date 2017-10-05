// package: dlkit.proto.authorization
// file: dlkit/proto/authorization.proto

var jspb = require("google-protobuf");
var dlkit_proto_authorization_pb = require("../../dlkit/proto/authorization_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var AuthorizationSession = {
  serviceName: "dlkit.proto.authorization.AuthorizationSession"
};
AuthorizationSession.GetVaultId = {
  methodName: "GetVaultId",
  service: AuthorizationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultIdRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultIdReply
};
AuthorizationSession.GetVault = {
  methodName: "GetVault",
  service: AuthorizationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultReply
};
AuthorizationSession.CanAccessAuthorizations = {
  methodName: "CanAccessAuthorizations",
  service: AuthorizationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanAccessAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanAccessAuthorizationsReply
};
AuthorizationSession.IsAuthorized = {
  methodName: "IsAuthorized",
  service: AuthorizationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.IsAuthorizedRequest,
  responseType: dlkit_proto_authorization_pb.IsAuthorizedReply
};
AuthorizationSession.GetAuthorizationCondition = {
  methodName: "GetAuthorizationCondition",
  service: AuthorizationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationConditionRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationConditionReply
};
AuthorizationSession.IsAuthorizedOnCondition = {
  methodName: "IsAuthorizedOnCondition",
  service: AuthorizationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.IsAuthorizedOnConditionRequest,
  responseType: dlkit_proto_authorization_pb.IsAuthorizedOnConditionReply
};
var AuthorizationLookupSession = {
  serviceName: "dlkit.proto.authorization.AuthorizationLookupSession"
};
AuthorizationLookupSession.GetVaultId = {
  methodName: "GetVaultId",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultIdRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultIdReply
};
AuthorizationLookupSession.GetVault = {
  methodName: "GetVault",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultReply
};
AuthorizationLookupSession.CanLookupAuthorizations = {
  methodName: "CanLookupAuthorizations",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanLookupAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanLookupAuthorizationsReply
};
AuthorizationLookupSession.UseComparativeAuthorizationView = {
  methodName: "UseComparativeAuthorizationView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseComparativeAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseComparativeAuthorizationViewReply
};
AuthorizationLookupSession.UsePlenaryAuthorizationView = {
  methodName: "UsePlenaryAuthorizationView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UsePlenaryAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UsePlenaryAuthorizationViewReply
};
AuthorizationLookupSession.UseFederatedVaultView = {
  methodName: "UseFederatedVaultView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseFederatedVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseFederatedVaultViewReply
};
AuthorizationLookupSession.UseIsolatedVaultView = {
  methodName: "UseIsolatedVaultView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseIsolatedVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseIsolatedVaultViewReply
};
AuthorizationLookupSession.UseEffectiveAuthorizationView = {
  methodName: "UseEffectiveAuthorizationView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseEffectiveAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseEffectiveAuthorizationViewReply
};
AuthorizationLookupSession.UseAnyEffectiveAuthorizationView = {
  methodName: "UseAnyEffectiveAuthorizationView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseAnyEffectiveAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseAnyEffectiveAuthorizationViewReply
};
AuthorizationLookupSession.UseImplicitAuthorizationView = {
  methodName: "UseImplicitAuthorizationView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseImplicitAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseImplicitAuthorizationViewReply
};
AuthorizationLookupSession.UseExplicitAuthorizationView = {
  methodName: "UseExplicitAuthorizationView",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseExplicitAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseExplicitAuthorizationViewReply
};
AuthorizationLookupSession.GetAuthorization = {
  methodName: "GetAuthorization",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationReply
};
AuthorizationLookupSession.GetAuthorizationsByIds = {
  methodName: "GetAuthorizationsByIds",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByIdsRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsByGenusType = {
  methodName: "GetAuthorizationsByGenusType",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByGenusTypeRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsByParentGenusType = {
  methodName: "GetAuthorizationsByParentGenusType",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByParentGenusTypeRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsByRecordType = {
  methodName: "GetAuthorizationsByRecordType",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByRecordTypeRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsOnDate = {
  methodName: "GetAuthorizationsOnDate",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsOnDateRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForResource = {
  methodName: "GetAuthorizationsForResource",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForResourceRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForResourceOnDate = {
  methodName: "GetAuthorizationsForResourceOnDate",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForResourceOnDateRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForAgent = {
  methodName: "GetAuthorizationsForAgent",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForAgentRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForAgentOnDate = {
  methodName: "GetAuthorizationsForAgentOnDate",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForAgentOnDateRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForFunction = {
  methodName: "GetAuthorizationsForFunction",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForFunctionRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForFunctionOnDate = {
  methodName: "GetAuthorizationsForFunctionOnDate",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForFunctionOnDateRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForResourceAndFunction = {
  methodName: "GetAuthorizationsForResourceAndFunction",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForResourceAndFunctionRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForResourceAndFunctionOnDate = {
  methodName: "GetAuthorizationsForResourceAndFunctionOnDate",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForResourceAndFunctionOnDateRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForAgentAndFunction = {
  methodName: "GetAuthorizationsForAgentAndFunction",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForAgentAndFunctionRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsForAgentAndFunctionOnDate = {
  methodName: "GetAuthorizationsForAgentAndFunctionOnDate",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsForAgentAndFunctionOnDateRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetAuthorizationsByQualifier = {
  methodName: "GetAuthorizationsByQualifier",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByQualifierRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationLookupSession.GetExplicitAuthorization = {
  methodName: "GetExplicitAuthorization",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetExplicitAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.GetExplicitAuthorizationReply
};
AuthorizationLookupSession.GetAuthorizations = {
  methodName: "GetAuthorizations",
  service: AuthorizationLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
var AuthorizationQuerySession = {
  serviceName: "dlkit.proto.authorization.AuthorizationQuerySession"
};
AuthorizationQuerySession.GetVaultId = {
  methodName: "GetVaultId",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultIdRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultIdReply
};
AuthorizationQuerySession.GetVault = {
  methodName: "GetVault",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultReply
};
AuthorizationQuerySession.CanSearchAuthorizations = {
  methodName: "CanSearchAuthorizations",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanSearchAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanSearchAuthorizationsReply
};
AuthorizationQuerySession.UseFederatedVaultView = {
  methodName: "UseFederatedVaultView",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseFederatedVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseFederatedVaultViewReply
};
AuthorizationQuerySession.UseIsolatedVaultView = {
  methodName: "UseIsolatedVaultView",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseIsolatedVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseIsolatedVaultViewReply
};
AuthorizationQuerySession.UseImplicitAuthorizationView = {
  methodName: "UseImplicitAuthorizationView",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseImplicitAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseImplicitAuthorizationViewReply
};
AuthorizationQuerySession.UseExplicitAuthorizationView = {
  methodName: "UseExplicitAuthorizationView",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseExplicitAuthorizationViewRequest,
  responseType: dlkit_proto_authorization_pb.UseExplicitAuthorizationViewReply
};
AuthorizationQuerySession.GetAuthorizationQuery = {
  methodName: "GetAuthorizationQuery",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationQueryRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationQueryReply
};
AuthorizationQuerySession.GetAuthorizationsByQuery = {
  methodName: "GetAuthorizationsByQuery",
  service: AuthorizationQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByQueryRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
var AuthorizationAdminSession = {
  serviceName: "dlkit.proto.authorization.AuthorizationAdminSession"
};
AuthorizationAdminSession.GetVaultId = {
  methodName: "GetVaultId",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultIdRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultIdReply
};
AuthorizationAdminSession.GetVault = {
  methodName: "GetVault",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultReply
};
AuthorizationAdminSession.CanCreateAuthorizations = {
  methodName: "CanCreateAuthorizations",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanCreateAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanCreateAuthorizationsReply
};
AuthorizationAdminSession.CanCreateAuthorizationWithRecordTypes = {
  methodName: "CanCreateAuthorizationWithRecordTypes",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanCreateAuthorizationWithRecordTypesRequest,
  responseType: dlkit_proto_authorization_pb.CanCreateAuthorizationWithRecordTypesReply
};
AuthorizationAdminSession.GetAuthorizationFormForCreateForAgent = {
  methodName: "GetAuthorizationFormForCreateForAgent",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForAgentRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForAgentReply
};
AuthorizationAdminSession.GetAuthorizationFormForCreateForResource = {
  methodName: "GetAuthorizationFormForCreateForResource",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceReply
};
AuthorizationAdminSession.GetAuthorizationFormForCreateForResourceAndTrust = {
  methodName: "GetAuthorizationFormForCreateForResourceAndTrust",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceAndTrustRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationFormForCreateForResourceAndTrustReply
};
AuthorizationAdminSession.CreateAuthorization = {
  methodName: "CreateAuthorization",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CreateAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.CreateAuthorizationReply
};
AuthorizationAdminSession.CanUpdateAuthorizations = {
  methodName: "CanUpdateAuthorizations",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanUpdateAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanUpdateAuthorizationsReply
};
AuthorizationAdminSession.GetAuthorizationFormForUpdate = {
  methodName: "GetAuthorizationFormForUpdate",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationFormForUpdateRequest,
  responseType: dlkit_proto_authorization_pb.GetAuthorizationFormForUpdateReply
};
AuthorizationAdminSession.UpdateAuthorization = {
  methodName: "UpdateAuthorization",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UpdateAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.UpdateAuthorizationReply
};
AuthorizationAdminSession.CanDeleteAuthorizations = {
  methodName: "CanDeleteAuthorizations",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanDeleteAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanDeleteAuthorizationsReply
};
AuthorizationAdminSession.DeleteAuthorization = {
  methodName: "DeleteAuthorization",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.DeleteAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.DeleteAuthorizationReply
};
AuthorizationAdminSession.CanManageAuthorizationAliases = {
  methodName: "CanManageAuthorizationAliases",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanManageAuthorizationAliasesRequest,
  responseType: dlkit_proto_authorization_pb.CanManageAuthorizationAliasesReply
};
AuthorizationAdminSession.AliasAuthorization = {
  methodName: "AliasAuthorization",
  service: AuthorizationAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.AliasAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.AliasAuthorizationReply
};
var AuthorizationVaultSession = {
  serviceName: "dlkit.proto.authorization.AuthorizationVaultSession"
};
AuthorizationVaultSession.UseComparativeVaultView = {
  methodName: "UseComparativeVaultView",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseComparativeVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseComparativeVaultViewReply
};
AuthorizationVaultSession.UsePlenaryVaultView = {
  methodName: "UsePlenaryVaultView",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UsePlenaryVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UsePlenaryVaultViewReply
};
AuthorizationVaultSession.CanLookupAuthorizationVaultMappings = {
  methodName: "CanLookupAuthorizationVaultMappings",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanLookupAuthorizationVaultMappingsRequest,
  responseType: dlkit_proto_authorization_pb.CanLookupAuthorizationVaultMappingsReply
};
AuthorizationVaultSession.GetAuthorizationIdsByVault = {
  methodName: "GetAuthorizationIdsByVault",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationIdsByVaultRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AuthorizationVaultSession.GetAuthorizationsByVault = {
  methodName: "GetAuthorizationsByVault",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsByVaultRequest,
  responseType: dlkit_proto_authorization_pb.Authorization
};
AuthorizationVaultSession.GetAuthorizationsIdsByVault = {
  methodName: "GetAuthorizationsIdsByVault",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAuthorizationsIdsByVaultRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AuthorizationVaultSession.GetVaultIdsByAuthorization = {
  methodName: "GetVaultIdsByAuthorization",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultIdsByAuthorizationRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AuthorizationVaultSession.GetVaultByAuthorization = {
  methodName: "GetVaultByAuthorization",
  service: AuthorizationVaultSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultByAuthorizationRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
var AuthorizationVaultAssignmentSession = {
  serviceName: "dlkit.proto.authorization.AuthorizationVaultAssignmentSession"
};
AuthorizationVaultAssignmentSession.CanAssignAuthorizations = {
  methodName: "CanAssignAuthorizations",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanAssignAuthorizationsRequest,
  responseType: dlkit_proto_authorization_pb.CanAssignAuthorizationsReply
};
AuthorizationVaultAssignmentSession.CanAssignAuthorizationsToVault = {
  methodName: "CanAssignAuthorizationsToVault",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanAssignAuthorizationsToVaultRequest,
  responseType: dlkit_proto_authorization_pb.CanAssignAuthorizationsToVaultReply
};
AuthorizationVaultAssignmentSession.GetAssignableVaultIds = {
  methodName: "GetAssignableVaultIds",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAssignableVaultIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AuthorizationVaultAssignmentSession.GetAssignableVaultIdsForAuthorization = {
  methodName: "GetAssignableVaultIdsForAuthorization",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetAssignableVaultIdsForAuthorizationRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AuthorizationVaultAssignmentSession.AssignAuthorizationToVault = {
  methodName: "AssignAuthorizationToVault",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.AssignAuthorizationToVaultRequest,
  responseType: dlkit_proto_authorization_pb.AssignAuthorizationToVaultReply
};
AuthorizationVaultAssignmentSession.UnassignAuthorizationFromVault = {
  methodName: "UnassignAuthorizationFromVault",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UnassignAuthorizationFromVaultRequest,
  responseType: dlkit_proto_authorization_pb.UnassignAuthorizationFromVaultReply
};
AuthorizationVaultAssignmentSession.ReassignAuthorizationToVault = {
  methodName: "ReassignAuthorizationToVault",
  service: AuthorizationVaultAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.ReassignAuthorizationToVaultRequest,
  responseType: dlkit_proto_authorization_pb.ReassignAuthorizationToVaultReply
};
var VaultLookupSession = {
  serviceName: "dlkit.proto.authorization.VaultLookupSession"
};
VaultLookupSession.CanLookupVaults = {
  methodName: "CanLookupVaults",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanLookupVaultsRequest,
  responseType: dlkit_proto_authorization_pb.CanLookupVaultsReply
};
VaultLookupSession.UseComparativeVaultView = {
  methodName: "UseComparativeVaultView",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseComparativeVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseComparativeVaultViewReply
};
VaultLookupSession.UsePlenaryVaultView = {
  methodName: "UsePlenaryVaultView",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UsePlenaryVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UsePlenaryVaultViewReply
};
VaultLookupSession.GetVault = {
  methodName: "GetVault",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultReply
};
VaultLookupSession.GetVaultsByIds = {
  methodName: "GetVaultsByIds",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsByIdsRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultLookupSession.GetVaultsByGenusType = {
  methodName: "GetVaultsByGenusType",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsByGenusTypeRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultLookupSession.GetVaultsByParentGenusType = {
  methodName: "GetVaultsByParentGenusType",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsByParentGenusTypeRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultLookupSession.GetVaultsByRecordType = {
  methodName: "GetVaultsByRecordType",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsByRecordTypeRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultLookupSession.GetVaultsByProvider = {
  methodName: "GetVaultsByProvider",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsByProviderRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultLookupSession.GetVaults = {
  methodName: "GetVaults",
  service: VaultLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
var VaultQuerySession = {
  serviceName: "dlkit.proto.authorization.VaultQuerySession"
};
VaultQuerySession.CanSearchVaults = {
  methodName: "CanSearchVaults",
  service: VaultQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanSearchVaultsRequest,
  responseType: dlkit_proto_authorization_pb.CanSearchVaultsReply
};
VaultQuerySession.GetVaultQuery = {
  methodName: "GetVaultQuery",
  service: VaultQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultQueryRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultQueryReply
};
VaultQuerySession.GetVaultsByQuery = {
  methodName: "GetVaultsByQuery",
  service: VaultQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetVaultsByQueryRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
var VaultAdminSession = {
  serviceName: "dlkit.proto.authorization.VaultAdminSession"
};
VaultAdminSession.CanCreateVaults = {
  methodName: "CanCreateVaults",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanCreateVaultsRequest,
  responseType: dlkit_proto_authorization_pb.CanCreateVaultsReply
};
VaultAdminSession.CanCreateVaultWithRecordTypes = {
  methodName: "CanCreateVaultWithRecordTypes",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanCreateVaultWithRecordTypesRequest,
  responseType: dlkit_proto_authorization_pb.CanCreateVaultWithRecordTypesReply
};
VaultAdminSession.GetVaultFormForCreate = {
  methodName: "GetVaultFormForCreate",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultFormForCreateRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultFormForCreateReply
};
VaultAdminSession.CreateVault = {
  methodName: "CreateVault",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CreateVaultRequest,
  responseType: dlkit_proto_authorization_pb.CreateVaultReply
};
VaultAdminSession.CanUpdateVaults = {
  methodName: "CanUpdateVaults",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanUpdateVaultsRequest,
  responseType: dlkit_proto_authorization_pb.CanUpdateVaultsReply
};
VaultAdminSession.GetVaultFormForUpdate = {
  methodName: "GetVaultFormForUpdate",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultFormForUpdateRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultFormForUpdateReply
};
VaultAdminSession.UpdateVault = {
  methodName: "UpdateVault",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UpdateVaultRequest,
  responseType: dlkit_proto_authorization_pb.UpdateVaultReply
};
VaultAdminSession.CanDeleteVaults = {
  methodName: "CanDeleteVaults",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanDeleteVaultsRequest,
  responseType: dlkit_proto_authorization_pb.CanDeleteVaultsReply
};
VaultAdminSession.DeleteVault = {
  methodName: "DeleteVault",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.DeleteVaultRequest,
  responseType: dlkit_proto_authorization_pb.DeleteVaultReply
};
VaultAdminSession.CanManageVaultAliases = {
  methodName: "CanManageVaultAliases",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanManageVaultAliasesRequest,
  responseType: dlkit_proto_authorization_pb.CanManageVaultAliasesReply
};
VaultAdminSession.AliasVault = {
  methodName: "AliasVault",
  service: VaultAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.AliasVaultRequest,
  responseType: dlkit_proto_authorization_pb.AliasVaultReply
};
var VaultHierarchySession = {
  serviceName: "dlkit.proto.authorization.VaultHierarchySession"
};
VaultHierarchySession.GetVaultHierarchyId = {
  methodName: "GetVaultHierarchyId",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultHierarchyIdRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultHierarchyIdReply
};
VaultHierarchySession.GetVaultHierarchy = {
  methodName: "GetVaultHierarchy",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultHierarchyRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultHierarchyReply
};
VaultHierarchySession.CanAccessVaultHierarchy = {
  methodName: "CanAccessVaultHierarchy",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanAccessVaultHierarchyRequest,
  responseType: dlkit_proto_authorization_pb.CanAccessVaultHierarchyReply
};
VaultHierarchySession.UseComparativeVaultView = {
  methodName: "UseComparativeVaultView",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UseComparativeVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UseComparativeVaultViewReply
};
VaultHierarchySession.UsePlenaryVaultView = {
  methodName: "UsePlenaryVaultView",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.UsePlenaryVaultViewRequest,
  responseType: dlkit_proto_authorization_pb.UsePlenaryVaultViewReply
};
VaultHierarchySession.GetRootVaultIds = {
  methodName: "GetRootVaultIds",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetRootVaultIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
VaultHierarchySession.GetRootVaults = {
  methodName: "GetRootVaults",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetRootVaultsRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultHierarchySession.HasParentVaults = {
  methodName: "HasParentVaults",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.HasParentVaultsRequest,
  responseType: dlkit_proto_authorization_pb.HasParentVaultsReply
};
VaultHierarchySession.IsParentOfVault = {
  methodName: "IsParentOfVault",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.IsParentOfVaultRequest,
  responseType: dlkit_proto_authorization_pb.IsParentOfVaultReply
};
VaultHierarchySession.GetParentVaultIds = {
  methodName: "GetParentVaultIds",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetParentVaultIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
VaultHierarchySession.GetParentVaults = {
  methodName: "GetParentVaults",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetParentVaultsRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultHierarchySession.IsAncestorOfVault = {
  methodName: "IsAncestorOfVault",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.IsAncestorOfVaultRequest,
  responseType: dlkit_proto_authorization_pb.IsAncestorOfVaultReply
};
VaultHierarchySession.HasChildVaults = {
  methodName: "HasChildVaults",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.HasChildVaultsRequest,
  responseType: dlkit_proto_authorization_pb.HasChildVaultsReply
};
VaultHierarchySession.IsChildOfVault = {
  methodName: "IsChildOfVault",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.IsChildOfVaultRequest,
  responseType: dlkit_proto_authorization_pb.IsChildOfVaultReply
};
VaultHierarchySession.GetChildVaultIds = {
  methodName: "GetChildVaultIds",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetChildVaultIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
VaultHierarchySession.GetChildVaults = {
  methodName: "GetChildVaults",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authorization_pb.GetChildVaultsRequest,
  responseType: dlkit_proto_authorization_pb.Vault
};
VaultHierarchySession.IsDescendantOfVault = {
  methodName: "IsDescendantOfVault",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.IsDescendantOfVaultRequest,
  responseType: dlkit_proto_authorization_pb.IsDescendantOfVaultReply
};
VaultHierarchySession.GetVaultNodeIds = {
  methodName: "GetVaultNodeIds",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultNodeIdsRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultNodeIdsReply
};
VaultHierarchySession.GetVaultNodes = {
  methodName: "GetVaultNodes",
  service: VaultHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultNodesRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultNodesReply
};
var VaultHierarchyDesignSession = {
  serviceName: "dlkit.proto.authorization.VaultHierarchyDesignSession"
};
VaultHierarchyDesignSession.GetVaultHierarchyId = {
  methodName: "GetVaultHierarchyId",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultHierarchyIdRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultHierarchyIdReply
};
VaultHierarchyDesignSession.GetVaultHierarchy = {
  methodName: "GetVaultHierarchy",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.GetVaultHierarchyRequest,
  responseType: dlkit_proto_authorization_pb.GetVaultHierarchyReply
};
VaultHierarchyDesignSession.CanModifyVaultHierarchy = {
  methodName: "CanModifyVaultHierarchy",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.CanModifyVaultHierarchyRequest,
  responseType: dlkit_proto_authorization_pb.CanModifyVaultHierarchyReply
};
VaultHierarchyDesignSession.AddRootVault = {
  methodName: "AddRootVault",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.AddRootVaultRequest,
  responseType: dlkit_proto_authorization_pb.AddRootVaultReply
};
VaultHierarchyDesignSession.RemoveRootVault = {
  methodName: "RemoveRootVault",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.RemoveRootVaultRequest,
  responseType: dlkit_proto_authorization_pb.RemoveRootVaultReply
};
VaultHierarchyDesignSession.AddChildVault = {
  methodName: "AddChildVault",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.AddChildVaultRequest,
  responseType: dlkit_proto_authorization_pb.AddChildVaultReply
};
VaultHierarchyDesignSession.RemoveChildVault = {
  methodName: "RemoveChildVault",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.RemoveChildVaultRequest,
  responseType: dlkit_proto_authorization_pb.RemoveChildVaultReply
};
VaultHierarchyDesignSession.RemoveChildVaults = {
  methodName: "RemoveChildVaults",
  service: VaultHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authorization_pb.RemoveChildVaultsRequest,
  responseType: dlkit_proto_authorization_pb.RemoveChildVaultsReply
};
module.exports = {
  AuthorizationSession: AuthorizationSession,
  AuthorizationLookupSession: AuthorizationLookupSession,
  AuthorizationQuerySession: AuthorizationQuerySession,
  AuthorizationAdminSession: AuthorizationAdminSession,
  AuthorizationVaultSession: AuthorizationVaultSession,
  AuthorizationVaultAssignmentSession: AuthorizationVaultAssignmentSession,
  VaultLookupSession: VaultLookupSession,
  VaultQuerySession: VaultQuerySession,
  VaultAdminSession: VaultAdminSession,
  VaultHierarchySession: VaultHierarchySession,
  VaultHierarchyDesignSession: VaultHierarchyDesignSession,
};

