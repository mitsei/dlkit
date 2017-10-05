// package: dlkit.proto.relationship
// file: dlkit/proto/relationship.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Relationship extends jspb.Message {
  hasDestination(): boolean;
  clearDestination(): void;
  getDestination(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestination(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFamily(): boolean;
  clearFamily(): void;
  getFamily(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setFamily(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasSource(): boolean;
  clearSource(): void;
  getSource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Relationship.AsObject;
  static toObject(includeInstance: boolean, msg: Relationship): Relationship.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Relationship, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Relationship;
  static deserializeBinaryFromReader(message: Relationship, reader: jspb.BinaryReader): Relationship;
}

export namespace Relationship {
  export type AsObject = {
    destination?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    family?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    source?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RelationshipQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipQuery.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipQuery): RelationshipQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipQuery;
  static deserializeBinaryFromReader(message: RelationshipQuery, reader: jspb.BinaryReader): RelationshipQuery;
}

export namespace RelationshipQuery {
  export type AsObject = {
  }
}

export class RelationshipQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipQueryInspector): RelationshipQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipQueryInspector;
  static deserializeBinaryFromReader(message: RelationshipQueryInspector, reader: jspb.BinaryReader): RelationshipQueryInspector;
}

export namespace RelationshipQueryInspector {
  export type AsObject = {
  }
}

export class RelationshipForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipForm.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipForm): RelationshipForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipForm;
  static deserializeBinaryFromReader(message: RelationshipForm, reader: jspb.BinaryReader): RelationshipForm;
}

export namespace RelationshipForm {
  export type AsObject = {
  }
}

export class RelationshipSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipSearchOrder): RelationshipSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipSearchOrder;
  static deserializeBinaryFromReader(message: RelationshipSearchOrder, reader: jspb.BinaryReader): RelationshipSearchOrder;
}

export namespace RelationshipSearchOrder {
  export type AsObject = {
  }
}

export class RelationshipSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipSearch.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipSearch): RelationshipSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipSearch;
  static deserializeBinaryFromReader(message: RelationshipSearch, reader: jspb.BinaryReader): RelationshipSearch;
}

export namespace RelationshipSearch {
  export type AsObject = {
  }
}

export class RelationshipSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipSearchResults): RelationshipSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipSearchResults;
  static deserializeBinaryFromReader(message: RelationshipSearchResults, reader: jspb.BinaryReader): RelationshipSearchResults;
}

export namespace RelationshipSearchResults {
  export type AsObject = {
  }
}

export class RelationshipList extends jspb.Message {
  clearRelationshipsList(): void;
  getRelationshipsList(): Array<Relationship>;
  setRelationshipsList(value: Array<Relationship>): void;
  addRelationships(value?: Relationship, index?: number): Relationship;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelationshipList.AsObject;
  static toObject(includeInstance: boolean, msg: RelationshipList): RelationshipList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelationshipList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelationshipList;
  static deserializeBinaryFromReader(message: RelationshipList, reader: jspb.BinaryReader): RelationshipList;
}

export namespace RelationshipList {
  export type AsObject = {
    relationshipsList: Array<Relationship.AsObject>,
  }
}

export class Family extends jspb.Message {
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
  toObject(includeInstance?: boolean): Family.AsObject;
  static toObject(includeInstance: boolean, msg: Family): Family.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Family, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Family;
  static deserializeBinaryFromReader(message: Family, reader: jspb.BinaryReader): Family;
}

export namespace Family {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class FamilyQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilyQuery.AsObject;
  static toObject(includeInstance: boolean, msg: FamilyQuery): FamilyQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilyQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilyQuery;
  static deserializeBinaryFromReader(message: FamilyQuery, reader: jspb.BinaryReader): FamilyQuery;
}

export namespace FamilyQuery {
  export type AsObject = {
  }
}

export class FamilyQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilyQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: FamilyQueryInspector): FamilyQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilyQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilyQueryInspector;
  static deserializeBinaryFromReader(message: FamilyQueryInspector, reader: jspb.BinaryReader): FamilyQueryInspector;
}

export namespace FamilyQueryInspector {
  export type AsObject = {
  }
}

export class FamilyForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilyForm.AsObject;
  static toObject(includeInstance: boolean, msg: FamilyForm): FamilyForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilyForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilyForm;
  static deserializeBinaryFromReader(message: FamilyForm, reader: jspb.BinaryReader): FamilyForm;
}

export namespace FamilyForm {
  export type AsObject = {
  }
}

export class FamilySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: FamilySearchOrder): FamilySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilySearchOrder;
  static deserializeBinaryFromReader(message: FamilySearchOrder, reader: jspb.BinaryReader): FamilySearchOrder;
}

export namespace FamilySearchOrder {
  export type AsObject = {
  }
}

export class FamilySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilySearch.AsObject;
  static toObject(includeInstance: boolean, msg: FamilySearch): FamilySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilySearch;
  static deserializeBinaryFromReader(message: FamilySearch, reader: jspb.BinaryReader): FamilySearch;
}

export namespace FamilySearch {
  export type AsObject = {
  }
}

export class FamilySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: FamilySearchResults): FamilySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilySearchResults;
  static deserializeBinaryFromReader(message: FamilySearchResults, reader: jspb.BinaryReader): FamilySearchResults;
}

export namespace FamilySearchResults {
  export type AsObject = {
  }
}

export class FamilyList extends jspb.Message {
  clearFamiliesList(): void;
  getFamiliesList(): Array<Family>;
  setFamiliesList(value: Array<Family>): void;
  addFamilies(value?: Family, index?: number): Family;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilyList.AsObject;
  static toObject(includeInstance: boolean, msg: FamilyList): FamilyList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilyList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilyList;
  static deserializeBinaryFromReader(message: FamilyList, reader: jspb.BinaryReader): FamilyList;
}

export namespace FamilyList {
  export type AsObject = {
    familiesList: Array<Family.AsObject>,
  }
}

export class FamilyNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilyNode.AsObject;
  static toObject(includeInstance: boolean, msg: FamilyNode): FamilyNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilyNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilyNode;
  static deserializeBinaryFromReader(message: FamilyNode, reader: jspb.BinaryReader): FamilyNode;
}

export namespace FamilyNode {
  export type AsObject = {
  }
}

export class FamilyNodeList extends jspb.Message {
  clearFamilyNodesList(): void;
  getFamilyNodesList(): Array<FamilyNode>;
  setFamilyNodesList(value: Array<FamilyNode>): void;
  addFamilyNodes(value?: FamilyNode, index?: number): FamilyNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FamilyNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: FamilyNodeList): FamilyNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FamilyNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FamilyNodeList;
  static deserializeBinaryFromReader(message: FamilyNodeList, reader: jspb.BinaryReader): FamilyNodeList;
}

export namespace FamilyNodeList {
  export type AsObject = {
    familyNodesList: Array<FamilyNode.AsObject>,
  }
}

export class GetFamilyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyIdReply): GetFamilyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyIdReply;
  static deserializeBinaryFromReader(message: GetFamilyIdReply, reader: jspb.BinaryReader): GetFamilyIdReply;
}

export namespace GetFamilyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFamilyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyIdRequest): GetFamilyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyIdRequest;
  static deserializeBinaryFromReader(message: GetFamilyIdRequest, reader: jspb.BinaryReader): GetFamilyIdRequest;
}

export namespace GetFamilyIdRequest {
  export type AsObject = {
  }
}

