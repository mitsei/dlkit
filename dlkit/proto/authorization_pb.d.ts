// package: dlkit.proto.authorization
// file: dlkit/proto/authorization.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Authorization extends jspb.Message {
  hasFunction(): boolean;
  clearFunction(): void;
  getFunction(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunction(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasQualifier(): boolean;
  clearQualifier(): void;
  getQualifier(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifier(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVault(): boolean;
  clearVault(): void;
  getVault(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setVault(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Authorization.AsObject;
  static toObject(includeInstance: boolean, msg: Authorization): Authorization.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Authorization, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Authorization;
  static deserializeBinaryFromReader(message: Authorization, reader: jspb.BinaryReader): Authorization;
}

export namespace Authorization {
  export type AsObject = {
    pb_function?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    qualifier?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vault?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
  }
}

export class AuthorizationQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationQuery): AuthorizationQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationQuery;
  static deserializeBinaryFromReader(message: AuthorizationQuery, reader: jspb.BinaryReader): AuthorizationQuery;
}

export namespace AuthorizationQuery {
  export type AsObject = {
  }
}

export class AuthorizationQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationQueryInspector): AuthorizationQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationQueryInspector;
  static deserializeBinaryFromReader(message: AuthorizationQueryInspector, reader: jspb.BinaryReader): AuthorizationQueryInspector;
}

export namespace AuthorizationQueryInspector {
  export type AsObject = {
  }
}

export class AuthorizationForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationForm.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationForm): AuthorizationForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationForm;
  static deserializeBinaryFromReader(message: AuthorizationForm, reader: jspb.BinaryReader): AuthorizationForm;
}

export namespace AuthorizationForm {
  export type AsObject = {
  }
}

export class AuthorizationSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationSearchOrder): AuthorizationSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationSearchOrder;
  static deserializeBinaryFromReader(message: AuthorizationSearchOrder, reader: jspb.BinaryReader): AuthorizationSearchOrder;
}

export namespace AuthorizationSearchOrder {
  export type AsObject = {
  }
}

export class AuthorizationSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationSearch): AuthorizationSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationSearch;
  static deserializeBinaryFromReader(message: AuthorizationSearch, reader: jspb.BinaryReader): AuthorizationSearch;
}

export namespace AuthorizationSearch {
  export type AsObject = {
  }
}

export class AuthorizationSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationSearchResults): AuthorizationSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationSearchResults;
  static deserializeBinaryFromReader(message: AuthorizationSearchResults, reader: jspb.BinaryReader): AuthorizationSearchResults;
}

export namespace AuthorizationSearchResults {
  export type AsObject = {
  }
}

export class AuthorizationList extends jspb.Message {
  clearAuthorizationsList(): void;
  getAuthorizationsList(): Array<Authorization>;
  setAuthorizationsList(value: Array<Authorization>): void;
  addAuthorizations(value?: Authorization, index?: number): Authorization;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationList.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationList): AuthorizationList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationList;
  static deserializeBinaryFromReader(message: AuthorizationList, reader: jspb.BinaryReader): AuthorizationList;
}

export namespace AuthorizationList {
  export type AsObject = {
    authorizationsList: Array<Authorization.AsObject>,
  }
}

export class AuthorizationCondition extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizationCondition.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizationCondition): AuthorizationCondition.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizationCondition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizationCondition;
  static deserializeBinaryFromReader(message: AuthorizationCondition, reader: jspb.BinaryReader): AuthorizationCondition;
}

export namespace AuthorizationCondition {
  export type AsObject = {
  }
}

export class Function extends jspb.Message {
  hasQualifierHierarchy(): boolean;
  clearQualifierHierarchy(): void;
  getQualifierHierarchy(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierHierarchy(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVault(): boolean;
  clearVault(): void;
  getVault(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setVault(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Function.AsObject;
  static toObject(includeInstance: boolean, msg: Function): Function.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Function, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Function;
  static deserializeBinaryFromReader(message: Function, reader: jspb.BinaryReader): Function;
}

export namespace Function {
  export type AsObject = {
    qualifierHierarchy?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vault?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
  }
}

export class FunctionQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionQuery.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionQuery): FunctionQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionQuery;
  static deserializeBinaryFromReader(message: FunctionQuery, reader: jspb.BinaryReader): FunctionQuery;
}

export namespace FunctionQuery {
  export type AsObject = {
  }
}

export class FunctionQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionQueryInspector): FunctionQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionQueryInspector;
  static deserializeBinaryFromReader(message: FunctionQueryInspector, reader: jspb.BinaryReader): FunctionQueryInspector;
}

export namespace FunctionQueryInspector {
  export type AsObject = {
  }
}

export class FunctionForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionForm.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionForm): FunctionForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionForm;
  static deserializeBinaryFromReader(message: FunctionForm, reader: jspb.BinaryReader): FunctionForm;
}

export namespace FunctionForm {
  export type AsObject = {
  }
}

export class FunctionSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionSearchOrder): FunctionSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionSearchOrder;
  static deserializeBinaryFromReader(message: FunctionSearchOrder, reader: jspb.BinaryReader): FunctionSearchOrder;
}

export namespace FunctionSearchOrder {
  export type AsObject = {
  }
}

export class FunctionSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionSearch.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionSearch): FunctionSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionSearch;
  static deserializeBinaryFromReader(message: FunctionSearch, reader: jspb.BinaryReader): FunctionSearch;
}

export namespace FunctionSearch {
  export type AsObject = {
  }
}

export class FunctionSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionSearchResults): FunctionSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionSearchResults;
  static deserializeBinaryFromReader(message: FunctionSearchResults, reader: jspb.BinaryReader): FunctionSearchResults;
}

export namespace FunctionSearchResults {
  export type AsObject = {
  }
}

export class FunctionList extends jspb.Message {
  clearFunctionsList(): void;
  getFunctionsList(): Array<Function>;
  setFunctionsList(value: Array<Function>): void;
  addFunctions(value?: Function, index?: number): Function;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FunctionList.AsObject;
  static toObject(includeInstance: boolean, msg: FunctionList): FunctionList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FunctionList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FunctionList;
  static deserializeBinaryFromReader(message: FunctionList, reader: jspb.BinaryReader): FunctionList;
}

export namespace FunctionList {
  export type AsObject = {
    functionsList: Array<Function.AsObject>,
  }
}

export class Qualifier extends jspb.Message {
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

  hasVault(): boolean;
  clearVault(): void;
  getVault(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setVault(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Qualifier.AsObject;
  static toObject(includeInstance: boolean, msg: Qualifier): Qualifier.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Qualifier, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Qualifier;
  static deserializeBinaryFromReader(message: Qualifier, reader: jspb.BinaryReader): Qualifier;
}

export namespace Qualifier {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    vault?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
  }
}

export class QualifierQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierQuery.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierQuery): QualifierQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierQuery;
  static deserializeBinaryFromReader(message: QualifierQuery, reader: jspb.BinaryReader): QualifierQuery;
}

export namespace QualifierQuery {
  export type AsObject = {
  }
}

export class QualifierQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierQueryInspector): QualifierQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierQueryInspector;
  static deserializeBinaryFromReader(message: QualifierQueryInspector, reader: jspb.BinaryReader): QualifierQueryInspector;
}

export namespace QualifierQueryInspector {
  export type AsObject = {
  }
}

export class QualifierForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierForm.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierForm): QualifierForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierForm;
  static deserializeBinaryFromReader(message: QualifierForm, reader: jspb.BinaryReader): QualifierForm;
}

export namespace QualifierForm {
  export type AsObject = {
  }
}

export class QualifierSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierSearchOrder): QualifierSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierSearchOrder;
  static deserializeBinaryFromReader(message: QualifierSearchOrder, reader: jspb.BinaryReader): QualifierSearchOrder;
}

export namespace QualifierSearchOrder {
  export type AsObject = {
  }
}

export class QualifierSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierSearch.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierSearch): QualifierSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierSearch;
  static deserializeBinaryFromReader(message: QualifierSearch, reader: jspb.BinaryReader): QualifierSearch;
}

export namespace QualifierSearch {
  export type AsObject = {
  }
}

export class QualifierSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierSearchResults): QualifierSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierSearchResults;
  static deserializeBinaryFromReader(message: QualifierSearchResults, reader: jspb.BinaryReader): QualifierSearchResults;
}

export namespace QualifierSearchResults {
  export type AsObject = {
  }
}

export class QualifierList extends jspb.Message {
  clearQualifiersList(): void;
  getQualifiersList(): Array<Qualifier>;
  setQualifiersList(value: Array<Qualifier>): void;
  addQualifiers(value?: Qualifier, index?: number): Qualifier;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierList.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierList): QualifierList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierList;
  static deserializeBinaryFromReader(message: QualifierList, reader: jspb.BinaryReader): QualifierList;
}

export namespace QualifierList {
  export type AsObject = {
    qualifiersList: Array<Qualifier.AsObject>,
  }
}

export class QualifierNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierNode.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierNode): QualifierNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierNode;
  static deserializeBinaryFromReader(message: QualifierNode, reader: jspb.BinaryReader): QualifierNode;
}

export namespace QualifierNode {
  export type AsObject = {
  }
}

export class QualifierNodeList extends jspb.Message {
  clearQualifierNodesList(): void;
  getQualifierNodesList(): Array<QualifierNode>;
  setQualifierNodesList(value: Array<QualifierNode>): void;
  addQualifierNodes(value?: QualifierNode, index?: number): QualifierNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QualifierNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: QualifierNodeList): QualifierNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QualifierNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QualifierNodeList;
  static deserializeBinaryFromReader(message: QualifierNodeList, reader: jspb.BinaryReader): QualifierNodeList;
}

export namespace QualifierNodeList {
  export type AsObject = {
    qualifierNodesList: Array<QualifierNode.AsObject>,
  }
}

export class Vault extends jspb.Message {
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
  toObject(includeInstance?: boolean): Vault.AsObject;
  static toObject(includeInstance: boolean, msg: Vault): Vault.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Vault, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Vault;
  static deserializeBinaryFromReader(message: Vault, reader: jspb.BinaryReader): Vault;
}

export namespace Vault {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class VaultQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultQuery.AsObject;
  static toObject(includeInstance: boolean, msg: VaultQuery): VaultQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultQuery;
  static deserializeBinaryFromReader(message: VaultQuery, reader: jspb.BinaryReader): VaultQuery;
}

export namespace VaultQuery {
  export type AsObject = {
  }
}

export class VaultQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: VaultQueryInspector): VaultQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultQueryInspector;
  static deserializeBinaryFromReader(message: VaultQueryInspector, reader: jspb.BinaryReader): VaultQueryInspector;
}

