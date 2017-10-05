// package: dlkit.proto.cataloging
// file: dlkit/proto/cataloging.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";

export class Catalog extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Catalog.AsObject;
  static toObject(includeInstance: boolean, msg: Catalog): Catalog.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Catalog, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Catalog;
  static deserializeBinaryFromReader(message: Catalog, reader: jspb.BinaryReader): Catalog;
}

export namespace Catalog {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CatalogQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogQuery.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogQuery): CatalogQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogQuery;
  static deserializeBinaryFromReader(message: CatalogQuery, reader: jspb.BinaryReader): CatalogQuery;
}

export namespace CatalogQuery {
  export type AsObject = {
  }
}

export class CatalogQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogQueryInspector): CatalogQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogQueryInspector;
  static deserializeBinaryFromReader(message: CatalogQueryInspector, reader: jspb.BinaryReader): CatalogQueryInspector;
}

export namespace CatalogQueryInspector {
  export type AsObject = {
  }
}

export class CatalogForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogForm.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogForm): CatalogForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogForm;
  static deserializeBinaryFromReader(message: CatalogForm, reader: jspb.BinaryReader): CatalogForm;
}

export namespace CatalogForm {
  export type AsObject = {
  }
}

export class CatalogSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogSearchOrder): CatalogSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogSearchOrder;
  static deserializeBinaryFromReader(message: CatalogSearchOrder, reader: jspb.BinaryReader): CatalogSearchOrder;
}

export namespace CatalogSearchOrder {
  export type AsObject = {
  }
}

export class CatalogSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogSearch.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogSearch): CatalogSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogSearch;
  static deserializeBinaryFromReader(message: CatalogSearch, reader: jspb.BinaryReader): CatalogSearch;
}

export namespace CatalogSearch {
  export type AsObject = {
  }
}

export class CatalogSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogSearchResults): CatalogSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogSearchResults;
  static deserializeBinaryFromReader(message: CatalogSearchResults, reader: jspb.BinaryReader): CatalogSearchResults;
}

export namespace CatalogSearchResults {
  export type AsObject = {
  }
}

export class CatalogList extends jspb.Message {
  clearCatalogsList(): void;
  getCatalogsList(): Array<Catalog>;
  setCatalogsList(value: Array<Catalog>): void;
  addCatalogs(value?: Catalog, index?: number): Catalog;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogList.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogList): CatalogList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogList;
  static deserializeBinaryFromReader(message: CatalogList, reader: jspb.BinaryReader): CatalogList;
}

export namespace CatalogList {
  export type AsObject = {
    catalogsList: Array<Catalog.AsObject>,
  }
}

export class CatalogNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogNode.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogNode): CatalogNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogNode;
  static deserializeBinaryFromReader(message: CatalogNode, reader: jspb.BinaryReader): CatalogNode;
}

export namespace CatalogNode {
  export type AsObject = {
  }
}

export class CatalogNodeList extends jspb.Message {
  clearCatalogNodesList(): void;
  getCatalogNodesList(): Array<CatalogNode>;
  setCatalogNodesList(value: Array<CatalogNode>): void;
  addCatalogNodes(value?: CatalogNode, index?: number): CatalogNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CatalogNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: CatalogNodeList): CatalogNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CatalogNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CatalogNodeList;
  static deserializeBinaryFromReader(message: CatalogNodeList, reader: jspb.BinaryReader): CatalogNodeList;
}

export namespace CatalogNodeList {
  export type AsObject = {
    catalogNodesList: Array<CatalogNode.AsObject>,
  }
}

export class CanLookupCatalogsReply extends jspb.Message {
  getCanLookupCatalogs(): boolean;
  setCanLookupCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCatalogsReply): CanLookupCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCatalogsReply;
  static deserializeBinaryFromReader(message: CanLookupCatalogsReply, reader: jspb.BinaryReader): CanLookupCatalogsReply;
}

export namespace CanLookupCatalogsReply {
  export type AsObject = {
    canLookupCatalogs: boolean,
  }
}

export class CanLookupCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCatalogsRequest): CanLookupCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCatalogsRequest;
  static deserializeBinaryFromReader(message: CanLookupCatalogsRequest, reader: jspb.BinaryReader): CanLookupCatalogsRequest;
}

