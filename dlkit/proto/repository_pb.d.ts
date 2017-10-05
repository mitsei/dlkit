// package: dlkit.proto.repository
// file: dlkit/proto/repository.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_transport_objects_pb from "../../dlkit/primordium/transport/objects_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Asset extends jspb.Message {
  clearAssetContentsList(): void;
  getAssetContentsList(): Array<AssetContent>;
  setAssetContentsList(value: Array<AssetContent>): void;
  addAssetContents(value?: AssetContent, index?: number): AssetContent;

  hasComposition(): boolean;
  clearComposition(): void;
  getComposition(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setComposition(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getCopyright(): string;
  setCopyright(value: string): void;

  getCopyrightRegistration(): string;
  setCopyrightRegistration(value: string): void;

  hasCreatedDate(): boolean;
  clearCreatedDate(): void;
  getCreatedDate(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCreatedDate(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  getDistributeAlterations(): boolean;
  setDistributeAlterations(value: boolean): void;

  getDistributeCompositions(): boolean;
  setDistributeCompositions(value: boolean): void;

  getDistributeVerbatim(): boolean;
  setDistributeVerbatim(value: boolean): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getPrincipalCreditString(): string;
  setPrincipalCreditString(value: string): void;

  clearProviderLinksList(): void;
  getProviderLinksList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setProviderLinksList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addProviderLinks(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  getPublicDomain(): boolean;
  setPublicDomain(value: boolean): void;

  getPublished(): boolean;
  setPublished(value: boolean): void;

  hasPublishedDate(): boolean;
  clearPublishedDate(): void;
  getPublishedDate(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setPublishedDate(value?: google_protobuf_timestamp_pb.Timestamp): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasRepository(): boolean;
  clearRepository(): void;
  getRepository(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setRepository(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasSource(): boolean;
  clearSource(): void;
  getSource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getTitle(): string;
  setTitle(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Asset.AsObject;
  static toObject(includeInstance: boolean, msg: Asset): Asset.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Asset, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Asset;
  static deserializeBinaryFromReader(message: Asset, reader: jspb.BinaryReader): Asset;
}

export namespace Asset {
  export type AsObject = {
    assetContentsList: Array<AssetContent.AsObject>,
    composition?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    copyright: string,
    copyrightRegistration: string,
    createdDate?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    distributeAlterations: boolean,
    distributeCompositions: boolean,
    distributeVerbatim: boolean,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    principalCreditString: string,
    providerLinksList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    publicDomain: boolean,
    published: boolean,
    publishedDate?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    repository?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    source?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    title: string,
  }
}

export class AssetQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AssetQuery): AssetQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetQuery;
  static deserializeBinaryFromReader(message: AssetQuery, reader: jspb.BinaryReader): AssetQuery;
}

export namespace AssetQuery {
  export type AsObject = {
  }
}

export class AssetQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AssetQueryInspector): AssetQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetQueryInspector;
  static deserializeBinaryFromReader(message: AssetQueryInspector, reader: jspb.BinaryReader): AssetQueryInspector;
}

export namespace AssetQueryInspector {
  export type AsObject = {
  }
}

export class AssetForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetForm.AsObject;
  static toObject(includeInstance: boolean, msg: AssetForm): AssetForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetForm;
  static deserializeBinaryFromReader(message: AssetForm, reader: jspb.BinaryReader): AssetForm;
}

export namespace AssetForm {
  export type AsObject = {
  }
}

export class AssetSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AssetSearchOrder): AssetSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetSearchOrder;
  static deserializeBinaryFromReader(message: AssetSearchOrder, reader: jspb.BinaryReader): AssetSearchOrder;
}

export namespace AssetSearchOrder {
  export type AsObject = {
  }
}

export class AssetSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AssetSearch): AssetSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetSearch;
  static deserializeBinaryFromReader(message: AssetSearch, reader: jspb.BinaryReader): AssetSearch;
}

export namespace AssetSearch {
  export type AsObject = {
  }
}

export class AssetSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AssetSearchResults): AssetSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetSearchResults;
  static deserializeBinaryFromReader(message: AssetSearchResults, reader: jspb.BinaryReader): AssetSearchResults;
}

export namespace AssetSearchResults {
  export type AsObject = {
  }
}

export class AssetList extends jspb.Message {
  clearAssetsList(): void;
  getAssetsList(): Array<Asset>;
  setAssetsList(value: Array<Asset>): void;
  addAssets(value?: Asset, index?: number): Asset;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetList.AsObject;
  static toObject(includeInstance: boolean, msg: AssetList): AssetList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetList;
  static deserializeBinaryFromReader(message: AssetList, reader: jspb.BinaryReader): AssetList;
}

export namespace AssetList {
  export type AsObject = {
    assetsList: Array<Asset.AsObject>,
  }
}

export class AssetContent extends jspb.Message {
  hasAccessibilityType(): boolean;
  clearAccessibilityType(): void;
  getAccessibilityType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAccessibilityType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasAsset(): boolean;
  clearAsset(): void;
  getAsset(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAsset(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasData(): boolean;
  clearData(): void;
  getData(): dlkit_primordium_transport_objects_pb.DataInputStream | undefined;
  setData(value?: dlkit_primordium_transport_objects_pb.DataInputStream): void;

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

  hasRepository(): boolean;
  clearRepository(): void;
  getRepository(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setRepository(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  getUrl(): string;
  setUrl(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetContent.AsObject;
  static toObject(includeInstance: boolean, msg: AssetContent): AssetContent.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetContent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetContent;
  static deserializeBinaryFromReader(message: AssetContent, reader: jspb.BinaryReader): AssetContent;
}

export namespace AssetContent {
  export type AsObject = {
    accessibilityType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    asset?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    data?: dlkit_primordium_transport_objects_pb.DataInputStream.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    repository?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    url: string,
  }
}

export class AssetContentQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetContentQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AssetContentQuery): AssetContentQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetContentQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetContentQuery;
  static deserializeBinaryFromReader(message: AssetContentQuery, reader: jspb.BinaryReader): AssetContentQuery;
}

export namespace AssetContentQuery {
  export type AsObject = {
  }
}

export class AssetContentQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetContentQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AssetContentQueryInspector): AssetContentQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetContentQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetContentQueryInspector;
  static deserializeBinaryFromReader(message: AssetContentQueryInspector, reader: jspb.BinaryReader): AssetContentQueryInspector;
}

export namespace AssetContentQueryInspector {
  export type AsObject = {
  }
}

export class AssetContentForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetContentForm.AsObject;
  static toObject(includeInstance: boolean, msg: AssetContentForm): AssetContentForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetContentForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetContentForm;
  static deserializeBinaryFromReader(message: AssetContentForm, reader: jspb.BinaryReader): AssetContentForm;
}

export namespace AssetContentForm {
  export type AsObject = {
  }
}

export class AssetContentList extends jspb.Message {
  clearAssetContentsList(): void;
  getAssetContentsList(): Array<AssetContent>;
  setAssetContentsList(value: Array<AssetContent>): void;
  addAssetContents(value?: AssetContent, index?: number): AssetContent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetContentList.AsObject;
  static toObject(includeInstance: boolean, msg: AssetContentList): AssetContentList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetContentList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetContentList;
  static deserializeBinaryFromReader(message: AssetContentList, reader: jspb.BinaryReader): AssetContentList;
}

export namespace AssetContentList {
  export type AsObject = {
    assetContentsList: Array<AssetContent.AsObject>,
  }
}

export class Composition extends jspb.Message {
  clearChildrenList(): void;
  getChildrenList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setChildrenList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addChildren(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

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

  hasRepository(): boolean;
  clearRepository(): void;
  getRepository(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setRepository(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Composition.AsObject;
  static toObject(includeInstance: boolean, msg: Composition): Composition.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Composition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Composition;
  static deserializeBinaryFromReader(message: Composition, reader: jspb.BinaryReader): Composition;
}

export namespace Composition {
  export type AsObject = {
    childrenList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    repository?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
  }
}

export class CompositionQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionQuery.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionQuery): CompositionQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionQuery;
  static deserializeBinaryFromReader(message: CompositionQuery, reader: jspb.BinaryReader): CompositionQuery;
}

export namespace CompositionQuery {
  export type AsObject = {
  }
}

export class CompositionQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionQueryInspector): CompositionQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionQueryInspector;
  static deserializeBinaryFromReader(message: CompositionQueryInspector, reader: jspb.BinaryReader): CompositionQueryInspector;
}

export namespace CompositionQueryInspector {
  export type AsObject = {
  }
}

export class CompositionForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionForm.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionForm): CompositionForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionForm;
  static deserializeBinaryFromReader(message: CompositionForm, reader: jspb.BinaryReader): CompositionForm;
}

export namespace CompositionForm {
  export type AsObject = {
  }
}

export class CompositionSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionSearchOrder): CompositionSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionSearchOrder;
  static deserializeBinaryFromReader(message: CompositionSearchOrder, reader: jspb.BinaryReader): CompositionSearchOrder;
}

export namespace CompositionSearchOrder {
  export type AsObject = {
  }
}

export class CompositionSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionSearch.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionSearch): CompositionSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionSearch;
  static deserializeBinaryFromReader(message: CompositionSearch, reader: jspb.BinaryReader): CompositionSearch;
}

export namespace CompositionSearch {
  export type AsObject = {
  }
}

export class CompositionSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionSearchResults): CompositionSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionSearchResults;
  static deserializeBinaryFromReader(message: CompositionSearchResults, reader: jspb.BinaryReader): CompositionSearchResults;
}

export namespace CompositionSearchResults {
  export type AsObject = {
  }
}

export class CompositionList extends jspb.Message {
  clearCompositionsList(): void;
  getCompositionsList(): Array<Composition>;
  setCompositionsList(value: Array<Composition>): void;
  addCompositions(value?: Composition, index?: number): Composition;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CompositionList.AsObject;
  static toObject(includeInstance: boolean, msg: CompositionList): CompositionList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CompositionList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CompositionList;
  static deserializeBinaryFromReader(message: CompositionList, reader: jspb.BinaryReader): CompositionList;
}

export namespace CompositionList {
  export type AsObject = {
    compositionsList: Array<Composition.AsObject>,
  }
}

export class Repository extends jspb.Message {
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
  toObject(includeInstance?: boolean): Repository.AsObject;
  static toObject(includeInstance: boolean, msg: Repository): Repository.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Repository, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Repository;
  static deserializeBinaryFromReader(message: Repository, reader: jspb.BinaryReader): Repository;
}

export namespace Repository {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class RepositoryQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositoryQuery.AsObject;
  static toObject(includeInstance: boolean, msg: RepositoryQuery): RepositoryQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositoryQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositoryQuery;
  static deserializeBinaryFromReader(message: RepositoryQuery, reader: jspb.BinaryReader): RepositoryQuery;
}

export namespace RepositoryQuery {
  export type AsObject = {
  }
}

export class RepositoryQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositoryQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: RepositoryQueryInspector): RepositoryQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositoryQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositoryQueryInspector;
  static deserializeBinaryFromReader(message: RepositoryQueryInspector, reader: jspb.BinaryReader): RepositoryQueryInspector;
}

export namespace RepositoryQueryInspector {
  export type AsObject = {
  }
}

export class RepositoryForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositoryForm.AsObject;
  static toObject(includeInstance: boolean, msg: RepositoryForm): RepositoryForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositoryForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositoryForm;
  static deserializeBinaryFromReader(message: RepositoryForm, reader: jspb.BinaryReader): RepositoryForm;
}

export namespace RepositoryForm {
  export type AsObject = {
  }
}

export class RepositorySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositorySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: RepositorySearchOrder): RepositorySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositorySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositorySearchOrder;
  static deserializeBinaryFromReader(message: RepositorySearchOrder, reader: jspb.BinaryReader): RepositorySearchOrder;
}

export namespace RepositorySearchOrder {
  export type AsObject = {
  }
}

export class RepositorySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositorySearch.AsObject;
  static toObject(includeInstance: boolean, msg: RepositorySearch): RepositorySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositorySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositorySearch;
  static deserializeBinaryFromReader(message: RepositorySearch, reader: jspb.BinaryReader): RepositorySearch;
}

export namespace RepositorySearch {
  export type AsObject = {
  }
}

export class RepositorySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositorySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: RepositorySearchResults): RepositorySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositorySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositorySearchResults;
  static deserializeBinaryFromReader(message: RepositorySearchResults, reader: jspb.BinaryReader): RepositorySearchResults;
}

export namespace RepositorySearchResults {
  export type AsObject = {
  }
}

export class RepositoryList extends jspb.Message {
  clearRepositoriesList(): void;
  getRepositoriesList(): Array<Repository>;
  setRepositoriesList(value: Array<Repository>): void;
  addRepositories(value?: Repository, index?: number): Repository;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositoryList.AsObject;
  static toObject(includeInstance: boolean, msg: RepositoryList): RepositoryList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositoryList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositoryList;
  static deserializeBinaryFromReader(message: RepositoryList, reader: jspb.BinaryReader): RepositoryList;
}

export namespace RepositoryList {
  export type AsObject = {
    repositoriesList: Array<Repository.AsObject>,
  }
}

export class RepositoryNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositoryNode.AsObject;
  static toObject(includeInstance: boolean, msg: RepositoryNode): RepositoryNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositoryNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositoryNode;
  static deserializeBinaryFromReader(message: RepositoryNode, reader: jspb.BinaryReader): RepositoryNode;
}

export namespace RepositoryNode {
  export type AsObject = {
  }
}

export class RepositoryNodeList extends jspb.Message {
  clearRepositoryNodesList(): void;
  getRepositoryNodesList(): Array<RepositoryNode>;
  setRepositoryNodesList(value: Array<RepositoryNode>): void;
  addRepositoryNodes(value?: RepositoryNode, index?: number): RepositoryNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RepositoryNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: RepositoryNodeList): RepositoryNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RepositoryNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RepositoryNodeList;
  static deserializeBinaryFromReader(message: RepositoryNodeList, reader: jspb.BinaryReader): RepositoryNodeList;
}

export namespace RepositoryNodeList {
  export type AsObject = {
    repositoryNodesList: Array<RepositoryNode.AsObject>,
  }
}

export class GetRepositoryIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryIdReply): GetRepositoryIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryIdReply;
  static deserializeBinaryFromReader(message: GetRepositoryIdReply, reader: jspb.BinaryReader): GetRepositoryIdReply;
}

export namespace GetRepositoryIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoryIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryIdRequest): GetRepositoryIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryIdRequest;
  static deserializeBinaryFromReader(message: GetRepositoryIdRequest, reader: jspb.BinaryReader): GetRepositoryIdRequest;
}

export namespace GetRepositoryIdRequest {
  export type AsObject = {
  }
}

export class GetRepositoryReply extends jspb.Message {
  hasRepository(): boolean;
  clearRepository(): void;
  getRepository(): Repository | undefined;
  setRepository(value?: Repository): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryReply): GetRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryReply;
  static deserializeBinaryFromReader(message: GetRepositoryReply, reader: jspb.BinaryReader): GetRepositoryReply;
}

export namespace GetRepositoryReply {
  export type AsObject = {
    repository?: Repository.AsObject,
  }
}

export class GetRepositoryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryRequest): GetRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryRequest;
  static deserializeBinaryFromReader(message: GetRepositoryRequest, reader: jspb.BinaryReader): GetRepositoryRequest;
}

export namespace GetRepositoryRequest {
  export type AsObject = {
  }
}

export class CanLookupAssetsReply extends jspb.Message {
  getCanLookupAssets(): boolean;
  setCanLookupAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssetsReply): CanLookupAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssetsReply;
  static deserializeBinaryFromReader(message: CanLookupAssetsReply, reader: jspb.BinaryReader): CanLookupAssetsReply;
}

export namespace CanLookupAssetsReply {
  export type AsObject = {
    canLookupAssets: boolean,
  }
}

export class CanLookupAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssetsRequest): CanLookupAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssetsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssetsRequest, reader: jspb.BinaryReader): CanLookupAssetsRequest;
}

export namespace CanLookupAssetsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssetViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssetViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssetViewReply): UseComparativeAssetViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssetViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssetViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssetViewReply, reader: jspb.BinaryReader): UseComparativeAssetViewReply;
}

export namespace UseComparativeAssetViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssetViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssetViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssetViewRequest): UseComparativeAssetViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssetViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssetViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssetViewRequest, reader: jspb.BinaryReader): UseComparativeAssetViewRequest;
}

export namespace UseComparativeAssetViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssetViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssetViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssetViewReply): UsePlenaryAssetViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssetViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssetViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssetViewReply, reader: jspb.BinaryReader): UsePlenaryAssetViewReply;
}

