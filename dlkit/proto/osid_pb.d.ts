// package: dlkit.proto.osid
// file: dlkit/proto/osid.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class OsidCondition extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCondition.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCondition): OsidCondition.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCondition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCondition;
  static deserializeBinaryFromReader(message: OsidCondition, reader: jspb.BinaryReader): OsidCondition;
}

export namespace OsidCondition {
  export type AsObject = {
  }
}

export class OsidInput extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidInput.AsObject;
  static toObject(includeInstance: boolean, msg: OsidInput): OsidInput.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidInput, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidInput;
  static deserializeBinaryFromReader(message: OsidInput, reader: jspb.BinaryReader): OsidInput;
}

export namespace OsidInput {
  export type AsObject = {
  }
}

export class OsidResult extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidResult.AsObject;
  static toObject(includeInstance: boolean, msg: OsidResult): OsidResult.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidResult, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidResult;
  static deserializeBinaryFromReader(message: OsidResult, reader: jspb.BinaryReader): OsidResult;
}

export namespace OsidResult {
  export type AsObject = {
  }
}

export class OsidObject extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidObject.AsObject;
  static toObject(includeInstance: boolean, msg: OsidObject): OsidObject.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidObject, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidObject;
  static deserializeBinaryFromReader(message: OsidObject, reader: jspb.BinaryReader): OsidObject;
}

export namespace OsidObject {
  export type AsObject = {
  }
}

export class OsidRelationship extends jspb.Message {
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

  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRelationship.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRelationship): OsidRelationship.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRelationship, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRelationship;
  static deserializeBinaryFromReader(message: OsidRelationship, reader: jspb.BinaryReader): OsidRelationship;
}

export namespace OsidRelationship {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    noCatalog?: OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class OsidCatalog extends jspb.Message {
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

  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCatalog.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCatalog): OsidCatalog.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCatalog, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCatalog;
  static deserializeBinaryFromReader(message: OsidCatalog, reader: jspb.BinaryReader): OsidCatalog;
}

