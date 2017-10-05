// package: dlkit.primordium.installation.primitives
// file: dlkit/primordium/installation/primitives.proto

import * as jspb from "google-protobuf";

export class Version extends jspb.Message {
  getScheme(): string;
  setScheme(value: string): void;

  clearComponentsList(): void;
  getComponentsList(): Array<number>;
  setComponentsList(value: Array<number>): void;
  addComponents(value: number, index?: number): number;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Version.AsObject;
  static toObject(includeInstance: boolean, msg: Version): Version.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Version, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Version;
  static deserializeBinaryFromReader(message: Version, reader: jspb.BinaryReader): Version;
}

export namespace Version {
  export type AsObject = {
    scheme: string,
    componentsList: Array<number>,
  }
}