export namespace UsePlenaryAssetViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssetViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssetViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssetViewRequest): UsePlenaryAssetViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssetViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssetViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssetViewRequest, reader: jspb.BinaryReader): UsePlenaryAssetViewRequest;
}

export namespace UsePlenaryAssetViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedRepositoryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedRepositoryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedRepositoryViewReply): UseFederatedRepositoryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedRepositoryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedRepositoryViewReply;
  static deserializeBinaryFromReader(message: UseFederatedRepositoryViewReply, reader: jspb.BinaryReader): UseFederatedRepositoryViewReply;
}

export namespace UseFederatedRepositoryViewReply {
  export type AsObject = {
  }
}

export class UseFederatedRepositoryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedRepositoryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedRepositoryViewRequest): UseFederatedRepositoryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedRepositoryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedRepositoryViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedRepositoryViewRequest, reader: jspb.BinaryReader): UseFederatedRepositoryViewRequest;
}

export namespace UseFederatedRepositoryViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedRepositoryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedRepositoryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedRepositoryViewReply): UseIsolatedRepositoryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedRepositoryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedRepositoryViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedRepositoryViewReply, reader: jspb.BinaryReader): UseIsolatedRepositoryViewReply;
}

export namespace UseIsolatedRepositoryViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedRepositoryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedRepositoryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedRepositoryViewRequest): UseIsolatedRepositoryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedRepositoryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedRepositoryViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedRepositoryViewRequest, reader: jspb.BinaryReader): UseIsolatedRepositoryViewRequest;
}

export namespace UseIsolatedRepositoryViewRequest {
  export type AsObject = {
  }
}

export class GetAssetReply extends jspb.Message {
  hasAsset(): boolean;
  clearAsset(): void;
  getAsset(): Asset | undefined;
  setAsset(value?: Asset): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetReply): GetAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetReply;
  static deserializeBinaryFromReader(message: GetAssetReply, reader: jspb.BinaryReader): GetAssetReply;
}

export namespace GetAssetReply {
  export type AsObject = {
    asset?: Asset.AsObject,
  }
}

export class GetAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetRequest): GetAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetRequest;
  static deserializeBinaryFromReader(message: GetAssetRequest, reader: jspb.BinaryReader): GetAssetRequest;
}

export namespace GetAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssetsByIdsRequest extends jspb.Message {
  clearAssetIdsList(): void;
  getAssetIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssetIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssetIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByIdsRequest): GetAssetsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByIdsRequest;
  static deserializeBinaryFromReader(message: GetAssetsByIdsRequest, reader: jspb.BinaryReader): GetAssetsByIdsRequest;
}

export namespace GetAssetsByIdsRequest {
  export type AsObject = {
    assetIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssetsByGenusTypeRequest extends jspb.Message {
  hasAssetGenusType(): boolean;
  clearAssetGenusType(): void;
  getAssetGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssetGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByGenusTypeRequest): GetAssetsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssetsByGenusTypeRequest, reader: jspb.BinaryReader): GetAssetsByGenusTypeRequest;
}

export namespace GetAssetsByGenusTypeRequest {
  export type AsObject = {
    assetGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssetsByParentGenusTypeRequest extends jspb.Message {
  hasAssetGenusType(): boolean;
  clearAssetGenusType(): void;
  getAssetGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssetGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByParentGenusTypeRequest): GetAssetsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssetsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAssetsByParentGenusTypeRequest;
}

export namespace GetAssetsByParentGenusTypeRequest {
  export type AsObject = {
    assetGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssetsByRecordTypeRequest extends jspb.Message {
  hasAssetRecordType(): boolean;
  clearAssetRecordType(): void;
  getAssetRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssetRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByRecordTypeRequest): GetAssetsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAssetsByRecordTypeRequest, reader: jspb.BinaryReader): GetAssetsByRecordTypeRequest;
}

export namespace GetAssetsByRecordTypeRequest {
  export type AsObject = {
    assetRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssetsByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByProviderRequest): GetAssetsByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByProviderRequest;
  static deserializeBinaryFromReader(message: GetAssetsByProviderRequest, reader: jspb.BinaryReader): GetAssetsByProviderRequest;
}

export namespace GetAssetsByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsRequest): GetAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsRequest;
  static deserializeBinaryFromReader(message: GetAssetsRequest, reader: jspb.BinaryReader): GetAssetsRequest;
}

export namespace GetAssetsRequest {
  export type AsObject = {
  }
}

export class CanSearchAssetsReply extends jspb.Message {
  getCanSearchAssets(): boolean;
  setCanSearchAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssetsReply): CanSearchAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssetsReply;
  static deserializeBinaryFromReader(message: CanSearchAssetsReply, reader: jspb.BinaryReader): CanSearchAssetsReply;
}

export namespace CanSearchAssetsReply {
  export type AsObject = {
    canSearchAssets: boolean,
  }
}

export class CanSearchAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssetsRequest): CanSearchAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssetsRequest;
  static deserializeBinaryFromReader(message: CanSearchAssetsRequest, reader: jspb.BinaryReader): CanSearchAssetsRequest;
}

export namespace CanSearchAssetsRequest {
  export type AsObject = {
  }
}

export class GetAssetQueryReply extends jspb.Message {
  hasAssetQuery(): boolean;
  clearAssetQuery(): void;
  getAssetQuery(): AssetQuery | undefined;
  setAssetQuery(value?: AssetQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetQueryReply): GetAssetQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetQueryReply;
  static deserializeBinaryFromReader(message: GetAssetQueryReply, reader: jspb.BinaryReader): GetAssetQueryReply;
}

export namespace GetAssetQueryReply {
  export type AsObject = {
    assetQuery?: AssetQuery.AsObject,
  }
}

export class GetAssetQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetQueryRequest): GetAssetQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetQueryRequest;
  static deserializeBinaryFromReader(message: GetAssetQueryRequest, reader: jspb.BinaryReader): GetAssetQueryRequest;
}

export namespace GetAssetQueryRequest {
  export type AsObject = {
  }
}

export class GetAssetsByQueryRequest extends jspb.Message {
  hasAssetQuery(): boolean;
  clearAssetQuery(): void;
  getAssetQuery(): AssetQuery | undefined;
  setAssetQuery(value?: AssetQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByQueryRequest): GetAssetsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByQueryRequest;
  static deserializeBinaryFromReader(message: GetAssetsByQueryRequest, reader: jspb.BinaryReader): GetAssetsByQueryRequest;
}

export namespace GetAssetsByQueryRequest {
  export type AsObject = {
    assetQuery?: AssetQuery.AsObject,
  }
}

export class GetAssetSearchReply extends jspb.Message {
  hasAssetSearch(): boolean;
  clearAssetSearch(): void;
  getAssetSearch(): AssetSearch | undefined;
  setAssetSearch(value?: AssetSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetSearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetSearchReply): GetAssetSearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetSearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetSearchReply;
  static deserializeBinaryFromReader(message: GetAssetSearchReply, reader: jspb.BinaryReader): GetAssetSearchReply;
}

export namespace GetAssetSearchReply {
  export type AsObject = {
    assetSearch?: AssetSearch.AsObject,
  }
}

export class GetAssetSearchRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetSearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetSearchRequest): GetAssetSearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetSearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetSearchRequest;
  static deserializeBinaryFromReader(message: GetAssetSearchRequest, reader: jspb.BinaryReader): GetAssetSearchRequest;
}

export namespace GetAssetSearchRequest {
  export type AsObject = {
  }
}

export class GetAssetSearchOrderReply extends jspb.Message {
  hasAssetSearchOrder(): boolean;
  clearAssetSearchOrder(): void;
  getAssetSearchOrder(): AssetSearchOrder | undefined;
  setAssetSearchOrder(value?: AssetSearchOrder): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetSearchOrderReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetSearchOrderReply): GetAssetSearchOrderReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetSearchOrderReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetSearchOrderReply;
  static deserializeBinaryFromReader(message: GetAssetSearchOrderReply, reader: jspb.BinaryReader): GetAssetSearchOrderReply;
}

export namespace GetAssetSearchOrderReply {
  export type AsObject = {
    assetSearchOrder?: AssetSearchOrder.AsObject,
  }
}

export class GetAssetSearchOrderRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetSearchOrderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetSearchOrderRequest): GetAssetSearchOrderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetSearchOrderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetSearchOrderRequest;
  static deserializeBinaryFromReader(message: GetAssetSearchOrderRequest, reader: jspb.BinaryReader): GetAssetSearchOrderRequest;
}

export namespace GetAssetSearchOrderRequest {
  export type AsObject = {
  }
}

export class GetAssetsBySearchReply extends jspb.Message {
  hasAssetSearchResults(): boolean;
  clearAssetSearchResults(): void;
  getAssetSearchResults(): AssetSearchResults | undefined;
  setAssetSearchResults(value?: AssetSearchResults): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsBySearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsBySearchReply): GetAssetsBySearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsBySearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsBySearchReply;
  static deserializeBinaryFromReader(message: GetAssetsBySearchReply, reader: jspb.BinaryReader): GetAssetsBySearchReply;
}

export namespace GetAssetsBySearchReply {
  export type AsObject = {
    assetSearchResults?: AssetSearchResults.AsObject,
  }
}

export class GetAssetsBySearchRequest extends jspb.Message {
  hasAssetQuery(): boolean;
  clearAssetQuery(): void;
  getAssetQuery(): AssetQuery | undefined;
  setAssetQuery(value?: AssetQuery): void;

  hasAssetSearch(): boolean;
  clearAssetSearch(): void;
  getAssetSearch(): AssetSearch | undefined;
  setAssetSearch(value?: AssetSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsBySearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsBySearchRequest): GetAssetsBySearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsBySearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsBySearchRequest;
  static deserializeBinaryFromReader(message: GetAssetsBySearchRequest, reader: jspb.BinaryReader): GetAssetsBySearchRequest;
}

export namespace GetAssetsBySearchRequest {
  export type AsObject = {
    assetQuery?: AssetQuery.AsObject,
    assetSearch?: AssetSearch.AsObject,
  }
}

export class GetAssetQueryFromInspectorReply extends jspb.Message {
  hasAssetQuery(): boolean;
  clearAssetQuery(): void;
  getAssetQuery(): AssetQuery | undefined;
  setAssetQuery(value?: AssetQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetQueryFromInspectorReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetQueryFromInspectorReply): GetAssetQueryFromInspectorReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetQueryFromInspectorReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetQueryFromInspectorReply;
  static deserializeBinaryFromReader(message: GetAssetQueryFromInspectorReply, reader: jspb.BinaryReader): GetAssetQueryFromInspectorReply;
}

export namespace GetAssetQueryFromInspectorReply {
  export type AsObject = {
    assetQuery?: AssetQuery.AsObject,
  }
}

export class GetAssetQueryFromInspectorRequest extends jspb.Message {
  hasAssetQueryInspector(): boolean;
  clearAssetQueryInspector(): void;
  getAssetQueryInspector(): AssetQueryInspector | undefined;
  setAssetQueryInspector(value?: AssetQueryInspector): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetQueryFromInspectorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetQueryFromInspectorRequest): GetAssetQueryFromInspectorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetQueryFromInspectorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetQueryFromInspectorRequest;
  static deserializeBinaryFromReader(message: GetAssetQueryFromInspectorRequest, reader: jspb.BinaryReader): GetAssetQueryFromInspectorRequest;
}

export namespace GetAssetQueryFromInspectorRequest {
  export type AsObject = {
    assetQueryInspector?: AssetQueryInspector.AsObject,
  }
}

export class CanCreateAssetsReply extends jspb.Message {
  getCanCreateAssets(): boolean;
  setCanCreateAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetsReply): CanCreateAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetsReply;
  static deserializeBinaryFromReader(message: CanCreateAssetsReply, reader: jspb.BinaryReader): CanCreateAssetsReply;
}

export namespace CanCreateAssetsReply {
  export type AsObject = {
    canCreateAssets: boolean,
  }
}

export class CanCreateAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetsRequest): CanCreateAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetsRequest;
  static deserializeBinaryFromReader(message: CanCreateAssetsRequest, reader: jspb.BinaryReader): CanCreateAssetsRequest;
}

export namespace CanCreateAssetsRequest {
  export type AsObject = {
  }
}

export class CanCreateAssetWithRecordTypesReply extends jspb.Message {
  getCanCreateAssetWithRecordTypes(): boolean;
  setCanCreateAssetWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetWithRecordTypesReply): CanCreateAssetWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAssetWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAssetWithRecordTypesReply;
}

export namespace CanCreateAssetWithRecordTypesReply {
  export type AsObject = {
    canCreateAssetWithRecordTypes: boolean,
  }
}

export class CanCreateAssetWithRecordTypesRequest extends jspb.Message {
  clearAssetRecordTypesList(): void;
  getAssetRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssetRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssetRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetWithRecordTypesRequest): CanCreateAssetWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAssetWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAssetWithRecordTypesRequest;
}

export namespace CanCreateAssetWithRecordTypesRequest {
  export type AsObject = {
    assetRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAssetFormForCreateReply extends jspb.Message {
  hasAssetForm(): boolean;
  clearAssetForm(): void;
  getAssetForm(): AssetForm | undefined;
  setAssetForm(value?: AssetForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetFormForCreateReply): GetAssetFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetFormForCreateReply;
  static deserializeBinaryFromReader(message: GetAssetFormForCreateReply, reader: jspb.BinaryReader): GetAssetFormForCreateReply;
}

export namespace GetAssetFormForCreateReply {
  export type AsObject = {
    assetForm?: AssetForm.AsObject,
  }
}

export class GetAssetFormForCreateRequest extends jspb.Message {
  clearAssetRecordTypesList(): void;
  getAssetRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssetRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssetRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetFormForCreateRequest): GetAssetFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetAssetFormForCreateRequest, reader: jspb.BinaryReader): GetAssetFormForCreateRequest;
}

export namespace GetAssetFormForCreateRequest {
  export type AsObject = {
    assetRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateAssetReply extends jspb.Message {
  hasAsset(): boolean;
  clearAsset(): void;
  getAsset(): Asset | undefined;
  setAsset(value?: Asset): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssetReply): CreateAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssetReply;
  static deserializeBinaryFromReader(message: CreateAssetReply, reader: jspb.BinaryReader): CreateAssetReply;
}

export namespace CreateAssetReply {
  export type AsObject = {
    asset?: Asset.AsObject,
  }
}

export class CreateAssetRequest extends jspb.Message {
  hasAssetForm(): boolean;
  clearAssetForm(): void;
  getAssetForm(): AssetForm | undefined;
  setAssetForm(value?: AssetForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssetRequest): CreateAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssetRequest;
  static deserializeBinaryFromReader(message: CreateAssetRequest, reader: jspb.BinaryReader): CreateAssetRequest;
}

export namespace CreateAssetRequest {
  export type AsObject = {
    assetForm?: AssetForm.AsObject,
  }
}

export class CanUpdateAssetsReply extends jspb.Message {
  getCanUpdateAssets(): boolean;
  setCanUpdateAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssetsReply): CanUpdateAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssetsReply;
  static deserializeBinaryFromReader(message: CanUpdateAssetsReply, reader: jspb.BinaryReader): CanUpdateAssetsReply;
}

export namespace CanUpdateAssetsReply {
  export type AsObject = {
    canUpdateAssets: boolean,
  }
}

export class CanUpdateAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssetsRequest): CanUpdateAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssetsRequest;
  static deserializeBinaryFromReader(message: CanUpdateAssetsRequest, reader: jspb.BinaryReader): CanUpdateAssetsRequest;
}

export namespace CanUpdateAssetsRequest {
  export type AsObject = {
  }
}

export class GetAssetFormForUpdateReply extends jspb.Message {
  hasAssetForm(): boolean;
  clearAssetForm(): void;
  getAssetForm(): AssetForm | undefined;
  setAssetForm(value?: AssetForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetFormForUpdateReply): GetAssetFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAssetFormForUpdateReply, reader: jspb.BinaryReader): GetAssetFormForUpdateReply;
}

export namespace GetAssetFormForUpdateReply {
  export type AsObject = {
    assetForm?: AssetForm.AsObject,
  }
}

export class GetAssetFormForUpdateRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetFormForUpdateRequest): GetAssetFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAssetFormForUpdateRequest, reader: jspb.BinaryReader): GetAssetFormForUpdateRequest;
}

export namespace GetAssetFormForUpdateRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssetReply): UpdateAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssetReply;
  static deserializeBinaryFromReader(message: UpdateAssetReply, reader: jspb.BinaryReader): UpdateAssetReply;
}

export namespace UpdateAssetReply {
  export type AsObject = {
  }
}

export class UpdateAssetRequest extends jspb.Message {
  hasAssetForm(): boolean;
  clearAssetForm(): void;
  getAssetForm(): AssetForm | undefined;
  setAssetForm(value?: AssetForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssetRequest): UpdateAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssetRequest;
  static deserializeBinaryFromReader(message: UpdateAssetRequest, reader: jspb.BinaryReader): UpdateAssetRequest;
}

