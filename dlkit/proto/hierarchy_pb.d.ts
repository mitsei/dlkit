// package: dlkit.proto.hierarchy
// file: dlkit/proto/hierarchy.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";

export class Hierarchy extends jspb.Message {
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
  toObject(includeInstance?: boolean): Hierarchy.AsObject;
  static toObject(includeInstance: boolean, msg: Hierarchy): Hierarchy.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Hierarchy, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Hierarchy;
  static deserializeBinaryFromReader(message: Hierarchy, reader: jspb.BinaryReader): Hierarchy;
}

export namespace Hierarchy {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class HierarchyQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchyQuery.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchyQuery): HierarchyQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchyQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchyQuery;
  static deserializeBinaryFromReader(message: HierarchyQuery, reader: jspb.BinaryReader): HierarchyQuery;
}

export namespace HierarchyQuery {
  export type AsObject = {
  }
}

export class HierarchyQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchyQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchyQueryInspector): HierarchyQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchyQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchyQueryInspector;
  static deserializeBinaryFromReader(message: HierarchyQueryInspector, reader: jspb.BinaryReader): HierarchyQueryInspector;
}

export namespace HierarchyQueryInspector {
  export type AsObject = {
  }
}

export class HierarchyForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchyForm.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchyForm): HierarchyForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchyForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchyForm;
  static deserializeBinaryFromReader(message: HierarchyForm, reader: jspb.BinaryReader): HierarchyForm;
}

export namespace HierarchyForm {
  export type AsObject = {
  }
}

export class HierarchySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchySearchOrder): HierarchySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchySearchOrder;
  static deserializeBinaryFromReader(message: HierarchySearchOrder, reader: jspb.BinaryReader): HierarchySearchOrder;
}

export namespace HierarchySearchOrder {
  export type AsObject = {
  }
}

export class HierarchySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchySearch.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchySearch): HierarchySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchySearch;
  static deserializeBinaryFromReader(message: HierarchySearch, reader: jspb.BinaryReader): HierarchySearch;
}

export namespace HierarchySearch {
  export type AsObject = {
  }
}

export class HierarchySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchySearchResults): HierarchySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchySearchResults;
  static deserializeBinaryFromReader(message: HierarchySearchResults, reader: jspb.BinaryReader): HierarchySearchResults;
}

export namespace HierarchySearchResults {
  export type AsObject = {
  }
}

export class HierarchyList extends jspb.Message {
  clearHierarchiesList(): void;
  getHierarchiesList(): Array<Hierarchy>;
  setHierarchiesList(value: Array<Hierarchy>): void;
  addHierarchies(value?: Hierarchy, index?: number): Hierarchy;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HierarchyList.AsObject;
  static toObject(includeInstance: boolean, msg: HierarchyList): HierarchyList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HierarchyList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HierarchyList;
  static deserializeBinaryFromReader(message: HierarchyList, reader: jspb.BinaryReader): HierarchyList;
}

export namespace HierarchyList {
  export type AsObject = {
    hierarchiesList: Array<Hierarchy.AsObject>,
  }
}

export class Node extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Node.AsObject;
  static toObject(includeInstance: boolean, msg: Node): Node.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Node, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Node;
  static deserializeBinaryFromReader(message: Node, reader: jspb.BinaryReader): Node;
}

export namespace Node {
  export type AsObject = {
  }
}

export class NodeList extends jspb.Message {
  clearNodesList(): void;
  getNodesList(): Array<Node>;
  setNodesList(value: Array<Node>): void;
  addNodes(value?: Node, index?: number): Node;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NodeList.AsObject;
  static toObject(includeInstance: boolean, msg: NodeList): NodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: NodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NodeList;
  static deserializeBinaryFromReader(message: NodeList, reader: jspb.BinaryReader): NodeList;
}

export namespace NodeList {
  export type AsObject = {
    nodesList: Array<Node.AsObject>,
  }
}

export class GetHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyIdReply): GetHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetHierarchyIdReply, reader: jspb.BinaryReader): GetHierarchyIdReply;
}

export namespace GetHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyIdRequest): GetHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetHierarchyIdRequest, reader: jspb.BinaryReader): GetHierarchyIdRequest;
}