export namespace OsidCatalog {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    noCatalog?: OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class OsidRule extends jspb.Message {
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

  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasRule(): boolean;
  clearRule(): void;
  getRule(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRule(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRule.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRule): OsidRule.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRule, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRule;
  static deserializeBinaryFromReader(message: OsidRule, reader: jspb.BinaryReader): OsidRule;
}

export namespace OsidRule {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    noCatalog?: OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    rule?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class OsidEnabler extends jspb.Message {
  hasCyclicEvent(): boolean;
  clearCyclicEvent(): void;
  getCyclicEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCyclicEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasDemographic(): boolean;
  clearDemographic(): void;
  getDemographic(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setDemographic(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasEvent(): boolean;
  clearEvent(): void;
  getEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  hasSchedule(): boolean;
  clearSchedule(): void;
  getSchedule(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSchedule(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidEnabler.AsObject;
  static toObject(includeInstance: boolean, msg: OsidEnabler): OsidEnabler.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidEnabler, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidEnabler;
  static deserializeBinaryFromReader(message: OsidEnabler, reader: jspb.BinaryReader): OsidEnabler;
}

export namespace OsidEnabler {
  export type AsObject = {
    cyclicEvent?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    demographic?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    event?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    noCatalog?: OsidCatalog.AsObject,
    schedule?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class OsidConstrainer extends jspb.Message {
  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidConstrainer.AsObject;
  static toObject(includeInstance: boolean, msg: OsidConstrainer): OsidConstrainer.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidConstrainer, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidConstrainer;
  static deserializeBinaryFromReader(message: OsidConstrainer, reader: jspb.BinaryReader): OsidConstrainer;
}

export namespace OsidConstrainer {
  export type AsObject = {
    noCatalog?: OsidCatalog.AsObject,
  }
}

export class OsidProcessor extends jspb.Message {
  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidProcessor.AsObject;
  static toObject(includeInstance: boolean, msg: OsidProcessor): OsidProcessor.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidProcessor, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidProcessor;
  static deserializeBinaryFromReader(message: OsidProcessor, reader: jspb.BinaryReader): OsidProcessor;
}

export namespace OsidProcessor {
  export type AsObject = {
    noCatalog?: OsidCatalog.AsObject,
  }
}

export class OsidGovernator extends jspb.Message {
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

  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidGovernator.AsObject;
  static toObject(includeInstance: boolean, msg: OsidGovernator): OsidGovernator.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidGovernator, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidGovernator;
  static deserializeBinaryFromReader(message: OsidGovernator, reader: jspb.BinaryReader): OsidGovernator;
}

export namespace OsidGovernator {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    noCatalog?: OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class OsidCompendium extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasEndDate(): boolean;
  clearEndDate(): void;
  getEndDate(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEndDate(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getExtrapolated(): boolean;
  setExtrapolated(value: boolean): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getInterpolated(): boolean;
  setInterpolated(value: boolean): void;

  hasNoCatalog(): boolean;
  clearNoCatalog(): void;
  getNoCatalog(): OsidCatalog | undefined;
  setNoCatalog(value?: OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasStartDate(): boolean;
  clearStartDate(): void;
  getStartDate(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStartDate(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCompendium.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCompendium): OsidCompendium.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCompendium, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCompendium;
  static deserializeBinaryFromReader(message: OsidCompendium, reader: jspb.BinaryReader): OsidCompendium;
}

export namespace OsidCompendium {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    endDate?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    extrapolated: boolean,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    interpolated: boolean,
    noCatalog?: OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    startDate?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class OsidCapsule extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCapsule.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCapsule): OsidCapsule.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCapsule, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCapsule;
  static deserializeBinaryFromReader(message: OsidCapsule, reader: jspb.BinaryReader): OsidCapsule;
}

export namespace OsidCapsule {
  export type AsObject = {
  }
}

export class OsidQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidQuery): OsidQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidQuery;
  static deserializeBinaryFromReader(message: OsidQuery, reader: jspb.BinaryReader): OsidQuery;
}

export namespace OsidQuery {
  export type AsObject = {
  }
}

export class OsidIdentifiableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidIdentifiableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidIdentifiableQuery): OsidIdentifiableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidIdentifiableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidIdentifiableQuery;
  static deserializeBinaryFromReader(message: OsidIdentifiableQuery, reader: jspb.BinaryReader): OsidIdentifiableQuery;
}

export namespace OsidIdentifiableQuery {
  export type AsObject = {
  }
}

export class OsidExtensibleQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidExtensibleQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidExtensibleQuery): OsidExtensibleQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidExtensibleQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidExtensibleQuery;
  static deserializeBinaryFromReader(message: OsidExtensibleQuery, reader: jspb.BinaryReader): OsidExtensibleQuery;
}

export namespace OsidExtensibleQuery {
  export type AsObject = {
  }
}

export class OsidBrowsableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidBrowsableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidBrowsableQuery): OsidBrowsableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidBrowsableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidBrowsableQuery;
  static deserializeBinaryFromReader(message: OsidBrowsableQuery, reader: jspb.BinaryReader): OsidBrowsableQuery;
}

export namespace OsidBrowsableQuery {
  export type AsObject = {
  }
}

export class OsidTemporalQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidTemporalQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidTemporalQuery): OsidTemporalQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidTemporalQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidTemporalQuery;
  static deserializeBinaryFromReader(message: OsidTemporalQuery, reader: jspb.BinaryReader): OsidTemporalQuery;
}

export namespace OsidTemporalQuery {
  export type AsObject = {
  }
}

export class OsidSubjugateableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSubjugateableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSubjugateableQuery): OsidSubjugateableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSubjugateableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSubjugateableQuery;
  static deserializeBinaryFromReader(message: OsidSubjugateableQuery, reader: jspb.BinaryReader): OsidSubjugateableQuery;
}

export namespace OsidSubjugateableQuery {
  export type AsObject = {
  }
}

export class OsidAggregateableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidAggregateableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidAggregateableQuery): OsidAggregateableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidAggregateableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidAggregateableQuery;
  static deserializeBinaryFromReader(message: OsidAggregateableQuery, reader: jspb.BinaryReader): OsidAggregateableQuery;
}

export namespace OsidAggregateableQuery {
  export type AsObject = {
  }
}

export class OsidContainableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidContainableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidContainableQuery): OsidContainableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidContainableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidContainableQuery;
  static deserializeBinaryFromReader(message: OsidContainableQuery, reader: jspb.BinaryReader): OsidContainableQuery;
}

export namespace OsidContainableQuery {
  export type AsObject = {
  }
}

export class OsidSourceableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSourceableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSourceableQuery): OsidSourceableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSourceableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSourceableQuery;
  static deserializeBinaryFromReader(message: OsidSourceableQuery, reader: jspb.BinaryReader): OsidSourceableQuery;
}

export namespace OsidSourceableQuery {
  export type AsObject = {
  }
}

export class OsidFederateableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidFederateableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidFederateableQuery): OsidFederateableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidFederateableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidFederateableQuery;
  static deserializeBinaryFromReader(message: OsidFederateableQuery, reader: jspb.BinaryReader): OsidFederateableQuery;
}

export namespace OsidFederateableQuery {
  export type AsObject = {
  }
}

export class OsidOperableQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidOperableQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidOperableQuery): OsidOperableQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidOperableQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidOperableQuery;
  static deserializeBinaryFromReader(message: OsidOperableQuery, reader: jspb.BinaryReader): OsidOperableQuery;
}

export namespace OsidOperableQuery {
  export type AsObject = {
  }
}