export namespace UpdateAssetRequest {
  export type AsObject = {
    assetForm?: AssetForm.AsObject,
  }
}

export class CanDeleteAssetsReply extends jspb.Message {
  getCanDeleteAssets(): boolean;
  setCanDeleteAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssetsReply): CanDeleteAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssetsReply;
  static deserializeBinaryFromReader(message: CanDeleteAssetsReply, reader: jspb.BinaryReader): CanDeleteAssetsReply;
}

export namespace CanDeleteAssetsReply {
  export type AsObject = {
    canDeleteAssets: boolean,
  }
}

export class CanDeleteAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssetsRequest): CanDeleteAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssetsRequest;
  static deserializeBinaryFromReader(message: CanDeleteAssetsRequest, reader: jspb.BinaryReader): CanDeleteAssetsRequest;
}

export namespace CanDeleteAssetsRequest {
  export type AsObject = {
  }
}

export class DeleteAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssetReply): DeleteAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssetReply;
  static deserializeBinaryFromReader(message: DeleteAssetReply, reader: jspb.BinaryReader): DeleteAssetReply;
}

export namespace DeleteAssetReply {
  export type AsObject = {
  }
}

export class DeleteAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssetRequest): DeleteAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssetRequest;
  static deserializeBinaryFromReader(message: DeleteAssetRequest, reader: jspb.BinaryReader): DeleteAssetRequest;
}

export namespace DeleteAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageAssetAliasesReply extends jspb.Message {
  getCanManageAssetAliases(): boolean;
  setCanManageAssetAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssetAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssetAliasesReply): CanManageAssetAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssetAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssetAliasesReply;
  static deserializeBinaryFromReader(message: CanManageAssetAliasesReply, reader: jspb.BinaryReader): CanManageAssetAliasesReply;
}

export namespace CanManageAssetAliasesReply {
  export type AsObject = {
    canManageAssetAliases: boolean,
  }
}

export class CanManageAssetAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssetAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssetAliasesRequest): CanManageAssetAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssetAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssetAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageAssetAliasesRequest, reader: jspb.BinaryReader): CanManageAssetAliasesRequest;
}

export namespace CanManageAssetAliasesRequest {
  export type AsObject = {
  }
}

export class AliasAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssetReply): AliasAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssetReply;
  static deserializeBinaryFromReader(message: AliasAssetReply, reader: jspb.BinaryReader): AliasAssetReply;
}

export namespace AliasAssetReply {
  export type AsObject = {
  }
}

export class AliasAssetRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssetRequest): AliasAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssetRequest;
  static deserializeBinaryFromReader(message: AliasAssetRequest, reader: jspb.BinaryReader): AliasAssetRequest;
}

export namespace AliasAssetRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanCreateAssetContentReply extends jspb.Message {
  getCanCreateAssetContent(): boolean;
  setCanCreateAssetContent(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetContentReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetContentReply): CanCreateAssetContentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetContentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetContentReply;
  static deserializeBinaryFromReader(message: CanCreateAssetContentReply, reader: jspb.BinaryReader): CanCreateAssetContentReply;
}

export namespace CanCreateAssetContentReply {
  export type AsObject = {
    canCreateAssetContent: boolean,
  }
}

export class CanCreateAssetContentRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetContentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetContentRequest): CanCreateAssetContentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetContentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetContentRequest;
  static deserializeBinaryFromReader(message: CanCreateAssetContentRequest, reader: jspb.BinaryReader): CanCreateAssetContentRequest;
}

export namespace CanCreateAssetContentRequest {
  export type AsObject = {
  }
}

export class CanCreateAssetContentWithRecordTypesReply extends jspb.Message {
  getCanCreateAssetContentWithRecordTypes(): boolean;
  setCanCreateAssetContentWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetContentWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetContentWithRecordTypesReply): CanCreateAssetContentWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetContentWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetContentWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAssetContentWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAssetContentWithRecordTypesReply;
}

export namespace CanCreateAssetContentWithRecordTypesReply {
  export type AsObject = {
    canCreateAssetContentWithRecordTypes: boolean,
  }
}

export class CanCreateAssetContentWithRecordTypesRequest extends jspb.Message {
  clearAssetContentRecordTypesList(): void;
  getAssetContentRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssetContentRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssetContentRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssetContentWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssetContentWithRecordTypesRequest): CanCreateAssetContentWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssetContentWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssetContentWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAssetContentWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAssetContentWithRecordTypesRequest;
}

export namespace CanCreateAssetContentWithRecordTypesRequest {
  export type AsObject = {
    assetContentRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAssetContentFormForCreateReply extends jspb.Message {
  hasAssetContentForm(): boolean;
  clearAssetContentForm(): void;
  getAssetContentForm(): AssetContentForm | undefined;
  setAssetContentForm(value?: AssetContentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetContentFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetContentFormForCreateReply): GetAssetContentFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetContentFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetContentFormForCreateReply;
  static deserializeBinaryFromReader(message: GetAssetContentFormForCreateReply, reader: jspb.BinaryReader): GetAssetContentFormForCreateReply;
}

export namespace GetAssetContentFormForCreateReply {
  export type AsObject = {
    assetContentForm?: AssetContentForm.AsObject,
  }
}

export class GetAssetContentFormForCreateRequest extends jspb.Message {
  clearAssetContentRecordTypesList(): void;
  getAssetContentRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssetContentRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssetContentRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetContentFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetContentFormForCreateRequest): GetAssetContentFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetContentFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetContentFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetAssetContentFormForCreateRequest, reader: jspb.BinaryReader): GetAssetContentFormForCreateRequest;
}

export namespace GetAssetContentFormForCreateRequest {
  export type AsObject = {
    assetContentRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateAssetContentReply extends jspb.Message {
  hasAssetContent(): boolean;
  clearAssetContent(): void;
  getAssetContent(): AssetContent | undefined;
  setAssetContent(value?: AssetContent): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssetContentReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssetContentReply): CreateAssetContentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssetContentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssetContentReply;
  static deserializeBinaryFromReader(message: CreateAssetContentReply, reader: jspb.BinaryReader): CreateAssetContentReply;
}

export namespace CreateAssetContentReply {
  export type AsObject = {
    assetContent?: AssetContent.AsObject,
  }
}

export class CreateAssetContentRequest extends jspb.Message {
  hasAssetContentForm(): boolean;
  clearAssetContentForm(): void;
  getAssetContentForm(): AssetContentForm | undefined;
  setAssetContentForm(value?: AssetContentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssetContentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssetContentRequest): CreateAssetContentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssetContentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssetContentRequest;
  static deserializeBinaryFromReader(message: CreateAssetContentRequest, reader: jspb.BinaryReader): CreateAssetContentRequest;
}

export namespace CreateAssetContentRequest {
  export type AsObject = {
    assetContentForm?: AssetContentForm.AsObject,
  }
}

export class CanUpdateAssetContentsReply extends jspb.Message {
  getCanUpdateAssetContents(): boolean;
  setCanUpdateAssetContents(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssetContentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssetContentsReply): CanUpdateAssetContentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssetContentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssetContentsReply;
  static deserializeBinaryFromReader(message: CanUpdateAssetContentsReply, reader: jspb.BinaryReader): CanUpdateAssetContentsReply;
}

export namespace CanUpdateAssetContentsReply {
  export type AsObject = {
    canUpdateAssetContents: boolean,
  }
}

export class CanUpdateAssetContentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssetContentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssetContentsRequest): CanUpdateAssetContentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssetContentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssetContentsRequest;
  static deserializeBinaryFromReader(message: CanUpdateAssetContentsRequest, reader: jspb.BinaryReader): CanUpdateAssetContentsRequest;
}

export namespace CanUpdateAssetContentsRequest {
  export type AsObject = {
  }
}

export class GetAssetContentFormForUpdateReply extends jspb.Message {
  hasAssetContentForm(): boolean;
  clearAssetContentForm(): void;
  getAssetContentForm(): AssetContentForm | undefined;
  setAssetContentForm(value?: AssetContentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetContentFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetContentFormForUpdateReply): GetAssetContentFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetContentFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetContentFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAssetContentFormForUpdateReply, reader: jspb.BinaryReader): GetAssetContentFormForUpdateReply;
}

export namespace GetAssetContentFormForUpdateReply {
  export type AsObject = {
    assetContentForm?: AssetContentForm.AsObject,
  }
}

export class GetAssetContentFormForUpdateRequest extends jspb.Message {
  hasAssetContentId(): boolean;
  clearAssetContentId(): void;
  getAssetContentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetContentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetContentFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetContentFormForUpdateRequest): GetAssetContentFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetContentFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetContentFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAssetContentFormForUpdateRequest, reader: jspb.BinaryReader): GetAssetContentFormForUpdateRequest;
}

export namespace GetAssetContentFormForUpdateRequest {
  export type AsObject = {
    assetContentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAssetContentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssetContentReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssetContentReply): UpdateAssetContentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssetContentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssetContentReply;
  static deserializeBinaryFromReader(message: UpdateAssetContentReply, reader: jspb.BinaryReader): UpdateAssetContentReply;
}

export namespace UpdateAssetContentReply {
  export type AsObject = {
  }
}

export class UpdateAssetContentRequest extends jspb.Message {
  hasAssetContentForm(): boolean;
  clearAssetContentForm(): void;
  getAssetContentForm(): AssetContentForm | undefined;
  setAssetContentForm(value?: AssetContentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssetContentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssetContentRequest): UpdateAssetContentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssetContentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssetContentRequest;
  static deserializeBinaryFromReader(message: UpdateAssetContentRequest, reader: jspb.BinaryReader): UpdateAssetContentRequest;
}

export namespace UpdateAssetContentRequest {
  export type AsObject = {
    assetContentForm?: AssetContentForm.AsObject,
  }
}

export class CanDeleteAssetContentsReply extends jspb.Message {
  getCanDeleteAssetContents(): boolean;
  setCanDeleteAssetContents(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssetContentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssetContentsReply): CanDeleteAssetContentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssetContentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssetContentsReply;
  static deserializeBinaryFromReader(message: CanDeleteAssetContentsReply, reader: jspb.BinaryReader): CanDeleteAssetContentsReply;
}

export namespace CanDeleteAssetContentsReply {
  export type AsObject = {
    canDeleteAssetContents: boolean,
  }
}

export class CanDeleteAssetContentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssetContentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssetContentsRequest): CanDeleteAssetContentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssetContentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssetContentsRequest;
  static deserializeBinaryFromReader(message: CanDeleteAssetContentsRequest, reader: jspb.BinaryReader): CanDeleteAssetContentsRequest;
}

export namespace CanDeleteAssetContentsRequest {
  export type AsObject = {
  }
}

export class DeleteAssetContentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssetContentReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssetContentReply): DeleteAssetContentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssetContentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssetContentReply;
  static deserializeBinaryFromReader(message: DeleteAssetContentReply, reader: jspb.BinaryReader): DeleteAssetContentReply;
}

export namespace DeleteAssetContentReply {
  export type AsObject = {
  }
}

export class DeleteAssetContentRequest extends jspb.Message {
  hasAssetContentId(): boolean;
  clearAssetContentId(): void;
  getAssetContentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetContentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssetContentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssetContentRequest): DeleteAssetContentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssetContentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssetContentRequest;
  static deserializeBinaryFromReader(message: DeleteAssetContentRequest, reader: jspb.BinaryReader): DeleteAssetContentRequest;
}

export namespace DeleteAssetContentRequest {
  export type AsObject = {
    assetContentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanRegisterForAssetNotificationsReply extends jspb.Message {
  getCanRegisterForAssetNotifications(): boolean;
  setCanRegisterForAssetNotifications(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanRegisterForAssetNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanRegisterForAssetNotificationsReply): CanRegisterForAssetNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanRegisterForAssetNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanRegisterForAssetNotificationsReply;
  static deserializeBinaryFromReader(message: CanRegisterForAssetNotificationsReply, reader: jspb.BinaryReader): CanRegisterForAssetNotificationsReply;
}

export namespace CanRegisterForAssetNotificationsReply {
  export type AsObject = {
    canRegisterForAssetNotifications: boolean,
  }
}

export class CanRegisterForAssetNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanRegisterForAssetNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanRegisterForAssetNotificationsRequest): CanRegisterForAssetNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanRegisterForAssetNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanRegisterForAssetNotificationsRequest;
  static deserializeBinaryFromReader(message: CanRegisterForAssetNotificationsRequest, reader: jspb.BinaryReader): CanRegisterForAssetNotificationsRequest;
}

export namespace CanRegisterForAssetNotificationsRequest {
  export type AsObject = {
  }
}

export class RegisterForNewAssetsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewAssetsReply): RegisterForNewAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewAssetsReply;
  static deserializeBinaryFromReader(message: RegisterForNewAssetsReply, reader: jspb.BinaryReader): RegisterForNewAssetsReply;
}

export namespace RegisterForNewAssetsReply {
  export type AsObject = {
  }
}

export class RegisterForNewAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewAssetsRequest): RegisterForNewAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewAssetsRequest;
  static deserializeBinaryFromReader(message: RegisterForNewAssetsRequest, reader: jspb.BinaryReader): RegisterForNewAssetsRequest;
}

export namespace RegisterForNewAssetsRequest {
  export type AsObject = {
  }
}

export class RegisterForNewAssetsByGenusTypeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewAssetsByGenusTypeReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewAssetsByGenusTypeReply): RegisterForNewAssetsByGenusTypeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewAssetsByGenusTypeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewAssetsByGenusTypeReply;
  static deserializeBinaryFromReader(message: RegisterForNewAssetsByGenusTypeReply, reader: jspb.BinaryReader): RegisterForNewAssetsByGenusTypeReply;
}

export namespace RegisterForNewAssetsByGenusTypeReply {
  export type AsObject = {
  }
}

export class RegisterForNewAssetsByGenusTypeRequest extends jspb.Message {
  hasAssetGenusType(): boolean;
  clearAssetGenusType(): void;
  getAssetGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssetGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewAssetsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewAssetsByGenusTypeRequest): RegisterForNewAssetsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewAssetsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewAssetsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: RegisterForNewAssetsByGenusTypeRequest, reader: jspb.BinaryReader): RegisterForNewAssetsByGenusTypeRequest;
}

export namespace RegisterForNewAssetsByGenusTypeRequest {
  export type AsObject = {
    assetGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class RegisterForChangedAssetsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedAssetsReply): RegisterForChangedAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedAssetsReply;
  static deserializeBinaryFromReader(message: RegisterForChangedAssetsReply, reader: jspb.BinaryReader): RegisterForChangedAssetsReply;
}

export namespace RegisterForChangedAssetsReply {
  export type AsObject = {
  }
}

export class RegisterForChangedAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedAssetsRequest): RegisterForChangedAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedAssetsRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedAssetsRequest, reader: jspb.BinaryReader): RegisterForChangedAssetsRequest;
}

export namespace RegisterForChangedAssetsRequest {
  export type AsObject = {
  }
}

export class RegisterForChangedAssetsByGenusTypeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedAssetsByGenusTypeReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedAssetsByGenusTypeReply): RegisterForChangedAssetsByGenusTypeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedAssetsByGenusTypeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedAssetsByGenusTypeReply;
  static deserializeBinaryFromReader(message: RegisterForChangedAssetsByGenusTypeReply, reader: jspb.BinaryReader): RegisterForChangedAssetsByGenusTypeReply;
}

export namespace RegisterForChangedAssetsByGenusTypeReply {
  export type AsObject = {
  }
}

export class RegisterForChangedAssetsByGenusTypeRequest extends jspb.Message {
  hasAssetGenusType(): boolean;
  clearAssetGenusType(): void;
  getAssetGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssetGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedAssetsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedAssetsByGenusTypeRequest): RegisterForChangedAssetsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedAssetsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedAssetsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedAssetsByGenusTypeRequest, reader: jspb.BinaryReader): RegisterForChangedAssetsByGenusTypeRequest;
}

export namespace RegisterForChangedAssetsByGenusTypeRequest {
  export type AsObject = {
    assetGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class RegisterForChangedAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedAssetReply): RegisterForChangedAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedAssetReply;
  static deserializeBinaryFromReader(message: RegisterForChangedAssetReply, reader: jspb.BinaryReader): RegisterForChangedAssetReply;
}

export namespace RegisterForChangedAssetReply {
  export type AsObject = {
  }
}

export class RegisterForChangedAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedAssetRequest): RegisterForChangedAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedAssetRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedAssetRequest, reader: jspb.BinaryReader): RegisterForChangedAssetRequest;
}

export namespace RegisterForChangedAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RegisterForDeletedAssetsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedAssetsReply): RegisterForDeletedAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedAssetsReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedAssetsReply, reader: jspb.BinaryReader): RegisterForDeletedAssetsReply;
}

export namespace RegisterForDeletedAssetsReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedAssetsRequest): RegisterForDeletedAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedAssetsRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedAssetsRequest, reader: jspb.BinaryReader): RegisterForDeletedAssetsRequest;
}

export namespace RegisterForDeletedAssetsRequest {
  export type AsObject = {
  }
}

export class RegisterForDeletedAssetsByGenusTypeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedAssetsByGenusTypeReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedAssetsByGenusTypeReply): RegisterForDeletedAssetsByGenusTypeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedAssetsByGenusTypeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedAssetsByGenusTypeReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedAssetsByGenusTypeReply, reader: jspb.BinaryReader): RegisterForDeletedAssetsByGenusTypeReply;
}

export namespace RegisterForDeletedAssetsByGenusTypeReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedAssetsByGenusTypeRequest extends jspb.Message {
  hasAssetGenusType(): boolean;
  clearAssetGenusType(): void;
  getAssetGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssetGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedAssetsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedAssetsByGenusTypeRequest): RegisterForDeletedAssetsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedAssetsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedAssetsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedAssetsByGenusTypeRequest, reader: jspb.BinaryReader): RegisterForDeletedAssetsByGenusTypeRequest;
}

export namespace RegisterForDeletedAssetsByGenusTypeRequest {
  export type AsObject = {
    assetGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class RegisterForDeletedAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedAssetReply): RegisterForDeletedAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedAssetReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedAssetReply, reader: jspb.BinaryReader): RegisterForDeletedAssetReply;
}

export namespace RegisterForDeletedAssetReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedAssetRequest): RegisterForDeletedAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedAssetRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedAssetRequest, reader: jspb.BinaryReader): RegisterForDeletedAssetRequest;
}

export namespace RegisterForDeletedAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReliableAssetNotificationsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReliableAssetNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReliableAssetNotificationsReply): ReliableAssetNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReliableAssetNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReliableAssetNotificationsReply;
  static deserializeBinaryFromReader(message: ReliableAssetNotificationsReply, reader: jspb.BinaryReader): ReliableAssetNotificationsReply;
}

export namespace ReliableAssetNotificationsReply {
  export type AsObject = {
  }
}

export class ReliableAssetNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReliableAssetNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReliableAssetNotificationsRequest): ReliableAssetNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReliableAssetNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReliableAssetNotificationsRequest;
  static deserializeBinaryFromReader(message: ReliableAssetNotificationsRequest, reader: jspb.BinaryReader): ReliableAssetNotificationsRequest;
}

export namespace ReliableAssetNotificationsRequest {
  export type AsObject = {
  }
}

export class UnreliableAssetNotificationsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnreliableAssetNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnreliableAssetNotificationsReply): UnreliableAssetNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnreliableAssetNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnreliableAssetNotificationsReply;
  static deserializeBinaryFromReader(message: UnreliableAssetNotificationsReply, reader: jspb.BinaryReader): UnreliableAssetNotificationsReply;
}

export namespace UnreliableAssetNotificationsReply {
  export type AsObject = {
  }
}

export class UnreliableAssetNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnreliableAssetNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnreliableAssetNotificationsRequest): UnreliableAssetNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnreliableAssetNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnreliableAssetNotificationsRequest;
  static deserializeBinaryFromReader(message: UnreliableAssetNotificationsRequest, reader: jspb.BinaryReader): UnreliableAssetNotificationsRequest;
}

export namespace UnreliableAssetNotificationsRequest {
  export type AsObject = {
  }
}

export class AcknowledgeAssetNotificationReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AcknowledgeAssetNotificationReply.AsObject;
  static toObject(includeInstance: boolean, msg: AcknowledgeAssetNotificationReply): AcknowledgeAssetNotificationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AcknowledgeAssetNotificationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AcknowledgeAssetNotificationReply;
  static deserializeBinaryFromReader(message: AcknowledgeAssetNotificationReply, reader: jspb.BinaryReader): AcknowledgeAssetNotificationReply;
}

export namespace AcknowledgeAssetNotificationReply {
  export type AsObject = {
  }
}

export class AcknowledgeAssetNotificationRequest extends jspb.Message {
  hasNotificationId(): boolean;
  clearNotificationId(): void;
  getNotificationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNotificationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AcknowledgeAssetNotificationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AcknowledgeAssetNotificationRequest): AcknowledgeAssetNotificationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AcknowledgeAssetNotificationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AcknowledgeAssetNotificationRequest;
  static deserializeBinaryFromReader(message: AcknowledgeAssetNotificationRequest, reader: jspb.BinaryReader): AcknowledgeAssetNotificationRequest;
}

export namespace AcknowledgeAssetNotificationRequest {
  export type AsObject = {
    notificationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssetRepositoryMappingsReply extends jspb.Message {
  getCanLookupAssetRepositoryMappings(): boolean;
  setCanLookupAssetRepositoryMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssetRepositoryMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssetRepositoryMappingsReply): CanLookupAssetRepositoryMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssetRepositoryMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssetRepositoryMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupAssetRepositoryMappingsReply, reader: jspb.BinaryReader): CanLookupAssetRepositoryMappingsReply;
}

export namespace CanLookupAssetRepositoryMappingsReply {
  export type AsObject = {
    canLookupAssetRepositoryMappings: boolean,
  }
}

export class CanLookupAssetRepositoryMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssetRepositoryMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssetRepositoryMappingsRequest): CanLookupAssetRepositoryMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssetRepositoryMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssetRepositoryMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssetRepositoryMappingsRequest, reader: jspb.BinaryReader): CanLookupAssetRepositoryMappingsRequest;
}

export namespace CanLookupAssetRepositoryMappingsRequest {
  export type AsObject = {
  }
}

export class UseComparativeRepositoryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeRepositoryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeRepositoryViewReply): UseComparativeRepositoryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeRepositoryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeRepositoryViewReply;
  static deserializeBinaryFromReader(message: UseComparativeRepositoryViewReply, reader: jspb.BinaryReader): UseComparativeRepositoryViewReply;
}

export namespace UseComparativeRepositoryViewReply {
  export type AsObject = {
  }
}

export class UseComparativeRepositoryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeRepositoryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeRepositoryViewRequest): UseComparativeRepositoryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeRepositoryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeRepositoryViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeRepositoryViewRequest, reader: jspb.BinaryReader): UseComparativeRepositoryViewRequest;
}

export namespace UseComparativeRepositoryViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryRepositoryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryRepositoryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryRepositoryViewReply): UsePlenaryRepositoryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryRepositoryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryRepositoryViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryRepositoryViewReply, reader: jspb.BinaryReader): UsePlenaryRepositoryViewReply;
}

export namespace UsePlenaryRepositoryViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryRepositoryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryRepositoryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryRepositoryViewRequest): UsePlenaryRepositoryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryRepositoryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryRepositoryViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryRepositoryViewRequest, reader: jspb.BinaryReader): UsePlenaryRepositoryViewRequest;
}

export namespace UsePlenaryRepositoryViewRequest {
  export type AsObject = {
  }
}

export class GetAssetIdsByRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetIdsByRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetIdsByRepositoryRequest): GetAssetIdsByRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetIdsByRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetIdsByRepositoryRequest;
  static deserializeBinaryFromReader(message: GetAssetIdsByRepositoryRequest, reader: jspb.BinaryReader): GetAssetIdsByRepositoryRequest;
}

export namespace GetAssetIdsByRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssetsByRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByRepositoryRequest): GetAssetsByRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByRepositoryRequest;
  static deserializeBinaryFromReader(message: GetAssetsByRepositoryRequest, reader: jspb.BinaryReader): GetAssetsByRepositoryRequest;
}

export namespace GetAssetsByRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssetIdsByRepositoriesRequest extends jspb.Message {
  clearRepositoryIdsList(): void;
  getRepositoryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setRepositoryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addRepositoryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetIdsByRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetIdsByRepositoriesRequest): GetAssetIdsByRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetIdsByRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetIdsByRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetAssetIdsByRepositoriesRequest, reader: jspb.BinaryReader): GetAssetIdsByRepositoriesRequest;
}

export namespace GetAssetIdsByRepositoriesRequest {
  export type AsObject = {
    repositoryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssetsByRepositoriesRequest extends jspb.Message {
  clearRepositoryIdsList(): void;
  getRepositoryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setRepositoryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addRepositoryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssetsByRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssetsByRepositoriesRequest): GetAssetsByRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssetsByRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssetsByRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetAssetsByRepositoriesRequest, reader: jspb.BinaryReader): GetAssetsByRepositoriesRequest;
}

export namespace GetAssetsByRepositoriesRequest {
  export type AsObject = {
    repositoryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetRepositoryIdsByAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryIdsByAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryIdsByAssetRequest): GetRepositoryIdsByAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryIdsByAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryIdsByAssetRequest;
  static deserializeBinaryFromReader(message: GetRepositoryIdsByAssetRequest, reader: jspb.BinaryReader): GetRepositoryIdsByAssetRequest;
}

export namespace GetRepositoryIdsByAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoriesByAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByAssetRequest): GetRepositoriesByAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByAssetRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByAssetRequest, reader: jspb.BinaryReader): GetRepositoriesByAssetRequest;
}

export namespace GetRepositoriesByAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAssetsReply extends jspb.Message {
  getCanAssignAssets(): boolean;
  setCanAssignAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssetsReply): CanAssignAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssetsReply;
  static deserializeBinaryFromReader(message: CanAssignAssetsReply, reader: jspb.BinaryReader): CanAssignAssetsReply;
}

export namespace CanAssignAssetsReply {
  export type AsObject = {
    canAssignAssets: boolean,
  }
}

export class CanAssignAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssetsRequest): CanAssignAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssetsRequest;
  static deserializeBinaryFromReader(message: CanAssignAssetsRequest, reader: jspb.BinaryReader): CanAssignAssetsRequest;
}

export namespace CanAssignAssetsRequest {
  export type AsObject = {
  }
}

export class CanAssignAssetsToRepositoryReply extends jspb.Message {
  getCanAssignAssetsToRepository(): boolean;
  setCanAssignAssetsToRepository(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssetsToRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssetsToRepositoryReply): CanAssignAssetsToRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssetsToRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssetsToRepositoryReply;
  static deserializeBinaryFromReader(message: CanAssignAssetsToRepositoryReply, reader: jspb.BinaryReader): CanAssignAssetsToRepositoryReply;
}

export namespace CanAssignAssetsToRepositoryReply {
  export type AsObject = {
    canAssignAssetsToRepository: boolean,
  }
}

export class CanAssignAssetsToRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssetsToRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssetsToRepositoryRequest): CanAssignAssetsToRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssetsToRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssetsToRepositoryRequest;
  static deserializeBinaryFromReader(message: CanAssignAssetsToRepositoryRequest, reader: jspb.BinaryReader): CanAssignAssetsToRepositoryRequest;
}

export namespace CanAssignAssetsToRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableRepositoryIdsRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableRepositoryIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableRepositoryIdsRequest): GetAssignableRepositoryIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableRepositoryIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableRepositoryIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableRepositoryIdsRequest, reader: jspb.BinaryReader): GetAssignableRepositoryIdsRequest;
}

export namespace GetAssignableRepositoryIdsRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableRepositoryIdsForAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableRepositoryIdsForAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableRepositoryIdsForAssetRequest): GetAssignableRepositoryIdsForAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableRepositoryIdsForAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableRepositoryIdsForAssetRequest;
  static deserializeBinaryFromReader(message: GetAssignableRepositoryIdsForAssetRequest, reader: jspb.BinaryReader): GetAssignableRepositoryIdsForAssetRequest;
}

export namespace GetAssignableRepositoryIdsForAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAssetToRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssetToRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssetToRepositoryReply): AssignAssetToRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssetToRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssetToRepositoryReply;
  static deserializeBinaryFromReader(message: AssignAssetToRepositoryReply, reader: jspb.BinaryReader): AssignAssetToRepositoryReply;
}

export namespace AssignAssetToRepositoryReply {
  export type AsObject = {
  }
}

export class AssignAssetToRepositoryRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssetToRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssetToRepositoryRequest): AssignAssetToRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssetToRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssetToRepositoryRequest;
  static deserializeBinaryFromReader(message: AssignAssetToRepositoryRequest, reader: jspb.BinaryReader): AssignAssetToRepositoryRequest;
}

export namespace AssignAssetToRepositoryRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAssetFromRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssetFromRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssetFromRepositoryReply): UnassignAssetFromRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssetFromRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssetFromRepositoryReply;
  static deserializeBinaryFromReader(message: UnassignAssetFromRepositoryReply, reader: jspb.BinaryReader): UnassignAssetFromRepositoryReply;
}

export namespace UnassignAssetFromRepositoryReply {
  export type AsObject = {
  }
}

export class UnassignAssetFromRepositoryRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssetFromRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssetFromRepositoryRequest): UnassignAssetFromRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssetFromRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssetFromRepositoryRequest;
  static deserializeBinaryFromReader(message: UnassignAssetFromRepositoryRequest, reader: jspb.BinaryReader): UnassignAssetFromRepositoryRequest;
}

export namespace UnassignAssetFromRepositoryRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAccessAssetCompositionsReply extends jspb.Message {
  getCanAccessAssetCompositions(): boolean;
  setCanAccessAssetCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAssetCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAssetCompositionsReply): CanAccessAssetCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAssetCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAssetCompositionsReply;
  static deserializeBinaryFromReader(message: CanAccessAssetCompositionsReply, reader: jspb.BinaryReader): CanAccessAssetCompositionsReply;
}

export namespace CanAccessAssetCompositionsReply {
  export type AsObject = {
    canAccessAssetCompositions: boolean,
  }
}

export class CanAccessAssetCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAssetCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAssetCompositionsRequest): CanAccessAssetCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAssetCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAssetCompositionsRequest;
  static deserializeBinaryFromReader(message: CanAccessAssetCompositionsRequest, reader: jspb.BinaryReader): CanAccessAssetCompositionsRequest;
}

export namespace CanAccessAssetCompositionsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssetCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssetCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssetCompositionViewReply): UseComparativeAssetCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssetCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssetCompositionViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssetCompositionViewReply, reader: jspb.BinaryReader): UseComparativeAssetCompositionViewReply;
}

export namespace UseComparativeAssetCompositionViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssetCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssetCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssetCompositionViewRequest): UseComparativeAssetCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssetCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssetCompositionViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssetCompositionViewRequest, reader: jspb.BinaryReader): UseComparativeAssetCompositionViewRequest;
}

export namespace UseComparativeAssetCompositionViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssetCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssetCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssetCompositionViewReply): UsePlenaryAssetCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssetCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssetCompositionViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssetCompositionViewReply, reader: jspb.BinaryReader): UsePlenaryAssetCompositionViewReply;
}

export namespace UsePlenaryAssetCompositionViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssetCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssetCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssetCompositionViewRequest): UsePlenaryAssetCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssetCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssetCompositionViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssetCompositionViewRequest, reader: jspb.BinaryReader): UsePlenaryAssetCompositionViewRequest;
}

export namespace UsePlenaryAssetCompositionViewRequest {
  export type AsObject = {
  }
}

export class GetCompositionAssetsRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionAssetsRequest): GetCompositionAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionAssetsRequest;
  static deserializeBinaryFromReader(message: GetCompositionAssetsRequest, reader: jspb.BinaryReader): GetCompositionAssetsRequest;
}

export namespace GetCompositionAssetsRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCompositionsByAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByAssetRequest): GetCompositionsByAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByAssetRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByAssetRequest, reader: jspb.BinaryReader): GetCompositionsByAssetRequest;
}

export namespace GetCompositionsByAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanComposeAssetsReply extends jspb.Message {
  getCanComposeAssets(): boolean;
  setCanComposeAssets(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanComposeAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanComposeAssetsReply): CanComposeAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanComposeAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanComposeAssetsReply;
  static deserializeBinaryFromReader(message: CanComposeAssetsReply, reader: jspb.BinaryReader): CanComposeAssetsReply;
}

export namespace CanComposeAssetsReply {
  export type AsObject = {
    canComposeAssets: boolean,
  }
}

export class CanComposeAssetsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanComposeAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanComposeAssetsRequest): CanComposeAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanComposeAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanComposeAssetsRequest;
  static deserializeBinaryFromReader(message: CanComposeAssetsRequest, reader: jspb.BinaryReader): CanComposeAssetsRequest;
}

export namespace CanComposeAssetsRequest {
  export type AsObject = {
  }
}

export class AddAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddAssetReply): AddAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddAssetReply;
  static deserializeBinaryFromReader(message: AddAssetReply, reader: jspb.BinaryReader): AddAssetReply;
}

export namespace AddAssetReply {
  export type AsObject = {
  }
}

export class AddAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddAssetRequest): AddAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddAssetRequest;
  static deserializeBinaryFromReader(message: AddAssetRequest, reader: jspb.BinaryReader): AddAssetRequest;
}

