// package: dlkit.proto.resource
// file: dlkit/proto/resource.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_authentication_pb from "../../dlkit/proto/authentication_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";

export class Resource extends jspb.Message {
  hasAvatar(): boolean;
  clearAvatar(): void;
  getAvatar(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAvatar(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBin(): boolean;
  clearBin(): void;
  getBin(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBin(value?: dlkit_proto_osid_pb.OsidCatalog): void;

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

  getGroup(): boolean;
  setGroup(value: boolean): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Resource.AsObject;
  static toObject(includeInstance: boolean, msg: Resource): Resource.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Resource, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Resource;
  static deserializeBinaryFromReader(message: Resource, reader: jspb.BinaryReader): Resource;
}

export namespace Resource {
  export type AsObject = {
    avatar?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bin?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    group: boolean,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class ResourceQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceQuery): ResourceQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceQuery;
  static deserializeBinaryFromReader(message: ResourceQuery, reader: jspb.BinaryReader): ResourceQuery;
}

export namespace ResourceQuery {
  export type AsObject = {
  }
}

export class ResourceQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceQueryInspector): ResourceQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceQueryInspector;
  static deserializeBinaryFromReader(message: ResourceQueryInspector, reader: jspb.BinaryReader): ResourceQueryInspector;
}

export namespace ResourceQueryInspector {
  export type AsObject = {
  }
}

export class ResourceForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceForm.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceForm): ResourceForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceForm;
  static deserializeBinaryFromReader(message: ResourceForm, reader: jspb.BinaryReader): ResourceForm;
}

export namespace ResourceForm {
  export type AsObject = {
  }
}

export class ResourceSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceSearchOrder): ResourceSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceSearchOrder;
  static deserializeBinaryFromReader(message: ResourceSearchOrder, reader: jspb.BinaryReader): ResourceSearchOrder;
}

export namespace ResourceSearchOrder {
  export type AsObject = {
  }
}

export class ResourceSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceSearch): ResourceSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceSearch;
  static deserializeBinaryFromReader(message: ResourceSearch, reader: jspb.BinaryReader): ResourceSearch;
}

export namespace ResourceSearch {
  export type AsObject = {
  }
}

export class ResourceSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceSearchResults): ResourceSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceSearchResults;
  static deserializeBinaryFromReader(message: ResourceSearchResults, reader: jspb.BinaryReader): ResourceSearchResults;
}

export namespace ResourceSearchResults {
  export type AsObject = {
  }
}

export class ResourceList extends jspb.Message {
  clearResourcesList(): void;
  getResourcesList(): Array<Resource>;
  setResourcesList(value: Array<Resource>): void;
  addResources(value?: Resource, index?: number): Resource;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceList.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceList): ResourceList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceList;
  static deserializeBinaryFromReader(message: ResourceList, reader: jspb.BinaryReader): ResourceList;
}

export namespace ResourceList {
  export type AsObject = {
    resourcesList: Array<Resource.AsObject>,
  }
}

export class ResourceNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceNode.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceNode): ResourceNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceNode;
  static deserializeBinaryFromReader(message: ResourceNode, reader: jspb.BinaryReader): ResourceNode;
}

export namespace ResourceNode {
  export type AsObject = {
  }
}

export class ResourceNodeList extends jspb.Message {
  clearResourceNodesList(): void;
  getResourceNodesList(): Array<ResourceNode>;
  setResourceNodesList(value: Array<ResourceNode>): void;
  addResourceNodes(value?: ResourceNode, index?: number): ResourceNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceNodeList): ResourceNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceNodeList;
  static deserializeBinaryFromReader(message: ResourceNodeList, reader: jspb.BinaryReader): ResourceNodeList;
}

export namespace ResourceNodeList {
  export type AsObject = {
    resourceNodesList: Array<ResourceNode.AsObject>,
  }
}

export class ResourceRelationship extends jspb.Message {
  hasBin(): boolean;
  clearBin(): void;
  getBin(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBin(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasDestinationResource(): boolean;
  clearDestinationResource(): void;
  getDestinationResource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationResource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSourceResource(): boolean;
  clearSourceResource(): void;
  getSourceResource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceResource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationship.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationship): ResourceRelationship.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationship, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationship;
  static deserializeBinaryFromReader(message: ResourceRelationship, reader: jspb.BinaryReader): ResourceRelationship;
}

export namespace ResourceRelationship {
  export type AsObject = {
    bin?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    destinationResource?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sourceResource?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ResourceRelationshipQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipQuery): ResourceRelationshipQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipQuery;
  static deserializeBinaryFromReader(message: ResourceRelationshipQuery, reader: jspb.BinaryReader): ResourceRelationshipQuery;
}

export namespace ResourceRelationshipQuery {
  export type AsObject = {
  }
}

export class ResourceRelationshipQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipQueryInspector): ResourceRelationshipQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipQueryInspector;
  static deserializeBinaryFromReader(message: ResourceRelationshipQueryInspector, reader: jspb.BinaryReader): ResourceRelationshipQueryInspector;
}

export namespace ResourceRelationshipQueryInspector {
  export type AsObject = {
  }
}

export class ResourceRelationshipForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipForm.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipForm): ResourceRelationshipForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipForm;
  static deserializeBinaryFromReader(message: ResourceRelationshipForm, reader: jspb.BinaryReader): ResourceRelationshipForm;
}

export namespace ResourceRelationshipForm {
  export type AsObject = {
  }
}

export class ResourceRelationshipSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipSearchOrder): ResourceRelationshipSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipSearchOrder;
  static deserializeBinaryFromReader(message: ResourceRelationshipSearchOrder, reader: jspb.BinaryReader): ResourceRelationshipSearchOrder;
}

export namespace ResourceRelationshipSearchOrder {
  export type AsObject = {
  }
}

export class ResourceRelationshipSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipSearch): ResourceRelationshipSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipSearch;
  static deserializeBinaryFromReader(message: ResourceRelationshipSearch, reader: jspb.BinaryReader): ResourceRelationshipSearch;
}

export namespace ResourceRelationshipSearch {
  export type AsObject = {
  }
}

export class ResourceRelationshipSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipSearchResults): ResourceRelationshipSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipSearchResults;
  static deserializeBinaryFromReader(message: ResourceRelationshipSearchResults, reader: jspb.BinaryReader): ResourceRelationshipSearchResults;
}

export namespace ResourceRelationshipSearchResults {
  export type AsObject = {
  }
}

export class ResourceRelationshipList extends jspb.Message {
  clearResourceRelationshipsList(): void;
  getResourceRelationshipsList(): Array<ResourceRelationship>;
  setResourceRelationshipsList(value: Array<ResourceRelationship>): void;
  addResourceRelationships(value?: ResourceRelationship, index?: number): ResourceRelationship;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceRelationshipList.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceRelationshipList): ResourceRelationshipList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceRelationshipList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceRelationshipList;
  static deserializeBinaryFromReader(message: ResourceRelationshipList, reader: jspb.BinaryReader): ResourceRelationshipList;
}

export namespace ResourceRelationshipList {
  export type AsObject = {
    resourceRelationshipsList: Array<ResourceRelationship.AsObject>,
  }
}

export class Bin extends jspb.Message {
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
  toObject(includeInstance?: boolean): Bin.AsObject;
  static toObject(includeInstance: boolean, msg: Bin): Bin.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Bin, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Bin;
  static deserializeBinaryFromReader(message: Bin, reader: jspb.BinaryReader): Bin;
}

export namespace Bin {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class BinQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinQuery.AsObject;
  static toObject(includeInstance: boolean, msg: BinQuery): BinQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinQuery;
  static deserializeBinaryFromReader(message: BinQuery, reader: jspb.BinaryReader): BinQuery;
}

export namespace BinQuery {
  export type AsObject = {
  }
}

export class BinQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: BinQueryInspector): BinQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinQueryInspector;
  static deserializeBinaryFromReader(message: BinQueryInspector, reader: jspb.BinaryReader): BinQueryInspector;
}

export namespace BinQueryInspector {
  export type AsObject = {
  }
}

export class BinForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinForm.AsObject;
  static toObject(includeInstance: boolean, msg: BinForm): BinForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinForm;
  static deserializeBinaryFromReader(message: BinForm, reader: jspb.BinaryReader): BinForm;
}

export namespace BinForm {
  export type AsObject = {
  }
}

export class BinSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: BinSearchOrder): BinSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinSearchOrder;
  static deserializeBinaryFromReader(message: BinSearchOrder, reader: jspb.BinaryReader): BinSearchOrder;
}

export namespace BinSearchOrder {
  export type AsObject = {
  }
}

export class BinSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinSearch.AsObject;
  static toObject(includeInstance: boolean, msg: BinSearch): BinSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinSearch;
  static deserializeBinaryFromReader(message: BinSearch, reader: jspb.BinaryReader): BinSearch;
}

export namespace BinSearch {
  export type AsObject = {
  }
}

export class BinSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: BinSearchResults): BinSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinSearchResults;
  static deserializeBinaryFromReader(message: BinSearchResults, reader: jspb.BinaryReader): BinSearchResults;
}

export namespace BinSearchResults {
  export type AsObject = {
  }
}

export class BinList extends jspb.Message {
  clearBinsList(): void;
  getBinsList(): Array<Bin>;
  setBinsList(value: Array<Bin>): void;
  addBins(value?: Bin, index?: number): Bin;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinList.AsObject;
  static toObject(includeInstance: boolean, msg: BinList): BinList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinList;
  static deserializeBinaryFromReader(message: BinList, reader: jspb.BinaryReader): BinList;
}

export namespace BinList {
  export type AsObject = {
    binsList: Array<Bin.AsObject>,
  }
}

export class BinNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinNode.AsObject;
  static toObject(includeInstance: boolean, msg: BinNode): BinNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinNode;
  static deserializeBinaryFromReader(message: BinNode, reader: jspb.BinaryReader): BinNode;
}

export namespace BinNode {
  export type AsObject = {
  }
}

