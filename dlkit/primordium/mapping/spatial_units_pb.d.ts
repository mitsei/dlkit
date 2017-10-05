// package: dlkit.primordium.mapping.spatial_units
// file: dlkit/primordium/mapping/spatial_units.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_mapping_coordinate_primitives_pb from "../../../dlkit/primordium/mapping/coordinate_primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../../dlkit/primordium/type/primitives_pb";

export class SpatialUnit extends jspb.Message {
  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  getType(): string;
  setType(value: string): void;

  hasCoordinate(): boolean;
  clearCoordinate(): void;
  getCoordinate(): dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate | undefined;
  setCoordinate(value?: dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate): void;

  getWidth(): number;
  setWidth(value: number): void;

  getHeight(): number;
  setHeight(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SpatialUnit.AsObject;
  static toObject(includeInstance: boolean, msg: SpatialUnit): SpatialUnit.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SpatialUnit, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SpatialUnit;
  static deserializeBinaryFromReader(message: SpatialUnit, reader: jspb.BinaryReader): SpatialUnit;
}

export namespace SpatialUnit {
  export type AsObject = {
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    type: string,
    coordinate?: dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate.AsObject,
    width: number,
    height: number,
  }
}