export namespace CanLookupCatalogsRequest {
  export type AsObject = {
  }
}

export class UseComparativeCatalogViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCatalogViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCatalogViewReply): UseComparativeCatalogViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCatalogViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCatalogViewReply;
  static deserializeBinaryFromReader(message: UseComparativeCatalogViewReply, reader: jspb.BinaryReader): UseComparativeCatalogViewReply;
}

export namespace UseComparativeCatalogViewReply {
  export type AsObject = {
  }
}

export class UseComparativeCatalogViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCatalogViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCatalogViewRequest): UseComparativeCatalogViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCatalogViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCatalogViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeCatalogViewRequest, reader: jspb.BinaryReader): UseComparativeCatalogViewRequest;
}

export namespace UseComparativeCatalogViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryCatalogViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCatalogViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCatalogViewReply): UsePlenaryCatalogViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCatalogViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCatalogViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryCatalogViewReply, reader: jspb.BinaryReader): UsePlenaryCatalogViewReply;
}

export namespace UsePlenaryCatalogViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryCatalogViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCatalogViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCatalogViewRequest): UsePlenaryCatalogViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCatalogViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCatalogViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryCatalogViewRequest, reader: jspb.BinaryReader): UsePlenaryCatalogViewRequest;
}

export namespace UsePlenaryCatalogViewRequest {
  export type AsObject = {
  }
}

export class GetCatalogReply extends jspb.Message {
  hasCatalog(): boolean;
  clearCatalog(): void;
  getCatalog(): Catalog | undefined;
  setCatalog(value?: Catalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogReply): GetCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogReply;
  static deserializeBinaryFromReader(message: GetCatalogReply, reader: jspb.BinaryReader): GetCatalogReply;
}

export namespace GetCatalogReply {
  export type AsObject = {
    catalog?: Catalog.AsObject,
  }
}

export class GetCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogRequest): GetCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogRequest;
  static deserializeBinaryFromReader(message: GetCatalogRequest, reader: jspb.BinaryReader): GetCatalogRequest;
}

export namespace GetCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCatalogsByIdsRequest extends jspb.Message {
  clearCatalogIdsList(): void;
  getCatalogIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setCatalogIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addCatalogIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsByIdsRequest): GetCatalogsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsByIdsRequest;
  static deserializeBinaryFromReader(message: GetCatalogsByIdsRequest, reader: jspb.BinaryReader): GetCatalogsByIdsRequest;
}

export namespace GetCatalogsByIdsRequest {
  export type AsObject = {
    catalogIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetCatalogsByGenusTypeRequest extends jspb.Message {
  hasCatalogGenusType(): boolean;
  clearCatalogGenusType(): void;
  getCatalogGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCatalogGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsByGenusTypeRequest): GetCatalogsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetCatalogsByGenusTypeRequest, reader: jspb.BinaryReader): GetCatalogsByGenusTypeRequest;
}

export namespace GetCatalogsByGenusTypeRequest {
  export type AsObject = {
    catalogGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCatalogsByParentGenusTypeRequest extends jspb.Message {
  hasCatalogGenusType(): boolean;
  clearCatalogGenusType(): void;
  getCatalogGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCatalogGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsByParentGenusTypeRequest): GetCatalogsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetCatalogsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetCatalogsByParentGenusTypeRequest;
}

export namespace GetCatalogsByParentGenusTypeRequest {
  export type AsObject = {
    catalogGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCatalogsByRecordTypeRequest extends jspb.Message {
  hasCatalogRecordType(): boolean;
  clearCatalogRecordType(): void;
  getCatalogRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCatalogRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsByRecordTypeRequest): GetCatalogsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetCatalogsByRecordTypeRequest, reader: jspb.BinaryReader): GetCatalogsByRecordTypeRequest;
}

export namespace GetCatalogsByRecordTypeRequest {
  export type AsObject = {
    catalogRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCatalogsByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsByProviderRequest): GetCatalogsByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsByProviderRequest;
  static deserializeBinaryFromReader(message: GetCatalogsByProviderRequest, reader: jspb.BinaryReader): GetCatalogsByProviderRequest;
}

export namespace GetCatalogsByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsRequest): GetCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsRequest;
  static deserializeBinaryFromReader(message: GetCatalogsRequest, reader: jspb.BinaryReader): GetCatalogsRequest;
}