export namespace GetHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): Hierarchy | undefined;
  setHierarchy(value?: Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyReply): GetHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyReply;
  static deserializeBinaryFromReader(message: GetHierarchyReply, reader: jspb.BinaryReader): GetHierarchyReply;
}

export namespace GetHierarchyReply {
  export type AsObject = {
    hierarchy?: Hierarchy.AsObject,
  }
}

export class GetHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyRequest): GetHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyRequest;
  static deserializeBinaryFromReader(message: GetHierarchyRequest, reader: jspb.BinaryReader): GetHierarchyRequest;
}

export namespace GetHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessHierarchyReply extends jspb.Message {
  getCanAccessHierarchy(): boolean;
  setCanAccessHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessHierarchyReply): CanAccessHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessHierarchyReply, reader: jspb.BinaryReader): CanAccessHierarchyReply;
}

export namespace CanAccessHierarchyReply {
  export type AsObject = {
    canAccessHierarchy: boolean,
  }
}

export class CanAccessHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessHierarchyRequest): CanAccessHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessHierarchyRequest, reader: jspb.BinaryReader): CanAccessHierarchyRequest;
}

export namespace CanAccessHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootsRequest): GetRootsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootsRequest;
  static deserializeBinaryFromReader(message: GetRootsRequest, reader: jspb.BinaryReader): GetRootsRequest;
}

export namespace GetRootsRequest {
  export type AsObject = {
  }
}

export class HasParentsReply extends jspb.Message {
  getHasParents(): boolean;
  setHasParents(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentsReply): HasParentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentsReply;
  static deserializeBinaryFromReader(message: HasParentsReply, reader: jspb.BinaryReader): HasParentsReply;
}

export namespace HasParentsReply {
  export type AsObject = {
    hasParents: boolean,
  }
}

export class HasParentsRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentsRequest): HasParentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentsRequest;
  static deserializeBinaryFromReader(message: HasParentsRequest, reader: jspb.BinaryReader): HasParentsRequest;
}

export namespace HasParentsRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentReply extends jspb.Message {
  getIsParent(): boolean;
  setIsParent(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentReply): IsParentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentReply;
  static deserializeBinaryFromReader(message: IsParentReply, reader: jspb.BinaryReader): IsParentReply;
}

export namespace IsParentReply {
  export type AsObject = {
    isParent: boolean,
  }
}

export class IsParentRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasParentId(): boolean;
  clearParentId(): void;
  getParentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setParentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentRequest): IsParentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentRequest;
  static deserializeBinaryFromReader(message: IsParentRequest, reader: jspb.BinaryReader): IsParentRequest;
}

export namespace IsParentRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    parentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentsRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentsRequest): GetParentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentsRequest;
  static deserializeBinaryFromReader(message: GetParentsRequest, reader: jspb.BinaryReader): GetParentsRequest;
}

export namespace GetParentsRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorReply extends jspb.Message {
  getIsAncestor(): boolean;
  setIsAncestor(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorReply): IsAncestorReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorReply;
  static deserializeBinaryFromReader(message: IsAncestorReply, reader: jspb.BinaryReader): IsAncestorReply;
}

export namespace IsAncestorReply {
  export type AsObject = {
    isAncestor: boolean,
  }
}

export class IsAncestorRequest extends jspb.Message {
  hasAncestorId(): boolean;
  clearAncestorId(): void;
  getAncestorId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAncestorId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorRequest): IsAncestorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorRequest;
  static deserializeBinaryFromReader(message: IsAncestorRequest, reader: jspb.BinaryReader): IsAncestorRequest;
}

export namespace IsAncestorRequest {
  export type AsObject = {
    ancestorId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildrenReply extends jspb.Message {
  getHasChildren(): boolean;
  setHasChildren(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildrenReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildrenReply): HasChildrenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildrenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildrenReply;
  static deserializeBinaryFromReader(message: HasChildrenReply, reader: jspb.BinaryReader): HasChildrenReply;
}

export namespace HasChildrenReply {
  export type AsObject = {
    hasChildren: boolean,
  }
}

export class HasChildrenRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildrenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildrenRequest): HasChildrenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildrenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildrenRequest;
  static deserializeBinaryFromReader(message: HasChildrenRequest, reader: jspb.BinaryReader): HasChildrenRequest;
}