export class OsidObjectQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidObjectQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidObjectQuery): OsidObjectQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidObjectQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidObjectQuery;
  static deserializeBinaryFromReader(message: OsidObjectQuery, reader: jspb.BinaryReader): OsidObjectQuery;
}

export namespace OsidObjectQuery {
  export type AsObject = {
  }
}

export class OsidRelationshipQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRelationshipQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRelationshipQuery): OsidRelationshipQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRelationshipQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRelationshipQuery;
  static deserializeBinaryFromReader(message: OsidRelationshipQuery, reader: jspb.BinaryReader): OsidRelationshipQuery;
}

export namespace OsidRelationshipQuery {
  export type AsObject = {
  }
}

export class OsidCatalogQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCatalogQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCatalogQuery): OsidCatalogQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCatalogQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCatalogQuery;
  static deserializeBinaryFromReader(message: OsidCatalogQuery, reader: jspb.BinaryReader): OsidCatalogQuery;
}

export namespace OsidCatalogQuery {
  export type AsObject = {
  }
}

export class OsidRuleQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRuleQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRuleQuery): OsidRuleQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRuleQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRuleQuery;
  static deserializeBinaryFromReader(message: OsidRuleQuery, reader: jspb.BinaryReader): OsidRuleQuery;
}

export namespace OsidRuleQuery {
  export type AsObject = {
  }
}

export class OsidEnablerQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidEnablerQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidEnablerQuery): OsidEnablerQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidEnablerQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidEnablerQuery;
  static deserializeBinaryFromReader(message: OsidEnablerQuery, reader: jspb.BinaryReader): OsidEnablerQuery;
}

export namespace OsidEnablerQuery {
  export type AsObject = {
  }
}

export class OsidConstrainerQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidConstrainerQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidConstrainerQuery): OsidConstrainerQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidConstrainerQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidConstrainerQuery;
  static deserializeBinaryFromReader(message: OsidConstrainerQuery, reader: jspb.BinaryReader): OsidConstrainerQuery;
}

export namespace OsidConstrainerQuery {
  export type AsObject = {
  }
}

export class OsidProcessorQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidProcessorQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidProcessorQuery): OsidProcessorQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidProcessorQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidProcessorQuery;
  static deserializeBinaryFromReader(message: OsidProcessorQuery, reader: jspb.BinaryReader): OsidProcessorQuery;
}

export namespace OsidProcessorQuery {
  export type AsObject = {
  }
}

export class OsidGovernatorQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidGovernatorQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidGovernatorQuery): OsidGovernatorQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidGovernatorQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidGovernatorQuery;
  static deserializeBinaryFromReader(message: OsidGovernatorQuery, reader: jspb.BinaryReader): OsidGovernatorQuery;
}

export namespace OsidGovernatorQuery {
  export type AsObject = {
  }
}

export class OsidCompendiumQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCompendiumQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCompendiumQuery): OsidCompendiumQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCompendiumQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCompendiumQuery;
  static deserializeBinaryFromReader(message: OsidCompendiumQuery, reader: jspb.BinaryReader): OsidCompendiumQuery;
}

export namespace OsidCompendiumQuery {
  export type AsObject = {
  }
}

export class OsidCapsuleQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCapsuleQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCapsuleQuery): OsidCapsuleQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCapsuleQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCapsuleQuery;
  static deserializeBinaryFromReader(message: OsidCapsuleQuery, reader: jspb.BinaryReader): OsidCapsuleQuery;
}

export namespace OsidCapsuleQuery {
  export type AsObject = {
  }
}

export class OsidQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidQueryInspector): OsidQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidQueryInspector;
  static deserializeBinaryFromReader(message: OsidQueryInspector, reader: jspb.BinaryReader): OsidQueryInspector;
}

export namespace OsidQueryInspector {
  export type AsObject = {
  }
}

export class OsidIdentifiableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidIdentifiableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidIdentifiableQueryInspector): OsidIdentifiableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidIdentifiableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidIdentifiableQueryInspector;
  static deserializeBinaryFromReader(message: OsidIdentifiableQueryInspector, reader: jspb.BinaryReader): OsidIdentifiableQueryInspector;
}

export namespace OsidIdentifiableQueryInspector {
  export type AsObject = {
  }
}

export class OsidExtensibleQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidExtensibleQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidExtensibleQueryInspector): OsidExtensibleQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidExtensibleQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidExtensibleQueryInspector;
  static deserializeBinaryFromReader(message: OsidExtensibleQueryInspector, reader: jspb.BinaryReader): OsidExtensibleQueryInspector;
}

export namespace OsidExtensibleQueryInspector {
  export type AsObject = {
  }
}

