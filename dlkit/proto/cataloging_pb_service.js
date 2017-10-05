// package: dlkit.proto.cataloging
// file: dlkit/proto/cataloging.proto

var jspb = require("google-protobuf");
var dlkit_proto_cataloging_pb = require("../../dlkit/proto/cataloging_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var CatalogLookupSession = {
  serviceName: "dlkit.proto.cataloging.CatalogLookupSession"
};
CatalogLookupSession.CanLookupCatalogs = {
  methodName: "CanLookupCatalogs",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanLookupCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.CanLookupCatalogsReply
};
CatalogLookupSession.UseComparativeCatalogView = {
  methodName: "UseComparativeCatalogView",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.UseComparativeCatalogViewRequest,
  responseType: dlkit_proto_cataloging_pb.UseComparativeCatalogViewReply
};
CatalogLookupSession.UsePlenaryCatalogView = {
  methodName: "UsePlenaryCatalogView",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.UsePlenaryCatalogViewRequest,
  responseType: dlkit_proto_cataloging_pb.UsePlenaryCatalogViewReply
};
CatalogLookupSession.GetCatalog = {
  methodName: "GetCatalog",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogReply
};
CatalogLookupSession.GetCatalogsByIds = {
  methodName: "GetCatalogsByIds",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsByIdsRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogLookupSession.GetCatalogsByGenusType = {
  methodName: "GetCatalogsByGenusType",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsByGenusTypeRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogLookupSession.GetCatalogsByParentGenusType = {
  methodName: "GetCatalogsByParentGenusType",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsByParentGenusTypeRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogLookupSession.GetCatalogsByRecordType = {
  methodName: "GetCatalogsByRecordType",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsByRecordTypeRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogLookupSession.GetCatalogsByProvider = {
  methodName: "GetCatalogsByProvider",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsByProviderRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogLookupSession.GetCatalogs = {
  methodName: "GetCatalogs",
  service: CatalogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
var CatalogQuerySession = {
  serviceName: "dlkit.proto.cataloging.CatalogQuerySession"
};
CatalogQuerySession.CanSearchCatalogs = {
  methodName: "CanSearchCatalogs",
  service: CatalogQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanSearchCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.CanSearchCatalogsReply
};
CatalogQuerySession.GetCatalogQuery = {
  methodName: "GetCatalogQuery",
  service: CatalogQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogQueryRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogQueryReply
};
CatalogQuerySession.GetCatalogsByQuery = {
  methodName: "GetCatalogsByQuery",
  service: CatalogQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetCatalogsByQueryRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
var CatalogAdminSession = {
  serviceName: "dlkit.proto.cataloging.CatalogAdminSession"
};
CatalogAdminSession.CanCreateCatalogs = {
  methodName: "CanCreateCatalogs",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanCreateCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.CanCreateCatalogsReply
};
CatalogAdminSession.CanCreateCatalogWithRecordTypes = {
  methodName: "CanCreateCatalogWithRecordTypes",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanCreateCatalogWithRecordTypesRequest,
  responseType: dlkit_proto_cataloging_pb.CanCreateCatalogWithRecordTypesReply
};
CatalogAdminSession.GetCatalogFormForCreate = {
  methodName: "GetCatalogFormForCreate",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogFormForCreateRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogFormForCreateReply
};
CatalogAdminSession.CreateCatalog = {
  methodName: "CreateCatalog",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CreateCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.CreateCatalogReply
};
CatalogAdminSession.CanUpdateCatalogs = {
  methodName: "CanUpdateCatalogs",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanUpdateCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.CanUpdateCatalogsReply
};
CatalogAdminSession.GetCatalogFormForUpdate = {
  methodName: "GetCatalogFormForUpdate",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogFormForUpdateRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogFormForUpdateReply
};
CatalogAdminSession.UpdateCatalog = {
  methodName: "UpdateCatalog",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.UpdateCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.UpdateCatalogReply
};
CatalogAdminSession.CanDeleteCatalogs = {
  methodName: "CanDeleteCatalogs",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanDeleteCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.CanDeleteCatalogsReply
};
CatalogAdminSession.DeleteCatalog = {
  methodName: "DeleteCatalog",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.DeleteCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.DeleteCatalogReply
};
CatalogAdminSession.CanManageCatalogAliases = {
  methodName: "CanManageCatalogAliases",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanManageCatalogAliasesRequest,
  responseType: dlkit_proto_cataloging_pb.CanManageCatalogAliasesReply
};
CatalogAdminSession.AliasCatalog = {
  methodName: "AliasCatalog",
  service: CatalogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.AliasCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.AliasCatalogReply
};
var CatalogHierarchySession = {
  serviceName: "dlkit.proto.cataloging.CatalogHierarchySession"
};
CatalogHierarchySession.GetCatalogHierarchyId = {
  methodName: "GetCatalogHierarchyId",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogHierarchyIdRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogHierarchyIdReply
};
CatalogHierarchySession.GetCatalogHierarchy = {
  methodName: "GetCatalogHierarchy",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogHierarchyRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogHierarchyReply
};
CatalogHierarchySession.CanAccessCatalogHierarchy = {
  methodName: "CanAccessCatalogHierarchy",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanAccessCatalogHierarchyRequest,
  responseType: dlkit_proto_cataloging_pb.CanAccessCatalogHierarchyReply
};
CatalogHierarchySession.UseComparativeCatalogView = {
  methodName: "UseComparativeCatalogView",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.UseComparativeCatalogViewRequest,
  responseType: dlkit_proto_cataloging_pb.UseComparativeCatalogViewReply
};
CatalogHierarchySession.UsePlenaryCatalogView = {
  methodName: "UsePlenaryCatalogView",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.UsePlenaryCatalogViewRequest,
  responseType: dlkit_proto_cataloging_pb.UsePlenaryCatalogViewReply
};
CatalogHierarchySession.GetRootCatalogIds = {
  methodName: "GetRootCatalogIds",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetRootCatalogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CatalogHierarchySession.GetRootCatalogs = {
  methodName: "GetRootCatalogs",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetRootCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogHierarchySession.HasParentCatalogs = {
  methodName: "HasParentCatalogs",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.HasParentCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.HasParentCatalogsReply
};
CatalogHierarchySession.IsParentOfCatalog = {
  methodName: "IsParentOfCatalog",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.IsParentOfCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.IsParentOfCatalogReply
};
CatalogHierarchySession.GetParentCatalogIds = {
  methodName: "GetParentCatalogIds",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetParentCatalogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CatalogHierarchySession.GetParentCatalogs = {
  methodName: "GetParentCatalogs",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetParentCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogHierarchySession.IsAncestorOfCatalog = {
  methodName: "IsAncestorOfCatalog",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.IsAncestorOfCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.IsAncestorOfCatalogReply
};
CatalogHierarchySession.HasChildCatalogs = {
  methodName: "HasChildCatalogs",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.HasChildCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.HasChildCatalogsReply
};
CatalogHierarchySession.IsChildOfCatalog = {
  methodName: "IsChildOfCatalog",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.IsChildOfCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.IsChildOfCatalogReply
};
CatalogHierarchySession.GetChildCatalogIds = {
  methodName: "GetChildCatalogIds",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetChildCatalogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CatalogHierarchySession.GetChildCatalogs = {
  methodName: "GetChildCatalogs",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_cataloging_pb.GetChildCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.Catalog
};
CatalogHierarchySession.IsDescendantOfCatalog = {
  methodName: "IsDescendantOfCatalog",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.IsDescendantOfCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.IsDescendantOfCatalogReply
};
CatalogHierarchySession.GetCatalogNodeIds = {
  methodName: "GetCatalogNodeIds",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogNodeIdsRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogNodeIdsReply
};
CatalogHierarchySession.GetCatalogNodes = {
  methodName: "GetCatalogNodes",
  service: CatalogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogNodesRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogNodesReply
};
var CatalogHierarchyDesignSession = {
  serviceName: "dlkit.proto.cataloging.CatalogHierarchyDesignSession"
};
CatalogHierarchyDesignSession.GetCatalogHierarchyId = {
  methodName: "GetCatalogHierarchyId",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogHierarchyIdRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogHierarchyIdReply
};
CatalogHierarchyDesignSession.GetCatalogHierarchy = {
  methodName: "GetCatalogHierarchy",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.GetCatalogHierarchyRequest,
  responseType: dlkit_proto_cataloging_pb.GetCatalogHierarchyReply
};
CatalogHierarchyDesignSession.CanModifyCatalogHierarchy = {
  methodName: "CanModifyCatalogHierarchy",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.CanModifyCatalogHierarchyRequest,
  responseType: dlkit_proto_cataloging_pb.CanModifyCatalogHierarchyReply
};
CatalogHierarchyDesignSession.AddRootCatalog = {
  methodName: "AddRootCatalog",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.AddRootCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.AddRootCatalogReply
};
CatalogHierarchyDesignSession.RemoveRootCatalog = {
  methodName: "RemoveRootCatalog",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.RemoveRootCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.RemoveRootCatalogReply
};
CatalogHierarchyDesignSession.AddChildCatalog = {
  methodName: "AddChildCatalog",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.AddChildCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.AddChildCatalogReply
};
CatalogHierarchyDesignSession.RemoveChildCatalog = {
  methodName: "RemoveChildCatalog",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.RemoveChildCatalogRequest,
  responseType: dlkit_proto_cataloging_pb.RemoveChildCatalogReply
};
CatalogHierarchyDesignSession.RemoveChildCatalogs = {
  methodName: "RemoveChildCatalogs",
  service: CatalogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_cataloging_pb.RemoveChildCatalogsRequest,
  responseType: dlkit_proto_cataloging_pb.RemoveChildCatalogsReply
};
module.exports = {
  CatalogLookupSession: CatalogLookupSession,
  CatalogQuerySession: CatalogQuerySession,
  CatalogAdminSession: CatalogAdminSession,
  CatalogHierarchySession: CatalogHierarchySession,
  CatalogHierarchyDesignSession: CatalogHierarchyDesignSession,
};