export class BinNodeList extends jspb.Message {
  clearBinNodesList(): void;
  getBinNodesList(): Array<BinNode>;
  setBinNodesList(value: Array<BinNode>): void;
  addBinNodes(value?: BinNode, index?: number): BinNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BinNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: BinNodeList): BinNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BinNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BinNodeList;
  static deserializeBinaryFromReader(message: BinNodeList, reader: jspb.BinaryReader): BinNodeList;
}

export namespace BinNodeList {
  export type AsObject = {
    binNodesList: Array<BinNode.AsObject>,
  }
}

export class GetBinIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinIdReply): GetBinIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinIdReply;
  static deserializeBinaryFromReader(message: GetBinIdReply, reader: jspb.BinaryReader): GetBinIdReply;
}

export namespace GetBinIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBinIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinIdRequest): GetBinIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinIdRequest;
  static deserializeBinaryFromReader(message: GetBinIdRequest, reader: jspb.BinaryReader): GetBinIdRequest;
}

export namespace GetBinIdRequest {
  export type AsObject = {
  }
}

export class GetBinReply extends jspb.Message {
  hasBin(): boolean;
  clearBin(): void;
  getBin(): Bin | undefined;
  setBin(value?: Bin): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinReply): GetBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinReply;
  static deserializeBinaryFromReader(message: GetBinReply, reader: jspb.BinaryReader): GetBinReply;
}

export namespace GetBinReply {
  export type AsObject = {
    bin?: Bin.AsObject,
  }
}

export class GetBinRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinRequest): GetBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinRequest;
  static deserializeBinaryFromReader(message: GetBinRequest, reader: jspb.BinaryReader): GetBinRequest;
}

export namespace GetBinRequest {
  export type AsObject = {
  }
}

export class CanLookupResourcesReply extends jspb.Message {
  getCanLookupResources(): boolean;
  setCanLookupResources(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupResourcesReply): CanLookupResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupResourcesReply;
  static deserializeBinaryFromReader(message: CanLookupResourcesReply, reader: jspb.BinaryReader): CanLookupResourcesReply;
}

export namespace CanLookupResourcesReply {
  export type AsObject = {
    canLookupResources: boolean,
  }
}

export class CanLookupResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupResourcesRequest): CanLookupResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupResourcesRequest;
  static deserializeBinaryFromReader(message: CanLookupResourcesRequest, reader: jspb.BinaryReader): CanLookupResourcesRequest;
}

export namespace CanLookupResourcesRequest {
  export type AsObject = {
  }
}

export class UseComparativeResourceViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeResourceViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeResourceViewReply): UseComparativeResourceViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeResourceViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeResourceViewReply;
  static deserializeBinaryFromReader(message: UseComparativeResourceViewReply, reader: jspb.BinaryReader): UseComparativeResourceViewReply;
}

export namespace UseComparativeResourceViewReply {
  export type AsObject = {
  }
}

export class UseComparativeResourceViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeResourceViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeResourceViewRequest): UseComparativeResourceViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeResourceViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeResourceViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeResourceViewRequest, reader: jspb.BinaryReader): UseComparativeResourceViewRequest;
}

export namespace UseComparativeResourceViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryResourceViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryResourceViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryResourceViewReply): UsePlenaryResourceViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryResourceViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryResourceViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryResourceViewReply, reader: jspb.BinaryReader): UsePlenaryResourceViewReply;
}

export namespace UsePlenaryResourceViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryResourceViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryResourceViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryResourceViewRequest): UsePlenaryResourceViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryResourceViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryResourceViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryResourceViewRequest, reader: jspb.BinaryReader): UsePlenaryResourceViewRequest;
}

export namespace UsePlenaryResourceViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedBinViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedBinViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedBinViewReply): UseFederatedBinViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedBinViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedBinViewReply;
  static deserializeBinaryFromReader(message: UseFederatedBinViewReply, reader: jspb.BinaryReader): UseFederatedBinViewReply;
}

export namespace UseFederatedBinViewReply {
  export type AsObject = {
  }
}

export class UseFederatedBinViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedBinViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedBinViewRequest): UseFederatedBinViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedBinViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedBinViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedBinViewRequest, reader: jspb.BinaryReader): UseFederatedBinViewRequest;
}

export namespace UseFederatedBinViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedBinViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedBinViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedBinViewReply): UseIsolatedBinViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedBinViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedBinViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedBinViewReply, reader: jspb.BinaryReader): UseIsolatedBinViewReply;
}

export namespace UseIsolatedBinViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedBinViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedBinViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedBinViewRequest): UseIsolatedBinViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedBinViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedBinViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedBinViewRequest, reader: jspb.BinaryReader): UseIsolatedBinViewRequest;
}

export namespace UseIsolatedBinViewRequest {
  export type AsObject = {
  }
}

export class GetResourceReply extends jspb.Message {
  hasResource(): boolean;
  clearResource(): void;
  getResource(): Resource | undefined;
  setResource(value?: Resource): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceReply): GetResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceReply;
  static deserializeBinaryFromReader(message: GetResourceReply, reader: jspb.BinaryReader): GetResourceReply;
}

export namespace GetResourceReply {
  export type AsObject = {
    resource?: Resource.AsObject,
  }
}

export class GetResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceRequest): GetResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceRequest;
  static deserializeBinaryFromReader(message: GetResourceRequest, reader: jspb.BinaryReader): GetResourceRequest;
}

export namespace GetResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResourcesByIdsRequest extends jspb.Message {
  clearResourceIdsList(): void;
  getResourceIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setResourceIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addResourceIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByIdsRequest): GetResourcesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByIdsRequest;
  static deserializeBinaryFromReader(message: GetResourcesByIdsRequest, reader: jspb.BinaryReader): GetResourcesByIdsRequest;
}

export namespace GetResourcesByIdsRequest {
  export type AsObject = {
    resourceIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetResourcesByGenusTypeRequest extends jspb.Message {
  hasResourceGenusType(): boolean;
  clearResourceGenusType(): void;
  getResourceGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setResourceGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByGenusTypeRequest): GetResourcesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetResourcesByGenusTypeRequest, reader: jspb.BinaryReader): GetResourcesByGenusTypeRequest;
}

export namespace GetResourcesByGenusTypeRequest {
  export type AsObject = {
    resourceGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetResourcesByParentGenusTypeRequest extends jspb.Message {
  hasResourceGenusType(): boolean;
  clearResourceGenusType(): void;
  getResourceGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setResourceGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByParentGenusTypeRequest): GetResourcesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetResourcesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetResourcesByParentGenusTypeRequest;
}

export namespace GetResourcesByParentGenusTypeRequest {
  export type AsObject = {
    resourceGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetResourcesByRecordTypeRequest extends jspb.Message {
  hasResourceRecordType(): boolean;
  clearResourceRecordType(): void;
  getResourceRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setResourceRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByRecordTypeRequest): GetResourcesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetResourcesByRecordTypeRequest, reader: jspb.BinaryReader): GetResourcesByRecordTypeRequest;
}

export namespace GetResourcesByRecordTypeRequest {
  export type AsObject = {
    resourceRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesRequest): GetResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesRequest;
  static deserializeBinaryFromReader(message: GetResourcesRequest, reader: jspb.BinaryReader): GetResourcesRequest;
}

export namespace GetResourcesRequest {
  export type AsObject = {
  }
}

export class CanSearchResourcesReply extends jspb.Message {
  getCanSearchResources(): boolean;
  setCanSearchResources(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchResourcesReply): CanSearchResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchResourcesReply;
  static deserializeBinaryFromReader(message: CanSearchResourcesReply, reader: jspb.BinaryReader): CanSearchResourcesReply;
}

export namespace CanSearchResourcesReply {
  export type AsObject = {
    canSearchResources: boolean,
  }
}

export class CanSearchResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchResourcesRequest): CanSearchResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchResourcesRequest;
  static deserializeBinaryFromReader(message: CanSearchResourcesRequest, reader: jspb.BinaryReader): CanSearchResourcesRequest;
}

export namespace CanSearchResourcesRequest {
  export type AsObject = {
  }
}

export class GetResourceQueryReply extends jspb.Message {
  hasResourceQuery(): boolean;
  clearResourceQuery(): void;
  getResourceQuery(): ResourceQuery | undefined;
  setResourceQuery(value?: ResourceQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceQueryReply): GetResourceQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceQueryReply;
  static deserializeBinaryFromReader(message: GetResourceQueryReply, reader: jspb.BinaryReader): GetResourceQueryReply;
}

export namespace GetResourceQueryReply {
  export type AsObject = {
    resourceQuery?: ResourceQuery.AsObject,
  }
}

export class GetResourceQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceQueryRequest): GetResourceQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceQueryRequest;
  static deserializeBinaryFromReader(message: GetResourceQueryRequest, reader: jspb.BinaryReader): GetResourceQueryRequest;
}

export namespace GetResourceQueryRequest {
  export type AsObject = {
  }
}

export class GetResourcesByQueryRequest extends jspb.Message {
  hasResourceQuery(): boolean;
  clearResourceQuery(): void;
  getResourceQuery(): ResourceQuery | undefined;
  setResourceQuery(value?: ResourceQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByQueryRequest): GetResourcesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByQueryRequest;
  static deserializeBinaryFromReader(message: GetResourcesByQueryRequest, reader: jspb.BinaryReader): GetResourcesByQueryRequest;
}

export namespace GetResourcesByQueryRequest {
  export type AsObject = {
    resourceQuery?: ResourceQuery.AsObject,
  }
}

export class GetResourceSearchReply extends jspb.Message {
  hasResourceSearch(): boolean;
  clearResourceSearch(): void;
  getResourceSearch(): ResourceSearch | undefined;
  setResourceSearch(value?: ResourceSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceSearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceSearchReply): GetResourceSearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceSearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceSearchReply;
  static deserializeBinaryFromReader(message: GetResourceSearchReply, reader: jspb.BinaryReader): GetResourceSearchReply;
}

