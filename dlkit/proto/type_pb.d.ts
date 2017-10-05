// package: dlkit.proto.type
// file: dlkit/proto/type.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";

export class TypeForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TypeForm.AsObject;
  static toObject(includeInstance: boolean, msg: TypeForm): TypeForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TypeForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TypeForm;
  static deserializeBinaryFromReader(message: TypeForm, reader: jspb.BinaryReader): TypeForm;
}

export namespace TypeForm {
  export type AsObject = {
  }
}

export class TypeList extends jspb.Message {
  clearTypesList(): void;
  getTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TypeList.AsObject;
  static toObject(includeInstance: boolean, msg: TypeList): TypeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TypeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TypeList;
  static deserializeBinaryFromReader(message: TypeList, reader: jspb.BinaryReader): TypeList;
}

export namespace TypeList {
  export type AsObject = {
    typesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