export class OsidBrowsableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidBrowsableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidBrowsableQueryInspector): OsidBrowsableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidBrowsableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidBrowsableQueryInspector;
  static deserializeBinaryFromReader(message: OsidBrowsableQueryInspector, reader: jspb.BinaryReader): OsidBrowsableQueryInspector;
}

export namespace OsidBrowsableQueryInspector {
  export type AsObject = {
  }
}

export class OsidTemporalQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidTemporalQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidTemporalQueryInspector): OsidTemporalQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidTemporalQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidTemporalQueryInspector;
  static deserializeBinaryFromReader(message: OsidTemporalQueryInspector, reader: jspb.BinaryReader): OsidTemporalQueryInspector;
}

export namespace OsidTemporalQueryInspector {
  export type AsObject = {
  }
}

export class OsidSubjugateableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSubjugateableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSubjugateableQueryInspector): OsidSubjugateableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSubjugateableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSubjugateableQueryInspector;
  static deserializeBinaryFromReader(message: OsidSubjugateableQueryInspector, reader: jspb.BinaryReader): OsidSubjugateableQueryInspector;
}

export namespace OsidSubjugateableQueryInspector {
  export type AsObject = {
  }
}

export class OsidAggregateableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidAggregateableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidAggregateableQueryInspector): OsidAggregateableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidAggregateableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidAggregateableQueryInspector;
  static deserializeBinaryFromReader(message: OsidAggregateableQueryInspector, reader: jspb.BinaryReader): OsidAggregateableQueryInspector;
}

export namespace OsidAggregateableQueryInspector {
  export type AsObject = {
  }
}

export class OsidContainableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidContainableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidContainableQueryInspector): OsidContainableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidContainableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidContainableQueryInspector;
  static deserializeBinaryFromReader(message: OsidContainableQueryInspector, reader: jspb.BinaryReader): OsidContainableQueryInspector;
}

export namespace OsidContainableQueryInspector {
  export type AsObject = {
  }
}

export class OsidSourceableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSourceableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSourceableQueryInspector): OsidSourceableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSourceableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSourceableQueryInspector;
  static deserializeBinaryFromReader(message: OsidSourceableQueryInspector, reader: jspb.BinaryReader): OsidSourceableQueryInspector;
}

export namespace OsidSourceableQueryInspector {
  export type AsObject = {
  }
}

export class OsidFederateableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidFederateableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidFederateableQueryInspector): OsidFederateableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidFederateableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidFederateableQueryInspector;
  static deserializeBinaryFromReader(message: OsidFederateableQueryInspector, reader: jspb.BinaryReader): OsidFederateableQueryInspector;
}

export namespace OsidFederateableQueryInspector {
  export type AsObject = {
  }
}

export class OsidOperableQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidOperableQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidOperableQueryInspector): OsidOperableQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidOperableQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidOperableQueryInspector;
  static deserializeBinaryFromReader(message: OsidOperableQueryInspector, reader: jspb.BinaryReader): OsidOperableQueryInspector;
}

export namespace OsidOperableQueryInspector {
  export type AsObject = {
  }
}

export class OsidObjectQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidObjectQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidObjectQueryInspector): OsidObjectQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidObjectQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidObjectQueryInspector;
  static deserializeBinaryFromReader(message: OsidObjectQueryInspector, reader: jspb.BinaryReader): OsidObjectQueryInspector;
}

export namespace OsidObjectQueryInspector {
  export type AsObject = {
  }
}

export class OsidRelationshipQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRelationshipQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRelationshipQueryInspector): OsidRelationshipQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRelationshipQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRelationshipQueryInspector;
  static deserializeBinaryFromReader(message: OsidRelationshipQueryInspector, reader: jspb.BinaryReader): OsidRelationshipQueryInspector;
}

export namespace OsidRelationshipQueryInspector {
  export type AsObject = {
  }
}

export class OsidCatalogQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCatalogQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCatalogQueryInspector): OsidCatalogQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCatalogQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCatalogQueryInspector;
  static deserializeBinaryFromReader(message: OsidCatalogQueryInspector, reader: jspb.BinaryReader): OsidCatalogQueryInspector;
}

export namespace OsidCatalogQueryInspector {
  export type AsObject = {
  }
}

export class OsidRuleQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRuleQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRuleQueryInspector): OsidRuleQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRuleQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRuleQueryInspector;
  static deserializeBinaryFromReader(message: OsidRuleQueryInspector, reader: jspb.BinaryReader): OsidRuleQueryInspector;
}

export namespace OsidRuleQueryInspector {
  export type AsObject = {
  }
}

export class OsidEnablerQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidEnablerQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidEnablerQueryInspector): OsidEnablerQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidEnablerQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidEnablerQueryInspector;
  static deserializeBinaryFromReader(message: OsidEnablerQueryInspector, reader: jspb.BinaryReader): OsidEnablerQueryInspector;
}

