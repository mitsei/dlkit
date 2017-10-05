// package: dlkit.proto.configuration
// file: dlkit/proto/configuration.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_calendaring_primitives_pb from "../../dlkit/primordium/calendaring/primitives_pb";
import * as dlkit_primordium_financials_unimplemented_primitives_pb from "../../dlkit/primordium/financials/unimplemented_primitives_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_installation_primitives_pb from "../../dlkit/primordium/installation/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_mapping_coordinate_primitives_pb from "../../dlkit/primordium/mapping/coordinate_primitives_pb";
import * as dlkit_primordium_mapping_spatial_units_pb from "../../dlkit/primordium/mapping/spatial_units_pb";
import * as dlkit_primordium_mapping_unimplemented_primitives_pb from "../../dlkit/primordium/mapping/unimplemented_primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Parameter extends jspb.Message {
  hasConfiguration(): boolean;
  clearConfiguration(): void;
  getConfiguration(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setConfiguration(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasValueCoordinateType(): boolean;
  clearValueCoordinateType(): void;
  getValueCoordinateType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setValueCoordinateType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasValueHeadingType(): boolean;
  clearValueHeadingType(): void;
  getValueHeadingType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setValueHeadingType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasValueObjectType(): boolean;
  clearValueObjectType(): void;
  getValueObjectType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setValueObjectType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasValueSpatialUnitRecordType(): boolean;
  clearValueSpatialUnitRecordType(): void;
  getValueSpatialUnitRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setValueSpatialUnitRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  getValueSyntax(): Parameter.Syntax;
  setValueSyntax(value: Parameter.Syntax): void;

  hasValueVersionScheme(): boolean;
  clearValueVersionScheme(): void;
  getValueVersionScheme(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setValueVersionScheme(value?: dlkit_primordium_type_primitives_pb.Type): void;

  getValuesShuffled(): boolean;
  setValuesShuffled(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Parameter.AsObject;
  static toObject(includeInstance: boolean, msg: Parameter): Parameter.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Parameter, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Parameter;
  static deserializeBinaryFromReader(message: Parameter, reader: jspb.BinaryReader): Parameter;
}

export namespace Parameter {
  export type AsObject = {
    configuration?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    valueCoordinateType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    valueHeadingType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    valueObjectType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    valueSpatialUnitRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    valueSyntax: Parameter.Syntax,
    valueVersionScheme?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    valuesShuffled: boolean,
  }

  export enum Syntax {
    NONE = 0,
    BOOLEAN = 1,
    BYTE = 2,
    CARDINAL = 3,
    COORDINATE = 4,
    CURRENCY = 5,
    DATETIME = 6,
    DECIMAL = 7,
    DISPLAYTEXT = 8,
    DISTANCE = 9,
    DURATION = 10,
    HEADING = 11,
    ID = 12,
    INTEGER = 13,
    OBJECT = 14,
    SPATIALUNIT = 15,
    SPEED = 16,
    STRING = 17,
    TIME = 18,
    TYPE = 19,
    VERSION = 20,
  }
}

export class ParameterQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterQuery): ParameterQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterQuery;
  static deserializeBinaryFromReader(message: ParameterQuery, reader: jspb.BinaryReader): ParameterQuery;
}

export namespace ParameterQuery {
  export type AsObject = {
  }
}

export class ParameterQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterQueryInspector): ParameterQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterQueryInspector;
  static deserializeBinaryFromReader(message: ParameterQueryInspector, reader: jspb.BinaryReader): ParameterQueryInspector;
}

export namespace ParameterQueryInspector {
  export type AsObject = {
  }
}

export class ParameterForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterForm.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterForm): ParameterForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterForm;
  static deserializeBinaryFromReader(message: ParameterForm, reader: jspb.BinaryReader): ParameterForm;
}

export namespace ParameterForm {
  export type AsObject = {
  }
}

export class ParameterSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterSearchOrder): ParameterSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterSearchOrder;
  static deserializeBinaryFromReader(message: ParameterSearchOrder, reader: jspb.BinaryReader): ParameterSearchOrder;
}