export namespace VaultQueryInspector {
  export type AsObject = {
  }
}

export class VaultForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultForm.AsObject;
  static toObject(includeInstance: boolean, msg: VaultForm): VaultForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultForm;
  static deserializeBinaryFromReader(message: VaultForm, reader: jspb.BinaryReader): VaultForm;
}

export namespace VaultForm {
  export type AsObject = {
  }
}

export class VaultSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: VaultSearchOrder): VaultSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultSearchOrder;
  static deserializeBinaryFromReader(message: VaultSearchOrder, reader: jspb.BinaryReader): VaultSearchOrder;
}

export namespace VaultSearchOrder {
  export type AsObject = {
  }
}

export class VaultSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultSearch.AsObject;
  static toObject(includeInstance: boolean, msg: VaultSearch): VaultSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultSearch;
  static deserializeBinaryFromReader(message: VaultSearch, reader: jspb.BinaryReader): VaultSearch;
}

export namespace VaultSearch {
  export type AsObject = {
  }
}

export class VaultSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: VaultSearchResults): VaultSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultSearchResults;
  static deserializeBinaryFromReader(message: VaultSearchResults, reader: jspb.BinaryReader): VaultSearchResults;
}

export namespace VaultSearchResults {
  export type AsObject = {
  }
}

export class VaultList extends jspb.Message {
  clearVaultsList(): void;
  getVaultsList(): Array<Vault>;
  setVaultsList(value: Array<Vault>): void;
  addVaults(value?: Vault, index?: number): Vault;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultList.AsObject;
  static toObject(includeInstance: boolean, msg: VaultList): VaultList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultList;
  static deserializeBinaryFromReader(message: VaultList, reader: jspb.BinaryReader): VaultList;
}

export namespace VaultList {
  export type AsObject = {
    vaultsList: Array<Vault.AsObject>,
  }
}

export class VaultNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultNode.AsObject;
  static toObject(includeInstance: boolean, msg: VaultNode): VaultNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultNode;
  static deserializeBinaryFromReader(message: VaultNode, reader: jspb.BinaryReader): VaultNode;
}

export namespace VaultNode {
  export type AsObject = {
  }
}

export class VaultNodeList extends jspb.Message {
  clearVaultNodesList(): void;
  getVaultNodesList(): Array<VaultNode>;
  setVaultNodesList(value: Array<VaultNode>): void;
  addVaultNodes(value?: VaultNode, index?: number): VaultNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VaultNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: VaultNodeList): VaultNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: VaultNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VaultNodeList;
  static deserializeBinaryFromReader(message: VaultNodeList, reader: jspb.BinaryReader): VaultNodeList;
}

export namespace VaultNodeList {
  export type AsObject = {
    vaultNodesList: Array<VaultNode.AsObject>,
  }
}

export class GetVaultIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultIdReply): GetVaultIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultIdReply;
  static deserializeBinaryFromReader(message: GetVaultIdReply, reader: jspb.BinaryReader): GetVaultIdReply;
}

export namespace GetVaultIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultIdRequest): GetVaultIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultIdRequest;
  static deserializeBinaryFromReader(message: GetVaultIdRequest, reader: jspb.BinaryReader): GetVaultIdRequest;
}

export namespace GetVaultIdRequest {
  export type AsObject = {
  }
}

export class GetVaultReply extends jspb.Message {
  hasVault(): boolean;
  clearVault(): void;
  getVault(): Vault | undefined;
  setVault(value?: Vault): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultReply): GetVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultReply;
  static deserializeBinaryFromReader(message: GetVaultReply, reader: jspb.BinaryReader): GetVaultReply;
}

export namespace GetVaultReply {
  export type AsObject = {
    vault?: Vault.AsObject,
  }
}

export class GetVaultRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultRequest): GetVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultRequest;
  static deserializeBinaryFromReader(message: GetVaultRequest, reader: jspb.BinaryReader): GetVaultRequest;
}

export namespace GetVaultRequest {
  export type AsObject = {
  }
}

export class CanAccessAuthorizationsReply extends jspb.Message {
  getCanAccessAuthorizations(): boolean;
  setCanAccessAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAuthorizationsReply): CanAccessAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanAccessAuthorizationsReply, reader: jspb.BinaryReader): CanAccessAuthorizationsReply;
}

export namespace CanAccessAuthorizationsReply {
  export type AsObject = {
    canAccessAuthorizations: boolean,
  }
}

export class CanAccessAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAuthorizationsRequest): CanAccessAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanAccessAuthorizationsRequest, reader: jspb.BinaryReader): CanAccessAuthorizationsRequest;
}

export namespace CanAccessAuthorizationsRequest {
  export type AsObject = {
  }
}

export class IsAuthorizedReply extends jspb.Message {
  getIsAuthorized(): boolean;
  setIsAuthorized(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAuthorizedReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAuthorizedReply): IsAuthorizedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAuthorizedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAuthorizedReply;
  static deserializeBinaryFromReader(message: IsAuthorizedReply, reader: jspb.BinaryReader): IsAuthorizedReply;
}

export namespace IsAuthorizedReply {
  export type AsObject = {
    isAuthorized: boolean,
  }
}

export class IsAuthorizedRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasQualifierId(): boolean;
  clearQualifierId(): void;
  getQualifierId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAuthorizedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAuthorizedRequest): IsAuthorizedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAuthorizedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAuthorizedRequest;
  static deserializeBinaryFromReader(message: IsAuthorizedRequest, reader: jspb.BinaryReader): IsAuthorizedRequest;
}

export namespace IsAuthorizedRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    qualifierId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationConditionReply extends jspb.Message {
  hasAuthorizationCondition(): boolean;
  clearAuthorizationCondition(): void;
  getAuthorizationCondition(): AuthorizationCondition | undefined;
  setAuthorizationCondition(value?: AuthorizationCondition): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationConditionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationConditionReply): GetAuthorizationConditionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationConditionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationConditionReply;
  static deserializeBinaryFromReader(message: GetAuthorizationConditionReply, reader: jspb.BinaryReader): GetAuthorizationConditionReply;
}

export namespace GetAuthorizationConditionReply {
  export type AsObject = {
    authorizationCondition?: AuthorizationCondition.AsObject,
  }
}

export class GetAuthorizationConditionRequest extends jspb.Message {
  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationConditionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationConditionRequest): GetAuthorizationConditionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationConditionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationConditionRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationConditionRequest, reader: jspb.BinaryReader): GetAuthorizationConditionRequest;
}

export namespace GetAuthorizationConditionRequest {
  export type AsObject = {
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAuthorizedOnConditionReply extends jspb.Message {
  getIsAuthorizedOnCondition(): boolean;
  setIsAuthorizedOnCondition(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAuthorizedOnConditionReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAuthorizedOnConditionReply): IsAuthorizedOnConditionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAuthorizedOnConditionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAuthorizedOnConditionReply;
  static deserializeBinaryFromReader(message: IsAuthorizedOnConditionReply, reader: jspb.BinaryReader): IsAuthorizedOnConditionReply;
}

export namespace IsAuthorizedOnConditionReply {
  export type AsObject = {
    isAuthorizedOnCondition: boolean,
  }
}

export class IsAuthorizedOnConditionRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCondition(): boolean;
  clearCondition(): void;
  getCondition(): AuthorizationCondition | undefined;
  setCondition(value?: AuthorizationCondition): void;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasQualifierId(): boolean;
  clearQualifierId(): void;
  getQualifierId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAuthorizedOnConditionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAuthorizedOnConditionRequest): IsAuthorizedOnConditionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAuthorizedOnConditionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAuthorizedOnConditionRequest;
  static deserializeBinaryFromReader(message: IsAuthorizedOnConditionRequest, reader: jspb.BinaryReader): IsAuthorizedOnConditionRequest;
}

export namespace IsAuthorizedOnConditionRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    condition?: AuthorizationCondition.AsObject,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    qualifierId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAuthorizationsReply extends jspb.Message {
  getCanLookupAuthorizations(): boolean;
  setCanLookupAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAuthorizationsReply): CanLookupAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanLookupAuthorizationsReply, reader: jspb.BinaryReader): CanLookupAuthorizationsReply;
}

export namespace CanLookupAuthorizationsReply {
  export type AsObject = {
    canLookupAuthorizations: boolean,
  }
}

export class CanLookupAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAuthorizationsRequest): CanLookupAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanLookupAuthorizationsRequest, reader: jspb.BinaryReader): CanLookupAuthorizationsRequest;
}

export namespace CanLookupAuthorizationsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAuthorizationViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAuthorizationViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAuthorizationViewReply): UseComparativeAuthorizationViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAuthorizationViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAuthorizationViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAuthorizationViewReply, reader: jspb.BinaryReader): UseComparativeAuthorizationViewReply;
}

export namespace UseComparativeAuthorizationViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAuthorizationViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAuthorizationViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAuthorizationViewRequest): UseComparativeAuthorizationViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAuthorizationViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAuthorizationViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAuthorizationViewRequest, reader: jspb.BinaryReader): UseComparativeAuthorizationViewRequest;
}

export namespace UseComparativeAuthorizationViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAuthorizationViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAuthorizationViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAuthorizationViewReply): UsePlenaryAuthorizationViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAuthorizationViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAuthorizationViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAuthorizationViewReply, reader: jspb.BinaryReader): UsePlenaryAuthorizationViewReply;
}

export namespace UsePlenaryAuthorizationViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAuthorizationViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAuthorizationViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAuthorizationViewRequest): UsePlenaryAuthorizationViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAuthorizationViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAuthorizationViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAuthorizationViewRequest, reader: jspb.BinaryReader): UsePlenaryAuthorizationViewRequest;
}

export namespace UsePlenaryAuthorizationViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedVaultViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedVaultViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedVaultViewReply): UseFederatedVaultViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedVaultViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedVaultViewReply;
  static deserializeBinaryFromReader(message: UseFederatedVaultViewReply, reader: jspb.BinaryReader): UseFederatedVaultViewReply;
}

export namespace UseFederatedVaultViewReply {
  export type AsObject = {
  }
}

export class UseFederatedVaultViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedVaultViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedVaultViewRequest): UseFederatedVaultViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedVaultViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedVaultViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedVaultViewRequest, reader: jspb.BinaryReader): UseFederatedVaultViewRequest;
}

export namespace UseFederatedVaultViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedVaultViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedVaultViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedVaultViewReply): UseIsolatedVaultViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedVaultViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedVaultViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedVaultViewReply, reader: jspb.BinaryReader): UseIsolatedVaultViewReply;
}