export class GetFamilyReply extends jspb.Message {
  hasFamily(): boolean;
  clearFamily(): void;
  getFamily(): Family | undefined;
  setFamily(value?: Family): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyReply): GetFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyReply;
  static deserializeBinaryFromReader(message: GetFamilyReply, reader: jspb.BinaryReader): GetFamilyReply;
}

export namespace GetFamilyReply {
  export type AsObject = {
    family?: Family.AsObject,
  }
}

export class GetFamilyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyRequest): GetFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyRequest;
  static deserializeBinaryFromReader(message: GetFamilyRequest, reader: jspb.BinaryReader): GetFamilyRequest;
}

export namespace GetFamilyRequest {
  export type AsObject = {
  }
}

export class CanLookupRelationshipsReply extends jspb.Message {
  getCanLookupRelationships(): boolean;
  setCanLookupRelationships(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupRelationshipsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupRelationshipsReply): CanLookupRelationshipsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupRelationshipsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupRelationshipsReply;
  static deserializeBinaryFromReader(message: CanLookupRelationshipsReply, reader: jspb.BinaryReader): CanLookupRelationshipsReply;
}

export namespace CanLookupRelationshipsReply {
  export type AsObject = {
    canLookupRelationships: boolean,
  }
}

export class CanLookupRelationshipsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupRelationshipsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupRelationshipsRequest): CanLookupRelationshipsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupRelationshipsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupRelationshipsRequest;
  static deserializeBinaryFromReader(message: CanLookupRelationshipsRequest, reader: jspb.BinaryReader): CanLookupRelationshipsRequest;
}

export namespace CanLookupRelationshipsRequest {
  export type AsObject = {
  }
}

export class UseComparativeRelationshipViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeRelationshipViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeRelationshipViewReply): UseComparativeRelationshipViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeRelationshipViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeRelationshipViewReply;
  static deserializeBinaryFromReader(message: UseComparativeRelationshipViewReply, reader: jspb.BinaryReader): UseComparativeRelationshipViewReply;
}

export namespace UseComparativeRelationshipViewReply {
  export type AsObject = {
  }
}

export class UseComparativeRelationshipViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeRelationshipViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeRelationshipViewRequest): UseComparativeRelationshipViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeRelationshipViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeRelationshipViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeRelationshipViewRequest, reader: jspb.BinaryReader): UseComparativeRelationshipViewRequest;
}

export namespace UseComparativeRelationshipViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryRelationshipViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryRelationshipViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryRelationshipViewReply): UsePlenaryRelationshipViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryRelationshipViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryRelationshipViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryRelationshipViewReply, reader: jspb.BinaryReader): UsePlenaryRelationshipViewReply;
}

export namespace UsePlenaryRelationshipViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryRelationshipViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryRelationshipViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryRelationshipViewRequest): UsePlenaryRelationshipViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryRelationshipViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryRelationshipViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryRelationshipViewRequest, reader: jspb.BinaryReader): UsePlenaryRelationshipViewRequest;
}

export namespace UsePlenaryRelationshipViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedFamilyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedFamilyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedFamilyViewReply): UseFederatedFamilyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedFamilyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedFamilyViewReply;
  static deserializeBinaryFromReader(message: UseFederatedFamilyViewReply, reader: jspb.BinaryReader): UseFederatedFamilyViewReply;
}

export namespace UseFederatedFamilyViewReply {
  export type AsObject = {
  }
}

export class UseFederatedFamilyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedFamilyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedFamilyViewRequest): UseFederatedFamilyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedFamilyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedFamilyViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedFamilyViewRequest, reader: jspb.BinaryReader): UseFederatedFamilyViewRequest;
}

export namespace UseFederatedFamilyViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedFamilyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedFamilyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedFamilyViewReply): UseIsolatedFamilyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedFamilyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedFamilyViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedFamilyViewReply, reader: jspb.BinaryReader): UseIsolatedFamilyViewReply;
}

export namespace UseIsolatedFamilyViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedFamilyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedFamilyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedFamilyViewRequest): UseIsolatedFamilyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedFamilyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedFamilyViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedFamilyViewRequest, reader: jspb.BinaryReader): UseIsolatedFamilyViewRequest;
}

export namespace UseIsolatedFamilyViewRequest {
  export type AsObject = {
  }
}

export class UseEffectiveRelationshipViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveRelationshipViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveRelationshipViewReply): UseEffectiveRelationshipViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveRelationshipViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveRelationshipViewReply;
  static deserializeBinaryFromReader(message: UseEffectiveRelationshipViewReply, reader: jspb.BinaryReader): UseEffectiveRelationshipViewReply;
}

export namespace UseEffectiveRelationshipViewReply {
  export type AsObject = {
  }
}

export class UseEffectiveRelationshipViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveRelationshipViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveRelationshipViewRequest): UseEffectiveRelationshipViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveRelationshipViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveRelationshipViewRequest;
  static deserializeBinaryFromReader(message: UseEffectiveRelationshipViewRequest, reader: jspb.BinaryReader): UseEffectiveRelationshipViewRequest;
}

export namespace UseEffectiveRelationshipViewRequest {
  export type AsObject = {
  }
}

export class UseAnyEffectiveRelationshipViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveRelationshipViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveRelationshipViewReply): UseAnyEffectiveRelationshipViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveRelationshipViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveRelationshipViewReply;
  static deserializeBinaryFromReader(message: UseAnyEffectiveRelationshipViewReply, reader: jspb.BinaryReader): UseAnyEffectiveRelationshipViewReply;
}

export namespace UseAnyEffectiveRelationshipViewReply {
  export type AsObject = {
  }
}

export class UseAnyEffectiveRelationshipViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveRelationshipViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveRelationshipViewRequest): UseAnyEffectiveRelationshipViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveRelationshipViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveRelationshipViewRequest;
  static deserializeBinaryFromReader(message: UseAnyEffectiveRelationshipViewRequest, reader: jspb.BinaryReader): UseAnyEffectiveRelationshipViewRequest;
}

export namespace UseAnyEffectiveRelationshipViewRequest {
  export type AsObject = {
  }
}

export class GetRelationshipReply extends jspb.Message {
  hasRelationship(): boolean;
  clearRelationship(): void;
  getRelationship(): Relationship | undefined;
  setRelationship(value?: Relationship): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipReply): GetRelationshipReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipReply;
  static deserializeBinaryFromReader(message: GetRelationshipReply, reader: jspb.BinaryReader): GetRelationshipReply;
}

export namespace GetRelationshipReply {
  export type AsObject = {
    relationship?: Relationship.AsObject,
  }
}

export class GetRelationshipRequest extends jspb.Message {
  hasRelationshipId(): boolean;
  clearRelationshipId(): void;
  getRelationshipId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRelationshipId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipRequest): GetRelationshipRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipRequest;
  static deserializeBinaryFromReader(message: GetRelationshipRequest, reader: jspb.BinaryReader): GetRelationshipRequest;
}

export namespace GetRelationshipRequest {
  export type AsObject = {
    relationshipId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRelationshipsByIdsRequest extends jspb.Message {
  clearRelationshipIdsList(): void;
  getRelationshipIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setRelationshipIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addRelationshipIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByIdsRequest): GetRelationshipsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByIdsRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByIdsRequest, reader: jspb.BinaryReader): GetRelationshipsByIdsRequest;
}