export namespace OsidEnablerQueryInspector {
  export type AsObject = {
  }
}

export class OsidConstrainerQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidConstrainerQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidConstrainerQueryInspector): OsidConstrainerQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidConstrainerQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidConstrainerQueryInspector;
  static deserializeBinaryFromReader(message: OsidConstrainerQueryInspector, reader: jspb.BinaryReader): OsidConstrainerQueryInspector;
}

export namespace OsidConstrainerQueryInspector {
  export type AsObject = {
  }
}

export class OsidProcessorQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidProcessorQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidProcessorQueryInspector): OsidProcessorQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidProcessorQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidProcessorQueryInspector;
  static deserializeBinaryFromReader(message: OsidProcessorQueryInspector, reader: jspb.BinaryReader): OsidProcessorQueryInspector;
}

export namespace OsidProcessorQueryInspector {
  export type AsObject = {
  }
}

export class OsidGovernatorQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidGovernatorQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidGovernatorQueryInspector): OsidGovernatorQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidGovernatorQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidGovernatorQueryInspector;
  static deserializeBinaryFromReader(message: OsidGovernatorQueryInspector, reader: jspb.BinaryReader): OsidGovernatorQueryInspector;
}

export namespace OsidGovernatorQueryInspector {
  export type AsObject = {
  }
}

export class OsidCompendiumQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCompendiumQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCompendiumQueryInspector): OsidCompendiumQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCompendiumQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCompendiumQueryInspector;
  static deserializeBinaryFromReader(message: OsidCompendiumQueryInspector, reader: jspb.BinaryReader): OsidCompendiumQueryInspector;
}

export namespace OsidCompendiumQueryInspector {
  export type AsObject = {
  }
}

export class OsidCapsuleQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCapsuleQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCapsuleQueryInspector): OsidCapsuleQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCapsuleQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCapsuleQueryInspector;
  static deserializeBinaryFromReader(message: OsidCapsuleQueryInspector, reader: jspb.BinaryReader): OsidCapsuleQueryInspector;
}

export namespace OsidCapsuleQueryInspector {
  export type AsObject = {
  }
}

export class OsidForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidForm): OsidForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidForm;
  static deserializeBinaryFromReader(message: OsidForm, reader: jspb.BinaryReader): OsidForm;
}

export namespace OsidForm {
  export type AsObject = {
  }
}

export class OsidIdentifiableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidIdentifiableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidIdentifiableForm): OsidIdentifiableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidIdentifiableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidIdentifiableForm;
  static deserializeBinaryFromReader(message: OsidIdentifiableForm, reader: jspb.BinaryReader): OsidIdentifiableForm;
}

export namespace OsidIdentifiableForm {
  export type AsObject = {
  }
}

export class OsidExtensibleForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidExtensibleForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidExtensibleForm): OsidExtensibleForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidExtensibleForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidExtensibleForm;
  static deserializeBinaryFromReader(message: OsidExtensibleForm, reader: jspb.BinaryReader): OsidExtensibleForm;
}

export namespace OsidExtensibleForm {
  export type AsObject = {
  }
}

export class OsidBrowsableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidBrowsableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidBrowsableForm): OsidBrowsableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidBrowsableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidBrowsableForm;
  static deserializeBinaryFromReader(message: OsidBrowsableForm, reader: jspb.BinaryReader): OsidBrowsableForm;
}

export namespace OsidBrowsableForm {
  export type AsObject = {
  }
}

export class OsidTemporalForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidTemporalForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidTemporalForm): OsidTemporalForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidTemporalForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidTemporalForm;
  static deserializeBinaryFromReader(message: OsidTemporalForm, reader: jspb.BinaryReader): OsidTemporalForm;
}

export namespace OsidTemporalForm {
  export type AsObject = {
  }
}

export class OsidSubjugateableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSubjugateableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSubjugateableForm): OsidSubjugateableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSubjugateableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSubjugateableForm;
  static deserializeBinaryFromReader(message: OsidSubjugateableForm, reader: jspb.BinaryReader): OsidSubjugateableForm;
}

export namespace OsidSubjugateableForm {
  export type AsObject = {
  }
}

export class OsidAggregateableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidAggregateableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidAggregateableForm): OsidAggregateableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidAggregateableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidAggregateableForm;
  static deserializeBinaryFromReader(message: OsidAggregateableForm, reader: jspb.BinaryReader): OsidAggregateableForm;
}

export namespace OsidAggregateableForm {
  export type AsObject = {
  }
}

export class OsidContainableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidContainableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidContainableForm): OsidContainableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidContainableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidContainableForm;
  static deserializeBinaryFromReader(message: OsidContainableForm, reader: jspb.BinaryReader): OsidContainableForm;
}