export namespace UseIsolatedVaultViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedVaultViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedVaultViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedVaultViewRequest): UseIsolatedVaultViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedVaultViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedVaultViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedVaultViewRequest, reader: jspb.BinaryReader): UseIsolatedVaultViewRequest;
}

export namespace UseIsolatedVaultViewRequest {
  export type AsObject = {
  }
}

export class UseEffectiveAuthorizationViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveAuthorizationViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveAuthorizationViewReply): UseEffectiveAuthorizationViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveAuthorizationViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveAuthorizationViewReply;
  static deserializeBinaryFromReader(message: UseEffectiveAuthorizationViewReply, reader: jspb.BinaryReader): UseEffectiveAuthorizationViewReply;
}

export namespace UseEffectiveAuthorizationViewReply {
  export type AsObject = {
  }
}

export class UseEffectiveAuthorizationViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveAuthorizationViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveAuthorizationViewRequest): UseEffectiveAuthorizationViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveAuthorizationViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveAuthorizationViewRequest;
  static deserializeBinaryFromReader(message: UseEffectiveAuthorizationViewRequest, reader: jspb.BinaryReader): UseEffectiveAuthorizationViewRequest;
}

export namespace UseEffectiveAuthorizationViewRequest {
  export type AsObject = {
  }
}

export class UseAnyEffectiveAuthorizationViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveAuthorizationViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveAuthorizationViewReply): UseAnyEffectiveAuthorizationViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveAuthorizationViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveAuthorizationViewReply;
  static deserializeBinaryFromReader(message: UseAnyEffectiveAuthorizationViewReply, reader: jspb.BinaryReader): UseAnyEffectiveAuthorizationViewReply;
}

export namespace UseAnyEffectiveAuthorizationViewReply {
  export type AsObject = {
  }
}

export class UseAnyEffectiveAuthorizationViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveAuthorizationViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveAuthorizationViewRequest): UseAnyEffectiveAuthorizationViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveAuthorizationViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveAuthorizationViewRequest;
  static deserializeBinaryFromReader(message: UseAnyEffectiveAuthorizationViewRequest, reader: jspb.BinaryReader): UseAnyEffectiveAuthorizationViewRequest;
}

export namespace UseAnyEffectiveAuthorizationViewRequest {
  export type AsObject = {
  }
}

export class UseImplicitAuthorizationViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseImplicitAuthorizationViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseImplicitAuthorizationViewReply): UseImplicitAuthorizationViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseImplicitAuthorizationViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseImplicitAuthorizationViewReply;
  static deserializeBinaryFromReader(message: UseImplicitAuthorizationViewReply, reader: jspb.BinaryReader): UseImplicitAuthorizationViewReply;
}

export namespace UseImplicitAuthorizationViewReply {
  export type AsObject = {
  }
}

export class UseImplicitAuthorizationViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseImplicitAuthorizationViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseImplicitAuthorizationViewRequest): UseImplicitAuthorizationViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseImplicitAuthorizationViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseImplicitAuthorizationViewRequest;
  static deserializeBinaryFromReader(message: UseImplicitAuthorizationViewRequest, reader: jspb.BinaryReader): UseImplicitAuthorizationViewRequest;
}

export namespace UseImplicitAuthorizationViewRequest {
  export type AsObject = {
  }
}

export class UseExplicitAuthorizationViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseExplicitAuthorizationViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseExplicitAuthorizationViewReply): UseExplicitAuthorizationViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseExplicitAuthorizationViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseExplicitAuthorizationViewReply;
  static deserializeBinaryFromReader(message: UseExplicitAuthorizationViewReply, reader: jspb.BinaryReader): UseExplicitAuthorizationViewReply;
}

export namespace UseExplicitAuthorizationViewReply {
  export type AsObject = {
  }
}

export class UseExplicitAuthorizationViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseExplicitAuthorizationViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseExplicitAuthorizationViewRequest): UseExplicitAuthorizationViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseExplicitAuthorizationViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseExplicitAuthorizationViewRequest;
  static deserializeBinaryFromReader(message: UseExplicitAuthorizationViewRequest, reader: jspb.BinaryReader): UseExplicitAuthorizationViewRequest;
}

export namespace UseExplicitAuthorizationViewRequest {
  export type AsObject = {
  }
}

export class GetAuthorizationReply extends jspb.Message {
  hasAuthorization(): boolean;
  clearAuthorization(): void;
  getAuthorization(): Authorization | undefined;
  setAuthorization(value?: Authorization): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationReply): GetAuthorizationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationReply;
  static deserializeBinaryFromReader(message: GetAuthorizationReply, reader: jspb.BinaryReader): GetAuthorizationReply;
}

export namespace GetAuthorizationReply {
  export type AsObject = {
    authorization?: Authorization.AsObject,
  }
}

export class GetAuthorizationRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationRequest): GetAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationRequest, reader: jspb.BinaryReader): GetAuthorizationRequest;
}

export namespace GetAuthorizationRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsByIdsRequest extends jspb.Message {
  clearAuthorizationIdsList(): void;
  getAuthorizationIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAuthorizationIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAuthorizationIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByIdsRequest): GetAuthorizationsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByIdsRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByIdsRequest, reader: jspb.BinaryReader): GetAuthorizationsByIdsRequest;
}

export namespace GetAuthorizationsByIdsRequest {
  export type AsObject = {
    authorizationIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAuthorizationsByGenusTypeRequest extends jspb.Message {
  hasAuthorizationGenusType(): boolean;
  clearAuthorizationGenusType(): void;
  getAuthorizationGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAuthorizationGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByGenusTypeRequest): GetAuthorizationsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByGenusTypeRequest, reader: jspb.BinaryReader): GetAuthorizationsByGenusTypeRequest;
}

export namespace GetAuthorizationsByGenusTypeRequest {
  export type AsObject = {
    authorizationGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAuthorizationsByParentGenusTypeRequest extends jspb.Message {
  hasAuthorizationGenusType(): boolean;
  clearAuthorizationGenusType(): void;
  getAuthorizationGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAuthorizationGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByParentGenusTypeRequest): GetAuthorizationsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAuthorizationsByParentGenusTypeRequest;
}

export namespace GetAuthorizationsByParentGenusTypeRequest {
  export type AsObject = {
    authorizationGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAuthorizationsByRecordTypeRequest extends jspb.Message {
  hasAuthorizationRecordType(): boolean;
  clearAuthorizationRecordType(): void;
  getAuthorizationRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAuthorizationRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByRecordTypeRequest): GetAuthorizationsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByRecordTypeRequest, reader: jspb.BinaryReader): GetAuthorizationsByRecordTypeRequest;
}

export namespace GetAuthorizationsByRecordTypeRequest {
  export type AsObject = {
    authorizationRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAuthorizationsOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsOnDateRequest): GetAuthorizationsOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsOnDateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsOnDateRequest, reader: jspb.BinaryReader): GetAuthorizationsOnDateRequest;
}

export namespace GetAuthorizationsOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAuthorizationsForResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForResourceRequest): GetAuthorizationsForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForResourceRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForResourceRequest, reader: jspb.BinaryReader): GetAuthorizationsForResourceRequest;
}

export namespace GetAuthorizationsForResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsForResourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForResourceOnDateRequest): GetAuthorizationsForResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForResourceOnDateRequest, reader: jspb.BinaryReader): GetAuthorizationsForResourceOnDateRequest;
}

export namespace GetAuthorizationsForResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAuthorizationsForAgentRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForAgentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForAgentRequest): GetAuthorizationsForAgentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForAgentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForAgentRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForAgentRequest, reader: jspb.BinaryReader): GetAuthorizationsForAgentRequest;
}

export namespace GetAuthorizationsForAgentRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsForAgentOnDateRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForAgentOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForAgentOnDateRequest): GetAuthorizationsForAgentOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForAgentOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForAgentOnDateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForAgentOnDateRequest, reader: jspb.BinaryReader): GetAuthorizationsForAgentOnDateRequest;
}

export namespace GetAuthorizationsForAgentOnDateRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAuthorizationsForFunctionRequest extends jspb.Message {
  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForFunctionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForFunctionRequest): GetAuthorizationsForFunctionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForFunctionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForFunctionRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForFunctionRequest, reader: jspb.BinaryReader): GetAuthorizationsForFunctionRequest;
}

export namespace GetAuthorizationsForFunctionRequest {
  export type AsObject = {
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsForFunctionOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForFunctionOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForFunctionOnDateRequest): GetAuthorizationsForFunctionOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForFunctionOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForFunctionOnDateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForFunctionOnDateRequest, reader: jspb.BinaryReader): GetAuthorizationsForFunctionOnDateRequest;
}

export namespace GetAuthorizationsForFunctionOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAuthorizationsForResourceAndFunctionRequest extends jspb.Message {
  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForResourceAndFunctionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForResourceAndFunctionRequest): GetAuthorizationsForResourceAndFunctionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForResourceAndFunctionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForResourceAndFunctionRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForResourceAndFunctionRequest, reader: jspb.BinaryReader): GetAuthorizationsForResourceAndFunctionRequest;
}

export namespace GetAuthorizationsForResourceAndFunctionRequest {
  export type AsObject = {
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsForResourceAndFunctionOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForResourceAndFunctionOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForResourceAndFunctionOnDateRequest): GetAuthorizationsForResourceAndFunctionOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForResourceAndFunctionOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForResourceAndFunctionOnDateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForResourceAndFunctionOnDateRequest, reader: jspb.BinaryReader): GetAuthorizationsForResourceAndFunctionOnDateRequest;
}

export namespace GetAuthorizationsForResourceAndFunctionOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAuthorizationsForAgentAndFunctionRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForAgentAndFunctionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForAgentAndFunctionRequest): GetAuthorizationsForAgentAndFunctionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForAgentAndFunctionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForAgentAndFunctionRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForAgentAndFunctionRequest, reader: jspb.BinaryReader): GetAuthorizationsForAgentAndFunctionRequest;
}

export namespace GetAuthorizationsForAgentAndFunctionRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsForAgentAndFunctionOnDateRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsForAgentAndFunctionOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsForAgentAndFunctionOnDateRequest): GetAuthorizationsForAgentAndFunctionOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsForAgentAndFunctionOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsForAgentAndFunctionOnDateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsForAgentAndFunctionOnDateRequest, reader: jspb.BinaryReader): GetAuthorizationsForAgentAndFunctionOnDateRequest;
}