export namespace GetRelationshipsByIdsRequest {
  export type AsObject = {
    relationshipIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetRelationshipsByGenusTypeRequest extends jspb.Message {
  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeRequest): GetRelationshipsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeRequest;
}

export namespace GetRelationshipsByGenusTypeRequest {
  export type AsObject = {
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRelationshipsByParentGenusTypeRequest extends jspb.Message {
  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByParentGenusTypeRequest): GetRelationshipsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetRelationshipsByParentGenusTypeRequest;
}

export namespace GetRelationshipsByParentGenusTypeRequest {
  export type AsObject = {
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRelationshipsByRecordTypeRequest extends jspb.Message {
  hasRelationshipRecordType(): boolean;
  clearRelationshipRecordType(): void;
  getRelationshipRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByRecordTypeRequest): GetRelationshipsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByRecordTypeRequest, reader: jspb.BinaryReader): GetRelationshipsByRecordTypeRequest;
}

export namespace GetRelationshipsByRecordTypeRequest {
  export type AsObject = {
    relationshipRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRelationshipsOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsOnDateRequest): GetRelationshipsOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsOnDateRequest;
}

export namespace GetRelationshipsOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsForSourceRequest extends jspb.Message {
  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsForSourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsForSourceRequest): GetRelationshipsForSourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsForSourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsForSourceRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsForSourceRequest, reader: jspb.BinaryReader): GetRelationshipsForSourceRequest;
}

export namespace GetRelationshipsForSourceRequest {
  export type AsObject = {
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRelationshipsForSourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsForSourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsForSourceOnDateRequest): GetRelationshipsForSourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsForSourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsForSourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsForSourceOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsForSourceOnDateRequest;
}

export namespace GetRelationshipsForSourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsByGenusTypeForSourceRequest extends jspb.Message {
  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeForSourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeForSourceRequest): GetRelationshipsByGenusTypeForSourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeForSourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeForSourceRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeForSourceRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeForSourceRequest;
}

export namespace GetRelationshipsByGenusTypeForSourceRequest {
  export type AsObject = {
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRelationshipsByGenusTypeForSourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeForSourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeForSourceOnDateRequest): GetRelationshipsByGenusTypeForSourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeForSourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeForSourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeForSourceOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeForSourceOnDateRequest;
}

export namespace GetRelationshipsByGenusTypeForSourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsForDestinationRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsForDestinationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsForDestinationRequest): GetRelationshipsForDestinationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsForDestinationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsForDestinationRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsForDestinationRequest, reader: jspb.BinaryReader): GetRelationshipsForDestinationRequest;
}

export namespace GetRelationshipsForDestinationRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRelationshipsForDestinationOnDateRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsForDestinationOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsForDestinationOnDateRequest): GetRelationshipsForDestinationOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsForDestinationOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsForDestinationOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsForDestinationOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsForDestinationOnDateRequest;
}

export namespace GetRelationshipsForDestinationOnDateRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsByGenusTypeForDestinationRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeForDestinationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeForDestinationRequest): GetRelationshipsByGenusTypeForDestinationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeForDestinationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeForDestinationRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeForDestinationRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeForDestinationRequest;
}

export namespace GetRelationshipsByGenusTypeForDestinationRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetRelationshipsByGenusTypeForDestinationOnDateRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeForDestinationOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeForDestinationOnDateRequest): GetRelationshipsByGenusTypeForDestinationOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeForDestinationOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeForDestinationOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeForDestinationOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeForDestinationOnDateRequest;
}

export namespace GetRelationshipsByGenusTypeForDestinationOnDateRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsForPeersRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsForPeersRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsForPeersRequest): GetRelationshipsForPeersRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsForPeersRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsForPeersRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsForPeersRequest, reader: jspb.BinaryReader): GetRelationshipsForPeersRequest;
}

export namespace GetRelationshipsForPeersRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRelationshipsForPeersOnDateRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsForPeersOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsForPeersOnDateRequest): GetRelationshipsForPeersOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsForPeersOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsForPeersOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsForPeersOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsForPeersOnDateRequest;
}

export namespace GetRelationshipsForPeersOnDateRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsByGenusTypeForPeersRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeForPeersRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeForPeersRequest): GetRelationshipsByGenusTypeForPeersRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeForPeersRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeForPeersRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeForPeersRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeForPeersRequest;
}

export namespace GetRelationshipsByGenusTypeForPeersRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetRelationshipsByGenusTypeForPeersOnDateRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasRelationshipGenusType(): boolean;
  clearRelationshipGenusType(): void;
  getRelationshipGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setRelationshipGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByGenusTypeForPeersOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByGenusTypeForPeersOnDateRequest): GetRelationshipsByGenusTypeForPeersOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByGenusTypeForPeersOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByGenusTypeForPeersOnDateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByGenusTypeForPeersOnDateRequest, reader: jspb.BinaryReader): GetRelationshipsByGenusTypeForPeersOnDateRequest;
}

export namespace GetRelationshipsByGenusTypeForPeersOnDateRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    relationshipGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetRelationshipsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsRequest): GetRelationshipsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsRequest, reader: jspb.BinaryReader): GetRelationshipsRequest;
}

export namespace GetRelationshipsRequest {
  export type AsObject = {
  }
}

export class CanSearchRelationshipsReply extends jspb.Message {
  getCanSearchRelationships(): boolean;
  setCanSearchRelationships(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchRelationshipsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchRelationshipsReply): CanSearchRelationshipsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchRelationshipsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchRelationshipsReply;
  static deserializeBinaryFromReader(message: CanSearchRelationshipsReply, reader: jspb.BinaryReader): CanSearchRelationshipsReply;
}

export namespace CanSearchRelationshipsReply {
  export type AsObject = {
    canSearchRelationships: boolean,
  }
}

export class CanSearchRelationshipsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchRelationshipsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchRelationshipsRequest): CanSearchRelationshipsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchRelationshipsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchRelationshipsRequest;
  static deserializeBinaryFromReader(message: CanSearchRelationshipsRequest, reader: jspb.BinaryReader): CanSearchRelationshipsRequest;
}

export namespace CanSearchRelationshipsRequest {
  export type AsObject = {
  }
}

export class GetRelationshipQueryReply extends jspb.Message {
  hasRelationshipQuery(): boolean;
  clearRelationshipQuery(): void;
  getRelationshipQuery(): RelationshipQuery | undefined;
  setRelationshipQuery(value?: RelationshipQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipQueryReply): GetRelationshipQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipQueryReply;
  static deserializeBinaryFromReader(message: GetRelationshipQueryReply, reader: jspb.BinaryReader): GetRelationshipQueryReply;
}

export namespace GetRelationshipQueryReply {
  export type AsObject = {
    relationshipQuery?: RelationshipQuery.AsObject,
  }
}

export class GetRelationshipQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipQueryRequest): GetRelationshipQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipQueryRequest;
  static deserializeBinaryFromReader(message: GetRelationshipQueryRequest, reader: jspb.BinaryReader): GetRelationshipQueryRequest;
}

export namespace GetRelationshipQueryRequest {
  export type AsObject = {
  }
}

export class GetRelationshipsByQueryRequest extends jspb.Message {
  hasRelationshipQuery(): boolean;
  clearRelationshipQuery(): void;
  getRelationshipQuery(): RelationshipQuery | undefined;
  setRelationshipQuery(value?: RelationshipQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipsByQueryRequest): GetRelationshipsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipsByQueryRequest;
  static deserializeBinaryFromReader(message: GetRelationshipsByQueryRequest, reader: jspb.BinaryReader): GetRelationshipsByQueryRequest;
}

export namespace GetRelationshipsByQueryRequest {
  export type AsObject = {
    relationshipQuery?: RelationshipQuery.AsObject,
  }
}

export class CanCreateRelationshipsReply extends jspb.Message {
  getCanCreateRelationships(): boolean;
  setCanCreateRelationships(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRelationshipsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRelationshipsReply): CanCreateRelationshipsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRelationshipsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRelationshipsReply;
  static deserializeBinaryFromReader(message: CanCreateRelationshipsReply, reader: jspb.BinaryReader): CanCreateRelationshipsReply;
}