export namespace HasChildrenRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildReply extends jspb.Message {
  getIsChild(): boolean;
  setIsChild(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildReply): IsChildReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildReply;
  static deserializeBinaryFromReader(message: IsChildReply, reader: jspb.BinaryReader): IsChildReply;
}

export namespace IsChildReply {
  export type AsObject = {
    isChild: boolean,
  }
}

export class IsChildRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildRequest): IsChildRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildRequest;
  static deserializeBinaryFromReader(message: IsChildRequest, reader: jspb.BinaryReader): IsChildRequest;
}

export namespace IsChildRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildrenRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildrenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildrenRequest): GetChildrenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildrenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildrenRequest;
  static deserializeBinaryFromReader(message: GetChildrenRequest, reader: jspb.BinaryReader): GetChildrenRequest;
}

export namespace GetChildrenRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantReply extends jspb.Message {
  getIsDescendant(): boolean;
  setIsDescendant(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantReply): IsDescendantReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantReply;
  static deserializeBinaryFromReader(message: IsDescendantReply, reader: jspb.BinaryReader): IsDescendantReply;
}

export namespace IsDescendantReply {
  export type AsObject = {
    isDescendant: boolean,
  }
}

export class IsDescendantRequest extends jspb.Message {
  hasDescendantId(): boolean;
  clearDescendantId(): void;
  getDescendantId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDescendantId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantRequest): IsDescendantRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantRequest;
  static deserializeBinaryFromReader(message: IsDescendantRequest, reader: jspb.BinaryReader): IsDescendantRequest;
}

export namespace IsDescendantRequest {
  export type AsObject = {
    descendantId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetNodesReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): Node | undefined;
  setNode(value?: Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetNodesReply): GetNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNodesReply;
  static deserializeBinaryFromReader(message: GetNodesReply, reader: jspb.BinaryReader): GetNodesReply;
}

export namespace GetNodesReply {
  export type AsObject = {
    node?: Node.AsObject,
  }
}

export class GetNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetNodesRequest): GetNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNodesRequest;
  static deserializeBinaryFromReader(message: GetNodesRequest, reader: jspb.BinaryReader): GetNodesRequest;
}

export namespace GetNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    includeSiblings: boolean,
  }
}

export class CanModifyHierarchyReply extends jspb.Message {
  getCanModifyHierarchy(): boolean;
  setCanModifyHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyHierarchyReply): CanModifyHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyHierarchyReply, reader: jspb.BinaryReader): CanModifyHierarchyReply;
}

export namespace CanModifyHierarchyReply {
  export type AsObject = {
    canModifyHierarchy: boolean,
  }
}

export class CanModifyHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyHierarchyRequest): CanModifyHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyHierarchyRequest, reader: jspb.BinaryReader): CanModifyHierarchyRequest;
}

export namespace CanModifyHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootReply): AddRootReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootReply;
  static deserializeBinaryFromReader(message: AddRootReply, reader: jspb.BinaryReader): AddRootReply;
}

export namespace AddRootReply {
  export type AsObject = {
  }
}

export class AddRootRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootRequest): AddRootRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootRequest;
  static deserializeBinaryFromReader(message: AddRootRequest, reader: jspb.BinaryReader): AddRootRequest;
}

export namespace AddRootRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildReply): AddChildReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildReply;
  static deserializeBinaryFromReader(message: AddChildReply, reader: jspb.BinaryReader): AddChildReply;
}

export namespace AddChildReply {
  export type AsObject = {
  }
}

export class AddChildRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildRequest): AddChildRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildRequest;
  static deserializeBinaryFromReader(message: AddChildRequest, reader: jspb.BinaryReader): AddChildRequest;
}

export namespace AddChildRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootReply): RemoveRootReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootReply;
  static deserializeBinaryFromReader(message: RemoveRootReply, reader: jspb.BinaryReader): RemoveRootReply;
}

export namespace RemoveRootReply {
  export type AsObject = {
  }
}

export class RemoveRootRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootRequest): RemoveRootRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootRequest;
  static deserializeBinaryFromReader(message: RemoveRootRequest, reader: jspb.BinaryReader): RemoveRootRequest;
}

