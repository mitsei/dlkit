// package: dlkit.primordium.mapping.coordinate_primitives
// file: dlkit/primordium/mapping/coordinate_primitives.proto

import * as jspb from "google-protobuf";

export class Coordinate extends jspb.Message {
  clearValuesList(): void;
  getValuesList(): Array<number>;
  setValuesList(value: Array<number>): void;
  addValues(value: number, index?: number): number;

  getUncertaintyMinus(): number;
  setUncertaintyMinus(value: number): void;

  getUncertaintyPlus(): number;
  setUncertaintyPlus(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Coordinate.AsObject;
  static toObject(includeInstance: boolean, msg: Coordinate): Coordinate.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Coordinate, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Coordinate;
  static deserializeBinaryFromReader(message: Coordinate, reader: jspb.BinaryReader): Coordinate;
}

export namespace Coordinate {
  export type AsObject = {
    valuesList: Array<number>,
    uncertaintyMinus: number,
    uncertaintyPlus: number,
  }
}