export namespace GetResourceSearchReply {
  export type AsObject = {
    resourceSearch?: ResourceSearch.AsObject,
  }
}

export class GetResourceSearchRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceSearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceSearchRequest): GetResourceSearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceSearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceSearchRequest;
  static deserializeBinaryFromReader(message: GetResourceSearchRequest, reader: jspb.BinaryReader): GetResourceSearchRequest;
}

export namespace GetResourceSearchRequest {
  export type AsObject = {
  }
}

export class GetResourceSearchOrderReply extends jspb.Message {
  hasResourceSearchOrder(): boolean;
  clearResourceSearchOrder(): void;
  getResourceSearchOrder(): ResourceSearchOrder | undefined;
  setResourceSearchOrder(value?: ResourceSearchOrder): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceSearchOrderReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceSearchOrderReply): GetResourceSearchOrderReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceSearchOrderReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceSearchOrderReply;
  static deserializeBinaryFromReader(message: GetResourceSearchOrderReply, reader: jspb.BinaryReader): GetResourceSearchOrderReply;
}

export namespace GetResourceSearchOrderReply {
  export type AsObject = {
    resourceSearchOrder?: ResourceSearchOrder.AsObject,
  }
}

export class GetResourceSearchOrderRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceSearchOrderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceSearchOrderRequest): GetResourceSearchOrderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceSearchOrderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceSearchOrderRequest;
  static deserializeBinaryFromReader(message: GetResourceSearchOrderRequest, reader: jspb.BinaryReader): GetResourceSearchOrderRequest;
}

export namespace GetResourceSearchOrderRequest {
  export type AsObject = {
  }
}

export class GetResourcesBySearchReply extends jspb.Message {
  hasResourceSearchResults(): boolean;
  clearResourceSearchResults(): void;
  getResourceSearchResults(): ResourceSearchResults | undefined;
  setResourceSearchResults(value?: ResourceSearchResults): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesBySearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesBySearchReply): GetResourcesBySearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesBySearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesBySearchReply;
  static deserializeBinaryFromReader(message: GetResourcesBySearchReply, reader: jspb.BinaryReader): GetResourcesBySearchReply;
}

export namespace GetResourcesBySearchReply {
  export type AsObject = {
    resourceSearchResults?: ResourceSearchResults.AsObject,
  }
}

export class GetResourcesBySearchRequest extends jspb.Message {
  hasResourceQuery(): boolean;
  clearResourceQuery(): void;
  getResourceQuery(): ResourceQuery | undefined;
  setResourceQuery(value?: ResourceQuery): void;

  hasResourceSearch(): boolean;
  clearResourceSearch(): void;
  getResourceSearch(): ResourceSearch | undefined;
  setResourceSearch(value?: ResourceSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesBySearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesBySearchRequest): GetResourcesBySearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesBySearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesBySearchRequest;
  static deserializeBinaryFromReader(message: GetResourcesBySearchRequest, reader: jspb.BinaryReader): GetResourcesBySearchRequest;
}

export namespace GetResourcesBySearchRequest {
  export type AsObject = {
    resourceQuery?: ResourceQuery.AsObject,
    resourceSearch?: ResourceSearch.AsObject,
  }
}

export class GetResourceQueryFromInspectorReply extends jspb.Message {
  hasResourceQuery(): boolean;
  clearResourceQuery(): void;
  getResourceQuery(): ResourceQuery | undefined;
  setResourceQuery(value?: ResourceQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceQueryFromInspectorReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceQueryFromInspectorReply): GetResourceQueryFromInspectorReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceQueryFromInspectorReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceQueryFromInspectorReply;
  static deserializeBinaryFromReader(message: GetResourceQueryFromInspectorReply, reader: jspb.BinaryReader): GetResourceQueryFromInspectorReply;
}

export namespace GetResourceQueryFromInspectorReply {
  export type AsObject = {
    resourceQuery?: ResourceQuery.AsObject,
  }
}

export class GetResourceQueryFromInspectorRequest extends jspb.Message {
  hasResourceQueryInspector(): boolean;
  clearResourceQueryInspector(): void;
  getResourceQueryInspector(): ResourceQueryInspector | undefined;
  setResourceQueryInspector(value?: ResourceQueryInspector): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceQueryFromInspectorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceQueryFromInspectorRequest): GetResourceQueryFromInspectorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceQueryFromInspectorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceQueryFromInspectorRequest;
  static deserializeBinaryFromReader(message: GetResourceQueryFromInspectorRequest, reader: jspb.BinaryReader): GetResourceQueryFromInspectorRequest;
}

export namespace GetResourceQueryFromInspectorRequest {
  export type AsObject = {
    resourceQueryInspector?: ResourceQueryInspector.AsObject,
  }
}

export class CanCreateResourcesReply extends jspb.Message {
  getCanCreateResources(): boolean;
  setCanCreateResources(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateResourcesReply): CanCreateResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateResourcesReply;
  static deserializeBinaryFromReader(message: CanCreateResourcesReply, reader: jspb.BinaryReader): CanCreateResourcesReply;
}

export namespace CanCreateResourcesReply {
  export type AsObject = {
    canCreateResources: boolean,
  }
}

export class CanCreateResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateResourcesRequest): CanCreateResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateResourcesRequest;
  static deserializeBinaryFromReader(message: CanCreateResourcesRequest, reader: jspb.BinaryReader): CanCreateResourcesRequest;
}

export namespace CanCreateResourcesRequest {
  export type AsObject = {
  }
}

export class CanCreateResourceWithRecordTypesReply extends jspb.Message {
  getCanCreateResourceWithRecordTypes(): boolean;
  setCanCreateResourceWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateResourceWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateResourceWithRecordTypesReply): CanCreateResourceWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateResourceWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateResourceWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateResourceWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateResourceWithRecordTypesReply;
}

export namespace CanCreateResourceWithRecordTypesReply {
  export type AsObject = {
    canCreateResourceWithRecordTypes: boolean,
  }
}

export class CanCreateResourceWithRecordTypesRequest extends jspb.Message {
  clearResourceRecordTypesList(): void;
  getResourceRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setResourceRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addResourceRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateResourceWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateResourceWithRecordTypesRequest): CanCreateResourceWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateResourceWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateResourceWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateResourceWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateResourceWithRecordTypesRequest;
}

export namespace CanCreateResourceWithRecordTypesRequest {
  export type AsObject = {
    resourceRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetResourceFormForCreateReply extends jspb.Message {
  hasResourceForm(): boolean;
  clearResourceForm(): void;
  getResourceForm(): ResourceForm | undefined;
  setResourceForm(value?: ResourceForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceFormForCreateReply): GetResourceFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceFormForCreateReply;
  static deserializeBinaryFromReader(message: GetResourceFormForCreateReply, reader: jspb.BinaryReader): GetResourceFormForCreateReply;
}

export namespace GetResourceFormForCreateReply {
  export type AsObject = {
    resourceForm?: ResourceForm.AsObject,
  }
}

export class GetResourceFormForCreateRequest extends jspb.Message {
  clearResourceRecordTypesList(): void;
  getResourceRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setResourceRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addResourceRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceFormForCreateRequest): GetResourceFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetResourceFormForCreateRequest, reader: jspb.BinaryReader): GetResourceFormForCreateRequest;
}

export namespace GetResourceFormForCreateRequest {
  export type AsObject = {
    resourceRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateResourceReply extends jspb.Message {
  hasResource(): boolean;
  clearResource(): void;
  getResource(): Resource | undefined;
  setResource(value?: Resource): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateResourceReply): CreateResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateResourceReply;
  static deserializeBinaryFromReader(message: CreateResourceReply, reader: jspb.BinaryReader): CreateResourceReply;
}

export namespace CreateResourceReply {
  export type AsObject = {
    resource?: Resource.AsObject,
  }
}

export class CreateResourceRequest extends jspb.Message {
  hasResourceForm(): boolean;
  clearResourceForm(): void;
  getResourceForm(): ResourceForm | undefined;
  setResourceForm(value?: ResourceForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateResourceRequest): CreateResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateResourceRequest;
  static deserializeBinaryFromReader(message: CreateResourceRequest, reader: jspb.BinaryReader): CreateResourceRequest;
}

export namespace CreateResourceRequest {
  export type AsObject = {
    resourceForm?: ResourceForm.AsObject,
  }
}

export class CanUpdateResourcesReply extends jspb.Message {
  getCanUpdateResources(): boolean;
  setCanUpdateResources(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateResourcesReply): CanUpdateResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateResourcesReply;
  static deserializeBinaryFromReader(message: CanUpdateResourcesReply, reader: jspb.BinaryReader): CanUpdateResourcesReply;
}

export namespace CanUpdateResourcesReply {
  export type AsObject = {
    canUpdateResources: boolean,
  }
}

export class CanUpdateResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateResourcesRequest): CanUpdateResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateResourcesRequest;
  static deserializeBinaryFromReader(message: CanUpdateResourcesRequest, reader: jspb.BinaryReader): CanUpdateResourcesRequest;
}

export namespace CanUpdateResourcesRequest {
  export type AsObject = {
  }
}

export class GetResourceFormForUpdateReply extends jspb.Message {
  hasResourceForm(): boolean;
  clearResourceForm(): void;
  getResourceForm(): ResourceForm | undefined;
  setResourceForm(value?: ResourceForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceFormForUpdateReply): GetResourceFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetResourceFormForUpdateReply, reader: jspb.BinaryReader): GetResourceFormForUpdateReply;
}

export namespace GetResourceFormForUpdateReply {
  export type AsObject = {
    resourceForm?: ResourceForm.AsObject,
  }
}

export class GetResourceFormForUpdateRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceFormForUpdateRequest): GetResourceFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetResourceFormForUpdateRequest, reader: jspb.BinaryReader): GetResourceFormForUpdateRequest;
}

export namespace GetResourceFormForUpdateRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateResourceReply): UpdateResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateResourceReply;
  static deserializeBinaryFromReader(message: UpdateResourceReply, reader: jspb.BinaryReader): UpdateResourceReply;
}