export namespace AddAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveAssetAheadReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveAssetAheadReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveAssetAheadReply): MoveAssetAheadReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveAssetAheadReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveAssetAheadReply;
  static deserializeBinaryFromReader(message: MoveAssetAheadReply, reader: jspb.BinaryReader): MoveAssetAheadReply;
}

export namespace MoveAssetAheadReply {
  export type AsObject = {
  }
}

export class MoveAssetAheadRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveAssetAheadRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveAssetAheadRequest): MoveAssetAheadRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveAssetAheadRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveAssetAheadRequest;
  static deserializeBinaryFromReader(message: MoveAssetAheadRequest, reader: jspb.BinaryReader): MoveAssetAheadRequest;
}

export namespace MoveAssetAheadRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveAssetBehindReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveAssetBehindReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveAssetBehindReply): MoveAssetBehindReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveAssetBehindReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveAssetBehindReply;
  static deserializeBinaryFromReader(message: MoveAssetBehindReply, reader: jspb.BinaryReader): MoveAssetBehindReply;
}

export namespace MoveAssetBehindReply {
  export type AsObject = {
  }
}

export class MoveAssetBehindRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveAssetBehindRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveAssetBehindRequest): MoveAssetBehindRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveAssetBehindRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveAssetBehindRequest;
  static deserializeBinaryFromReader(message: MoveAssetBehindRequest, reader: jspb.BinaryReader): MoveAssetBehindRequest;
}

export namespace MoveAssetBehindRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class OrderAssetsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderAssetsReply.AsObject;
  static toObject(includeInstance: boolean, msg: OrderAssetsReply): OrderAssetsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderAssetsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderAssetsReply;
  static deserializeBinaryFromReader(message: OrderAssetsReply, reader: jspb.BinaryReader): OrderAssetsReply;
}

export namespace OrderAssetsReply {
  export type AsObject = {
  }
}

export class OrderAssetsRequest extends jspb.Message {
  clearAssetIdsList(): void;
  getAssetIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssetIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssetIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: OrderAssetsRequest): OrderAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderAssetsRequest;
  static deserializeBinaryFromReader(message: OrderAssetsRequest, reader: jspb.BinaryReader): OrderAssetsRequest;
}

export namespace OrderAssetsRequest {
  export type AsObject = {
    assetIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveAssetReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveAssetReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveAssetReply): RemoveAssetReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveAssetReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveAssetReply;
  static deserializeBinaryFromReader(message: RemoveAssetReply, reader: jspb.BinaryReader): RemoveAssetReply;
}

export namespace RemoveAssetReply {
  export type AsObject = {
  }
}

export class RemoveAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveAssetRequest): RemoveAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveAssetRequest;
  static deserializeBinaryFromReader(message: RemoveAssetRequest, reader: jspb.BinaryReader): RemoveAssetRequest;
}

export namespace RemoveAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupCompositionsReply extends jspb.Message {
  getCanLookupCompositions(): boolean;
  setCanLookupCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCompositionsReply): CanLookupCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCompositionsReply;
  static deserializeBinaryFromReader(message: CanLookupCompositionsReply, reader: jspb.BinaryReader): CanLookupCompositionsReply;
}

export namespace CanLookupCompositionsReply {
  export type AsObject = {
    canLookupCompositions: boolean,
  }
}

export class CanLookupCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCompositionsRequest): CanLookupCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCompositionsRequest;
  static deserializeBinaryFromReader(message: CanLookupCompositionsRequest, reader: jspb.BinaryReader): CanLookupCompositionsRequest;
}

export namespace CanLookupCompositionsRequest {
  export type AsObject = {
  }
}

export class UseComparativeCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCompositionViewReply): UseComparativeCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCompositionViewReply;
  static deserializeBinaryFromReader(message: UseComparativeCompositionViewReply, reader: jspb.BinaryReader): UseComparativeCompositionViewReply;
}

export namespace UseComparativeCompositionViewReply {
  export type AsObject = {
  }
}

export class UseComparativeCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCompositionViewRequest): UseComparativeCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCompositionViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeCompositionViewRequest, reader: jspb.BinaryReader): UseComparativeCompositionViewRequest;
}

export namespace UseComparativeCompositionViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCompositionViewReply): UsePlenaryCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCompositionViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryCompositionViewReply, reader: jspb.BinaryReader): UsePlenaryCompositionViewReply;
}

export namespace UsePlenaryCompositionViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCompositionViewRequest): UsePlenaryCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCompositionViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryCompositionViewRequest, reader: jspb.BinaryReader): UsePlenaryCompositionViewRequest;
}

export namespace UsePlenaryCompositionViewRequest {
  export type AsObject = {
  }
}

export class UseActiveCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseActiveCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseActiveCompositionViewReply): UseActiveCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseActiveCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseActiveCompositionViewReply;
  static deserializeBinaryFromReader(message: UseActiveCompositionViewReply, reader: jspb.BinaryReader): UseActiveCompositionViewReply;
}

export namespace UseActiveCompositionViewReply {
  export type AsObject = {
  }
}

export class UseActiveCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseActiveCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseActiveCompositionViewRequest): UseActiveCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseActiveCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseActiveCompositionViewRequest;
  static deserializeBinaryFromReader(message: UseActiveCompositionViewRequest, reader: jspb.BinaryReader): UseActiveCompositionViewRequest;
}

export namespace UseActiveCompositionViewRequest {
  export type AsObject = {
  }
}

export class UseAnyStatusCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyStatusCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyStatusCompositionViewReply): UseAnyStatusCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyStatusCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyStatusCompositionViewReply;
  static deserializeBinaryFromReader(message: UseAnyStatusCompositionViewReply, reader: jspb.BinaryReader): UseAnyStatusCompositionViewReply;
}

export namespace UseAnyStatusCompositionViewReply {
  export type AsObject = {
  }
}

export class UseAnyStatusCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyStatusCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyStatusCompositionViewRequest): UseAnyStatusCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyStatusCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyStatusCompositionViewRequest;
  static deserializeBinaryFromReader(message: UseAnyStatusCompositionViewRequest, reader: jspb.BinaryReader): UseAnyStatusCompositionViewRequest;
}

export namespace UseAnyStatusCompositionViewRequest {
  export type AsObject = {
  }
}

export class UseSequesteredCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseSequesteredCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseSequesteredCompositionViewReply): UseSequesteredCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseSequesteredCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseSequesteredCompositionViewReply;
  static deserializeBinaryFromReader(message: UseSequesteredCompositionViewReply, reader: jspb.BinaryReader): UseSequesteredCompositionViewReply;
}

export namespace UseSequesteredCompositionViewReply {
  export type AsObject = {
  }
}

export class UseSequesteredCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseSequesteredCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseSequesteredCompositionViewRequest): UseSequesteredCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseSequesteredCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseSequesteredCompositionViewRequest;
  static deserializeBinaryFromReader(message: UseSequesteredCompositionViewRequest, reader: jspb.BinaryReader): UseSequesteredCompositionViewRequest;
}

export namespace UseSequesteredCompositionViewRequest {
  export type AsObject = {
  }
}

export class UseUnsequesteredCompositionViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseUnsequesteredCompositionViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseUnsequesteredCompositionViewReply): UseUnsequesteredCompositionViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseUnsequesteredCompositionViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseUnsequesteredCompositionViewReply;
  static deserializeBinaryFromReader(message: UseUnsequesteredCompositionViewReply, reader: jspb.BinaryReader): UseUnsequesteredCompositionViewReply;
}

export namespace UseUnsequesteredCompositionViewReply {
  export type AsObject = {
  }
}

export class UseUnsequesteredCompositionViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseUnsequesteredCompositionViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseUnsequesteredCompositionViewRequest): UseUnsequesteredCompositionViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseUnsequesteredCompositionViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseUnsequesteredCompositionViewRequest;
  static deserializeBinaryFromReader(message: UseUnsequesteredCompositionViewRequest, reader: jspb.BinaryReader): UseUnsequesteredCompositionViewRequest;
}

export namespace UseUnsequesteredCompositionViewRequest {
  export type AsObject = {
  }
}

export class GetCompositionReply extends jspb.Message {
  hasComposition(): boolean;
  clearComposition(): void;
  getComposition(): Composition | undefined;
  setComposition(value?: Composition): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionReply): GetCompositionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionReply;
  static deserializeBinaryFromReader(message: GetCompositionReply, reader: jspb.BinaryReader): GetCompositionReply;
}

export namespace GetCompositionReply {
  export type AsObject = {
    composition?: Composition.AsObject,
  }
}

export class GetCompositionRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionRequest): GetCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionRequest;
  static deserializeBinaryFromReader(message: GetCompositionRequest, reader: jspb.BinaryReader): GetCompositionRequest;
}

export namespace GetCompositionRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCompositionsByIdsRequest extends jspb.Message {
  clearCompositionIdsList(): void;
  getCompositionIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setCompositionIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addCompositionIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByIdsRequest): GetCompositionsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByIdsRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByIdsRequest, reader: jspb.BinaryReader): GetCompositionsByIdsRequest;
}

export namespace GetCompositionsByIdsRequest {
  export type AsObject = {
    compositionIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetCompositionsByGenusTypeRequest extends jspb.Message {
  hasCompositionGenusType(): boolean;
  clearCompositionGenusType(): void;
  getCompositionGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCompositionGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByGenusTypeRequest): GetCompositionsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByGenusTypeRequest, reader: jspb.BinaryReader): GetCompositionsByGenusTypeRequest;
}

export namespace GetCompositionsByGenusTypeRequest {
  export type AsObject = {
    compositionGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCompositionsByParentGenusTypeRequest extends jspb.Message {
  hasCompositionGenusType(): boolean;
  clearCompositionGenusType(): void;
  getCompositionGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCompositionGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByParentGenusTypeRequest): GetCompositionsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetCompositionsByParentGenusTypeRequest;
}

export namespace GetCompositionsByParentGenusTypeRequest {
  export type AsObject = {
    compositionGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCompositionsByRecordTypeRequest extends jspb.Message {
  hasCompositionRecordType(): boolean;
  clearCompositionRecordType(): void;
  getCompositionRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCompositionRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByRecordTypeRequest): GetCompositionsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByRecordTypeRequest, reader: jspb.BinaryReader): GetCompositionsByRecordTypeRequest;
}

export namespace GetCompositionsByRecordTypeRequest {
  export type AsObject = {
    compositionRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCompositionsByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByProviderRequest): GetCompositionsByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByProviderRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByProviderRequest, reader: jspb.BinaryReader): GetCompositionsByProviderRequest;
}

export namespace GetCompositionsByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsRequest): GetCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsRequest;
  static deserializeBinaryFromReader(message: GetCompositionsRequest, reader: jspb.BinaryReader): GetCompositionsRequest;
}

export namespace GetCompositionsRequest {
  export type AsObject = {
  }
}

export class CanSearchCompositionsReply extends jspb.Message {
  getCanSearchCompositions(): boolean;
  setCanSearchCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchCompositionsReply): CanSearchCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchCompositionsReply;
  static deserializeBinaryFromReader(message: CanSearchCompositionsReply, reader: jspb.BinaryReader): CanSearchCompositionsReply;
}

export namespace CanSearchCompositionsReply {
  export type AsObject = {
    canSearchCompositions: boolean,
  }
}

export class CanSearchCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchCompositionsRequest): CanSearchCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchCompositionsRequest;
  static deserializeBinaryFromReader(message: CanSearchCompositionsRequest, reader: jspb.BinaryReader): CanSearchCompositionsRequest;
}

export namespace CanSearchCompositionsRequest {
  export type AsObject = {
  }
}

export class GetCompositionQueryReply extends jspb.Message {
  hasCompositionQuery(): boolean;
  clearCompositionQuery(): void;
  getCompositionQuery(): CompositionQuery | undefined;
  setCompositionQuery(value?: CompositionQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionQueryReply): GetCompositionQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionQueryReply;
  static deserializeBinaryFromReader(message: GetCompositionQueryReply, reader: jspb.BinaryReader): GetCompositionQueryReply;
}

export namespace GetCompositionQueryReply {
  export type AsObject = {
    compositionQuery?: CompositionQuery.AsObject,
  }
}

export class GetCompositionQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionQueryRequest): GetCompositionQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionQueryRequest;
  static deserializeBinaryFromReader(message: GetCompositionQueryRequest, reader: jspb.BinaryReader): GetCompositionQueryRequest;
}

export namespace GetCompositionQueryRequest {
  export type AsObject = {
  }
}

export class GetCompositionsByQueryRequest extends jspb.Message {
  hasCompositionQuery(): boolean;
  clearCompositionQuery(): void;
  getCompositionQuery(): CompositionQuery | undefined;
  setCompositionQuery(value?: CompositionQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByQueryRequest): GetCompositionsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByQueryRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByQueryRequest, reader: jspb.BinaryReader): GetCompositionsByQueryRequest;
}

export namespace GetCompositionsByQueryRequest {
  export type AsObject = {
    compositionQuery?: CompositionQuery.AsObject,
  }
}

export class GetCompositionSearchReply extends jspb.Message {
  hasCompositionSearch(): boolean;
  clearCompositionSearch(): void;
  getCompositionSearch(): CompositionSearch | undefined;
  setCompositionSearch(value?: CompositionSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionSearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionSearchReply): GetCompositionSearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionSearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionSearchReply;
  static deserializeBinaryFromReader(message: GetCompositionSearchReply, reader: jspb.BinaryReader): GetCompositionSearchReply;
}

export namespace GetCompositionSearchReply {
  export type AsObject = {
    compositionSearch?: CompositionSearch.AsObject,
  }
}

export class GetCompositionSearchRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionSearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionSearchRequest): GetCompositionSearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionSearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionSearchRequest;
  static deserializeBinaryFromReader(message: GetCompositionSearchRequest, reader: jspb.BinaryReader): GetCompositionSearchRequest;
}

export namespace GetCompositionSearchRequest {
  export type AsObject = {
  }
}

export class GetCompositionSearchOrderReply extends jspb.Message {
  hasCompositionSearchOrder(): boolean;
  clearCompositionSearchOrder(): void;
  getCompositionSearchOrder(): CompositionSearchOrder | undefined;
  setCompositionSearchOrder(value?: CompositionSearchOrder): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionSearchOrderReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionSearchOrderReply): GetCompositionSearchOrderReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionSearchOrderReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionSearchOrderReply;
  static deserializeBinaryFromReader(message: GetCompositionSearchOrderReply, reader: jspb.BinaryReader): GetCompositionSearchOrderReply;
}

export namespace GetCompositionSearchOrderReply {
  export type AsObject = {
    compositionSearchOrder?: CompositionSearchOrder.AsObject,
  }
}

export class GetCompositionSearchOrderRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionSearchOrderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionSearchOrderRequest): GetCompositionSearchOrderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionSearchOrderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionSearchOrderRequest;
  static deserializeBinaryFromReader(message: GetCompositionSearchOrderRequest, reader: jspb.BinaryReader): GetCompositionSearchOrderRequest;
}

export namespace GetCompositionSearchOrderRequest {
  export type AsObject = {
  }
}

export class GetCompositionsBySearchReply extends jspb.Message {
  hasCompositionSearchResults(): boolean;
  clearCompositionSearchResults(): void;
  getCompositionSearchResults(): CompositionSearchResults | undefined;
  setCompositionSearchResults(value?: CompositionSearchResults): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsBySearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsBySearchReply): GetCompositionsBySearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsBySearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsBySearchReply;
  static deserializeBinaryFromReader(message: GetCompositionsBySearchReply, reader: jspb.BinaryReader): GetCompositionsBySearchReply;
}

export namespace GetCompositionsBySearchReply {
  export type AsObject = {
    compositionSearchResults?: CompositionSearchResults.AsObject,
  }
}

export class GetCompositionsBySearchRequest extends jspb.Message {
  hasCompositionQuery(): boolean;
  clearCompositionQuery(): void;
  getCompositionQuery(): CompositionQuery | undefined;
  setCompositionQuery(value?: CompositionQuery): void;

  hasCompositionSearch(): boolean;
  clearCompositionSearch(): void;
  getCompositionSearch(): CompositionSearch | undefined;
  setCompositionSearch(value?: CompositionSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsBySearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsBySearchRequest): GetCompositionsBySearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsBySearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsBySearchRequest;
  static deserializeBinaryFromReader(message: GetCompositionsBySearchRequest, reader: jspb.BinaryReader): GetCompositionsBySearchRequest;
}

export namespace GetCompositionsBySearchRequest {
  export type AsObject = {
    compositionQuery?: CompositionQuery.AsObject,
    compositionSearch?: CompositionSearch.AsObject,
  }
}

