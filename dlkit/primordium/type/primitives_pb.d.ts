// package: dlkit.primordium.type.primitives
// file: dlkit/primordium/type/primitives.proto

import * as jspb from "google-protobuf";

export class Type extends jspb.Message {
  getAuthority(): string;
  setAuthority(value: string): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): DisplayText | undefined;
  setDescription(value?: DisplayText): void;

  hasDisplayLabel(): boolean;
  clearDisplayLabel(): void;
  getDisplayLabel(): DisplayText | undefined;
  setDisplayLabel(value?: DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): DisplayText | undefined;
  setDisplayName(value?: DisplayText): void;

  getDomain(): string;
  setDomain(value: string): void;

  getIdentifier(): string;
  setIdentifier(value: string): void;

  getNamespace(): string;
  setNamespace(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Type.AsObject;
  static toObject(includeInstance: boolean, msg: Type): Type.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Type, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Type;
  static deserializeBinaryFromReader(message: Type, reader: jspb.BinaryReader): Type;
}

export namespace Type {
  export type AsObject = {
    authority: string,
    description?: DisplayText.AsObject,
    displayLabel?: DisplayText.AsObject,
    displayName?: DisplayText.AsObject,
    domain: string,
    identifier: string,
    namespace: string,
  }
}

export class DisplayText extends jspb.Message {
  getText(): string;
  setText(value: string): void;

  hasFormatTypeId(): boolean;
  clearFormatTypeId(): void;
  getFormatTypeId(): Type | undefined;
  setFormatTypeId(value?: Type): void;

  hasLanguageTypeId(): boolean;
  clearLanguageTypeId(): void;
  getLanguageTypeId(): Type | undefined;
  setLanguageTypeId(value?: Type): void;

  hasScriptTypeId(): boolean;
  clearScriptTypeId(): void;
  getScriptTypeId(): Type | undefined;
  setScriptTypeId(value?: Type): void;

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
    formatTypeId?: Type.AsObject,
    languageTypeId?: Type.AsObject,
    scriptTypeId?: Type.AsObject,
  }
}