export namespace CanCreateRelationshipsReply {
  export type AsObject = {
    canCreateRelationships: boolean,
  }
}

export class CanCreateRelationshipsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRelationshipsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRelationshipsRequest): CanCreateRelationshipsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRelationshipsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRelationshipsRequest;
  static deserializeBinaryFromReader(message: CanCreateRelationshipsRequest, reader: jspb.BinaryReader): CanCreateRelationshipsRequest;
}

export namespace CanCreateRelationshipsRequest {
  export type AsObject = {
  }
}

export class CanCreateRelationshipWithRecordTypesReply extends jspb.Message {
  getCanCreateRelationshipWithRecordTypes(): boolean;
  setCanCreateRelationshipWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRelationshipWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRelationshipWithRecordTypesReply): CanCreateRelationshipWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRelationshipWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRelationshipWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateRelationshipWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateRelationshipWithRecordTypesReply;
}

export namespace CanCreateRelationshipWithRecordTypesReply {
  export type AsObject = {
    canCreateRelationshipWithRecordTypes: boolean,
  }
}

export class CanCreateRelationshipWithRecordTypesRequest extends jspb.Message {
  clearRelationshipRecordTypesList(): void;
  getRelationshipRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRelationshipRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRelationshipRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateRelationshipWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateRelationshipWithRecordTypesRequest): CanCreateRelationshipWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateRelationshipWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateRelationshipWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateRelationshipWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateRelationshipWithRecordTypesRequest;
}

export namespace CanCreateRelationshipWithRecordTypesRequest {
  export type AsObject = {
    relationshipRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetRelationshipFormForCreateReply extends jspb.Message {
  hasRelationshipForm(): boolean;
  clearRelationshipForm(): void;
  getRelationshipForm(): RelationshipForm | undefined;
  setRelationshipForm(value?: RelationshipForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipFormForCreateReply): GetRelationshipFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipFormForCreateReply;
  static deserializeBinaryFromReader(message: GetRelationshipFormForCreateReply, reader: jspb.BinaryReader): GetRelationshipFormForCreateReply;
}

export namespace GetRelationshipFormForCreateReply {
  export type AsObject = {
    relationshipForm?: RelationshipForm.AsObject,
  }
}

export class GetRelationshipFormForCreateRequest extends jspb.Message {
  hasDestinationId(): boolean;
  clearDestinationId(): void;
  getDestinationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDestinationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRelationshipRecordTypesList(): void;
  getRelationshipRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRelationshipRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRelationshipRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasSourceId(): boolean;
  clearSourceId(): void;
  getSourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipFormForCreateRequest): GetRelationshipFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipFormForCreateRequest, reader: jspb.BinaryReader): GetRelationshipFormForCreateRequest;
}

export namespace GetRelationshipFormForCreateRequest {
  export type AsObject = {
    destinationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    relationshipRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    sourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateRelationshipReply extends jspb.Message {
  hasRelationship(): boolean;
  clearRelationship(): void;
  getRelationship(): Relationship | undefined;
  setRelationship(value?: Relationship): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateRelationshipReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateRelationshipReply): CreateRelationshipReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateRelationshipReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateRelationshipReply;
  static deserializeBinaryFromReader(message: CreateRelationshipReply, reader: jspb.BinaryReader): CreateRelationshipReply;
}

export namespace CreateRelationshipReply {
  export type AsObject = {
    relationship?: Relationship.AsObject,
  }
}

export class CreateRelationshipRequest extends jspb.Message {
  hasRelationshipForm(): boolean;
  clearRelationshipForm(): void;
  getRelationshipForm(): RelationshipForm | undefined;
  setRelationshipForm(value?: RelationshipForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateRelationshipRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateRelationshipRequest): CreateRelationshipRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateRelationshipRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateRelationshipRequest;
  static deserializeBinaryFromReader(message: CreateRelationshipRequest, reader: jspb.BinaryReader): CreateRelationshipRequest;
}

export namespace CreateRelationshipRequest {
  export type AsObject = {
    relationshipForm?: RelationshipForm.AsObject,
  }
}

export class CanUpdateRelationshipsReply extends jspb.Message {
  getCanUpdateRelationships(): boolean;
  setCanUpdateRelationships(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateRelationshipsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateRelationshipsReply): CanUpdateRelationshipsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateRelationshipsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateRelationshipsReply;
  static deserializeBinaryFromReader(message: CanUpdateRelationshipsReply, reader: jspb.BinaryReader): CanUpdateRelationshipsReply;
}

export namespace CanUpdateRelationshipsReply {
  export type AsObject = {
    canUpdateRelationships: boolean,
  }
}

export class CanUpdateRelationshipsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateRelationshipsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateRelationshipsRequest): CanUpdateRelationshipsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateRelationshipsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateRelationshipsRequest;
  static deserializeBinaryFromReader(message: CanUpdateRelationshipsRequest, reader: jspb.BinaryReader): CanUpdateRelationshipsRequest;
}

export namespace CanUpdateRelationshipsRequest {
  export type AsObject = {
  }
}

export class GetRelationshipFormForUpdateReply extends jspb.Message {
  hasRelationshipForm(): boolean;
  clearRelationshipForm(): void;
  getRelationshipForm(): RelationshipForm | undefined;
  setRelationshipForm(value?: RelationshipForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipFormForUpdateReply): GetRelationshipFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetRelationshipFormForUpdateReply, reader: jspb.BinaryReader): GetRelationshipFormForUpdateReply;
}

export namespace GetRelationshipFormForUpdateReply {
  export type AsObject = {
    relationshipForm?: RelationshipForm.AsObject,
  }
}

export class GetRelationshipFormForUpdateRequest extends jspb.Message {
  hasRelationshipId(): boolean;
  clearRelationshipId(): void;
  getRelationshipId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRelationshipId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRelationshipFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRelationshipFormForUpdateRequest): GetRelationshipFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRelationshipFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRelationshipFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetRelationshipFormForUpdateRequest, reader: jspb.BinaryReader): GetRelationshipFormForUpdateRequest;
}

export namespace GetRelationshipFormForUpdateRequest {
  export type AsObject = {
    relationshipId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateRelationshipReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRelationshipReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRelationshipReply): UpdateRelationshipReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRelationshipReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRelationshipReply;
  static deserializeBinaryFromReader(message: UpdateRelationshipReply, reader: jspb.BinaryReader): UpdateRelationshipReply;
}

export namespace UpdateRelationshipReply {
  export type AsObject = {
  }
}

export class UpdateRelationshipRequest extends jspb.Message {
  hasRelationshipForm(): boolean;
  clearRelationshipForm(): void;
  getRelationshipForm(): RelationshipForm | undefined;
  setRelationshipForm(value?: RelationshipForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRelationshipRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRelationshipRequest): UpdateRelationshipRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRelationshipRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRelationshipRequest;
  static deserializeBinaryFromReader(message: UpdateRelationshipRequest, reader: jspb.BinaryReader): UpdateRelationshipRequest;
}

export namespace UpdateRelationshipRequest {
  export type AsObject = {
    relationshipForm?: RelationshipForm.AsObject,
  }
}

export class CanDeleteRelationshipsReply extends jspb.Message {
  getCanDeleteRelationships(): boolean;
  setCanDeleteRelationships(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteRelationshipsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteRelationshipsReply): CanDeleteRelationshipsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteRelationshipsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteRelationshipsReply;
  static deserializeBinaryFromReader(message: CanDeleteRelationshipsReply, reader: jspb.BinaryReader): CanDeleteRelationshipsReply;
}