export namespace UpdateResourceReply {
  export type AsObject = {
  }
}

export class UpdateResourceRequest extends jspb.Message {
  hasResourceForm(): boolean;
  clearResourceForm(): void;
  getResourceForm(): ResourceForm | undefined;
  setResourceForm(value?: ResourceForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateResourceRequest): UpdateResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateResourceRequest;
  static deserializeBinaryFromReader(message: UpdateResourceRequest, reader: jspb.BinaryReader): UpdateResourceRequest;
}

export namespace UpdateResourceRequest {
  export type AsObject = {
    resourceForm?: ResourceForm.AsObject,
  }
}

export class CanDeleteResourcesReply extends jspb.Message {
  getCanDeleteResources(): boolean;
  setCanDeleteResources(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteResourcesReply): CanDeleteResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteResourcesReply;
  static deserializeBinaryFromReader(message: CanDeleteResourcesReply, reader: jspb.BinaryReader): CanDeleteResourcesReply;
}

export namespace CanDeleteResourcesReply {
  export type AsObject = {
    canDeleteResources: boolean,
  }
}

export class CanDeleteResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteResourcesRequest): CanDeleteResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteResourcesRequest;
  static deserializeBinaryFromReader(message: CanDeleteResourcesRequest, reader: jspb.BinaryReader): CanDeleteResourcesRequest;
}

export namespace CanDeleteResourcesRequest {
  export type AsObject = {
  }
}

export class DeleteResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteResourceReply): DeleteResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteResourceReply;
  static deserializeBinaryFromReader(message: DeleteResourceReply, reader: jspb.BinaryReader): DeleteResourceReply;
}

export namespace DeleteResourceReply {
  export type AsObject = {
  }
}

export class DeleteResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteResourceRequest): DeleteResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteResourceRequest;
  static deserializeBinaryFromReader(message: DeleteResourceRequest, reader: jspb.BinaryReader): DeleteResourceRequest;
}

export namespace DeleteResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageResourceAliasesReply extends jspb.Message {
  getCanManageResourceAliases(): boolean;
  setCanManageResourceAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageResourceAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageResourceAliasesReply): CanManageResourceAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageResourceAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageResourceAliasesReply;
  static deserializeBinaryFromReader(message: CanManageResourceAliasesReply, reader: jspb.BinaryReader): CanManageResourceAliasesReply;
}

export namespace CanManageResourceAliasesReply {
  export type AsObject = {
    canManageResourceAliases: boolean,
  }
}

export class CanManageResourceAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageResourceAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageResourceAliasesRequest): CanManageResourceAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageResourceAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageResourceAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageResourceAliasesRequest, reader: jspb.BinaryReader): CanManageResourceAliasesRequest;
}

export namespace CanManageResourceAliasesRequest {
  export type AsObject = {
  }
}

export class AliasResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasResourceReply): AliasResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasResourceReply;
  static deserializeBinaryFromReader(message: AliasResourceReply, reader: jspb.BinaryReader): AliasResourceReply;
}

export namespace AliasResourceReply {
  export type AsObject = {
  }
}

export class AliasResourceRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasResourceRequest): AliasResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasResourceRequest;
  static deserializeBinaryFromReader(message: AliasResourceRequest, reader: jspb.BinaryReader): AliasResourceRequest;
}

export namespace AliasResourceRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanRegisterForResourceNotificationsReply extends jspb.Message {
  getCanRegisterForResourceNotifications(): boolean;
  setCanRegisterForResourceNotifications(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanRegisterForResourceNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanRegisterForResourceNotificationsReply): CanRegisterForResourceNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanRegisterForResourceNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanRegisterForResourceNotificationsReply;
  static deserializeBinaryFromReader(message: CanRegisterForResourceNotificationsReply, reader: jspb.BinaryReader): CanRegisterForResourceNotificationsReply;
}

export namespace CanRegisterForResourceNotificationsReply {
  export type AsObject = {
    canRegisterForResourceNotifications: boolean,
  }
}

export class CanRegisterForResourceNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanRegisterForResourceNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanRegisterForResourceNotificationsRequest): CanRegisterForResourceNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanRegisterForResourceNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanRegisterForResourceNotificationsRequest;
  static deserializeBinaryFromReader(message: CanRegisterForResourceNotificationsRequest, reader: jspb.BinaryReader): CanRegisterForResourceNotificationsRequest;
}

export namespace CanRegisterForResourceNotificationsRequest {
  export type AsObject = {
  }
}

export class RegisterForNewResourcesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewResourcesReply): RegisterForNewResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewResourcesReply;
  static deserializeBinaryFromReader(message: RegisterForNewResourcesReply, reader: jspb.BinaryReader): RegisterForNewResourcesReply;
}

export namespace RegisterForNewResourcesReply {
  export type AsObject = {
  }
}

export class RegisterForNewResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewResourcesRequest): RegisterForNewResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewResourcesRequest;
  static deserializeBinaryFromReader(message: RegisterForNewResourcesRequest, reader: jspb.BinaryReader): RegisterForNewResourcesRequest;
}

export namespace RegisterForNewResourcesRequest {
  export type AsObject = {
  }
}

export class RegisterForChangedResourcesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedResourcesReply): RegisterForChangedResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedResourcesReply;
  static deserializeBinaryFromReader(message: RegisterForChangedResourcesReply, reader: jspb.BinaryReader): RegisterForChangedResourcesReply;
}

export namespace RegisterForChangedResourcesReply {
  export type AsObject = {
  }
}

export class RegisterForChangedResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedResourcesRequest): RegisterForChangedResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedResourcesRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedResourcesRequest, reader: jspb.BinaryReader): RegisterForChangedResourcesRequest;
}

export namespace RegisterForChangedResourcesRequest {
  export type AsObject = {
  }
}

export class RegisterForChangedResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedResourceReply): RegisterForChangedResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedResourceReply;
  static deserializeBinaryFromReader(message: RegisterForChangedResourceReply, reader: jspb.BinaryReader): RegisterForChangedResourceReply;
}

export namespace RegisterForChangedResourceReply {
  export type AsObject = {
  }
}

export class RegisterForChangedResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedResourceRequest): RegisterForChangedResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedResourceRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedResourceRequest, reader: jspb.BinaryReader): RegisterForChangedResourceRequest;
}

export namespace RegisterForChangedResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RegisterForDeletedResourcesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedResourcesReply): RegisterForDeletedResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedResourcesReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedResourcesReply, reader: jspb.BinaryReader): RegisterForDeletedResourcesReply;
}

export namespace RegisterForDeletedResourcesReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedResourcesRequest): RegisterForDeletedResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedResourcesRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedResourcesRequest, reader: jspb.BinaryReader): RegisterForDeletedResourcesRequest;
}

export namespace RegisterForDeletedResourcesRequest {
  export type AsObject = {
  }
}

export class RegisterForDeletedResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedResourceReply): RegisterForDeletedResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedResourceReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedResourceReply, reader: jspb.BinaryReader): RegisterForDeletedResourceReply;
}

export namespace RegisterForDeletedResourceReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedResourceRequest): RegisterForDeletedResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedResourceRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedResourceRequest, reader: jspb.BinaryReader): RegisterForDeletedResourceRequest;
}

export namespace RegisterForDeletedResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReliableResourceNotificationsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReliableResourceNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReliableResourceNotificationsReply): ReliableResourceNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReliableResourceNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReliableResourceNotificationsReply;
  static deserializeBinaryFromReader(message: ReliableResourceNotificationsReply, reader: jspb.BinaryReader): ReliableResourceNotificationsReply;
}

export namespace ReliableResourceNotificationsReply {
  export type AsObject = {
  }
}

export class ReliableResourceNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReliableResourceNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReliableResourceNotificationsRequest): ReliableResourceNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReliableResourceNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReliableResourceNotificationsRequest;
  static deserializeBinaryFromReader(message: ReliableResourceNotificationsRequest, reader: jspb.BinaryReader): ReliableResourceNotificationsRequest;
}

export namespace ReliableResourceNotificationsRequest {
  export type AsObject = {
  }
}

export class UnreliableResourceNotificationsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnreliableResourceNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnreliableResourceNotificationsReply): UnreliableResourceNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnreliableResourceNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnreliableResourceNotificationsReply;
  static deserializeBinaryFromReader(message: UnreliableResourceNotificationsReply, reader: jspb.BinaryReader): UnreliableResourceNotificationsReply;
}

export namespace UnreliableResourceNotificationsReply {
  export type AsObject = {
  }
}

export class UnreliableResourceNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnreliableResourceNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnreliableResourceNotificationsRequest): UnreliableResourceNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnreliableResourceNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnreliableResourceNotificationsRequest;
  static deserializeBinaryFromReader(message: UnreliableResourceNotificationsRequest, reader: jspb.BinaryReader): UnreliableResourceNotificationsRequest;
}

export namespace UnreliableResourceNotificationsRequest {
  export type AsObject = {
  }
}

export class AcknowledgeResourceNotificationReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AcknowledgeResourceNotificationReply.AsObject;
  static toObject(includeInstance: boolean, msg: AcknowledgeResourceNotificationReply): AcknowledgeResourceNotificationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AcknowledgeResourceNotificationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AcknowledgeResourceNotificationReply;
  static deserializeBinaryFromReader(message: AcknowledgeResourceNotificationReply, reader: jspb.BinaryReader): AcknowledgeResourceNotificationReply;
}

export namespace AcknowledgeResourceNotificationReply {
  export type AsObject = {
  }
}

export class AcknowledgeResourceNotificationRequest extends jspb.Message {
  hasNotificationId(): boolean;
  clearNotificationId(): void;
  getNotificationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNotificationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AcknowledgeResourceNotificationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AcknowledgeResourceNotificationRequest): AcknowledgeResourceNotificationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AcknowledgeResourceNotificationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AcknowledgeResourceNotificationRequest;
  static deserializeBinaryFromReader(message: AcknowledgeResourceNotificationRequest, reader: jspb.BinaryReader): AcknowledgeResourceNotificationRequest;
}