export namespace RemoveRootRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildReply): RemoveChildReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildReply;
  static deserializeBinaryFromReader(message: RemoveChildReply, reader: jspb.BinaryReader): RemoveChildReply;
}

export namespace RemoveChildReply {
  export type AsObject = {
  }
}

export class RemoveChildRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildRequest): RemoveChildRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildRequest;
  static deserializeBinaryFromReader(message: RemoveChildRequest, reader: jspb.BinaryReader): RemoveChildRequest;
}

export namespace RemoveChildRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildrenReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildrenReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildrenReply): RemoveChildrenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildrenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildrenReply;
  static deserializeBinaryFromReader(message: RemoveChildrenReply, reader: jspb.BinaryReader): RemoveChildrenReply;
}

export namespace RemoveChildrenReply {
  export type AsObject = {
  }
}

export class RemoveChildrenRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildrenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildrenRequest): RemoveChildrenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildrenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildrenRequest;
  static deserializeBinaryFromReader(message: RemoveChildrenRequest, reader: jspb.BinaryReader): RemoveChildrenRequest;
}

export namespace RemoveChildrenRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupHierarchiesReply extends jspb.Message {
  getCanLookupHierarchies(): boolean;
  setCanLookupHierarchies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupHierarchiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupHierarchiesReply): CanLookupHierarchiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupHierarchiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupHierarchiesReply;
  static deserializeBinaryFromReader(message: CanLookupHierarchiesReply, reader: jspb.BinaryReader): CanLookupHierarchiesReply;
}

export namespace CanLookupHierarchiesReply {
  export type AsObject = {
    canLookupHierarchies: boolean,
  }
}

export class CanLookupHierarchiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupHierarchiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupHierarchiesRequest): CanLookupHierarchiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupHierarchiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupHierarchiesRequest;
  static deserializeBinaryFromReader(message: CanLookupHierarchiesRequest, reader: jspb.BinaryReader): CanLookupHierarchiesRequest;
}

export namespace CanLookupHierarchiesRequest {
  export type AsObject = {
  }
}

export class UseComparativeHierarchyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeHierarchyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeHierarchyViewReply): UseComparativeHierarchyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeHierarchyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeHierarchyViewReply;
  static deserializeBinaryFromReader(message: UseComparativeHierarchyViewReply, reader: jspb.BinaryReader): UseComparativeHierarchyViewReply;
}

export namespace UseComparativeHierarchyViewReply {
  export type AsObject = {
  }
}

export class UseComparativeHierarchyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeHierarchyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeHierarchyViewRequest): UseComparativeHierarchyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeHierarchyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeHierarchyViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeHierarchyViewRequest, reader: jspb.BinaryReader): UseComparativeHierarchyViewRequest;
}

export namespace UseComparativeHierarchyViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryHierarchyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryHierarchyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryHierarchyViewReply): UsePlenaryHierarchyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryHierarchyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryHierarchyViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryHierarchyViewReply, reader: jspb.BinaryReader): UsePlenaryHierarchyViewReply;
}

export namespace UsePlenaryHierarchyViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryHierarchyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryHierarchyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryHierarchyViewRequest): UsePlenaryHierarchyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryHierarchyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryHierarchyViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryHierarchyViewRequest, reader: jspb.BinaryReader): UsePlenaryHierarchyViewRequest;
}

export namespace UsePlenaryHierarchyViewRequest {
  export type AsObject = {
  }
}

export class GetHierarchiesByIdsRequest extends jspb.Message {
  clearHierarchyIdsList(): void;
  getHierarchyIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setHierarchyIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addHierarchyIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchiesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchiesByIdsRequest): GetHierarchiesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchiesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchiesByIdsRequest;
  static deserializeBinaryFromReader(message: GetHierarchiesByIdsRequest, reader: jspb.BinaryReader): GetHierarchiesByIdsRequest;
}