export namespace GetAuthorizationsForAgentAndFunctionOnDateRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAuthorizationsByQualifierRequest extends jspb.Message {
  hasQualifierId(): boolean;
  clearQualifierId(): void;
  getQualifierId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByQualifierRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByQualifierRequest): GetAuthorizationsByQualifierRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByQualifierRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByQualifierRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByQualifierRequest, reader: jspb.BinaryReader): GetAuthorizationsByQualifierRequest;
}

export namespace GetAuthorizationsByQualifierRequest {
  export type AsObject = {
    qualifierId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetExplicitAuthorizationReply extends jspb.Message {
  hasAuthorization(): boolean;
  clearAuthorization(): void;
  getAuthorization(): Authorization | undefined;
  setAuthorization(value?: Authorization): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetExplicitAuthorizationReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetExplicitAuthorizationReply): GetExplicitAuthorizationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetExplicitAuthorizationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetExplicitAuthorizationReply;
  static deserializeBinaryFromReader(message: GetExplicitAuthorizationReply, reader: jspb.BinaryReader): GetExplicitAuthorizationReply;
}

export namespace GetExplicitAuthorizationReply {
  export type AsObject = {
    authorization?: Authorization.AsObject,
  }
}

export class GetExplicitAuthorizationRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetExplicitAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetExplicitAuthorizationRequest): GetExplicitAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetExplicitAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetExplicitAuthorizationRequest;
  static deserializeBinaryFromReader(message: GetExplicitAuthorizationRequest, reader: jspb.BinaryReader): GetExplicitAuthorizationRequest;
}

export namespace GetExplicitAuthorizationRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsRequest): GetAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsRequest, reader: jspb.BinaryReader): GetAuthorizationsRequest;
}

export namespace GetAuthorizationsRequest {
  export type AsObject = {
  }
}

export class CanSearchAuthorizationsReply extends jspb.Message {
  getCanSearchAuthorizations(): boolean;
  setCanSearchAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAuthorizationsReply): CanSearchAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanSearchAuthorizationsReply, reader: jspb.BinaryReader): CanSearchAuthorizationsReply;
}

export namespace CanSearchAuthorizationsReply {
  export type AsObject = {
    canSearchAuthorizations: boolean,
  }
}

export class CanSearchAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAuthorizationsRequest): CanSearchAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanSearchAuthorizationsRequest, reader: jspb.BinaryReader): CanSearchAuthorizationsRequest;
}

export namespace CanSearchAuthorizationsRequest {
  export type AsObject = {
  }
}

export class GetAuthorizationQueryReply extends jspb.Message {
  hasAuthorizationQuery(): boolean;
  clearAuthorizationQuery(): void;
  getAuthorizationQuery(): AuthorizationQuery | undefined;
  setAuthorizationQuery(value?: AuthorizationQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationQueryReply): GetAuthorizationQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationQueryReply;
  static deserializeBinaryFromReader(message: GetAuthorizationQueryReply, reader: jspb.BinaryReader): GetAuthorizationQueryReply;
}

export namespace GetAuthorizationQueryReply {
  export type AsObject = {
    authorizationQuery?: AuthorizationQuery.AsObject,
  }
}

export class GetAuthorizationQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationQueryRequest): GetAuthorizationQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationQueryRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationQueryRequest, reader: jspb.BinaryReader): GetAuthorizationQueryRequest;
}

export namespace GetAuthorizationQueryRequest {
  export type AsObject = {
  }
}

export class GetAuthorizationsByQueryRequest extends jspb.Message {
  hasAuthorizationQuery(): boolean;
  clearAuthorizationQuery(): void;
  getAuthorizationQuery(): AuthorizationQuery | undefined;
  setAuthorizationQuery(value?: AuthorizationQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByQueryRequest): GetAuthorizationsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByQueryRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByQueryRequest, reader: jspb.BinaryReader): GetAuthorizationsByQueryRequest;
}

export namespace GetAuthorizationsByQueryRequest {
  export type AsObject = {
    authorizationQuery?: AuthorizationQuery.AsObject,
  }
}

export class CanCreateAuthorizationsReply extends jspb.Message {
  getCanCreateAuthorizations(): boolean;
  setCanCreateAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAuthorizationsReply): CanCreateAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanCreateAuthorizationsReply, reader: jspb.BinaryReader): CanCreateAuthorizationsReply;
}

export namespace CanCreateAuthorizationsReply {
  export type AsObject = {
    canCreateAuthorizations: boolean,
  }
}

export class CanCreateAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAuthorizationsRequest): CanCreateAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanCreateAuthorizationsRequest, reader: jspb.BinaryReader): CanCreateAuthorizationsRequest;
}

export namespace CanCreateAuthorizationsRequest {
  export type AsObject = {
  }
}

export class CanCreateAuthorizationWithRecordTypesReply extends jspb.Message {
  getCanCreateAuthorizationWithRecordTypes(): boolean;
  setCanCreateAuthorizationWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAuthorizationWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAuthorizationWithRecordTypesReply): CanCreateAuthorizationWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAuthorizationWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAuthorizationWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAuthorizationWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAuthorizationWithRecordTypesReply;
}

export namespace CanCreateAuthorizationWithRecordTypesReply {
  export type AsObject = {
    canCreateAuthorizationWithRecordTypes: boolean,
  }
}

export class CanCreateAuthorizationWithRecordTypesRequest extends jspb.Message {
  clearAuthorizationRecordTypesList(): void;
  getAuthorizationRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAuthorizationRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAuthorizationRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAuthorizationWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAuthorizationWithRecordTypesRequest): CanCreateAuthorizationWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAuthorizationWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAuthorizationWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAuthorizationWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAuthorizationWithRecordTypesRequest;
}

export namespace CanCreateAuthorizationWithRecordTypesRequest {
  export type AsObject = {
    authorizationRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAuthorizationFormForCreateForAgentReply extends jspb.Message {
  hasAuthorizationForm(): boolean;
  clearAuthorizationForm(): void;
  getAuthorizationForm(): AuthorizationForm | undefined;
  setAuthorizationForm(value?: AuthorizationForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForCreateForAgentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForCreateForAgentReply): GetAuthorizationFormForCreateForAgentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForCreateForAgentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForCreateForAgentReply;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForCreateForAgentReply, reader: jspb.BinaryReader): GetAuthorizationFormForCreateForAgentReply;
}

export namespace GetAuthorizationFormForCreateForAgentReply {
  export type AsObject = {
    authorizationForm?: AuthorizationForm.AsObject,
  }
}

export class GetAuthorizationFormForCreateForAgentRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearAuthorizationRecordTypesList(): void;
  getAuthorizationRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAuthorizationRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAuthorizationRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasQualifierId(): boolean;
  clearQualifierId(): void;
  getQualifierId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForCreateForAgentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForCreateForAgentRequest): GetAuthorizationFormForCreateForAgentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForCreateForAgentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForCreateForAgentRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForCreateForAgentRequest, reader: jspb.BinaryReader): GetAuthorizationFormForCreateForAgentRequest;
}

export namespace GetAuthorizationFormForCreateForAgentRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    authorizationRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    qualifierId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationFormForCreateForResourceReply extends jspb.Message {
  hasAuthorizationForm(): boolean;
  clearAuthorizationForm(): void;
  getAuthorizationForm(): AuthorizationForm | undefined;
  setAuthorizationForm(value?: AuthorizationForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForCreateForResourceReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForCreateForResourceReply): GetAuthorizationFormForCreateForResourceReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForCreateForResourceReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForCreateForResourceReply;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForCreateForResourceReply, reader: jspb.BinaryReader): GetAuthorizationFormForCreateForResourceReply;
}

export namespace GetAuthorizationFormForCreateForResourceReply {
  export type AsObject = {
    authorizationForm?: AuthorizationForm.AsObject,
  }
}

export class GetAuthorizationFormForCreateForResourceRequest extends jspb.Message {
  clearAuthorizationRecordTypesList(): void;
  getAuthorizationRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAuthorizationRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAuthorizationRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasQualifierId(): boolean;
  clearQualifierId(): void;
  getQualifierId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForCreateForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForCreateForResourceRequest): GetAuthorizationFormForCreateForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForCreateForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForCreateForResourceRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForCreateForResourceRequest, reader: jspb.BinaryReader): GetAuthorizationFormForCreateForResourceRequest;
}

export namespace GetAuthorizationFormForCreateForResourceRequest {
  export type AsObject = {
    authorizationRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    qualifierId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationFormForCreateForResourceAndTrustReply extends jspb.Message {
  hasAuthorizationForm(): boolean;
  clearAuthorizationForm(): void;
  getAuthorizationForm(): AuthorizationForm | undefined;
  setAuthorizationForm(value?: AuthorizationForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForCreateForResourceAndTrustReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForCreateForResourceAndTrustReply): GetAuthorizationFormForCreateForResourceAndTrustReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForCreateForResourceAndTrustReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForCreateForResourceAndTrustReply;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForCreateForResourceAndTrustReply, reader: jspb.BinaryReader): GetAuthorizationFormForCreateForResourceAndTrustReply;
}

export namespace GetAuthorizationFormForCreateForResourceAndTrustReply {
  export type AsObject = {
    authorizationForm?: AuthorizationForm.AsObject,
  }
}

export class GetAuthorizationFormForCreateForResourceAndTrustRequest extends jspb.Message {
  clearAuthorizationRecordTypesList(): void;
  getAuthorizationRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAuthorizationRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAuthorizationRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasFunctionId(): boolean;
  clearFunctionId(): void;
  getFunctionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFunctionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasQualifierId(): boolean;
  clearQualifierId(): void;
  getQualifierId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQualifierId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTrustId(): boolean;
  clearTrustId(): void;
  getTrustId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setTrustId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForCreateForResourceAndTrustRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForCreateForResourceAndTrustRequest): GetAuthorizationFormForCreateForResourceAndTrustRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForCreateForResourceAndTrustRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForCreateForResourceAndTrustRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForCreateForResourceAndTrustRequest, reader: jspb.BinaryReader): GetAuthorizationFormForCreateForResourceAndTrustRequest;
}