export namespace AcknowledgeResourceNotificationRequest {
  export type AsObject = {
    notificationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UseComparativeBinViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeBinViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeBinViewReply): UseComparativeBinViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeBinViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeBinViewReply;
  static deserializeBinaryFromReader(message: UseComparativeBinViewReply, reader: jspb.BinaryReader): UseComparativeBinViewReply;
}

export namespace UseComparativeBinViewReply {
  export type AsObject = {
  }
}

export class UseComparativeBinViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeBinViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeBinViewRequest): UseComparativeBinViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeBinViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeBinViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeBinViewRequest, reader: jspb.BinaryReader): UseComparativeBinViewRequest;
}

export namespace UseComparativeBinViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryBinViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryBinViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryBinViewReply): UsePlenaryBinViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryBinViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryBinViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryBinViewReply, reader: jspb.BinaryReader): UsePlenaryBinViewReply;
}

export namespace UsePlenaryBinViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryBinViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryBinViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryBinViewRequest): UsePlenaryBinViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryBinViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryBinViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryBinViewRequest, reader: jspb.BinaryReader): UsePlenaryBinViewRequest;
}

export namespace UsePlenaryBinViewRequest {
  export type AsObject = {
  }
}

export class CanLookupResourceBinMappingsReply extends jspb.Message {
  getCanLookupResourceBinMappings(): boolean;
  setCanLookupResourceBinMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupResourceBinMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupResourceBinMappingsReply): CanLookupResourceBinMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupResourceBinMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupResourceBinMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupResourceBinMappingsReply, reader: jspb.BinaryReader): CanLookupResourceBinMappingsReply;
}

export namespace CanLookupResourceBinMappingsReply {
  export type AsObject = {
    canLookupResourceBinMappings: boolean,
  }
}

export class CanLookupResourceBinMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupResourceBinMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupResourceBinMappingsRequest): CanLookupResourceBinMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupResourceBinMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupResourceBinMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupResourceBinMappingsRequest, reader: jspb.BinaryReader): CanLookupResourceBinMappingsRequest;
}

export namespace CanLookupResourceBinMappingsRequest {
  export type AsObject = {
  }
}

export class GetResourceIdsByBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceIdsByBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceIdsByBinRequest): GetResourceIdsByBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceIdsByBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceIdsByBinRequest;
  static deserializeBinaryFromReader(message: GetResourceIdsByBinRequest, reader: jspb.BinaryReader): GetResourceIdsByBinRequest;
}

export namespace GetResourceIdsByBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResourcesByBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByBinRequest): GetResourcesByBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByBinRequest;
  static deserializeBinaryFromReader(message: GetResourcesByBinRequest, reader: jspb.BinaryReader): GetResourcesByBinRequest;
}

export namespace GetResourcesByBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResourceIdsByBinsRequest extends jspb.Message {
  clearBinIdsList(): void;
  getBinIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBinIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBinIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceIdsByBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceIdsByBinsRequest): GetResourceIdsByBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceIdsByBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceIdsByBinsRequest;
  static deserializeBinaryFromReader(message: GetResourceIdsByBinsRequest, reader: jspb.BinaryReader): GetResourceIdsByBinsRequest;
}

export namespace GetResourceIdsByBinsRequest {
  export type AsObject = {
    binIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetResourcesByBinsRequest extends jspb.Message {
  clearBinIdsList(): void;
  getBinIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBinIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBinIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourcesByBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourcesByBinsRequest): GetResourcesByBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourcesByBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourcesByBinsRequest;
  static deserializeBinaryFromReader(message: GetResourcesByBinsRequest, reader: jspb.BinaryReader): GetResourcesByBinsRequest;
}

export namespace GetResourcesByBinsRequest {
  export type AsObject = {
    binIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBinIdsByResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinIdsByResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinIdsByResourceRequest): GetBinIdsByResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinIdsByResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinIdsByResourceRequest;
  static deserializeBinaryFromReader(message: GetBinIdsByResourceRequest, reader: jspb.BinaryReader): GetBinIdsByResourceRequest;
}

export namespace GetBinIdsByResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBinsByResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByResourceRequest): GetBinsByResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByResourceRequest;
  static deserializeBinaryFromReader(message: GetBinsByResourceRequest, reader: jspb.BinaryReader): GetBinsByResourceRequest;
}

export namespace GetBinsByResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignResourcesReply extends jspb.Message {
  getCanAssignResources(): boolean;
  setCanAssignResources(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignResourcesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignResourcesReply): CanAssignResourcesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignResourcesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignResourcesReply;
  static deserializeBinaryFromReader(message: CanAssignResourcesReply, reader: jspb.BinaryReader): CanAssignResourcesReply;
}

export namespace CanAssignResourcesReply {
  export type AsObject = {
    canAssignResources: boolean,
  }
}

export class CanAssignResourcesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignResourcesRequest): CanAssignResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignResourcesRequest;
  static deserializeBinaryFromReader(message: CanAssignResourcesRequest, reader: jspb.BinaryReader): CanAssignResourcesRequest;
}

export namespace CanAssignResourcesRequest {
  export type AsObject = {
  }
}

export class CanAssignResourcesToBinReply extends jspb.Message {
  getCanAssignResourcesToBin(): boolean;
  setCanAssignResourcesToBin(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignResourcesToBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignResourcesToBinReply): CanAssignResourcesToBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignResourcesToBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignResourcesToBinReply;
  static deserializeBinaryFromReader(message: CanAssignResourcesToBinReply, reader: jspb.BinaryReader): CanAssignResourcesToBinReply;
}

export namespace CanAssignResourcesToBinReply {
  export type AsObject = {
    canAssignResourcesToBin: boolean,
  }
}

export class CanAssignResourcesToBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignResourcesToBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignResourcesToBinRequest): CanAssignResourcesToBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignResourcesToBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignResourcesToBinRequest;
  static deserializeBinaryFromReader(message: CanAssignResourcesToBinRequest, reader: jspb.BinaryReader): CanAssignResourcesToBinRequest;
}

export namespace CanAssignResourcesToBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBinIdsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBinIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBinIdsRequest): GetAssignableBinIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBinIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBinIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableBinIdsRequest, reader: jspb.BinaryReader): GetAssignableBinIdsRequest;
}

export namespace GetAssignableBinIdsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBinIdsForResourceRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBinIdsForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBinIdsForResourceRequest): GetAssignableBinIdsForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBinIdsForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBinIdsForResourceRequest;
  static deserializeBinaryFromReader(message: GetAssignableBinIdsForResourceRequest, reader: jspb.BinaryReader): GetAssignableBinIdsForResourceRequest;
}

export namespace GetAssignableBinIdsForResourceRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignResourceToBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignResourceToBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignResourceToBinReply): AssignResourceToBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignResourceToBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignResourceToBinReply;
  static deserializeBinaryFromReader(message: AssignResourceToBinReply, reader: jspb.BinaryReader): AssignResourceToBinReply;
}

export namespace AssignResourceToBinReply {
  export type AsObject = {
  }
}

export class AssignResourceToBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignResourceToBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignResourceToBinRequest): AssignResourceToBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignResourceToBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignResourceToBinRequest;
  static deserializeBinaryFromReader(message: AssignResourceToBinRequest, reader: jspb.BinaryReader): AssignResourceToBinRequest;
}

export namespace AssignResourceToBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignResourceFromBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignResourceFromBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignResourceFromBinReply): UnassignResourceFromBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignResourceFromBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignResourceFromBinReply;
  static deserializeBinaryFromReader(message: UnassignResourceFromBinReply, reader: jspb.BinaryReader): UnassignResourceFromBinReply;
}

export namespace UnassignResourceFromBinReply {
  export type AsObject = {
  }
}

export class UnassignResourceFromBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignResourceFromBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignResourceFromBinRequest): UnassignResourceFromBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignResourceFromBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignResourceFromBinRequest;
  static deserializeBinaryFromReader(message: UnassignResourceFromBinRequest, reader: jspb.BinaryReader): UnassignResourceFromBinRequest;
}

export namespace UnassignResourceFromBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupResourceAgentMappingsReply extends jspb.Message {
  getCanLookupResourceAgentMappings(): boolean;
  setCanLookupResourceAgentMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupResourceAgentMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupResourceAgentMappingsReply): CanLookupResourceAgentMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupResourceAgentMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupResourceAgentMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupResourceAgentMappingsReply, reader: jspb.BinaryReader): CanLookupResourceAgentMappingsReply;
}

export namespace CanLookupResourceAgentMappingsReply {
  export type AsObject = {
    canLookupResourceAgentMappings: boolean,
  }
}

export class CanLookupResourceAgentMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupResourceAgentMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupResourceAgentMappingsRequest): CanLookupResourceAgentMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupResourceAgentMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupResourceAgentMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupResourceAgentMappingsRequest, reader: jspb.BinaryReader): CanLookupResourceAgentMappingsRequest;
}

export namespace CanLookupResourceAgentMappingsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAgentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAgentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAgentViewReply): UseComparativeAgentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAgentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAgentViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAgentViewReply, reader: jspb.BinaryReader): UseComparativeAgentViewReply;
}

export namespace UseComparativeAgentViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAgentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAgentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAgentViewRequest): UseComparativeAgentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAgentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAgentViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAgentViewRequest, reader: jspb.BinaryReader): UseComparativeAgentViewRequest;
}

export namespace UseComparativeAgentViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAgentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAgentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAgentViewReply): UsePlenaryAgentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAgentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAgentViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAgentViewReply, reader: jspb.BinaryReader): UsePlenaryAgentViewReply;
}

export namespace UsePlenaryAgentViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAgentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAgentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAgentViewRequest): UsePlenaryAgentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAgentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAgentViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAgentViewRequest, reader: jspb.BinaryReader): UsePlenaryAgentViewRequest;
}

export namespace UsePlenaryAgentViewRequest {
  export type AsObject = {
  }
}