export namespace GetCatalogsRequest {
  export type AsObject = {
  }
}

export class CanSearchCatalogsReply extends jspb.Message {
  getCanSearchCatalogs(): boolean;
  setCanSearchCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchCatalogsReply): CanSearchCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchCatalogsReply;
  static deserializeBinaryFromReader(message: CanSearchCatalogsReply, reader: jspb.BinaryReader): CanSearchCatalogsReply;
}

export namespace CanSearchCatalogsReply {
  export type AsObject = {
    canSearchCatalogs: boolean,
  }
}

export class CanSearchCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchCatalogsRequest): CanSearchCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchCatalogsRequest;
  static deserializeBinaryFromReader(message: CanSearchCatalogsRequest, reader: jspb.BinaryReader): CanSearchCatalogsRequest;
}

export namespace CanSearchCatalogsRequest {
  export type AsObject = {
  }
}

export class GetCatalogQueryReply extends jspb.Message {
  hasCatalogQuery(): boolean;
  clearCatalogQuery(): void;
  getCatalogQuery(): CatalogQuery | undefined;
  setCatalogQuery(value?: CatalogQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogQueryReply): GetCatalogQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogQueryReply;
  static deserializeBinaryFromReader(message: GetCatalogQueryReply, reader: jspb.BinaryReader): GetCatalogQueryReply;
}

export namespace GetCatalogQueryReply {
  export type AsObject = {
    catalogQuery?: CatalogQuery.AsObject,
  }
}

export class GetCatalogQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogQueryRequest): GetCatalogQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogQueryRequest;
  static deserializeBinaryFromReader(message: GetCatalogQueryRequest, reader: jspb.BinaryReader): GetCatalogQueryRequest;
}

export namespace GetCatalogQueryRequest {
  export type AsObject = {
  }
}

export class GetCatalogsByQueryRequest extends jspb.Message {
  hasCatalogQuery(): boolean;
  clearCatalogQuery(): void;
  getCatalogQuery(): CatalogQuery | undefined;
  setCatalogQuery(value?: CatalogQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogsByQueryRequest): GetCatalogsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogsByQueryRequest;
  static deserializeBinaryFromReader(message: GetCatalogsByQueryRequest, reader: jspb.BinaryReader): GetCatalogsByQueryRequest;
}

export namespace GetCatalogsByQueryRequest {
  export type AsObject = {
    catalogQuery?: CatalogQuery.AsObject,
  }
}

export class CanCreateCatalogsReply extends jspb.Message {
  getCanCreateCatalogs(): boolean;
  setCanCreateCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCatalogsReply): CanCreateCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCatalogsReply;
  static deserializeBinaryFromReader(message: CanCreateCatalogsReply, reader: jspb.BinaryReader): CanCreateCatalogsReply;
}

export namespace CanCreateCatalogsReply {
  export type AsObject = {
    canCreateCatalogs: boolean,
  }
}

export class CanCreateCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCatalogsRequest): CanCreateCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCatalogsRequest;
  static deserializeBinaryFromReader(message: CanCreateCatalogsRequest, reader: jspb.BinaryReader): CanCreateCatalogsRequest;
}

export namespace CanCreateCatalogsRequest {
  export type AsObject = {
  }
}

export class CanCreateCatalogWithRecordTypesReply extends jspb.Message {
  getCanCreateCatalogWithRecordTypes(): boolean;
  setCanCreateCatalogWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCatalogWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCatalogWithRecordTypesReply): CanCreateCatalogWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCatalogWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCatalogWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateCatalogWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateCatalogWithRecordTypesReply;
}

export namespace CanCreateCatalogWithRecordTypesReply {
  export type AsObject = {
    canCreateCatalogWithRecordTypes: boolean,
  }
}

export class CanCreateCatalogWithRecordTypesRequest extends jspb.Message {
  clearCatalogRecordTypesList(): void;
  getCatalogRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setCatalogRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addCatalogRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCatalogWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCatalogWithRecordTypesRequest): CanCreateCatalogWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCatalogWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCatalogWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateCatalogWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateCatalogWithRecordTypesRequest;
}

