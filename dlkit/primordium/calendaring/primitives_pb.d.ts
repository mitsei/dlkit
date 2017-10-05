// package: dlkit.primordium.calendaring.primitives
// file: dlkit/primordium/calendaring/primitives.proto

import * as jspb from "google-protobuf";

export class DateTimeInterval extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DateTimeInterval.AsObject;
  static toObject(includeInstance: boolean, msg: DateTimeInterval): DateTimeInterval.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DateTimeInterval, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DateTimeInterval;
  static deserializeBinaryFromReader(message: DateTimeInterval, reader: jspb.BinaryReader): DateTimeInterval;
}

export namespace DateTimeInterval {
  export type AsObject = {
  }
}

export class Duration extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Duration.AsObject;
  static toObject(includeInstance: boolean, msg: Duration): Duration.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Duration, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Duration;
  static deserializeBinaryFromReader(message: Duration, reader: jspb.BinaryReader): Duration;
}

export namespace Duration {
  export type AsObject = {
  }
}

export class Time extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Time.AsObject;
  static toObject(includeInstance: boolean, msg: Time): Time.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Time, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Time;
  static deserializeBinaryFromReader(message: Time, reader: jspb.BinaryReader): Time;
}

export namespace Time {
  export type AsObject = {
  }
}