export class GetResourceIdByAgentReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceIdByAgentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceIdByAgentReply): GetResourceIdByAgentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceIdByAgentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceIdByAgentReply;
  static deserializeBinaryFromReader(message: GetResourceIdByAgentReply, reader: jspb.BinaryReader): GetResourceIdByAgentReply;
}

export namespace GetResourceIdByAgentReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResourceIdByAgentRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceIdByAgentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceIdByAgentRequest): GetResourceIdByAgentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceIdByAgentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceIdByAgentRequest;
  static deserializeBinaryFromReader(message: GetResourceIdByAgentRequest, reader: jspb.BinaryReader): GetResourceIdByAgentRequest;
}

export namespace GetResourceIdByAgentRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResourceByAgentReply extends jspb.Message {
  hasResource(): boolean;
  clearResource(): void;
  getResource(): Resource | undefined;
  setResource(value?: Resource): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceByAgentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceByAgentReply): GetResourceByAgentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceByAgentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceByAgentReply;
  static deserializeBinaryFromReader(message: GetResourceByAgentReply, reader: jspb.BinaryReader): GetResourceByAgentReply;
}

export namespace GetResourceByAgentReply {
  export type AsObject = {
    resource?: Resource.AsObject,
  }
}

export class GetResourceByAgentRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResourceByAgentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResourceByAgentRequest): GetResourceByAgentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResourceByAgentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResourceByAgentRequest;
  static deserializeBinaryFromReader(message: GetResourceByAgentRequest, reader: jspb.BinaryReader): GetResourceByAgentRequest;
}

export namespace GetResourceByAgentRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAgentIdsByResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentIdsByResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentIdsByResourceRequest): GetAgentIdsByResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentIdsByResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentIdsByResourceRequest;
  static deserializeBinaryFromReader(message: GetAgentIdsByResourceRequest, reader: jspb.BinaryReader): GetAgentIdsByResourceRequest;
}

export namespace GetAgentIdsByResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAgentsByResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentsByResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentsByResourceRequest): GetAgentsByResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentsByResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentsByResourceRequest;
  static deserializeBinaryFromReader(message: GetAgentsByResourceRequest, reader: jspb.BinaryReader): GetAgentsByResourceRequest;
}

export namespace GetAgentsByResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAgentsReply extends jspb.Message {
  getCanAssignAgents(): boolean;
  setCanAssignAgents(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAgentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAgentsReply): CanAssignAgentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAgentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAgentsReply;
  static deserializeBinaryFromReader(message: CanAssignAgentsReply, reader: jspb.BinaryReader): CanAssignAgentsReply;
}

export namespace CanAssignAgentsReply {
  export type AsObject = {
    canAssignAgents: boolean,
  }
}

export class CanAssignAgentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAgentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAgentsRequest): CanAssignAgentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAgentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAgentsRequest;
  static deserializeBinaryFromReader(message: CanAssignAgentsRequest, reader: jspb.BinaryReader): CanAssignAgentsRequest;
}

export namespace CanAssignAgentsRequest {
  export type AsObject = {
  }
}

export class CanAssignAgentsToResourceReply extends jspb.Message {
  getCanAssignAgentsToResource(): boolean;
  setCanAssignAgentsToResource(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAgentsToResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAgentsToResourceReply): CanAssignAgentsToResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAgentsToResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAgentsToResourceReply;
  static deserializeBinaryFromReader(message: CanAssignAgentsToResourceReply, reader: jspb.BinaryReader): CanAssignAgentsToResourceReply;
}

export namespace CanAssignAgentsToResourceReply {
  export type AsObject = {
    canAssignAgentsToResource: boolean,
  }
}

export class CanAssignAgentsToResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAgentsToResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAgentsToResourceRequest): CanAssignAgentsToResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAgentsToResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAgentsToResourceRequest;
  static deserializeBinaryFromReader(message: CanAssignAgentsToResourceRequest, reader: jspb.BinaryReader): CanAssignAgentsToResourceRequest;
}

export namespace CanAssignAgentsToResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAgentToResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAgentToResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAgentToResourceReply): AssignAgentToResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAgentToResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAgentToResourceReply;
  static deserializeBinaryFromReader(message: AssignAgentToResourceReply, reader: jspb.BinaryReader): AssignAgentToResourceReply;
}

export namespace AssignAgentToResourceReply {
  export type AsObject = {
  }
}

export class AssignAgentToResourceRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAgentToResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAgentToResourceRequest): AssignAgentToResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAgentToResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAgentToResourceRequest;
  static deserializeBinaryFromReader(message: AssignAgentToResourceRequest, reader: jspb.BinaryReader): AssignAgentToResourceRequest;
}

export namespace AssignAgentToResourceRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAgentFromResourceReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAgentFromResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAgentFromResourceReply): UnassignAgentFromResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAgentFromResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAgentFromResourceReply;
  static deserializeBinaryFromReader(message: UnassignAgentFromResourceReply, reader: jspb.BinaryReader): UnassignAgentFromResourceReply;
}

export namespace UnassignAgentFromResourceReply {
  export type AsObject = {
  }
}

export class UnassignAgentFromResourceRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAgentFromResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAgentFromResourceRequest): UnassignAgentFromResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAgentFromResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAgentFromResourceRequest;
  static deserializeBinaryFromReader(message: UnassignAgentFromResourceRequest, reader: jspb.BinaryReader): UnassignAgentFromResourceRequest;
}

export namespace UnassignAgentFromResourceRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupBinsReply extends jspb.Message {
  getCanLookupBins(): boolean;
  setCanLookupBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupBinsReply): CanLookupBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupBinsReply;
  static deserializeBinaryFromReader(message: CanLookupBinsReply, reader: jspb.BinaryReader): CanLookupBinsReply;
}

export namespace CanLookupBinsReply {
  export type AsObject = {
    canLookupBins: boolean,
  }
}

export class CanLookupBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupBinsRequest): CanLookupBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupBinsRequest;
  static deserializeBinaryFromReader(message: CanLookupBinsRequest, reader: jspb.BinaryReader): CanLookupBinsRequest;
}

export namespace CanLookupBinsRequest {
  export type AsObject = {
  }
}

export class GetBinsByIdsRequest extends jspb.Message {
  clearBinIdsList(): void;
  getBinIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBinIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBinIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByIdsRequest): GetBinsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByIdsRequest;
  static deserializeBinaryFromReader(message: GetBinsByIdsRequest, reader: jspb.BinaryReader): GetBinsByIdsRequest;
}

export namespace GetBinsByIdsRequest {
  export type AsObject = {
    binIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBinsByGenusTypeRequest extends jspb.Message {
  hasBinGenusType(): boolean;
  clearBinGenusType(): void;
  getBinGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBinGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByGenusTypeRequest): GetBinsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetBinsByGenusTypeRequest, reader: jspb.BinaryReader): GetBinsByGenusTypeRequest;
}

export namespace GetBinsByGenusTypeRequest {
  export type AsObject = {
    binGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBinsByParentGenusTypeRequest extends jspb.Message {
  hasBinGenusType(): boolean;
  clearBinGenusType(): void;
  getBinGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBinGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByParentGenusTypeRequest): GetBinsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetBinsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetBinsByParentGenusTypeRequest;
}

export namespace GetBinsByParentGenusTypeRequest {
  export type AsObject = {
    binGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBinsByRecordTypeRequest extends jspb.Message {
  hasBinRecordType(): boolean;
  clearBinRecordType(): void;
  getBinRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBinRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByRecordTypeRequest): GetBinsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetBinsByRecordTypeRequest, reader: jspb.BinaryReader): GetBinsByRecordTypeRequest;
}

export namespace GetBinsByRecordTypeRequest {
  export type AsObject = {
    binRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBinsByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByProviderRequest): GetBinsByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByProviderRequest;
  static deserializeBinaryFromReader(message: GetBinsByProviderRequest, reader: jspb.BinaryReader): GetBinsByProviderRequest;
}

export namespace GetBinsByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsRequest): GetBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsRequest;
  static deserializeBinaryFromReader(message: GetBinsRequest, reader: jspb.BinaryReader): GetBinsRequest;
}

export namespace GetBinsRequest {
  export type AsObject = {
  }
}

export class CanSearchBinsReply extends jspb.Message {
  getCanSearchBins(): boolean;
  setCanSearchBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchBinsReply): CanSearchBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchBinsReply;
  static deserializeBinaryFromReader(message: CanSearchBinsReply, reader: jspb.BinaryReader): CanSearchBinsReply;
}

export namespace CanSearchBinsReply {
  export type AsObject = {
    canSearchBins: boolean,
  }
}

export class CanSearchBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchBinsRequest): CanSearchBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchBinsRequest;
  static deserializeBinaryFromReader(message: CanSearchBinsRequest, reader: jspb.BinaryReader): CanSearchBinsRequest;
}

export namespace CanSearchBinsRequest {
  export type AsObject = {
  }
}

export class GetBinQueryReply extends jspb.Message {
  hasBinQuery(): boolean;
  clearBinQuery(): void;
  getBinQuery(): BinQuery | undefined;
  setBinQuery(value?: BinQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinQueryReply): GetBinQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinQueryReply;
  static deserializeBinaryFromReader(message: GetBinQueryReply, reader: jspb.BinaryReader): GetBinQueryReply;
}

export namespace GetBinQueryReply {
  export type AsObject = {
    binQuery?: BinQuery.AsObject,
  }
}

export class GetBinQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinQueryRequest): GetBinQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinQueryRequest;
  static deserializeBinaryFromReader(message: GetBinQueryRequest, reader: jspb.BinaryReader): GetBinQueryRequest;
}

export namespace GetBinQueryRequest {
  export type AsObject = {
  }
}

export class GetBinsByQueryRequest extends jspb.Message {
  hasBinQuery(): boolean;
  clearBinQuery(): void;
  getBinQuery(): BinQuery | undefined;
  setBinQuery(value?: BinQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinsByQueryRequest): GetBinsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinsByQueryRequest;
  static deserializeBinaryFromReader(message: GetBinsByQueryRequest, reader: jspb.BinaryReader): GetBinsByQueryRequest;
}