export namespace CanCreateCatalogWithRecordTypesRequest {
  export type AsObject = {
    catalogRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetCatalogFormForCreateReply extends jspb.Message {
  hasCatalogForm(): boolean;
  clearCatalogForm(): void;
  getCatalogForm(): CatalogForm | undefined;
  setCatalogForm(value?: CatalogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogFormForCreateReply): GetCatalogFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogFormForCreateReply;
  static deserializeBinaryFromReader(message: GetCatalogFormForCreateReply, reader: jspb.BinaryReader): GetCatalogFormForCreateReply;
}

export namespace GetCatalogFormForCreateReply {
  export type AsObject = {
    catalogForm?: CatalogForm.AsObject,
  }
}

export class GetCatalogFormForCreateRequest extends jspb.Message {
  clearCatalogRecordTypesList(): void;
  getCatalogRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setCatalogRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addCatalogRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogFormForCreateRequest): GetCatalogFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetCatalogFormForCreateRequest, reader: jspb.BinaryReader): GetCatalogFormForCreateRequest;
}

export namespace GetCatalogFormForCreateRequest {
  export type AsObject = {
    catalogRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateCatalogReply extends jspb.Message {
  hasCatalog(): boolean;
  clearCatalog(): void;
  getCatalog(): Catalog | undefined;
  setCatalog(value?: Catalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateCatalogReply): CreateCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateCatalogReply;
  static deserializeBinaryFromReader(message: CreateCatalogReply, reader: jspb.BinaryReader): CreateCatalogReply;
}

export namespace CreateCatalogReply {
  export type AsObject = {
    catalog?: Catalog.AsObject,
  }
}

export class CreateCatalogRequest extends jspb.Message {
  hasCatalogForm(): boolean;
  clearCatalogForm(): void;
  getCatalogForm(): CatalogForm | undefined;
  setCatalogForm(value?: CatalogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateCatalogRequest): CreateCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateCatalogRequest;
  static deserializeBinaryFromReader(message: CreateCatalogRequest, reader: jspb.BinaryReader): CreateCatalogRequest;
}

export namespace CreateCatalogRequest {
  export type AsObject = {
    catalogForm?: CatalogForm.AsObject,
  }
}

export class CanUpdateCatalogsReply extends jspb.Message {
  getCanUpdateCatalogs(): boolean;
  setCanUpdateCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateCatalogsReply): CanUpdateCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateCatalogsReply;
  static deserializeBinaryFromReader(message: CanUpdateCatalogsReply, reader: jspb.BinaryReader): CanUpdateCatalogsReply;
}

export namespace CanUpdateCatalogsReply {
  export type AsObject = {
    canUpdateCatalogs: boolean,
  }
}

export class CanUpdateCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateCatalogsRequest): CanUpdateCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateCatalogsRequest;
  static deserializeBinaryFromReader(message: CanUpdateCatalogsRequest, reader: jspb.BinaryReader): CanUpdateCatalogsRequest;
}

export namespace CanUpdateCatalogsRequest {
  export type AsObject = {
  }
}

export class GetCatalogFormForUpdateReply extends jspb.Message {
  hasCatalogForm(): boolean;
  clearCatalogForm(): void;
  getCatalogForm(): CatalogForm | undefined;
  setCatalogForm(value?: CatalogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogFormForUpdateReply): GetCatalogFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetCatalogFormForUpdateReply, reader: jspb.BinaryReader): GetCatalogFormForUpdateReply;
}

export namespace GetCatalogFormForUpdateReply {
  export type AsObject = {
    catalogForm?: CatalogForm.AsObject,
  }
}

export class GetCatalogFormForUpdateRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogFormForUpdateRequest): GetCatalogFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetCatalogFormForUpdateRequest, reader: jspb.BinaryReader): GetCatalogFormForUpdateRequest;
}

export namespace GetCatalogFormForUpdateRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateCatalogReply): UpdateCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateCatalogReply;
  static deserializeBinaryFromReader(message: UpdateCatalogReply, reader: jspb.BinaryReader): UpdateCatalogReply;
}

export namespace UpdateCatalogReply {
  export type AsObject = {
  }
}