export namespace CanDeleteRelationshipsReply {
  export type AsObject = {
    canDeleteRelationships: boolean,
  }
}

export class CanDeleteRelationshipsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteRelationshipsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteRelationshipsRequest): CanDeleteRelationshipsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteRelationshipsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteRelationshipsRequest;
  static deserializeBinaryFromReader(message: CanDeleteRelationshipsRequest, reader: jspb.BinaryReader): CanDeleteRelationshipsRequest;
}

export namespace CanDeleteRelationshipsRequest {
  export type AsObject = {
  }
}

export class DeleteRelationshipReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteRelationshipReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteRelationshipReply): DeleteRelationshipReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteRelationshipReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteRelationshipReply;
  static deserializeBinaryFromReader(message: DeleteRelationshipReply, reader: jspb.BinaryReader): DeleteRelationshipReply;
}

export namespace DeleteRelationshipReply {
  export type AsObject = {
  }
}

export class DeleteRelationshipRequest extends jspb.Message {
  hasRelationshipId(): boolean;
  clearRelationshipId(): void;
  getRelationshipId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRelationshipId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteRelationshipRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteRelationshipRequest): DeleteRelationshipRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteRelationshipRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteRelationshipRequest;
  static deserializeBinaryFromReader(message: DeleteRelationshipRequest, reader: jspb.BinaryReader): DeleteRelationshipRequest;
}

export namespace DeleteRelationshipRequest {
  export type AsObject = {
    relationshipId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageRelationshipAliasesReply extends jspb.Message {
  getCanManageRelationshipAliases(): boolean;
  setCanManageRelationshipAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageRelationshipAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageRelationshipAliasesReply): CanManageRelationshipAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageRelationshipAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageRelationshipAliasesReply;
  static deserializeBinaryFromReader(message: CanManageRelationshipAliasesReply, reader: jspb.BinaryReader): CanManageRelationshipAliasesReply;
}

export namespace CanManageRelationshipAliasesReply {
  export type AsObject = {
    canManageRelationshipAliases: boolean,
  }
}

export class CanManageRelationshipAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageRelationshipAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageRelationshipAliasesRequest): CanManageRelationshipAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageRelationshipAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageRelationshipAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageRelationshipAliasesRequest, reader: jspb.BinaryReader): CanManageRelationshipAliasesRequest;
}

export namespace CanManageRelationshipAliasesRequest {
  export type AsObject = {
  }
}

export class AliasRelationshipReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasRelationshipReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasRelationshipReply): AliasRelationshipReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasRelationshipReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasRelationshipReply;
  static deserializeBinaryFromReader(message: AliasRelationshipReply, reader: jspb.BinaryReader): AliasRelationshipReply;
}

export namespace AliasRelationshipReply {
  export type AsObject = {
  }
}

export class AliasRelationshipRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRelationshipId(): boolean;
  clearRelationshipId(): void;
  getRelationshipId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRelationshipId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasRelationshipRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasRelationshipRequest): AliasRelationshipRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasRelationshipRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasRelationshipRequest;
  static deserializeBinaryFromReader(message: AliasRelationshipRequest, reader: jspb.BinaryReader): AliasRelationshipRequest;
}

export namespace AliasRelationshipRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    relationshipId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupFamiliesReply extends jspb.Message {
  getCanLookupFamilies(): boolean;
  setCanLookupFamilies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupFamiliesReply): CanLookupFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupFamiliesReply;
  static deserializeBinaryFromReader(message: CanLookupFamiliesReply, reader: jspb.BinaryReader): CanLookupFamiliesReply;
}

export namespace CanLookupFamiliesReply {
  export type AsObject = {
    canLookupFamilies: boolean,
  }
}

export class CanLookupFamiliesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupFamiliesRequest): CanLookupFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupFamiliesRequest;
  static deserializeBinaryFromReader(message: CanLookupFamiliesRequest, reader: jspb.BinaryReader): CanLookupFamiliesRequest;
}

export namespace CanLookupFamiliesRequest {
  export type AsObject = {
  }
}

export class UseComparativeFamilyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeFamilyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeFamilyViewReply): UseComparativeFamilyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeFamilyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeFamilyViewReply;
  static deserializeBinaryFromReader(message: UseComparativeFamilyViewReply, reader: jspb.BinaryReader): UseComparativeFamilyViewReply;
}

export namespace UseComparativeFamilyViewReply {
  export type AsObject = {
  }
}

export class UseComparativeFamilyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeFamilyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeFamilyViewRequest): UseComparativeFamilyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeFamilyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeFamilyViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeFamilyViewRequest, reader: jspb.BinaryReader): UseComparativeFamilyViewRequest;
}

export namespace UseComparativeFamilyViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryFamilyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryFamilyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryFamilyViewReply): UsePlenaryFamilyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryFamilyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryFamilyViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryFamilyViewReply, reader: jspb.BinaryReader): UsePlenaryFamilyViewReply;
}

export namespace UsePlenaryFamilyViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryFamilyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryFamilyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryFamilyViewRequest): UsePlenaryFamilyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryFamilyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryFamilyViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryFamilyViewRequest, reader: jspb.BinaryReader): UsePlenaryFamilyViewRequest;
}

export namespace UsePlenaryFamilyViewRequest {
  export type AsObject = {
  }
}

export class GetFamiliesByIdsRequest extends jspb.Message {
  clearFamilyIdsList(): void;
  getFamilyIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setFamilyIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addFamilyIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamiliesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamiliesByIdsRequest): GetFamiliesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamiliesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamiliesByIdsRequest;
  static deserializeBinaryFromReader(message: GetFamiliesByIdsRequest, reader: jspb.BinaryReader): GetFamiliesByIdsRequest;
}

export namespace GetFamiliesByIdsRequest {
  export type AsObject = {
    familyIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetFamiliesByGenusTypeRequest extends jspb.Message {
  hasFamilyGenusType(): boolean;
  clearFamilyGenusType(): void;
  getFamilyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setFamilyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamiliesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamiliesByGenusTypeRequest): GetFamiliesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamiliesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamiliesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetFamiliesByGenusTypeRequest, reader: jspb.BinaryReader): GetFamiliesByGenusTypeRequest;
}

export namespace GetFamiliesByGenusTypeRequest {
  export type AsObject = {
    familyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetFamiliesByParentGenusTypeRequest extends jspb.Message {
  hasFamilyGenusType(): boolean;
  clearFamilyGenusType(): void;
  getFamilyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setFamilyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamiliesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamiliesByParentGenusTypeRequest): GetFamiliesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamiliesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamiliesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetFamiliesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetFamiliesByParentGenusTypeRequest;
}

export namespace GetFamiliesByParentGenusTypeRequest {
  export type AsObject = {
    familyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetFamiliesByRecordTypeRequest extends jspb.Message {
  hasFamilyRecordType(): boolean;
  clearFamilyRecordType(): void;
  getFamilyRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setFamilyRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamiliesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamiliesByRecordTypeRequest): GetFamiliesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamiliesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamiliesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetFamiliesByRecordTypeRequest, reader: jspb.BinaryReader): GetFamiliesByRecordTypeRequest;
}

export namespace GetFamiliesByRecordTypeRequest {
  export type AsObject = {
    familyRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetFamiliesByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamiliesByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamiliesByProviderRequest): GetFamiliesByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamiliesByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamiliesByProviderRequest;
  static deserializeBinaryFromReader(message: GetFamiliesByProviderRequest, reader: jspb.BinaryReader): GetFamiliesByProviderRequest;
}

export namespace GetFamiliesByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFamiliesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamiliesRequest): GetFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamiliesRequest;
  static deserializeBinaryFromReader(message: GetFamiliesRequest, reader: jspb.BinaryReader): GetFamiliesRequest;
}