export namespace GetAuthorizationFormForCreateForResourceAndTrustRequest {
  export type AsObject = {
    authorizationRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    functionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    qualifierId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    trustId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateAuthorizationReply extends jspb.Message {
  hasAuthorization(): boolean;
  clearAuthorization(): void;
  getAuthorization(): Authorization | undefined;
  setAuthorization(value?: Authorization): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAuthorizationReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAuthorizationReply): CreateAuthorizationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAuthorizationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAuthorizationReply;
  static deserializeBinaryFromReader(message: CreateAuthorizationReply, reader: jspb.BinaryReader): CreateAuthorizationReply;
}

export namespace CreateAuthorizationReply {
  export type AsObject = {
    authorization?: Authorization.AsObject,
  }
}

export class CreateAuthorizationRequest extends jspb.Message {
  hasAuthorizationForm(): boolean;
  clearAuthorizationForm(): void;
  getAuthorizationForm(): AuthorizationForm | undefined;
  setAuthorizationForm(value?: AuthorizationForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAuthorizationRequest): CreateAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAuthorizationRequest;
  static deserializeBinaryFromReader(message: CreateAuthorizationRequest, reader: jspb.BinaryReader): CreateAuthorizationRequest;
}

export namespace CreateAuthorizationRequest {
  export type AsObject = {
    authorizationForm?: AuthorizationForm.AsObject,
  }
}

export class CanUpdateAuthorizationsReply extends jspb.Message {
  getCanUpdateAuthorizations(): boolean;
  setCanUpdateAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAuthorizationsReply): CanUpdateAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanUpdateAuthorizationsReply, reader: jspb.BinaryReader): CanUpdateAuthorizationsReply;
}

export namespace CanUpdateAuthorizationsReply {
  export type AsObject = {
    canUpdateAuthorizations: boolean,
  }
}

export class CanUpdateAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAuthorizationsRequest): CanUpdateAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanUpdateAuthorizationsRequest, reader: jspb.BinaryReader): CanUpdateAuthorizationsRequest;
}

export namespace CanUpdateAuthorizationsRequest {
  export type AsObject = {
  }
}

export class GetAuthorizationFormForUpdateReply extends jspb.Message {
  hasAuthorizationForm(): boolean;
  clearAuthorizationForm(): void;
  getAuthorizationForm(): AuthorizationForm | undefined;
  setAuthorizationForm(value?: AuthorizationForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForUpdateReply): GetAuthorizationFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForUpdateReply, reader: jspb.BinaryReader): GetAuthorizationFormForUpdateReply;
}

export namespace GetAuthorizationFormForUpdateReply {
  export type AsObject = {
    authorizationForm?: AuthorizationForm.AsObject,
  }
}

export class GetAuthorizationFormForUpdateRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationFormForUpdateRequest): GetAuthorizationFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationFormForUpdateRequest, reader: jspb.BinaryReader): GetAuthorizationFormForUpdateRequest;
}

export namespace GetAuthorizationFormForUpdateRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAuthorizationReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAuthorizationReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAuthorizationReply): UpdateAuthorizationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAuthorizationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAuthorizationReply;
  static deserializeBinaryFromReader(message: UpdateAuthorizationReply, reader: jspb.BinaryReader): UpdateAuthorizationReply;
}

export namespace UpdateAuthorizationReply {
  export type AsObject = {
  }
}

export class UpdateAuthorizationRequest extends jspb.Message {
  hasAuthorizationForm(): boolean;
  clearAuthorizationForm(): void;
  getAuthorizationForm(): AuthorizationForm | undefined;
  setAuthorizationForm(value?: AuthorizationForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAuthorizationRequest): UpdateAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAuthorizationRequest;
  static deserializeBinaryFromReader(message: UpdateAuthorizationRequest, reader: jspb.BinaryReader): UpdateAuthorizationRequest;
}

export namespace UpdateAuthorizationRequest {
  export type AsObject = {
    authorizationForm?: AuthorizationForm.AsObject,
  }
}

export class CanDeleteAuthorizationsReply extends jspb.Message {
  getCanDeleteAuthorizations(): boolean;
  setCanDeleteAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAuthorizationsReply): CanDeleteAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanDeleteAuthorizationsReply, reader: jspb.BinaryReader): CanDeleteAuthorizationsReply;
}

export namespace CanDeleteAuthorizationsReply {
  export type AsObject = {
    canDeleteAuthorizations: boolean,
  }
}

export class CanDeleteAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAuthorizationsRequest): CanDeleteAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanDeleteAuthorizationsRequest, reader: jspb.BinaryReader): CanDeleteAuthorizationsRequest;
}

export namespace CanDeleteAuthorizationsRequest {
  export type AsObject = {
  }
}

export class DeleteAuthorizationReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAuthorizationReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAuthorizationReply): DeleteAuthorizationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAuthorizationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAuthorizationReply;
  static deserializeBinaryFromReader(message: DeleteAuthorizationReply, reader: jspb.BinaryReader): DeleteAuthorizationReply;
}

export namespace DeleteAuthorizationReply {
  export type AsObject = {
  }
}

export class DeleteAuthorizationRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAuthorizationRequest): DeleteAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAuthorizationRequest;
  static deserializeBinaryFromReader(message: DeleteAuthorizationRequest, reader: jspb.BinaryReader): DeleteAuthorizationRequest;
}

export namespace DeleteAuthorizationRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageAuthorizationAliasesReply extends jspb.Message {
  getCanManageAuthorizationAliases(): boolean;
  setCanManageAuthorizationAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAuthorizationAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAuthorizationAliasesReply): CanManageAuthorizationAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAuthorizationAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAuthorizationAliasesReply;
  static deserializeBinaryFromReader(message: CanManageAuthorizationAliasesReply, reader: jspb.BinaryReader): CanManageAuthorizationAliasesReply;
}

export namespace CanManageAuthorizationAliasesReply {
  export type AsObject = {
    canManageAuthorizationAliases: boolean,
  }
}

export class CanManageAuthorizationAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAuthorizationAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAuthorizationAliasesRequest): CanManageAuthorizationAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAuthorizationAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAuthorizationAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageAuthorizationAliasesRequest, reader: jspb.BinaryReader): CanManageAuthorizationAliasesRequest;
}

export namespace CanManageAuthorizationAliasesRequest {
  export type AsObject = {
  }
}

export class AliasAuthorizationReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAuthorizationReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAuthorizationReply): AliasAuthorizationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAuthorizationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAuthorizationReply;
  static deserializeBinaryFromReader(message: AliasAuthorizationReply, reader: jspb.BinaryReader): AliasAuthorizationReply;
}

export namespace AliasAuthorizationReply {
  export type AsObject = {
  }
}

export class AliasAuthorizationRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAuthorizationRequest): AliasAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAuthorizationRequest;
  static deserializeBinaryFromReader(message: AliasAuthorizationRequest, reader: jspb.BinaryReader): AliasAuthorizationRequest;
}

export namespace AliasAuthorizationRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UseComparativeVaultViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeVaultViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeVaultViewReply): UseComparativeVaultViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeVaultViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeVaultViewReply;
  static deserializeBinaryFromReader(message: UseComparativeVaultViewReply, reader: jspb.BinaryReader): UseComparativeVaultViewReply;
}

export namespace UseComparativeVaultViewReply {
  export type AsObject = {
  }
}

export class UseComparativeVaultViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeVaultViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeVaultViewRequest): UseComparativeVaultViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeVaultViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeVaultViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeVaultViewRequest, reader: jspb.BinaryReader): UseComparativeVaultViewRequest;
}

export namespace UseComparativeVaultViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryVaultViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryVaultViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryVaultViewReply): UsePlenaryVaultViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryVaultViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryVaultViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryVaultViewReply, reader: jspb.BinaryReader): UsePlenaryVaultViewReply;
}

export namespace UsePlenaryVaultViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryVaultViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryVaultViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryVaultViewRequest): UsePlenaryVaultViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryVaultViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryVaultViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryVaultViewRequest, reader: jspb.BinaryReader): UsePlenaryVaultViewRequest;
}

export namespace UsePlenaryVaultViewRequest {
  export type AsObject = {
  }
}

export class CanLookupAuthorizationVaultMappingsReply extends jspb.Message {
  getCanLookupAuthorizationVaultMappings(): boolean;
  setCanLookupAuthorizationVaultMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAuthorizationVaultMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAuthorizationVaultMappingsReply): CanLookupAuthorizationVaultMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAuthorizationVaultMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAuthorizationVaultMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupAuthorizationVaultMappingsReply, reader: jspb.BinaryReader): CanLookupAuthorizationVaultMappingsReply;
}

export namespace CanLookupAuthorizationVaultMappingsReply {
  export type AsObject = {
    canLookupAuthorizationVaultMappings: boolean,
  }
}

export class CanLookupAuthorizationVaultMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAuthorizationVaultMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAuthorizationVaultMappingsRequest): CanLookupAuthorizationVaultMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAuthorizationVaultMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAuthorizationVaultMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupAuthorizationVaultMappingsRequest, reader: jspb.BinaryReader): CanLookupAuthorizationVaultMappingsRequest;
}

export namespace CanLookupAuthorizationVaultMappingsRequest {
  export type AsObject = {
  }
}

export class GetAuthorizationIdsByVaultRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationIdsByVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationIdsByVaultRequest): GetAuthorizationIdsByVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationIdsByVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationIdsByVaultRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationIdsByVaultRequest, reader: jspb.BinaryReader): GetAuthorizationIdsByVaultRequest;
}

export namespace GetAuthorizationIdsByVaultRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsByVaultRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsByVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsByVaultRequest): GetAuthorizationsByVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsByVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsByVaultRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsByVaultRequest, reader: jspb.BinaryReader): GetAuthorizationsByVaultRequest;
}

export namespace GetAuthorizationsByVaultRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAuthorizationsIdsByVaultRequest extends jspb.Message {
  clearVaultIdsList(): void;
  getVaultIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setVaultIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addVaultIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizationsIdsByVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizationsIdsByVaultRequest): GetAuthorizationsIdsByVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAuthorizationsIdsByVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizationsIdsByVaultRequest;
  static deserializeBinaryFromReader(message: GetAuthorizationsIdsByVaultRequest, reader: jspb.BinaryReader): GetAuthorizationsIdsByVaultRequest;
}

export namespace GetAuthorizationsIdsByVaultRequest {
  export type AsObject = {
    vaultIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetVaultIdsByAuthorizationRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultIdsByAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultIdsByAuthorizationRequest): GetVaultIdsByAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultIdsByAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultIdsByAuthorizationRequest;
  static deserializeBinaryFromReader(message: GetVaultIdsByAuthorizationRequest, reader: jspb.BinaryReader): GetVaultIdsByAuthorizationRequest;
}

export namespace GetVaultIdsByAuthorizationRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultByAuthorizationRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultByAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultByAuthorizationRequest): GetVaultByAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultByAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultByAuthorizationRequest;
  static deserializeBinaryFromReader(message: GetVaultByAuthorizationRequest, reader: jspb.BinaryReader): GetVaultByAuthorizationRequest;
}

export namespace GetVaultByAuthorizationRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAuthorizationsReply extends jspb.Message {
  getCanAssignAuthorizations(): boolean;
  setCanAssignAuthorizations(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAuthorizationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAuthorizationsReply): CanAssignAuthorizationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAuthorizationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAuthorizationsReply;
  static deserializeBinaryFromReader(message: CanAssignAuthorizationsReply, reader: jspb.BinaryReader): CanAssignAuthorizationsReply;
}