export class UpdateCatalogRequest extends jspb.Message {
  hasCatalogForm(): boolean;
  clearCatalogForm(): void;
  getCatalogForm(): CatalogForm | undefined;
  setCatalogForm(value?: CatalogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateCatalogRequest): UpdateCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateCatalogRequest;
  static deserializeBinaryFromReader(message: UpdateCatalogRequest, reader: jspb.BinaryReader): UpdateCatalogRequest;
}

export namespace UpdateCatalogRequest {
  export type AsObject = {
    catalogForm?: CatalogForm.AsObject,
  }
}

export class CanDeleteCatalogsReply extends jspb.Message {
  getCanDeleteCatalogs(): boolean;
  setCanDeleteCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteCatalogsReply): CanDeleteCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteCatalogsReply;
  static deserializeBinaryFromReader(message: CanDeleteCatalogsReply, reader: jspb.BinaryReader): CanDeleteCatalogsReply;
}

export namespace CanDeleteCatalogsReply {
  export type AsObject = {
    canDeleteCatalogs: boolean,
  }
}

export class CanDeleteCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteCatalogsRequest): CanDeleteCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteCatalogsRequest;
  static deserializeBinaryFromReader(message: CanDeleteCatalogsRequest, reader: jspb.BinaryReader): CanDeleteCatalogsRequest;
}

export namespace CanDeleteCatalogsRequest {
  export type AsObject = {
  }
}

export class DeleteCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCatalogReply): DeleteCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCatalogReply;
  static deserializeBinaryFromReader(message: DeleteCatalogReply, reader: jspb.BinaryReader): DeleteCatalogReply;
}

export namespace DeleteCatalogReply {
  export type AsObject = {
  }
}

export class DeleteCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCatalogRequest): DeleteCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCatalogRequest;
  static deserializeBinaryFromReader(message: DeleteCatalogRequest, reader: jspb.BinaryReader): DeleteCatalogRequest;
}

export namespace DeleteCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageCatalogAliasesReply extends jspb.Message {
  getCanManageCatalogAliases(): boolean;
  setCanManageCatalogAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageCatalogAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageCatalogAliasesReply): CanManageCatalogAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageCatalogAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageCatalogAliasesReply;
  static deserializeBinaryFromReader(message: CanManageCatalogAliasesReply, reader: jspb.BinaryReader): CanManageCatalogAliasesReply;
}

export namespace CanManageCatalogAliasesReply {
  export type AsObject = {
    canManageCatalogAliases: boolean,
  }
}

export class CanManageCatalogAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageCatalogAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageCatalogAliasesRequest): CanManageCatalogAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageCatalogAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageCatalogAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageCatalogAliasesRequest, reader: jspb.BinaryReader): CanManageCatalogAliasesRequest;
}

export namespace CanManageCatalogAliasesRequest {
  export type AsObject = {
  }
}

export class AliasCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasCatalogReply): AliasCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasCatalogReply;
  static deserializeBinaryFromReader(message: AliasCatalogReply, reader: jspb.BinaryReader): AliasCatalogReply;
}

export namespace AliasCatalogReply {
  export type AsObject = {
  }
}

export class AliasCatalogRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasCatalogRequest): AliasCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasCatalogRequest;
  static deserializeBinaryFromReader(message: AliasCatalogRequest, reader: jspb.BinaryReader): AliasCatalogRequest;
}

export namespace AliasCatalogRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCatalogHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogHierarchyIdReply): GetCatalogHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetCatalogHierarchyIdReply, reader: jspb.BinaryReader): GetCatalogHierarchyIdReply;
}

export namespace GetCatalogHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCatalogHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogHierarchyIdRequest): GetCatalogHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetCatalogHierarchyIdRequest, reader: jspb.BinaryReader): GetCatalogHierarchyIdRequest;
}

export namespace GetCatalogHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetCatalogHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogHierarchyReply): GetCatalogHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogHierarchyReply;
  static deserializeBinaryFromReader(message: GetCatalogHierarchyReply, reader: jspb.BinaryReader): GetCatalogHierarchyReply;
}

export namespace GetCatalogHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetCatalogHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogHierarchyRequest): GetCatalogHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogHierarchyRequest;
  static deserializeBinaryFromReader(message: GetCatalogHierarchyRequest, reader: jspb.BinaryReader): GetCatalogHierarchyRequest;
}