export namespace GetFamiliesRequest {
  export type AsObject = {
  }
}

export class CanCreateFamiliesReply extends jspb.Message {
  getCanCreateFamilies(): boolean;
  setCanCreateFamilies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateFamiliesReply): CanCreateFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateFamiliesReply;
  static deserializeBinaryFromReader(message: CanCreateFamiliesReply, reader: jspb.BinaryReader): CanCreateFamiliesReply;
}

export namespace CanCreateFamiliesReply {
  export type AsObject = {
    canCreateFamilies: boolean,
  }
}

export class CanCreateFamiliesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateFamiliesRequest): CanCreateFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateFamiliesRequest;
  static deserializeBinaryFromReader(message: CanCreateFamiliesRequest, reader: jspb.BinaryReader): CanCreateFamiliesRequest;
}

export namespace CanCreateFamiliesRequest {
  export type AsObject = {
  }
}

export class CanCreateFamilyWithRecordTypesReply extends jspb.Message {
  getCanCreateFamilyWithRecordTypes(): boolean;
  setCanCreateFamilyWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateFamilyWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateFamilyWithRecordTypesReply): CanCreateFamilyWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateFamilyWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateFamilyWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateFamilyWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateFamilyWithRecordTypesReply;
}

export namespace CanCreateFamilyWithRecordTypesReply {
  export type AsObject = {
    canCreateFamilyWithRecordTypes: boolean,
  }
}

export class CanCreateFamilyWithRecordTypesRequest extends jspb.Message {
  clearFamilyRecordTypesList(): void;
  getFamilyRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setFamilyRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addFamilyRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateFamilyWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateFamilyWithRecordTypesRequest): CanCreateFamilyWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateFamilyWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateFamilyWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateFamilyWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateFamilyWithRecordTypesRequest;
}

export namespace CanCreateFamilyWithRecordTypesRequest {
  export type AsObject = {
    familyRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetFamilyFormForCreateReply extends jspb.Message {
  hasFamilyForm(): boolean;
  clearFamilyForm(): void;
  getFamilyForm(): FamilyForm | undefined;
  setFamilyForm(value?: FamilyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyFormForCreateReply): GetFamilyFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyFormForCreateReply;
  static deserializeBinaryFromReader(message: GetFamilyFormForCreateReply, reader: jspb.BinaryReader): GetFamilyFormForCreateReply;
}

export namespace GetFamilyFormForCreateReply {
  export type AsObject = {
    familyForm?: FamilyForm.AsObject,
  }
}

export class GetFamilyFormForCreateRequest extends jspb.Message {
  clearFamilyRecordTypesList(): void;
  getFamilyRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setFamilyRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addFamilyRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyFormForCreateRequest): GetFamilyFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetFamilyFormForCreateRequest, reader: jspb.BinaryReader): GetFamilyFormForCreateRequest;
}

export namespace GetFamilyFormForCreateRequest {
  export type AsObject = {
    familyRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateFamilyReply extends jspb.Message {
  hasFamily(): boolean;
  clearFamily(): void;
  getFamily(): Family | undefined;
  setFamily(value?: Family): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateFamilyReply): CreateFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateFamilyReply;
  static deserializeBinaryFromReader(message: CreateFamilyReply, reader: jspb.BinaryReader): CreateFamilyReply;
}

export namespace CreateFamilyReply {
  export type AsObject = {
    family?: Family.AsObject,
  }
}

export class CreateFamilyRequest extends jspb.Message {
  hasFamilyForm(): boolean;
  clearFamilyForm(): void;
  getFamilyForm(): FamilyForm | undefined;
  setFamilyForm(value?: FamilyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateFamilyRequest): CreateFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateFamilyRequest;
  static deserializeBinaryFromReader(message: CreateFamilyRequest, reader: jspb.BinaryReader): CreateFamilyRequest;
}

export namespace CreateFamilyRequest {
  export type AsObject = {
    familyForm?: FamilyForm.AsObject,
  }
}

export class CanUpdateFamiliesReply extends jspb.Message {
  getCanUpdateFamilies(): boolean;
  setCanUpdateFamilies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateFamiliesReply): CanUpdateFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateFamiliesReply;
  static deserializeBinaryFromReader(message: CanUpdateFamiliesReply, reader: jspb.BinaryReader): CanUpdateFamiliesReply;
}

export namespace CanUpdateFamiliesReply {
  export type AsObject = {
    canUpdateFamilies: boolean,
  }
}

export class CanUpdateFamiliesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateFamiliesRequest): CanUpdateFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateFamiliesRequest;
  static deserializeBinaryFromReader(message: CanUpdateFamiliesRequest, reader: jspb.BinaryReader): CanUpdateFamiliesRequest;
}

export namespace CanUpdateFamiliesRequest {
  export type AsObject = {
  }
}

export class GetFamilyFormForUpdateReply extends jspb.Message {
  hasFamilyForm(): boolean;
  clearFamilyForm(): void;
  getFamilyForm(): FamilyForm | undefined;
  setFamilyForm(value?: FamilyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyFormForUpdateReply): GetFamilyFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetFamilyFormForUpdateReply, reader: jspb.BinaryReader): GetFamilyFormForUpdateReply;
}

export namespace GetFamilyFormForUpdateReply {
  export type AsObject = {
    familyForm?: FamilyForm.AsObject,
  }
}

export class GetFamilyFormForUpdateRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyFormForUpdateRequest): GetFamilyFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetFamilyFormForUpdateRequest, reader: jspb.BinaryReader): GetFamilyFormForUpdateRequest;
}

export namespace GetFamilyFormForUpdateRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateFamilyReply): UpdateFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateFamilyReply;
  static deserializeBinaryFromReader(message: UpdateFamilyReply, reader: jspb.BinaryReader): UpdateFamilyReply;
}

export namespace UpdateFamilyReply {
  export type AsObject = {
  }
}

export class UpdateFamilyRequest extends jspb.Message {
  hasFamilyForm(): boolean;
  clearFamilyForm(): void;
  getFamilyForm(): FamilyForm | undefined;
  setFamilyForm(value?: FamilyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateFamilyRequest): UpdateFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateFamilyRequest;
  static deserializeBinaryFromReader(message: UpdateFamilyRequest, reader: jspb.BinaryReader): UpdateFamilyRequest;
}

export namespace UpdateFamilyRequest {
  export type AsObject = {
    familyForm?: FamilyForm.AsObject,
  }
}

export class CanDeleteFamiliesReply extends jspb.Message {
  getCanDeleteFamilies(): boolean;
  setCanDeleteFamilies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteFamiliesReply): CanDeleteFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteFamiliesReply;
  static deserializeBinaryFromReader(message: CanDeleteFamiliesReply, reader: jspb.BinaryReader): CanDeleteFamiliesReply;
}

export namespace CanDeleteFamiliesReply {
  export type AsObject = {
    canDeleteFamilies: boolean,
  }
}

export class CanDeleteFamiliesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteFamiliesRequest): CanDeleteFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteFamiliesRequest;
  static deserializeBinaryFromReader(message: CanDeleteFamiliesRequest, reader: jspb.BinaryReader): CanDeleteFamiliesRequest;
}

export namespace CanDeleteFamiliesRequest {
  export type AsObject = {
  }
}

export class DeleteFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteFamilyReply): DeleteFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteFamilyReply;
  static deserializeBinaryFromReader(message: DeleteFamilyReply, reader: jspb.BinaryReader): DeleteFamilyReply;
}

export namespace DeleteFamilyReply {
  export type AsObject = {
  }
}

