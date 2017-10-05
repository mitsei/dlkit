// package: dlkit.proto.repository
// file: dlkit/proto/repository.proto

var jspb = require("google-protobuf");
var dlkit_proto_repository_pb = require("../../dlkit/proto/repository_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_transport_objects_pb = require("../../dlkit/primordium/transport/objects_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var AssetLookupSession = {
  serviceName: "dlkit.proto.repository.AssetLookupSession"
};
AssetLookupSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
AssetLookupSession.GetRepository = {
  methodName: "GetRepository",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
AssetLookupSession.CanLookupAssets = {
  methodName: "CanLookupAssets",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanLookupAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanLookupAssetsReply
};
AssetLookupSession.UseComparativeAssetView = {
  methodName: "UseComparativeAssetView",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeAssetViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeAssetViewReply
};
AssetLookupSession.UsePlenaryAssetView = {
  methodName: "UsePlenaryAssetView",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryAssetViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryAssetViewReply
};
AssetLookupSession.UseFederatedRepositoryView = {
  methodName: "UseFederatedRepositoryView",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseFederatedRepositoryViewReply
};
AssetLookupSession.UseIsolatedRepositoryView = {
  methodName: "UseIsolatedRepositoryView",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply
};
AssetLookupSession.GetAsset = {
  methodName: "GetAsset",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetRequest,
  responseType: dlkit_proto_repository_pb.GetAssetReply
};
AssetLookupSession.GetAssetsByIds = {
  methodName: "GetAssetsByIds",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByIdsRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetLookupSession.GetAssetsByGenusType = {
  methodName: "GetAssetsByGenusType",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetLookupSession.GetAssetsByParentGenusType = {
  methodName: "GetAssetsByParentGenusType",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByParentGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetLookupSession.GetAssetsByRecordType = {
  methodName: "GetAssetsByRecordType",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByRecordTypeRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetLookupSession.GetAssetsByProvider = {
  methodName: "GetAssetsByProvider",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByProviderRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetLookupSession.GetAssets = {
  methodName: "GetAssets",
  service: AssetLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
var AssetQuerySession = {
  serviceName: "dlkit.proto.repository.AssetQuerySession"
};
AssetQuerySession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
AssetQuerySession.GetRepository = {
  methodName: "GetRepository",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
AssetQuerySession.CanSearchAssets = {
  methodName: "CanSearchAssets",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanSearchAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanSearchAssetsReply
};
AssetQuerySession.UseFederatedRepositoryView = {
  methodName: "UseFederatedRepositoryView",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseFederatedRepositoryViewReply
};
AssetQuerySession.UseIsolatedRepositoryView = {
  methodName: "UseIsolatedRepositoryView",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply
};
AssetQuerySession.GetAssetQuery = {
  methodName: "GetAssetQuery",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetQueryRequest,
  responseType: dlkit_proto_repository_pb.GetAssetQueryReply
};
AssetQuerySession.GetAssetsByQuery = {
  methodName: "GetAssetsByQuery",
  service: AssetQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByQueryRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
var AssetSearchSession = {
  serviceName: "dlkit.proto.repository.AssetSearchSession"
};
AssetSearchSession.GetAssetSearch = {
  methodName: "GetAssetSearch",
  service: AssetSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetSearchRequest,
  responseType: dlkit_proto_repository_pb.GetAssetSearchReply
};
AssetSearchSession.GetAssetSearchOrder = {
  methodName: "GetAssetSearchOrder",
  service: AssetSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetSearchOrderRequest,
  responseType: dlkit_proto_repository_pb.GetAssetSearchOrderReply
};
AssetSearchSession.GetAssetsBySearch = {
  methodName: "GetAssetsBySearch",
  service: AssetSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetsBySearchRequest,
  responseType: dlkit_proto_repository_pb.GetAssetsBySearchReply
};
AssetSearchSession.GetAssetQueryFromInspector = {
  methodName: "GetAssetQueryFromInspector",
  service: AssetSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetQueryFromInspectorRequest,
  responseType: dlkit_proto_repository_pb.GetAssetQueryFromInspectorReply
};
var AssetAdminSession = {
  serviceName: "dlkit.proto.repository.AssetAdminSession"
};
AssetAdminSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
AssetAdminSession.GetRepository = {
  methodName: "GetRepository",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
AssetAdminSession.CanCreateAssets = {
  methodName: "CanCreateAssets",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanCreateAssetsReply
};
AssetAdminSession.CanCreateAssetWithRecordTypes = {
  methodName: "CanCreateAssetWithRecordTypes",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateAssetWithRecordTypesRequest,
  responseType: dlkit_proto_repository_pb.CanCreateAssetWithRecordTypesReply
};
AssetAdminSession.GetAssetFormForCreate = {
  methodName: "GetAssetFormForCreate",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetFormForCreateRequest,
  responseType: dlkit_proto_repository_pb.GetAssetFormForCreateReply
};
AssetAdminSession.CreateAsset = {
  methodName: "CreateAsset",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CreateAssetRequest,
  responseType: dlkit_proto_repository_pb.CreateAssetReply
};
AssetAdminSession.CanUpdateAssets = {
  methodName: "CanUpdateAssets",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanUpdateAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanUpdateAssetsReply
};
AssetAdminSession.GetAssetFormForUpdate = {
  methodName: "GetAssetFormForUpdate",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetFormForUpdateRequest,
  responseType: dlkit_proto_repository_pb.GetAssetFormForUpdateReply
};
AssetAdminSession.UpdateAsset = {
  methodName: "UpdateAsset",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UpdateAssetRequest,
  responseType: dlkit_proto_repository_pb.UpdateAssetReply
};
AssetAdminSession.CanDeleteAssets = {
  methodName: "CanDeleteAssets",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanDeleteAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanDeleteAssetsReply
};
AssetAdminSession.DeleteAsset = {
  methodName: "DeleteAsset",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.DeleteAssetRequest,
  responseType: dlkit_proto_repository_pb.DeleteAssetReply
};
AssetAdminSession.CanManageAssetAliases = {
  methodName: "CanManageAssetAliases",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanManageAssetAliasesRequest,
  responseType: dlkit_proto_repository_pb.CanManageAssetAliasesReply
};
AssetAdminSession.AliasAsset = {
  methodName: "AliasAsset",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AliasAssetRequest,
  responseType: dlkit_proto_repository_pb.AliasAssetReply
};
AssetAdminSession.CanCreateAssetContent = {
  methodName: "CanCreateAssetContent",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateAssetContentRequest,
  responseType: dlkit_proto_repository_pb.CanCreateAssetContentReply
};
AssetAdminSession.CanCreateAssetContentWithRecordTypes = {
  methodName: "CanCreateAssetContentWithRecordTypes",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateAssetContentWithRecordTypesRequest,
  responseType: dlkit_proto_repository_pb.CanCreateAssetContentWithRecordTypesReply
};
AssetAdminSession.GetAssetContentFormForCreate = {
  methodName: "GetAssetContentFormForCreate",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetContentFormForCreateRequest,
  responseType: dlkit_proto_repository_pb.GetAssetContentFormForCreateReply
};
AssetAdminSession.CreateAssetContent = {
  methodName: "CreateAssetContent",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CreateAssetContentRequest,
  responseType: dlkit_proto_repository_pb.CreateAssetContentReply
};
AssetAdminSession.CanUpdateAssetContents = {
  methodName: "CanUpdateAssetContents",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanUpdateAssetContentsRequest,
  responseType: dlkit_proto_repository_pb.CanUpdateAssetContentsReply
};
AssetAdminSession.GetAssetContentFormForUpdate = {
  methodName: "GetAssetContentFormForUpdate",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetAssetContentFormForUpdateRequest,
  responseType: dlkit_proto_repository_pb.GetAssetContentFormForUpdateReply
};
AssetAdminSession.UpdateAssetContent = {
  methodName: "UpdateAssetContent",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UpdateAssetContentRequest,
  responseType: dlkit_proto_repository_pb.UpdateAssetContentReply
};
AssetAdminSession.CanDeleteAssetContents = {
  methodName: "CanDeleteAssetContents",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanDeleteAssetContentsRequest,
  responseType: dlkit_proto_repository_pb.CanDeleteAssetContentsReply
};
AssetAdminSession.DeleteAssetContent = {
  methodName: "DeleteAssetContent",
  service: AssetAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.DeleteAssetContentRequest,
  responseType: dlkit_proto_repository_pb.DeleteAssetContentReply
};
var AssetNotificationSession = {
  serviceName: "dlkit.proto.repository.AssetNotificationSession"
};
AssetNotificationSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
AssetNotificationSession.GetRepository = {
  methodName: "GetRepository",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
AssetNotificationSession.CanRegisterForAssetNotifications = {
  methodName: "CanRegisterForAssetNotifications",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanRegisterForAssetNotificationsRequest,
  responseType: dlkit_proto_repository_pb.CanRegisterForAssetNotificationsReply
};
AssetNotificationSession.UseFederatedRepositoryView = {
  methodName: "UseFederatedRepositoryView",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseFederatedRepositoryViewReply
};
AssetNotificationSession.UseIsolatedRepositoryView = {
  methodName: "UseIsolatedRepositoryView",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply
};
AssetNotificationSession.RegisterForNewAssets = {
  methodName: "RegisterForNewAssets",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForNewAssetsRequest,
  responseType: dlkit_proto_repository_pb.RegisterForNewAssetsReply
};
AssetNotificationSession.RegisterForNewAssetsByGenusType = {
  methodName: "RegisterForNewAssetsByGenusType",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForNewAssetsByGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.RegisterForNewAssetsByGenusTypeReply
};
AssetNotificationSession.RegisterForChangedAssets = {
  methodName: "RegisterForChangedAssets",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForChangedAssetsRequest,
  responseType: dlkit_proto_repository_pb.RegisterForChangedAssetsReply
};
AssetNotificationSession.RegisterForChangedAssetsByGenusType = {
  methodName: "RegisterForChangedAssetsByGenusType",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForChangedAssetsByGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.RegisterForChangedAssetsByGenusTypeReply
};
AssetNotificationSession.RegisterForChangedAsset = {
  methodName: "RegisterForChangedAsset",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForChangedAssetRequest,
  responseType: dlkit_proto_repository_pb.RegisterForChangedAssetReply
};
AssetNotificationSession.RegisterForDeletedAssets = {
  methodName: "RegisterForDeletedAssets",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForDeletedAssetsRequest,
  responseType: dlkit_proto_repository_pb.RegisterForDeletedAssetsReply
};
AssetNotificationSession.RegisterForDeletedAssetsByGenusType = {
  methodName: "RegisterForDeletedAssetsByGenusType",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForDeletedAssetsByGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.RegisterForDeletedAssetsByGenusTypeReply
};
AssetNotificationSession.RegisterForDeletedAsset = {
  methodName: "RegisterForDeletedAsset",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RegisterForDeletedAssetRequest,
  responseType: dlkit_proto_repository_pb.RegisterForDeletedAssetReply
};
AssetNotificationSession.ReliableAssetNotifications = {
  methodName: "ReliableAssetNotifications",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.ReliableAssetNotificationsRequest,
  responseType: dlkit_proto_repository_pb.ReliableAssetNotificationsReply
};
AssetNotificationSession.UnreliableAssetNotifications = {
  methodName: "UnreliableAssetNotifications",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UnreliableAssetNotificationsRequest,
  responseType: dlkit_proto_repository_pb.UnreliableAssetNotificationsReply
};
AssetNotificationSession.AcknowledgeAssetNotification = {
  methodName: "AcknowledgeAssetNotification",
  service: AssetNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AcknowledgeAssetNotificationRequest,
  responseType: dlkit_proto_repository_pb.AcknowledgeAssetNotificationReply
};
var AssetRepositorySession = {
  serviceName: "dlkit.proto.repository.AssetRepositorySession"
};
AssetRepositorySession.CanLookupAssetRepositoryMappings = {
  methodName: "CanLookupAssetRepositoryMappings",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanLookupAssetRepositoryMappingsRequest,
  responseType: dlkit_proto_repository_pb.CanLookupAssetRepositoryMappingsReply
};
AssetRepositorySession.UseComparativeRepositoryView = {
  methodName: "UseComparativeRepositoryView",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeRepositoryViewReply
};
AssetRepositorySession.UsePlenaryRepositoryView = {
  methodName: "UsePlenaryRepositoryView",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryRepositoryViewReply
};
AssetRepositorySession.GetAssetIdsByRepository = {
  methodName: "GetAssetIdsByRepository",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetIdsByRepositoryRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssetRepositorySession.GetAssetsByRepository = {
  methodName: "GetAssetsByRepository",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByRepositoryRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetRepositorySession.GetAssetIdsByRepositories = {
  methodName: "GetAssetIdsByRepositories",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetIdsByRepositoriesRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssetRepositorySession.GetAssetsByRepositories = {
  methodName: "GetAssetsByRepositories",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssetsByRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetRepositorySession.GetRepositoryIdsByAsset = {
  methodName: "GetRepositoryIdsByAsset",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdsByAssetRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssetRepositorySession.GetRepositoriesByAsset = {
  methodName: "GetRepositoriesByAsset",
  service: AssetRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByAssetRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
var AssetRepositoryAssignmentSession = {
  serviceName: "dlkit.proto.repository.AssetRepositoryAssignmentSession"
};
AssetRepositoryAssignmentSession.CanAssignAssets = {
  methodName: "CanAssignAssets",
  service: AssetRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanAssignAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanAssignAssetsReply
};
AssetRepositoryAssignmentSession.CanAssignAssetsToRepository = {
  methodName: "CanAssignAssetsToRepository",
  service: AssetRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanAssignAssetsToRepositoryRequest,
  responseType: dlkit_proto_repository_pb.CanAssignAssetsToRepositoryReply
};
AssetRepositoryAssignmentSession.GetAssignableRepositoryIds = {
  methodName: "GetAssignableRepositoryIds",
  service: AssetRepositoryAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssignableRepositoryIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssetRepositoryAssignmentSession.GetAssignableRepositoryIdsForAsset = {
  methodName: "GetAssignableRepositoryIdsForAsset",
  service: AssetRepositoryAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssignableRepositoryIdsForAssetRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
AssetRepositoryAssignmentSession.AssignAssetToRepository = {
  methodName: "AssignAssetToRepository",
  service: AssetRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AssignAssetToRepositoryRequest,
  responseType: dlkit_proto_repository_pb.AssignAssetToRepositoryReply
};
AssetRepositoryAssignmentSession.UnassignAssetFromRepository = {
  methodName: "UnassignAssetFromRepository",
  service: AssetRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UnassignAssetFromRepositoryRequest,
  responseType: dlkit_proto_repository_pb.UnassignAssetFromRepositoryReply
};
var AssetCompositionSession = {
  serviceName: "dlkit.proto.repository.AssetCompositionSession"
};
AssetCompositionSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
AssetCompositionSession.GetRepository = {
  methodName: "GetRepository",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
AssetCompositionSession.CanAccessAssetCompositions = {
  methodName: "CanAccessAssetCompositions",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanAccessAssetCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanAccessAssetCompositionsReply
};
AssetCompositionSession.UseComparativeAssetCompositionView = {
  methodName: "UseComparativeAssetCompositionView",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeAssetCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeAssetCompositionViewReply
};
AssetCompositionSession.UsePlenaryAssetCompositionView = {
  methodName: "UsePlenaryAssetCompositionView",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryAssetCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryAssetCompositionViewReply
};
AssetCompositionSession.UseFederatedRepositoryView = {
  methodName: "UseFederatedRepositoryView",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseFederatedRepositoryViewReply
};
AssetCompositionSession.UseIsolatedRepositoryView = {
  methodName: "UseIsolatedRepositoryView",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply
};
AssetCompositionSession.GetCompositionAssets = {
  methodName: "GetCompositionAssets",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionAssetsRequest,
  responseType: dlkit_proto_repository_pb.Asset
};
AssetCompositionSession.GetCompositionsByAsset = {
  methodName: "GetCompositionsByAsset",
  service: AssetCompositionSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByAssetRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
var AssetCompositionDesignSession = {
  serviceName: "dlkit.proto.repository.AssetCompositionDesignSession"
};
AssetCompositionDesignSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
AssetCompositionDesignSession.GetRepository = {
  methodName: "GetRepository",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
AssetCompositionDesignSession.CanComposeAssets = {
  methodName: "CanComposeAssets",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanComposeAssetsRequest,
  responseType: dlkit_proto_repository_pb.CanComposeAssetsReply
};
AssetCompositionDesignSession.AddAsset = {
  methodName: "AddAsset",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AddAssetRequest,
  responseType: dlkit_proto_repository_pb.AddAssetReply
};
AssetCompositionDesignSession.MoveAssetAhead = {
  methodName: "MoveAssetAhead",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.MoveAssetAheadRequest,
  responseType: dlkit_proto_repository_pb.MoveAssetAheadReply
};
AssetCompositionDesignSession.MoveAssetBehind = {
  methodName: "MoveAssetBehind",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.MoveAssetBehindRequest,
  responseType: dlkit_proto_repository_pb.MoveAssetBehindReply
};
AssetCompositionDesignSession.OrderAssets = {
  methodName: "OrderAssets",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.OrderAssetsRequest,
  responseType: dlkit_proto_repository_pb.OrderAssetsReply
};
AssetCompositionDesignSession.RemoveAsset = {
  methodName: "RemoveAsset",
  service: AssetCompositionDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RemoveAssetRequest,
  responseType: dlkit_proto_repository_pb.RemoveAssetReply
};
var CompositionLookupSession = {
  serviceName: "dlkit.proto.repository.CompositionLookupSession"
};
CompositionLookupSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
CompositionLookupSession.GetRepository = {
  methodName: "GetRepository",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
CompositionLookupSession.CanLookupCompositions = {
  methodName: "CanLookupCompositions",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanLookupCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanLookupCompositionsReply
};
CompositionLookupSession.UseComparativeCompositionView = {
  methodName: "UseComparativeCompositionView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeCompositionViewReply
};
CompositionLookupSession.UsePlenaryCompositionView = {
  methodName: "UsePlenaryCompositionView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryCompositionViewReply
};
CompositionLookupSession.UseFederatedRepositoryView = {
  methodName: "UseFederatedRepositoryView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseFederatedRepositoryViewReply
};
CompositionLookupSession.UseIsolatedRepositoryView = {
  methodName: "UseIsolatedRepositoryView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply
};
CompositionLookupSession.UseActiveCompositionView = {
  methodName: "UseActiveCompositionView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseActiveCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseActiveCompositionViewReply
};
CompositionLookupSession.UseAnyStatusCompositionView = {
  methodName: "UseAnyStatusCompositionView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseAnyStatusCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseAnyStatusCompositionViewReply
};
CompositionLookupSession.UseSequesteredCompositionView = {
  methodName: "UseSequesteredCompositionView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseSequesteredCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseSequesteredCompositionViewReply
};
CompositionLookupSession.UseUnsequesteredCompositionView = {
  methodName: "UseUnsequesteredCompositionView",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseUnsequesteredCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseUnsequesteredCompositionViewReply
};
CompositionLookupSession.GetComposition = {
  methodName: "GetComposition",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionReply
};
CompositionLookupSession.GetCompositionsByIds = {
  methodName: "GetCompositionsByIds",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByIdsRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionLookupSession.GetCompositionsByGenusType = {
  methodName: "GetCompositionsByGenusType",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionLookupSession.GetCompositionsByParentGenusType = {
  methodName: "GetCompositionsByParentGenusType",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByParentGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionLookupSession.GetCompositionsByRecordType = {
  methodName: "GetCompositionsByRecordType",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByRecordTypeRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionLookupSession.GetCompositionsByProvider = {
  methodName: "GetCompositionsByProvider",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByProviderRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionLookupSession.GetCompositions = {
  methodName: "GetCompositions",
  service: CompositionLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
var CompositionQuerySession = {
  serviceName: "dlkit.proto.repository.CompositionQuerySession"
};
CompositionQuerySession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
CompositionQuerySession.GetRepository = {
  methodName: "GetRepository",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
CompositionQuerySession.CanSearchCompositions = {
  methodName: "CanSearchCompositions",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanSearchCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanSearchCompositionsReply
};
CompositionQuerySession.UseFederatedRepositoryView = {
  methodName: "UseFederatedRepositoryView",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseFederatedRepositoryViewReply
};
CompositionQuerySession.UseIsolatedRepositoryView = {
  methodName: "UseIsolatedRepositoryView",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply
};
CompositionQuerySession.UseSequesteredCompositionView = {
  methodName: "UseSequesteredCompositionView",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseSequesteredCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseSequesteredCompositionViewReply
};
CompositionQuerySession.UseUnsequesteredCompositionView = {
  methodName: "UseUnsequesteredCompositionView",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseUnsequesteredCompositionViewRequest,
  responseType: dlkit_proto_repository_pb.UseUnsequesteredCompositionViewReply
};
CompositionQuerySession.GetCompositionQuery = {
  methodName: "GetCompositionQuery",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionQueryRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionQueryReply
};
CompositionQuerySession.GetCompositionsByQuery = {
  methodName: "GetCompositionsByQuery",
  service: CompositionQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByQueryRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
var CompositionSearchSession = {
  serviceName: "dlkit.proto.repository.CompositionSearchSession"
};
CompositionSearchSession.GetCompositionSearch = {
  methodName: "GetCompositionSearch",
  service: CompositionSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionSearchRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionSearchReply
};
CompositionSearchSession.GetCompositionSearchOrder = {
  methodName: "GetCompositionSearchOrder",
  service: CompositionSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionSearchOrderRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionSearchOrderReply
};
CompositionSearchSession.GetCompositionsBySearch = {
  methodName: "GetCompositionsBySearch",
  service: CompositionSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionsBySearchRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionsBySearchReply
};
CompositionSearchSession.GetCompositionQueryFromInspector = {
  methodName: "GetCompositionQueryFromInspector",
  service: CompositionSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionQueryFromInspectorRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionQueryFromInspectorReply
};
var CompositionAdminSession = {
  serviceName: "dlkit.proto.repository.CompositionAdminSession"
};
CompositionAdminSession.GetRepositoryId = {
  methodName: "GetRepositoryId",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryIdReply
};
CompositionAdminSession.GetRepository = {
  methodName: "GetRepository",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
CompositionAdminSession.CanCreateCompositions = {
  methodName: "CanCreateCompositions",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanCreateCompositionsReply
};
CompositionAdminSession.CanCreateCompositionWithRecordTypes = {
  methodName: "CanCreateCompositionWithRecordTypes",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateCompositionWithRecordTypesRequest,
  responseType: dlkit_proto_repository_pb.CanCreateCompositionWithRecordTypesReply
};
CompositionAdminSession.GetCompositionFormForCreate = {
  methodName: "GetCompositionFormForCreate",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionFormForCreateRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionFormForCreateReply
};
CompositionAdminSession.CreateComposition = {
  methodName: "CreateComposition",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CreateCompositionRequest,
  responseType: dlkit_proto_repository_pb.CreateCompositionReply
};
CompositionAdminSession.CanUpdateCompositions = {
  methodName: "CanUpdateCompositions",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanUpdateCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanUpdateCompositionsReply
};
CompositionAdminSession.GetCompositionFormForUpdate = {
  methodName: "GetCompositionFormForUpdate",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetCompositionFormForUpdateRequest,
  responseType: dlkit_proto_repository_pb.GetCompositionFormForUpdateReply
};
CompositionAdminSession.UpdateComposition = {
  methodName: "UpdateComposition",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UpdateCompositionRequest,
  responseType: dlkit_proto_repository_pb.UpdateCompositionReply
};
CompositionAdminSession.CanDeleteCompositions = {
  methodName: "CanDeleteCompositions",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanDeleteCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanDeleteCompositionsReply
};
CompositionAdminSession.DeleteComposition = {
  methodName: "DeleteComposition",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.DeleteCompositionRequest,
  responseType: dlkit_proto_repository_pb.DeleteCompositionReply
};
CompositionAdminSession.DeleteCompositionNode = {
  methodName: "DeleteCompositionNode",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.DeleteCompositionNodeRequest,
  responseType: dlkit_proto_repository_pb.DeleteCompositionNodeReply
};
CompositionAdminSession.AddCompositionChild = {
  methodName: "AddCompositionChild",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AddCompositionChildRequest,
  responseType: dlkit_proto_repository_pb.AddCompositionChildReply
};
CompositionAdminSession.RemoveCompositionChild = {
  methodName: "RemoveCompositionChild",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RemoveCompositionChildRequest,
  responseType: dlkit_proto_repository_pb.RemoveCompositionChildReply
};
CompositionAdminSession.CanManageCompositionAliases = {
  methodName: "CanManageCompositionAliases",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanManageCompositionAliasesRequest,
  responseType: dlkit_proto_repository_pb.CanManageCompositionAliasesReply
};
CompositionAdminSession.AliasComposition = {
  methodName: "AliasComposition",
  service: CompositionAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AliasCompositionRequest,
  responseType: dlkit_proto_repository_pb.AliasCompositionReply
};
var CompositionRepositorySession = {
  serviceName: "dlkit.proto.repository.CompositionRepositorySession"
};
CompositionRepositorySession.UseComparativeCompositionRepositoryView = {
  methodName: "UseComparativeCompositionRepositoryView",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeCompositionRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeCompositionRepositoryViewReply
};
CompositionRepositorySession.UsePlenaryCompositionRepositoryView = {
  methodName: "UsePlenaryCompositionRepositoryView",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryCompositionRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryCompositionRepositoryViewReply
};
CompositionRepositorySession.CanLookupCompositionRepositoryMappings = {
  methodName: "CanLookupCompositionRepositoryMappings",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanLookupCompositionRepositoryMappingsRequest,
  responseType: dlkit_proto_repository_pb.CanLookupCompositionRepositoryMappingsReply
};
CompositionRepositorySession.GetCompositionIdsByRepository = {
  methodName: "GetCompositionIdsByRepository",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionIdsByRepositoryRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CompositionRepositorySession.GetCompositionsByRepository = {
  methodName: "GetCompositionsByRepository",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByRepositoryRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionRepositorySession.GetCompositionIdsByRepositories = {
  methodName: "GetCompositionIdsByRepositories",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionIdsByRepositoriesRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CompositionRepositorySession.GetCompositionsByRepositories = {
  methodName: "GetCompositionsByRepositories",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetCompositionsByRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.Composition
};
CompositionRepositorySession.GetRepositoryIdsByComposition = {
  methodName: "GetRepositoryIdsByComposition",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoryIdsByCompositionRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CompositionRepositorySession.GetRepositoriesByComposition = {
  methodName: "GetRepositoriesByComposition",
  service: CompositionRepositorySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByCompositionRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
var CompositionRepositoryAssignmentSession = {
  serviceName: "dlkit.proto.repository.CompositionRepositoryAssignmentSession"
};
CompositionRepositoryAssignmentSession.CanAssignCompositions = {
  methodName: "CanAssignCompositions",
  service: CompositionRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanAssignCompositionsRequest,
  responseType: dlkit_proto_repository_pb.CanAssignCompositionsReply
};
CompositionRepositoryAssignmentSession.CanAssignCompositionsToRepository = {
  methodName: "CanAssignCompositionsToRepository",
  service: CompositionRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanAssignCompositionsToRepositoryRequest,
  responseType: dlkit_proto_repository_pb.CanAssignCompositionsToRepositoryReply
};
CompositionRepositoryAssignmentSession.GetAssignableRepositoryIds = {
  methodName: "GetAssignableRepositoryIds",
  service: CompositionRepositoryAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssignableRepositoryIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CompositionRepositoryAssignmentSession.GetAssignableRepositoryIdsForComposition = {
  methodName: "GetAssignableRepositoryIdsForComposition",
  service: CompositionRepositoryAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetAssignableRepositoryIdsForCompositionRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CompositionRepositoryAssignmentSession.AssignCompositionToRepository = {
  methodName: "AssignCompositionToRepository",
  service: CompositionRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AssignCompositionToRepositoryRequest,
  responseType: dlkit_proto_repository_pb.AssignCompositionToRepositoryReply
};
CompositionRepositoryAssignmentSession.UnassignCompositionFromRepository = {
  methodName: "UnassignCompositionFromRepository",
  service: CompositionRepositoryAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UnassignCompositionFromRepositoryRequest,
  responseType: dlkit_proto_repository_pb.UnassignCompositionFromRepositoryReply
};
var RepositoryLookupSession = {
  serviceName: "dlkit.proto.repository.RepositoryLookupSession"
};
RepositoryLookupSession.CanLookupRepositories = {
  methodName: "CanLookupRepositories",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanLookupRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.CanLookupRepositoriesReply
};
RepositoryLookupSession.UseComparativeRepositoryView = {
  methodName: "UseComparativeRepositoryView",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeRepositoryViewReply
};
RepositoryLookupSession.UsePlenaryRepositoryView = {
  methodName: "UsePlenaryRepositoryView",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryRepositoryViewReply
};
RepositoryLookupSession.GetRepository = {
  methodName: "GetRepository",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryReply
};
RepositoryLookupSession.GetRepositoriesByIds = {
  methodName: "GetRepositoriesByIds",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByIdsRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryLookupSession.GetRepositoriesByGenusType = {
  methodName: "GetRepositoriesByGenusType",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryLookupSession.GetRepositoriesByParentGenusType = {
  methodName: "GetRepositoriesByParentGenusType",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByParentGenusTypeRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryLookupSession.GetRepositoriesByRecordType = {
  methodName: "GetRepositoriesByRecordType",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByRecordTypeRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryLookupSession.GetRepositoriesByProvider = {
  methodName: "GetRepositoriesByProvider",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByProviderRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryLookupSession.GetRepositories = {
  methodName: "GetRepositories",
  service: RepositoryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
var RepositoryQuerySession = {
  serviceName: "dlkit.proto.repository.RepositoryQuerySession"
};
RepositoryQuerySession.CanSearchRepositories = {
  methodName: "CanSearchRepositories",
  service: RepositoryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanSearchRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.CanSearchRepositoriesReply
};
RepositoryQuerySession.GetRepositoryQuery = {
  methodName: "GetRepositoryQuery",
  service: RepositoryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryQueryRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryQueryReply
};
RepositoryQuerySession.GetRepositoriesByQuery = {
  methodName: "GetRepositoriesByQuery",
  service: RepositoryQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRepositoriesByQueryRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
var RepositoryAdminSession = {
  serviceName: "dlkit.proto.repository.RepositoryAdminSession"
};
RepositoryAdminSession.CanCreateRepositories = {
  methodName: "CanCreateRepositories",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.CanCreateRepositoriesReply
};
RepositoryAdminSession.CanCreateRepositoryWithRecordTypes = {
  methodName: "CanCreateRepositoryWithRecordTypes",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanCreateRepositoryWithRecordTypesRequest,
  responseType: dlkit_proto_repository_pb.CanCreateRepositoryWithRecordTypesReply
};
RepositoryAdminSession.GetRepositoryFormForCreate = {
  methodName: "GetRepositoryFormForCreate",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryFormForCreateRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryFormForCreateReply
};
RepositoryAdminSession.CreateRepository = {
  methodName: "CreateRepository",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CreateRepositoryRequest,
  responseType: dlkit_proto_repository_pb.CreateRepositoryReply
};
RepositoryAdminSession.CanUpdateRepositories = {
  methodName: "CanUpdateRepositories",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanUpdateRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.CanUpdateRepositoriesReply
};
RepositoryAdminSession.GetRepositoryFormForUpdate = {
  methodName: "GetRepositoryFormForUpdate",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryFormForUpdateRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryFormForUpdateReply
};
RepositoryAdminSession.UpdateRepository = {
  methodName: "UpdateRepository",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UpdateRepositoryRequest,
  responseType: dlkit_proto_repository_pb.UpdateRepositoryReply
};
RepositoryAdminSession.CanDeleteRepositories = {
  methodName: "CanDeleteRepositories",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanDeleteRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.CanDeleteRepositoriesReply
};
RepositoryAdminSession.DeleteRepository = {
  methodName: "DeleteRepository",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.DeleteRepositoryRequest,
  responseType: dlkit_proto_repository_pb.DeleteRepositoryReply
};
RepositoryAdminSession.CanManageRepositoryAliases = {
  methodName: "CanManageRepositoryAliases",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanManageRepositoryAliasesRequest,
  responseType: dlkit_proto_repository_pb.CanManageRepositoryAliasesReply
};
RepositoryAdminSession.AliasRepository = {
  methodName: "AliasRepository",
  service: RepositoryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AliasRepositoryRequest,
  responseType: dlkit_proto_repository_pb.AliasRepositoryReply
};
var RepositoryHierarchySession = {
  serviceName: "dlkit.proto.repository.RepositoryHierarchySession"
};
RepositoryHierarchySession.GetRepositoryHierarchyId = {
  methodName: "GetRepositoryHierarchyId",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryHierarchyIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryHierarchyIdReply
};
RepositoryHierarchySession.GetRepositoryHierarchy = {
  methodName: "GetRepositoryHierarchy",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryHierarchyRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryHierarchyReply
};
RepositoryHierarchySession.CanAccessRepositoryHierarchy = {
  methodName: "CanAccessRepositoryHierarchy",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanAccessRepositoryHierarchyRequest,
  responseType: dlkit_proto_repository_pb.CanAccessRepositoryHierarchyReply
};
RepositoryHierarchySession.UseComparativeRepositoryView = {
  methodName: "UseComparativeRepositoryView",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UseComparativeRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UseComparativeRepositoryViewReply
};
RepositoryHierarchySession.UsePlenaryRepositoryView = {
  methodName: "UsePlenaryRepositoryView",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.UsePlenaryRepositoryViewRequest,
  responseType: dlkit_proto_repository_pb.UsePlenaryRepositoryViewReply
};
RepositoryHierarchySession.GetRootRepositoryIds = {
  methodName: "GetRootRepositoryIds",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRootRepositoryIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
RepositoryHierarchySession.GetRootRepositories = {
  methodName: "GetRootRepositories",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetRootRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryHierarchySession.HasParentRepositories = {
  methodName: "HasParentRepositories",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.HasParentRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.HasParentRepositoriesReply
};
RepositoryHierarchySession.IsParentOfRepository = {
  methodName: "IsParentOfRepository",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.IsParentOfRepositoryRequest,
  responseType: dlkit_proto_repository_pb.IsParentOfRepositoryReply
};
RepositoryHierarchySession.GetParentRepositoryIds = {
  methodName: "GetParentRepositoryIds",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetParentRepositoryIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
RepositoryHierarchySession.GetParentRepositories = {
  methodName: "GetParentRepositories",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetParentRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryHierarchySession.IsAncestorOfRepository = {
  methodName: "IsAncestorOfRepository",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.IsAncestorOfRepositoryRequest,
  responseType: dlkit_proto_repository_pb.IsAncestorOfRepositoryReply
};
RepositoryHierarchySession.HasChildRepositories = {
  methodName: "HasChildRepositories",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.HasChildRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.HasChildRepositoriesReply
};
RepositoryHierarchySession.IsChildOfRepository = {
  methodName: "IsChildOfRepository",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.IsChildOfRepositoryRequest,
  responseType: dlkit_proto_repository_pb.IsChildOfRepositoryReply
};
RepositoryHierarchySession.GetChildRepositoryIds = {
  methodName: "GetChildRepositoryIds",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetChildRepositoryIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
RepositoryHierarchySession.GetChildRepositories = {
  methodName: "GetChildRepositories",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_repository_pb.GetChildRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.Repository
};
RepositoryHierarchySession.IsDescendantOfRepository = {
  methodName: "IsDescendantOfRepository",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.IsDescendantOfRepositoryRequest,
  responseType: dlkit_proto_repository_pb.IsDescendantOfRepositoryReply
};
RepositoryHierarchySession.GetRepositoryNodeIds = {
  methodName: "GetRepositoryNodeIds",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryNodeIdsRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryNodeIdsReply
};
RepositoryHierarchySession.GetRepositoryNodes = {
  methodName: "GetRepositoryNodes",
  service: RepositoryHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryNodesRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryNodesReply
};
var RepositoryHierarchyDesignSession = {
  serviceName: "dlkit.proto.repository.RepositoryHierarchyDesignSession"
};
RepositoryHierarchyDesignSession.GetRepositoryHierarchyId = {
  methodName: "GetRepositoryHierarchyId",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryHierarchyIdRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryHierarchyIdReply
};
RepositoryHierarchyDesignSession.GetRepositoryHierarchy = {
  methodName: "GetRepositoryHierarchy",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.GetRepositoryHierarchyRequest,
  responseType: dlkit_proto_repository_pb.GetRepositoryHierarchyReply
};
RepositoryHierarchyDesignSession.CanModifyRepositoryHierarchy = {
  methodName: "CanModifyRepositoryHierarchy",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.CanModifyRepositoryHierarchyRequest,
  responseType: dlkit_proto_repository_pb.CanModifyRepositoryHierarchyReply
};
RepositoryHierarchyDesignSession.AddRootRepository = {
  methodName: "AddRootRepository",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AddRootRepositoryRequest,
  responseType: dlkit_proto_repository_pb.AddRootRepositoryReply
};
RepositoryHierarchyDesignSession.RemoveRootRepository = {
  methodName: "RemoveRootRepository",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RemoveRootRepositoryRequest,
  responseType: dlkit_proto_repository_pb.RemoveRootRepositoryReply
};
RepositoryHierarchyDesignSession.AddChildRepository = {
  methodName: "AddChildRepository",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.AddChildRepositoryRequest,
  responseType: dlkit_proto_repository_pb.AddChildRepositoryReply
};
RepositoryHierarchyDesignSession.RemoveChildRepository = {
  methodName: "RemoveChildRepository",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RemoveChildRepositoryRequest,
  responseType: dlkit_proto_repository_pb.RemoveChildRepositoryReply
};
RepositoryHierarchyDesignSession.RemoveChildRepositories = {
  methodName: "RemoveChildRepositories",
  service: RepositoryHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_repository_pb.RemoveChildRepositoriesRequest,
  responseType: dlkit_proto_repository_pb.RemoveChildRepositoriesReply
};
module.exports = {
  AssetLookupSession: AssetLookupSession,
  AssetQuerySession: AssetQuerySession,
  AssetSearchSession: AssetSearchSession,
  AssetAdminSession: AssetAdminSession,
  AssetNotificationSession: AssetNotificationSession,
  AssetRepositorySession: AssetRepositorySession,
  AssetRepositoryAssignmentSession: AssetRepositoryAssignmentSession,
  AssetCompositionSession: AssetCompositionSession,
  AssetCompositionDesignSession: AssetCompositionDesignSession,
  CompositionLookupSession: CompositionLookupSession,
  CompositionQuerySession: CompositionQuerySession,
  CompositionSearchSession: CompositionSearchSession,
  CompositionAdminSession: CompositionAdminSession,
  CompositionRepositorySession: CompositionRepositorySession,
  CompositionRepositoryAssignmentSession: CompositionRepositoryAssignmentSession,
  RepositoryLookupSession: RepositoryLookupSession,
  RepositoryQuerySession: RepositoryQuerySession,
  RepositoryAdminSession: RepositoryAdminSession,
  RepositoryHierarchySession: RepositoryHierarchySession,
  RepositoryHierarchyDesignSession: RepositoryHierarchyDesignSession,
};