export class GetCompositionQueryFromInspectorReply extends jspb.Message {
  hasCompositionQuery(): boolean;
  clearCompositionQuery(): void;
  getCompositionQuery(): CompositionQuery | undefined;
  setCompositionQuery(value?: CompositionQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionQueryFromInspectorReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionQueryFromInspectorReply): GetCompositionQueryFromInspectorReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionQueryFromInspectorReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionQueryFromInspectorReply;
  static deserializeBinaryFromReader(message: GetCompositionQueryFromInspectorReply, reader: jspb.BinaryReader): GetCompositionQueryFromInspectorReply;
}

export namespace GetCompositionQueryFromInspectorReply {
  export type AsObject = {
    compositionQuery?: CompositionQuery.AsObject,
  }
}

export class GetCompositionQueryFromInspectorRequest extends jspb.Message {
  hasCompositionQueryInspector(): boolean;
  clearCompositionQueryInspector(): void;
  getCompositionQueryInspector(): CompositionQueryInspector | undefined;
  setCompositionQueryInspector(value?: CompositionQueryInspector): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionQueryFromInspectorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionQueryFromInspectorRequest): GetCompositionQueryFromInspectorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionQueryFromInspectorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionQueryFromInspectorRequest;
  static deserializeBinaryFromReader(message: GetCompositionQueryFromInspectorRequest, reader: jspb.BinaryReader): GetCompositionQueryFromInspectorRequest;
}

export namespace GetCompositionQueryFromInspectorRequest {
  export type AsObject = {
    compositionQueryInspector?: CompositionQueryInspector.AsObject,
  }
}

export class CanCreateCompositionsReply extends jspb.Message {
  getCanCreateCompositions(): boolean;
  setCanCreateCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCompositionsReply): CanCreateCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCompositionsReply;
  static deserializeBinaryFromReader(message: CanCreateCompositionsReply, reader: jspb.BinaryReader): CanCreateCompositionsReply;
}

export namespace CanCreateCompositionsReply {
  export type AsObject = {
    canCreateCompositions: boolean,
  }
}

export class CanCreateCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCompositionsRequest): CanCreateCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCompositionsRequest;
  static deserializeBinaryFromReader(message: CanCreateCompositionsRequest, reader: jspb.BinaryReader): CanCreateCompositionsRequest;
}

export namespace CanCreateCompositionsRequest {
  export type AsObject = {
  }
}

export class CanCreateCompositionWithRecordTypesReply extends jspb.Message {
  getCanCreateCompositionWithRecordTypes(): boolean;
  setCanCreateCompositionWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCompositionWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCompositionWithRecordTypesReply): CanCreateCompositionWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCompositionWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCompositionWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateCompositionWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateCompositionWithRecordTypesReply;
}

export namespace CanCreateCompositionWithRecordTypesReply {
  export type AsObject = {
    canCreateCompositionWithRecordTypes: boolean,
  }
}

export class CanCreateCompositionWithRecordTypesRequest extends jspb.Message {
  clearCompositionRecordTypesList(): void;
  getCompositionRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setCompositionRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addCompositionRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCompositionWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCompositionWithRecordTypesRequest): CanCreateCompositionWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCompositionWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCompositionWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateCompositionWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateCompositionWithRecordTypesRequest;
}

export namespace CanCreateCompositionWithRecordTypesRequest {
  export type AsObject = {
    compositionRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetCompositionFormForCreateReply extends jspb.Message {
  hasCompositionForm(): boolean;
  clearCompositionForm(): void;
  getCompositionForm(): CompositionForm | undefined;
  setCompositionForm(value?: CompositionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionFormForCreateReply): GetCompositionFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionFormForCreateReply;
  static deserializeBinaryFromReader(message: GetCompositionFormForCreateReply, reader: jspb.BinaryReader): GetCompositionFormForCreateReply;
}

export namespace GetCompositionFormForCreateReply {
  export type AsObject = {
    compositionForm?: CompositionForm.AsObject,
  }
}

export class GetCompositionFormForCreateRequest extends jspb.Message {
  clearCompositionRecordTypesList(): void;
  getCompositionRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setCompositionRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addCompositionRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionFormForCreateRequest): GetCompositionFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetCompositionFormForCreateRequest, reader: jspb.BinaryReader): GetCompositionFormForCreateRequest;
}

export namespace GetCompositionFormForCreateRequest {
  export type AsObject = {
    compositionRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateCompositionReply extends jspb.Message {
  hasComposition(): boolean;
  clearComposition(): void;
  getComposition(): Composition | undefined;
  setComposition(value?: Composition): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateCompositionReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateCompositionReply): CreateCompositionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateCompositionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateCompositionReply;
  static deserializeBinaryFromReader(message: CreateCompositionReply, reader: jspb.BinaryReader): CreateCompositionReply;
}

export namespace CreateCompositionReply {
  export type AsObject = {
    composition?: Composition.AsObject,
  }
}

export class CreateCompositionRequest extends jspb.Message {
  hasComposiitonForm(): boolean;
  clearComposiitonForm(): void;
  getComposiitonForm(): CompositionForm | undefined;
  setComposiitonForm(value?: CompositionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateCompositionRequest): CreateCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateCompositionRequest;
  static deserializeBinaryFromReader(message: CreateCompositionRequest, reader: jspb.BinaryReader): CreateCompositionRequest;
}

export namespace CreateCompositionRequest {
  export type AsObject = {
    composiitonForm?: CompositionForm.AsObject,
  }
}

export class CanUpdateCompositionsReply extends jspb.Message {
  getCanUpdateCompositions(): boolean;
  setCanUpdateCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateCompositionsReply): CanUpdateCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateCompositionsReply;
  static deserializeBinaryFromReader(message: CanUpdateCompositionsReply, reader: jspb.BinaryReader): CanUpdateCompositionsReply;
}

export namespace CanUpdateCompositionsReply {
  export type AsObject = {
    canUpdateCompositions: boolean,
  }
}

export class CanUpdateCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateCompositionsRequest): CanUpdateCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateCompositionsRequest;
  static deserializeBinaryFromReader(message: CanUpdateCompositionsRequest, reader: jspb.BinaryReader): CanUpdateCompositionsRequest;
}

export namespace CanUpdateCompositionsRequest {
  export type AsObject = {
  }
}

export class GetCompositionFormForUpdateReply extends jspb.Message {
  hasCompositionForm(): boolean;
  clearCompositionForm(): void;
  getCompositionForm(): CompositionForm | undefined;
  setCompositionForm(value?: CompositionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionFormForUpdateReply): GetCompositionFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetCompositionFormForUpdateReply, reader: jspb.BinaryReader): GetCompositionFormForUpdateReply;
}

export namespace GetCompositionFormForUpdateReply {
  export type AsObject = {
    compositionForm?: CompositionForm.AsObject,
  }
}

export class GetCompositionFormForUpdateRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionFormForUpdateRequest): GetCompositionFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetCompositionFormForUpdateRequest, reader: jspb.BinaryReader): GetCompositionFormForUpdateRequest;
}

export namespace GetCompositionFormForUpdateRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateCompositionReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateCompositionReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateCompositionReply): UpdateCompositionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateCompositionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateCompositionReply;
  static deserializeBinaryFromReader(message: UpdateCompositionReply, reader: jspb.BinaryReader): UpdateCompositionReply;
}

export namespace UpdateCompositionReply {
  export type AsObject = {
  }
}

export class UpdateCompositionRequest extends jspb.Message {
  hasComposiitonForm(): boolean;
  clearComposiitonForm(): void;
  getComposiitonForm(): CompositionForm | undefined;
  setComposiitonForm(value?: CompositionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateCompositionRequest): UpdateCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateCompositionRequest;
  static deserializeBinaryFromReader(message: UpdateCompositionRequest, reader: jspb.BinaryReader): UpdateCompositionRequest;
}

export namespace UpdateCompositionRequest {
  export type AsObject = {
    composiitonForm?: CompositionForm.AsObject,
  }
}

export class CanDeleteCompositionsReply extends jspb.Message {
  getCanDeleteCompositions(): boolean;
  setCanDeleteCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteCompositionsReply): CanDeleteCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteCompositionsReply;
  static deserializeBinaryFromReader(message: CanDeleteCompositionsReply, reader: jspb.BinaryReader): CanDeleteCompositionsReply;
}

export namespace CanDeleteCompositionsReply {
  export type AsObject = {
    canDeleteCompositions: boolean,
  }
}

export class CanDeleteCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteCompositionsRequest): CanDeleteCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteCompositionsRequest;
  static deserializeBinaryFromReader(message: CanDeleteCompositionsRequest, reader: jspb.BinaryReader): CanDeleteCompositionsRequest;
}

export namespace CanDeleteCompositionsRequest {
  export type AsObject = {
  }
}

export class DeleteCompositionReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCompositionReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCompositionReply): DeleteCompositionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCompositionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCompositionReply;
  static deserializeBinaryFromReader(message: DeleteCompositionReply, reader: jspb.BinaryReader): DeleteCompositionReply;
}

export namespace DeleteCompositionReply {
  export type AsObject = {
  }
}

export class DeleteCompositionRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCompositionRequest): DeleteCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCompositionRequest;
  static deserializeBinaryFromReader(message: DeleteCompositionRequest, reader: jspb.BinaryReader): DeleteCompositionRequest;
}

export namespace DeleteCompositionRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class DeleteCompositionNodeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCompositionNodeReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCompositionNodeReply): DeleteCompositionNodeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCompositionNodeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCompositionNodeReply;
  static deserializeBinaryFromReader(message: DeleteCompositionNodeReply, reader: jspb.BinaryReader): DeleteCompositionNodeReply;
}

export namespace DeleteCompositionNodeReply {
  export type AsObject = {
  }
}

export class DeleteCompositionNodeRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCompositionNodeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCompositionNodeRequest): DeleteCompositionNodeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCompositionNodeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCompositionNodeRequest;
  static deserializeBinaryFromReader(message: DeleteCompositionNodeRequest, reader: jspb.BinaryReader): DeleteCompositionNodeRequest;
}

export namespace DeleteCompositionNodeRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddCompositionChildReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddCompositionChildReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddCompositionChildReply): AddCompositionChildReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddCompositionChildReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddCompositionChildReply;
  static deserializeBinaryFromReader(message: AddCompositionChildReply, reader: jspb.BinaryReader): AddCompositionChildReply;
}

export namespace AddCompositionChildReply {
  export type AsObject = {
  }
}

export class AddCompositionChildRequest extends jspb.Message {
  hasChildCompositionId(): boolean;
  clearChildCompositionId(): void;
  getChildCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddCompositionChildRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddCompositionChildRequest): AddCompositionChildRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddCompositionChildRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddCompositionChildRequest;
  static deserializeBinaryFromReader(message: AddCompositionChildRequest, reader: jspb.BinaryReader): AddCompositionChildRequest;
}

export namespace AddCompositionChildRequest {
  export type AsObject = {
    childCompositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveCompositionChildReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveCompositionChildReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveCompositionChildReply): RemoveCompositionChildReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveCompositionChildReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveCompositionChildReply;
  static deserializeBinaryFromReader(message: RemoveCompositionChildReply, reader: jspb.BinaryReader): RemoveCompositionChildReply;
}

export namespace RemoveCompositionChildReply {
  export type AsObject = {
  }
}

export class RemoveCompositionChildRequest extends jspb.Message {
  hasChildCompositionId(): boolean;
  clearChildCompositionId(): void;
  getChildCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveCompositionChildRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveCompositionChildRequest): RemoveCompositionChildRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveCompositionChildRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveCompositionChildRequest;
  static deserializeBinaryFromReader(message: RemoveCompositionChildRequest, reader: jspb.BinaryReader): RemoveCompositionChildRequest;
}

export namespace RemoveCompositionChildRequest {
  export type AsObject = {
    childCompositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageCompositionAliasesReply extends jspb.Message {
  getCanManageCompositionAliases(): boolean;
  setCanManageCompositionAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageCompositionAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageCompositionAliasesReply): CanManageCompositionAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageCompositionAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageCompositionAliasesReply;
  static deserializeBinaryFromReader(message: CanManageCompositionAliasesReply, reader: jspb.BinaryReader): CanManageCompositionAliasesReply;
}

export namespace CanManageCompositionAliasesReply {
  export type AsObject = {
    canManageCompositionAliases: boolean,
  }
}

export class CanManageCompositionAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageCompositionAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageCompositionAliasesRequest): CanManageCompositionAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageCompositionAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageCompositionAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageCompositionAliasesRequest, reader: jspb.BinaryReader): CanManageCompositionAliasesRequest;
}

export namespace CanManageCompositionAliasesRequest {
  export type AsObject = {
  }
}

export class AliasCompositionReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasCompositionReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasCompositionReply): AliasCompositionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasCompositionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasCompositionReply;
  static deserializeBinaryFromReader(message: AliasCompositionReply, reader: jspb.BinaryReader): AliasCompositionReply;
}

export namespace AliasCompositionReply {
  export type AsObject = {
  }
}

export class AliasCompositionRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasCompositionRequest): AliasCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasCompositionRequest;
  static deserializeBinaryFromReader(message: AliasCompositionRequest, reader: jspb.BinaryReader): AliasCompositionRequest;
}

export namespace AliasCompositionRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UseComparativeCompositionRepositoryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCompositionRepositoryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCompositionRepositoryViewReply): UseComparativeCompositionRepositoryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCompositionRepositoryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCompositionRepositoryViewReply;
  static deserializeBinaryFromReader(message: UseComparativeCompositionRepositoryViewReply, reader: jspb.BinaryReader): UseComparativeCompositionRepositoryViewReply;
}

export namespace UseComparativeCompositionRepositoryViewReply {
  export type AsObject = {
  }
}

export class UseComparativeCompositionRepositoryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCompositionRepositoryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCompositionRepositoryViewRequest): UseComparativeCompositionRepositoryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCompositionRepositoryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCompositionRepositoryViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeCompositionRepositoryViewRequest, reader: jspb.BinaryReader): UseComparativeCompositionRepositoryViewRequest;
}

export namespace UseComparativeCompositionRepositoryViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryCompositionRepositoryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCompositionRepositoryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCompositionRepositoryViewReply): UsePlenaryCompositionRepositoryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCompositionRepositoryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCompositionRepositoryViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryCompositionRepositoryViewReply, reader: jspb.BinaryReader): UsePlenaryCompositionRepositoryViewReply;
}

export namespace UsePlenaryCompositionRepositoryViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryCompositionRepositoryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCompositionRepositoryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCompositionRepositoryViewRequest): UsePlenaryCompositionRepositoryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCompositionRepositoryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCompositionRepositoryViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryCompositionRepositoryViewRequest, reader: jspb.BinaryReader): UsePlenaryCompositionRepositoryViewRequest;
}

export namespace UsePlenaryCompositionRepositoryViewRequest {
  export type AsObject = {
  }
}

export class CanLookupCompositionRepositoryMappingsReply extends jspb.Message {
  getCanLookupCompositionRepositoryMappings(): boolean;
  setCanLookupCompositionRepositoryMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCompositionRepositoryMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCompositionRepositoryMappingsReply): CanLookupCompositionRepositoryMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCompositionRepositoryMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCompositionRepositoryMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupCompositionRepositoryMappingsReply, reader: jspb.BinaryReader): CanLookupCompositionRepositoryMappingsReply;
}

export namespace CanLookupCompositionRepositoryMappingsReply {
  export type AsObject = {
    canLookupCompositionRepositoryMappings: boolean,
  }
}

export class CanLookupCompositionRepositoryMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCompositionRepositoryMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCompositionRepositoryMappingsRequest): CanLookupCompositionRepositoryMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCompositionRepositoryMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCompositionRepositoryMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupCompositionRepositoryMappingsRequest, reader: jspb.BinaryReader): CanLookupCompositionRepositoryMappingsRequest;
}

export namespace CanLookupCompositionRepositoryMappingsRequest {
  export type AsObject = {
  }
}

export class GetCompositionIdsByRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionIdsByRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionIdsByRepositoryRequest): GetCompositionIdsByRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionIdsByRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionIdsByRepositoryRequest;
  static deserializeBinaryFromReader(message: GetCompositionIdsByRepositoryRequest, reader: jspb.BinaryReader): GetCompositionIdsByRepositoryRequest;
}

export namespace GetCompositionIdsByRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCompositionsByRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByRepositoryRequest): GetCompositionsByRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByRepositoryRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByRepositoryRequest, reader: jspb.BinaryReader): GetCompositionsByRepositoryRequest;
}

export namespace GetCompositionsByRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCompositionIdsByRepositoriesRequest extends jspb.Message {
  clearRepositoryIdsList(): void;
  getRepositoryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setRepositoryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addRepositoryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionIdsByRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionIdsByRepositoriesRequest): GetCompositionIdsByRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionIdsByRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionIdsByRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetCompositionIdsByRepositoriesRequest, reader: jspb.BinaryReader): GetCompositionIdsByRepositoriesRequest;
}