export namespace GetCatalogHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessCatalogHierarchyReply extends jspb.Message {
  getCanAccessCatalogHierarchy(): boolean;
  setCanAccessCatalogHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessCatalogHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessCatalogHierarchyReply): CanAccessCatalogHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessCatalogHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessCatalogHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessCatalogHierarchyReply, reader: jspb.BinaryReader): CanAccessCatalogHierarchyReply;
}

export namespace CanAccessCatalogHierarchyReply {
  export type AsObject = {
    canAccessCatalogHierarchy: boolean,
  }
}

export class CanAccessCatalogHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessCatalogHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessCatalogHierarchyRequest): CanAccessCatalogHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessCatalogHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessCatalogHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessCatalogHierarchyRequest, reader: jspb.BinaryReader): CanAccessCatalogHierarchyRequest;
}

export namespace CanAccessCatalogHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootCatalogIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootCatalogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootCatalogIdsRequest): GetRootCatalogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootCatalogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootCatalogIdsRequest;
  static deserializeBinaryFromReader(message: GetRootCatalogIdsRequest, reader: jspb.BinaryReader): GetRootCatalogIdsRequest;
}

export namespace GetRootCatalogIdsRequest {
  export type AsObject = {
  }
}

export class GetRootCatalogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootCatalogsRequest): GetRootCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootCatalogsRequest;
  static deserializeBinaryFromReader(message: GetRootCatalogsRequest, reader: jspb.BinaryReader): GetRootCatalogsRequest;
}

export namespace GetRootCatalogsRequest {
  export type AsObject = {
  }
}

export class HasParentCatalogsReply extends jspb.Message {
  getHasParentCatalogs(): boolean;
  setHasParentCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentCatalogsReply): HasParentCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentCatalogsReply;
  static deserializeBinaryFromReader(message: HasParentCatalogsReply, reader: jspb.BinaryReader): HasParentCatalogsReply;
}

export namespace HasParentCatalogsReply {
  export type AsObject = {
    hasParentCatalogs: boolean,
  }
}

export class HasParentCatalogsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentCatalogsRequest): HasParentCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentCatalogsRequest;
  static deserializeBinaryFromReader(message: HasParentCatalogsRequest, reader: jspb.BinaryReader): HasParentCatalogsRequest;
}

export namespace HasParentCatalogsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfCatalogReply extends jspb.Message {
  getIsParentOfCatalog(): boolean;
  setIsParentOfCatalog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfCatalogReply): IsParentOfCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfCatalogReply;
  static deserializeBinaryFromReader(message: IsParentOfCatalogReply, reader: jspb.BinaryReader): IsParentOfCatalogReply;
}

export namespace IsParentOfCatalogReply {
  export type AsObject = {
    isParentOfCatalog: boolean,
  }
}

export class IsParentOfCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfCatalogRequest): IsParentOfCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfCatalogRequest;
  static deserializeBinaryFromReader(message: IsParentOfCatalogRequest, reader: jspb.BinaryReader): IsParentOfCatalogRequest;
}

export namespace IsParentOfCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentCatalogIdsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentCatalogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentCatalogIdsRequest): GetParentCatalogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentCatalogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentCatalogIdsRequest;
  static deserializeBinaryFromReader(message: GetParentCatalogIdsRequest, reader: jspb.BinaryReader): GetParentCatalogIdsRequest;
}

export namespace GetParentCatalogIdsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentCatalogsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentCatalogsRequest): GetParentCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentCatalogsRequest;
  static deserializeBinaryFromReader(message: GetParentCatalogsRequest, reader: jspb.BinaryReader): GetParentCatalogsRequest;
}

export namespace GetParentCatalogsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfCatalogReply extends jspb.Message {
  getIsAncestorOfCatalog(): boolean;
  setIsAncestorOfCatalog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfCatalogReply): IsAncestorOfCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfCatalogReply;
  static deserializeBinaryFromReader(message: IsAncestorOfCatalogReply, reader: jspb.BinaryReader): IsAncestorOfCatalogReply;
}

export namespace IsAncestorOfCatalogReply {
  export type AsObject = {
    isAncestorOfCatalog: boolean,
  }
}