export namespace GetHierarchiesByIdsRequest {
  export type AsObject = {
    hierarchyIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetHierarchiesByGenusTypeRequest extends jspb.Message {
  hasHierarchyGenusType(): boolean;
  clearHierarchyGenusType(): void;
  getHierarchyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setHierarchyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchiesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchiesByGenusTypeRequest): GetHierarchiesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchiesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchiesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetHierarchiesByGenusTypeRequest, reader: jspb.BinaryReader): GetHierarchiesByGenusTypeRequest;
}

export namespace GetHierarchiesByGenusTypeRequest {
  export type AsObject = {
    hierarchyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetHierarchiesByParentGenusTypeRequest extends jspb.Message {
  hasHierarchyGenusType(): boolean;
  clearHierarchyGenusType(): void;
  getHierarchyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setHierarchyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchiesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchiesByParentGenusTypeRequest): GetHierarchiesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchiesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchiesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetHierarchiesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetHierarchiesByParentGenusTypeRequest;
}

export namespace GetHierarchiesByParentGenusTypeRequest {
  export type AsObject = {
    hierarchyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetHierarchiesByRecordTypeRequest extends jspb.Message {
  hasHierarchyRecordType(): boolean;
  clearHierarchyRecordType(): void;
  getHierarchyRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setHierarchyRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchiesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchiesByRecordTypeRequest): GetHierarchiesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchiesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchiesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetHierarchiesByRecordTypeRequest, reader: jspb.BinaryReader): GetHierarchiesByRecordTypeRequest;
}

export namespace GetHierarchiesByRecordTypeRequest {
  export type AsObject = {
    hierarchyRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetHierarchiesByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchiesByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchiesByProviderRequest): GetHierarchiesByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchiesByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchiesByProviderRequest;
  static deserializeBinaryFromReader(message: GetHierarchiesByProviderRequest, reader: jspb.BinaryReader): GetHierarchiesByProviderRequest;
}

export namespace GetHierarchiesByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetHierarchiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchiesRequest): GetHierarchiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchiesRequest;
  static deserializeBinaryFromReader(message: GetHierarchiesRequest, reader: jspb.BinaryReader): GetHierarchiesRequest;
}

export namespace GetHierarchiesRequest {
  export type AsObject = {
  }
}

export class CanCreateHierarchiesReply extends jspb.Message {
  getCanCreateHierarchies(): boolean;
  setCanCreateHierarchies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateHierarchiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateHierarchiesReply): CanCreateHierarchiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateHierarchiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateHierarchiesReply;
  static deserializeBinaryFromReader(message: CanCreateHierarchiesReply, reader: jspb.BinaryReader): CanCreateHierarchiesReply;
}

export namespace CanCreateHierarchiesReply {
  export type AsObject = {
    canCreateHierarchies: boolean,
  }
}

export class CanCreateHierarchiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateHierarchiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateHierarchiesRequest): CanCreateHierarchiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateHierarchiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateHierarchiesRequest;
  static deserializeBinaryFromReader(message: CanCreateHierarchiesRequest, reader: jspb.BinaryReader): CanCreateHierarchiesRequest;
}

export namespace CanCreateHierarchiesRequest {
  export type AsObject = {
  }
}

export class CanCreateHierarchyWithRecordTypesReply extends jspb.Message {
  getCanCreateHierarchyWithRecordTypes(): boolean;
  setCanCreateHierarchyWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateHierarchyWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateHierarchyWithRecordTypesReply): CanCreateHierarchyWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateHierarchyWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateHierarchyWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateHierarchyWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateHierarchyWithRecordTypesReply;
}

export namespace CanCreateHierarchyWithRecordTypesReply {
  export type AsObject = {
    canCreateHierarchyWithRecordTypes: boolean,
  }
}

export class CanCreateHierarchyWithRecordTypesRequest extends jspb.Message {
  clearHierarchyRecordTypesList(): void;
  getHierarchyRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setHierarchyRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addHierarchyRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateHierarchyWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateHierarchyWithRecordTypesRequest): CanCreateHierarchyWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateHierarchyWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateHierarchyWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateHierarchyWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateHierarchyWithRecordTypesRequest;
}

