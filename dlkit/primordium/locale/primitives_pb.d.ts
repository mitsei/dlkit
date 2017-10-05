// package: dlkit.primordium.locale.primitives
// file: dlkit/primordium/locale/primitives.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_type_primitives_pb from "../../../dlkit/primordium/type/primitives_pb";

export class DisplayText extends jspb.Message {
  getText(): string;
  setText(value: string): void;

  hasFormatTypeId(): boolean;
  clearFormatTypeId(): void;
  getFormatTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setFormatTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasLanguageTypeId(): boolean;
  clearLanguageTypeId(): void;
  getLanguageTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLanguageTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasScriptTypeId(): boolean;
  clearScriptTypeId(): void;
  getScriptTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setScriptTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DisplayText.AsObject;
  static toObject(includeInstance: boolean, msg: DisplayText): DisplayText.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DisplayText, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DisplayText;
  static deserializeBinaryFromReader(message: DisplayText, reader: jspb.BinaryReader): DisplayText;
}

export namespace DisplayText {
  export type AsObject = {
    text: string,
    formatTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    languageTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    scriptTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