export namespace CanAssignAuthorizationsReply {
  export type AsObject = {
    canAssignAuthorizations: boolean,
  }
}

export class CanAssignAuthorizationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAuthorizationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAuthorizationsRequest): CanAssignAuthorizationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAuthorizationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAuthorizationsRequest;
  static deserializeBinaryFromReader(message: CanAssignAuthorizationsRequest, reader: jspb.BinaryReader): CanAssignAuthorizationsRequest;
}

export namespace CanAssignAuthorizationsRequest {
  export type AsObject = {
  }
}

export class CanAssignAuthorizationsToVaultReply extends jspb.Message {
  getCanAssignAuthorizationsToVault(): boolean;
  setCanAssignAuthorizationsToVault(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAuthorizationsToVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAuthorizationsToVaultReply): CanAssignAuthorizationsToVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAuthorizationsToVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAuthorizationsToVaultReply;
  static deserializeBinaryFromReader(message: CanAssignAuthorizationsToVaultReply, reader: jspb.BinaryReader): CanAssignAuthorizationsToVaultReply;
}

export namespace CanAssignAuthorizationsToVaultReply {
  export type AsObject = {
    canAssignAuthorizationsToVault: boolean,
  }
}

export class CanAssignAuthorizationsToVaultRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAuthorizationsToVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAuthorizationsToVaultRequest): CanAssignAuthorizationsToVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAuthorizationsToVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAuthorizationsToVaultRequest;
  static deserializeBinaryFromReader(message: CanAssignAuthorizationsToVaultRequest, reader: jspb.BinaryReader): CanAssignAuthorizationsToVaultRequest;
}

export namespace CanAssignAuthorizationsToVaultRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableVaultIdsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableVaultIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableVaultIdsRequest): GetAssignableVaultIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableVaultIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableVaultIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableVaultIdsRequest, reader: jspb.BinaryReader): GetAssignableVaultIdsRequest;
}

export namespace GetAssignableVaultIdsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableVaultIdsForAuthorizationRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableVaultIdsForAuthorizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableVaultIdsForAuthorizationRequest): GetAssignableVaultIdsForAuthorizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableVaultIdsForAuthorizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableVaultIdsForAuthorizationRequest;
  static deserializeBinaryFromReader(message: GetAssignableVaultIdsForAuthorizationRequest, reader: jspb.BinaryReader): GetAssignableVaultIdsForAuthorizationRequest;
}

export namespace GetAssignableVaultIdsForAuthorizationRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAuthorizationToVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAuthorizationToVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAuthorizationToVaultReply): AssignAuthorizationToVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAuthorizationToVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAuthorizationToVaultReply;
  static deserializeBinaryFromReader(message: AssignAuthorizationToVaultReply, reader: jspb.BinaryReader): AssignAuthorizationToVaultReply;
}

export namespace AssignAuthorizationToVaultReply {
  export type AsObject = {
  }
}

export class AssignAuthorizationToVaultRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAuthorizationToVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAuthorizationToVaultRequest): AssignAuthorizationToVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAuthorizationToVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAuthorizationToVaultRequest;
  static deserializeBinaryFromReader(message: AssignAuthorizationToVaultRequest, reader: jspb.BinaryReader): AssignAuthorizationToVaultRequest;
}

export namespace AssignAuthorizationToVaultRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAuthorizationFromVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAuthorizationFromVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAuthorizationFromVaultReply): UnassignAuthorizationFromVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAuthorizationFromVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAuthorizationFromVaultReply;
  static deserializeBinaryFromReader(message: UnassignAuthorizationFromVaultReply, reader: jspb.BinaryReader): UnassignAuthorizationFromVaultReply;
}

export namespace UnassignAuthorizationFromVaultReply {
  export type AsObject = {
  }
}

export class UnassignAuthorizationFromVaultRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAuthorizationFromVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAuthorizationFromVaultRequest): UnassignAuthorizationFromVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAuthorizationFromVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAuthorizationFromVaultRequest;
  static deserializeBinaryFromReader(message: UnassignAuthorizationFromVaultRequest, reader: jspb.BinaryReader): UnassignAuthorizationFromVaultRequest;
}

export namespace UnassignAuthorizationFromVaultRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignAuthorizationToVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAuthorizationToVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAuthorizationToVaultReply): ReassignAuthorizationToVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAuthorizationToVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAuthorizationToVaultReply;
  static deserializeBinaryFromReader(message: ReassignAuthorizationToVaultReply, reader: jspb.BinaryReader): ReassignAuthorizationToVaultReply;
}

export namespace ReassignAuthorizationToVaultReply {
  export type AsObject = {
  }
}

export class ReassignAuthorizationToVaultRequest extends jspb.Message {
  hasAuthorizationId(): boolean;
  clearAuthorizationId(): void;
  getAuthorizationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAuthorizationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromVaultId(): boolean;
  clearFromVaultId(): void;
  getFromVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToVaultId(): boolean;
  clearToVaultId(): void;
  getToVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAuthorizationToVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAuthorizationToVaultRequest): ReassignAuthorizationToVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAuthorizationToVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAuthorizationToVaultRequest;
  static deserializeBinaryFromReader(message: ReassignAuthorizationToVaultRequest, reader: jspb.BinaryReader): ReassignAuthorizationToVaultRequest;
}

export namespace ReassignAuthorizationToVaultRequest {
  export type AsObject = {
    authorizationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromVaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toVaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupVaultsReply extends jspb.Message {
  getCanLookupVaults(): boolean;
  setCanLookupVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupVaultsReply): CanLookupVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupVaultsReply;
  static deserializeBinaryFromReader(message: CanLookupVaultsReply, reader: jspb.BinaryReader): CanLookupVaultsReply;
}

export namespace CanLookupVaultsReply {
  export type AsObject = {
    canLookupVaults: boolean,
  }
}

export class CanLookupVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupVaultsRequest): CanLookupVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupVaultsRequest;
  static deserializeBinaryFromReader(message: CanLookupVaultsRequest, reader: jspb.BinaryReader): CanLookupVaultsRequest;
}

export namespace CanLookupVaultsRequest {
  export type AsObject = {
  }
}

export class GetVaultsByIdsRequest extends jspb.Message {
  clearVaultIdsList(): void;
  getVaultIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setVaultIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addVaultIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsByIdsRequest): GetVaultsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsByIdsRequest;
  static deserializeBinaryFromReader(message: GetVaultsByIdsRequest, reader: jspb.BinaryReader): GetVaultsByIdsRequest;
}

export namespace GetVaultsByIdsRequest {
  export type AsObject = {
    vaultIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetVaultsByGenusTypeRequest extends jspb.Message {
  hasVaultGenusType(): boolean;
  clearVaultGenusType(): void;
  getVaultGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setVaultGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsByGenusTypeRequest): GetVaultsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetVaultsByGenusTypeRequest, reader: jspb.BinaryReader): GetVaultsByGenusTypeRequest;
}

export namespace GetVaultsByGenusTypeRequest {
  export type AsObject = {
    vaultGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetVaultsByParentGenusTypeRequest extends jspb.Message {
  hasVaultGenusType(): boolean;
  clearVaultGenusType(): void;
  getVaultGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setVaultGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsByParentGenusTypeRequest): GetVaultsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetVaultsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetVaultsByParentGenusTypeRequest;
}

export namespace GetVaultsByParentGenusTypeRequest {
  export type AsObject = {
    vaultGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetVaultsByRecordTypeRequest extends jspb.Message {
  hasVaultRecordType(): boolean;
  clearVaultRecordType(): void;
  getVaultRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setVaultRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsByRecordTypeRequest): GetVaultsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetVaultsByRecordTypeRequest, reader: jspb.BinaryReader): GetVaultsByRecordTypeRequest;
}

export namespace GetVaultsByRecordTypeRequest {
  export type AsObject = {
    vaultRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetVaultsByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsByProviderRequest): GetVaultsByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsByProviderRequest;
  static deserializeBinaryFromReader(message: GetVaultsByProviderRequest, reader: jspb.BinaryReader): GetVaultsByProviderRequest;
}

export namespace GetVaultsByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsRequest): GetVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsRequest;
  static deserializeBinaryFromReader(message: GetVaultsRequest, reader: jspb.BinaryReader): GetVaultsRequest;
}

export namespace GetVaultsRequest {
  export type AsObject = {
  }
}

export class CanSearchVaultsReply extends jspb.Message {
  getCanSearchVaults(): boolean;
  setCanSearchVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchVaultsReply): CanSearchVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchVaultsReply;
  static deserializeBinaryFromReader(message: CanSearchVaultsReply, reader: jspb.BinaryReader): CanSearchVaultsReply;
}

export namespace CanSearchVaultsReply {
  export type AsObject = {
    canSearchVaults: boolean,
  }
}

export class CanSearchVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchVaultsRequest): CanSearchVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchVaultsRequest;
  static deserializeBinaryFromReader(message: CanSearchVaultsRequest, reader: jspb.BinaryReader): CanSearchVaultsRequest;
}

export namespace CanSearchVaultsRequest {
  export type AsObject = {
  }
}

export class GetVaultQueryReply extends jspb.Message {
  hasVaultQuery(): boolean;
  clearVaultQuery(): void;
  getVaultQuery(): VaultQuery | undefined;
  setVaultQuery(value?: VaultQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultQueryReply): GetVaultQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultQueryReply;
  static deserializeBinaryFromReader(message: GetVaultQueryReply, reader: jspb.BinaryReader): GetVaultQueryReply;
}

export namespace GetVaultQueryReply {
  export type AsObject = {
    vaultQuery?: VaultQuery.AsObject,
  }
}

export class GetVaultQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultQueryRequest): GetVaultQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultQueryRequest;
  static deserializeBinaryFromReader(message: GetVaultQueryRequest, reader: jspb.BinaryReader): GetVaultQueryRequest;
}

export namespace GetVaultQueryRequest {
  export type AsObject = {
  }
}

export class GetVaultsByQueryRequest extends jspb.Message {
  hasVaultQuery(): boolean;
  clearVaultQuery(): void;
  getVaultQuery(): VaultQuery | undefined;
  setVaultQuery(value?: VaultQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultsByQueryRequest): GetVaultsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultsByQueryRequest;
  static deserializeBinaryFromReader(message: GetVaultsByQueryRequest, reader: jspb.BinaryReader): GetVaultsByQueryRequest;
}

export namespace GetVaultsByQueryRequest {
  export type AsObject = {
    vaultQuery?: VaultQuery.AsObject,
  }
}