export namespace CanCreateHierarchyWithRecordTypesRequest {
  export type AsObject = {
    hierarchyRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetHierarchyFormForCreateReply extends jspb.Message {
  hasHierarchyForm(): boolean;
  clearHierarchyForm(): void;
  getHierarchyForm(): HierarchyForm | undefined;
  setHierarchyForm(value?: HierarchyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyFormForCreateReply): GetHierarchyFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyFormForCreateReply;
  static deserializeBinaryFromReader(message: GetHierarchyFormForCreateReply, reader: jspb.BinaryReader): GetHierarchyFormForCreateReply;
}

export namespace GetHierarchyFormForCreateReply {
  export type AsObject = {
    hierarchyForm?: HierarchyForm.AsObject,
  }
}

export class GetHierarchyFormForCreateRequest extends jspb.Message {
  clearHierarchyRecordTypesList(): void;
  getHierarchyRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setHierarchyRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addHierarchyRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyFormForCreateRequest): GetHierarchyFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetHierarchyFormForCreateRequest, reader: jspb.BinaryReader): GetHierarchyFormForCreateRequest;
}

export namespace GetHierarchyFormForCreateRequest {
  export type AsObject = {
    hierarchyRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): Hierarchy | undefined;
  setHierarchy(value?: Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateHierarchyReply): CreateHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateHierarchyReply;
  static deserializeBinaryFromReader(message: CreateHierarchyReply, reader: jspb.BinaryReader): CreateHierarchyReply;
}

export namespace CreateHierarchyReply {
  export type AsObject = {
    hierarchy?: Hierarchy.AsObject,
  }
}

export class CreateHierarchyRequest extends jspb.Message {
  hasHierarchyForm(): boolean;
  clearHierarchyForm(): void;
  getHierarchyForm(): HierarchyForm | undefined;
  setHierarchyForm(value?: HierarchyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateHierarchyRequest): CreateHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateHierarchyRequest;
  static deserializeBinaryFromReader(message: CreateHierarchyRequest, reader: jspb.BinaryReader): CreateHierarchyRequest;
}

export namespace CreateHierarchyRequest {
  export type AsObject = {
    hierarchyForm?: HierarchyForm.AsObject,
  }
}

export class CanUpdateHierarchiesReply extends jspb.Message {
  getCanUpdateHierarchies(): boolean;
  setCanUpdateHierarchies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateHierarchiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateHierarchiesReply): CanUpdateHierarchiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateHierarchiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateHierarchiesReply;
  static deserializeBinaryFromReader(message: CanUpdateHierarchiesReply, reader: jspb.BinaryReader): CanUpdateHierarchiesReply;
}

export namespace CanUpdateHierarchiesReply {
  export type AsObject = {
    canUpdateHierarchies: boolean,
  }
}

export class CanUpdateHierarchiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateHierarchiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateHierarchiesRequest): CanUpdateHierarchiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateHierarchiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateHierarchiesRequest;
  static deserializeBinaryFromReader(message: CanUpdateHierarchiesRequest, reader: jspb.BinaryReader): CanUpdateHierarchiesRequest;
}

export namespace CanUpdateHierarchiesRequest {
  export type AsObject = {
  }
}

export class GetHierarchyFormForUpdateReply extends jspb.Message {
  hasHierarchyForm(): boolean;
  clearHierarchyForm(): void;
  getHierarchyForm(): HierarchyForm | undefined;
  setHierarchyForm(value?: HierarchyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyFormForUpdateReply): GetHierarchyFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetHierarchyFormForUpdateReply, reader: jspb.BinaryReader): GetHierarchyFormForUpdateReply;
}

export namespace GetHierarchyFormForUpdateReply {
  export type AsObject = {
    hierarchyForm?: HierarchyForm.AsObject,
  }
}

export class GetHierarchyFormForUpdateRequest extends jspb.Message {
  hasHierarchyId(): boolean;
  clearHierarchyId(): void;
  getHierarchyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setHierarchyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetHierarchyFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetHierarchyFormForUpdateRequest): GetHierarchyFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetHierarchyFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetHierarchyFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetHierarchyFormForUpdateRequest, reader: jspb.BinaryReader): GetHierarchyFormForUpdateRequest;
}

export namespace GetHierarchyFormForUpdateRequest {
  export type AsObject = {
    hierarchyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateHierarchyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateHierarchyReply): UpdateHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateHierarchyReply;
  static deserializeBinaryFromReader(message: UpdateHierarchyReply, reader: jspb.BinaryReader): UpdateHierarchyReply;
}

