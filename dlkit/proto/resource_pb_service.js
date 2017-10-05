// package: dlkit.proto.resource
// file: dlkit/proto/resource.proto

var jspb = require("google-protobuf");
var dlkit_proto_resource_pb = require("../../dlkit/proto/resource_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_authentication_pb = require("../../dlkit/proto/authentication_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var ResourceLookupSession = {
  serviceName: "dlkit.proto.resource.ResourceLookupSession"
};
ResourceLookupSession.GetBinId = {
  methodName: "GetBinId",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinIdReply
};
ResourceLookupSession.GetBin = {
  methodName: "GetBin",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
ResourceLookupSession.CanLookupResources = {
  methodName: "CanLookupResources",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanLookupResourcesRequest,
  responseType: dlkit_proto_resource_pb.CanLookupResourcesReply
};
ResourceLookupSession.UseComparativeResourceView = {
  methodName: "UseComparativeResourceView",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseComparativeResourceViewRequest,
  responseType: dlkit_proto_resource_pb.UseComparativeResourceViewReply
};
ResourceLookupSession.UsePlenaryResourceView = {
  methodName: "UsePlenaryResourceView",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UsePlenaryResourceViewRequest,
  responseType: dlkit_proto_resource_pb.UsePlenaryResourceViewReply
};
ResourceLookupSession.UseFederatedBinView = {
  methodName: "UseFederatedBinView",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseFederatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseFederatedBinViewReply
};
ResourceLookupSession.UseIsolatedBinView = {
  methodName: "UseIsolatedBinView",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseIsolatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseIsolatedBinViewReply
};
ResourceLookupSession.GetResource = {
  methodName: "GetResource",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceRequest,
  responseType: dlkit_proto_resource_pb.GetResourceReply
};
ResourceLookupSession.GetResourcesByIds = {
  methodName: "GetResourcesByIds",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByIdsRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
ResourceLookupSession.GetResourcesByGenusType = {
  methodName: "GetResourcesByGenusType",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByGenusTypeRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
ResourceLookupSession.GetResourcesByParentGenusType = {
  methodName: "GetResourcesByParentGenusType",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByParentGenusTypeRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
ResourceLookupSession.GetResourcesByRecordType = {
  methodName: "GetResourcesByRecordType",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByRecordTypeRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
ResourceLookupSession.GetResources = {
  methodName: "GetResources",
  service: ResourceLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
var ResourceQuerySession = {
  serviceName: "dlkit.proto.resource.ResourceQuerySession"
};
ResourceQuerySession.GetBinId = {
  methodName: "GetBinId",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinIdReply
};
ResourceQuerySession.GetBin = {
  methodName: "GetBin",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
ResourceQuerySession.CanSearchResources = {
  methodName: "CanSearchResources",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanSearchResourcesRequest,
  responseType: dlkit_proto_resource_pb.CanSearchResourcesReply
};
ResourceQuerySession.UseFederatedBinView = {
  methodName: "UseFederatedBinView",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseFederatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseFederatedBinViewReply
};
ResourceQuerySession.UseIsolatedBinView = {
  methodName: "UseIsolatedBinView",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseIsolatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseIsolatedBinViewReply
};
ResourceQuerySession.GetResourceQuery = {
  methodName: "GetResourceQuery",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceQueryRequest,
  responseType: dlkit_proto_resource_pb.GetResourceQueryReply
};
ResourceQuerySession.GetResourcesByQuery = {
  methodName: "GetResourcesByQuery",
  service: ResourceQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByQueryRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
var ResourceSearchSession = {
  serviceName: "dlkit.proto.resource.ResourceSearchSession"
};
ResourceSearchSession.GetResourceSearch = {
  methodName: "GetResourceSearch",
  service: ResourceSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceSearchRequest,
  responseType: dlkit_proto_resource_pb.GetResourceSearchReply
};
ResourceSearchSession.GetResourceSearchOrder = {
  methodName: "GetResourceSearchOrder",
  service: ResourceSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceSearchOrderRequest,
  responseType: dlkit_proto_resource_pb.GetResourceSearchOrderReply
};
ResourceSearchSession.GetResourcesBySearch = {
  methodName: "GetResourcesBySearch",
  service: ResourceSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourcesBySearchRequest,
  responseType: dlkit_proto_resource_pb.GetResourcesBySearchReply
};
ResourceSearchSession.GetResourceQueryFromInspector = {
  methodName: "GetResourceQueryFromInspector",
  service: ResourceSearchSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceQueryFromInspectorRequest,
  responseType: dlkit_proto_resource_pb.GetResourceQueryFromInspectorReply
};
var ResourceAdminSession = {
  serviceName: "dlkit.proto.resource.ResourceAdminSession"
};
ResourceAdminSession.GetBinId = {
  methodName: "GetBinId",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinIdReply
};
ResourceAdminSession.GetBin = {
  methodName: "GetBin",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
ResourceAdminSession.CanCreateResources = {
  methodName: "CanCreateResources",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanCreateResourcesRequest,
  responseType: dlkit_proto_resource_pb.CanCreateResourcesReply
};
ResourceAdminSession.CanCreateResourceWithRecordTypes = {
  methodName: "CanCreateResourceWithRecordTypes",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanCreateResourceWithRecordTypesRequest,
  responseType: dlkit_proto_resource_pb.CanCreateResourceWithRecordTypesReply
};
ResourceAdminSession.GetResourceFormForCreate = {
  methodName: "GetResourceFormForCreate",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceFormForCreateRequest,
  responseType: dlkit_proto_resource_pb.GetResourceFormForCreateReply
};
ResourceAdminSession.CreateResource = {
  methodName: "CreateResource",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CreateResourceRequest,
  responseType: dlkit_proto_resource_pb.CreateResourceReply
};
ResourceAdminSession.CanUpdateResources = {
  methodName: "CanUpdateResources",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanUpdateResourcesRequest,
  responseType: dlkit_proto_resource_pb.CanUpdateResourcesReply
};
ResourceAdminSession.GetResourceFormForUpdate = {
  methodName: "GetResourceFormForUpdate",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceFormForUpdateRequest,
  responseType: dlkit_proto_resource_pb.GetResourceFormForUpdateReply
};
ResourceAdminSession.UpdateResource = {
  methodName: "UpdateResource",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UpdateResourceRequest,
  responseType: dlkit_proto_resource_pb.UpdateResourceReply
};
ResourceAdminSession.CanDeleteResources = {
  methodName: "CanDeleteResources",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanDeleteResourcesRequest,
  responseType: dlkit_proto_resource_pb.CanDeleteResourcesReply
};
ResourceAdminSession.DeleteResource = {
  methodName: "DeleteResource",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.DeleteResourceRequest,
  responseType: dlkit_proto_resource_pb.DeleteResourceReply
};
ResourceAdminSession.CanManageResourceAliases = {
  methodName: "CanManageResourceAliases",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanManageResourceAliasesRequest,
  responseType: dlkit_proto_resource_pb.CanManageResourceAliasesReply
};
ResourceAdminSession.AliasResource = {
  methodName: "AliasResource",
  service: ResourceAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AliasResourceRequest,
  responseType: dlkit_proto_resource_pb.AliasResourceReply
};
var ResourceNotificationSession = {
  serviceName: "dlkit.proto.resource.ResourceNotificationSession"
};
ResourceNotificationSession.GetBinId = {
  methodName: "GetBinId",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinIdReply
};
ResourceNotificationSession.GetBin = {
  methodName: "GetBin",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
ResourceNotificationSession.CanRegisterForResourceNotifications = {
  methodName: "CanRegisterForResourceNotifications",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanRegisterForResourceNotificationsRequest,
  responseType: dlkit_proto_resource_pb.CanRegisterForResourceNotificationsReply
};
ResourceNotificationSession.UseFederatedBinView = {
  methodName: "UseFederatedBinView",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseFederatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseFederatedBinViewReply
};
ResourceNotificationSession.UseIsolatedBinView = {
  methodName: "UseIsolatedBinView",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseIsolatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseIsolatedBinViewReply
};
ResourceNotificationSession.RegisterForNewResources = {
  methodName: "RegisterForNewResources",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RegisterForNewResourcesRequest,
  responseType: dlkit_proto_resource_pb.RegisterForNewResourcesReply
};
ResourceNotificationSession.RegisterForChangedResources = {
  methodName: "RegisterForChangedResources",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RegisterForChangedResourcesRequest,
  responseType: dlkit_proto_resource_pb.RegisterForChangedResourcesReply
};
ResourceNotificationSession.RegisterForChangedResource = {
  methodName: "RegisterForChangedResource",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RegisterForChangedResourceRequest,
  responseType: dlkit_proto_resource_pb.RegisterForChangedResourceReply
};
ResourceNotificationSession.RegisterForDeletedResources = {
  methodName: "RegisterForDeletedResources",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RegisterForDeletedResourcesRequest,
  responseType: dlkit_proto_resource_pb.RegisterForDeletedResourcesReply
};
ResourceNotificationSession.RegisterForDeletedResource = {
  methodName: "RegisterForDeletedResource",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RegisterForDeletedResourceRequest,
  responseType: dlkit_proto_resource_pb.RegisterForDeletedResourceReply
};
ResourceNotificationSession.ReliableResourceNotifications = {
  methodName: "ReliableResourceNotifications",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.ReliableResourceNotificationsRequest,
  responseType: dlkit_proto_resource_pb.ReliableResourceNotificationsReply
};
ResourceNotificationSession.UnreliableResourceNotifications = {
  methodName: "UnreliableResourceNotifications",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UnreliableResourceNotificationsRequest,
  responseType: dlkit_proto_resource_pb.UnreliableResourceNotificationsReply
};
ResourceNotificationSession.AcknowledgeResourceNotification = {
  methodName: "AcknowledgeResourceNotification",
  service: ResourceNotificationSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AcknowledgeResourceNotificationRequest,
  responseType: dlkit_proto_resource_pb.AcknowledgeResourceNotificationReply
};
var ResourceBinSession = {
  serviceName: "dlkit.proto.resource.ResourceBinSession"
};
ResourceBinSession.UseComparativeBinView = {
  methodName: "UseComparativeBinView",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseComparativeBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseComparativeBinViewReply
};
ResourceBinSession.UsePlenaryBinView = {
  methodName: "UsePlenaryBinView",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UsePlenaryBinViewRequest,
  responseType: dlkit_proto_resource_pb.UsePlenaryBinViewReply
};
ResourceBinSession.CanLookupResourceBinMappings = {
  methodName: "CanLookupResourceBinMappings",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanLookupResourceBinMappingsRequest,
  responseType: dlkit_proto_resource_pb.CanLookupResourceBinMappingsReply
};
ResourceBinSession.GetResourceIdsByBin = {
  methodName: "GetResourceIdsByBin",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourceIdsByBinRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ResourceBinSession.GetResourcesByBin = {
  methodName: "GetResourcesByBin",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByBinRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
ResourceBinSession.GetResourceIdsByBins = {
  methodName: "GetResourceIdsByBins",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourceIdsByBinsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ResourceBinSession.GetResourcesByBins = {
  methodName: "GetResourcesByBins",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetResourcesByBinsRequest,
  responseType: dlkit_proto_resource_pb.Resource
};
ResourceBinSession.GetBinIdsByResource = {
  methodName: "GetBinIdsByResource",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinIdsByResourceRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ResourceBinSession.GetBinsByResource = {
  methodName: "GetBinsByResource",
  service: ResourceBinSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByResourceRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
var ResourceBinAssignmentSession = {
  serviceName: "dlkit.proto.resource.ResourceBinAssignmentSession"
};
ResourceBinAssignmentSession.CanAssignResources = {
  methodName: "CanAssignResources",
  service: ResourceBinAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanAssignResourcesRequest,
  responseType: dlkit_proto_resource_pb.CanAssignResourcesReply
};
ResourceBinAssignmentSession.CanAssignResourcesToBin = {
  methodName: "CanAssignResourcesToBin",
  service: ResourceBinAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanAssignResourcesToBinRequest,
  responseType: dlkit_proto_resource_pb.CanAssignResourcesToBinReply
};
ResourceBinAssignmentSession.GetAssignableBinIds = {
  methodName: "GetAssignableBinIds",
  service: ResourceBinAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetAssignableBinIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ResourceBinAssignmentSession.GetAssignableBinIdsForResource = {
  methodName: "GetAssignableBinIdsForResource",
  service: ResourceBinAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetAssignableBinIdsForResourceRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ResourceBinAssignmentSession.AssignResourceToBin = {
  methodName: "AssignResourceToBin",
  service: ResourceBinAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AssignResourceToBinRequest,
  responseType: dlkit_proto_resource_pb.AssignResourceToBinReply
};
ResourceBinAssignmentSession.UnassignResourceFromBin = {
  methodName: "UnassignResourceFromBin",
  service: ResourceBinAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UnassignResourceFromBinRequest,
  responseType: dlkit_proto_resource_pb.UnassignResourceFromBinReply
};
var ResourceAgentSession = {
  serviceName: "dlkit.proto.resource.ResourceAgentSession"
};
ResourceAgentSession.GetBinId = {
  methodName: "GetBinId",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinIdReply
};
ResourceAgentSession.GetBin = {
  methodName: "GetBin",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
ResourceAgentSession.CanLookupResourceAgentMappings = {
  methodName: "CanLookupResourceAgentMappings",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanLookupResourceAgentMappingsRequest,
  responseType: dlkit_proto_resource_pb.CanLookupResourceAgentMappingsReply
};
ResourceAgentSession.UseComparativeAgentView = {
  methodName: "UseComparativeAgentView",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseComparativeAgentViewRequest,
  responseType: dlkit_proto_resource_pb.UseComparativeAgentViewReply
};
ResourceAgentSession.UsePlenaryAgentView = {
  methodName: "UsePlenaryAgentView",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UsePlenaryAgentViewRequest,
  responseType: dlkit_proto_resource_pb.UsePlenaryAgentViewReply
};
ResourceAgentSession.UseFederatedBinView = {
  methodName: "UseFederatedBinView",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseFederatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseFederatedBinViewReply
};
ResourceAgentSession.UseIsolatedBinView = {
  methodName: "UseIsolatedBinView",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseIsolatedBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseIsolatedBinViewReply
};
ResourceAgentSession.GetResourceIdByAgent = {
  methodName: "GetResourceIdByAgent",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceIdByAgentRequest,
  responseType: dlkit_proto_resource_pb.GetResourceIdByAgentReply
};
ResourceAgentSession.GetResourceByAgent = {
  methodName: "GetResourceByAgent",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetResourceByAgentRequest,
  responseType: dlkit_proto_resource_pb.GetResourceByAgentReply
};
ResourceAgentSession.GetAgentIdsByResource = {
  methodName: "GetAgentIdsByResource",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetAgentIdsByResourceRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
ResourceAgentSession.GetAgentsByResource = {
  methodName: "GetAgentsByResource",
  service: ResourceAgentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetAgentsByResourceRequest,
  responseType: dlkit_proto_authentication_pb.Agent
};
var ResourceAgentAssignmentSession = {
  serviceName: "dlkit.proto.resource.ResourceAgentAssignmentSession"
};
ResourceAgentAssignmentSession.GetBinId = {
  methodName: "GetBinId",
  service: ResourceAgentAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinIdReply
};
ResourceAgentAssignmentSession.GetBin = {
  methodName: "GetBin",
  service: ResourceAgentAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
ResourceAgentAssignmentSession.CanAssignAgents = {
  methodName: "CanAssignAgents",
  service: ResourceAgentAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanAssignAgentsRequest,
  responseType: dlkit_proto_resource_pb.CanAssignAgentsReply
};
ResourceAgentAssignmentSession.CanAssignAgentsToResource = {
  methodName: "CanAssignAgentsToResource",
  service: ResourceAgentAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanAssignAgentsToResourceRequest,
  responseType: dlkit_proto_resource_pb.CanAssignAgentsToResourceReply
};
ResourceAgentAssignmentSession.AssignAgentToResource = {
  methodName: "AssignAgentToResource",
  service: ResourceAgentAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AssignAgentToResourceRequest,
  responseType: dlkit_proto_resource_pb.AssignAgentToResourceReply
};
ResourceAgentAssignmentSession.UnassignAgentFromResource = {
  methodName: "UnassignAgentFromResource",
  service: ResourceAgentAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UnassignAgentFromResourceRequest,
  responseType: dlkit_proto_resource_pb.UnassignAgentFromResourceReply
};
var BinLookupSession = {
  serviceName: "dlkit.proto.resource.BinLookupSession"
};
BinLookupSession.CanLookupBins = {
  methodName: "CanLookupBins",
  service: BinLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanLookupBinsRequest,
  responseType: dlkit_proto_resource_pb.CanLookupBinsReply
};
BinLookupSession.UseComparativeBinView = {
  methodName: "UseComparativeBinView",
  service: BinLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseComparativeBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseComparativeBinViewReply
};
BinLookupSession.UsePlenaryBinView = {
  methodName: "UsePlenaryBinView",
  service: BinLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UsePlenaryBinViewRequest,
  responseType: dlkit_proto_resource_pb.UsePlenaryBinViewReply
};
BinLookupSession.GetBin = {
  methodName: "GetBin",
  service: BinLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinRequest,
  responseType: dlkit_proto_resource_pb.GetBinReply
};
BinLookupSession.GetBinsByIds = {
  methodName: "GetBinsByIds",
  service: BinLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByIdsRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinLookupSession.GetBinsByGenusType = {
  methodName: "GetBinsByGenusType",
  service: BinLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByGenusTypeRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinLookupSession.GetBinsByParentGenusType = {
  methodName: "GetBinsByParentGenusType",
  service: BinLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByParentGenusTypeRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinLookupSession.GetBinsByRecordType = {
  methodName: "GetBinsByRecordType",
  service: BinLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByRecordTypeRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinLookupSession.GetBinsByProvider = {
  methodName: "GetBinsByProvider",
  service: BinLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByProviderRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinLookupSession.GetBins = {
  methodName: "GetBins",
  service: BinLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
var BinQuerySession = {
  serviceName: "dlkit.proto.resource.BinQuerySession"
};
BinQuerySession.CanSearchBins = {
  methodName: "CanSearchBins",
  service: BinQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanSearchBinsRequest,
  responseType: dlkit_proto_resource_pb.CanSearchBinsReply
};
BinQuerySession.GetBinQuery = {
  methodName: "GetBinQuery",
  service: BinQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinQueryRequest,
  responseType: dlkit_proto_resource_pb.GetBinQueryReply
};
BinQuerySession.GetBinsByQuery = {
  methodName: "GetBinsByQuery",
  service: BinQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetBinsByQueryRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
var BinAdminSession = {
  serviceName: "dlkit.proto.resource.BinAdminSession"
};
BinAdminSession.CanCreateBins = {
  methodName: "CanCreateBins",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanCreateBinsRequest,
  responseType: dlkit_proto_resource_pb.CanCreateBinsReply
};
BinAdminSession.CanCreateBinWithRecordTypes = {
  methodName: "CanCreateBinWithRecordTypes",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanCreateBinWithRecordTypesRequest,
  responseType: dlkit_proto_resource_pb.CanCreateBinWithRecordTypesReply
};
BinAdminSession.GetBinFormForCreate = {
  methodName: "GetBinFormForCreate",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinFormForCreateRequest,
  responseType: dlkit_proto_resource_pb.GetBinFormForCreateReply
};
BinAdminSession.CreateBin = {
  methodName: "CreateBin",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CreateBinRequest,
  responseType: dlkit_proto_resource_pb.CreateBinReply
};
BinAdminSession.CanUpdateBins = {
  methodName: "CanUpdateBins",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanUpdateBinsRequest,
  responseType: dlkit_proto_resource_pb.CanUpdateBinsReply
};
BinAdminSession.GetBinFormForUpdate = {
  methodName: "GetBinFormForUpdate",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinFormForUpdateRequest,
  responseType: dlkit_proto_resource_pb.GetBinFormForUpdateReply
};
BinAdminSession.UpdateBin = {
  methodName: "UpdateBin",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UpdateBinRequest,
  responseType: dlkit_proto_resource_pb.UpdateBinReply
};
BinAdminSession.CanDeleteBins = {
  methodName: "CanDeleteBins",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanDeleteBinsRequest,
  responseType: dlkit_proto_resource_pb.CanDeleteBinsReply
};
BinAdminSession.DeleteBin = {
  methodName: "DeleteBin",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.DeleteBinRequest,
  responseType: dlkit_proto_resource_pb.DeleteBinReply
};
BinAdminSession.CanManageBinAliases = {
  methodName: "CanManageBinAliases",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanManageBinAliasesRequest,
  responseType: dlkit_proto_resource_pb.CanManageBinAliasesReply
};
BinAdminSession.AliasBin = {
  methodName: "AliasBin",
  service: BinAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AliasBinRequest,
  responseType: dlkit_proto_resource_pb.AliasBinReply
};
var BinHierarchySession = {
  serviceName: "dlkit.proto.resource.BinHierarchySession"
};
BinHierarchySession.GetBinHierarchyId = {
  methodName: "GetBinHierarchyId",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinHierarchyIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinHierarchyIdReply
};
BinHierarchySession.GetBinHierarchy = {
  methodName: "GetBinHierarchy",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinHierarchyRequest,
  responseType: dlkit_proto_resource_pb.GetBinHierarchyReply
};
BinHierarchySession.CanAccessBinHierarchy = {
  methodName: "CanAccessBinHierarchy",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanAccessBinHierarchyRequest,
  responseType: dlkit_proto_resource_pb.CanAccessBinHierarchyReply
};
BinHierarchySession.UseComparativeBinView = {
  methodName: "UseComparativeBinView",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UseComparativeBinViewRequest,
  responseType: dlkit_proto_resource_pb.UseComparativeBinViewReply
};
BinHierarchySession.UsePlenaryBinView = {
  methodName: "UsePlenaryBinView",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.UsePlenaryBinViewRequest,
  responseType: dlkit_proto_resource_pb.UsePlenaryBinViewReply
};
BinHierarchySession.GetRootBinIds = {
  methodName: "GetRootBinIds",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetRootBinIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BinHierarchySession.GetRootBins = {
  methodName: "GetRootBins",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetRootBinsRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinHierarchySession.HasParentBins = {
  methodName: "HasParentBins",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.HasParentBinsRequest,
  responseType: dlkit_proto_resource_pb.HasParentBinsReply
};
BinHierarchySession.IsParentOfBin = {
  methodName: "IsParentOfBin",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.IsParentOfBinRequest,
  responseType: dlkit_proto_resource_pb.IsParentOfBinReply
};
BinHierarchySession.GetParentBinIds = {
  methodName: "GetParentBinIds",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetParentBinIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BinHierarchySession.GetParentBins = {
  methodName: "GetParentBins",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetParentBinsRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinHierarchySession.IsAncestorOfBin = {
  methodName: "IsAncestorOfBin",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.IsAncestorOfBinRequest,
  responseType: dlkit_proto_resource_pb.IsAncestorOfBinReply
};
BinHierarchySession.HasChildBins = {
  methodName: "HasChildBins",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.HasChildBinsRequest,
  responseType: dlkit_proto_resource_pb.HasChildBinsReply
};
BinHierarchySession.IsChildOfBin = {
  methodName: "IsChildOfBin",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.IsChildOfBinRequest,
  responseType: dlkit_proto_resource_pb.IsChildOfBinReply
};
BinHierarchySession.GetChildBinIds = {
  methodName: "GetChildBinIds",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetChildBinIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BinHierarchySession.GetChildBins = {
  methodName: "GetChildBins",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_resource_pb.GetChildBinsRequest,
  responseType: dlkit_proto_resource_pb.Bin
};
BinHierarchySession.IsDescendantOfBin = {
  methodName: "IsDescendantOfBin",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.IsDescendantOfBinRequest,
  responseType: dlkit_proto_resource_pb.IsDescendantOfBinReply
};
BinHierarchySession.GetBinNodeIds = {
  methodName: "GetBinNodeIds",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinNodeIdsRequest,
  responseType: dlkit_proto_resource_pb.GetBinNodeIdsReply
};
BinHierarchySession.GetBinNodes = {
  methodName: "GetBinNodes",
  service: BinHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinNodesRequest,
  responseType: dlkit_proto_resource_pb.GetBinNodesReply
};
var BinHierarchyDesignSession = {
  serviceName: "dlkit.proto.resource.BinHierarchyDesignSession"
};
BinHierarchyDesignSession.GetBinHierarchyId = {
  methodName: "GetBinHierarchyId",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinHierarchyIdRequest,
  responseType: dlkit_proto_resource_pb.GetBinHierarchyIdReply
};
BinHierarchyDesignSession.GetBinHierarchy = {
  methodName: "GetBinHierarchy",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.GetBinHierarchyRequest,
  responseType: dlkit_proto_resource_pb.GetBinHierarchyReply
};
BinHierarchyDesignSession.CanModifyBinHierarchy = {
  methodName: "CanModifyBinHierarchy",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.CanModifyBinHierarchyRequest,
  responseType: dlkit_proto_resource_pb.CanModifyBinHierarchyReply
};
BinHierarchyDesignSession.AddRootBin = {
  methodName: "AddRootBin",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AddRootBinRequest,
  responseType: dlkit_proto_resource_pb.AddRootBinReply
};
BinHierarchyDesignSession.RemoveRootBin = {
  methodName: "RemoveRootBin",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RemoveRootBinRequest,
  responseType: dlkit_proto_resource_pb.RemoveRootBinReply
};
BinHierarchyDesignSession.AddChildBin = {
  methodName: "AddChildBin",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.AddChildBinRequest,
  responseType: dlkit_proto_resource_pb.AddChildBinReply
};
BinHierarchyDesignSession.RemoveChildBin = {
  methodName: "RemoveChildBin",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RemoveChildBinRequest,
  responseType: dlkit_proto_resource_pb.RemoveChildBinReply
};
BinHierarchyDesignSession.RemoveChildBins = {
  methodName: "RemoveChildBins",
  service: BinHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_resource_pb.RemoveChildBinsRequest,
  responseType: dlkit_proto_resource_pb.RemoveChildBinsReply
};
module.exports = {
  ResourceLookupSession: ResourceLookupSession,
  ResourceQuerySession: ResourceQuerySession,
  ResourceSearchSession: ResourceSearchSession,
  ResourceAdminSession: ResourceAdminSession,
  ResourceNotificationSession: ResourceNotificationSession,
  ResourceBinSession: ResourceBinSession,
  ResourceBinAssignmentSession: ResourceBinAssignmentSession,
  ResourceAgentSession: ResourceAgentSession,
  ResourceAgentAssignmentSession: ResourceAgentAssignmentSession,
  BinLookupSession: BinLookupSession,
  BinQuerySession: BinQuerySession,
  BinAdminSession: BinAdminSession,
  BinHierarchySession: BinHierarchySession,
  BinHierarchyDesignSession: BinHierarchyDesignSession,
};