export class IsAncestorOfCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfCatalogRequest): IsAncestorOfCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfCatalogRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfCatalogRequest, reader: jspb.BinaryReader): IsAncestorOfCatalogRequest;
}

export namespace IsAncestorOfCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildCatalogsReply extends jspb.Message {
  getHasChildCatalogs(): boolean;
  setHasChildCatalogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildCatalogsReply): HasChildCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildCatalogsReply;
  static deserializeBinaryFromReader(message: HasChildCatalogsReply, reader: jspb.BinaryReader): HasChildCatalogsReply;
}

export namespace HasChildCatalogsReply {
  export type AsObject = {
    hasChildCatalogs: boolean,
  }
}

export class HasChildCatalogsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildCatalogsRequest): HasChildCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildCatalogsRequest;
  static deserializeBinaryFromReader(message: HasChildCatalogsRequest, reader: jspb.BinaryReader): HasChildCatalogsRequest;
}

export namespace HasChildCatalogsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfCatalogReply extends jspb.Message {
  getIsChildOfCatalog(): boolean;
  setIsChildOfCatalog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfCatalogReply): IsChildOfCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfCatalogReply;
  static deserializeBinaryFromReader(message: IsChildOfCatalogReply, reader: jspb.BinaryReader): IsChildOfCatalogReply;
}

export namespace IsChildOfCatalogReply {
  export type AsObject = {
    isChildOfCatalog: boolean,
  }
}

export class IsChildOfCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfCatalogRequest): IsChildOfCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfCatalogRequest;
  static deserializeBinaryFromReader(message: IsChildOfCatalogRequest, reader: jspb.BinaryReader): IsChildOfCatalogRequest;
}

export namespace IsChildOfCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildCatalogIdsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildCatalogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildCatalogIdsRequest): GetChildCatalogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildCatalogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildCatalogIdsRequest;
  static deserializeBinaryFromReader(message: GetChildCatalogIdsRequest, reader: jspb.BinaryReader): GetChildCatalogIdsRequest;
}

export namespace GetChildCatalogIdsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildCatalogsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildCatalogsRequest): GetChildCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildCatalogsRequest;
  static deserializeBinaryFromReader(message: GetChildCatalogsRequest, reader: jspb.BinaryReader): GetChildCatalogsRequest;
}

export namespace GetChildCatalogsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfCatalogReply extends jspb.Message {
  getIsDescendantOfCatalog(): boolean;
  setIsDescendantOfCatalog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfCatalogReply): IsDescendantOfCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfCatalogReply;
  static deserializeBinaryFromReader(message: IsDescendantOfCatalogReply, reader: jspb.BinaryReader): IsDescendantOfCatalogReply;
}

export namespace IsDescendantOfCatalogReply {
  export type AsObject = {
    isDescendantOfCatalog: boolean,
  }
}

export class IsDescendantOfCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfCatalogRequest): IsDescendantOfCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfCatalogRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfCatalogRequest, reader: jspb.BinaryReader): IsDescendantOfCatalogRequest;
}

export namespace IsDescendantOfCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCatalogNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogNodeIdsReply): GetCatalogNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogNodeIdsReply;
  static deserializeBinaryFromReader(message: GetCatalogNodeIdsReply, reader: jspb.BinaryReader): GetCatalogNodeIdsReply;
}

export namespace GetCatalogNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetCatalogNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogNodeIdsRequest): GetCatalogNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetCatalogNodeIdsRequest, reader: jspb.BinaryReader): GetCatalogNodeIdsRequest;
}

export namespace GetCatalogNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class GetCatalogNodesReply extends jspb.Message {
  hasCatalogNode(): boolean;
  clearCatalogNode(): void;
  getCatalogNode(): CatalogNode | undefined;
  setCatalogNode(value?: CatalogNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogNodesReply): GetCatalogNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogNodesReply;
  static deserializeBinaryFromReader(message: GetCatalogNodesReply, reader: jspb.BinaryReader): GetCatalogNodesReply;
}

export namespace GetCatalogNodesReply {
  export type AsObject = {
    catalogNode?: CatalogNode.AsObject,
  }
}

export class GetCatalogNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCatalogNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCatalogNodesRequest): GetCatalogNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCatalogNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCatalogNodesRequest;
  static deserializeBinaryFromReader(message: GetCatalogNodesRequest, reader: jspb.BinaryReader): GetCatalogNodesRequest;
}

