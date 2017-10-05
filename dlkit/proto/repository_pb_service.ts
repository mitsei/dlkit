// package: dlkit.proto.repository
// file: dlkit/proto/repository.proto

import * as dlkit_proto_repository_pb from "../../dlkit/proto/repository_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_transport_objects_pb from "../../dlkit/primordium/transport/objects_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class AssetLookupSession {
  static serviceName = "dlkit.proto.repository.AssetLookupSession";
}
export namespace AssetLookupSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanLookupAssets {
    static readonly methodName = "CanLookupAssets";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanLookupAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanLookupAssetsReply;
  }
  export class UseComparativeAssetView {
    static readonly methodName = "UseComparativeAssetView";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeAssetViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeAssetViewReply;
  }
  export class UsePlenaryAssetView {
    static readonly methodName = "UsePlenaryAssetView";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryAssetViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryAssetViewReply;
  }
  export class UseFederatedRepositoryView {
    static readonly methodName = "UseFederatedRepositoryView";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseFederatedRepositoryViewReply;
  }
  export class UseIsolatedRepositoryView {
    static readonly methodName = "UseIsolatedRepositoryView";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply;
  }
  export class GetAsset {
    static readonly methodName = "GetAsset";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetReply;
  }
  export class GetAssetsByIds {
    static readonly methodName = "GetAssetsByIds";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByIdsRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetAssetsByGenusType {
    static readonly methodName = "GetAssetsByGenusType";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetAssetsByParentGenusType {
    static readonly methodName = "GetAssetsByParentGenusType";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetAssetsByRecordType {
    static readonly methodName = "GetAssetsByRecordType";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetAssetsByProvider {
    static readonly methodName = "GetAssetsByProvider";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByProviderRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetAssets {
    static readonly methodName = "GetAssets";
    static readonly service = AssetLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
}
export class AssetQuerySession {
  static serviceName = "dlkit.proto.repository.AssetQuerySession";
}
export namespace AssetQuerySession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanSearchAssets {
    static readonly methodName = "CanSearchAssets";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanSearchAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanSearchAssetsReply;
  }
  export class UseFederatedRepositoryView {
    static readonly methodName = "UseFederatedRepositoryView";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseFederatedRepositoryViewReply;
  }
  export class UseIsolatedRepositoryView {
    static readonly methodName = "UseIsolatedRepositoryView";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply;
  }
  export class GetAssetQuery {
    static readonly methodName = "GetAssetQuery";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetQueryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetQueryReply;
  }
  export class GetAssetsByQuery {
    static readonly methodName = "GetAssetsByQuery";
    static readonly service = AssetQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByQueryRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
}
export class AssetSearchSession {
  static serviceName = "dlkit.proto.repository.AssetSearchSession";
}
export namespace AssetSearchSession {
  export class GetAssetSearch {
    static readonly methodName = "GetAssetSearch";
    static readonly service = AssetSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetSearchRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetSearchReply;
  }
  export class GetAssetSearchOrder {
    static readonly methodName = "GetAssetSearchOrder";
    static readonly service = AssetSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetSearchOrderRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetSearchOrderReply;
  }
  export class GetAssetsBySearch {
    static readonly methodName = "GetAssetsBySearch";
    static readonly service = AssetSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsBySearchRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetsBySearchReply;
  }
  export class GetAssetQueryFromInspector {
    static readonly methodName = "GetAssetQueryFromInspector";
    static readonly service = AssetSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetQueryFromInspectorRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetQueryFromInspectorReply;
  }
}
export class AssetAdminSession {
  static serviceName = "dlkit.proto.repository.AssetAdminSession";
}
export namespace AssetAdminSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanCreateAssets {
    static readonly methodName = "CanCreateAssets";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateAssetsReply;
  }
  export class CanCreateAssetWithRecordTypes {
    static readonly methodName = "CanCreateAssetWithRecordTypes";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateAssetWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateAssetWithRecordTypesReply;
  }
  export class GetAssetFormForCreate {
    static readonly methodName = "GetAssetFormForCreate";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetFormForCreateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetFormForCreateReply;
  }
  export class CreateAsset {
    static readonly methodName = "CreateAsset";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CreateAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.CreateAssetReply;
  }
  export class CanUpdateAssets {
    static readonly methodName = "CanUpdateAssets";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanUpdateAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanUpdateAssetsReply;
  }
  export class GetAssetFormForUpdate {
    static readonly methodName = "GetAssetFormForUpdate";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetFormForUpdateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetFormForUpdateReply;
  }
  export class UpdateAsset {
    static readonly methodName = "UpdateAsset";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UpdateAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.UpdateAssetReply;
  }
  export class CanDeleteAssets {
    static readonly methodName = "CanDeleteAssets";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanDeleteAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanDeleteAssetsReply;
  }
  export class DeleteAsset {
    static readonly methodName = "DeleteAsset";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.DeleteAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.DeleteAssetReply;
  }
  export class CanManageAssetAliases {
    static readonly methodName = "CanManageAssetAliases";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanManageAssetAliasesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanManageAssetAliasesReply;
  }
  export class AliasAsset {
    static readonly methodName = "AliasAsset";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AliasAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.AliasAssetReply;
  }
  export class CanCreateAssetContent {
    static readonly methodName = "CanCreateAssetContent";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateAssetContentRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateAssetContentReply;
  }
  export class CanCreateAssetContentWithRecordTypes {
    static readonly methodName = "CanCreateAssetContentWithRecordTypes";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateAssetContentWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateAssetContentWithRecordTypesReply;
  }
  export class GetAssetContentFormForCreate {
    static readonly methodName = "GetAssetContentFormForCreate";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetContentFormForCreateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetContentFormForCreateReply;
  }
  export class CreateAssetContent {
    static readonly methodName = "CreateAssetContent";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CreateAssetContentRequest;
    static readonly responseType = dlkit_proto_repository_pb.CreateAssetContentReply;
  }
  export class CanUpdateAssetContents {
    static readonly methodName = "CanUpdateAssetContents";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanUpdateAssetContentsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanUpdateAssetContentsReply;
  }
  export class GetAssetContentFormForUpdate {
    static readonly methodName = "GetAssetContentFormForUpdate";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetContentFormForUpdateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetAssetContentFormForUpdateReply;
  }
  export class UpdateAssetContent {
    static readonly methodName = "UpdateAssetContent";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UpdateAssetContentRequest;
    static readonly responseType = dlkit_proto_repository_pb.UpdateAssetContentReply;
  }
  export class CanDeleteAssetContents {
    static readonly methodName = "CanDeleteAssetContents";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanDeleteAssetContentsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanDeleteAssetContentsReply;
  }
  export class DeleteAssetContent {
    static readonly methodName = "DeleteAssetContent";
    static readonly service = AssetAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.DeleteAssetContentRequest;
    static readonly responseType = dlkit_proto_repository_pb.DeleteAssetContentReply;
  }
}
export class AssetNotificationSession {
  static serviceName = "dlkit.proto.repository.AssetNotificationSession";
}
export namespace AssetNotificationSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanRegisterForAssetNotifications {
    static readonly methodName = "CanRegisterForAssetNotifications";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanRegisterForAssetNotificationsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanRegisterForAssetNotificationsReply;
  }
  export class UseFederatedRepositoryView {
    static readonly methodName = "UseFederatedRepositoryView";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseFederatedRepositoryViewReply;
  }
  export class UseIsolatedRepositoryView {
    static readonly methodName = "UseIsolatedRepositoryView";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply;
  }
  export class RegisterForNewAssets {
    static readonly methodName = "RegisterForNewAssets";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForNewAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForNewAssetsReply;
  }
  export class RegisterForNewAssetsByGenusType {
    static readonly methodName = "RegisterForNewAssetsByGenusType";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForNewAssetsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForNewAssetsByGenusTypeReply;
  }
  export class RegisterForChangedAssets {
    static readonly methodName = "RegisterForChangedAssets";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForChangedAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForChangedAssetsReply;
  }
  export class RegisterForChangedAssetsByGenusType {
    static readonly methodName = "RegisterForChangedAssetsByGenusType";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForChangedAssetsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForChangedAssetsByGenusTypeReply;
  }
  export class RegisterForChangedAsset {
    static readonly methodName = "RegisterForChangedAsset";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForChangedAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForChangedAssetReply;
  }
  export class RegisterForDeletedAssets {
    static readonly methodName = "RegisterForDeletedAssets";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForDeletedAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForDeletedAssetsReply;
  }
  export class RegisterForDeletedAssetsByGenusType {
    static readonly methodName = "RegisterForDeletedAssetsByGenusType";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForDeletedAssetsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForDeletedAssetsByGenusTypeReply;
  }
  export class RegisterForDeletedAsset {
    static readonly methodName = "RegisterForDeletedAsset";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RegisterForDeletedAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.RegisterForDeletedAssetReply;
  }
  export class ReliableAssetNotifications {
    static readonly methodName = "ReliableAssetNotifications";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.ReliableAssetNotificationsRequest;
    static readonly responseType = dlkit_proto_repository_pb.ReliableAssetNotificationsReply;
  }
  export class UnreliableAssetNotifications {
    static readonly methodName = "UnreliableAssetNotifications";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UnreliableAssetNotificationsRequest;
    static readonly responseType = dlkit_proto_repository_pb.UnreliableAssetNotificationsReply;
  }
  export class AcknowledgeAssetNotification {
    static readonly methodName = "AcknowledgeAssetNotification";
    static readonly service = AssetNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AcknowledgeAssetNotificationRequest;
    static readonly responseType = dlkit_proto_repository_pb.AcknowledgeAssetNotificationReply;
  }
}
export class AssetRepositorySession {
  static serviceName = "dlkit.proto.repository.AssetRepositorySession";
}
export namespace AssetRepositorySession {
  export class CanLookupAssetRepositoryMappings {
    static readonly methodName = "CanLookupAssetRepositoryMappings";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanLookupAssetRepositoryMappingsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanLookupAssetRepositoryMappingsReply;
  }
  export class UseComparativeRepositoryView {
    static readonly methodName = "UseComparativeRepositoryView";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeRepositoryViewReply;
  }
  export class UsePlenaryRepositoryView {
    static readonly methodName = "UsePlenaryRepositoryView";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryRepositoryViewReply;
  }
  export class GetAssetIdsByRepository {
    static readonly methodName = "GetAssetIdsByRepository";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetIdsByRepositoryRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssetsByRepository {
    static readonly methodName = "GetAssetsByRepository";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetAssetIdsByRepositories {
    static readonly methodName = "GetAssetIdsByRepositories";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetIdsByRepositoriesRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssetsByRepositories {
    static readonly methodName = "GetAssetsByRepositories";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssetsByRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetRepositoryIdsByAsset {
    static readonly methodName = "GetRepositoryIdsByAsset";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdsByAssetRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRepositoriesByAsset {
    static readonly methodName = "GetRepositoriesByAsset";
    static readonly service = AssetRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
}
export class AssetRepositoryAssignmentSession {
  static serviceName = "dlkit.proto.repository.AssetRepositoryAssignmentSession";
}
export namespace AssetRepositoryAssignmentSession {
  export class CanAssignAssets {
    static readonly methodName = "CanAssignAssets";
    static readonly service = AssetRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanAssignAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanAssignAssetsReply;
  }
  export class CanAssignAssetsToRepository {
    static readonly methodName = "CanAssignAssetsToRepository";
    static readonly service = AssetRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanAssignAssetsToRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanAssignAssetsToRepositoryReply;
  }
  export class GetAssignableRepositoryIds {
    static readonly methodName = "GetAssignableRepositoryIds";
    static readonly service = AssetRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssignableRepositoryIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableRepositoryIdsForAsset {
    static readonly methodName = "GetAssignableRepositoryIdsForAsset";
    static readonly service = AssetRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssignableRepositoryIdsForAssetRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignAssetToRepository {
    static readonly methodName = "AssignAssetToRepository";
    static readonly service = AssetRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AssignAssetToRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.AssignAssetToRepositoryReply;
  }
  export class UnassignAssetFromRepository {
    static readonly methodName = "UnassignAssetFromRepository";
    static readonly service = AssetRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UnassignAssetFromRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.UnassignAssetFromRepositoryReply;
  }
}
export class AssetCompositionSession {
  static serviceName = "dlkit.proto.repository.AssetCompositionSession";
}
export namespace AssetCompositionSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanAccessAssetCompositions {
    static readonly methodName = "CanAccessAssetCompositions";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanAccessAssetCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanAccessAssetCompositionsReply;
  }
  export class UseComparativeAssetCompositionView {
    static readonly methodName = "UseComparativeAssetCompositionView";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeAssetCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeAssetCompositionViewReply;
  }
  export class UsePlenaryAssetCompositionView {
    static readonly methodName = "UsePlenaryAssetCompositionView";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryAssetCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryAssetCompositionViewReply;
  }
  export class UseFederatedRepositoryView {
    static readonly methodName = "UseFederatedRepositoryView";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseFederatedRepositoryViewReply;
  }
  export class UseIsolatedRepositoryView {
    static readonly methodName = "UseIsolatedRepositoryView";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply;
  }
  export class GetCompositionAssets {
    static readonly methodName = "GetCompositionAssets";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.Asset;
  }
  export class GetCompositionsByAsset {
    static readonly methodName = "GetCompositionsByAsset";
    static readonly service = AssetCompositionSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
}
export class AssetCompositionDesignSession {
  static serviceName = "dlkit.proto.repository.AssetCompositionDesignSession";
}
export namespace AssetCompositionDesignSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanComposeAssets {
    static readonly methodName = "CanComposeAssets";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanComposeAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanComposeAssetsReply;
  }
  export class AddAsset {
    static readonly methodName = "AddAsset";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AddAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.AddAssetReply;
  }
  export class MoveAssetAhead {
    static readonly methodName = "MoveAssetAhead";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.MoveAssetAheadRequest;
    static readonly responseType = dlkit_proto_repository_pb.MoveAssetAheadReply;
  }
  export class MoveAssetBehind {
    static readonly methodName = "MoveAssetBehind";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.MoveAssetBehindRequest;
    static readonly responseType = dlkit_proto_repository_pb.MoveAssetBehindReply;
  }
  export class OrderAssets {
    static readonly methodName = "OrderAssets";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.OrderAssetsRequest;
    static readonly responseType = dlkit_proto_repository_pb.OrderAssetsReply;
  }
  export class RemoveAsset {
    static readonly methodName = "RemoveAsset";
    static readonly service = AssetCompositionDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RemoveAssetRequest;
    static readonly responseType = dlkit_proto_repository_pb.RemoveAssetReply;
  }
}
export class CompositionLookupSession {
  static serviceName = "dlkit.proto.repository.CompositionLookupSession";
}
export namespace CompositionLookupSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanLookupCompositions {
    static readonly methodName = "CanLookupCompositions";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanLookupCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanLookupCompositionsReply;
  }
  export class UseComparativeCompositionView {
    static readonly methodName = "UseComparativeCompositionView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeCompositionViewReply;
  }
  export class UsePlenaryCompositionView {
    static readonly methodName = "UsePlenaryCompositionView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryCompositionViewReply;
  }
  export class UseFederatedRepositoryView {
    static readonly methodName = "UseFederatedRepositoryView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseFederatedRepositoryViewReply;
  }
  export class UseIsolatedRepositoryView {
    static readonly methodName = "UseIsolatedRepositoryView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply;
  }
  export class UseActiveCompositionView {
    static readonly methodName = "UseActiveCompositionView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseActiveCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseActiveCompositionViewReply;
  }
  export class UseAnyStatusCompositionView {
    static readonly methodName = "UseAnyStatusCompositionView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseAnyStatusCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseAnyStatusCompositionViewReply;
  }
  export class UseSequesteredCompositionView {
    static readonly methodName = "UseSequesteredCompositionView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseSequesteredCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseSequesteredCompositionViewReply;
  }
  export class UseUnsequesteredCompositionView {
    static readonly methodName = "UseUnsequesteredCompositionView";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseUnsequesteredCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseUnsequesteredCompositionViewReply;
  }
  export class GetComposition {
    static readonly methodName = "GetComposition";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionReply;
  }
  export class GetCompositionsByIds {
    static readonly methodName = "GetCompositionsByIds";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByIdsRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetCompositionsByGenusType {
    static readonly methodName = "GetCompositionsByGenusType";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetCompositionsByParentGenusType {
    static readonly methodName = "GetCompositionsByParentGenusType";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetCompositionsByRecordType {
    static readonly methodName = "GetCompositionsByRecordType";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetCompositionsByProvider {
    static readonly methodName = "GetCompositionsByProvider";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByProviderRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetCompositions {
    static readonly methodName = "GetCompositions";
    static readonly service = CompositionLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
}
export class CompositionQuerySession {
  static serviceName = "dlkit.proto.repository.CompositionQuerySession";
}
export namespace CompositionQuerySession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanSearchCompositions {
    static readonly methodName = "CanSearchCompositions";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanSearchCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanSearchCompositionsReply;
  }
  export class UseFederatedRepositoryView {
    static readonly methodName = "UseFederatedRepositoryView";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseFederatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseFederatedRepositoryViewReply;
  }
  export class UseIsolatedRepositoryView {
    static readonly methodName = "UseIsolatedRepositoryView";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseIsolatedRepositoryViewReply;
  }
  export class UseSequesteredCompositionView {
    static readonly methodName = "UseSequesteredCompositionView";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseSequesteredCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseSequesteredCompositionViewReply;
  }
  export class UseUnsequesteredCompositionView {
    static readonly methodName = "UseUnsequesteredCompositionView";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseUnsequesteredCompositionViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseUnsequesteredCompositionViewReply;
  }
  export class GetCompositionQuery {
    static readonly methodName = "GetCompositionQuery";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionQueryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionQueryReply;
  }
  export class GetCompositionsByQuery {
    static readonly methodName = "GetCompositionsByQuery";
    static readonly service = CompositionQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByQueryRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
}
export class CompositionSearchSession {
  static serviceName = "dlkit.proto.repository.CompositionSearchSession";
}
export namespace CompositionSearchSession {
  export class GetCompositionSearch {
    static readonly methodName = "GetCompositionSearch";
    static readonly service = CompositionSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionSearchRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionSearchReply;
  }
  export class GetCompositionSearchOrder {
    static readonly methodName = "GetCompositionSearchOrder";
    static readonly service = CompositionSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionSearchOrderRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionSearchOrderReply;
  }
  export class GetCompositionsBySearch {
    static readonly methodName = "GetCompositionsBySearch";
    static readonly service = CompositionSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsBySearchRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionsBySearchReply;
  }
  export class GetCompositionQueryFromInspector {
    static readonly methodName = "GetCompositionQueryFromInspector";
    static readonly service = CompositionSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionQueryFromInspectorRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionQueryFromInspectorReply;
  }
}
export class CompositionAdminSession {
  static serviceName = "dlkit.proto.repository.CompositionAdminSession";
}
export namespace CompositionAdminSession {
  export class GetRepositoryId {
    static readonly methodName = "GetRepositoryId";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryIdReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class CanCreateCompositions {
    static readonly methodName = "CanCreateCompositions";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateCompositionsReply;
  }
  export class CanCreateCompositionWithRecordTypes {
    static readonly methodName = "CanCreateCompositionWithRecordTypes";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateCompositionWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateCompositionWithRecordTypesReply;
  }
  export class GetCompositionFormForCreate {
    static readonly methodName = "GetCompositionFormForCreate";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionFormForCreateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionFormForCreateReply;
  }
  export class CreateComposition {
    static readonly methodName = "CreateComposition";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CreateCompositionRequest;
    static readonly responseType = dlkit_proto_repository_pb.CreateCompositionReply;
  }
  export class CanUpdateCompositions {
    static readonly methodName = "CanUpdateCompositions";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanUpdateCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanUpdateCompositionsReply;
  }
  export class GetCompositionFormForUpdate {
    static readonly methodName = "GetCompositionFormForUpdate";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionFormForUpdateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetCompositionFormForUpdateReply;
  }
  export class UpdateComposition {
    static readonly methodName = "UpdateComposition";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UpdateCompositionRequest;
    static readonly responseType = dlkit_proto_repository_pb.UpdateCompositionReply;
  }
  export class CanDeleteCompositions {
    static readonly methodName = "CanDeleteCompositions";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanDeleteCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanDeleteCompositionsReply;
  }
  export class DeleteComposition {
    static readonly methodName = "DeleteComposition";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.DeleteCompositionRequest;
    static readonly responseType = dlkit_proto_repository_pb.DeleteCompositionReply;
  }
  export class DeleteCompositionNode {
    static readonly methodName = "DeleteCompositionNode";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.DeleteCompositionNodeRequest;
    static readonly responseType = dlkit_proto_repository_pb.DeleteCompositionNodeReply;
  }
  export class AddCompositionChild {
    static readonly methodName = "AddCompositionChild";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AddCompositionChildRequest;
    static readonly responseType = dlkit_proto_repository_pb.AddCompositionChildReply;
  }
  export class RemoveCompositionChild {
    static readonly methodName = "RemoveCompositionChild";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RemoveCompositionChildRequest;
    static readonly responseType = dlkit_proto_repository_pb.RemoveCompositionChildReply;
  }
  export class CanManageCompositionAliases {
    static readonly methodName = "CanManageCompositionAliases";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanManageCompositionAliasesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanManageCompositionAliasesReply;
  }
  export class AliasComposition {
    static readonly methodName = "AliasComposition";
    static readonly service = CompositionAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AliasCompositionRequest;
    static readonly responseType = dlkit_proto_repository_pb.AliasCompositionReply;
  }
}
export class CompositionRepositorySession {
  static serviceName = "dlkit.proto.repository.CompositionRepositorySession";
}
export namespace CompositionRepositorySession {
  export class UseComparativeCompositionRepositoryView {
    static readonly methodName = "UseComparativeCompositionRepositoryView";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeCompositionRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeCompositionRepositoryViewReply;
  }
  export class UsePlenaryCompositionRepositoryView {
    static readonly methodName = "UsePlenaryCompositionRepositoryView";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryCompositionRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryCompositionRepositoryViewReply;
  }
  export class CanLookupCompositionRepositoryMappings {
    static readonly methodName = "CanLookupCompositionRepositoryMappings";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanLookupCompositionRepositoryMappingsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanLookupCompositionRepositoryMappingsReply;
  }
  export class GetCompositionIdsByRepository {
    static readonly methodName = "GetCompositionIdsByRepository";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionIdsByRepositoryRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetCompositionsByRepository {
    static readonly methodName = "GetCompositionsByRepository";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetCompositionIdsByRepositories {
    static readonly methodName = "GetCompositionIdsByRepositories";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionIdsByRepositoriesRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetCompositionsByRepositories {
    static readonly methodName = "GetCompositionsByRepositories";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetCompositionsByRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.Composition;
  }
  export class GetRepositoryIdsByComposition {
    static readonly methodName = "GetRepositoryIdsByComposition";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryIdsByCompositionRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRepositoriesByComposition {
    static readonly methodName = "GetRepositoriesByComposition";
    static readonly service = CompositionRepositorySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByCompositionRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
}
export class CompositionRepositoryAssignmentSession {
  static serviceName = "dlkit.proto.repository.CompositionRepositoryAssignmentSession";
}
export namespace CompositionRepositoryAssignmentSession {
  export class CanAssignCompositions {
    static readonly methodName = "CanAssignCompositions";
    static readonly service = CompositionRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanAssignCompositionsRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanAssignCompositionsReply;
  }
  export class CanAssignCompositionsToRepository {
    static readonly methodName = "CanAssignCompositionsToRepository";
    static readonly service = CompositionRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanAssignCompositionsToRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanAssignCompositionsToRepositoryReply;
  }
  export class GetAssignableRepositoryIds {
    static readonly methodName = "GetAssignableRepositoryIds";
    static readonly service = CompositionRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssignableRepositoryIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableRepositoryIdsForComposition {
    static readonly methodName = "GetAssignableRepositoryIdsForComposition";
    static readonly service = CompositionRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetAssignableRepositoryIdsForCompositionRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignCompositionToRepository {
    static readonly methodName = "AssignCompositionToRepository";
    static readonly service = CompositionRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AssignCompositionToRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.AssignCompositionToRepositoryReply;
  }
  export class UnassignCompositionFromRepository {
    static readonly methodName = "UnassignCompositionFromRepository";
    static readonly service = CompositionRepositoryAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UnassignCompositionFromRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.UnassignCompositionFromRepositoryReply;
  }
}
export class RepositoryLookupSession {
  static serviceName = "dlkit.proto.repository.RepositoryLookupSession";
}
export namespace RepositoryLookupSession {
  export class CanLookupRepositories {
    static readonly methodName = "CanLookupRepositories";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanLookupRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanLookupRepositoriesReply;
  }
  export class UseComparativeRepositoryView {
    static readonly methodName = "UseComparativeRepositoryView";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeRepositoryViewReply;
  }
  export class UsePlenaryRepositoryView {
    static readonly methodName = "UsePlenaryRepositoryView";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryRepositoryViewReply;
  }
  export class GetRepository {
    static readonly methodName = "GetRepository";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryReply;
  }
  export class GetRepositoriesByIds {
    static readonly methodName = "GetRepositoriesByIds";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByIdsRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class GetRepositoriesByGenusType {
    static readonly methodName = "GetRepositoriesByGenusType";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class GetRepositoriesByParentGenusType {
    static readonly methodName = "GetRepositoriesByParentGenusType";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class GetRepositoriesByRecordType {
    static readonly methodName = "GetRepositoriesByRecordType";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class GetRepositoriesByProvider {
    static readonly methodName = "GetRepositoriesByProvider";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByProviderRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class GetRepositories {
    static readonly methodName = "GetRepositories";
    static readonly service = RepositoryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
}
export class RepositoryQuerySession {
  static serviceName = "dlkit.proto.repository.RepositoryQuerySession";
}
export namespace RepositoryQuerySession {
  export class CanSearchRepositories {
    static readonly methodName = "CanSearchRepositories";
    static readonly service = RepositoryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanSearchRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanSearchRepositoriesReply;
  }
  export class GetRepositoryQuery {
    static readonly methodName = "GetRepositoryQuery";
    static readonly service = RepositoryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryQueryRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryQueryReply;
  }
  export class GetRepositoriesByQuery {
    static readonly methodName = "GetRepositoriesByQuery";
    static readonly service = RepositoryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoriesByQueryRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
}
export class RepositoryAdminSession {
  static serviceName = "dlkit.proto.repository.RepositoryAdminSession";
}
export namespace RepositoryAdminSession {
  export class CanCreateRepositories {
    static readonly methodName = "CanCreateRepositories";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateRepositoriesReply;
  }
  export class CanCreateRepositoryWithRecordTypes {
    static readonly methodName = "CanCreateRepositoryWithRecordTypes";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanCreateRepositoryWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanCreateRepositoryWithRecordTypesReply;
  }
  export class GetRepositoryFormForCreate {
    static readonly methodName = "GetRepositoryFormForCreate";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryFormForCreateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryFormForCreateReply;
  }
  export class CreateRepository {
    static readonly methodName = "CreateRepository";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CreateRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.CreateRepositoryReply;
  }
  export class CanUpdateRepositories {
    static readonly methodName = "CanUpdateRepositories";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanUpdateRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanUpdateRepositoriesReply;
  }
  export class GetRepositoryFormForUpdate {
    static readonly methodName = "GetRepositoryFormForUpdate";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryFormForUpdateRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryFormForUpdateReply;
  }
  export class UpdateRepository {
    static readonly methodName = "UpdateRepository";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UpdateRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.UpdateRepositoryReply;
  }
  export class CanDeleteRepositories {
    static readonly methodName = "CanDeleteRepositories";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanDeleteRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanDeleteRepositoriesReply;
  }
  export class DeleteRepository {
    static readonly methodName = "DeleteRepository";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.DeleteRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.DeleteRepositoryReply;
  }
  export class CanManageRepositoryAliases {
    static readonly methodName = "CanManageRepositoryAliases";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanManageRepositoryAliasesRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanManageRepositoryAliasesReply;
  }
  export class AliasRepository {
    static readonly methodName = "AliasRepository";
    static readonly service = RepositoryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AliasRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.AliasRepositoryReply;
  }
}
export class RepositoryHierarchySession {
  static serviceName = "dlkit.proto.repository.RepositoryHierarchySession";
}
export namespace RepositoryHierarchySession {
  export class GetRepositoryHierarchyId {
    static readonly methodName = "GetRepositoryHierarchyId";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryHierarchyIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryHierarchyIdReply;
  }
  export class GetRepositoryHierarchy {
    static readonly methodName = "GetRepositoryHierarchy";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryHierarchyRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryHierarchyReply;
  }
  export class CanAccessRepositoryHierarchy {
    static readonly methodName = "CanAccessRepositoryHierarchy";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanAccessRepositoryHierarchyRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanAccessRepositoryHierarchyReply;
  }
  export class UseComparativeRepositoryView {
    static readonly methodName = "UseComparativeRepositoryView";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UseComparativeRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UseComparativeRepositoryViewReply;
  }
  export class UsePlenaryRepositoryView {
    static readonly methodName = "UsePlenaryRepositoryView";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.UsePlenaryRepositoryViewRequest;
    static readonly responseType = dlkit_proto_repository_pb.UsePlenaryRepositoryViewReply;
  }
  export class GetRootRepositoryIds {
    static readonly methodName = "GetRootRepositoryIds";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRootRepositoryIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootRepositories {
    static readonly methodName = "GetRootRepositories";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetRootRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class HasParentRepositories {
    static readonly methodName = "HasParentRepositories";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.HasParentRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.HasParentRepositoriesReply;
  }
  export class IsParentOfRepository {
    static readonly methodName = "IsParentOfRepository";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.IsParentOfRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.IsParentOfRepositoryReply;
  }
  export class GetParentRepositoryIds {
    static readonly methodName = "GetParentRepositoryIds";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetParentRepositoryIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentRepositories {
    static readonly methodName = "GetParentRepositories";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetParentRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class IsAncestorOfRepository {
    static readonly methodName = "IsAncestorOfRepository";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.IsAncestorOfRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.IsAncestorOfRepositoryReply;
  }
  export class HasChildRepositories {
    static readonly methodName = "HasChildRepositories";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.HasChildRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.HasChildRepositoriesReply;
  }
  export class IsChildOfRepository {
    static readonly methodName = "IsChildOfRepository";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.IsChildOfRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.IsChildOfRepositoryReply;
  }
  export class GetChildRepositoryIds {
    static readonly methodName = "GetChildRepositoryIds";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetChildRepositoryIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildRepositories {
    static readonly methodName = "GetChildRepositories";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_repository_pb.GetChildRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.Repository;
  }
  export class IsDescendantOfRepository {
    static readonly methodName = "IsDescendantOfRepository";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.IsDescendantOfRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.IsDescendantOfRepositoryReply;
  }
  export class GetRepositoryNodeIds {
    static readonly methodName = "GetRepositoryNodeIds";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryNodeIdsRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryNodeIdsReply;
  }
  export class GetRepositoryNodes {
    static readonly methodName = "GetRepositoryNodes";
    static readonly service = RepositoryHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryNodesRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryNodesReply;
  }
}
export class RepositoryHierarchyDesignSession {
  static serviceName = "dlkit.proto.repository.RepositoryHierarchyDesignSession";
}
export namespace RepositoryHierarchyDesignSession {
  export class GetRepositoryHierarchyId {
    static readonly methodName = "GetRepositoryHierarchyId";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryHierarchyIdRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryHierarchyIdReply;
  }
  export class GetRepositoryHierarchy {
    static readonly methodName = "GetRepositoryHierarchy";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.GetRepositoryHierarchyRequest;
    static readonly responseType = dlkit_proto_repository_pb.GetRepositoryHierarchyReply;
  }
  export class CanModifyRepositoryHierarchy {
    static readonly methodName = "CanModifyRepositoryHierarchy";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.CanModifyRepositoryHierarchyRequest;
    static readonly responseType = dlkit_proto_repository_pb.CanModifyRepositoryHierarchyReply;
  }
  export class AddRootRepository {
    static readonly methodName = "AddRootRepository";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AddRootRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.AddRootRepositoryReply;
  }
  export class RemoveRootRepository {
    static readonly methodName = "RemoveRootRepository";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RemoveRootRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.RemoveRootRepositoryReply;
  }
  export class AddChildRepository {
    static readonly methodName = "AddChildRepository";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.AddChildRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.AddChildRepositoryReply;
  }
  export class RemoveChildRepository {
    static readonly methodName = "RemoveChildRepository";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RemoveChildRepositoryRequest;
    static readonly responseType = dlkit_proto_repository_pb.RemoveChildRepositoryReply;
  }
  export class RemoveChildRepositories {
    static readonly methodName = "RemoveChildRepositories";
    static readonly service = RepositoryHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_repository_pb.RemoveChildRepositoriesRequest;
    static readonly responseType = dlkit_proto_repository_pb.RemoveChildRepositoriesReply;
  }
}
