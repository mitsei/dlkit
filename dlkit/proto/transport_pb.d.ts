// package: dlkit.proto.transport
// file: dlkit/proto/transport.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";

export class Endpoint extends jspb.Message {
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
  toObject(includeInstance?: boolean): Endpoint.AsObject;
  static toObject(includeInstance: boolean, msg: Endpoint): Endpoint.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Endpoint, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Endpoint;
  static deserializeBinaryFromReader(message: Endpoint, reader: jspb.BinaryReader): Endpoint;
}

export namespace Endpoint {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class EndpointList extends jspb.Message {
  clearEndpointsList(): void;
  getEndpointsList(): Array<Endpoint>;
  setEndpointsList(value: Array<Endpoint>): void;
  addEndpoints(value?: Endpoint, index?: number): Endpoint;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EndpointList.AsObject;
  static toObject(includeInstance: boolean, msg: EndpointList): EndpointList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EndpointList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EndpointList;
  static deserializeBinaryFromReader(message: EndpointList, reader: jspb.BinaryReader): EndpointList;
}

export namespace EndpointList {
  export type AsObject = {
    endpointsList: Array<Endpoint.AsObject>,
  }
}

export class Request extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Request.AsObject;
  static toObject(includeInstance: boolean, msg: Request): Request.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Request, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Request;
  static deserializeBinaryFromReader(message: Request, reader: jspb.BinaryReader): Request;
}

export namespace Request {
  export type AsObject = {
  }
}

export class Response extends jspb.Message {
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
  toObject(includeInstance?: boolean): Response.AsObject;
  static toObject(includeInstance: boolean, msg: Response): Response.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Response, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Response;
  static deserializeBinaryFromReader(message: Response, reader: jspb.BinaryReader): Response;
}

export namespace Response {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class DataInputStream extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DataInputStream.AsObject;
  static toObject(includeInstance: boolean, msg: DataInputStream): DataInputStream.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DataInputStream, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DataInputStream;
  static deserializeBinaryFromReader(message: DataInputStream, reader: jspb.BinaryReader): DataInputStream;
}

export namespace DataInputStream {
  export type AsObject = {
  }
}

export class DataOutputStream extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DataOutputStream.AsObject;
  static toObject(includeInstance: boolean, msg: DataOutputStream): DataOutputStream.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DataOutputStream, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DataOutputStream;
  static deserializeBinaryFromReader(message: DataOutputStream, reader: jspb.BinaryReader): DataOutputStream;
}

export namespace DataOutputStream {
  export type AsObject = {
  }
}