export namespace GetCompositionIdsByRepositoriesRequest {
  export type AsObject = {
    repositoryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetCompositionsByRepositoriesRequest extends jspb.Message {
  clearRepositoryIdsList(): void;
  getRepositoryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setRepositoryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addRepositoryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCompositionsByRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCompositionsByRepositoriesRequest): GetCompositionsByRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCompositionsByRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCompositionsByRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetCompositionsByRepositoriesRequest, reader: jspb.BinaryReader): GetCompositionsByRepositoriesRequest;
}

export namespace GetCompositionsByRepositoriesRequest {
  export type AsObject = {
    repositoryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetRepositoryIdsByCompositionRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryIdsByCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryIdsByCompositionRequest): GetRepositoryIdsByCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryIdsByCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryIdsByCompositionRequest;
  static deserializeBinaryFromReader(message: GetRepositoryIdsByCompositionRequest, reader: jspb.BinaryReader): GetRepositoryIdsByCompositionRequest;
}

export namespace GetRepositoryIdsByCompositionRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoriesByCompositionRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByCompositionRequest): GetRepositoriesByCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByCompositionRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByCompositionRequest, reader: jspb.BinaryReader): GetRepositoriesByCompositionRequest;
}

export namespace GetRepositoriesByCompositionRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignCompositionsReply extends jspb.Message {
  getCanAssignCompositions(): boolean;
  setCanAssignCompositions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCompositionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCompositionsReply): CanAssignCompositionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCompositionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCompositionsReply;
  static deserializeBinaryFromReader(message: CanAssignCompositionsReply, reader: jspb.BinaryReader): CanAssignCompositionsReply;
}

export namespace CanAssignCompositionsReply {
  export type AsObject = {
    canAssignCompositions: boolean,
  }
}

export class CanAssignCompositionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCompositionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCompositionsRequest): CanAssignCompositionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCompositionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCompositionsRequest;
  static deserializeBinaryFromReader(message: CanAssignCompositionsRequest, reader: jspb.BinaryReader): CanAssignCompositionsRequest;
}

export namespace CanAssignCompositionsRequest {
  export type AsObject = {
  }
}

export class CanAssignCompositionsToRepositoryReply extends jspb.Message {
  getCanAssignCompositionsToRepository(): boolean;
  setCanAssignCompositionsToRepository(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCompositionsToRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCompositionsToRepositoryReply): CanAssignCompositionsToRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCompositionsToRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCompositionsToRepositoryReply;
  static deserializeBinaryFromReader(message: CanAssignCompositionsToRepositoryReply, reader: jspb.BinaryReader): CanAssignCompositionsToRepositoryReply;
}

export namespace CanAssignCompositionsToRepositoryReply {
  export type AsObject = {
    canAssignCompositionsToRepository: boolean,
  }
}

export class CanAssignCompositionsToRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCompositionsToRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCompositionsToRepositoryRequest): CanAssignCompositionsToRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCompositionsToRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCompositionsToRepositoryRequest;
  static deserializeBinaryFromReader(message: CanAssignCompositionsToRepositoryRequest, reader: jspb.BinaryReader): CanAssignCompositionsToRepositoryRequest;
}

export namespace CanAssignCompositionsToRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableRepositoryIdsForCompositionRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableRepositoryIdsForCompositionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableRepositoryIdsForCompositionRequest): GetAssignableRepositoryIdsForCompositionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableRepositoryIdsForCompositionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableRepositoryIdsForCompositionRequest;
  static deserializeBinaryFromReader(message: GetAssignableRepositoryIdsForCompositionRequest, reader: jspb.BinaryReader): GetAssignableRepositoryIdsForCompositionRequest;
}

export namespace GetAssignableRepositoryIdsForCompositionRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignCompositionToRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignCompositionToRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignCompositionToRepositoryReply): AssignCompositionToRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignCompositionToRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignCompositionToRepositoryReply;
  static deserializeBinaryFromReader(message: AssignCompositionToRepositoryReply, reader: jspb.BinaryReader): AssignCompositionToRepositoryReply;
}

export namespace AssignCompositionToRepositoryReply {
  export type AsObject = {
  }
}

export class AssignCompositionToRepositoryRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignCompositionToRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignCompositionToRepositoryRequest): AssignCompositionToRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignCompositionToRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignCompositionToRepositoryRequest;
  static deserializeBinaryFromReader(message: AssignCompositionToRepositoryRequest, reader: jspb.BinaryReader): AssignCompositionToRepositoryRequest;
}

export namespace AssignCompositionToRepositoryRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignCompositionFromRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignCompositionFromRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignCompositionFromRepositoryReply): UnassignCompositionFromRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignCompositionFromRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignCompositionFromRepositoryReply;
  static deserializeBinaryFromReader(message: UnassignCompositionFromRepositoryReply, reader: jspb.BinaryReader): UnassignCompositionFromRepositoryReply;
}

export namespace UnassignCompositionFromRepositoryReply {
  export type AsObject = {
  }
}

export class UnassignCompositionFromRepositoryRequest extends jspb.Message {
  hasCompositionId(): boolean;
  clearCompositionId(): void;
  getCompositionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCompositionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignCompositionFromRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignCompositionFromRepositoryRequest): UnassignCompositionFromRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignCompositionFromRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignCompositionFromRepositoryRequest;
  static deserializeBinaryFromReader(message: UnassignCompositionFromRepositoryRequest, reader: jspb.BinaryReader): UnassignCompositionFromRepositoryRequest;
}

export namespace UnassignCompositionFromRepositoryRequest {
  export type AsObject = {
    compositionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupRepositoriesReply extends jspb.Message {
  getCanLookupRepositories(): boolean;
  setCanLookupRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupRepositoriesReply): CanLookupRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupRepositoriesReply;
  static deserializeBinaryFromReader(message: CanLookupRepositoriesReply, reader: jspb.BinaryReader): CanLookupRepositoriesReply;
}

export namespace CanLookupRepositoriesReply {
  export type AsObject = {
    canLookupRepositories: boolean,
  }
}

export class CanLookupRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupRepositoriesRequest): CanLookupRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupRepositoriesRequest;
  static deserializeBinaryFromReader(message: CanLookupRepositoriesRequest, reader: jspb.BinaryReader): CanLookupRepositoriesRequest;
}

export namespace CanLookupRepositoriesRequest {
  export type AsObject = {
  }
}

export class GetRepositoriesByIdsRequest extends jspb.Message {
  clearRepositoryIdsList(): void;
  getRepositoryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setRepositoryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addRepositoryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByIdsRequest): GetRepositoriesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByIdsRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByIdsRequest, reader: jspb.BinaryReader): GetRepositoriesByIdsRequest;
}

export namespace GetRepositoriesByIdsRequest {
  export type AsObject = {
    repositoryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetRepositoriesByGenusTypeRequest extends jspb.Message {
  hasRepositoryGenusType(): boolean;
  clearRepositoryGenusType(): void;
  getRepositoryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRepositoryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByGenusTypeRequest): GetRepositoriesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByGenusTypeRequest, reader: jspb.BinaryReader): GetRepositoriesByGenusTypeRequest;
}

export namespace GetRepositoriesByGenusTypeRequest {
  export type AsObject = {
    repositoryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRepositoriesByParentGenusTypeRequest extends jspb.Message {
  hasRepositoryGenusType(): boolean;
  clearRepositoryGenusType(): void;
  getRepositoryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRepositoryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByParentGenusTypeRequest): GetRepositoriesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetRepositoriesByParentGenusTypeRequest;
}

export namespace GetRepositoriesByParentGenusTypeRequest {
  export type AsObject = {
    repositoryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRepositoriesByRecordTypeRequest extends jspb.Message {
  hasRepositoryRecordType(): boolean;
  clearRepositoryRecordType(): void;
  getRepositoryRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRepositoryRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByRecordTypeRequest): GetRepositoriesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByRecordTypeRequest, reader: jspb.BinaryReader): GetRepositoriesByRecordTypeRequest;
}

export namespace GetRepositoriesByRecordTypeRequest {
  export type AsObject = {
    repositoryRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRepositoriesByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByProviderRequest): GetRepositoriesByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByProviderRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByProviderRequest, reader: jspb.BinaryReader): GetRepositoriesByProviderRequest;
}

export namespace GetRepositoriesByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesRequest): GetRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesRequest, reader: jspb.BinaryReader): GetRepositoriesRequest;
}

export namespace GetRepositoriesRequest {
  export type AsObject = {
  }
}

export class CanSearchRepositoriesReply extends jspb.Message {
  getCanSearchRepositories(): boolean;
  setCanSearchRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchRepositoriesReply): CanSearchRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchRepositoriesReply;
  static deserializeBinaryFromReader(message: CanSearchRepositoriesReply, reader: jspb.BinaryReader): CanSearchRepositoriesReply;
}

export namespace CanSearchRepositoriesReply {
  export type AsObject = {
    canSearchRepositories: boolean,
  }
}

export class CanSearchRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchRepositoriesRequest): CanSearchRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchRepositoriesRequest;
  static deserializeBinaryFromReader(message: CanSearchRepositoriesRequest, reader: jspb.BinaryReader): CanSearchRepositoriesRequest;
}

export namespace CanSearchRepositoriesRequest {
  export type AsObject = {
  }
}

export class GetRepositoryQueryReply extends jspb.Message {
  hasRepositoryQuery(): boolean;
  clearRepositoryQuery(): void;
  getRepositoryQuery(): RepositoryQuery | undefined;
  setRepositoryQuery(value?: RepositoryQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryQueryReply): GetRepositoryQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryQueryReply;
  static deserializeBinaryFromReader(message: GetRepositoryQueryReply, reader: jspb.BinaryReader): GetRepositoryQueryReply;
}

export namespace GetRepositoryQueryReply {
  export type AsObject = {
    repositoryQuery?: RepositoryQuery.AsObject,
  }
}

export class GetRepositoryQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryQueryRequest): GetRepositoryQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryQueryRequest;
  static deserializeBinaryFromReader(message: GetRepositoryQueryRequest, reader: jspb.BinaryReader): GetRepositoryQueryRequest;
}

export namespace GetRepositoryQueryRequest {
  export type AsObject = {
  }
}

export class GetRepositoriesByQueryRequest extends jspb.Message {
  hasRepositoryQuery(): boolean;
  clearRepositoryQuery(): void;
  getRepositoryQuery(): RepositoryQuery | undefined;
  setRepositoryQuery(value?: RepositoryQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoriesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoriesByQueryRequest): GetRepositoriesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoriesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoriesByQueryRequest;
  static deserializeBinaryFromReader(message: GetRepositoriesByQueryRequest, reader: jspb.BinaryReader): GetRepositoriesByQueryRequest;
}

export namespace GetRepositoriesByQueryRequest {
  export type AsObject = {
    repositoryQuery?: RepositoryQuery.AsObject,
  }
}

export class CanCreateRepositoriesReply extends jspb.Message {
  getCanCreateRepositories(): boolean;
  setCanCreateRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRepositoriesReply): CanCreateRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRepositoriesReply;
  static deserializeBinaryFromReader(message: CanCreateRepositoriesReply, reader: jspb.BinaryReader): CanCreateRepositoriesReply;
}

export namespace CanCreateRepositoriesReply {
  export type AsObject = {
    canCreateRepositories: boolean,
  }
}

export class CanCreateRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRepositoriesRequest): CanCreateRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRepositoriesRequest;
  static deserializeBinaryFromReader(message: CanCreateRepositoriesRequest, reader: jspb.BinaryReader): CanCreateRepositoriesRequest;
}

export namespace CanCreateRepositoriesRequest {
  export type AsObject = {
  }
}

export class CanCreateRepositoryWithRecordTypesReply extends jspb.Message {
  getCanCreateRepositoryWithRecordTypes(): boolean;
  setCanCreateRepositoryWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRepositoryWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRepositoryWithRecordTypesReply): CanCreateRepositoryWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRepositoryWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRepositoryWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateRepositoryWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateRepositoryWithRecordTypesReply;
}

export namespace CanCreateRepositoryWithRecordTypesReply {
  export type AsObject = {
    canCreateRepositoryWithRecordTypes: boolean,
  }
}

export class CanCreateRepositoryWithRecordTypesRequest extends jspb.Message {
  clearRepositoryRecordTypesList(): void;
  getRepositoryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRepositoryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRepositoryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRepositoryWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRepositoryWithRecordTypesRequest): CanCreateRepositoryWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRepositoryWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRepositoryWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateRepositoryWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateRepositoryWithRecordTypesRequest;
}

export namespace CanCreateRepositoryWithRecordTypesRequest {
  export type AsObject = {
    repositoryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetRepositoryFormForCreateReply extends jspb.Message {
  hasRepositoryForm(): boolean;
  clearRepositoryForm(): void;
  getRepositoryForm(): RepositoryForm | undefined;
  setRepositoryForm(value?: RepositoryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryFormForCreateReply): GetRepositoryFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryFormForCreateReply;
  static deserializeBinaryFromReader(message: GetRepositoryFormForCreateReply, reader: jspb.BinaryReader): GetRepositoryFormForCreateReply;
}

export namespace GetRepositoryFormForCreateReply {
  export type AsObject = {
    repositoryForm?: RepositoryForm.AsObject,
  }
}

export class GetRepositoryFormForCreateRequest extends jspb.Message {
  clearRepositoryRecordTypesList(): void;
  getRepositoryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRepositoryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRepositoryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryFormForCreateRequest): GetRepositoryFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetRepositoryFormForCreateRequest, reader: jspb.BinaryReader): GetRepositoryFormForCreateRequest;
}

export namespace GetRepositoryFormForCreateRequest {
  export type AsObject = {
    repositoryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateRepositoryReply extends jspb.Message {
  hasRepository(): boolean;
  clearRepository(): void;
  getRepository(): Repository | undefined;
  setRepository(value?: Repository): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateRepositoryReply): CreateRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateRepositoryReply;
  static deserializeBinaryFromReader(message: CreateRepositoryReply, reader: jspb.BinaryReader): CreateRepositoryReply;
}

export namespace CreateRepositoryReply {
  export type AsObject = {
    repository?: Repository.AsObject,
  }
}

export class CreateRepositoryRequest extends jspb.Message {
  hasRepositoryForm(): boolean;
  clearRepositoryForm(): void;
  getRepositoryForm(): RepositoryForm | undefined;
  setRepositoryForm(value?: RepositoryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateRepositoryRequest): CreateRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateRepositoryRequest;
  static deserializeBinaryFromReader(message: CreateRepositoryRequest, reader: jspb.BinaryReader): CreateRepositoryRequest;
}

export namespace CreateRepositoryRequest {
  export type AsObject = {
    repositoryForm?: RepositoryForm.AsObject,
  }
}

export class CanUpdateRepositoriesReply extends jspb.Message {
  getCanUpdateRepositories(): boolean;
  setCanUpdateRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateRepositoriesReply): CanUpdateRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateRepositoriesReply;
  static deserializeBinaryFromReader(message: CanUpdateRepositoriesReply, reader: jspb.BinaryReader): CanUpdateRepositoriesReply;
}

export namespace CanUpdateRepositoriesReply {
  export type AsObject = {
    canUpdateRepositories: boolean,
  }
}

export class CanUpdateRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateRepositoriesRequest): CanUpdateRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateRepositoriesRequest;
  static deserializeBinaryFromReader(message: CanUpdateRepositoriesRequest, reader: jspb.BinaryReader): CanUpdateRepositoriesRequest;
}

export namespace CanUpdateRepositoriesRequest {
  export type AsObject = {
  }
}

export class GetRepositoryFormForUpdateReply extends jspb.Message {
  hasRepositoryForm(): boolean;
  clearRepositoryForm(): void;
  getRepositoryForm(): RepositoryForm | undefined;
  setRepositoryForm(value?: RepositoryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryFormForUpdateReply): GetRepositoryFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetRepositoryFormForUpdateReply, reader: jspb.BinaryReader): GetRepositoryFormForUpdateReply;
}

export namespace GetRepositoryFormForUpdateReply {
  export type AsObject = {
    repositoryForm?: RepositoryForm.AsObject,
  }
}

export class GetRepositoryFormForUpdateRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryFormForUpdateRequest): GetRepositoryFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetRepositoryFormForUpdateRequest, reader: jspb.BinaryReader): GetRepositoryFormForUpdateRequest;
}

export namespace GetRepositoryFormForUpdateRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRepositoryReply): UpdateRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRepositoryReply;
  static deserializeBinaryFromReader(message: UpdateRepositoryReply, reader: jspb.BinaryReader): UpdateRepositoryReply;
}

export namespace UpdateRepositoryReply {
  export type AsObject = {
  }
}

export class UpdateRepositoryRequest extends jspb.Message {
  hasRepositoryForm(): boolean;
  clearRepositoryForm(): void;
  getRepositoryForm(): RepositoryForm | undefined;
  setRepositoryForm(value?: RepositoryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRepositoryRequest): UpdateRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRepositoryRequest;
  static deserializeBinaryFromReader(message: UpdateRepositoryRequest, reader: jspb.BinaryReader): UpdateRepositoryRequest;
}

