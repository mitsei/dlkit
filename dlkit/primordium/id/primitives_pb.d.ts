// package: dlkit.primordium.id.primitives
// file: dlkit/primordium/id/primitives.proto

import * as jspb from "google-protobuf";

export class Id extends jspb.Message {
  getNamespace(): string;
  setNamespace(value: string): void;

  getIdentifier(): string;
  setIdentifier(value: string): void;

  getAuthority(): string;
  setAuthority(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Id.AsObject;
  static toObject(includeInstance: boolean, msg: Id): Id.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Id, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Id;
  static deserializeBinaryFromReader(message: Id, reader: jspb.BinaryReader): Id;
}

export namespace Id {
  export type AsObject = {
    namespace: string,
    identifier: string,
    authority: string,
  }
}