export class DeleteFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteFamilyRequest): DeleteFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteFamilyRequest;
  static deserializeBinaryFromReader(message: DeleteFamilyRequest, reader: jspb.BinaryReader): DeleteFamilyRequest;
}

export namespace DeleteFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageFamilyAliasesReply extends jspb.Message {
  getCanManageFamilyAliases(): boolean;
  setCanManageFamilyAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageFamilyAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageFamilyAliasesReply): CanManageFamilyAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageFamilyAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageFamilyAliasesReply;
  static deserializeBinaryFromReader(message: CanManageFamilyAliasesReply, reader: jspb.BinaryReader): CanManageFamilyAliasesReply;
}

export namespace CanManageFamilyAliasesReply {
  export type AsObject = {
    canManageFamilyAliases: boolean,
  }
}

export class CanManageFamilyAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageFamilyAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageFamilyAliasesRequest): CanManageFamilyAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageFamilyAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageFamilyAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageFamilyAliasesRequest, reader: jspb.BinaryReader): CanManageFamilyAliasesRequest;
}

export namespace CanManageFamilyAliasesRequest {
  export type AsObject = {
  }
}

export class AliasFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasFamilyReply): AliasFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasFamilyReply;
  static deserializeBinaryFromReader(message: AliasFamilyReply, reader: jspb.BinaryReader): AliasFamilyReply;
}

export namespace AliasFamilyReply {
  export type AsObject = {
  }
}

export class AliasFamilyRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasFamilyRequest): AliasFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasFamilyRequest;
  static deserializeBinaryFromReader(message: AliasFamilyRequest, reader: jspb.BinaryReader): AliasFamilyRequest;
}

export namespace AliasFamilyRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFamilyHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyHierarchyIdReply): GetFamilyHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetFamilyHierarchyIdReply, reader: jspb.BinaryReader): GetFamilyHierarchyIdReply;
}

export namespace GetFamilyHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFamilyHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyHierarchyIdRequest): GetFamilyHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetFamilyHierarchyIdRequest, reader: jspb.BinaryReader): GetFamilyHierarchyIdRequest;
}

export namespace GetFamilyHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetFamilyHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyHierarchyReply): GetFamilyHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyHierarchyReply;
  static deserializeBinaryFromReader(message: GetFamilyHierarchyReply, reader: jspb.BinaryReader): GetFamilyHierarchyReply;
}

export namespace GetFamilyHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetFamilyHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyHierarchyRequest): GetFamilyHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyHierarchyRequest;
  static deserializeBinaryFromReader(message: GetFamilyHierarchyRequest, reader: jspb.BinaryReader): GetFamilyHierarchyRequest;
}

export namespace GetFamilyHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessFamilyHierarchyReply extends jspb.Message {
  getCanAccessFamilyHierarchy(): boolean;
  setCanAccessFamilyHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessFamilyHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessFamilyHierarchyReply): CanAccessFamilyHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessFamilyHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessFamilyHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessFamilyHierarchyReply, reader: jspb.BinaryReader): CanAccessFamilyHierarchyReply;
}

export namespace CanAccessFamilyHierarchyReply {
  export type AsObject = {
    canAccessFamilyHierarchy: boolean,
  }
}

export class CanAccessFamilyHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessFamilyHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessFamilyHierarchyRequest): CanAccessFamilyHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessFamilyHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessFamilyHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessFamilyHierarchyRequest, reader: jspb.BinaryReader): CanAccessFamilyHierarchyRequest;
}

export namespace CanAccessFamilyHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootFamilyIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootFamilyIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootFamilyIdsRequest): GetRootFamilyIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootFamilyIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootFamilyIdsRequest;
  static deserializeBinaryFromReader(message: GetRootFamilyIdsRequest, reader: jspb.BinaryReader): GetRootFamilyIdsRequest;
}

export namespace GetRootFamilyIdsRequest {
  export type AsObject = {
  }
}

export class GetRootFamiliesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootFamiliesRequest): GetRootFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootFamiliesRequest;
  static deserializeBinaryFromReader(message: GetRootFamiliesRequest, reader: jspb.BinaryReader): GetRootFamiliesRequest;
}

export namespace GetRootFamiliesRequest {
  export type AsObject = {
  }
}

export class HasParentFamiliesReply extends jspb.Message {
  getHasParentFamilies(): boolean;
  setHasParentFamilies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentFamiliesReply): HasParentFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentFamiliesReply;
  static deserializeBinaryFromReader(message: HasParentFamiliesReply, reader: jspb.BinaryReader): HasParentFamiliesReply;
}

export namespace HasParentFamiliesReply {
  export type AsObject = {
    hasParentFamilies: boolean,
  }
}

export class HasParentFamiliesRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentFamiliesRequest): HasParentFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentFamiliesRequest;
  static deserializeBinaryFromReader(message: HasParentFamiliesRequest, reader: jspb.BinaryReader): HasParentFamiliesRequest;
}

export namespace HasParentFamiliesRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfFamilyReply extends jspb.Message {
  getIsParentOfFamily(): boolean;
  setIsParentOfFamily(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfFamilyReply): IsParentOfFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfFamilyReply;
  static deserializeBinaryFromReader(message: IsParentOfFamilyReply, reader: jspb.BinaryReader): IsParentOfFamilyReply;
}

export namespace IsParentOfFamilyReply {
  export type AsObject = {
    isParentOfFamily: boolean,
  }
}

export class IsParentOfFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfFamilyRequest): IsParentOfFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfFamilyRequest;
  static deserializeBinaryFromReader(message: IsParentOfFamilyRequest, reader: jspb.BinaryReader): IsParentOfFamilyRequest;
}

export namespace IsParentOfFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentFamilyIdsRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentFamilyIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentFamilyIdsRequest): GetParentFamilyIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentFamilyIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentFamilyIdsRequest;
  static deserializeBinaryFromReader(message: GetParentFamilyIdsRequest, reader: jspb.BinaryReader): GetParentFamilyIdsRequest;
}

export namespace GetParentFamilyIdsRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentFamiliesRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentFamiliesRequest): GetParentFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentFamiliesRequest;
  static deserializeBinaryFromReader(message: GetParentFamiliesRequest, reader: jspb.BinaryReader): GetParentFamiliesRequest;
}

export namespace GetParentFamiliesRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfFamilyReply extends jspb.Message {
  getIsAncestorOfFamily(): boolean;
  setIsAncestorOfFamily(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfFamilyReply): IsAncestorOfFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfFamilyReply;
  static deserializeBinaryFromReader(message: IsAncestorOfFamilyReply, reader: jspb.BinaryReader): IsAncestorOfFamilyReply;
}

export namespace IsAncestorOfFamilyReply {
  export type AsObject = {
    isAncestorOfFamily: boolean,
  }
}

export class IsAncestorOfFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfFamilyRequest): IsAncestorOfFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfFamilyRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfFamilyRequest, reader: jspb.BinaryReader): IsAncestorOfFamilyRequest;
}

export namespace IsAncestorOfFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildFamiliesReply extends jspb.Message {
  getHasChildFamilies(): boolean;
  setHasChildFamilies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildFamiliesReply): HasChildFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildFamiliesReply;
  static deserializeBinaryFromReader(message: HasChildFamiliesReply, reader: jspb.BinaryReader): HasChildFamiliesReply;
}

export namespace HasChildFamiliesReply {
  export type AsObject = {
    hasChildFamilies: boolean,
  }
}

export class HasChildFamiliesRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildFamiliesRequest): HasChildFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildFamiliesRequest;
  static deserializeBinaryFromReader(message: HasChildFamiliesRequest, reader: jspb.BinaryReader): HasChildFamiliesRequest;
}