export namespace GetBinsByQueryRequest {
  export type AsObject = {
    binQuery?: BinQuery.AsObject,
  }
}

export class CanCreateBinsReply extends jspb.Message {
  getCanCreateBins(): boolean;
  setCanCreateBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBinsReply): CanCreateBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBinsReply;
  static deserializeBinaryFromReader(message: CanCreateBinsReply, reader: jspb.BinaryReader): CanCreateBinsReply;
}

export namespace CanCreateBinsReply {
  export type AsObject = {
    canCreateBins: boolean,
  }
}

export class CanCreateBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBinsRequest): CanCreateBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBinsRequest;
  static deserializeBinaryFromReader(message: CanCreateBinsRequest, reader: jspb.BinaryReader): CanCreateBinsRequest;
}

export namespace CanCreateBinsRequest {
  export type AsObject = {
  }
}

export class CanCreateBinWithRecordTypesReply extends jspb.Message {
  getCanCreateBinWithRecordTypes(): boolean;
  setCanCreateBinWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBinWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBinWithRecordTypesReply): CanCreateBinWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBinWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBinWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateBinWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateBinWithRecordTypesReply;
}

export namespace CanCreateBinWithRecordTypesReply {
  export type AsObject = {
    canCreateBinWithRecordTypes: boolean,
  }
}

export class CanCreateBinWithRecordTypesRequest extends jspb.Message {
  clearBinRecordTypesList(): void;
  getBinRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setBinRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addBinRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBinWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBinWithRecordTypesRequest): CanCreateBinWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBinWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBinWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateBinWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateBinWithRecordTypesRequest;
}

export namespace CanCreateBinWithRecordTypesRequest {
  export type AsObject = {
    binRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetBinFormForCreateReply extends jspb.Message {
  hasBinForm(): boolean;
  clearBinForm(): void;
  getBinForm(): BinForm | undefined;
  setBinForm(value?: BinForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinFormForCreateReply): GetBinFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinFormForCreateReply;
  static deserializeBinaryFromReader(message: GetBinFormForCreateReply, reader: jspb.BinaryReader): GetBinFormForCreateReply;
}

export namespace GetBinFormForCreateReply {
  export type AsObject = {
    binForm?: BinForm.AsObject,
  }
}

export class GetBinFormForCreateRequest extends jspb.Message {
  clearBinRecordTypesList(): void;
  getBinRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setBinRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addBinRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinFormForCreateRequest): GetBinFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetBinFormForCreateRequest, reader: jspb.BinaryReader): GetBinFormForCreateRequest;
}

export namespace GetBinFormForCreateRequest {
  export type AsObject = {
    binRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateBinReply extends jspb.Message {
  hasBin(): boolean;
  clearBin(): void;
  getBin(): Bin | undefined;
  setBin(value?: Bin): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateBinReply): CreateBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateBinReply;
  static deserializeBinaryFromReader(message: CreateBinReply, reader: jspb.BinaryReader): CreateBinReply;
}

export namespace CreateBinReply {
  export type AsObject = {
    bin?: Bin.AsObject,
  }
}

export class CreateBinRequest extends jspb.Message {
  hasBinForm(): boolean;
  clearBinForm(): void;
  getBinForm(): BinForm | undefined;
  setBinForm(value?: BinForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateBinRequest): CreateBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateBinRequest;
  static deserializeBinaryFromReader(message: CreateBinRequest, reader: jspb.BinaryReader): CreateBinRequest;
}

export namespace CreateBinRequest {
  export type AsObject = {
    binForm?: BinForm.AsObject,
  }
}

export class CanUpdateBinsReply extends jspb.Message {
  getCanUpdateBins(): boolean;
  setCanUpdateBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateBinsReply): CanUpdateBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateBinsReply;
  static deserializeBinaryFromReader(message: CanUpdateBinsReply, reader: jspb.BinaryReader): CanUpdateBinsReply;
}

export namespace CanUpdateBinsReply {
  export type AsObject = {
    canUpdateBins: boolean,
  }
}

export class CanUpdateBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateBinsRequest): CanUpdateBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateBinsRequest;
  static deserializeBinaryFromReader(message: CanUpdateBinsRequest, reader: jspb.BinaryReader): CanUpdateBinsRequest;
}

export namespace CanUpdateBinsRequest {
  export type AsObject = {
  }
}

export class GetBinFormForUpdateReply extends jspb.Message {
  hasBinForm(): boolean;
  clearBinForm(): void;
  getBinForm(): BinForm | undefined;
  setBinForm(value?: BinForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinFormForUpdateReply): GetBinFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetBinFormForUpdateReply, reader: jspb.BinaryReader): GetBinFormForUpdateReply;
}

export namespace GetBinFormForUpdateReply {
  export type AsObject = {
    binForm?: BinForm.AsObject,
  }
}

export class GetBinFormForUpdateRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinFormForUpdateRequest): GetBinFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetBinFormForUpdateRequest, reader: jspb.BinaryReader): GetBinFormForUpdateRequest;
}

export namespace GetBinFormForUpdateRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateBinReply): UpdateBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateBinReply;
  static deserializeBinaryFromReader(message: UpdateBinReply, reader: jspb.BinaryReader): UpdateBinReply;
}

export namespace UpdateBinReply {
  export type AsObject = {
  }
}

export class UpdateBinRequest extends jspb.Message {
  hasBinForm(): boolean;
  clearBinForm(): void;
  getBinForm(): BinForm | undefined;
  setBinForm(value?: BinForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateBinRequest): UpdateBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateBinRequest;
  static deserializeBinaryFromReader(message: UpdateBinRequest, reader: jspb.BinaryReader): UpdateBinRequest;
}

export namespace UpdateBinRequest {
  export type AsObject = {
    binForm?: BinForm.AsObject,
  }
}

export class CanDeleteBinsReply extends jspb.Message {
  getCanDeleteBins(): boolean;
  setCanDeleteBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteBinsReply): CanDeleteBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteBinsReply;
  static deserializeBinaryFromReader(message: CanDeleteBinsReply, reader: jspb.BinaryReader): CanDeleteBinsReply;
}

export namespace CanDeleteBinsReply {
  export type AsObject = {
    canDeleteBins: boolean,
  }
}

export class CanDeleteBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteBinsRequest): CanDeleteBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteBinsRequest;
  static deserializeBinaryFromReader(message: CanDeleteBinsRequest, reader: jspb.BinaryReader): CanDeleteBinsRequest;
}

export namespace CanDeleteBinsRequest {
  export type AsObject = {
  }
}

export class DeleteBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteBinReply): DeleteBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteBinReply;
  static deserializeBinaryFromReader(message: DeleteBinReply, reader: jspb.BinaryReader): DeleteBinReply;
}

export namespace DeleteBinReply {
  export type AsObject = {
  }
}

export class DeleteBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteBinRequest): DeleteBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteBinRequest;
  static deserializeBinaryFromReader(message: DeleteBinRequest, reader: jspb.BinaryReader): DeleteBinRequest;
}

export namespace DeleteBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageBinAliasesReply extends jspb.Message {
  getCanManageBinAliases(): boolean;
  setCanManageBinAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageBinAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageBinAliasesReply): CanManageBinAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageBinAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageBinAliasesReply;
  static deserializeBinaryFromReader(message: CanManageBinAliasesReply, reader: jspb.BinaryReader): CanManageBinAliasesReply;
}

export namespace CanManageBinAliasesReply {
  export type AsObject = {
    canManageBinAliases: boolean,
  }
}

export class CanManageBinAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageBinAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageBinAliasesRequest): CanManageBinAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageBinAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageBinAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageBinAliasesRequest, reader: jspb.BinaryReader): CanManageBinAliasesRequest;
}

export namespace CanManageBinAliasesRequest {
  export type AsObject = {
  }
}

export class AliasBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasBinReply): AliasBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasBinReply;
  static deserializeBinaryFromReader(message: AliasBinReply, reader: jspb.BinaryReader): AliasBinReply;
}

export namespace AliasBinReply {
  export type AsObject = {
  }
}

export class AliasBinRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasBinRequest): AliasBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasBinRequest;
  static deserializeBinaryFromReader(message: AliasBinRequest, reader: jspb.BinaryReader): AliasBinRequest;
}

export namespace AliasBinRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBinHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinHierarchyIdReply): GetBinHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetBinHierarchyIdReply, reader: jspb.BinaryReader): GetBinHierarchyIdReply;
}

export namespace GetBinHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBinHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinHierarchyIdRequest): GetBinHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetBinHierarchyIdRequest, reader: jspb.BinaryReader): GetBinHierarchyIdRequest;
}

export namespace GetBinHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetBinHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinHierarchyReply): GetBinHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinHierarchyReply;
  static deserializeBinaryFromReader(message: GetBinHierarchyReply, reader: jspb.BinaryReader): GetBinHierarchyReply;
}

export namespace GetBinHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetBinHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinHierarchyRequest): GetBinHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinHierarchyRequest;
  static deserializeBinaryFromReader(message: GetBinHierarchyRequest, reader: jspb.BinaryReader): GetBinHierarchyRequest;
}

export namespace GetBinHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessBinHierarchyReply extends jspb.Message {
  getCanAccessBinHierarchy(): boolean;
  setCanAccessBinHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessBinHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessBinHierarchyReply): CanAccessBinHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessBinHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessBinHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessBinHierarchyReply, reader: jspb.BinaryReader): CanAccessBinHierarchyReply;
}

export namespace CanAccessBinHierarchyReply {
  export type AsObject = {
    canAccessBinHierarchy: boolean,
  }
}

export class CanAccessBinHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessBinHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessBinHierarchyRequest): CanAccessBinHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessBinHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessBinHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessBinHierarchyRequest, reader: jspb.BinaryReader): CanAccessBinHierarchyRequest;
}

export namespace CanAccessBinHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootBinIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootBinIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootBinIdsRequest): GetRootBinIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootBinIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootBinIdsRequest;
  static deserializeBinaryFromReader(message: GetRootBinIdsRequest, reader: jspb.BinaryReader): GetRootBinIdsRequest;
}