export namespace ParameterSearchOrder {
  export type AsObject = {
  }
}

export class ParameterSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterSearch): ParameterSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterSearch;
  static deserializeBinaryFromReader(message: ParameterSearch, reader: jspb.BinaryReader): ParameterSearch;
}

export namespace ParameterSearch {
  export type AsObject = {
  }
}

export class ParameterSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterSearchResults): ParameterSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterSearchResults;
  static deserializeBinaryFromReader(message: ParameterSearchResults, reader: jspb.BinaryReader): ParameterSearchResults;
}

export namespace ParameterSearchResults {
  export type AsObject = {
  }
}

export class ParameterList extends jspb.Message {
  clearParametersList(): void;
  getParametersList(): Array<Parameter>;
  setParametersList(value: Array<Parameter>): void;
  addParameters(value?: Parameter, index?: number): Parameter;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParameterList.AsObject;
  static toObject(includeInstance: boolean, msg: ParameterList): ParameterList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ParameterList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParameterList;
  static deserializeBinaryFromReader(message: ParameterList, reader: jspb.BinaryReader): ParameterList;
}

export namespace ParameterList {
  export type AsObject = {
    parametersList: Array<Parameter.AsObject>,
  }
}

export class Value extends jspb.Message {
  getBooleanValue(): boolean;
  setBooleanValue(value: boolean): void;

  clearBytesValueList(): void;
  getBytesValueList(): Array<Uint8Array | string>;
  getBytesValueList_asU8(): Array<Uint8Array>;
  getBytesValueList_asB64(): Array<string>;
  setBytesValueList(value: Array<Uint8Array | string>): void;
  addBytesValue(value: Uint8Array | string, index?: number): Uint8Array | string;

  getCardinalValue(): number;
  setCardinalValue(value: number): void;

