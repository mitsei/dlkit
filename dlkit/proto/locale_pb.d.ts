// package: dlkit.proto.locale
// file: dlkit/proto/locale.proto

import * as jspb from "google-protobuf";

export class CalendarInfo extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarInfo.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarInfo): CalendarInfo.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarInfo;
  static deserializeBinaryFromReader(message: CalendarInfo, reader: jspb.BinaryReader): CalendarInfo;
}

export namespace CalendarInfo {
  export type AsObject = {
  }
}

export class TimeInfo extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimeInfo.AsObject;
  static toObject(includeInstance: boolean, msg: TimeInfo): TimeInfo.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimeInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimeInfo;
  static deserializeBinaryFromReader(message: TimeInfo, reader: jspb.BinaryReader): TimeInfo;
}

export namespace TimeInfo {
  export type AsObject = {
  }
}

export class CalendarUnit extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarUnit.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarUnit): CalendarUnit.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarUnit, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarUnit;
  static deserializeBinaryFromReader(message: CalendarUnit, reader: jspb.BinaryReader): CalendarUnit;
}

export namespace CalendarUnit {
  export type AsObject = {
  }
}

export class Locale extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Locale.AsObject;
  static toObject(includeInstance: boolean, msg: Locale): Locale.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Locale, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Locale;
  static deserializeBinaryFromReader(message: Locale, reader: jspb.BinaryReader): Locale;
}

export namespace Locale {
  export type AsObject = {
  }
}

export class LocaleList extends jspb.Message {
  clearLocalesList(): void;
  getLocalesList(): Array<Locale>;
  setLocalesList(value: Array<Locale>): void;
  addLocales(value?: Locale, index?: number): Locale;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocaleList.AsObject;
  static toObject(includeInstance: boolean, msg: LocaleList): LocaleList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocaleList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocaleList;
  static deserializeBinaryFromReader(message: LocaleList, reader: jspb.BinaryReader): LocaleList;
}

export namespace LocaleList {
  export type AsObject = {
    localesList: Array<Locale.AsObject>,
  }
}