export namespace GetRootBinIdsRequest {
  export type AsObject = {
  }
}

export class GetRootBinsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootBinsRequest): GetRootBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootBinsRequest;
  static deserializeBinaryFromReader(message: GetRootBinsRequest, reader: jspb.BinaryReader): GetRootBinsRequest;
}

export namespace GetRootBinsRequest {
  export type AsObject = {
  }
}

export class HasParentBinsReply extends jspb.Message {
  getHasParentBins(): boolean;
  setHasParentBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentBinsReply): HasParentBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentBinsReply;
  static deserializeBinaryFromReader(message: HasParentBinsReply, reader: jspb.BinaryReader): HasParentBinsReply;
}

export namespace HasParentBinsReply {
  export type AsObject = {
    hasParentBins: boolean,
  }
}

export class HasParentBinsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentBinsRequest): HasParentBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentBinsRequest;
  static deserializeBinaryFromReader(message: HasParentBinsRequest, reader: jspb.BinaryReader): HasParentBinsRequest;
}

export namespace HasParentBinsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfBinReply extends jspb.Message {
  getIsParentOfBin(): boolean;
  setIsParentOfBin(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfBinReply): IsParentOfBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfBinReply;
  static deserializeBinaryFromReader(message: IsParentOfBinReply, reader: jspb.BinaryReader): IsParentOfBinReply;
}

export namespace IsParentOfBinReply {
  export type AsObject = {
    isParentOfBin: boolean,
  }
}

export class IsParentOfBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfBinRequest): IsParentOfBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfBinRequest;
  static deserializeBinaryFromReader(message: IsParentOfBinRequest, reader: jspb.BinaryReader): IsParentOfBinRequest;
}

export namespace IsParentOfBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentBinIdsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentBinIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentBinIdsRequest): GetParentBinIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentBinIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentBinIdsRequest;
  static deserializeBinaryFromReader(message: GetParentBinIdsRequest, reader: jspb.BinaryReader): GetParentBinIdsRequest;
}

export namespace GetParentBinIdsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentBinsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentBinsRequest): GetParentBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentBinsRequest;
  static deserializeBinaryFromReader(message: GetParentBinsRequest, reader: jspb.BinaryReader): GetParentBinsRequest;
}

export namespace GetParentBinsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfBinReply extends jspb.Message {
  getIsAncestorOfBin(): boolean;
  setIsAncestorOfBin(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfBinReply): IsAncestorOfBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfBinReply;
  static deserializeBinaryFromReader(message: IsAncestorOfBinReply, reader: jspb.BinaryReader): IsAncestorOfBinReply;
}

export namespace IsAncestorOfBinReply {
  export type AsObject = {
    isAncestorOfBin: boolean,
  }
}

export class IsAncestorOfBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfBinRequest): IsAncestorOfBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfBinRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfBinRequest, reader: jspb.BinaryReader): IsAncestorOfBinRequest;
}

export namespace IsAncestorOfBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildBinsReply extends jspb.Message {
  getHasChildBins(): boolean;
  setHasChildBins(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildBinsReply): HasChildBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildBinsReply;
  static deserializeBinaryFromReader(message: HasChildBinsReply, reader: jspb.BinaryReader): HasChildBinsReply;
}

export namespace HasChildBinsReply {
  export type AsObject = {
    hasChildBins: boolean,
  }
}

export class HasChildBinsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildBinsRequest): HasChildBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildBinsRequest;
  static deserializeBinaryFromReader(message: HasChildBinsRequest, reader: jspb.BinaryReader): HasChildBinsRequest;
}

export namespace HasChildBinsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfBinReply extends jspb.Message {
  getIsChildOfBin(): boolean;
  setIsChildOfBin(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfBinReply): IsChildOfBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfBinReply;
  static deserializeBinaryFromReader(message: IsChildOfBinReply, reader: jspb.BinaryReader): IsChildOfBinReply;
}

export namespace IsChildOfBinReply {
  export type AsObject = {
    isChildOfBin: boolean,
  }
}

export class IsChildOfBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfBinRequest): IsChildOfBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfBinRequest;
  static deserializeBinaryFromReader(message: IsChildOfBinRequest, reader: jspb.BinaryReader): IsChildOfBinRequest;
}

export namespace IsChildOfBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildBinIdsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildBinIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildBinIdsRequest): GetChildBinIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildBinIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildBinIdsRequest;
  static deserializeBinaryFromReader(message: GetChildBinIdsRequest, reader: jspb.BinaryReader): GetChildBinIdsRequest;
}

export namespace GetChildBinIdsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildBinsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildBinsRequest): GetChildBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildBinsRequest;
  static deserializeBinaryFromReader(message: GetChildBinsRequest, reader: jspb.BinaryReader): GetChildBinsRequest;
}

export namespace GetChildBinsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfBinReply extends jspb.Message {
  getIsDescendantOfBin(): boolean;
  setIsDescendantOfBin(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfBinReply): IsDescendantOfBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfBinReply;
  static deserializeBinaryFromReader(message: IsDescendantOfBinReply, reader: jspb.BinaryReader): IsDescendantOfBinReply;
}

export namespace IsDescendantOfBinReply {
  export type AsObject = {
    isDescendantOfBin: boolean,
  }
}

export class IsDescendantOfBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfBinRequest): IsDescendantOfBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfBinRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfBinRequest, reader: jspb.BinaryReader): IsDescendantOfBinRequest;
}

export namespace IsDescendantOfBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBinNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinNodeIdsReply): GetBinNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinNodeIdsReply;
  static deserializeBinaryFromReader(message: GetBinNodeIdsReply, reader: jspb.BinaryReader): GetBinNodeIdsReply;
}

export namespace GetBinNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetBinNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinNodeIdsRequest): GetBinNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetBinNodeIdsRequest, reader: jspb.BinaryReader): GetBinNodeIdsRequest;
}

export namespace GetBinNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class GetBinNodesReply extends jspb.Message {
  hasBinNode(): boolean;
  clearBinNode(): void;
  getBinNode(): BinNode | undefined;
  setBinNode(value?: BinNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinNodesReply): GetBinNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinNodesReply;
  static deserializeBinaryFromReader(message: GetBinNodesReply, reader: jspb.BinaryReader): GetBinNodesReply;
}

export namespace GetBinNodesReply {
  export type AsObject = {
    binNode?: BinNode.AsObject,
  }
}

export class GetBinNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBinNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBinNodesRequest): GetBinNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBinNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBinNodesRequest;
  static deserializeBinaryFromReader(message: GetBinNodesRequest, reader: jspb.BinaryReader): GetBinNodesRequest;
}

export namespace GetBinNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class CanModifyBinHierarchyReply extends jspb.Message {
  getCanModifyBinHierarchy(): boolean;
  setCanModifyBinHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyBinHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyBinHierarchyReply): CanModifyBinHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyBinHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyBinHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyBinHierarchyReply, reader: jspb.BinaryReader): CanModifyBinHierarchyReply;
}

export namespace CanModifyBinHierarchyReply {
  export type AsObject = {
    canModifyBinHierarchy: boolean,
  }
}

export class CanModifyBinHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyBinHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyBinHierarchyRequest): CanModifyBinHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyBinHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyBinHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyBinHierarchyRequest, reader: jspb.BinaryReader): CanModifyBinHierarchyRequest;
}

export namespace CanModifyBinHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootBinReply): AddRootBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootBinReply;
  static deserializeBinaryFromReader(message: AddRootBinReply, reader: jspb.BinaryReader): AddRootBinReply;
}

export namespace AddRootBinReply {
  export type AsObject = {
  }
}

export class AddRootBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootBinRequest): AddRootBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootBinRequest;
  static deserializeBinaryFromReader(message: AddRootBinRequest, reader: jspb.BinaryReader): AddRootBinRequest;
}

export namespace AddRootBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootBinReply): RemoveRootBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootBinReply;
  static deserializeBinaryFromReader(message: RemoveRootBinReply, reader: jspb.BinaryReader): RemoveRootBinReply;
}

export namespace RemoveRootBinReply {
  export type AsObject = {
  }
}

export class RemoveRootBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootBinRequest): RemoveRootBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootBinRequest;
  static deserializeBinaryFromReader(message: RemoveRootBinRequest, reader: jspb.BinaryReader): RemoveRootBinRequest;
}

export namespace RemoveRootBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildBinReply): AddChildBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildBinReply;
  static deserializeBinaryFromReader(message: AddChildBinReply, reader: jspb.BinaryReader): AddChildBinReply;
}

export namespace AddChildBinReply {
  export type AsObject = {
  }
}

export class AddChildBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildBinRequest): AddChildBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildBinRequest;
  static deserializeBinaryFromReader(message: AddChildBinRequest, reader: jspb.BinaryReader): AddChildBinRequest;
}

export namespace AddChildBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildBinReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBinReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBinReply): RemoveChildBinReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBinReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBinReply;
  static deserializeBinaryFromReader(message: RemoveChildBinReply, reader: jspb.BinaryReader): RemoveChildBinReply;
}

export namespace RemoveChildBinReply {
  export type AsObject = {
  }
}

export class RemoveChildBinRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBinRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBinRequest): RemoveChildBinRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBinRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBinRequest;
  static deserializeBinaryFromReader(message: RemoveChildBinRequest, reader: jspb.BinaryReader): RemoveChildBinRequest;
}

export namespace RemoveChildBinRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildBinsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBinsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBinsReply): RemoveChildBinsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBinsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBinsReply;
  static deserializeBinaryFromReader(message: RemoveChildBinsReply, reader: jspb.BinaryReader): RemoveChildBinsReply;
}

export namespace RemoveChildBinsReply {
  export type AsObject = {
  }
}

export class RemoveChildBinsRequest extends jspb.Message {
  hasBinId(): boolean;
  clearBinId(): void;
  getBinId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBinId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBinsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBinsRequest): RemoveChildBinsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBinsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBinsRequest;
  static deserializeBinaryFromReader(message: RemoveChildBinsRequest, reader: jspb.BinaryReader): RemoveChildBinsRequest;
}

export namespace RemoveChildBinsRequest {
  export type AsObject = {
    binId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