  hasConfiguration(): boolean;
  clearConfiguration(): void;
  getConfiguration(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setConfiguration(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasCoordinateValue(): boolean;
  clearCoordinateValue(): void;
  getCoordinateValue(): dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate | undefined;
  setCoordinateValue(value?: dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate): void;

  hasCurrencyValue(): boolean;
  clearCurrencyValue(): void;
  getCurrencyValue(): dlkit_primordium_financials_unimplemented_primitives_pb.Currency | undefined;
  setCurrencyValue(value?: dlkit_primordium_financials_unimplemented_primitives_pb.Currency): void;

  hasDateTimeValue(): boolean;
  clearDateTimeValue(): void;
  getDateTimeValue(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setDateTimeValue(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getDecimalValue(): number;
  setDecimalValue(value: number): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDistanceValue(): boolean;
  clearDistanceValue(): void;
  getDistanceValue(): dlkit_primordium_mapping_unimplemented_primitives_pb.Distance | undefined;
  setDistanceValue(value?: dlkit_primordium_mapping_unimplemented_primitives_pb.Distance): void;

  hasDurationValue(): boolean;
  clearDurationValue(): void;
  getDurationValue(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setDurationValue(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasIdValue(): boolean;
  clearIdValue(): void;
  getIdValue(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setIdValue(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIntegerValue(): number;
  setIntegerValue(value: number): void;

  hasParameter(): boolean;
  clearParameter(): void;
  getParameter(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setParameter(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getPriority(): number;
  setPriority(value: number): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasSpatialUnitValue(): boolean;
  clearSpatialUnitValue(): void;
  getSpatialUnitValue(): dlkit_primordium_mapping_spatial_units_pb.SpatialUnit | undefined;
  setSpatialUnitValue(value?: dlkit_primordium_mapping_spatial_units_pb.SpatialUnit): void;

  hasSpeedValue(): boolean;
  clearSpeedValue(): void;
  getSpeedValue(): dlkit_primordium_mapping_unimplemented_primitives_pb.Speed | undefined;
  setSpeedValue(value?: dlkit_primordium_mapping_unimplemented_primitives_pb.Speed): void;

  getStringValue(): string;
  setStringValue(value: string): void;

  hasTimeValue(): boolean;
  clearTimeValue(): void;
  getTimeValue(): dlkit_primordium_calendaring_primitives_pb.Time | undefined;
  setTimeValue(value?: dlkit_primordium_calendaring_primitives_pb.Time): void;

  hasTypeValue(): boolean;
  clearTypeValue(): void;
  getTypeValue(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setTypeValue(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasVersionValue(): boolean;
  clearVersionValue(): void;
  getVersionValue(): dlkit_primordium_installation_primitives_pb.Version | undefined;
  setVersionValue(value?: dlkit_primordium_installation_primitives_pb.Version): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Value.AsObject;
  static toObject(includeInstance: boolean, msg: Value): Value.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Value, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Value;
  static deserializeBinaryFromReader(message: Value, reader: jspb.BinaryReader): Value;
}

export namespace Value {
  export type AsObject = {
    booleanValue: boolean,
    bytesValueList: Array<Uint8Array | string>,
    cardinalValue: number,
    configuration?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    coordinateValue?: dlkit_primordium_mapping_coordinate_primitives_pb.Coordinate.AsObject,
    currencyValue?: dlkit_primordium_financials_unimplemented_primitives_pb.Currency.AsObject,
    dateTimeValue?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    decimalValue: number,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    distanceValue?: dlkit_primordium_mapping_unimplemented_primitives_pb.Distance.AsObject,
    durationValue?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    idValue?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    integerValue: number,
    parameter?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    priority: number,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    spatialUnitValue?: dlkit_primordium_mapping_spatial_units_pb.SpatialUnit.AsObject,
    speedValue?: dlkit_primordium_mapping_unimplemented_primitives_pb.Speed.AsObject,
    stringValue: string,
    timeValue?: dlkit_primordium_calendaring_primitives_pb.Time.AsObject,
    typeValue?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    versionValue?: dlkit_primordium_installation_primitives_pb.Version.AsObject,
  }
}

export class ValueQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ValueQuery): ValueQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueQuery;
  static deserializeBinaryFromReader(message: ValueQuery, reader: jspb.BinaryReader): ValueQuery;
}

export namespace ValueQuery {
  export type AsObject = {
  }
}

export class ValueQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ValueQueryInspector): ValueQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueQueryInspector;
  static deserializeBinaryFromReader(message: ValueQueryInspector, reader: jspb.BinaryReader): ValueQueryInspector;
}

export namespace ValueQueryInspector {
  export type AsObject = {
  }
}

export class ValueForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueForm.AsObject;
  static toObject(includeInstance: boolean, msg: ValueForm): ValueForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueForm;
  static deserializeBinaryFromReader(message: ValueForm, reader: jspb.BinaryReader): ValueForm;
}

export namespace ValueForm {
  export type AsObject = {
  }
}

export class ValueSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ValueSearchOrder): ValueSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueSearchOrder;
  static deserializeBinaryFromReader(message: ValueSearchOrder, reader: jspb.BinaryReader): ValueSearchOrder;
}

export namespace ValueSearchOrder {
  export type AsObject = {
  }
}

export class ValueSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ValueSearch): ValueSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueSearch;
  static deserializeBinaryFromReader(message: ValueSearch, reader: jspb.BinaryReader): ValueSearch;
}

export namespace ValueSearch {
  export type AsObject = {
  }
}

export class ValueSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ValueSearchResults): ValueSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueSearchResults;
  static deserializeBinaryFromReader(message: ValueSearchResults, reader: jspb.BinaryReader): ValueSearchResults;
}

export namespace ValueSearchResults {
  export type AsObject = {
  }
}

export class ValueList extends jspb.Message {
  clearValuesList(): void;
  getValuesList(): Array<Value>;
  setValuesList(value: Array<Value>): void;
  addValues(value?: Value, index?: number): Value;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueList.AsObject;
  static toObject(includeInstance: boolean, msg: ValueList): ValueList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueList;
  static deserializeBinaryFromReader(message: ValueList, reader: jspb.BinaryReader): ValueList;
}

export namespace ValueList {
  export type AsObject = {
    valuesList: Array<Value.AsObject>,
  }
}

export class ValueCondition extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ValueCondition.AsObject;
  static toObject(includeInstance: boolean, msg: ValueCondition): ValueCondition.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ValueCondition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ValueCondition;
  static deserializeBinaryFromReader(message: ValueCondition, reader: jspb.BinaryReader): ValueCondition;
}