export class CanCreateVaultsReply extends jspb.Message {
  getCanCreateVaults(): boolean;
  setCanCreateVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateVaultsReply): CanCreateVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateVaultsReply;
  static deserializeBinaryFromReader(message: CanCreateVaultsReply, reader: jspb.BinaryReader): CanCreateVaultsReply;
}

export namespace CanCreateVaultsReply {
  export type AsObject = {
    canCreateVaults: boolean,
  }
}

export class CanCreateVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateVaultsRequest): CanCreateVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateVaultsRequest;
  static deserializeBinaryFromReader(message: CanCreateVaultsRequest, reader: jspb.BinaryReader): CanCreateVaultsRequest;
}

export namespace CanCreateVaultsRequest {
  export type AsObject = {
  }
}

export class CanCreateVaultWithRecordTypesReply extends jspb.Message {
  getCanCreateVaultWithRecordTypes(): boolean;
  setCanCreateVaultWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateVaultWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateVaultWithRecordTypesReply): CanCreateVaultWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateVaultWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateVaultWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateVaultWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateVaultWithRecordTypesReply;
}

export namespace CanCreateVaultWithRecordTypesReply {
  export type AsObject = {
    canCreateVaultWithRecordTypes: boolean,
  }
}

export class CanCreateVaultWithRecordTypesRequest extends jspb.Message {
  clearVaultRecordTypesList(): void;
  getVaultRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setVaultRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addVaultRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateVaultWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateVaultWithRecordTypesRequest): CanCreateVaultWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateVaultWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateVaultWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateVaultWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateVaultWithRecordTypesRequest;
}

export namespace CanCreateVaultWithRecordTypesRequest {
  export type AsObject = {
    vaultRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetVaultFormForCreateReply extends jspb.Message {
  hasVaultForm(): boolean;
  clearVaultForm(): void;
  getVaultForm(): VaultForm | undefined;
  setVaultForm(value?: VaultForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultFormForCreateReply): GetVaultFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultFormForCreateReply;
  static deserializeBinaryFromReader(message: GetVaultFormForCreateReply, reader: jspb.BinaryReader): GetVaultFormForCreateReply;
}

export namespace GetVaultFormForCreateReply {
  export type AsObject = {
    vaultForm?: VaultForm.AsObject,
  }
}

export class GetVaultFormForCreateRequest extends jspb.Message {
  clearVaultRecordTypesList(): void;
  getVaultRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setVaultRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addVaultRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultFormForCreateRequest): GetVaultFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetVaultFormForCreateRequest, reader: jspb.BinaryReader): GetVaultFormForCreateRequest;
}

export namespace GetVaultFormForCreateRequest {
  export type AsObject = {
    vaultRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateVaultReply extends jspb.Message {
  hasVault(): boolean;
  clearVault(): void;
  getVault(): Vault | undefined;
  setVault(value?: Vault): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateVaultReply): CreateVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateVaultReply;
  static deserializeBinaryFromReader(message: CreateVaultReply, reader: jspb.BinaryReader): CreateVaultReply;
}

export namespace CreateVaultReply {
  export type AsObject = {
    vault?: Vault.AsObject,
  }
}

export class CreateVaultRequest extends jspb.Message {
  hasVaultForm(): boolean;
  clearVaultForm(): void;
  getVaultForm(): VaultForm | undefined;
  setVaultForm(value?: VaultForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateVaultRequest): CreateVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateVaultRequest;
  static deserializeBinaryFromReader(message: CreateVaultRequest, reader: jspb.BinaryReader): CreateVaultRequest;
}

export namespace CreateVaultRequest {
  export type AsObject = {
    vaultForm?: VaultForm.AsObject,
  }
}

export class CanUpdateVaultsReply extends jspb.Message {
  getCanUpdateVaults(): boolean;
  setCanUpdateVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateVaultsReply): CanUpdateVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateVaultsReply;
  static deserializeBinaryFromReader(message: CanUpdateVaultsReply, reader: jspb.BinaryReader): CanUpdateVaultsReply;
}

export namespace CanUpdateVaultsReply {
  export type AsObject = {
    canUpdateVaults: boolean,
  }
}

export class CanUpdateVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateVaultsRequest): CanUpdateVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateVaultsRequest;
  static deserializeBinaryFromReader(message: CanUpdateVaultsRequest, reader: jspb.BinaryReader): CanUpdateVaultsRequest;
}

export namespace CanUpdateVaultsRequest {
  export type AsObject = {
  }
}

export class GetVaultFormForUpdateReply extends jspb.Message {
  hasVaultForm(): boolean;
  clearVaultForm(): void;
  getVaultForm(): VaultForm | undefined;
  setVaultForm(value?: VaultForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultFormForUpdateReply): GetVaultFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetVaultFormForUpdateReply, reader: jspb.BinaryReader): GetVaultFormForUpdateReply;
}

export namespace GetVaultFormForUpdateReply {
  export type AsObject = {
    vaultForm?: VaultForm.AsObject,
  }
}

export class GetVaultFormForUpdateRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultFormForUpdateRequest): GetVaultFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetVaultFormForUpdateRequest, reader: jspb.BinaryReader): GetVaultFormForUpdateRequest;
}

export namespace GetVaultFormForUpdateRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateVaultReply): UpdateVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateVaultReply;
  static deserializeBinaryFromReader(message: UpdateVaultReply, reader: jspb.BinaryReader): UpdateVaultReply;
}

export namespace UpdateVaultReply {
  export type AsObject = {
  }
}

export class UpdateVaultRequest extends jspb.Message {
  hasVaultForm(): boolean;
  clearVaultForm(): void;
  getVaultForm(): VaultForm | undefined;
  setVaultForm(value?: VaultForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateVaultRequest): UpdateVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateVaultRequest;
  static deserializeBinaryFromReader(message: UpdateVaultRequest, reader: jspb.BinaryReader): UpdateVaultRequest;
}

export namespace UpdateVaultRequest {
  export type AsObject = {
    vaultForm?: VaultForm.AsObject,
  }
}

export class CanDeleteVaultsReply extends jspb.Message {
  getCanDeleteVaults(): boolean;
  setCanDeleteVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteVaultsReply): CanDeleteVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteVaultsReply;
  static deserializeBinaryFromReader(message: CanDeleteVaultsReply, reader: jspb.BinaryReader): CanDeleteVaultsReply;
}

export namespace CanDeleteVaultsReply {
  export type AsObject = {
    canDeleteVaults: boolean,
  }
}

export class CanDeleteVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteVaultsRequest): CanDeleteVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteVaultsRequest;
  static deserializeBinaryFromReader(message: CanDeleteVaultsRequest, reader: jspb.BinaryReader): CanDeleteVaultsRequest;
}

export namespace CanDeleteVaultsRequest {
  export type AsObject = {
  }
}

export class DeleteVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteVaultReply): DeleteVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteVaultReply;
  static deserializeBinaryFromReader(message: DeleteVaultReply, reader: jspb.BinaryReader): DeleteVaultReply;
}

export namespace DeleteVaultReply {
  export type AsObject = {
  }
}

export class DeleteVaultRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteVaultRequest): DeleteVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteVaultRequest;
  static deserializeBinaryFromReader(message: DeleteVaultRequest, reader: jspb.BinaryReader): DeleteVaultRequest;
}

export namespace DeleteVaultRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageVaultAliasesReply extends jspb.Message {
  getCanManageVaultAliases(): boolean;
  setCanManageVaultAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageVaultAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageVaultAliasesReply): CanManageVaultAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageVaultAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageVaultAliasesReply;
  static deserializeBinaryFromReader(message: CanManageVaultAliasesReply, reader: jspb.BinaryReader): CanManageVaultAliasesReply;
}

export namespace CanManageVaultAliasesReply {
  export type AsObject = {
    canManageVaultAliases: boolean,
  }
}

export class CanManageVaultAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageVaultAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageVaultAliasesRequest): CanManageVaultAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageVaultAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageVaultAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageVaultAliasesRequest, reader: jspb.BinaryReader): CanManageVaultAliasesRequest;
}

export namespace CanManageVaultAliasesRequest {
  export type AsObject = {
  }
}

export class AliasVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasVaultReply): AliasVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasVaultReply;
  static deserializeBinaryFromReader(message: AliasVaultReply, reader: jspb.BinaryReader): AliasVaultReply;
}

export namespace AliasVaultReply {
  export type AsObject = {
  }
}

export class AliasVaultRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasVaultRequest): AliasVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasVaultRequest;
  static deserializeBinaryFromReader(message: AliasVaultRequest, reader: jspb.BinaryReader): AliasVaultRequest;
}

export namespace AliasVaultRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultHierarchyIdReply): GetVaultHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetVaultHierarchyIdReply, reader: jspb.BinaryReader): GetVaultHierarchyIdReply;
}

export namespace GetVaultHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultHierarchyIdRequest): GetVaultHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetVaultHierarchyIdRequest, reader: jspb.BinaryReader): GetVaultHierarchyIdRequest;
}

export namespace GetVaultHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetVaultHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultHierarchyReply): GetVaultHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultHierarchyReply;
  static deserializeBinaryFromReader(message: GetVaultHierarchyReply, reader: jspb.BinaryReader): GetVaultHierarchyReply;
}

export namespace GetVaultHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetVaultHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultHierarchyRequest): GetVaultHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultHierarchyRequest;
  static deserializeBinaryFromReader(message: GetVaultHierarchyRequest, reader: jspb.BinaryReader): GetVaultHierarchyRequest;
}

export namespace GetVaultHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessVaultHierarchyReply extends jspb.Message {
  getCanAccessVaultHierarchy(): boolean;
  setCanAccessVaultHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessVaultHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessVaultHierarchyReply): CanAccessVaultHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessVaultHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessVaultHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessVaultHierarchyReply, reader: jspb.BinaryReader): CanAccessVaultHierarchyReply;
}

export namespace CanAccessVaultHierarchyReply {
  export type AsObject = {
    canAccessVaultHierarchy: boolean,
  }
}

export class CanAccessVaultHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessVaultHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessVaultHierarchyRequest): CanAccessVaultHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessVaultHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessVaultHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessVaultHierarchyRequest, reader: jspb.BinaryReader): CanAccessVaultHierarchyRequest;
}

export namespace CanAccessVaultHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootVaultIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootVaultIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootVaultIdsRequest): GetRootVaultIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootVaultIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootVaultIdsRequest;
  static deserializeBinaryFromReader(message: GetRootVaultIdsRequest, reader: jspb.BinaryReader): GetRootVaultIdsRequest;
}

export namespace GetRootVaultIdsRequest {
  export type AsObject = {
  }
}

