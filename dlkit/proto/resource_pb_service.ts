// package: dlkit.proto.resource
// file: dlkit/proto/resource.proto

import * as dlkit_proto_resource_pb from "../../dlkit/proto/resource_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_authentication_pb from "../../dlkit/proto/authentication_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
export class ResourceLookupSession {
  static serviceName = "dlkit.proto.resource.ResourceLookupSession";
}
export namespace ResourceLookupSession {
  export class GetBinId {
    static readonly methodName = "GetBinId";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinIdReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class CanLookupResources {
    static readonly methodName = "CanLookupResources";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanLookupResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanLookupResourcesReply;
  }
  export class UseComparativeResourceView {
    static readonly methodName = "UseComparativeResourceView";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseComparativeResourceViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseComparativeResourceViewReply;
  }
  export class UsePlenaryResourceView {
    static readonly methodName = "UsePlenaryResourceView";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UsePlenaryResourceViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UsePlenaryResourceViewReply;
  }
  export class UseFederatedBinView {
    static readonly methodName = "UseFederatedBinView";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseFederatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseFederatedBinViewReply;
  }
  export class UseIsolatedBinView {
    static readonly methodName = "UseIsolatedBinView";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseIsolatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseIsolatedBinViewReply;
  }
  export class GetResource {
    static readonly methodName = "GetResource";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceReply;
  }
  export class GetResourcesByIds {
    static readonly methodName = "GetResourcesByIds";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByIdsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
  export class GetResourcesByGenusType {
    static readonly methodName = "GetResourcesByGenusType";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
  export class GetResourcesByParentGenusType {
    static readonly methodName = "GetResourcesByParentGenusType";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
  export class GetResourcesByRecordType {
    static readonly methodName = "GetResourcesByRecordType";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
  export class GetResources {
    static readonly methodName = "GetResources";
    static readonly service = ResourceLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
}
export class ResourceQuerySession {
  static serviceName = "dlkit.proto.resource.ResourceQuerySession";
}
export namespace ResourceQuerySession {
  export class GetBinId {
    static readonly methodName = "GetBinId";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinIdReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class CanSearchResources {
    static readonly methodName = "CanSearchResources";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanSearchResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanSearchResourcesReply;
  }
  export class UseFederatedBinView {
    static readonly methodName = "UseFederatedBinView";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseFederatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseFederatedBinViewReply;
  }
  export class UseIsolatedBinView {
    static readonly methodName = "UseIsolatedBinView";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseIsolatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseIsolatedBinViewReply;
  }
  export class GetResourceQuery {
    static readonly methodName = "GetResourceQuery";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceQueryRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceQueryReply;
  }
  export class GetResourcesByQuery {
    static readonly methodName = "GetResourcesByQuery";
    static readonly service = ResourceQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByQueryRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
}
export class ResourceSearchSession {
  static serviceName = "dlkit.proto.resource.ResourceSearchSession";
}
export namespace ResourceSearchSession {
  export class GetResourceSearch {
    static readonly methodName = "GetResourceSearch";
    static readonly service = ResourceSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceSearchRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceSearchReply;
  }
  export class GetResourceSearchOrder {
    static readonly methodName = "GetResourceSearchOrder";
    static readonly service = ResourceSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceSearchOrderRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceSearchOrderReply;
  }
  export class GetResourcesBySearch {
    static readonly methodName = "GetResourcesBySearch";
    static readonly service = ResourceSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesBySearchRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourcesBySearchReply;
  }
  export class GetResourceQueryFromInspector {
    static readonly methodName = "GetResourceQueryFromInspector";
    static readonly service = ResourceSearchSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceQueryFromInspectorRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceQueryFromInspectorReply;
  }
}
export class ResourceAdminSession {
  static serviceName = "dlkit.proto.resource.ResourceAdminSession";
}
export namespace ResourceAdminSession {
  export class GetBinId {
    static readonly methodName = "GetBinId";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinIdReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class CanCreateResources {
    static readonly methodName = "CanCreateResources";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanCreateResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanCreateResourcesReply;
  }
  export class CanCreateResourceWithRecordTypes {
    static readonly methodName = "CanCreateResourceWithRecordTypes";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanCreateResourceWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanCreateResourceWithRecordTypesReply;
  }
  export class GetResourceFormForCreate {
    static readonly methodName = "GetResourceFormForCreate";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceFormForCreateRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceFormForCreateReply;
  }
  export class CreateResource {
    static readonly methodName = "CreateResource";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CreateResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.CreateResourceReply;
  }
  export class CanUpdateResources {
    static readonly methodName = "CanUpdateResources";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanUpdateResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanUpdateResourcesReply;
  }
  export class GetResourceFormForUpdate {
    static readonly methodName = "GetResourceFormForUpdate";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceFormForUpdateRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceFormForUpdateReply;
  }
  export class UpdateResource {
    static readonly methodName = "UpdateResource";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UpdateResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.UpdateResourceReply;
  }
  export class CanDeleteResources {
    static readonly methodName = "CanDeleteResources";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanDeleteResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanDeleteResourcesReply;
  }
  export class DeleteResource {
    static readonly methodName = "DeleteResource";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.DeleteResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.DeleteResourceReply;
  }
  export class CanManageResourceAliases {
    static readonly methodName = "CanManageResourceAliases";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanManageResourceAliasesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanManageResourceAliasesReply;
  }
  export class AliasResource {
    static readonly methodName = "AliasResource";
    static readonly service = ResourceAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AliasResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.AliasResourceReply;
  }
}
export class ResourceNotificationSession {
  static serviceName = "dlkit.proto.resource.ResourceNotificationSession";
}
export namespace ResourceNotificationSession {
  export class GetBinId {
    static readonly methodName = "GetBinId";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinIdReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class CanRegisterForResourceNotifications {
    static readonly methodName = "CanRegisterForResourceNotifications";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanRegisterForResourceNotificationsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanRegisterForResourceNotificationsReply;
  }
  export class UseFederatedBinView {
    static readonly methodName = "UseFederatedBinView";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseFederatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseFederatedBinViewReply;
  }
  export class UseIsolatedBinView {
    static readonly methodName = "UseIsolatedBinView";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseIsolatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseIsolatedBinViewReply;
  }
  export class RegisterForNewResources {
    static readonly methodName = "RegisterForNewResources";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RegisterForNewResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.RegisterForNewResourcesReply;
  }
  export class RegisterForChangedResources {
    static readonly methodName = "RegisterForChangedResources";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RegisterForChangedResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.RegisterForChangedResourcesReply;
  }
  export class RegisterForChangedResource {
    static readonly methodName = "RegisterForChangedResource";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RegisterForChangedResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.RegisterForChangedResourceReply;
  }
  export class RegisterForDeletedResources {
    static readonly methodName = "RegisterForDeletedResources";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RegisterForDeletedResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.RegisterForDeletedResourcesReply;
  }
  export class RegisterForDeletedResource {
    static readonly methodName = "RegisterForDeletedResource";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RegisterForDeletedResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.RegisterForDeletedResourceReply;
  }
  export class ReliableResourceNotifications {
    static readonly methodName = "ReliableResourceNotifications";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.ReliableResourceNotificationsRequest;
    static readonly responseType = dlkit_proto_resource_pb.ReliableResourceNotificationsReply;
  }
  export class UnreliableResourceNotifications {
    static readonly methodName = "UnreliableResourceNotifications";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UnreliableResourceNotificationsRequest;
    static readonly responseType = dlkit_proto_resource_pb.UnreliableResourceNotificationsReply;
  }
  export class AcknowledgeResourceNotification {
    static readonly methodName = "AcknowledgeResourceNotification";
    static readonly service = ResourceNotificationSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AcknowledgeResourceNotificationRequest;
    static readonly responseType = dlkit_proto_resource_pb.AcknowledgeResourceNotificationReply;
  }
}
export class ResourceBinSession {
  static serviceName = "dlkit.proto.resource.ResourceBinSession";
}
export namespace ResourceBinSession {
  export class UseComparativeBinView {
    static readonly methodName = "UseComparativeBinView";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseComparativeBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseComparativeBinViewReply;
  }
  export class UsePlenaryBinView {
    static readonly methodName = "UsePlenaryBinView";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UsePlenaryBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UsePlenaryBinViewReply;
  }
  export class CanLookupResourceBinMappings {
    static readonly methodName = "CanLookupResourceBinMappings";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanLookupResourceBinMappingsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanLookupResourceBinMappingsReply;
  }
  export class GetResourceIdsByBin {
    static readonly methodName = "GetResourceIdsByBin";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceIdsByBinRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetResourcesByBin {
    static readonly methodName = "GetResourcesByBin";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
  export class GetResourceIdsByBins {
    static readonly methodName = "GetResourceIdsByBins";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceIdsByBinsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetResourcesByBins {
    static readonly methodName = "GetResourcesByBins";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetResourcesByBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Resource;
  }
  export class GetBinIdsByResource {
    static readonly methodName = "GetBinIdsByResource";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdsByResourceRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBinsByResource {
    static readonly methodName = "GetBinsByResource";
    static readonly service = ResourceBinSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
}
export class ResourceBinAssignmentSession {
  static serviceName = "dlkit.proto.resource.ResourceBinAssignmentSession";
}
export namespace ResourceBinAssignmentSession {
  export class CanAssignResources {
    static readonly methodName = "CanAssignResources";
    static readonly service = ResourceBinAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanAssignResourcesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanAssignResourcesReply;
  }
  export class CanAssignResourcesToBin {
    static readonly methodName = "CanAssignResourcesToBin";
    static readonly service = ResourceBinAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanAssignResourcesToBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanAssignResourcesToBinReply;
  }
  export class GetAssignableBinIds {
    static readonly methodName = "GetAssignableBinIds";
    static readonly service = ResourceBinAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetAssignableBinIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBinIdsForResource {
    static readonly methodName = "GetAssignableBinIdsForResource";
    static readonly service = ResourceBinAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetAssignableBinIdsForResourceRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignResourceToBin {
    static readonly methodName = "AssignResourceToBin";
    static readonly service = ResourceBinAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AssignResourceToBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.AssignResourceToBinReply;
  }
  export class UnassignResourceFromBin {
    static readonly methodName = "UnassignResourceFromBin";
    static readonly service = ResourceBinAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UnassignResourceFromBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.UnassignResourceFromBinReply;
  }
}
export class ResourceAgentSession {
  static serviceName = "dlkit.proto.resource.ResourceAgentSession";
}
export namespace ResourceAgentSession {
  export class GetBinId {
    static readonly methodName = "GetBinId";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinIdReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class CanLookupResourceAgentMappings {
    static readonly methodName = "CanLookupResourceAgentMappings";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanLookupResourceAgentMappingsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanLookupResourceAgentMappingsReply;
  }
  export class UseComparativeAgentView {
    static readonly methodName = "UseComparativeAgentView";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseComparativeAgentViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseComparativeAgentViewReply;
  }
  export class UsePlenaryAgentView {
    static readonly methodName = "UsePlenaryAgentView";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UsePlenaryAgentViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UsePlenaryAgentViewReply;
  }
  export class UseFederatedBinView {
    static readonly methodName = "UseFederatedBinView";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseFederatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseFederatedBinViewReply;
  }
  export class UseIsolatedBinView {
    static readonly methodName = "UseIsolatedBinView";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseIsolatedBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseIsolatedBinViewReply;
  }
  export class GetResourceIdByAgent {
    static readonly methodName = "GetResourceIdByAgent";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceIdByAgentRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceIdByAgentReply;
  }
  export class GetResourceByAgent {
    static readonly methodName = "GetResourceByAgent";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetResourceByAgentRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetResourceByAgentReply;
  }
  export class GetAgentIdsByResource {
    static readonly methodName = "GetAgentIdsByResource";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetAgentIdsByResourceRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAgentsByResource {
    static readonly methodName = "GetAgentsByResource";
    static readonly service = ResourceAgentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetAgentsByResourceRequest;
    static readonly responseType = dlkit_proto_authentication_pb.Agent;
  }
}
export class ResourceAgentAssignmentSession {
  static serviceName = "dlkit.proto.resource.ResourceAgentAssignmentSession";
}
export namespace ResourceAgentAssignmentSession {
  export class GetBinId {
    static readonly methodName = "GetBinId";
    static readonly service = ResourceAgentAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinIdReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = ResourceAgentAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class CanAssignAgents {
    static readonly methodName = "CanAssignAgents";
    static readonly service = ResourceAgentAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanAssignAgentsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanAssignAgentsReply;
  }
  export class CanAssignAgentsToResource {
    static readonly methodName = "CanAssignAgentsToResource";
    static readonly service = ResourceAgentAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanAssignAgentsToResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanAssignAgentsToResourceReply;
  }
  export class AssignAgentToResource {
    static readonly methodName = "AssignAgentToResource";
    static readonly service = ResourceAgentAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AssignAgentToResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.AssignAgentToResourceReply;
  }
  export class UnassignAgentFromResource {
    static readonly methodName = "UnassignAgentFromResource";
    static readonly service = ResourceAgentAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UnassignAgentFromResourceRequest;
    static readonly responseType = dlkit_proto_resource_pb.UnassignAgentFromResourceReply;
  }
}
export class BinLookupSession {
  static serviceName = "dlkit.proto.resource.BinLookupSession";
}
export namespace BinLookupSession {
  export class CanLookupBins {
    static readonly methodName = "CanLookupBins";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanLookupBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanLookupBinsReply;
  }
  export class UseComparativeBinView {
    static readonly methodName = "UseComparativeBinView";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseComparativeBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseComparativeBinViewReply;
  }
  export class UsePlenaryBinView {
    static readonly methodName = "UsePlenaryBinView";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UsePlenaryBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UsePlenaryBinViewReply;
  }
  export class GetBin {
    static readonly methodName = "GetBin";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinReply;
  }
  export class GetBinsByIds {
    static readonly methodName = "GetBinsByIds";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByIdsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class GetBinsByGenusType {
    static readonly methodName = "GetBinsByGenusType";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class GetBinsByParentGenusType {
    static readonly methodName = "GetBinsByParentGenusType";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class GetBinsByRecordType {
    static readonly methodName = "GetBinsByRecordType";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class GetBinsByProvider {
    static readonly methodName = "GetBinsByProvider";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByProviderRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class GetBins {
    static readonly methodName = "GetBins";
    static readonly service = BinLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
}
export class BinQuerySession {
  static serviceName = "dlkit.proto.resource.BinQuerySession";
}
export namespace BinQuerySession {
  export class CanSearchBins {
    static readonly methodName = "CanSearchBins";
    static readonly service = BinQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanSearchBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanSearchBinsReply;
  }
  export class GetBinQuery {
    static readonly methodName = "GetBinQuery";
    static readonly service = BinQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinQueryRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinQueryReply;
  }
  export class GetBinsByQuery {
    static readonly methodName = "GetBinsByQuery";
    static readonly service = BinQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetBinsByQueryRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
}
export class BinAdminSession {
  static serviceName = "dlkit.proto.resource.BinAdminSession";
}
export namespace BinAdminSession {
  export class CanCreateBins {
    static readonly methodName = "CanCreateBins";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanCreateBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanCreateBinsReply;
  }
  export class CanCreateBinWithRecordTypes {
    static readonly methodName = "CanCreateBinWithRecordTypes";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanCreateBinWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanCreateBinWithRecordTypesReply;
  }
  export class GetBinFormForCreate {
    static readonly methodName = "GetBinFormForCreate";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinFormForCreateRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinFormForCreateReply;
  }
  export class CreateBin {
    static readonly methodName = "CreateBin";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CreateBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.CreateBinReply;
  }
  export class CanUpdateBins {
    static readonly methodName = "CanUpdateBins";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanUpdateBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanUpdateBinsReply;
  }
  export class GetBinFormForUpdate {
    static readonly methodName = "GetBinFormForUpdate";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinFormForUpdateRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinFormForUpdateReply;
  }
  export class UpdateBin {
    static readonly methodName = "UpdateBin";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UpdateBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.UpdateBinReply;
  }
  export class CanDeleteBins {
    static readonly methodName = "CanDeleteBins";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanDeleteBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanDeleteBinsReply;
  }
  export class DeleteBin {
    static readonly methodName = "DeleteBin";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.DeleteBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.DeleteBinReply;
  }
  export class CanManageBinAliases {
    static readonly methodName = "CanManageBinAliases";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanManageBinAliasesRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanManageBinAliasesReply;
  }
  export class AliasBin {
    static readonly methodName = "AliasBin";
    static readonly service = BinAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AliasBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.AliasBinReply;
  }
}
export class BinHierarchySession {
  static serviceName = "dlkit.proto.resource.BinHierarchySession";
}
export namespace BinHierarchySession {
  export class GetBinHierarchyId {
    static readonly methodName = "GetBinHierarchyId";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinHierarchyIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinHierarchyIdReply;
  }
  export class GetBinHierarchy {
    static readonly methodName = "GetBinHierarchy";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinHierarchyRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinHierarchyReply;
  }
  export class CanAccessBinHierarchy {
    static readonly methodName = "CanAccessBinHierarchy";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanAccessBinHierarchyRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanAccessBinHierarchyReply;
  }
  export class UseComparativeBinView {
    static readonly methodName = "UseComparativeBinView";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UseComparativeBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UseComparativeBinViewReply;
  }
  export class UsePlenaryBinView {
    static readonly methodName = "UsePlenaryBinView";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.UsePlenaryBinViewRequest;
    static readonly responseType = dlkit_proto_resource_pb.UsePlenaryBinViewReply;
  }
  export class GetRootBinIds {
    static readonly methodName = "GetRootBinIds";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetRootBinIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootBins {
    static readonly methodName = "GetRootBins";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetRootBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class HasParentBins {
    static readonly methodName = "HasParentBins";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.HasParentBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.HasParentBinsReply;
  }
  export class IsParentOfBin {
    static readonly methodName = "IsParentOfBin";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.IsParentOfBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.IsParentOfBinReply;
  }
  export class GetParentBinIds {
    static readonly methodName = "GetParentBinIds";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetParentBinIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentBins {
    static readonly methodName = "GetParentBins";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetParentBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class IsAncestorOfBin {
    static readonly methodName = "IsAncestorOfBin";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.IsAncestorOfBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.IsAncestorOfBinReply;
  }
  export class HasChildBins {
    static readonly methodName = "HasChildBins";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.HasChildBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.HasChildBinsReply;
  }
  export class IsChildOfBin {
    static readonly methodName = "IsChildOfBin";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.IsChildOfBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.IsChildOfBinReply;
  }
  export class GetChildBinIds {
    static readonly methodName = "GetChildBinIds";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetChildBinIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildBins {
    static readonly methodName = "GetChildBins";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_resource_pb.GetChildBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.Bin;
  }
  export class IsDescendantOfBin {
    static readonly methodName = "IsDescendantOfBin";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.IsDescendantOfBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.IsDescendantOfBinReply;
  }
  export class GetBinNodeIds {
    static readonly methodName = "GetBinNodeIds";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinNodeIdsRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinNodeIdsReply;
  }
  export class GetBinNodes {
    static readonly methodName = "GetBinNodes";
    static readonly service = BinHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinNodesRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinNodesReply;
  }
}
export class BinHierarchyDesignSession {
  static serviceName = "dlkit.proto.resource.BinHierarchyDesignSession";
}
export namespace BinHierarchyDesignSession {
  export class GetBinHierarchyId {
    static readonly methodName = "GetBinHierarchyId";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinHierarchyIdRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinHierarchyIdReply;
  }
  export class GetBinHierarchy {
    static readonly methodName = "GetBinHierarchy";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.GetBinHierarchyRequest;
    static readonly responseType = dlkit_proto_resource_pb.GetBinHierarchyReply;
  }
  export class CanModifyBinHierarchy {
    static readonly methodName = "CanModifyBinHierarchy";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.CanModifyBinHierarchyRequest;
    static readonly responseType = dlkit_proto_resource_pb.CanModifyBinHierarchyReply;
  }
  export class AddRootBin {
    static readonly methodName = "AddRootBin";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AddRootBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.AddRootBinReply;
  }
  export class RemoveRootBin {
    static readonly methodName = "RemoveRootBin";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RemoveRootBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.RemoveRootBinReply;
  }
  export class AddChildBin {
    static readonly methodName = "AddChildBin";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.AddChildBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.AddChildBinReply;
  }
  export class RemoveChildBin {
    static readonly methodName = "RemoveChildBin";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RemoveChildBinRequest;
    static readonly responseType = dlkit_proto_resource_pb.RemoveChildBinReply;
  }
  export class RemoveChildBins {
    static readonly methodName = "RemoveChildBins";
    static readonly service = BinHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_resource_pb.RemoveChildBinsRequest;
    static readonly responseType = dlkit_proto_resource_pb.RemoveChildBinsReply;
  }
}