export namespace ValueCondition {
  export type AsObject = {
  }
}

export class Configuration extends jspb.Message {
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
  toObject(includeInstance?: boolean): Configuration.AsObject;
  static toObject(includeInstance: boolean, msg: Configuration): Configuration.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Configuration, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Configuration;
  static deserializeBinaryFromReader(message: Configuration, reader: jspb.BinaryReader): Configuration;
}

export namespace Configuration {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class ConfigurationQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationQuery): ConfigurationQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationQuery;
  static deserializeBinaryFromReader(message: ConfigurationQuery, reader: jspb.BinaryReader): ConfigurationQuery;
}

export namespace ConfigurationQuery {
  export type AsObject = {
  }
}

export class ConfigurationQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationQueryInspector): ConfigurationQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationQueryInspector;
  static deserializeBinaryFromReader(message: ConfigurationQueryInspector, reader: jspb.BinaryReader): ConfigurationQueryInspector;
}

export namespace ConfigurationQueryInspector {
  export type AsObject = {
  }
}

export class ConfigurationForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationForm.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationForm): ConfigurationForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationForm;
  static deserializeBinaryFromReader(message: ConfigurationForm, reader: jspb.BinaryReader): ConfigurationForm;
}

export namespace ConfigurationForm {
  export type AsObject = {
  }
}

export class ConfigurationSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationSearchOrder): ConfigurationSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationSearchOrder;
  static deserializeBinaryFromReader(message: ConfigurationSearchOrder, reader: jspb.BinaryReader): ConfigurationSearchOrder;
}

export namespace ConfigurationSearchOrder {
  export type AsObject = {
  }
}

export class ConfigurationSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationSearch): ConfigurationSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationSearch;
  static deserializeBinaryFromReader(message: ConfigurationSearch, reader: jspb.BinaryReader): ConfigurationSearch;
}

export namespace ConfigurationSearch {
  export type AsObject = {
  }
}

export class ConfigurationSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationSearchResults): ConfigurationSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationSearchResults;
  static deserializeBinaryFromReader(message: ConfigurationSearchResults, reader: jspb.BinaryReader): ConfigurationSearchResults;
}

export namespace ConfigurationSearchResults {
  export type AsObject = {
  }
}

export class ConfigurationList extends jspb.Message {
  clearConfigurationsList(): void;
  getConfigurationsList(): Array<Configuration>;
  setConfigurationsList(value: Array<Configuration>): void;
  addConfigurations(value?: Configuration, index?: number): Configuration;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationList.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationList): ConfigurationList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationList;
  static deserializeBinaryFromReader(message: ConfigurationList, reader: jspb.BinaryReader): ConfigurationList;
}

export namespace ConfigurationList {
  export type AsObject = {
    configurationsList: Array<Configuration.AsObject>,
  }
}

export class ConfigurationNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationNode.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationNode): ConfigurationNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationNode;
  static deserializeBinaryFromReader(message: ConfigurationNode, reader: jspb.BinaryReader): ConfigurationNode;
}

export namespace ConfigurationNode {
  export type AsObject = {
  }
}

export class ConfigurationNodeList extends jspb.Message {
  clearConfigurationNodesList(): void;
  getConfigurationNodesList(): Array<ConfigurationNode>;
  setConfigurationNodesList(value: Array<ConfigurationNode>): void;
  addConfigurationNodes(value?: ConfigurationNode, index?: number): ConfigurationNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ConfigurationNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: ConfigurationNodeList): ConfigurationNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ConfigurationNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ConfigurationNodeList;
  static deserializeBinaryFromReader(message: ConfigurationNodeList, reader: jspb.BinaryReader): ConfigurationNodeList;
}

export namespace ConfigurationNodeList {
  export type AsObject = {
    configurationNodesList: Array<ConfigurationNode.AsObject>,
  }
}

