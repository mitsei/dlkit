// package: dlkit.proto.mapping
// file: dlkit/proto/mapping.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_mapping_coordinate_primitives_pb from "../../dlkit/primordium/mapping/coordinate_primitives_pb";
import * as dlkit_primordium_mapping_spatial_units_pb from "../../dlkit/primordium/mapping/spatial_units_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";

export class Location extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasMap(): boolean;
  clearMap(): void;
  getMap(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setMap(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasSpatialUnit(): boolean;
  clearSpatialUnit(): void;
  getSpatialUnit(): dlkit_primordium_mapping_spatial_units_pb.SpatialUnit | undefined;
  setSpatialUnit(value?: dlkit_primordium_mapping_spatial_units_pb.SpatialUnit): void;

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
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    map?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    spatialUnit?: dlkit_primordium_mapping_spatial_units_pb.SpatialUnit.AsObject,
  }
}

export class LocationQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationQuery.AsObject;
  static toObject(includeInstance: boolean, msg: LocationQuery): LocationQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationQuery;
  static deserializeBinaryFromReader(message: LocationQuery, reader: jspb.BinaryReader): LocationQuery;
}

export namespace LocationQuery {
  export type AsObject = {
  }
}

export class LocationQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: LocationQueryInspector): LocationQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationQueryInspector;
  static deserializeBinaryFromReader(message: LocationQueryInspector, reader: jspb.BinaryReader): LocationQueryInspector;
}

export namespace LocationQueryInspector {
  export type AsObject = {
  }
}

export class LocationForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationForm.AsObject;
  static toObject(includeInstance: boolean, msg: LocationForm): LocationForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationForm;
  static deserializeBinaryFromReader(message: LocationForm, reader: jspb.BinaryReader): LocationForm;
}

export namespace LocationForm {
  export type AsObject = {
  }
}

export class LocationSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: LocationSearchOrder): LocationSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationSearchOrder;
  static deserializeBinaryFromReader(message: LocationSearchOrder, reader: jspb.BinaryReader): LocationSearchOrder;
}

export namespace LocationSearchOrder {
  export type AsObject = {
  }
}

export class LocationSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationSearch.AsObject;
  static toObject(includeInstance: boolean, msg: LocationSearch): LocationSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationSearch;
  static deserializeBinaryFromReader(message: LocationSearch, reader: jspb.BinaryReader): LocationSearch;
}

export namespace LocationSearch {
  export type AsObject = {
  }
}

export class LocationSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: LocationSearchResults): LocationSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationSearchResults;
  static deserializeBinaryFromReader(message: LocationSearchResults, reader: jspb.BinaryReader): LocationSearchResults;
}

export namespace LocationSearchResults {
  export type AsObject = {
  }
}

export class LocationList extends jspb.Message {
  clearLocationsList(): void;
  getLocationsList(): Array<Location>;
  setLocationsList(value: Array<Location>): void;
  addLocations(value?: Location, index?: number): Location;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationList.AsObject;
  static toObject(includeInstance: boolean, msg: LocationList): LocationList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationList;
  static deserializeBinaryFromReader(message: LocationList, reader: jspb.BinaryReader): LocationList;
}

export namespace LocationList {
  export type AsObject = {
    locationsList: Array<Location.AsObject>,
  }
}

export class LocationNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationNode.AsObject;
  static toObject(includeInstance: boolean, msg: LocationNode): LocationNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationNode;
  static deserializeBinaryFromReader(message: LocationNode, reader: jspb.BinaryReader): LocationNode;
}

export namespace LocationNode {
  export type AsObject = {
  }
}

export class LocationNodeList extends jspb.Message {
  clearLocationNodesList(): void;
  getLocationNodesList(): Array<LocationNode>;
  setLocationNodesList(value: Array<LocationNode>): void;
  addLocationNodes(value?: LocationNode, index?: number): LocationNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocationNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: LocationNodeList): LocationNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LocationNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocationNodeList;
  static deserializeBinaryFromReader(message: LocationNodeList, reader: jspb.BinaryReader): LocationNodeList;
}

export namespace LocationNodeList {
  export type AsObject = {
    locationNodesList: Array<LocationNode.AsObject>,
  }
}

export class Map extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Map.AsObject;
  static toObject(includeInstance: boolean, msg: Map): Map.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Map, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Map;
  static deserializeBinaryFromReader(message: Map, reader: jspb.BinaryReader): Map;
}

export namespace Map {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class MapQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapQuery.AsObject;
  static toObject(includeInstance: boolean, msg: MapQuery): MapQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapQuery;
  static deserializeBinaryFromReader(message: MapQuery, reader: jspb.BinaryReader): MapQuery;
}

export namespace MapQuery {
  export type AsObject = {
  }
}

export class MapQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: MapQueryInspector): MapQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapQueryInspector;
  static deserializeBinaryFromReader(message: MapQueryInspector, reader: jspb.BinaryReader): MapQueryInspector;
}

export namespace MapQueryInspector {
  export type AsObject = {
  }
}

