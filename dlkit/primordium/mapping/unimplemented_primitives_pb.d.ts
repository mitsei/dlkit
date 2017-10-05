// package: dlkit.primordium.mapping.unimplemented_primitives
// file: dlkit/primordium/mapping/unimplemented_primitives.proto

import * as jspb from "google-protobuf";

export class Distance extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Distance.AsObject;
  static toObject(includeInstance: boolean, msg: Distance): Distance.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Distance, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Distance;
  static deserializeBinaryFromReader(message: Distance, reader: jspb.BinaryReader): Distance;
}

export namespace Distance {
  export type AsObject = {
  }
}

export class Location extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Location.AsObject;
  static toObject(includeInstance: boolean, msg: Location): Location.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Location, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Location;
  static deserializeBinaryFromReader(message: Location, reader: jspb.BinaryReader): Location;
}

export namespace Location {
  export type AsObject = {
  }
}

export class Speed extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Speed.AsObject;
  static toObject(includeInstance: boolean, msg: Speed): Speed.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Speed, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Speed;
  static deserializeBinaryFromReader(message: Speed, reader: jspb.BinaryReader): Speed;
}

export namespace Speed {
  export type AsObject = {
  }
}