export namespace OsidContainableForm {
  export type AsObject = {
  }
}

export class OsidSourceableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSourceableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSourceableForm): OsidSourceableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSourceableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSourceableForm;
  static deserializeBinaryFromReader(message: OsidSourceableForm, reader: jspb.BinaryReader): OsidSourceableForm;
}

export namespace OsidSourceableForm {
  export type AsObject = {
  }
}

export class OsidFederateableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidFederateableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidFederateableForm): OsidFederateableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidFederateableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidFederateableForm;
  static deserializeBinaryFromReader(message: OsidFederateableForm, reader: jspb.BinaryReader): OsidFederateableForm;
}

export namespace OsidFederateableForm {
  export type AsObject = {
  }
}

export class OsidOperableForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidOperableForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidOperableForm): OsidOperableForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidOperableForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidOperableForm;
  static deserializeBinaryFromReader(message: OsidOperableForm, reader: jspb.BinaryReader): OsidOperableForm;
}

export namespace OsidOperableForm {
  export type AsObject = {
  }
}

export class OsidObjectForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidObjectForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidObjectForm): OsidObjectForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidObjectForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidObjectForm;
  static deserializeBinaryFromReader(message: OsidObjectForm, reader: jspb.BinaryReader): OsidObjectForm;
}

export namespace OsidObjectForm {
  export type AsObject = {
  }
}

export class OsidRelationshipForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRelationshipForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRelationshipForm): OsidRelationshipForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRelationshipForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRelationshipForm;
  static deserializeBinaryFromReader(message: OsidRelationshipForm, reader: jspb.BinaryReader): OsidRelationshipForm;
}

export namespace OsidRelationshipForm {
  export type AsObject = {
  }
}

export class OsidCatalogForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCatalogForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCatalogForm): OsidCatalogForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCatalogForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCatalogForm;
  static deserializeBinaryFromReader(message: OsidCatalogForm, reader: jspb.BinaryReader): OsidCatalogForm;
}

export namespace OsidCatalogForm {
  export type AsObject = {
  }
}

export class OsidRuleForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRuleForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRuleForm): OsidRuleForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRuleForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRuleForm;
  static deserializeBinaryFromReader(message: OsidRuleForm, reader: jspb.BinaryReader): OsidRuleForm;
}

export namespace OsidRuleForm {
  export type AsObject = {
  }
}

export class OsidEnablerForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidEnablerForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidEnablerForm): OsidEnablerForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidEnablerForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidEnablerForm;
  static deserializeBinaryFromReader(message: OsidEnablerForm, reader: jspb.BinaryReader): OsidEnablerForm;
}

export namespace OsidEnablerForm {
  export type AsObject = {
  }
}

export class OsidConstrainerForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidConstrainerForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidConstrainerForm): OsidConstrainerForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidConstrainerForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidConstrainerForm;
  static deserializeBinaryFromReader(message: OsidConstrainerForm, reader: jspb.BinaryReader): OsidConstrainerForm;
}

export namespace OsidConstrainerForm {
  export type AsObject = {
  }
}

export class OsidProcessorForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidProcessorForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidProcessorForm): OsidProcessorForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidProcessorForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidProcessorForm;
  static deserializeBinaryFromReader(message: OsidProcessorForm, reader: jspb.BinaryReader): OsidProcessorForm;
}

export namespace OsidProcessorForm {
  export type AsObject = {
  }
}

export class OsidGovernatorForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidGovernatorForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidGovernatorForm): OsidGovernatorForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidGovernatorForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidGovernatorForm;
  static deserializeBinaryFromReader(message: OsidGovernatorForm, reader: jspb.BinaryReader): OsidGovernatorForm;
}

export namespace OsidGovernatorForm {
  export type AsObject = {
  }
}

export class OsidCompendiumForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCompendiumForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCompendiumForm): OsidCompendiumForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCompendiumForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCompendiumForm;
  static deserializeBinaryFromReader(message: OsidCompendiumForm, reader: jspb.BinaryReader): OsidCompendiumForm;
}

export namespace OsidCompendiumForm {
  export type AsObject = {
  }
}

export class OsidCapsuleForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCapsuleForm.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCapsuleForm): OsidCapsuleForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCapsuleForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCapsuleForm;
  static deserializeBinaryFromReader(message: OsidCapsuleForm, reader: jspb.BinaryReader): OsidCapsuleForm;
}

export namespace OsidCapsuleForm {
  export type AsObject = {
  }
}

export class OsidSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSearchOrder): OsidSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSearchOrder;
  static deserializeBinaryFromReader(message: OsidSearchOrder, reader: jspb.BinaryReader): OsidSearchOrder;
}

