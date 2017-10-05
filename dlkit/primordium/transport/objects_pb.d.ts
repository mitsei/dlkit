// package: dlkit.primordium.transport.objects
// file: dlkit/primordium/transport/objects.proto

import * as jspb from "google-protobuf";

export class DataInputStream extends jspb.Message {
  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): void;

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
    data: Uint8Array | string,
  }
}