export namespace UpdateHierarchyReply {
  export type AsObject = {
  }
}

export class UpdateHierarchyRequest extends jspb.Message {
  hasHierarchyForm(): boolean;
  clearHierarchyForm(): void;
  getHierarchyForm(): HierarchyForm | undefined;
  setHierarchyForm(value?: HierarchyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateHierarchyRequest): UpdateHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateHierarchyRequest;
  static deserializeBinaryFromReader(message: UpdateHierarchyRequest, reader: jspb.BinaryReader): UpdateHierarchyRequest;
}

export namespace UpdateHierarchyRequest {
  export type AsObject = {
    hierarchyForm?: HierarchyForm.AsObject,
  }
}

export class CanDeleteHierarchiesReply extends jspb.Message {
  getCanDeleteHierarchies(): boolean;
  setCanDeleteHierarchies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteHierarchiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteHierarchiesReply): CanDeleteHierarchiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteHierarchiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteHierarchiesReply;
  static deserializeBinaryFromReader(message: CanDeleteHierarchiesReply, reader: jspb.BinaryReader): CanDeleteHierarchiesReply;
}

export namespace CanDeleteHierarchiesReply {
  export type AsObject = {
    canDeleteHierarchies: boolean,
  }
}

export class CanDeleteHierarchiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteHierarchiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteHierarchiesRequest): CanDeleteHierarchiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteHierarchiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteHierarchiesRequest;
  static deserializeBinaryFromReader(message: CanDeleteHierarchiesRequest, reader: jspb.BinaryReader): CanDeleteHierarchiesRequest;
}

export namespace CanDeleteHierarchiesRequest {
  export type AsObject = {
  }
}

export class DeleteHierarchyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteHierarchyReply): DeleteHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteHierarchyReply;
  static deserializeBinaryFromReader(message: DeleteHierarchyReply, reader: jspb.BinaryReader): DeleteHierarchyReply;
}

export namespace DeleteHierarchyReply {
  export type AsObject = {
  }
}

export class DeleteHierarchyRequest extends jspb.Message {
  hasHierarchyId(): boolean;
  clearHierarchyId(): void;
  getHierarchyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setHierarchyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteHierarchyRequest): DeleteHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteHierarchyRequest;
  static deserializeBinaryFromReader(message: DeleteHierarchyRequest, reader: jspb.BinaryReader): DeleteHierarchyRequest;
}

export namespace DeleteHierarchyRequest {
  export type AsObject = {
    hierarchyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageHierarchyAliasesReply extends jspb.Message {
  getCanManageHierarchyAliases(): boolean;
  setCanManageHierarchyAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageHierarchyAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageHierarchyAliasesReply): CanManageHierarchyAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageHierarchyAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageHierarchyAliasesReply;
  static deserializeBinaryFromReader(message: CanManageHierarchyAliasesReply, reader: jspb.BinaryReader): CanManageHierarchyAliasesReply;
}

export namespace CanManageHierarchyAliasesReply {
  export type AsObject = {
    canManageHierarchyAliases: boolean,
  }
}

export class CanManageHierarchyAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageHierarchyAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageHierarchyAliasesRequest): CanManageHierarchyAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageHierarchyAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageHierarchyAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageHierarchyAliasesRequest, reader: jspb.BinaryReader): CanManageHierarchyAliasesRequest;
}

export namespace CanManageHierarchyAliasesRequest {
  export type AsObject = {
  }
}

export class AliasHierarchyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasHierarchyReply): AliasHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasHierarchyReply;
  static deserializeBinaryFromReader(message: AliasHierarchyReply, reader: jspb.BinaryReader): AliasHierarchyReply;
}

export namespace AliasHierarchyReply {
  export type AsObject = {
  }
}

export class AliasHierarchyRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasHierarchyId(): boolean;
  clearHierarchyId(): void;
  getHierarchyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setHierarchyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasHierarchyRequest): AliasHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasHierarchyRequest;
  static deserializeBinaryFromReader(message: AliasHierarchyRequest, reader: jspb.BinaryReader): AliasHierarchyRequest;
}

export namespace AliasHierarchyRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    hierarchyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

