// package: dlkit.proto.id
// file: dlkit/proto/id.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";

export class IdForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IdForm.AsObject;
  static toObject(includeInstance: boolean, msg: IdForm): IdForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IdForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IdForm;
  static deserializeBinaryFromReader(message: IdForm, reader: jspb.BinaryReader): IdForm;
}

export namespace IdForm {
  export type AsObject = {
  }
}

export class IdList extends jspb.Message {
  clearIdsList(): void;
  getIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IdList.AsObject;
  static toObject(includeInstance: boolean, msg: IdList): IdList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IdList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IdList;
  static deserializeBinaryFromReader(message: IdList, reader: jspb.BinaryReader): IdList;
}

export namespace IdList {
  export type AsObject = {
    idsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

