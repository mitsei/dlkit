// package: dlkit.proto.cataloging
// file: dlkit/proto/cataloging.proto

import * as dlkit_proto_cataloging_pb from "../../dlkit/proto/cataloging_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
export class CatalogLookupSession {
  static serviceName = "dlkit.proto.cataloging.CatalogLookupSession";
}
export namespace CatalogLookupSession {
  export class CanLookupCatalogs {
    static readonly methodName = "CanLookupCatalogs";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanLookupCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanLookupCatalogsReply;
  }
  export class UseComparativeCatalogView {
    static readonly methodName = "UseComparativeCatalogView";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.UseComparativeCatalogViewRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.UseComparativeCatalogViewReply;
  }
  export class UsePlenaryCatalogView {
    static readonly methodName = "UsePlenaryCatalogView";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.UsePlenaryCatalogViewRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.UsePlenaryCatalogViewReply;
  }
  export class GetCatalog {
    static readonly methodName = "GetCatalog";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogReply;
  }
  export class GetCatalogsByIds {
    static readonly methodName = "GetCatalogsByIds";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsByIdsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class GetCatalogsByGenusType {
    static readonly methodName = "GetCatalogsByGenusType";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class GetCatalogsByParentGenusType {
    static readonly methodName = "GetCatalogsByParentGenusType";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class GetCatalogsByRecordType {
    static readonly methodName = "GetCatalogsByRecordType";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class GetCatalogsByProvider {
    static readonly methodName = "GetCatalogsByProvider";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsByProviderRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class GetCatalogs {
    static readonly methodName = "GetCatalogs";
    static readonly service = CatalogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
}
export class CatalogQuerySession {
  static serviceName = "dlkit.proto.cataloging.CatalogQuerySession";
}
export namespace CatalogQuerySession {
  export class CanSearchCatalogs {
    static readonly methodName = "CanSearchCatalogs";
    static readonly service = CatalogQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanSearchCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanSearchCatalogsReply;
  }
  export class GetCatalogQuery {
    static readonly methodName = "GetCatalogQuery";
    static readonly service = CatalogQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogQueryRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogQueryReply;
  }
  export class GetCatalogsByQuery {
    static readonly methodName = "GetCatalogsByQuery";
    static readonly service = CatalogQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogsByQueryRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
}
export class CatalogAdminSession {
  static serviceName = "dlkit.proto.cataloging.CatalogAdminSession";
}
export namespace CatalogAdminSession {
  export class CanCreateCatalogs {
    static readonly methodName = "CanCreateCatalogs";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanCreateCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanCreateCatalogsReply;
  }
  export class CanCreateCatalogWithRecordTypes {
    static readonly methodName = "CanCreateCatalogWithRecordTypes";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanCreateCatalogWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanCreateCatalogWithRecordTypesReply;
  }
  export class GetCatalogFormForCreate {
    static readonly methodName = "GetCatalogFormForCreate";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogFormForCreateRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogFormForCreateReply;
  }
  export class CreateCatalog {
    static readonly methodName = "CreateCatalog";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CreateCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CreateCatalogReply;
  }
  export class CanUpdateCatalogs {
    static readonly methodName = "CanUpdateCatalogs";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanUpdateCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanUpdateCatalogsReply;
  }
  export class GetCatalogFormForUpdate {
    static readonly methodName = "GetCatalogFormForUpdate";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogFormForUpdateRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogFormForUpdateReply;
  }
  export class UpdateCatalog {
    static readonly methodName = "UpdateCatalog";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.UpdateCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.UpdateCatalogReply;
  }
  export class CanDeleteCatalogs {
    static readonly methodName = "CanDeleteCatalogs";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanDeleteCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanDeleteCatalogsReply;
  }
  export class DeleteCatalog {
    static readonly methodName = "DeleteCatalog";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.DeleteCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.DeleteCatalogReply;
  }
  export class CanManageCatalogAliases {
    static readonly methodName = "CanManageCatalogAliases";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanManageCatalogAliasesRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanManageCatalogAliasesReply;
  }
  export class AliasCatalog {
    static readonly methodName = "AliasCatalog";
    static readonly service = CatalogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.AliasCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.AliasCatalogReply;
  }
}
export class CatalogHierarchySession {
  static serviceName = "dlkit.proto.cataloging.CatalogHierarchySession";
}
export namespace CatalogHierarchySession {
  export class GetCatalogHierarchyId {
    static readonly methodName = "GetCatalogHierarchyId";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogHierarchyIdRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogHierarchyIdReply;
  }
  export class GetCatalogHierarchy {
    static readonly methodName = "GetCatalogHierarchy";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogHierarchyRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogHierarchyReply;
  }
  export class CanAccessCatalogHierarchy {
    static readonly methodName = "CanAccessCatalogHierarchy";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanAccessCatalogHierarchyRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanAccessCatalogHierarchyReply;
  }
  export class UseComparativeCatalogView {
    static readonly methodName = "UseComparativeCatalogView";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.UseComparativeCatalogViewRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.UseComparativeCatalogViewReply;
  }
  export class UsePlenaryCatalogView {
    static readonly methodName = "UsePlenaryCatalogView";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.UsePlenaryCatalogViewRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.UsePlenaryCatalogViewReply;
  }
  export class GetRootCatalogIds {
    static readonly methodName = "GetRootCatalogIds";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetRootCatalogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootCatalogs {
    static readonly methodName = "GetRootCatalogs";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetRootCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class HasParentCatalogs {
    static readonly methodName = "HasParentCatalogs";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.HasParentCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.HasParentCatalogsReply;
  }
  export class IsParentOfCatalog {
    static readonly methodName = "IsParentOfCatalog";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.IsParentOfCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.IsParentOfCatalogReply;
  }
  export class GetParentCatalogIds {
    static readonly methodName = "GetParentCatalogIds";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetParentCatalogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentCatalogs {
    static readonly methodName = "GetParentCatalogs";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetParentCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class IsAncestorOfCatalog {
    static readonly methodName = "IsAncestorOfCatalog";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.IsAncestorOfCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.IsAncestorOfCatalogReply;
  }
  export class HasChildCatalogs {
    static readonly methodName = "HasChildCatalogs";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.HasChildCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.HasChildCatalogsReply;
  }
  export class IsChildOfCatalog {
    static readonly methodName = "IsChildOfCatalog";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.IsChildOfCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.IsChildOfCatalogReply;
  }
  export class GetChildCatalogIds {
    static readonly methodName = "GetChildCatalogIds";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetChildCatalogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildCatalogs {
    static readonly methodName = "GetChildCatalogs";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_cataloging_pb.GetChildCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.Catalog;
  }
  export class IsDescendantOfCatalog {
    static readonly methodName = "IsDescendantOfCatalog";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.IsDescendantOfCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.IsDescendantOfCatalogReply;
  }
  export class GetCatalogNodeIds {
    static readonly methodName = "GetCatalogNodeIds";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogNodeIdsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogNodeIdsReply;
  }
  export class GetCatalogNodes {
    static readonly methodName = "GetCatalogNodes";
    static readonly service = CatalogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogNodesRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogNodesReply;
  }
}
export class CatalogHierarchyDesignSession {
  static serviceName = "dlkit.proto.cataloging.CatalogHierarchyDesignSession";
}
export namespace CatalogHierarchyDesignSession {
  export class GetCatalogHierarchyId {
    static readonly methodName = "GetCatalogHierarchyId";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogHierarchyIdRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogHierarchyIdReply;
  }
  export class GetCatalogHierarchy {
    static readonly methodName = "GetCatalogHierarchy";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.GetCatalogHierarchyRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.GetCatalogHierarchyReply;
  }
  export class CanModifyCatalogHierarchy {
    static readonly methodName = "CanModifyCatalogHierarchy";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.CanModifyCatalogHierarchyRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.CanModifyCatalogHierarchyReply;
  }
  export class AddRootCatalog {
    static readonly methodName = "AddRootCatalog";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.AddRootCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.AddRootCatalogReply;
  }
  export class RemoveRootCatalog {
    static readonly methodName = "RemoveRootCatalog";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.RemoveRootCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.RemoveRootCatalogReply;
  }
  export class AddChildCatalog {
    static readonly methodName = "AddChildCatalog";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.AddChildCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.AddChildCatalogReply;
  }
  export class RemoveChildCatalog {
    static readonly methodName = "RemoveChildCatalog";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.RemoveChildCatalogRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.RemoveChildCatalogReply;
  }
  export class RemoveChildCatalogs {
    static readonly methodName = "RemoveChildCatalogs";
    static readonly service = CatalogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_cataloging_pb.RemoveChildCatalogsRequest;
    static readonly responseType = dlkit_proto_cataloging_pb.RemoveChildCatalogsReply;
  }
}