export class MapForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapForm.AsObject;
  static toObject(includeInstance: boolean, msg: MapForm): MapForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapForm;
  static deserializeBinaryFromReader(message: MapForm, reader: jspb.BinaryReader): MapForm;
}

export namespace MapForm {
  export type AsObject = {
  }
}

export class MapSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: MapSearchOrder): MapSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapSearchOrder;
  static deserializeBinaryFromReader(message: MapSearchOrder, reader: jspb.BinaryReader): MapSearchOrder;
}

export namespace MapSearchOrder {
  export type AsObject = {
  }
}

export class MapSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapSearch.AsObject;
  static toObject(includeInstance: boolean, msg: MapSearch): MapSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapSearch;
  static deserializeBinaryFromReader(message: MapSearch, reader: jspb.BinaryReader): MapSearch;
}

export namespace MapSearch {
  export type AsObject = {
  }
}

export class MapSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: MapSearchResults): MapSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapSearchResults;
  static deserializeBinaryFromReader(message: MapSearchResults, reader: jspb.BinaryReader): MapSearchResults;
}

export namespace MapSearchResults {
  export type AsObject = {
  }
}

export class MapList extends jspb.Message {
  clearMapsList(): void;
  getMapsList(): Array<Map>;
  setMapsList(value: Array<Map>): void;
  addMaps(value?: Map, index?: number): Map;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapList.AsObject;
  static toObject(includeInstance: boolean, msg: MapList): MapList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapList;
  static deserializeBinaryFromReader(message: MapList, reader: jspb.BinaryReader): MapList;
}

export namespace MapList {
  export type AsObject = {
    mapsList: Array<Map.AsObject>,
  }
}

export class MapNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapNode.AsObject;
  static toObject(includeInstance: boolean, msg: MapNode): MapNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapNode;
  static deserializeBinaryFromReader(message: MapNode, reader: jspb.BinaryReader): MapNode;
}

export namespace MapNode {
  export type AsObject = {
  }
}

export class MapNodeList extends jspb.Message {
  clearMapNodesList(): void;
  getMapNodesList(): Array<MapNode>;
  setMapNodesList(value: Array<MapNode>): void;
  addMapNodes(value?: MapNode, index?: number): MapNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MapNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: MapNodeList): MapNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MapNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MapNodeList;
  static deserializeBinaryFromReader(message: MapNodeList, reader: jspb.BinaryReader): MapNodeList;
}

export namespace MapNodeList {
  export type AsObject = {
    mapNodesList: Array<MapNode.AsObject>,
  }
}

export class ResourceLocation extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceLocation.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceLocation): ResourceLocation.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceLocation, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceLocation;
  static deserializeBinaryFromReader(message: ResourceLocation, reader: jspb.BinaryReader): ResourceLocation;
}

export namespace ResourceLocation {
  export type AsObject = {
  }
}

export class ResourceLocationList extends jspb.Message {
  clearResourceLocationsList(): void;
  getResourceLocationsList(): Array<ResourceLocation>;
  setResourceLocationsList(value: Array<ResourceLocation>): void;
  addResourceLocations(value?: ResourceLocation, index?: number): ResourceLocation;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResourceLocationList.AsObject;
  static toObject(includeInstance: boolean, msg: ResourceLocationList): ResourceLocationList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResourceLocationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResourceLocationList;
  static deserializeBinaryFromReader(message: ResourceLocationList, reader: jspb.BinaryReader): ResourceLocationList;
}

export namespace ResourceLocationList {
  export type AsObject = {
    resourceLocationsList: Array<ResourceLocation.AsObject>,
  }
}

export class CoordinateList extends jspb.Message {
  clearCoordinatesList(): void;
  getCoordinatesList(): Array<dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate>;
  setCoordinatesList(value: Array<dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate>): void;
  addCoordinates(value?: dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate, index?: number): dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CoordinateList.AsObject;
  static toObject(includeInstance: boolean, msg: CoordinateList): CoordinateList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CoordinateList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CoordinateList;
  static deserializeBinaryFromReader(message: CoordinateList, reader: jspb.BinaryReader): CoordinateList;
}

export namespace CoordinateList {
  export type AsObject = {
    coordinatesList: Array<dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate.AsObject>,
  }
}

export class SpatialUnitList extends jspb.Message {
  clearSpatialUnitsList(): void;
  getSpatialUnitsList(): Array<dlkit_primordium_mapping_spatial_units_pb.SpatialUnit>;
  setSpatialUnitsList(value: Array<dlkit_primordium_mapping_spatial_units_pb.SpatialUnit>): void;
  addSpatialUnits(value?: dlkit_primordium_mapping_spatial_units_pb.SpatialUnit, index?: number): dlkit_primordium_mapping_spatial_units_pb.SpatialUnit;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SpatialUnitList.AsObject;
  static toObject(includeInstance: boolean, msg: SpatialUnitList): SpatialUnitList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SpatialUnitList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SpatialUnitList;
  static deserializeBinaryFromReader(message: SpatialUnitList, reader: jspb.BinaryReader): SpatialUnitList;
}

export namespace SpatialUnitList {
  export type AsObject = {
    spatialUnitsList: Array<dlkit_primordium_mapping_spatial_units_pb.SpatialUnit.AsObject>,
  }
}