export namespace HasChildFamiliesRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfFamilyReply extends jspb.Message {
  getIsChildOfFamily(): boolean;
  setIsChildOfFamily(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfFamilyReply): IsChildOfFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfFamilyReply;
  static deserializeBinaryFromReader(message: IsChildOfFamilyReply, reader: jspb.BinaryReader): IsChildOfFamilyReply;
}

export namespace IsChildOfFamilyReply {
  export type AsObject = {
    isChildOfFamily: boolean,
  }
}

export class IsChildOfFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfFamilyRequest): IsChildOfFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfFamilyRequest;
  static deserializeBinaryFromReader(message: IsChildOfFamilyRequest, reader: jspb.BinaryReader): IsChildOfFamilyRequest;
}

export namespace IsChildOfFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildFamilyIdsRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildFamilyIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildFamilyIdsRequest): GetChildFamilyIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildFamilyIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildFamilyIdsRequest;
  static deserializeBinaryFromReader(message: GetChildFamilyIdsRequest, reader: jspb.BinaryReader): GetChildFamilyIdsRequest;
}

export namespace GetChildFamilyIdsRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildFamiliesRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildFamiliesRequest): GetChildFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildFamiliesRequest;
  static deserializeBinaryFromReader(message: GetChildFamiliesRequest, reader: jspb.BinaryReader): GetChildFamiliesRequest;
}

export namespace GetChildFamiliesRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfFamilyReply extends jspb.Message {
  getIsDescendantOfFamily(): boolean;
  setIsDescendantOfFamily(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfFamilyReply): IsDescendantOfFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfFamilyReply;
  static deserializeBinaryFromReader(message: IsDescendantOfFamilyReply, reader: jspb.BinaryReader): IsDescendantOfFamilyReply;
}

export namespace IsDescendantOfFamilyReply {
  export type AsObject = {
    isDescendantOfFamily: boolean,
  }
}

export class IsDescendantOfFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfFamilyRequest): IsDescendantOfFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfFamilyRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfFamilyRequest, reader: jspb.BinaryReader): IsDescendantOfFamilyRequest;
}

export namespace IsDescendantOfFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFamilyNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyNodeIdsReply): GetFamilyNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyNodeIdsReply;
  static deserializeBinaryFromReader(message: GetFamilyNodeIdsReply, reader: jspb.BinaryReader): GetFamilyNodeIdsReply;
}

export namespace GetFamilyNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetFamilyNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyNodeIdsRequest): GetFamilyNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetFamilyNodeIdsRequest, reader: jspb.BinaryReader): GetFamilyNodeIdsRequest;
}

export namespace GetFamilyNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    includeSiblings: boolean,
  }
}

export class GetFamilyNodesReply extends jspb.Message {
  hasFamilyNode(): boolean;
  clearFamilyNode(): void;
  getFamilyNode(): FamilyNode | undefined;
  setFamilyNode(value?: FamilyNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyNodesReply): GetFamilyNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyNodesReply;
  static deserializeBinaryFromReader(message: GetFamilyNodesReply, reader: jspb.BinaryReader): GetFamilyNodesReply;
}

export namespace GetFamilyNodesReply {
  export type AsObject = {
    familyNode?: FamilyNode.AsObject,
  }
}

export class GetFamilyNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFamilyNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFamilyNodesRequest): GetFamilyNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFamilyNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFamilyNodesRequest;
  static deserializeBinaryFromReader(message: GetFamilyNodesRequest, reader: jspb.BinaryReader): GetFamilyNodesRequest;
}

export namespace GetFamilyNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    includeSiblings: boolean,
  }
}

export class CanModifyFamilyHierarchyReply extends jspb.Message {
  getCanModifyFamilyHierarchy(): boolean;
  setCanModifyFamilyHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyFamilyHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyFamilyHierarchyReply): CanModifyFamilyHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyFamilyHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyFamilyHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyFamilyHierarchyReply, reader: jspb.BinaryReader): CanModifyFamilyHierarchyReply;
}

export namespace CanModifyFamilyHierarchyReply {
  export type AsObject = {
    canModifyFamilyHierarchy: boolean,
  }
}

export class CanModifyFamilyHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyFamilyHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyFamilyHierarchyRequest): CanModifyFamilyHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyFamilyHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyFamilyHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyFamilyHierarchyRequest, reader: jspb.BinaryReader): CanModifyFamilyHierarchyRequest;
}

export namespace CanModifyFamilyHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootFamilyReply): AddRootFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootFamilyReply;
  static deserializeBinaryFromReader(message: AddRootFamilyReply, reader: jspb.BinaryReader): AddRootFamilyReply;
}

export namespace AddRootFamilyReply {
  export type AsObject = {
  }
}

export class AddRootFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootFamilyRequest): AddRootFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootFamilyRequest;
  static deserializeBinaryFromReader(message: AddRootFamilyRequest, reader: jspb.BinaryReader): AddRootFamilyRequest;
}

export namespace AddRootFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootFamilyReply): RemoveRootFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootFamilyReply;
  static deserializeBinaryFromReader(message: RemoveRootFamilyReply, reader: jspb.BinaryReader): RemoveRootFamilyReply;
}

export namespace RemoveRootFamilyReply {
  export type AsObject = {
  }
}

export class RemoveRootFamilyRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootFamilyRequest): RemoveRootFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootFamilyRequest;
  static deserializeBinaryFromReader(message: RemoveRootFamilyRequest, reader: jspb.BinaryReader): RemoveRootFamilyRequest;
}

export namespace RemoveRootFamilyRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildFamilyReply): AddChildFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildFamilyReply;
  static deserializeBinaryFromReader(message: AddChildFamilyReply, reader: jspb.BinaryReader): AddChildFamilyReply;
}

export namespace AddChildFamilyReply {
  export type AsObject = {
  }
}

export class AddChildFamilyRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildFamilyRequest): AddChildFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildFamilyRequest;
  static deserializeBinaryFromReader(message: AddChildFamilyRequest, reader: jspb.BinaryReader): AddChildFamilyRequest;
}

export namespace AddChildFamilyRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildFamilyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildFamilyReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildFamilyReply): RemoveChildFamilyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildFamilyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildFamilyReply;
  static deserializeBinaryFromReader(message: RemoveChildFamilyReply, reader: jspb.BinaryReader): RemoveChildFamilyReply;
}

export namespace RemoveChildFamilyReply {
  export type AsObject = {
  }
}

export class RemoveChildFamilyRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildFamilyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildFamilyRequest): RemoveChildFamilyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildFamilyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildFamilyRequest;
  static deserializeBinaryFromReader(message: RemoveChildFamilyRequest, reader: jspb.BinaryReader): RemoveChildFamilyRequest;
}

export namespace RemoveChildFamilyRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildFamiliesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildFamiliesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildFamiliesReply): RemoveChildFamiliesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildFamiliesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildFamiliesReply;
  static deserializeBinaryFromReader(message: RemoveChildFamiliesReply, reader: jspb.BinaryReader): RemoveChildFamiliesReply;
}

export namespace RemoveChildFamiliesReply {
  export type AsObject = {
  }
}

export class RemoveChildFamiliesRequest extends jspb.Message {
  hasFamilyId(): boolean;
  clearFamilyId(): void;
  getFamilyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFamilyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildFamiliesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildFamiliesRequest): RemoveChildFamiliesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildFamiliesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildFamiliesRequest;
  static deserializeBinaryFromReader(message: RemoveChildFamiliesRequest, reader: jspb.BinaryReader): RemoveChildFamiliesRequest;
}

export namespace RemoveChildFamiliesRequest {
  export type AsObject = {
    familyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