export namespace OsidSearchOrder {
  export type AsObject = {
  }
}

export class OsidIdentifiableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidIdentifiableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidIdentifiableSearchOrder): OsidIdentifiableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidIdentifiableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidIdentifiableSearchOrder;
  static deserializeBinaryFromReader(message: OsidIdentifiableSearchOrder, reader: jspb.BinaryReader): OsidIdentifiableSearchOrder;
}

export namespace OsidIdentifiableSearchOrder {
  export type AsObject = {
  }
}

export class OsidExtensibleSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidExtensibleSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidExtensibleSearchOrder): OsidExtensibleSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidExtensibleSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidExtensibleSearchOrder;
  static deserializeBinaryFromReader(message: OsidExtensibleSearchOrder, reader: jspb.BinaryReader): OsidExtensibleSearchOrder;
}

export namespace OsidExtensibleSearchOrder {
  export type AsObject = {
  }
}

export class OsidBrowsableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidBrowsableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidBrowsableSearchOrder): OsidBrowsableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidBrowsableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidBrowsableSearchOrder;
  static deserializeBinaryFromReader(message: OsidBrowsableSearchOrder, reader: jspb.BinaryReader): OsidBrowsableSearchOrder;
}

export namespace OsidBrowsableSearchOrder {
  export type AsObject = {
  }
}

export class OsidTemporalSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidTemporalSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidTemporalSearchOrder): OsidTemporalSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidTemporalSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidTemporalSearchOrder;
  static deserializeBinaryFromReader(message: OsidTemporalSearchOrder, reader: jspb.BinaryReader): OsidTemporalSearchOrder;
}

export namespace OsidTemporalSearchOrder {
  export type AsObject = {
  }
}

export class OsidSubjugateableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSubjugateableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSubjugateableSearchOrder): OsidSubjugateableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSubjugateableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSubjugateableSearchOrder;
  static deserializeBinaryFromReader(message: OsidSubjugateableSearchOrder, reader: jspb.BinaryReader): OsidSubjugateableSearchOrder;
}

export namespace OsidSubjugateableSearchOrder {
  export type AsObject = {
  }
}

export class OsidAggregateableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidAggregateableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidAggregateableSearchOrder): OsidAggregateableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidAggregateableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidAggregateableSearchOrder;
  static deserializeBinaryFromReader(message: OsidAggregateableSearchOrder, reader: jspb.BinaryReader): OsidAggregateableSearchOrder;
}

export namespace OsidAggregateableSearchOrder {
  export type AsObject = {
  }
}

export class OsidContainableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidContainableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidContainableSearchOrder): OsidContainableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidContainableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidContainableSearchOrder;
  static deserializeBinaryFromReader(message: OsidContainableSearchOrder, reader: jspb.BinaryReader): OsidContainableSearchOrder;
}

export namespace OsidContainableSearchOrder {
  export type AsObject = {
  }
}

export class OsidSourceableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSourceableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSourceableSearchOrder): OsidSourceableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSourceableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSourceableSearchOrder;
  static deserializeBinaryFromReader(message: OsidSourceableSearchOrder, reader: jspb.BinaryReader): OsidSourceableSearchOrder;
}

export namespace OsidSourceableSearchOrder {
  export type AsObject = {
  }
}

export class OsidFederateableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidFederateableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidFederateableSearchOrder): OsidFederateableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidFederateableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidFederateableSearchOrder;
  static deserializeBinaryFromReader(message: OsidFederateableSearchOrder, reader: jspb.BinaryReader): OsidFederateableSearchOrder;
}

export namespace OsidFederateableSearchOrder {
  export type AsObject = {
  }
}

export class OsidOperableSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidOperableSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidOperableSearchOrder): OsidOperableSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidOperableSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidOperableSearchOrder;
  static deserializeBinaryFromReader(message: OsidOperableSearchOrder, reader: jspb.BinaryReader): OsidOperableSearchOrder;
}

export namespace OsidOperableSearchOrder {
  export type AsObject = {
  }
}

export class OsidObjectSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidObjectSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidObjectSearchOrder): OsidObjectSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidObjectSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidObjectSearchOrder;
  static deserializeBinaryFromReader(message: OsidObjectSearchOrder, reader: jspb.BinaryReader): OsidObjectSearchOrder;
}

export namespace OsidObjectSearchOrder {
  export type AsObject = {
  }
}

export class OsidRelationshipSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRelationshipSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRelationshipSearchOrder): OsidRelationshipSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRelationshipSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRelationshipSearchOrder;
  static deserializeBinaryFromReader(message: OsidRelationshipSearchOrder, reader: jspb.BinaryReader): OsidRelationshipSearchOrder;
}

export namespace OsidRelationshipSearchOrder {
  export type AsObject = {
  }
}