export class GetRootVaultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootVaultsRequest): GetRootVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootVaultsRequest;
  static deserializeBinaryFromReader(message: GetRootVaultsRequest, reader: jspb.BinaryReader): GetRootVaultsRequest;
}

export namespace GetRootVaultsRequest {
  export type AsObject = {
  }
}

export class HasParentVaultsReply extends jspb.Message {
  getHasParentVaults(): boolean;
  setHasParentVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentVaultsReply): HasParentVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentVaultsReply;
  static deserializeBinaryFromReader(message: HasParentVaultsReply, reader: jspb.BinaryReader): HasParentVaultsReply;
}

export namespace HasParentVaultsReply {
  export type AsObject = {
    hasParentVaults: boolean,
  }
}

export class HasParentVaultsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentVaultsRequest): HasParentVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentVaultsRequest;
  static deserializeBinaryFromReader(message: HasParentVaultsRequest, reader: jspb.BinaryReader): HasParentVaultsRequest;
}

export namespace HasParentVaultsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfVaultReply extends jspb.Message {
  getIsParentOfVault(): boolean;
  setIsParentOfVault(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfVaultReply): IsParentOfVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfVaultReply;
  static deserializeBinaryFromReader(message: IsParentOfVaultReply, reader: jspb.BinaryReader): IsParentOfVaultReply;
}

export namespace IsParentOfVaultReply {
  export type AsObject = {
    isParentOfVault: boolean,
  }
}

export class IsParentOfVaultRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfVaultRequest): IsParentOfVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfVaultRequest;
  static deserializeBinaryFromReader(message: IsParentOfVaultRequest, reader: jspb.BinaryReader): IsParentOfVaultRequest;
}

export namespace IsParentOfVaultRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentVaultIdsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentVaultIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentVaultIdsRequest): GetParentVaultIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentVaultIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentVaultIdsRequest;
  static deserializeBinaryFromReader(message: GetParentVaultIdsRequest, reader: jspb.BinaryReader): GetParentVaultIdsRequest;
}

export namespace GetParentVaultIdsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentVaultsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentVaultsRequest): GetParentVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentVaultsRequest;
  static deserializeBinaryFromReader(message: GetParentVaultsRequest, reader: jspb.BinaryReader): GetParentVaultsRequest;
}

export namespace GetParentVaultsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfVaultReply extends jspb.Message {
  getIsAncestorOfVault(): boolean;
  setIsAncestorOfVault(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfVaultReply): IsAncestorOfVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfVaultReply;
  static deserializeBinaryFromReader(message: IsAncestorOfVaultReply, reader: jspb.BinaryReader): IsAncestorOfVaultReply;
}

export namespace IsAncestorOfVaultReply {
  export type AsObject = {
    isAncestorOfVault: boolean,
  }
}

export class IsAncestorOfVaultRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfVaultRequest): IsAncestorOfVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfVaultRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfVaultRequest, reader: jspb.BinaryReader): IsAncestorOfVaultRequest;
}

export namespace IsAncestorOfVaultRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildVaultsReply extends jspb.Message {
  getHasChildVaults(): boolean;
  setHasChildVaults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildVaultsReply): HasChildVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildVaultsReply;
  static deserializeBinaryFromReader(message: HasChildVaultsReply, reader: jspb.BinaryReader): HasChildVaultsReply;
}

export namespace HasChildVaultsReply {
  export type AsObject = {
    hasChildVaults: boolean,
  }
}

export class HasChildVaultsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildVaultsRequest): HasChildVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildVaultsRequest;
  static deserializeBinaryFromReader(message: HasChildVaultsRequest, reader: jspb.BinaryReader): HasChildVaultsRequest;
}

export namespace HasChildVaultsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfVaultReply extends jspb.Message {
  getIsChildOfVault(): boolean;
  setIsChildOfVault(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfVaultReply): IsChildOfVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfVaultReply;
  static deserializeBinaryFromReader(message: IsChildOfVaultReply, reader: jspb.BinaryReader): IsChildOfVaultReply;
}

export namespace IsChildOfVaultReply {
  export type AsObject = {
    isChildOfVault: boolean,
  }
}

export class IsChildOfVaultRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfVaultRequest): IsChildOfVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfVaultRequest;
  static deserializeBinaryFromReader(message: IsChildOfVaultRequest, reader: jspb.BinaryReader): IsChildOfVaultRequest;
}

export namespace IsChildOfVaultRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildVaultIdsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildVaultIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildVaultIdsRequest): GetChildVaultIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildVaultIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildVaultIdsRequest;
  static deserializeBinaryFromReader(message: GetChildVaultIdsRequest, reader: jspb.BinaryReader): GetChildVaultIdsRequest;
}

export namespace GetChildVaultIdsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildVaultsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildVaultsRequest): GetChildVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildVaultsRequest;
  static deserializeBinaryFromReader(message: GetChildVaultsRequest, reader: jspb.BinaryReader): GetChildVaultsRequest;
}

export namespace GetChildVaultsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfVaultReply extends jspb.Message {
  getIsDescendantOfVault(): boolean;
  setIsDescendantOfVault(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfVaultReply): IsDescendantOfVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfVaultReply;
  static deserializeBinaryFromReader(message: IsDescendantOfVaultReply, reader: jspb.BinaryReader): IsDescendantOfVaultReply;
}

export namespace IsDescendantOfVaultReply {
  export type AsObject = {
    isDescendantOfVault: boolean,
  }
}

export class IsDescendantOfVaultRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfVaultRequest): IsDescendantOfVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfVaultRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfVaultRequest, reader: jspb.BinaryReader): IsDescendantOfVaultRequest;
}

export namespace IsDescendantOfVaultRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultNodeIdsReply): GetVaultNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultNodeIdsReply;
  static deserializeBinaryFromReader(message: GetVaultNodeIdsReply, reader: jspb.BinaryReader): GetVaultNodeIdsReply;
}

export namespace GetVaultNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetVaultNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultNodeIdsRequest): GetVaultNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetVaultNodeIdsRequest, reader: jspb.BinaryReader): GetVaultNodeIdsRequest;
}

export namespace GetVaultNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetVaultNodesReply extends jspb.Message {
  hasVaultNode(): boolean;
  clearVaultNode(): void;
  getVaultNode(): VaultNode | undefined;
  setVaultNode(value?: VaultNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultNodesReply): GetVaultNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultNodesReply;
  static deserializeBinaryFromReader(message: GetVaultNodesReply, reader: jspb.BinaryReader): GetVaultNodesReply;
}

export namespace GetVaultNodesReply {
  export type AsObject = {
    vaultNode?: VaultNode.AsObject,
  }
}

export class GetVaultNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetVaultNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetVaultNodesRequest): GetVaultNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetVaultNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetVaultNodesRequest;
  static deserializeBinaryFromReader(message: GetVaultNodesRequest, reader: jspb.BinaryReader): GetVaultNodesRequest;
}

export namespace GetVaultNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanModifyVaultHierarchyReply extends jspb.Message {
  getCanModifyVaultHierarchy(): boolean;
  setCanModifyVaultHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyVaultHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyVaultHierarchyReply): CanModifyVaultHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyVaultHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyVaultHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyVaultHierarchyReply, reader: jspb.BinaryReader): CanModifyVaultHierarchyReply;
}

export namespace CanModifyVaultHierarchyReply {
  export type AsObject = {
    canModifyVaultHierarchy: boolean,
  }
}

export class CanModifyVaultHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyVaultHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyVaultHierarchyRequest): CanModifyVaultHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyVaultHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyVaultHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyVaultHierarchyRequest, reader: jspb.BinaryReader): CanModifyVaultHierarchyRequest;
}

export namespace CanModifyVaultHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootVaultReply): AddRootVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootVaultReply;
  static deserializeBinaryFromReader(message: AddRootVaultReply, reader: jspb.BinaryReader): AddRootVaultReply;
}

export namespace AddRootVaultReply {
  export type AsObject = {
  }
}

export class AddRootVaultRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootVaultRequest): AddRootVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootVaultRequest;
  static deserializeBinaryFromReader(message: AddRootVaultRequest, reader: jspb.BinaryReader): AddRootVaultRequest;
}

export namespace AddRootVaultRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootVaultReply): RemoveRootVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootVaultReply;
  static deserializeBinaryFromReader(message: RemoveRootVaultReply, reader: jspb.BinaryReader): RemoveRootVaultReply;
}

export namespace RemoveRootVaultReply {
  export type AsObject = {
  }
}

export class RemoveRootVaultRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootVaultRequest): RemoveRootVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootVaultRequest;
  static deserializeBinaryFromReader(message: RemoveRootVaultRequest, reader: jspb.BinaryReader): RemoveRootVaultRequest;
}

export namespace RemoveRootVaultRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildVaultReply): AddChildVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildVaultReply;
  static deserializeBinaryFromReader(message: AddChildVaultReply, reader: jspb.BinaryReader): AddChildVaultReply;
}

export namespace AddChildVaultReply {
  export type AsObject = {
  }
}

export class AddChildVaultRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildVaultRequest): AddChildVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildVaultRequest;
  static deserializeBinaryFromReader(message: AddChildVaultRequest, reader: jspb.BinaryReader): AddChildVaultRequest;
}

export namespace AddChildVaultRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildVaultReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildVaultReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildVaultReply): RemoveChildVaultReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildVaultReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildVaultReply;
  static deserializeBinaryFromReader(message: RemoveChildVaultReply, reader: jspb.BinaryReader): RemoveChildVaultReply;
}

export namespace RemoveChildVaultReply {
  export type AsObject = {
  }
}

export class RemoveChildVaultRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildVaultRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildVaultRequest): RemoveChildVaultRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildVaultRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildVaultRequest;
  static deserializeBinaryFromReader(message: RemoveChildVaultRequest, reader: jspb.BinaryReader): RemoveChildVaultRequest;
}

export namespace RemoveChildVaultRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildVaultsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildVaultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildVaultsReply): RemoveChildVaultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildVaultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildVaultsReply;
  static deserializeBinaryFromReader(message: RemoveChildVaultsReply, reader: jspb.BinaryReader): RemoveChildVaultsReply;
}

export namespace RemoveChildVaultsReply {
  export type AsObject = {
  }
}

export class RemoveChildVaultsRequest extends jspb.Message {
  hasVaultId(): boolean;
  clearVaultId(): void;
  getVaultId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setVaultId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildVaultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildVaultsRequest): RemoveChildVaultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildVaultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildVaultsRequest;
  static deserializeBinaryFromReader(message: RemoveChildVaultsRequest, reader: jspb.BinaryReader): RemoveChildVaultsRequest;
}

export namespace RemoveChildVaultsRequest {
  export type AsObject = {
    vaultId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