export namespace GetCatalogNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class CanModifyCatalogHierarchyReply extends jspb.Message {
  getCanModifyCatalogHierarchy(): boolean;
  setCanModifyCatalogHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyCatalogHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyCatalogHierarchyReply): CanModifyCatalogHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyCatalogHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyCatalogHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyCatalogHierarchyReply, reader: jspb.BinaryReader): CanModifyCatalogHierarchyReply;
}

export namespace CanModifyCatalogHierarchyReply {
  export type AsObject = {
    canModifyCatalogHierarchy: boolean,
  }
}

export class CanModifyCatalogHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyCatalogHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyCatalogHierarchyRequest): CanModifyCatalogHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyCatalogHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyCatalogHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyCatalogHierarchyRequest, reader: jspb.BinaryReader): CanModifyCatalogHierarchyRequest;
}

export namespace CanModifyCatalogHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootCatalogReply): AddRootCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootCatalogReply;
  static deserializeBinaryFromReader(message: AddRootCatalogReply, reader: jspb.BinaryReader): AddRootCatalogReply;
}

export namespace AddRootCatalogReply {
  export type AsObject = {
  }
}

export class AddRootCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootCatalogRequest): AddRootCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootCatalogRequest;
  static deserializeBinaryFromReader(message: AddRootCatalogRequest, reader: jspb.BinaryReader): AddRootCatalogRequest;
}

export namespace AddRootCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootCatalogReply): RemoveRootCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootCatalogReply;
  static deserializeBinaryFromReader(message: RemoveRootCatalogReply, reader: jspb.BinaryReader): RemoveRootCatalogReply;
}

export namespace RemoveRootCatalogReply {
  export type AsObject = {
  }
}

export class RemoveRootCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootCatalogRequest): RemoveRootCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootCatalogRequest;
  static deserializeBinaryFromReader(message: RemoveRootCatalogRequest, reader: jspb.BinaryReader): RemoveRootCatalogRequest;
}

export namespace RemoveRootCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildCatalogReply): AddChildCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildCatalogReply;
  static deserializeBinaryFromReader(message: AddChildCatalogReply, reader: jspb.BinaryReader): AddChildCatalogReply;
}

export namespace AddChildCatalogReply {
  export type AsObject = {
  }
}

export class AddChildCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildCatalogRequest): AddChildCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildCatalogRequest;
  static deserializeBinaryFromReader(message: AddChildCatalogRequest, reader: jspb.BinaryReader): AddChildCatalogRequest;
}

export namespace AddChildCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildCatalogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildCatalogReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildCatalogReply): RemoveChildCatalogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildCatalogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildCatalogReply;
  static deserializeBinaryFromReader(message: RemoveChildCatalogReply, reader: jspb.BinaryReader): RemoveChildCatalogReply;
}

export namespace RemoveChildCatalogReply {
  export type AsObject = {
  }
}

export class RemoveChildCatalogRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildCatalogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildCatalogRequest): RemoveChildCatalogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildCatalogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildCatalogRequest;
  static deserializeBinaryFromReader(message: RemoveChildCatalogRequest, reader: jspb.BinaryReader): RemoveChildCatalogRequest;
}

export namespace RemoveChildCatalogRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildCatalogsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildCatalogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildCatalogsReply): RemoveChildCatalogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildCatalogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildCatalogsReply;
  static deserializeBinaryFromReader(message: RemoveChildCatalogsReply, reader: jspb.BinaryReader): RemoveChildCatalogsReply;
}

export namespace RemoveChildCatalogsReply {
  export type AsObject = {
  }
}

export class RemoveChildCatalogsRequest extends jspb.Message {
  hasCatalogId(): boolean;
  clearCatalogId(): void;
  getCatalogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCatalogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildCatalogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildCatalogsRequest): RemoveChildCatalogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildCatalogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildCatalogsRequest;
  static deserializeBinaryFromReader(message: RemoveChildCatalogsRequest, reader: jspb.BinaryReader): RemoveChildCatalogsRequest;
}

export namespace RemoveChildCatalogsRequest {
  export type AsObject = {
    catalogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