export class OsidCatalogSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCatalogSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCatalogSearchOrder): OsidCatalogSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCatalogSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCatalogSearchOrder;
  static deserializeBinaryFromReader(message: OsidCatalogSearchOrder, reader: jspb.BinaryReader): OsidCatalogSearchOrder;
}

export namespace OsidCatalogSearchOrder {
  export type AsObject = {
  }
}

export class OsidRuleSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidRuleSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidRuleSearchOrder): OsidRuleSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidRuleSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidRuleSearchOrder;
  static deserializeBinaryFromReader(message: OsidRuleSearchOrder, reader: jspb.BinaryReader): OsidRuleSearchOrder;
}

export namespace OsidRuleSearchOrder {
  export type AsObject = {
  }
}

export class OsidEnablerSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidEnablerSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidEnablerSearchOrder): OsidEnablerSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidEnablerSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidEnablerSearchOrder;
  static deserializeBinaryFromReader(message: OsidEnablerSearchOrder, reader: jspb.BinaryReader): OsidEnablerSearchOrder;
}

export namespace OsidEnablerSearchOrder {
  export type AsObject = {
  }
}

export class OsidConstrainerSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidConstrainerSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidConstrainerSearchOrder): OsidConstrainerSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidConstrainerSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidConstrainerSearchOrder;
  static deserializeBinaryFromReader(message: OsidConstrainerSearchOrder, reader: jspb.BinaryReader): OsidConstrainerSearchOrder;
}

export namespace OsidConstrainerSearchOrder {
  export type AsObject = {
  }
}

export class OsidProcessorSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidProcessorSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidProcessorSearchOrder): OsidProcessorSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidProcessorSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidProcessorSearchOrder;
  static deserializeBinaryFromReader(message: OsidProcessorSearchOrder, reader: jspb.BinaryReader): OsidProcessorSearchOrder;
}

export namespace OsidProcessorSearchOrder {
  export type AsObject = {
  }
}

export class OsidGovernatorSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidGovernatorSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidGovernatorSearchOrder): OsidGovernatorSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidGovernatorSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidGovernatorSearchOrder;
  static deserializeBinaryFromReader(message: OsidGovernatorSearchOrder, reader: jspb.BinaryReader): OsidGovernatorSearchOrder;
}

export namespace OsidGovernatorSearchOrder {
  export type AsObject = {
  }
}

export class OsidCompendiumSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCompendiumSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCompendiumSearchOrder): OsidCompendiumSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCompendiumSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCompendiumSearchOrder;
  static deserializeBinaryFromReader(message: OsidCompendiumSearchOrder, reader: jspb.BinaryReader): OsidCompendiumSearchOrder;
}

export namespace OsidCompendiumSearchOrder {
  export type AsObject = {
  }
}

export class OsidCapsuleSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidCapsuleSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OsidCapsuleSearchOrder): OsidCapsuleSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidCapsuleSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidCapsuleSearchOrder;
  static deserializeBinaryFromReader(message: OsidCapsuleSearchOrder, reader: jspb.BinaryReader): OsidCapsuleSearchOrder;
}

export namespace OsidCapsuleSearchOrder {
  export type AsObject = {
  }
}

export class OsidSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSearch.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSearch): OsidSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSearch;
  static deserializeBinaryFromReader(message: OsidSearch, reader: jspb.BinaryReader): OsidSearch;
}

export namespace OsidSearch {
  export type AsObject = {
  }
}

export class OsidSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: OsidSearchResults): OsidSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidSearchResults;
  static deserializeBinaryFromReader(message: OsidSearchResults, reader: jspb.BinaryReader): OsidSearchResults;
}

export namespace OsidSearchResults {
  export type AsObject = {
  }
}

export class OsidList extends jspb.Message {
  clearOsidsList(): void;
  getOsidsList(): Array<Osid>;
  setOsidsList(value: Array<Osid>): void;
  addOsids(value?: Osid, index?: number): Osid;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidList.AsObject;
  static toObject(includeInstance: boolean, msg: OsidList): OsidList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidList;
  static deserializeBinaryFromReader(message: OsidList, reader: jspb.BinaryReader): OsidList;
}

export namespace OsidList {
  export type AsObject = {
    osidsList: Array<Osid.AsObject>,
  }
}

export class Osid extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Osid.AsObject;
  static toObject(includeInstance: boolean, msg: Osid): Osid.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Osid, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Osid;
  static deserializeBinaryFromReader(message: Osid, reader: jspb.BinaryReader): Osid;
}

export namespace Osid {
  export type AsObject = {
  }
}

export class OsidNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OsidNode.AsObject;
  static toObject(includeInstance: boolean, msg: OsidNode): OsidNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OsidNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OsidNode;
  static deserializeBinaryFromReader(message: OsidNode, reader: jspb.BinaryReader): OsidNode;
}

export namespace OsidNode {
  export type AsObject = {
  }
}