export namespace UpdateRepositoryRequest {
  export type AsObject = {
    repositoryForm?: RepositoryForm.AsObject,
  }
}

export class CanDeleteRepositoriesReply extends jspb.Message {
  getCanDeleteRepositories(): boolean;
  setCanDeleteRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteRepositoriesReply): CanDeleteRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteRepositoriesReply;
  static deserializeBinaryFromReader(message: CanDeleteRepositoriesReply, reader: jspb.BinaryReader): CanDeleteRepositoriesReply;
}

export namespace CanDeleteRepositoriesReply {
  export type AsObject = {
    canDeleteRepositories: boolean,
  }
}

export class CanDeleteRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteRepositoriesRequest): CanDeleteRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteRepositoriesRequest;
  static deserializeBinaryFromReader(message: CanDeleteRepositoriesRequest, reader: jspb.BinaryReader): CanDeleteRepositoriesRequest;
}

export namespace CanDeleteRepositoriesRequest {
  export type AsObject = {
  }
}

export class DeleteRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteRepositoryReply): DeleteRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteRepositoryReply;
  static deserializeBinaryFromReader(message: DeleteRepositoryReply, reader: jspb.BinaryReader): DeleteRepositoryReply;
}

export namespace DeleteRepositoryReply {
  export type AsObject = {
  }
}

export class DeleteRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteRepositoryRequest): DeleteRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteRepositoryRequest;
  static deserializeBinaryFromReader(message: DeleteRepositoryRequest, reader: jspb.BinaryReader): DeleteRepositoryRequest;
}

export namespace DeleteRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageRepositoryAliasesReply extends jspb.Message {
  getCanManageRepositoryAliases(): boolean;
  setCanManageRepositoryAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageRepositoryAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageRepositoryAliasesReply): CanManageRepositoryAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageRepositoryAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageRepositoryAliasesReply;
  static deserializeBinaryFromReader(message: CanManageRepositoryAliasesReply, reader: jspb.BinaryReader): CanManageRepositoryAliasesReply;
}

export namespace CanManageRepositoryAliasesReply {
  export type AsObject = {
    canManageRepositoryAliases: boolean,
  }
}

export class CanManageRepositoryAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageRepositoryAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageRepositoryAliasesRequest): CanManageRepositoryAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageRepositoryAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageRepositoryAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageRepositoryAliasesRequest, reader: jspb.BinaryReader): CanManageRepositoryAliasesRequest;
}

export namespace CanManageRepositoryAliasesRequest {
  export type AsObject = {
  }
}

export class AliasRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasRepositoryReply): AliasRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasRepositoryReply;
  static deserializeBinaryFromReader(message: AliasRepositoryReply, reader: jspb.BinaryReader): AliasRepositoryReply;
}

export namespace AliasRepositoryReply {
  export type AsObject = {
  }
}

export class AliasRepositoryRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasRepositoryRequest): AliasRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasRepositoryRequest;
  static deserializeBinaryFromReader(message: AliasRepositoryRequest, reader: jspb.BinaryReader): AliasRepositoryRequest;
}

export namespace AliasRepositoryRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoryHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryHierarchyIdReply): GetRepositoryHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetRepositoryHierarchyIdReply, reader: jspb.BinaryReader): GetRepositoryHierarchyIdReply;
}

export namespace GetRepositoryHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoryHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryHierarchyIdRequest): GetRepositoryHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetRepositoryHierarchyIdRequest, reader: jspb.BinaryReader): GetRepositoryHierarchyIdRequest;
}

export namespace GetRepositoryHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetRepositoryHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryHierarchyReply): GetRepositoryHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryHierarchyReply;
  static deserializeBinaryFromReader(message: GetRepositoryHierarchyReply, reader: jspb.BinaryReader): GetRepositoryHierarchyReply;
}

export namespace GetRepositoryHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetRepositoryHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryHierarchyRequest): GetRepositoryHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryHierarchyRequest;
  static deserializeBinaryFromReader(message: GetRepositoryHierarchyRequest, reader: jspb.BinaryReader): GetRepositoryHierarchyRequest;
}

export namespace GetRepositoryHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessRepositoryHierarchyReply extends jspb.Message {
  getCanAccessRepositoryHierarchy(): boolean;
  setCanAccessRepositoryHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessRepositoryHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessRepositoryHierarchyReply): CanAccessRepositoryHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessRepositoryHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessRepositoryHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessRepositoryHierarchyReply, reader: jspb.BinaryReader): CanAccessRepositoryHierarchyReply;
}

export namespace CanAccessRepositoryHierarchyReply {
  export type AsObject = {
    canAccessRepositoryHierarchy: boolean,
  }
}

export class CanAccessRepositoryHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessRepositoryHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessRepositoryHierarchyRequest): CanAccessRepositoryHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessRepositoryHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessRepositoryHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessRepositoryHierarchyRequest, reader: jspb.BinaryReader): CanAccessRepositoryHierarchyRequest;
}

export namespace CanAccessRepositoryHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootRepositoryIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootRepositoryIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootRepositoryIdsRequest): GetRootRepositoryIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootRepositoryIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootRepositoryIdsRequest;
  static deserializeBinaryFromReader(message: GetRootRepositoryIdsRequest, reader: jspb.BinaryReader): GetRootRepositoryIdsRequest;
}

export namespace GetRootRepositoryIdsRequest {
  export type AsObject = {
  }
}

export class GetRootRepositoriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootRepositoriesRequest): GetRootRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetRootRepositoriesRequest, reader: jspb.BinaryReader): GetRootRepositoriesRequest;
}

export namespace GetRootRepositoriesRequest {
  export type AsObject = {
  }
}

export class HasParentRepositoriesReply extends jspb.Message {
  getHasParentRepositories(): boolean;
  setHasParentRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentRepositoriesReply): HasParentRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentRepositoriesReply;
  static deserializeBinaryFromReader(message: HasParentRepositoriesReply, reader: jspb.BinaryReader): HasParentRepositoriesReply;
}

export namespace HasParentRepositoriesReply {
  export type AsObject = {
    hasParentRepositories: boolean,
  }
}

export class HasParentRepositoriesRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentRepositoriesRequest): HasParentRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentRepositoriesRequest;
  static deserializeBinaryFromReader(message: HasParentRepositoriesRequest, reader: jspb.BinaryReader): HasParentRepositoriesRequest;
}

export namespace HasParentRepositoriesRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfRepositoryReply extends jspb.Message {
  getIsParentOfRepository(): boolean;
  setIsParentOfRepository(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfRepositoryReply): IsParentOfRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfRepositoryReply;
  static deserializeBinaryFromReader(message: IsParentOfRepositoryReply, reader: jspb.BinaryReader): IsParentOfRepositoryReply;
}

export namespace IsParentOfRepositoryReply {
  export type AsObject = {
    isParentOfRepository: boolean,
  }
}

export class IsParentOfRepositoryRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfRepositoryRequest): IsParentOfRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfRepositoryRequest;
  static deserializeBinaryFromReader(message: IsParentOfRepositoryRequest, reader: jspb.BinaryReader): IsParentOfRepositoryRequest;
}

export namespace IsParentOfRepositoryRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentRepositoryIdsRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentRepositoryIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentRepositoryIdsRequest): GetParentRepositoryIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentRepositoryIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentRepositoryIdsRequest;
  static deserializeBinaryFromReader(message: GetParentRepositoryIdsRequest, reader: jspb.BinaryReader): GetParentRepositoryIdsRequest;
}

export namespace GetParentRepositoryIdsRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentRepositoriesRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentRepositoriesRequest): GetParentRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetParentRepositoriesRequest, reader: jspb.BinaryReader): GetParentRepositoriesRequest;
}

export namespace GetParentRepositoriesRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfRepositoryReply extends jspb.Message {
  getIsAncestorOfRepository(): boolean;
  setIsAncestorOfRepository(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfRepositoryReply): IsAncestorOfRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfRepositoryReply;
  static deserializeBinaryFromReader(message: IsAncestorOfRepositoryReply, reader: jspb.BinaryReader): IsAncestorOfRepositoryReply;
}

export namespace IsAncestorOfRepositoryReply {
  export type AsObject = {
    isAncestorOfRepository: boolean,
  }
}

export class IsAncestorOfRepositoryRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfRepositoryRequest): IsAncestorOfRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfRepositoryRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfRepositoryRequest, reader: jspb.BinaryReader): IsAncestorOfRepositoryRequest;
}

export namespace IsAncestorOfRepositoryRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildRepositoriesReply extends jspb.Message {
  getHasChildRepositories(): boolean;
  setHasChildRepositories(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildRepositoriesReply): HasChildRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildRepositoriesReply;
  static deserializeBinaryFromReader(message: HasChildRepositoriesReply, reader: jspb.BinaryReader): HasChildRepositoriesReply;
}

export namespace HasChildRepositoriesReply {
  export type AsObject = {
    hasChildRepositories: boolean,
  }
}

export class HasChildRepositoriesRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildRepositoriesRequest): HasChildRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildRepositoriesRequest;
  static deserializeBinaryFromReader(message: HasChildRepositoriesRequest, reader: jspb.BinaryReader): HasChildRepositoriesRequest;
}

export namespace HasChildRepositoriesRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfRepositoryReply extends jspb.Message {
  getIsChildOfRepository(): boolean;
  setIsChildOfRepository(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfRepositoryReply): IsChildOfRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfRepositoryReply;
  static deserializeBinaryFromReader(message: IsChildOfRepositoryReply, reader: jspb.BinaryReader): IsChildOfRepositoryReply;
}

export namespace IsChildOfRepositoryReply {
  export type AsObject = {
    isChildOfRepository: boolean,
  }
}

export class IsChildOfRepositoryRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfRepositoryRequest): IsChildOfRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfRepositoryRequest;
  static deserializeBinaryFromReader(message: IsChildOfRepositoryRequest, reader: jspb.BinaryReader): IsChildOfRepositoryRequest;
}

export namespace IsChildOfRepositoryRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildRepositoryIdsRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildRepositoryIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildRepositoryIdsRequest): GetChildRepositoryIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildRepositoryIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildRepositoryIdsRequest;
  static deserializeBinaryFromReader(message: GetChildRepositoryIdsRequest, reader: jspb.BinaryReader): GetChildRepositoryIdsRequest;
}

export namespace GetChildRepositoryIdsRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildRepositoriesRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildRepositoriesRequest): GetChildRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildRepositoriesRequest;
  static deserializeBinaryFromReader(message: GetChildRepositoriesRequest, reader: jspb.BinaryReader): GetChildRepositoriesRequest;
}

export namespace GetChildRepositoriesRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfRepositoryReply extends jspb.Message {
  getIsDescendantOfRepository(): boolean;
  setIsDescendantOfRepository(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfRepositoryReply): IsDescendantOfRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfRepositoryReply;
  static deserializeBinaryFromReader(message: IsDescendantOfRepositoryReply, reader: jspb.BinaryReader): IsDescendantOfRepositoryReply;
}

export namespace IsDescendantOfRepositoryReply {
  export type AsObject = {
    isDescendantOfRepository: boolean,
  }
}

export class IsDescendantOfRepositoryRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfRepositoryRequest): IsDescendantOfRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfRepositoryRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfRepositoryRequest, reader: jspb.BinaryReader): IsDescendantOfRepositoryRequest;
}

export namespace IsDescendantOfRepositoryRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoryNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryNodeIdsReply): GetRepositoryNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryNodeIdsReply;
  static deserializeBinaryFromReader(message: GetRepositoryNodeIdsReply, reader: jspb.BinaryReader): GetRepositoryNodeIdsReply;
}

export namespace GetRepositoryNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetRepositoryNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryNodeIdsRequest): GetRepositoryNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetRepositoryNodeIdsRequest, reader: jspb.BinaryReader): GetRepositoryNodeIdsRequest;
}

export namespace GetRepositoryNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRepositoryNodesReply extends jspb.Message {
  hasRepositoryNode(): boolean;
  clearRepositoryNode(): void;
  getRepositoryNode(): RepositoryNode | undefined;
  setRepositoryNode(value?: RepositoryNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryNodesReply): GetRepositoryNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryNodesReply;
  static deserializeBinaryFromReader(message: GetRepositoryNodesReply, reader: jspb.BinaryReader): GetRepositoryNodesReply;
}

export namespace GetRepositoryNodesReply {
  export type AsObject = {
    repositoryNode?: RepositoryNode.AsObject,
  }
}

export class GetRepositoryNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRepositoryNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRepositoryNodesRequest): GetRepositoryNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRepositoryNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRepositoryNodesRequest;
  static deserializeBinaryFromReader(message: GetRepositoryNodesRequest, reader: jspb.BinaryReader): GetRepositoryNodesRequest;
}

export namespace GetRepositoryNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanModifyRepositoryHierarchyReply extends jspb.Message {
  getCanModifyRepositoryHierarchy(): boolean;
  setCanModifyRepositoryHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyRepositoryHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyRepositoryHierarchyReply): CanModifyRepositoryHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyRepositoryHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyRepositoryHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyRepositoryHierarchyReply, reader: jspb.BinaryReader): CanModifyRepositoryHierarchyReply;
}

export namespace CanModifyRepositoryHierarchyReply {
  export type AsObject = {
    canModifyRepositoryHierarchy: boolean,
  }
}

export class CanModifyRepositoryHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyRepositoryHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyRepositoryHierarchyRequest): CanModifyRepositoryHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyRepositoryHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyRepositoryHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyRepositoryHierarchyRequest, reader: jspb.BinaryReader): CanModifyRepositoryHierarchyRequest;
}

export namespace CanModifyRepositoryHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootRepositoryReply): AddRootRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootRepositoryReply;
  static deserializeBinaryFromReader(message: AddRootRepositoryReply, reader: jspb.BinaryReader): AddRootRepositoryReply;
}

export namespace AddRootRepositoryReply {
  export type AsObject = {
  }
}

export class AddRootRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootRepositoryRequest): AddRootRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootRepositoryRequest;
  static deserializeBinaryFromReader(message: AddRootRepositoryRequest, reader: jspb.BinaryReader): AddRootRepositoryRequest;
}

export namespace AddRootRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootRepositoryReply): RemoveRootRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootRepositoryReply;
  static deserializeBinaryFromReader(message: RemoveRootRepositoryReply, reader: jspb.BinaryReader): RemoveRootRepositoryReply;
}

export namespace RemoveRootRepositoryReply {
  export type AsObject = {
  }
}

export class RemoveRootRepositoryRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootRepositoryRequest): RemoveRootRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootRepositoryRequest;
  static deserializeBinaryFromReader(message: RemoveRootRepositoryRequest, reader: jspb.BinaryReader): RemoveRootRepositoryRequest;
}

export namespace RemoveRootRepositoryRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildRepositoryReply): AddChildRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildRepositoryReply;
  static deserializeBinaryFromReader(message: AddChildRepositoryReply, reader: jspb.BinaryReader): AddChildRepositoryReply;
}

export namespace AddChildRepositoryReply {
  export type AsObject = {
  }
}

export class AddChildRepositoryRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildRepositoryRequest): AddChildRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildRepositoryRequest;
  static deserializeBinaryFromReader(message: AddChildRepositoryRequest, reader: jspb.BinaryReader): AddChildRepositoryRequest;
}

export namespace AddChildRepositoryRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildRepositoryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildRepositoryReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildRepositoryReply): RemoveChildRepositoryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildRepositoryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildRepositoryReply;
  static deserializeBinaryFromReader(message: RemoveChildRepositoryReply, reader: jspb.BinaryReader): RemoveChildRepositoryReply;
}

export namespace RemoveChildRepositoryReply {
  export type AsObject = {
  }
}

export class RemoveChildRepositoryRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildRepositoryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildRepositoryRequest): RemoveChildRepositoryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildRepositoryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildRepositoryRequest;
  static deserializeBinaryFromReader(message: RemoveChildRepositoryRequest, reader: jspb.BinaryReader): RemoveChildRepositoryRequest;
}

export namespace RemoveChildRepositoryRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildRepositoriesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildRepositoriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildRepositoriesReply): RemoveChildRepositoriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildRepositoriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildRepositoriesReply;
  static deserializeBinaryFromReader(message: RemoveChildRepositoriesReply, reader: jspb.BinaryReader): RemoveChildRepositoriesReply;
}

export namespace RemoveChildRepositoriesReply {
  export type AsObject = {
  }
}

export class RemoveChildRepositoriesRequest extends jspb.Message {
  hasRepositoryId(): boolean;
  clearRepositoryId(): void;
  getRepositoryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRepositoryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildRepositoriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildRepositoriesRequest): RemoveChildRepositoriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildRepositoriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildRepositoriesRequest;
  static deserializeBinaryFromReader(message: RemoveChildRepositoriesRequest, reader: jspb.BinaryReader): RemoveChildRepositoriesRequest;
}

export namespace RemoveChildRepositoriesRequest {
  export type AsObject = {
    repositoryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

