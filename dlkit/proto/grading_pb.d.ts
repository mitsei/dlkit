// package: dlkit.proto.grading
// file: dlkit/proto/grading.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Grade extends jspb.Message {
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

  hasGradeSystem(): boolean;
  clearGradeSystem(): void;
  getGradeSystem(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystem(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebook(): boolean;
  clearGradebook(): void;
  getGradebook(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setGradebook(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getInputScoreEndRange(): number;
  setInputScoreEndRange(value: number): void;

  getInputScoreStartRange(): number;
  setInputScoreStartRange(value: number): void;

  getOutputScore(): number;
  setOutputScore(value: number): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Grade.AsObject;
  static toObject(includeInstance: boolean, msg: Grade): Grade.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Grade, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Grade;
  static deserializeBinaryFromReader(message: Grade, reader: jspb.BinaryReader): Grade;
}

export namespace Grade {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    gradeSystem?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebook?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    inputScoreEndRange: number,
    inputScoreStartRange: number,
    outputScore: number,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GradeQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeQuery.AsObject;
  static toObject(includeInstance: boolean, msg: GradeQuery): GradeQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeQuery;
  static deserializeBinaryFromReader(message: GradeQuery, reader: jspb.BinaryReader): GradeQuery;
}

export namespace GradeQuery {
  export type AsObject = {
  }
}

export class GradeQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: GradeQueryInspector): GradeQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeQueryInspector;
  static deserializeBinaryFromReader(message: GradeQueryInspector, reader: jspb.BinaryReader): GradeQueryInspector;
}

export namespace GradeQueryInspector {
  export type AsObject = {
  }
}

export class GradeForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeForm.AsObject;
  static toObject(includeInstance: boolean, msg: GradeForm): GradeForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeForm;
  static deserializeBinaryFromReader(message: GradeForm, reader: jspb.BinaryReader): GradeForm;
}

export namespace GradeForm {
  export type AsObject = {
  }
}

export class GradeSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSearchOrder): GradeSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSearchOrder;
  static deserializeBinaryFromReader(message: GradeSearchOrder, reader: jspb.BinaryReader): GradeSearchOrder;
}

export namespace GradeSearchOrder {
  export type AsObject = {
  }
}

export class GradeList extends jspb.Message {
  clearGradesList(): void;
  getGradesList(): Array<Grade>;
  setGradesList(value: Array<Grade>): void;
  addGrades(value?: Grade, index?: number): Grade;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeList.AsObject;
  static toObject(includeInstance: boolean, msg: GradeList): GradeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeList;
  static deserializeBinaryFromReader(message: GradeList, reader: jspb.BinaryReader): GradeList;
}

export namespace GradeList {
  export type AsObject = {
    gradesList: Array<Grade.AsObject>,
  }
}

export class GradeSystem extends jspb.Message {
  getBasedOnGrades(): boolean;
  setBasedOnGrades(value: boolean): void;

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

  hasGradebook(): boolean;
  clearGradebook(): void;
  getGradebook(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setGradebook(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  getHighestNumericScore(): number;
  setHighestNumericScore(value: number): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getLowestNumericScore(): number;
  setLowestNumericScore(value: number): void;

  getNumericScoreIncrement(): number;
  setNumericScoreIncrement(value: number): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystem.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystem): GradeSystem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystem;
  static deserializeBinaryFromReader(message: GradeSystem, reader: jspb.BinaryReader): GradeSystem;
}

export namespace GradeSystem {
  export type AsObject = {
    basedOnGrades: boolean,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    gradebook?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    highestNumericScore: number,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    lowestNumericScore: number,
    numericScoreIncrement: number,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GradeSystemQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemQuery.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemQuery): GradeSystemQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemQuery;
  static deserializeBinaryFromReader(message: GradeSystemQuery, reader: jspb.BinaryReader): GradeSystemQuery;
}

export namespace GradeSystemQuery {
  export type AsObject = {
  }
}

export class GradeSystemQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemQueryInspector): GradeSystemQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemQueryInspector;
  static deserializeBinaryFromReader(message: GradeSystemQueryInspector, reader: jspb.BinaryReader): GradeSystemQueryInspector;
}

export namespace GradeSystemQueryInspector {
  export type AsObject = {
  }
}

export class GradeSystemForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemForm.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemForm): GradeSystemForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemForm;
  static deserializeBinaryFromReader(message: GradeSystemForm, reader: jspb.BinaryReader): GradeSystemForm;
}

export namespace GradeSystemForm {
  export type AsObject = {
  }
}

export class GradeSystemSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemSearchOrder): GradeSystemSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemSearchOrder;
  static deserializeBinaryFromReader(message: GradeSystemSearchOrder, reader: jspb.BinaryReader): GradeSystemSearchOrder;
}

export namespace GradeSystemSearchOrder {
  export type AsObject = {
  }
}

export class GradeSystemSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemSearch.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemSearch): GradeSystemSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemSearch;
  static deserializeBinaryFromReader(message: GradeSystemSearch, reader: jspb.BinaryReader): GradeSystemSearch;
}

export namespace GradeSystemSearch {
  export type AsObject = {
  }
}

export class GradeSystemSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemSearchResults): GradeSystemSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemSearchResults;
  static deserializeBinaryFromReader(message: GradeSystemSearchResults, reader: jspb.BinaryReader): GradeSystemSearchResults;
}

export namespace GradeSystemSearchResults {
  export type AsObject = {
  }
}

export class GradeSystemList extends jspb.Message {
  clearGradeSystemsList(): void;
  getGradeSystemsList(): Array<GradeSystem>;
  setGradeSystemsList(value: Array<GradeSystem>): void;
  addGradeSystems(value?: GradeSystem, index?: number): GradeSystem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeSystemList.AsObject;
  static toObject(includeInstance: boolean, msg: GradeSystemList): GradeSystemList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeSystemList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeSystemList;
  static deserializeBinaryFromReader(message: GradeSystemList, reader: jspb.BinaryReader): GradeSystemList;
}

export namespace GradeSystemList {
  export type AsObject = {
    gradeSystemsList: Array<GradeSystem.AsObject>,
  }
}

export class GradeEntry extends jspb.Message {
  hasGrade(): boolean;
  clearGrade(): void;
  getGrade(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGrade(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebook(): boolean;
  clearGradebook(): void;
  getGradebook(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setGradebook(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasGradebookColumn(): boolean;
  clearGradebookColumn(): void;
  getGradebookColumn(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumn(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIgnoredForCalculations(): boolean;
  setIgnoredForCalculations(value: boolean): void;

  hasResource(): boolean;
  clearResource(): void;
  getResource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getScore(): number;
  setScore(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntry.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntry): GradeEntry.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntry, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntry;
  static deserializeBinaryFromReader(message: GradeEntry, reader: jspb.BinaryReader): GradeEntry;
}

export namespace GradeEntry {
  export type AsObject = {
    grade?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebook?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    gradebookColumn?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    ignoredForCalculations: boolean,
    resource?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    score: number,
  }
}

export class GradeEntryQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntryQuery.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntryQuery): GradeEntryQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntryQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntryQuery;
  static deserializeBinaryFromReader(message: GradeEntryQuery, reader: jspb.BinaryReader): GradeEntryQuery;
}

export namespace GradeEntryQuery {
  export type AsObject = {
  }
}

export class GradeEntryQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntryQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntryQueryInspector): GradeEntryQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntryQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntryQueryInspector;
  static deserializeBinaryFromReader(message: GradeEntryQueryInspector, reader: jspb.BinaryReader): GradeEntryQueryInspector;
}

export namespace GradeEntryQueryInspector {
  export type AsObject = {
  }
}

export class GradeEntryForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntryForm.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntryForm): GradeEntryForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntryForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntryForm;
  static deserializeBinaryFromReader(message: GradeEntryForm, reader: jspb.BinaryReader): GradeEntryForm;
}

export namespace GradeEntryForm {
  export type AsObject = {
  }
}

export class GradeEntrySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntrySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntrySearchOrder): GradeEntrySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntrySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntrySearchOrder;
  static deserializeBinaryFromReader(message: GradeEntrySearchOrder, reader: jspb.BinaryReader): GradeEntrySearchOrder;
}

export namespace GradeEntrySearchOrder {
  export type AsObject = {
  }
}

export class GradeEntrySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntrySearch.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntrySearch): GradeEntrySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntrySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntrySearch;
  static deserializeBinaryFromReader(message: GradeEntrySearch, reader: jspb.BinaryReader): GradeEntrySearch;
}

export namespace GradeEntrySearch {
  export type AsObject = {
  }
}

export class GradeEntrySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntrySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntrySearchResults): GradeEntrySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntrySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntrySearchResults;
  static deserializeBinaryFromReader(message: GradeEntrySearchResults, reader: jspb.BinaryReader): GradeEntrySearchResults;
}

export namespace GradeEntrySearchResults {
  export type AsObject = {
  }
}

export class GradeEntryList extends jspb.Message {
  clearGradeEntriesList(): void;
  getGradeEntriesList(): Array<GradeEntry>;
  setGradeEntriesList(value: Array<GradeEntry>): void;
  addGradeEntries(value?: GradeEntry, index?: number): GradeEntry;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradeEntryList.AsObject;
  static toObject(includeInstance: boolean, msg: GradeEntryList): GradeEntryList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradeEntryList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradeEntryList;
  static deserializeBinaryFromReader(message: GradeEntryList, reader: jspb.BinaryReader): GradeEntryList;
}

export namespace GradeEntryList {
  export type AsObject = {
    gradeEntriesList: Array<GradeEntry.AsObject>,
  }
}

export class GradebookColumn extends jspb.Message {
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

  hasGradeSystem(): boolean;
  clearGradeSystem(): void;
  getGradeSystem(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystem(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebook(): boolean;
  clearGradebook(): void;
  getGradebook(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setGradebook(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumn.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumn): GradebookColumn.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumn, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumn;
  static deserializeBinaryFromReader(message: GradebookColumn, reader: jspb.BinaryReader): GradebookColumn;
}

export namespace GradebookColumn {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    gradeSystem?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebook?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GradebookColumnQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnQuery.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnQuery): GradebookColumnQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnQuery;
  static deserializeBinaryFromReader(message: GradebookColumnQuery, reader: jspb.BinaryReader): GradebookColumnQuery;
}

export namespace GradebookColumnQuery {
  export type AsObject = {
  }
}

export class GradebookColumnQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnQueryInspector): GradebookColumnQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnQueryInspector;
  static deserializeBinaryFromReader(message: GradebookColumnQueryInspector, reader: jspb.BinaryReader): GradebookColumnQueryInspector;
}

export namespace GradebookColumnQueryInspector {
  export type AsObject = {
  }
}

export class GradebookColumnForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnForm.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnForm): GradebookColumnForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnForm;
  static deserializeBinaryFromReader(message: GradebookColumnForm, reader: jspb.BinaryReader): GradebookColumnForm;
}

export namespace GradebookColumnForm {
  export type AsObject = {
  }
}

export class GradebookColumnSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSearchOrder): GradebookColumnSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSearchOrder;
  static deserializeBinaryFromReader(message: GradebookColumnSearchOrder, reader: jspb.BinaryReader): GradebookColumnSearchOrder;
}

export namespace GradebookColumnSearchOrder {
  export type AsObject = {
  }
}

export class GradebookColumnSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSearch.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSearch): GradebookColumnSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSearch;
  static deserializeBinaryFromReader(message: GradebookColumnSearch, reader: jspb.BinaryReader): GradebookColumnSearch;
}

export namespace GradebookColumnSearch {
  export type AsObject = {
  }
}

export class GradebookColumnSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSearchResults): GradebookColumnSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSearchResults;
  static deserializeBinaryFromReader(message: GradebookColumnSearchResults, reader: jspb.BinaryReader): GradebookColumnSearchResults;
}

export namespace GradebookColumnSearchResults {
  export type AsObject = {
  }
}

export class GradebookColumnList extends jspb.Message {
  clearGradebookColumnsList(): void;
  getGradebookColumnsList(): Array<GradebookColumn>;
  setGradebookColumnsList(value: Array<GradebookColumn>): void;
  addGradebookColumns(value?: GradebookColumn, index?: number): GradebookColumn;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnList.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnList): GradebookColumnList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnList;
  static deserializeBinaryFromReader(message: GradebookColumnList, reader: jspb.BinaryReader): GradebookColumnList;
}

export namespace GradebookColumnList {
  export type AsObject = {
    gradebookColumnsList: Array<GradebookColumn.AsObject>,
  }
}

export class GradebookColumnSummary extends jspb.Message {
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

  hasGradebookColumn(): boolean;
  clearGradebookColumn(): void;
  getGradebookColumn(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumn(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSummary.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSummary): GradebookColumnSummary.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSummary, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSummary;
  static deserializeBinaryFromReader(message: GradebookColumnSummary, reader: jspb.BinaryReader): GradebookColumnSummary;
}

export namespace GradebookColumnSummary {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    gradebookColumn?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GradebookColumnSummaryQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSummaryQuery.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSummaryQuery): GradebookColumnSummaryQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSummaryQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSummaryQuery;
  static deserializeBinaryFromReader(message: GradebookColumnSummaryQuery, reader: jspb.BinaryReader): GradebookColumnSummaryQuery;
}

export namespace GradebookColumnSummaryQuery {
  export type AsObject = {
  }
}

export class GradebookColumnSummaryQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSummaryQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSummaryQueryInspector): GradebookColumnSummaryQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSummaryQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSummaryQueryInspector;
  static deserializeBinaryFromReader(message: GradebookColumnSummaryQueryInspector, reader: jspb.BinaryReader): GradebookColumnSummaryQueryInspector;
}

export namespace GradebookColumnSummaryQueryInspector {
  export type AsObject = {
  }
}

export class GradebookColumnSummarySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookColumnSummarySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookColumnSummarySearchOrder): GradebookColumnSummarySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookColumnSummarySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookColumnSummarySearchOrder;
  static deserializeBinaryFromReader(message: GradebookColumnSummarySearchOrder, reader: jspb.BinaryReader): GradebookColumnSummarySearchOrder;
}

export namespace GradebookColumnSummarySearchOrder {
  export type AsObject = {
  }
}

export class Gradebook extends jspb.Message {
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
  toObject(includeInstance?: boolean): Gradebook.AsObject;
  static toObject(includeInstance: boolean, msg: Gradebook): Gradebook.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Gradebook, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Gradebook;
  static deserializeBinaryFromReader(message: Gradebook, reader: jspb.BinaryReader): Gradebook;
}

export namespace Gradebook {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GradebookQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookQuery.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookQuery): GradebookQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookQuery;
  static deserializeBinaryFromReader(message: GradebookQuery, reader: jspb.BinaryReader): GradebookQuery;
}

export namespace GradebookQuery {
  export type AsObject = {
  }
}

export class GradebookQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookQueryInspector): GradebookQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookQueryInspector;
  static deserializeBinaryFromReader(message: GradebookQueryInspector, reader: jspb.BinaryReader): GradebookQueryInspector;
}

export namespace GradebookQueryInspector {
  export type AsObject = {
  }
}

export class GradebookForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookForm.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookForm): GradebookForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookForm;
  static deserializeBinaryFromReader(message: GradebookForm, reader: jspb.BinaryReader): GradebookForm;
}

export namespace GradebookForm {
  export type AsObject = {
  }
}

export class GradebookSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookSearchOrder): GradebookSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookSearchOrder;
  static deserializeBinaryFromReader(message: GradebookSearchOrder, reader: jspb.BinaryReader): GradebookSearchOrder;
}

export namespace GradebookSearchOrder {
  export type AsObject = {
  }
}

export class GradebookSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookSearch.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookSearch): GradebookSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookSearch;
  static deserializeBinaryFromReader(message: GradebookSearch, reader: jspb.BinaryReader): GradebookSearch;
}

export namespace GradebookSearch {
  export type AsObject = {
  }
}

export class GradebookSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookSearchResults): GradebookSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookSearchResults;
  static deserializeBinaryFromReader(message: GradebookSearchResults, reader: jspb.BinaryReader): GradebookSearchResults;
}

export namespace GradebookSearchResults {
  export type AsObject = {
  }
}

export class GradebookList extends jspb.Message {
  clearGradebooksList(): void;
  getGradebooksList(): Array<Gradebook>;
  setGradebooksList(value: Array<Gradebook>): void;
  addGradebooks(value?: Gradebook, index?: number): Gradebook;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookList.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookList): GradebookList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookList;
  static deserializeBinaryFromReader(message: GradebookList, reader: jspb.BinaryReader): GradebookList;
}

export namespace GradebookList {
  export type AsObject = {
    gradebooksList: Array<Gradebook.AsObject>,
  }
}

export class GradebookNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookNode.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookNode): GradebookNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookNode;
  static deserializeBinaryFromReader(message: GradebookNode, reader: jspb.BinaryReader): GradebookNode;
}

export namespace GradebookNode {
  export type AsObject = {
  }
}

export class GradebookNodeList extends jspb.Message {
  clearGradebookNodesList(): void;
  getGradebookNodesList(): Array<GradebookNode>;
  setGradebookNodesList(value: Array<GradebookNode>): void;
  addGradebookNodes(value?: GradebookNode, index?: number): GradebookNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GradebookNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: GradebookNodeList): GradebookNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GradebookNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GradebookNodeList;
  static deserializeBinaryFromReader(message: GradebookNodeList, reader: jspb.BinaryReader): GradebookNodeList;
}

export namespace GradebookNodeList {
  export type AsObject = {
    gradebookNodesList: Array<GradebookNode.AsObject>,
  }
}

export class GetGradebookIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookIdReply): GetGradebookIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookIdReply;
  static deserializeBinaryFromReader(message: GetGradebookIdReply, reader: jspb.BinaryReader): GetGradebookIdReply;
}

export namespace GetGradebookIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookIdRequest): GetGradebookIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookIdRequest;
  static deserializeBinaryFromReader(message: GetGradebookIdRequest, reader: jspb.BinaryReader): GetGradebookIdRequest;
}

export namespace GetGradebookIdRequest {
  export type AsObject = {
  }
}

export class GetGradebookReply extends jspb.Message {
  hasGradebook(): boolean;
  clearGradebook(): void;
  getGradebook(): Gradebook | undefined;
  setGradebook(value?: Gradebook): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookReply): GetGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookReply;
  static deserializeBinaryFromReader(message: GetGradebookReply, reader: jspb.BinaryReader): GetGradebookReply;
}

export namespace GetGradebookReply {
  export type AsObject = {
    gradebook?: Gradebook.AsObject,
  }
}

export class GetGradebookRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookRequest): GetGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookRequest;
  static deserializeBinaryFromReader(message: GetGradebookRequest, reader: jspb.BinaryReader): GetGradebookRequest;
}

export namespace GetGradebookRequest {
  export type AsObject = {
  }
}

export class CanLookupGradeSystemsReply extends jspb.Message {
  getCanLookupGradeSystems(): boolean;
  setCanLookupGradeSystems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradeSystemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradeSystemsReply): CanLookupGradeSystemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradeSystemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradeSystemsReply;
  static deserializeBinaryFromReader(message: CanLookupGradeSystemsReply, reader: jspb.BinaryReader): CanLookupGradeSystemsReply;
}

export namespace CanLookupGradeSystemsReply {
  export type AsObject = {
    canLookupGradeSystems: boolean,
  }
}

export class CanLookupGradeSystemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradeSystemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradeSystemsRequest): CanLookupGradeSystemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradeSystemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradeSystemsRequest;
  static deserializeBinaryFromReader(message: CanLookupGradeSystemsRequest, reader: jspb.BinaryReader): CanLookupGradeSystemsRequest;
}

export namespace CanLookupGradeSystemsRequest {
  export type AsObject = {
  }
}

export class UseComparativeGradeSystemViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradeSystemViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradeSystemViewReply): UseComparativeGradeSystemViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradeSystemViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradeSystemViewReply;
  static deserializeBinaryFromReader(message: UseComparativeGradeSystemViewReply, reader: jspb.BinaryReader): UseComparativeGradeSystemViewReply;
}

export namespace UseComparativeGradeSystemViewReply {
  export type AsObject = {
  }
}

export class UseComparativeGradeSystemViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradeSystemViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradeSystemViewRequest): UseComparativeGradeSystemViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradeSystemViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradeSystemViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeGradeSystemViewRequest, reader: jspb.BinaryReader): UseComparativeGradeSystemViewRequest;
}

export namespace UseComparativeGradeSystemViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryGradeSystemViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradeSystemViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradeSystemViewReply): UsePlenaryGradeSystemViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradeSystemViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradeSystemViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryGradeSystemViewReply, reader: jspb.BinaryReader): UsePlenaryGradeSystemViewReply;
}

export namespace UsePlenaryGradeSystemViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryGradeSystemViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradeSystemViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradeSystemViewRequest): UsePlenaryGradeSystemViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradeSystemViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradeSystemViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryGradeSystemViewRequest, reader: jspb.BinaryReader): UsePlenaryGradeSystemViewRequest;
}

export namespace UsePlenaryGradeSystemViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedGradebookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedGradebookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedGradebookViewReply): UseFederatedGradebookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedGradebookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedGradebookViewReply;
  static deserializeBinaryFromReader(message: UseFederatedGradebookViewReply, reader: jspb.BinaryReader): UseFederatedGradebookViewReply;
}

export namespace UseFederatedGradebookViewReply {
  export type AsObject = {
  }
}

export class UseFederatedGradebookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedGradebookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedGradebookViewRequest): UseFederatedGradebookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedGradebookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedGradebookViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedGradebookViewRequest, reader: jspb.BinaryReader): UseFederatedGradebookViewRequest;
}

export namespace UseFederatedGradebookViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedGradebookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedGradebookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedGradebookViewReply): UseIsolatedGradebookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedGradebookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedGradebookViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedGradebookViewReply, reader: jspb.BinaryReader): UseIsolatedGradebookViewReply;
}

export namespace UseIsolatedGradebookViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedGradebookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedGradebookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedGradebookViewRequest): UseIsolatedGradebookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedGradebookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedGradebookViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedGradebookViewRequest, reader: jspb.BinaryReader): UseIsolatedGradebookViewRequest;
}

export namespace UseIsolatedGradebookViewRequest {
  export type AsObject = {
  }
}

export class GetGradeSystemReply extends jspb.Message {
  hasGradeSystem(): boolean;
  clearGradeSystem(): void;
  getGradeSystem(): GradeSystem | undefined;
  setGradeSystem(value?: GradeSystem): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemReply): GetGradeSystemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemReply;
  static deserializeBinaryFromReader(message: GetGradeSystemReply, reader: jspb.BinaryReader): GetGradeSystemReply;
}

export namespace GetGradeSystemReply {
  export type AsObject = {
    gradeSystem?: GradeSystem.AsObject,
  }
}

export class GetGradeSystemRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemRequest): GetGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemRequest, reader: jspb.BinaryReader): GetGradeSystemRequest;
}

export namespace GetGradeSystemRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeSystemByGradeReply extends jspb.Message {
  hasGradeSystem(): boolean;
  clearGradeSystem(): void;
  getGradeSystem(): GradeSystem | undefined;
  setGradeSystem(value?: GradeSystem): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemByGradeReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemByGradeReply): GetGradeSystemByGradeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemByGradeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemByGradeReply;
  static deserializeBinaryFromReader(message: GetGradeSystemByGradeReply, reader: jspb.BinaryReader): GetGradeSystemByGradeReply;
}

export namespace GetGradeSystemByGradeReply {
  export type AsObject = {
    gradeSystem?: GradeSystem.AsObject,
  }
}

export class GetGradeSystemByGradeRequest extends jspb.Message {
  hasGradeId(): boolean;
  clearGradeId(): void;
  getGradeId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemByGradeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemByGradeRequest): GetGradeSystemByGradeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemByGradeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemByGradeRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemByGradeRequest, reader: jspb.BinaryReader): GetGradeSystemByGradeRequest;
}

export namespace GetGradeSystemByGradeRequest {
  export type AsObject = {
    gradeId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeSystemsByIdsRequest extends jspb.Message {
  clearGradeSystemIdsList(): void;
  getGradeSystemIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradeSystemIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradeSystemIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByIdsRequest): GetGradeSystemsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByIdsRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByIdsRequest, reader: jspb.BinaryReader): GetGradeSystemsByIdsRequest;
}

export namespace GetGradeSystemsByIdsRequest {
  export type AsObject = {
    gradeSystemIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradeSystemsByGenusTypeRequest extends jspb.Message {
  hasGradeSystemGenusType(): boolean;
  clearGradeSystemGenusType(): void;
  getGradeSystemGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradeSystemGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByGenusTypeRequest): GetGradeSystemsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByGenusTypeRequest, reader: jspb.BinaryReader): GetGradeSystemsByGenusTypeRequest;
}

export namespace GetGradeSystemsByGenusTypeRequest {
  export type AsObject = {
    gradeSystemGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradeSystemsByParentGenusTypeRequest extends jspb.Message {
  hasGradeSystemGenusType(): boolean;
  clearGradeSystemGenusType(): void;
  getGradeSystemGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradeSystemGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByParentGenusTypeRequest): GetGradeSystemsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetGradeSystemsByParentGenusTypeRequest;
}

export namespace GetGradeSystemsByParentGenusTypeRequest {
  export type AsObject = {
    gradeSystemGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradeSystemsByRecordTypeRequest extends jspb.Message {
  hasGradeSystemRecordType(): boolean;
  clearGradeSystemRecordType(): void;
  getGradeSystemRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradeSystemRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByRecordTypeRequest): GetGradeSystemsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByRecordTypeRequest, reader: jspb.BinaryReader): GetGradeSystemsByRecordTypeRequest;
}

export namespace GetGradeSystemsByRecordTypeRequest {
  export type AsObject = {
    gradeSystemRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradeSystemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsRequest): GetGradeSystemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsRequest, reader: jspb.BinaryReader): GetGradeSystemsRequest;
}

export namespace GetGradeSystemsRequest {
  export type AsObject = {
  }
}

export class CanSearchGradeSystemsReply extends jspb.Message {
  getCanSearchGradeSystems(): boolean;
  setCanSearchGradeSystems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchGradeSystemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchGradeSystemsReply): CanSearchGradeSystemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchGradeSystemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchGradeSystemsReply;
  static deserializeBinaryFromReader(message: CanSearchGradeSystemsReply, reader: jspb.BinaryReader): CanSearchGradeSystemsReply;
}

export namespace CanSearchGradeSystemsReply {
  export type AsObject = {
    canSearchGradeSystems: boolean,
  }
}

export class CanSearchGradeSystemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchGradeSystemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchGradeSystemsRequest): CanSearchGradeSystemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchGradeSystemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchGradeSystemsRequest;
  static deserializeBinaryFromReader(message: CanSearchGradeSystemsRequest, reader: jspb.BinaryReader): CanSearchGradeSystemsRequest;
}

export namespace CanSearchGradeSystemsRequest {
  export type AsObject = {
  }
}

export class GetGradeSystemQueryReply extends jspb.Message {
  hasGradeSystemQuery(): boolean;
  clearGradeSystemQuery(): void;
  getGradeSystemQuery(): GradeSystemQuery | undefined;
  setGradeSystemQuery(value?: GradeSystemQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemQueryReply): GetGradeSystemQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemQueryReply;
  static deserializeBinaryFromReader(message: GetGradeSystemQueryReply, reader: jspb.BinaryReader): GetGradeSystemQueryReply;
}

export namespace GetGradeSystemQueryReply {
  export type AsObject = {
    gradeSystemQuery?: GradeSystemQuery.AsObject,
  }
}

export class GetGradeSystemQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemQueryRequest): GetGradeSystemQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemQueryRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemQueryRequest, reader: jspb.BinaryReader): GetGradeSystemQueryRequest;
}

export namespace GetGradeSystemQueryRequest {
  export type AsObject = {
  }
}

export class GetGradeSystemsByQueryRequest extends jspb.Message {
  hasGradeSystemQuery(): boolean;
  clearGradeSystemQuery(): void;
  getGradeSystemQuery(): GradeSystemQuery | undefined;
  setGradeSystemQuery(value?: GradeSystemQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByQueryRequest): GetGradeSystemsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByQueryRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByQueryRequest, reader: jspb.BinaryReader): GetGradeSystemsByQueryRequest;
}

export namespace GetGradeSystemsByQueryRequest {
  export type AsObject = {
    gradeSystemQuery?: GradeSystemQuery.AsObject,
  }
}

export class CanCreateGradeSystemsReply extends jspb.Message {
  getCanCreateGradeSystems(): boolean;
  setCanCreateGradeSystems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeSystemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeSystemsReply): CanCreateGradeSystemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeSystemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeSystemsReply;
  static deserializeBinaryFromReader(message: CanCreateGradeSystemsReply, reader: jspb.BinaryReader): CanCreateGradeSystemsReply;
}

export namespace CanCreateGradeSystemsReply {
  export type AsObject = {
    canCreateGradeSystems: boolean,
  }
}

export class CanCreateGradeSystemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeSystemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeSystemsRequest): CanCreateGradeSystemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeSystemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeSystemsRequest;
  static deserializeBinaryFromReader(message: CanCreateGradeSystemsRequest, reader: jspb.BinaryReader): CanCreateGradeSystemsRequest;
}

export namespace CanCreateGradeSystemsRequest {
  export type AsObject = {
  }
}

export class CanCreateGradeSystemWithRecordTypesReply extends jspb.Message {
  getCanCreateGradeSystemWithRecordTypes(): boolean;
  setCanCreateGradeSystemWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeSystemWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeSystemWithRecordTypesReply): CanCreateGradeSystemWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeSystemWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeSystemWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateGradeSystemWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateGradeSystemWithRecordTypesReply;
}

export namespace CanCreateGradeSystemWithRecordTypesReply {
  export type AsObject = {
    canCreateGradeSystemWithRecordTypes: boolean,
  }
}

export class CanCreateGradeSystemWithRecordTypesRequest extends jspb.Message {
  clearGradeSystemRecordTypesList(): void;
  getGradeSystemRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeSystemRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeSystemRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeSystemWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeSystemWithRecordTypesRequest): CanCreateGradeSystemWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeSystemWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeSystemWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradeSystemWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateGradeSystemWithRecordTypesRequest;
}

export namespace CanCreateGradeSystemWithRecordTypesRequest {
  export type AsObject = {
    gradeSystemRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetGradeSystemFormForCreateReply extends jspb.Message {
  hasGradeSystemForm(): boolean;
  clearGradeSystemForm(): void;
  getGradeSystemForm(): GradeSystemForm | undefined;
  setGradeSystemForm(value?: GradeSystemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemFormForCreateReply): GetGradeSystemFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemFormForCreateReply;
  static deserializeBinaryFromReader(message: GetGradeSystemFormForCreateReply, reader: jspb.BinaryReader): GetGradeSystemFormForCreateReply;
}

export namespace GetGradeSystemFormForCreateReply {
  export type AsObject = {
    gradeSystemForm?: GradeSystemForm.AsObject,
  }
}

export class GetGradeSystemFormForCreateRequest extends jspb.Message {
  clearGradeSystemRecordTypesList(): void;
  getGradeSystemRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeSystemRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeSystemRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemFormForCreateRequest): GetGradeSystemFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemFormForCreateRequest, reader: jspb.BinaryReader): GetGradeSystemFormForCreateRequest;
}

export namespace GetGradeSystemFormForCreateRequest {
  export type AsObject = {
    gradeSystemRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateGradeSystemReply extends jspb.Message {
  hasGradeSystem(): boolean;
  clearGradeSystem(): void;
  getGradeSystem(): GradeSystem | undefined;
  setGradeSystem(value?: GradeSystem): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradeSystemReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradeSystemReply): CreateGradeSystemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradeSystemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradeSystemReply;
  static deserializeBinaryFromReader(message: CreateGradeSystemReply, reader: jspb.BinaryReader): CreateGradeSystemReply;
}

export namespace CreateGradeSystemReply {
  export type AsObject = {
    gradeSystem?: GradeSystem.AsObject,
  }
}

export class CreateGradeSystemRequest extends jspb.Message {
  hasGradeSystemForm(): boolean;
  clearGradeSystemForm(): void;
  getGradeSystemForm(): GradeSystemForm | undefined;
  setGradeSystemForm(value?: GradeSystemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradeSystemRequest): CreateGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradeSystemRequest;
  static deserializeBinaryFromReader(message: CreateGradeSystemRequest, reader: jspb.BinaryReader): CreateGradeSystemRequest;
}

export namespace CreateGradeSystemRequest {
  export type AsObject = {
    gradeSystemForm?: GradeSystemForm.AsObject,
  }
}

export class CanUpdateGradeSystemsReply extends jspb.Message {
  getCanUpdateGradeSystems(): boolean;
  setCanUpdateGradeSystems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradeSystemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradeSystemsReply): CanUpdateGradeSystemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradeSystemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradeSystemsReply;
  static deserializeBinaryFromReader(message: CanUpdateGradeSystemsReply, reader: jspb.BinaryReader): CanUpdateGradeSystemsReply;
}

export namespace CanUpdateGradeSystemsReply {
  export type AsObject = {
    canUpdateGradeSystems: boolean,
  }
}

export class CanUpdateGradeSystemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradeSystemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradeSystemsRequest): CanUpdateGradeSystemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradeSystemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradeSystemsRequest;
  static deserializeBinaryFromReader(message: CanUpdateGradeSystemsRequest, reader: jspb.BinaryReader): CanUpdateGradeSystemsRequest;
}

export namespace CanUpdateGradeSystemsRequest {
  export type AsObject = {
  }
}

export class GetGradeSystemFormForUpdateReply extends jspb.Message {
  hasGradeSystemForm(): boolean;
  clearGradeSystemForm(): void;
  getGradeSystemForm(): GradeSystemForm | undefined;
  setGradeSystemForm(value?: GradeSystemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemFormForUpdateReply): GetGradeSystemFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetGradeSystemFormForUpdateReply, reader: jspb.BinaryReader): GetGradeSystemFormForUpdateReply;
}

export namespace GetGradeSystemFormForUpdateReply {
  export type AsObject = {
    gradeSystemForm?: GradeSystemForm.AsObject,
  }
}

export class GetGradeSystemFormForUpdateRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemFormForUpdateRequest): GetGradeSystemFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemFormForUpdateRequest, reader: jspb.BinaryReader): GetGradeSystemFormForUpdateRequest;
}

export namespace GetGradeSystemFormForUpdateRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateGradeSystemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradeSystemReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradeSystemReply): UpdateGradeSystemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradeSystemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradeSystemReply;
  static deserializeBinaryFromReader(message: UpdateGradeSystemReply, reader: jspb.BinaryReader): UpdateGradeSystemReply;
}

export namespace UpdateGradeSystemReply {
  export type AsObject = {
  }
}

export class UpdateGradeSystemRequest extends jspb.Message {
  hasGradeSystemForm(): boolean;
  clearGradeSystemForm(): void;
  getGradeSystemForm(): GradeSystemForm | undefined;
  setGradeSystemForm(value?: GradeSystemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradeSystemRequest): UpdateGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradeSystemRequest;
  static deserializeBinaryFromReader(message: UpdateGradeSystemRequest, reader: jspb.BinaryReader): UpdateGradeSystemRequest;
}

export namespace UpdateGradeSystemRequest {
  export type AsObject = {
    gradeSystemForm?: GradeSystemForm.AsObject,
  }
}

export class CanDeleteGradeSystemsReply extends jspb.Message {
  getCanDeleteGradeSystems(): boolean;
  setCanDeleteGradeSystems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradeSystemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradeSystemsReply): CanDeleteGradeSystemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradeSystemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradeSystemsReply;
  static deserializeBinaryFromReader(message: CanDeleteGradeSystemsReply, reader: jspb.BinaryReader): CanDeleteGradeSystemsReply;
}

export namespace CanDeleteGradeSystemsReply {
  export type AsObject = {
    canDeleteGradeSystems: boolean,
  }
}

export class CanDeleteGradeSystemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradeSystemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradeSystemsRequest): CanDeleteGradeSystemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradeSystemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradeSystemsRequest;
  static deserializeBinaryFromReader(message: CanDeleteGradeSystemsRequest, reader: jspb.BinaryReader): CanDeleteGradeSystemsRequest;
}

export namespace CanDeleteGradeSystemsRequest {
  export type AsObject = {
  }
}

export class DeleteGradeSystemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradeSystemReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradeSystemReply): DeleteGradeSystemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradeSystemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradeSystemReply;
  static deserializeBinaryFromReader(message: DeleteGradeSystemReply, reader: jspb.BinaryReader): DeleteGradeSystemReply;
}

export namespace DeleteGradeSystemReply {
  export type AsObject = {
  }
}

export class DeleteGradeSystemRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradeSystemRequest): DeleteGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradeSystemRequest;
  static deserializeBinaryFromReader(message: DeleteGradeSystemRequest, reader: jspb.BinaryReader): DeleteGradeSystemRequest;
}

export namespace DeleteGradeSystemRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageGradeSystemAliasesReply extends jspb.Message {
  getCanManageGradeSystemAliases(): boolean;
  setCanManageGradeSystemAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradeSystemAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradeSystemAliasesReply): CanManageGradeSystemAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradeSystemAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradeSystemAliasesReply;
  static deserializeBinaryFromReader(message: CanManageGradeSystemAliasesReply, reader: jspb.BinaryReader): CanManageGradeSystemAliasesReply;
}

export namespace CanManageGradeSystemAliasesReply {
  export type AsObject = {
    canManageGradeSystemAliases: boolean,
  }
}

export class CanManageGradeSystemAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradeSystemAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradeSystemAliasesRequest): CanManageGradeSystemAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradeSystemAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradeSystemAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageGradeSystemAliasesRequest, reader: jspb.BinaryReader): CanManageGradeSystemAliasesRequest;
}

export namespace CanManageGradeSystemAliasesRequest {
  export type AsObject = {
  }
}

export class AliasGradeSystemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradeSystemReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradeSystemReply): AliasGradeSystemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradeSystemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradeSystemReply;
  static deserializeBinaryFromReader(message: AliasGradeSystemReply, reader: jspb.BinaryReader): AliasGradeSystemReply;
}

export namespace AliasGradeSystemReply {
  export type AsObject = {
  }
}

export class AliasGradeSystemRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradeSystemRequest): AliasGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradeSystemRequest;
  static deserializeBinaryFromReader(message: AliasGradeSystemRequest, reader: jspb.BinaryReader): AliasGradeSystemRequest;
}

export namespace AliasGradeSystemRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanCreateGradesReply extends jspb.Message {
  getCanCreateGrades(): boolean;
  setCanCreateGrades(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradesReply): CanCreateGradesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradesReply;
  static deserializeBinaryFromReader(message: CanCreateGradesReply, reader: jspb.BinaryReader): CanCreateGradesReply;
}

export namespace CanCreateGradesReply {
  export type AsObject = {
    canCreateGrades: boolean,
  }
}

export class CanCreateGradesRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradesRequest): CanCreateGradesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradesRequest, reader: jspb.BinaryReader): CanCreateGradesRequest;
}

export namespace CanCreateGradesRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanCreateGradeWithRecordTypesReply extends jspb.Message {
  getCanCreateGradeWithRecordTypes(): boolean;
  setCanCreateGradeWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeWithRecordTypesReply): CanCreateGradeWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateGradeWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateGradeWithRecordTypesReply;
}

export namespace CanCreateGradeWithRecordTypesReply {
  export type AsObject = {
    canCreateGradeWithRecordTypes: boolean,
  }
}

export class CanCreateGradeWithRecordTypesRequest extends jspb.Message {
  clearGradeRecordTypesList(): void;
  getGradeRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeWithRecordTypesRequest): CanCreateGradeWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradeWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateGradeWithRecordTypesRequest;
}

export namespace CanCreateGradeWithRecordTypesRequest {
  export type AsObject = {
    gradeRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeFormForCreateReply extends jspb.Message {
  hasGradeForm(): boolean;
  clearGradeForm(): void;
  getGradeForm(): GradeForm | undefined;
  setGradeForm(value?: GradeForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeFormForCreateReply): GetGradeFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeFormForCreateReply;
  static deserializeBinaryFromReader(message: GetGradeFormForCreateReply, reader: jspb.BinaryReader): GetGradeFormForCreateReply;
}

export namespace GetGradeFormForCreateReply {
  export type AsObject = {
    gradeForm?: GradeForm.AsObject,
  }
}

export class GetGradeFormForCreateRequest extends jspb.Message {
  clearGradeRecordTypesList(): void;
  getGradeRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeFormForCreateRequest): GetGradeFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetGradeFormForCreateRequest, reader: jspb.BinaryReader): GetGradeFormForCreateRequest;
}

export namespace GetGradeFormForCreateRequest {
  export type AsObject = {
    gradeRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateGradeReply extends jspb.Message {
  hasGrade(): boolean;
  clearGrade(): void;
  getGrade(): Grade | undefined;
  setGrade(value?: Grade): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradeReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradeReply): CreateGradeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradeReply;
  static deserializeBinaryFromReader(message: CreateGradeReply, reader: jspb.BinaryReader): CreateGradeReply;
}

export namespace CreateGradeReply {
  export type AsObject = {
    grade?: Grade.AsObject,
  }
}

export class CreateGradeRequest extends jspb.Message {
  hasGradeForm(): boolean;
  clearGradeForm(): void;
  getGradeForm(): GradeForm | undefined;
  setGradeForm(value?: GradeForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradeRequest): CreateGradeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradeRequest;
  static deserializeBinaryFromReader(message: CreateGradeRequest, reader: jspb.BinaryReader): CreateGradeRequest;
}

export namespace CreateGradeRequest {
  export type AsObject = {
    gradeForm?: GradeForm.AsObject,
  }
}

export class CanUpdateGradesReply extends jspb.Message {
  getCanUpdateGrades(): boolean;
  setCanUpdateGrades(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradesReply): CanUpdateGradesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradesReply;
  static deserializeBinaryFromReader(message: CanUpdateGradesReply, reader: jspb.BinaryReader): CanUpdateGradesReply;
}

export namespace CanUpdateGradesReply {
  export type AsObject = {
    canUpdateGrades: boolean,
  }
}

export class CanUpdateGradesRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradesRequest): CanUpdateGradesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradesRequest;
  static deserializeBinaryFromReader(message: CanUpdateGradesRequest, reader: jspb.BinaryReader): CanUpdateGradesRequest;
}

export namespace CanUpdateGradesRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeFormForUpdateReply extends jspb.Message {
  hasGradeForm(): boolean;
  clearGradeForm(): void;
  getGradeForm(): GradeForm | undefined;
  setGradeForm(value?: GradeForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeFormForUpdateReply): GetGradeFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetGradeFormForUpdateReply, reader: jspb.BinaryReader): GetGradeFormForUpdateReply;
}

export namespace GetGradeFormForUpdateReply {
  export type AsObject = {
    gradeForm?: GradeForm.AsObject,
  }
}

export class GetGradeFormForUpdateRequest extends jspb.Message {
  hasGradeId(): boolean;
  clearGradeId(): void;
  getGradeId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeFormForUpdateRequest): GetGradeFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetGradeFormForUpdateRequest, reader: jspb.BinaryReader): GetGradeFormForUpdateRequest;
}

export namespace GetGradeFormForUpdateRequest {
  export type AsObject = {
    gradeId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateGradeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradeReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradeReply): UpdateGradeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradeReply;
  static deserializeBinaryFromReader(message: UpdateGradeReply, reader: jspb.BinaryReader): UpdateGradeReply;
}

export namespace UpdateGradeReply {
  export type AsObject = {
  }
}

export class UpdateGradeRequest extends jspb.Message {
  hasGradeForm(): boolean;
  clearGradeForm(): void;
  getGradeForm(): GradeForm | undefined;
  setGradeForm(value?: GradeForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradeRequest): UpdateGradeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradeRequest;
  static deserializeBinaryFromReader(message: UpdateGradeRequest, reader: jspb.BinaryReader): UpdateGradeRequest;
}

export namespace UpdateGradeRequest {
  export type AsObject = {
    gradeForm?: GradeForm.AsObject,
  }
}

export class CanDeleteGradesReply extends jspb.Message {
  getCanDeleteGrades(): boolean;
  setCanDeleteGrades(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradesReply): CanDeleteGradesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradesReply;
  static deserializeBinaryFromReader(message: CanDeleteGradesReply, reader: jspb.BinaryReader): CanDeleteGradesReply;
}

export namespace CanDeleteGradesReply {
  export type AsObject = {
    canDeleteGrades: boolean,
  }
}

export class CanDeleteGradesRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradesRequest): CanDeleteGradesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradesRequest;
  static deserializeBinaryFromReader(message: CanDeleteGradesRequest, reader: jspb.BinaryReader): CanDeleteGradesRequest;
}

export namespace CanDeleteGradesRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class DeleteGradeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradeReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradeReply): DeleteGradeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradeReply;
  static deserializeBinaryFromReader(message: DeleteGradeReply, reader: jspb.BinaryReader): DeleteGradeReply;
}

export namespace DeleteGradeReply {
  export type AsObject = {
  }
}

export class DeleteGradeRequest extends jspb.Message {
  hasGradeId(): boolean;
  clearGradeId(): void;
  getGradeId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradeRequest): DeleteGradeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradeRequest;
  static deserializeBinaryFromReader(message: DeleteGradeRequest, reader: jspb.BinaryReader): DeleteGradeRequest;
}

export namespace DeleteGradeRequest {
  export type AsObject = {
    gradeId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageGradeAliasesReply extends jspb.Message {
  getCanManageGradeAliases(): boolean;
  setCanManageGradeAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradeAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradeAliasesReply): CanManageGradeAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradeAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradeAliasesReply;
  static deserializeBinaryFromReader(message: CanManageGradeAliasesReply, reader: jspb.BinaryReader): CanManageGradeAliasesReply;
}

export namespace CanManageGradeAliasesReply {
  export type AsObject = {
    canManageGradeAliases: boolean,
  }
}

export class CanManageGradeAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradeAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradeAliasesRequest): CanManageGradeAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradeAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradeAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageGradeAliasesRequest, reader: jspb.BinaryReader): CanManageGradeAliasesRequest;
}

export namespace CanManageGradeAliasesRequest {
  export type AsObject = {
  }
}

export class AliasGradeReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradeReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradeReply): AliasGradeReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradeReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradeReply;
  static deserializeBinaryFromReader(message: AliasGradeReply, reader: jspb.BinaryReader): AliasGradeReply;
}

export namespace AliasGradeReply {
  export type AsObject = {
  }
}

export class AliasGradeRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradeId(): boolean;
  clearGradeId(): void;
  getGradeId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradeRequest): AliasGradeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradeRequest;
  static deserializeBinaryFromReader(message: AliasGradeRequest, reader: jspb.BinaryReader): AliasGradeRequest;
}

export namespace AliasGradeRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradeId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UseComparativeGradebookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradebookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradebookViewReply): UseComparativeGradebookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradebookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradebookViewReply;
  static deserializeBinaryFromReader(message: UseComparativeGradebookViewReply, reader: jspb.BinaryReader): UseComparativeGradebookViewReply;
}

export namespace UseComparativeGradebookViewReply {
  export type AsObject = {
  }
}

export class UseComparativeGradebookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradebookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradebookViewRequest): UseComparativeGradebookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradebookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradebookViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeGradebookViewRequest, reader: jspb.BinaryReader): UseComparativeGradebookViewRequest;
}

export namespace UseComparativeGradebookViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryGradebookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradebookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradebookViewReply): UsePlenaryGradebookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradebookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradebookViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryGradebookViewReply, reader: jspb.BinaryReader): UsePlenaryGradebookViewReply;
}

export namespace UsePlenaryGradebookViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryGradebookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradebookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradebookViewRequest): UsePlenaryGradebookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradebookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradebookViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryGradebookViewRequest, reader: jspb.BinaryReader): UsePlenaryGradebookViewRequest;
}

export namespace UsePlenaryGradebookViewRequest {
  export type AsObject = {
  }
}

export class CanLookupGradeSystemGradebookMappingsReply extends jspb.Message {
  getCanLookupGradeSystemGradebookMappings(): boolean;
  setCanLookupGradeSystemGradebookMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradeSystemGradebookMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradeSystemGradebookMappingsReply): CanLookupGradeSystemGradebookMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradeSystemGradebookMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradeSystemGradebookMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupGradeSystemGradebookMappingsReply, reader: jspb.BinaryReader): CanLookupGradeSystemGradebookMappingsReply;
}

export namespace CanLookupGradeSystemGradebookMappingsReply {
  export type AsObject = {
    canLookupGradeSystemGradebookMappings: boolean,
  }
}

export class CanLookupGradeSystemGradebookMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradeSystemGradebookMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradeSystemGradebookMappingsRequest): CanLookupGradeSystemGradebookMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradeSystemGradebookMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradeSystemGradebookMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupGradeSystemGradebookMappingsRequest, reader: jspb.BinaryReader): CanLookupGradeSystemGradebookMappingsRequest;
}

export namespace CanLookupGradeSystemGradebookMappingsRequest {
  export type AsObject = {
  }
}

export class GetGradeSystemIdsByGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemIdsByGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemIdsByGradebookRequest): GetGradeSystemIdsByGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemIdsByGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemIdsByGradebookRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemIdsByGradebookRequest, reader: jspb.BinaryReader): GetGradeSystemIdsByGradebookRequest;
}

export namespace GetGradeSystemIdsByGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeSystemsByGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByGradebookRequest): GetGradeSystemsByGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByGradebookRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByGradebookRequest, reader: jspb.BinaryReader): GetGradeSystemsByGradebookRequest;
}

export namespace GetGradeSystemsByGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeSystemIdsByGradebooksRequest extends jspb.Message {
  clearGradebookIdsList(): void;
  getGradebookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemIdsByGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemIdsByGradebooksRequest): GetGradeSystemIdsByGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemIdsByGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemIdsByGradebooksRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemIdsByGradebooksRequest, reader: jspb.BinaryReader): GetGradeSystemIdsByGradebooksRequest;
}

export namespace GetGradeSystemIdsByGradebooksRequest {
  export type AsObject = {
    gradebookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradeSystemsByGradebooksRequest extends jspb.Message {
  clearGradebookIdsList(): void;
  getGradebookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeSystemsByGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeSystemsByGradebooksRequest): GetGradeSystemsByGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeSystemsByGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeSystemsByGradebooksRequest;
  static deserializeBinaryFromReader(message: GetGradeSystemsByGradebooksRequest, reader: jspb.BinaryReader): GetGradeSystemsByGradebooksRequest;
}

export namespace GetGradeSystemsByGradebooksRequest {
  export type AsObject = {
    gradebookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradebookIdsByGradeSystemRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookIdsByGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookIdsByGradeSystemRequest): GetGradebookIdsByGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookIdsByGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookIdsByGradeSystemRequest;
  static deserializeBinaryFromReader(message: GetGradebookIdsByGradeSystemRequest, reader: jspb.BinaryReader): GetGradebookIdsByGradeSystemRequest;
}

export namespace GetGradebookIdsByGradeSystemRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebooksByGradeSystemRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByGradeSystemRequest): GetGradebooksByGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByGradeSystemRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByGradeSystemRequest, reader: jspb.BinaryReader): GetGradebooksByGradeSystemRequest;
}

export namespace GetGradebooksByGradeSystemRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignGradeSystemReply extends jspb.Message {
  getCanAssignGradeSystem(): boolean;
  setCanAssignGradeSystem(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradeSystemReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradeSystemReply): CanAssignGradeSystemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradeSystemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradeSystemReply;
  static deserializeBinaryFromReader(message: CanAssignGradeSystemReply, reader: jspb.BinaryReader): CanAssignGradeSystemReply;
}

export namespace CanAssignGradeSystemReply {
  export type AsObject = {
    canAssignGradeSystem: boolean,
  }
}

export class CanAssignGradeSystemRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradeSystemRequest): CanAssignGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradeSystemRequest;
  static deserializeBinaryFromReader(message: CanAssignGradeSystemRequest, reader: jspb.BinaryReader): CanAssignGradeSystemRequest;
}

export namespace CanAssignGradeSystemRequest {
  export type AsObject = {
  }
}

export class CanAssignGradeSystemsToGradebookReply extends jspb.Message {
  getCanAssignGradeSystemsToGradebook(): boolean;
  setCanAssignGradeSystemsToGradebook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradeSystemsToGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradeSystemsToGradebookReply): CanAssignGradeSystemsToGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradeSystemsToGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradeSystemsToGradebookReply;
  static deserializeBinaryFromReader(message: CanAssignGradeSystemsToGradebookReply, reader: jspb.BinaryReader): CanAssignGradeSystemsToGradebookReply;
}

export namespace CanAssignGradeSystemsToGradebookReply {
  export type AsObject = {
    canAssignGradeSystemsToGradebook: boolean,
  }
}

export class CanAssignGradeSystemsToGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradeSystemsToGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradeSystemsToGradebookRequest): CanAssignGradeSystemsToGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradeSystemsToGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradeSystemsToGradebookRequest;
  static deserializeBinaryFromReader(message: CanAssignGradeSystemsToGradebookRequest, reader: jspb.BinaryReader): CanAssignGradeSystemsToGradebookRequest;
}

export namespace CanAssignGradeSystemsToGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableGradebookIdsRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableGradebookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableGradebookIdsRequest): GetAssignableGradebookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableGradebookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableGradebookIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableGradebookIdsRequest, reader: jspb.BinaryReader): GetAssignableGradebookIdsRequest;
}

export namespace GetAssignableGradebookIdsRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableGradebookIdsForGradeSystemRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableGradebookIdsForGradeSystemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableGradebookIdsForGradeSystemRequest): GetAssignableGradebookIdsForGradeSystemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableGradebookIdsForGradeSystemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableGradebookIdsForGradeSystemRequest;
  static deserializeBinaryFromReader(message: GetAssignableGradebookIdsForGradeSystemRequest, reader: jspb.BinaryReader): GetAssignableGradebookIdsForGradeSystemRequest;
}

export namespace GetAssignableGradebookIdsForGradeSystemRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignGradeSystemToGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignGradeSystemToGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignGradeSystemToGradebookReply): AssignGradeSystemToGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignGradeSystemToGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignGradeSystemToGradebookReply;
  static deserializeBinaryFromReader(message: AssignGradeSystemToGradebookReply, reader: jspb.BinaryReader): AssignGradeSystemToGradebookReply;
}

export namespace AssignGradeSystemToGradebookReply {
  export type AsObject = {
  }
}

export class AssignGradeSystemToGradebookRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignGradeSystemToGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignGradeSystemToGradebookRequest): AssignGradeSystemToGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignGradeSystemToGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignGradeSystemToGradebookRequest;
  static deserializeBinaryFromReader(message: AssignGradeSystemToGradebookRequest, reader: jspb.BinaryReader): AssignGradeSystemToGradebookRequest;
}

export namespace AssignGradeSystemToGradebookRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignGradeSystemFromGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignGradeSystemFromGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignGradeSystemFromGradebookReply): UnassignGradeSystemFromGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignGradeSystemFromGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignGradeSystemFromGradebookReply;
  static deserializeBinaryFromReader(message: UnassignGradeSystemFromGradebookReply, reader: jspb.BinaryReader): UnassignGradeSystemFromGradebookReply;
}

export namespace UnassignGradeSystemFromGradebookReply {
  export type AsObject = {
  }
}

export class UnassignGradeSystemFromGradebookRequest extends jspb.Message {
  hasGradeSystemId(): boolean;
  clearGradeSystemId(): void;
  getGradeSystemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignGradeSystemFromGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignGradeSystemFromGradebookRequest): UnassignGradeSystemFromGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignGradeSystemFromGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignGradeSystemFromGradebookRequest;
  static deserializeBinaryFromReader(message: UnassignGradeSystemFromGradebookRequest, reader: jspb.BinaryReader): UnassignGradeSystemFromGradebookRequest;
}

export namespace UnassignGradeSystemFromGradebookRequest {
  export type AsObject = {
    gradeSystemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupGradeEntriesReply extends jspb.Message {
  getCanLookupGradeEntries(): boolean;
  setCanLookupGradeEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradeEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradeEntriesReply): CanLookupGradeEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradeEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradeEntriesReply;
  static deserializeBinaryFromReader(message: CanLookupGradeEntriesReply, reader: jspb.BinaryReader): CanLookupGradeEntriesReply;
}

export namespace CanLookupGradeEntriesReply {
  export type AsObject = {
    canLookupGradeEntries: boolean,
  }
}

export class CanLookupGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradeEntriesRequest): CanLookupGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradeEntriesRequest;
  static deserializeBinaryFromReader(message: CanLookupGradeEntriesRequest, reader: jspb.BinaryReader): CanLookupGradeEntriesRequest;
}

export namespace CanLookupGradeEntriesRequest {
  export type AsObject = {
  }
}

export class UseComparativeGradeEntryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradeEntryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradeEntryViewReply): UseComparativeGradeEntryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradeEntryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradeEntryViewReply;
  static deserializeBinaryFromReader(message: UseComparativeGradeEntryViewReply, reader: jspb.BinaryReader): UseComparativeGradeEntryViewReply;
}

export namespace UseComparativeGradeEntryViewReply {
  export type AsObject = {
  }
}

export class UseComparativeGradeEntryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradeEntryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradeEntryViewRequest): UseComparativeGradeEntryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradeEntryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradeEntryViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeGradeEntryViewRequest, reader: jspb.BinaryReader): UseComparativeGradeEntryViewRequest;
}

export namespace UseComparativeGradeEntryViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryGradeEntryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradeEntryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradeEntryViewReply): UsePlenaryGradeEntryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradeEntryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradeEntryViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryGradeEntryViewReply, reader: jspb.BinaryReader): UsePlenaryGradeEntryViewReply;
}

export namespace UsePlenaryGradeEntryViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryGradeEntryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradeEntryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradeEntryViewRequest): UsePlenaryGradeEntryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradeEntryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradeEntryViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryGradeEntryViewRequest, reader: jspb.BinaryReader): UsePlenaryGradeEntryViewRequest;
}

export namespace UsePlenaryGradeEntryViewRequest {
  export type AsObject = {
  }
}

export class UseEffectiveGradeEntryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveGradeEntryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveGradeEntryViewReply): UseEffectiveGradeEntryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveGradeEntryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveGradeEntryViewReply;
  static deserializeBinaryFromReader(message: UseEffectiveGradeEntryViewReply, reader: jspb.BinaryReader): UseEffectiveGradeEntryViewReply;
}

export namespace UseEffectiveGradeEntryViewReply {
  export type AsObject = {
  }
}

export class UseEffectiveGradeEntryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveGradeEntryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveGradeEntryViewRequest): UseEffectiveGradeEntryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveGradeEntryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveGradeEntryViewRequest;
  static deserializeBinaryFromReader(message: UseEffectiveGradeEntryViewRequest, reader: jspb.BinaryReader): UseEffectiveGradeEntryViewRequest;
}

export namespace UseEffectiveGradeEntryViewRequest {
  export type AsObject = {
  }
}

export class UseAnyEffectiveGradeEntryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveGradeEntryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveGradeEntryViewReply): UseAnyEffectiveGradeEntryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveGradeEntryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveGradeEntryViewReply;
  static deserializeBinaryFromReader(message: UseAnyEffectiveGradeEntryViewReply, reader: jspb.BinaryReader): UseAnyEffectiveGradeEntryViewReply;
}

export namespace UseAnyEffectiveGradeEntryViewReply {
  export type AsObject = {
  }
}

export class UseAnyEffectiveGradeEntryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveGradeEntryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveGradeEntryViewRequest): UseAnyEffectiveGradeEntryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveGradeEntryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveGradeEntryViewRequest;
  static deserializeBinaryFromReader(message: UseAnyEffectiveGradeEntryViewRequest, reader: jspb.BinaryReader): UseAnyEffectiveGradeEntryViewRequest;
}

export namespace UseAnyEffectiveGradeEntryViewRequest {
  export type AsObject = {
  }
}

export class GetGradeEntryReply extends jspb.Message {
  hasGradeEntry(): boolean;
  clearGradeEntry(): void;
  getGradeEntry(): GradeEntry | undefined;
  setGradeEntry(value?: GradeEntry): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryReply): GetGradeEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryReply;
  static deserializeBinaryFromReader(message: GetGradeEntryReply, reader: jspb.BinaryReader): GetGradeEntryReply;
}

export namespace GetGradeEntryReply {
  export type AsObject = {
    gradeEntry?: GradeEntry.AsObject,
  }
}

export class GetGradeEntryRequest extends jspb.Message {
  hasGradeEntryId(): boolean;
  clearGradeEntryId(): void;
  getGradeEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryRequest): GetGradeEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryRequest;
  static deserializeBinaryFromReader(message: GetGradeEntryRequest, reader: jspb.BinaryReader): GetGradeEntryRequest;
}

export namespace GetGradeEntryRequest {
  export type AsObject = {
    gradeEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeEntriesByIdsRequest extends jspb.Message {
  clearGradeEntryIdsList(): void;
  getGradeEntryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradeEntryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradeEntryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesByIdsRequest): GetGradeEntriesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesByIdsRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesByIdsRequest, reader: jspb.BinaryReader): GetGradeEntriesByIdsRequest;
}

export namespace GetGradeEntriesByIdsRequest {
  export type AsObject = {
    gradeEntryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradeEntriesByGenusTypeRequest extends jspb.Message {
  hasGradeEntryGenusType(): boolean;
  clearGradeEntryGenusType(): void;
  getGradeEntryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradeEntryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesByGenusTypeRequest): GetGradeEntriesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesByGenusTypeRequest, reader: jspb.BinaryReader): GetGradeEntriesByGenusTypeRequest;
}

export namespace GetGradeEntriesByGenusTypeRequest {
  export type AsObject = {
    gradeEntryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradeEntriesByParentGenusTypeRequest extends jspb.Message {
  hasGradeEntryGenusType(): boolean;
  clearGradeEntryGenusType(): void;
  getGradeEntryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradeEntryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesByParentGenusTypeRequest): GetGradeEntriesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetGradeEntriesByParentGenusTypeRequest;
}

export namespace GetGradeEntriesByParentGenusTypeRequest {
  export type AsObject = {
    gradeEntryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradeEntriesByRecordTypeRequest extends jspb.Message {
  hasGradeEntryRecordType(): boolean;
  clearGradeEntryRecordType(): void;
  getGradeEntryRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradeEntryRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesByRecordTypeRequest): GetGradeEntriesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesByRecordTypeRequest, reader: jspb.BinaryReader): GetGradeEntriesByRecordTypeRequest;
}

export namespace GetGradeEntriesByRecordTypeRequest {
  export type AsObject = {
    gradeEntryRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradeEntriesOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesOnDateRequest): GetGradeEntriesOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesOnDateRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesOnDateRequest, reader: jspb.BinaryReader): GetGradeEntriesOnDateRequest;
}

export namespace GetGradeEntriesOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetGradeEntriesForGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesForGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesForGradebookColumnRequest): GetGradeEntriesForGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesForGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesForGradebookColumnRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesForGradebookColumnRequest, reader: jspb.BinaryReader): GetGradeEntriesForGradebookColumnRequest;
}

export namespace GetGradeEntriesForGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeEntriesForGradebookColumnOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesForGradebookColumnOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesForGradebookColumnOnDateRequest): GetGradeEntriesForGradebookColumnOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesForGradebookColumnOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesForGradebookColumnOnDateRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesForGradebookColumnOnDateRequest, reader: jspb.BinaryReader): GetGradeEntriesForGradebookColumnOnDateRequest;
}

export namespace GetGradeEntriesForGradebookColumnOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetGradeEntriesForResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesForResourceRequest): GetGradeEntriesForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesForResourceRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesForResourceRequest, reader: jspb.BinaryReader): GetGradeEntriesForResourceRequest;
}

export namespace GetGradeEntriesForResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeEntriesForResourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesForResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesForResourceOnDateRequest): GetGradeEntriesForResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesForResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesForResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesForResourceOnDateRequest, reader: jspb.BinaryReader): GetGradeEntriesForResourceOnDateRequest;
}

export namespace GetGradeEntriesForResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetGradeEntriesForGradebookColumnAndResourceRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesForGradebookColumnAndResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesForGradebookColumnAndResourceRequest): GetGradeEntriesForGradebookColumnAndResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesForGradebookColumnAndResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesForGradebookColumnAndResourceRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesForGradebookColumnAndResourceRequest, reader: jspb.BinaryReader): GetGradeEntriesForGradebookColumnAndResourceRequest;
}

export namespace GetGradeEntriesForGradebookColumnAndResourceRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeEntriesForGradebookColumnAndResourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesForGradebookColumnAndResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesForGradebookColumnAndResourceOnDateRequest): GetGradeEntriesForGradebookColumnAndResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesForGradebookColumnAndResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesForGradebookColumnAndResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesForGradebookColumnAndResourceOnDateRequest, reader: jspb.BinaryReader): GetGradeEntriesForGradebookColumnAndResourceOnDateRequest;
}

export namespace GetGradeEntriesForGradebookColumnAndResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetGradeEntriesByGraderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesByGraderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesByGraderRequest): GetGradeEntriesByGraderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesByGraderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesByGraderRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesByGraderRequest, reader: jspb.BinaryReader): GetGradeEntriesByGraderRequest;
}

export namespace GetGradeEntriesByGraderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesRequest): GetGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesRequest, reader: jspb.BinaryReader): GetGradeEntriesRequest;
}

export namespace GetGradeEntriesRequest {
  export type AsObject = {
  }
}

export class CanSearchGradeEntriesReply extends jspb.Message {
  getCanSearchGradeEntries(): boolean;
  setCanSearchGradeEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchGradeEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchGradeEntriesReply): CanSearchGradeEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchGradeEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchGradeEntriesReply;
  static deserializeBinaryFromReader(message: CanSearchGradeEntriesReply, reader: jspb.BinaryReader): CanSearchGradeEntriesReply;
}

export namespace CanSearchGradeEntriesReply {
  export type AsObject = {
    canSearchGradeEntries: boolean,
  }
}

export class CanSearchGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchGradeEntriesRequest): CanSearchGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchGradeEntriesRequest;
  static deserializeBinaryFromReader(message: CanSearchGradeEntriesRequest, reader: jspb.BinaryReader): CanSearchGradeEntriesRequest;
}

export namespace CanSearchGradeEntriesRequest {
  export type AsObject = {
  }
}

export class GetGradeEntryQueryReply extends jspb.Message {
  hasGradeEntryQuery(): boolean;
  clearGradeEntryQuery(): void;
  getGradeEntryQuery(): GradeEntryQuery | undefined;
  setGradeEntryQuery(value?: GradeEntryQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryQueryReply): GetGradeEntryQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryQueryReply;
  static deserializeBinaryFromReader(message: GetGradeEntryQueryReply, reader: jspb.BinaryReader): GetGradeEntryQueryReply;
}

export namespace GetGradeEntryQueryReply {
  export type AsObject = {
    gradeEntryQuery?: GradeEntryQuery.AsObject,
  }
}

export class GetGradeEntryQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryQueryRequest): GetGradeEntryQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryQueryRequest;
  static deserializeBinaryFromReader(message: GetGradeEntryQueryRequest, reader: jspb.BinaryReader): GetGradeEntryQueryRequest;
}

export namespace GetGradeEntryQueryRequest {
  export type AsObject = {
  }
}

export class GetGradeEntriesByQueryRequest extends jspb.Message {
  hasGradeEntryQuery(): boolean;
  clearGradeEntryQuery(): void;
  getGradeEntryQuery(): GradeEntryQuery | undefined;
  setGradeEntryQuery(value?: GradeEntryQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntriesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntriesByQueryRequest): GetGradeEntriesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntriesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntriesByQueryRequest;
  static deserializeBinaryFromReader(message: GetGradeEntriesByQueryRequest, reader: jspb.BinaryReader): GetGradeEntriesByQueryRequest;
}

export namespace GetGradeEntriesByQueryRequest {
  export type AsObject = {
    gradeEntryQuery?: GradeEntryQuery.AsObject,
  }
}

export class CanCreateGradeEntriesReply extends jspb.Message {
  getCanCreateGradeEntries(): boolean;
  setCanCreateGradeEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeEntriesReply): CanCreateGradeEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeEntriesReply;
  static deserializeBinaryFromReader(message: CanCreateGradeEntriesReply, reader: jspb.BinaryReader): CanCreateGradeEntriesReply;
}

export namespace CanCreateGradeEntriesReply {
  export type AsObject = {
    canCreateGradeEntries: boolean,
  }
}

export class CanCreateGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeEntriesRequest): CanCreateGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeEntriesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradeEntriesRequest, reader: jspb.BinaryReader): CanCreateGradeEntriesRequest;
}

export namespace CanCreateGradeEntriesRequest {
  export type AsObject = {
  }
}

export class CanCreateGradeEntryWithRecordTypesReply extends jspb.Message {
  getCanCreateGradeEntryWithRecordTypes(): boolean;
  setCanCreateGradeEntryWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeEntryWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeEntryWithRecordTypesReply): CanCreateGradeEntryWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeEntryWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeEntryWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateGradeEntryWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateGradeEntryWithRecordTypesReply;
}

export namespace CanCreateGradeEntryWithRecordTypesReply {
  export type AsObject = {
    canCreateGradeEntryWithRecordTypes: boolean,
  }
}

export class CanCreateGradeEntryWithRecordTypesRequest extends jspb.Message {
  clearGradeEntryRecordTypesList(): void;
  getGradeEntryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeEntryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeEntryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradeEntryWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradeEntryWithRecordTypesRequest): CanCreateGradeEntryWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradeEntryWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradeEntryWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradeEntryWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateGradeEntryWithRecordTypesRequest;
}

export namespace CanCreateGradeEntryWithRecordTypesRequest {
  export type AsObject = {
    gradeEntryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetGradeEntryFormForCreateReply extends jspb.Message {
  hasGradeEntryForm(): boolean;
  clearGradeEntryForm(): void;
  getGradeEntryForm(): GradeEntryForm | undefined;
  setGradeEntryForm(value?: GradeEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryFormForCreateReply): GetGradeEntryFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryFormForCreateReply;
  static deserializeBinaryFromReader(message: GetGradeEntryFormForCreateReply, reader: jspb.BinaryReader): GetGradeEntryFormForCreateReply;
}

export namespace GetGradeEntryFormForCreateReply {
  export type AsObject = {
    gradeEntryForm?: GradeEntryForm.AsObject,
  }
}

export class GetGradeEntryFormForCreateRequest extends jspb.Message {
  clearGradeEntryRecordTypesList(): void;
  getGradeEntryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeEntryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeEntryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryFormForCreateRequest): GetGradeEntryFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetGradeEntryFormForCreateRequest, reader: jspb.BinaryReader): GetGradeEntryFormForCreateRequest;
}

export namespace GetGradeEntryFormForCreateRequest {
  export type AsObject = {
    gradeEntryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateGradeEntryReply extends jspb.Message {
  hasGradeEntry(): boolean;
  clearGradeEntry(): void;
  getGradeEntry(): GradeEntry | undefined;
  setGradeEntry(value?: GradeEntry): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradeEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradeEntryReply): CreateGradeEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradeEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradeEntryReply;
  static deserializeBinaryFromReader(message: CreateGradeEntryReply, reader: jspb.BinaryReader): CreateGradeEntryReply;
}

export namespace CreateGradeEntryReply {
  export type AsObject = {
    gradeEntry?: GradeEntry.AsObject,
  }
}

export class CreateGradeEntryRequest extends jspb.Message {
  hasGradeEntryForm(): boolean;
  clearGradeEntryForm(): void;
  getGradeEntryForm(): GradeEntryForm | undefined;
  setGradeEntryForm(value?: GradeEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradeEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradeEntryRequest): CreateGradeEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradeEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradeEntryRequest;
  static deserializeBinaryFromReader(message: CreateGradeEntryRequest, reader: jspb.BinaryReader): CreateGradeEntryRequest;
}

export namespace CreateGradeEntryRequest {
  export type AsObject = {
    gradeEntryForm?: GradeEntryForm.AsObject,
  }
}

export class CanOverridecalculatedGradeEntriesReply extends jspb.Message {
  getCanOverridecalculatedGradeEntries(): boolean;
  setCanOverridecalculatedGradeEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanOverridecalculatedGradeEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanOverridecalculatedGradeEntriesReply): CanOverridecalculatedGradeEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanOverridecalculatedGradeEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanOverridecalculatedGradeEntriesReply;
  static deserializeBinaryFromReader(message: CanOverridecalculatedGradeEntriesReply, reader: jspb.BinaryReader): CanOverridecalculatedGradeEntriesReply;
}

export namespace CanOverridecalculatedGradeEntriesReply {
  export type AsObject = {
    canOverridecalculatedGradeEntries: boolean,
  }
}

export class CanOverridecalculatedGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanOverridecalculatedGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanOverridecalculatedGradeEntriesRequest): CanOverridecalculatedGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanOverridecalculatedGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanOverridecalculatedGradeEntriesRequest;
  static deserializeBinaryFromReader(message: CanOverridecalculatedGradeEntriesRequest, reader: jspb.BinaryReader): CanOverridecalculatedGradeEntriesRequest;
}

export namespace CanOverridecalculatedGradeEntriesRequest {
  export type AsObject = {
  }
}

export class GetGradeEntryFormForOverrideReply extends jspb.Message {
  hasGradeEntryForm(): boolean;
  clearGradeEntryForm(): void;
  getGradeEntryForm(): GradeEntryForm | undefined;
  setGradeEntryForm(value?: GradeEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryFormForOverrideReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryFormForOverrideReply): GetGradeEntryFormForOverrideReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryFormForOverrideReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryFormForOverrideReply;
  static deserializeBinaryFromReader(message: GetGradeEntryFormForOverrideReply, reader: jspb.BinaryReader): GetGradeEntryFormForOverrideReply;
}

export namespace GetGradeEntryFormForOverrideReply {
  export type AsObject = {
    gradeEntryForm?: GradeEntryForm.AsObject,
  }
}

export class GetGradeEntryFormForOverrideRequest extends jspb.Message {
  hasGradeEntryId(): boolean;
  clearGradeEntryId(): void;
  getGradeEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearGradeEntryRecordTypesList(): void;
  getGradeEntryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradeEntryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradeEntryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryFormForOverrideRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryFormForOverrideRequest): GetGradeEntryFormForOverrideRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryFormForOverrideRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryFormForOverrideRequest;
  static deserializeBinaryFromReader(message: GetGradeEntryFormForOverrideRequest, reader: jspb.BinaryReader): GetGradeEntryFormForOverrideRequest;
}

export namespace GetGradeEntryFormForOverrideRequest {
  export type AsObject = {
    gradeEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradeEntryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class OverrideCalculatedGradeEntryReply extends jspb.Message {
  hasGradeEntry(): boolean;
  clearGradeEntry(): void;
  getGradeEntry(): GradeEntry | undefined;
  setGradeEntry(value?: GradeEntry): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OverrideCalculatedGradeEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: OverrideCalculatedGradeEntryReply): OverrideCalculatedGradeEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OverrideCalculatedGradeEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OverrideCalculatedGradeEntryReply;
  static deserializeBinaryFromReader(message: OverrideCalculatedGradeEntryReply, reader: jspb.BinaryReader): OverrideCalculatedGradeEntryReply;
}

export namespace OverrideCalculatedGradeEntryReply {
  export type AsObject = {
    gradeEntry?: GradeEntry.AsObject,
  }
}

export class OverrideCalculatedGradeEntryRequest extends jspb.Message {
  hasGradeEntryForm(): boolean;
  clearGradeEntryForm(): void;
  getGradeEntryForm(): GradeEntryForm | undefined;
  setGradeEntryForm(value?: GradeEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OverrideCalculatedGradeEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: OverrideCalculatedGradeEntryRequest): OverrideCalculatedGradeEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OverrideCalculatedGradeEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OverrideCalculatedGradeEntryRequest;
  static deserializeBinaryFromReader(message: OverrideCalculatedGradeEntryRequest, reader: jspb.BinaryReader): OverrideCalculatedGradeEntryRequest;
}

export namespace OverrideCalculatedGradeEntryRequest {
  export type AsObject = {
    gradeEntryForm?: GradeEntryForm.AsObject,
  }
}

export class CanUpdateGradeEntriesReply extends jspb.Message {
  getCanUpdateGradeEntries(): boolean;
  setCanUpdateGradeEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradeEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradeEntriesReply): CanUpdateGradeEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradeEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradeEntriesReply;
  static deserializeBinaryFromReader(message: CanUpdateGradeEntriesReply, reader: jspb.BinaryReader): CanUpdateGradeEntriesReply;
}

export namespace CanUpdateGradeEntriesReply {
  export type AsObject = {
    canUpdateGradeEntries: boolean,
  }
}

export class CanUpdateGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradeEntriesRequest): CanUpdateGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradeEntriesRequest;
  static deserializeBinaryFromReader(message: CanUpdateGradeEntriesRequest, reader: jspb.BinaryReader): CanUpdateGradeEntriesRequest;
}

export namespace CanUpdateGradeEntriesRequest {
  export type AsObject = {
  }
}

export class GetGradeEntryFormForUpdateReply extends jspb.Message {
  hasGradeEntryForm(): boolean;
  clearGradeEntryForm(): void;
  getGradeEntryForm(): GradeEntryForm | undefined;
  setGradeEntryForm(value?: GradeEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryFormForUpdateReply): GetGradeEntryFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetGradeEntryFormForUpdateReply, reader: jspb.BinaryReader): GetGradeEntryFormForUpdateReply;
}

export namespace GetGradeEntryFormForUpdateReply {
  export type AsObject = {
    gradeEntryForm?: GradeEntryForm.AsObject,
  }
}

export class GetGradeEntryFormForUpdateRequest extends jspb.Message {
  hasGradeEntryId(): boolean;
  clearGradeEntryId(): void;
  getGradeEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradeEntryFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradeEntryFormForUpdateRequest): GetGradeEntryFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradeEntryFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradeEntryFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetGradeEntryFormForUpdateRequest, reader: jspb.BinaryReader): GetGradeEntryFormForUpdateRequest;
}

export namespace GetGradeEntryFormForUpdateRequest {
  export type AsObject = {
    gradeEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateGradeEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradeEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradeEntryReply): UpdateGradeEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradeEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradeEntryReply;
  static deserializeBinaryFromReader(message: UpdateGradeEntryReply, reader: jspb.BinaryReader): UpdateGradeEntryReply;
}

export namespace UpdateGradeEntryReply {
  export type AsObject = {
  }
}

export class UpdateGradeEntryRequest extends jspb.Message {
  hasGradeEntryForm(): boolean;
  clearGradeEntryForm(): void;
  getGradeEntryForm(): GradeEntryForm | undefined;
  setGradeEntryForm(value?: GradeEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradeEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradeEntryRequest): UpdateGradeEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradeEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradeEntryRequest;
  static deserializeBinaryFromReader(message: UpdateGradeEntryRequest, reader: jspb.BinaryReader): UpdateGradeEntryRequest;
}

export namespace UpdateGradeEntryRequest {
  export type AsObject = {
    gradeEntryForm?: GradeEntryForm.AsObject,
  }
}

export class CanDeleteGradeEntriesReply extends jspb.Message {
  getCanDeleteGradeEntries(): boolean;
  setCanDeleteGradeEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradeEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradeEntriesReply): CanDeleteGradeEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradeEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradeEntriesReply;
  static deserializeBinaryFromReader(message: CanDeleteGradeEntriesReply, reader: jspb.BinaryReader): CanDeleteGradeEntriesReply;
}

export namespace CanDeleteGradeEntriesReply {
  export type AsObject = {
    canDeleteGradeEntries: boolean,
  }
}

export class CanDeleteGradeEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradeEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradeEntriesRequest): CanDeleteGradeEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradeEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradeEntriesRequest;
  static deserializeBinaryFromReader(message: CanDeleteGradeEntriesRequest, reader: jspb.BinaryReader): CanDeleteGradeEntriesRequest;
}

export namespace CanDeleteGradeEntriesRequest {
  export type AsObject = {
  }
}

export class DeleteGradeEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradeEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradeEntryReply): DeleteGradeEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradeEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradeEntryReply;
  static deserializeBinaryFromReader(message: DeleteGradeEntryReply, reader: jspb.BinaryReader): DeleteGradeEntryReply;
}

export namespace DeleteGradeEntryReply {
  export type AsObject = {
  }
}

export class DeleteGradeEntryRequest extends jspb.Message {
  hasGradeEntryId(): boolean;
  clearGradeEntryId(): void;
  getGradeEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradeEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradeEntryRequest): DeleteGradeEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradeEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradeEntryRequest;
  static deserializeBinaryFromReader(message: DeleteGradeEntryRequest, reader: jspb.BinaryReader): DeleteGradeEntryRequest;
}

export namespace DeleteGradeEntryRequest {
  export type AsObject = {
    gradeEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageGradeEntryAliasesReply extends jspb.Message {
  getCanManageGradeEntryAliases(): boolean;
  setCanManageGradeEntryAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradeEntryAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradeEntryAliasesReply): CanManageGradeEntryAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradeEntryAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradeEntryAliasesReply;
  static deserializeBinaryFromReader(message: CanManageGradeEntryAliasesReply, reader: jspb.BinaryReader): CanManageGradeEntryAliasesReply;
}

export namespace CanManageGradeEntryAliasesReply {
  export type AsObject = {
    canManageGradeEntryAliases: boolean,
  }
}

export class CanManageGradeEntryAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradeEntryAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradeEntryAliasesRequest): CanManageGradeEntryAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradeEntryAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradeEntryAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageGradeEntryAliasesRequest, reader: jspb.BinaryReader): CanManageGradeEntryAliasesRequest;
}

export namespace CanManageGradeEntryAliasesRequest {
  export type AsObject = {
  }
}

export class AliasGradeEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradeEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradeEntryReply): AliasGradeEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradeEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradeEntryReply;
  static deserializeBinaryFromReader(message: AliasGradeEntryReply, reader: jspb.BinaryReader): AliasGradeEntryReply;
}

export namespace AliasGradeEntryReply {
  export type AsObject = {
  }
}

export class AliasGradeEntryRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradeEntryId(): boolean;
  clearGradeEntryId(): void;
  getGradeEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradeEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradeEntryRequest): AliasGradeEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradeEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradeEntryRequest;
  static deserializeBinaryFromReader(message: AliasGradeEntryRequest, reader: jspb.BinaryReader): AliasGradeEntryRequest;
}

export namespace AliasGradeEntryRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradeEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupGradebookColumnsReply extends jspb.Message {
  getCanLookupGradebookColumns(): boolean;
  setCanLookupGradebookColumns(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradebookColumnsReply): CanLookupGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradebookColumnsReply;
  static deserializeBinaryFromReader(message: CanLookupGradebookColumnsReply, reader: jspb.BinaryReader): CanLookupGradebookColumnsReply;
}

export namespace CanLookupGradebookColumnsReply {
  export type AsObject = {
    canLookupGradebookColumns: boolean,
  }
}

export class CanLookupGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradebookColumnsRequest): CanLookupGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: CanLookupGradebookColumnsRequest, reader: jspb.BinaryReader): CanLookupGradebookColumnsRequest;
}

export namespace CanLookupGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class UseComparativeGradebookColumnViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradebookColumnViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradebookColumnViewReply): UseComparativeGradebookColumnViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradebookColumnViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradebookColumnViewReply;
  static deserializeBinaryFromReader(message: UseComparativeGradebookColumnViewReply, reader: jspb.BinaryReader): UseComparativeGradebookColumnViewReply;
}

export namespace UseComparativeGradebookColumnViewReply {
  export type AsObject = {
  }
}

export class UseComparativeGradebookColumnViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeGradebookColumnViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeGradebookColumnViewRequest): UseComparativeGradebookColumnViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeGradebookColumnViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeGradebookColumnViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeGradebookColumnViewRequest, reader: jspb.BinaryReader): UseComparativeGradebookColumnViewRequest;
}

export namespace UseComparativeGradebookColumnViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryGradebookColumnViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradebookColumnViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradebookColumnViewReply): UsePlenaryGradebookColumnViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradebookColumnViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradebookColumnViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryGradebookColumnViewReply, reader: jspb.BinaryReader): UsePlenaryGradebookColumnViewReply;
}

export namespace UsePlenaryGradebookColumnViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryGradebookColumnViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryGradebookColumnViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryGradebookColumnViewRequest): UsePlenaryGradebookColumnViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryGradebookColumnViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryGradebookColumnViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryGradebookColumnViewRequest, reader: jspb.BinaryReader): UsePlenaryGradebookColumnViewRequest;
}

export namespace UsePlenaryGradebookColumnViewRequest {
  export type AsObject = {
  }
}

export class GetGradebookColumnReply extends jspb.Message {
  hasGradebookColumn(): boolean;
  clearGradebookColumn(): void;
  getGradebookColumn(): GradebookColumn | undefined;
  setGradebookColumn(value?: GradebookColumn): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnReply): GetGradebookColumnReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnReply;
  static deserializeBinaryFromReader(message: GetGradebookColumnReply, reader: jspb.BinaryReader): GetGradebookColumnReply;
}

export namespace GetGradebookColumnReply {
  export type AsObject = {
    gradebookColumn?: GradebookColumn.AsObject,
  }
}

export class GetGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnRequest): GetGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnRequest, reader: jspb.BinaryReader): GetGradebookColumnRequest;
}

export namespace GetGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookColumnsByIdsRequest extends jspb.Message {
  clearGradebookColumnIdsList(): void;
  getGradebookColumnIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookColumnIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookColumnIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByIdsRequest): GetGradebookColumnsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByIdsRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByIdsRequest, reader: jspb.BinaryReader): GetGradebookColumnsByIdsRequest;
}

export namespace GetGradebookColumnsByIdsRequest {
  export type AsObject = {
    gradebookColumnIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradebookColumnsByGenusTypeRequest extends jspb.Message {
  hasGradebookColumnGenusType(): boolean;
  clearGradebookColumnGenusType(): void;
  getGradebookColumnGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradebookColumnGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByGenusTypeRequest): GetGradebookColumnsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByGenusTypeRequest, reader: jspb.BinaryReader): GetGradebookColumnsByGenusTypeRequest;
}

export namespace GetGradebookColumnsByGenusTypeRequest {
  export type AsObject = {
    gradebookColumnGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradebookColumnsByParentGenusTypeRequest extends jspb.Message {
  hasGradebookColumnGenusType(): boolean;
  clearGradebookColumnGenusType(): void;
  getGradebookColumnGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradebookColumnGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByParentGenusTypeRequest): GetGradebookColumnsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetGradebookColumnsByParentGenusTypeRequest;
}

export namespace GetGradebookColumnsByParentGenusTypeRequest {
  export type AsObject = {
    gradebookColumnGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradebookColumnsByRecordTypeRequest extends jspb.Message {
  hasGradebookColumnRecordType(): boolean;
  clearGradebookColumnRecordType(): void;
  getGradebookColumnRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradebookColumnRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByRecordTypeRequest): GetGradebookColumnsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByRecordTypeRequest, reader: jspb.BinaryReader): GetGradebookColumnsByRecordTypeRequest;
}

export namespace GetGradebookColumnsByRecordTypeRequest {
  export type AsObject = {
    gradebookColumnRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsRequest): GetGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsRequest, reader: jspb.BinaryReader): GetGradebookColumnsRequest;
}

export namespace GetGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class SupportsSummaryReply extends jspb.Message {
  getSupportsSummary(): boolean;
  setSupportsSummary(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupportsSummaryReply.AsObject;
  static toObject(includeInstance: boolean, msg: SupportsSummaryReply): SupportsSummaryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupportsSummaryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupportsSummaryReply;
  static deserializeBinaryFromReader(message: SupportsSummaryReply, reader: jspb.BinaryReader): SupportsSummaryReply;
}

export namespace SupportsSummaryReply {
  export type AsObject = {
    supportsSummary: boolean,
  }
}

export class SupportsSummaryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupportsSummaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SupportsSummaryRequest): SupportsSummaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupportsSummaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupportsSummaryRequest;
  static deserializeBinaryFromReader(message: SupportsSummaryRequest, reader: jspb.BinaryReader): SupportsSummaryRequest;
}

export namespace SupportsSummaryRequest {
  export type AsObject = {
  }
}

export class GetGradebookColumnSummaryReply extends jspb.Message {
  hasGradebookColumnSummary(): boolean;
  clearGradebookColumnSummary(): void;
  getGradebookColumnSummary(): GradebookColumnSummary | undefined;
  setGradebookColumnSummary(value?: GradebookColumnSummary): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnSummaryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnSummaryReply): GetGradebookColumnSummaryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnSummaryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnSummaryReply;
  static deserializeBinaryFromReader(message: GetGradebookColumnSummaryReply, reader: jspb.BinaryReader): GetGradebookColumnSummaryReply;
}

export namespace GetGradebookColumnSummaryReply {
  export type AsObject = {
    gradebookColumnSummary?: GradebookColumnSummary.AsObject,
  }
}

export class GetGradebookColumnSummaryRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnSummaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnSummaryRequest): GetGradebookColumnSummaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnSummaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnSummaryRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnSummaryRequest, reader: jspb.BinaryReader): GetGradebookColumnSummaryRequest;
}

export namespace GetGradebookColumnSummaryRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanSearchGradebookColumnsReply extends jspb.Message {
  getCanSearchGradebookColumns(): boolean;
  setCanSearchGradebookColumns(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchGradebookColumnsReply): CanSearchGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchGradebookColumnsReply;
  static deserializeBinaryFromReader(message: CanSearchGradebookColumnsReply, reader: jspb.BinaryReader): CanSearchGradebookColumnsReply;
}

export namespace CanSearchGradebookColumnsReply {
  export type AsObject = {
    canSearchGradebookColumns: boolean,
  }
}

export class CanSearchGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchGradebookColumnsRequest): CanSearchGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: CanSearchGradebookColumnsRequest, reader: jspb.BinaryReader): CanSearchGradebookColumnsRequest;
}

export namespace CanSearchGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class GetGradebookColumnQueryReply extends jspb.Message {
  hasGradebookColumnQuery(): boolean;
  clearGradebookColumnQuery(): void;
  getGradebookColumnQuery(): GradebookColumnQuery | undefined;
  setGradebookColumnQuery(value?: GradebookColumnQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnQueryReply): GetGradebookColumnQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnQueryReply;
  static deserializeBinaryFromReader(message: GetGradebookColumnQueryReply, reader: jspb.BinaryReader): GetGradebookColumnQueryReply;
}

export namespace GetGradebookColumnQueryReply {
  export type AsObject = {
    gradebookColumnQuery?: GradebookColumnQuery.AsObject,
  }
}

export class GetGradebookColumnQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnQueryRequest): GetGradebookColumnQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnQueryRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnQueryRequest, reader: jspb.BinaryReader): GetGradebookColumnQueryRequest;
}

export namespace GetGradebookColumnQueryRequest {
  export type AsObject = {
  }
}

export class GetGradebookColumnsByQueryRequest extends jspb.Message {
  hasGradebookColumnQuery(): boolean;
  clearGradebookColumnQuery(): void;
  getGradebookColumnQuery(): GradebookColumnQuery | undefined;
  setGradebookColumnQuery(value?: GradebookColumnQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByQueryRequest): GetGradebookColumnsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByQueryRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByQueryRequest, reader: jspb.BinaryReader): GetGradebookColumnsByQueryRequest;
}

export namespace GetGradebookColumnsByQueryRequest {
  export type AsObject = {
    gradebookColumnQuery?: GradebookColumnQuery.AsObject,
  }
}

export class CanCreateGradebookColumnsReply extends jspb.Message {
  getCanCreateGradebookColumns(): boolean;
  setCanCreateGradebookColumns(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebookColumnsReply): CanCreateGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebookColumnsReply;
  static deserializeBinaryFromReader(message: CanCreateGradebookColumnsReply, reader: jspb.BinaryReader): CanCreateGradebookColumnsReply;
}

export namespace CanCreateGradebookColumnsReply {
  export type AsObject = {
    canCreateGradebookColumns: boolean,
  }
}

export class CanCreateGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebookColumnsRequest): CanCreateGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: CanCreateGradebookColumnsRequest, reader: jspb.BinaryReader): CanCreateGradebookColumnsRequest;
}

export namespace CanCreateGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class CanCreateGradebookColumnWithRecordTypesReply extends jspb.Message {
  getCanCreateGradebookColumnWithRecordTypes(): boolean;
  setCanCreateGradebookColumnWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebookColumnWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebookColumnWithRecordTypesReply): CanCreateGradebookColumnWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebookColumnWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebookColumnWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateGradebookColumnWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateGradebookColumnWithRecordTypesReply;
}

export namespace CanCreateGradebookColumnWithRecordTypesReply {
  export type AsObject = {
    canCreateGradebookColumnWithRecordTypes: boolean,
  }
}

export class CanCreateGradebookColumnWithRecordTypesRequest extends jspb.Message {
  clearGradebookColumnRecordTypesList(): void;
  getGradebookColumnRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradebookColumnRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradebookColumnRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebookColumnWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebookColumnWithRecordTypesRequest): CanCreateGradebookColumnWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebookColumnWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebookColumnWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradebookColumnWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateGradebookColumnWithRecordTypesRequest;
}

export namespace CanCreateGradebookColumnWithRecordTypesRequest {
  export type AsObject = {
    gradebookColumnRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetGradebookColumnFormForCreateReply extends jspb.Message {
  hasGradebookColumnForm(): boolean;
  clearGradebookColumnForm(): void;
  getGradebookColumnForm(): GradebookColumnForm | undefined;
  setGradebookColumnForm(value?: GradebookColumnForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnFormForCreateReply): GetGradebookColumnFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnFormForCreateReply;
  static deserializeBinaryFromReader(message: GetGradebookColumnFormForCreateReply, reader: jspb.BinaryReader): GetGradebookColumnFormForCreateReply;
}

export namespace GetGradebookColumnFormForCreateReply {
  export type AsObject = {
    gradebookColumnForm?: GradebookColumnForm.AsObject,
  }
}

export class GetGradebookColumnFormForCreateRequest extends jspb.Message {
  clearGradebookColumnRecordTypesList(): void;
  getGradebookColumnRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradebookColumnRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradebookColumnRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnFormForCreateRequest): GetGradebookColumnFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnFormForCreateRequest, reader: jspb.BinaryReader): GetGradebookColumnFormForCreateRequest;
}

export namespace GetGradebookColumnFormForCreateRequest {
  export type AsObject = {
    gradebookColumnRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateGradebookColumnReply extends jspb.Message {
  hasGradebookColumn(): boolean;
  clearGradebookColumn(): void;
  getGradebookColumn(): GradebookColumn | undefined;
  setGradebookColumn(value?: GradebookColumn): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradebookColumnReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradebookColumnReply): CreateGradebookColumnReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradebookColumnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradebookColumnReply;
  static deserializeBinaryFromReader(message: CreateGradebookColumnReply, reader: jspb.BinaryReader): CreateGradebookColumnReply;
}

export namespace CreateGradebookColumnReply {
  export type AsObject = {
    gradebookColumn?: GradebookColumn.AsObject,
  }
}

export class CreateGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnForm(): boolean;
  clearGradebookColumnForm(): void;
  getGradebookColumnForm(): GradebookColumnForm | undefined;
  setGradebookColumnForm(value?: GradebookColumnForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradebookColumnRequest): CreateGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradebookColumnRequest;
  static deserializeBinaryFromReader(message: CreateGradebookColumnRequest, reader: jspb.BinaryReader): CreateGradebookColumnRequest;
}

export namespace CreateGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnForm?: GradebookColumnForm.AsObject,
  }
}

export class CanUpdateGradebookColumnsReply extends jspb.Message {
  getCanUpdateGradebookColumns(): boolean;
  setCanUpdateGradebookColumns(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradebookColumnsReply): CanUpdateGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradebookColumnsReply;
  static deserializeBinaryFromReader(message: CanUpdateGradebookColumnsReply, reader: jspb.BinaryReader): CanUpdateGradebookColumnsReply;
}

export namespace CanUpdateGradebookColumnsReply {
  export type AsObject = {
    canUpdateGradebookColumns: boolean,
  }
}

export class CanUpdateGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradebookColumnsRequest): CanUpdateGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: CanUpdateGradebookColumnsRequest, reader: jspb.BinaryReader): CanUpdateGradebookColumnsRequest;
}

export namespace CanUpdateGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class GetGradebookColumnFormForUpdateReply extends jspb.Message {
  hasGradebookColumnForm(): boolean;
  clearGradebookColumnForm(): void;
  getGradebookColumnForm(): GradebookColumnForm | undefined;
  setGradebookColumnForm(value?: GradebookColumnForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnFormForUpdateReply): GetGradebookColumnFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetGradebookColumnFormForUpdateReply, reader: jspb.BinaryReader): GetGradebookColumnFormForUpdateReply;
}

export namespace GetGradebookColumnFormForUpdateReply {
  export type AsObject = {
    gradebookColumnForm?: GradebookColumnForm.AsObject,
  }
}

export class GetGradebookColumnFormForUpdateRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnFormForUpdateRequest): GetGradebookColumnFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnFormForUpdateRequest, reader: jspb.BinaryReader): GetGradebookColumnFormForUpdateRequest;
}

export namespace GetGradebookColumnFormForUpdateRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateGradebookColumnReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradebookColumnReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradebookColumnReply): UpdateGradebookColumnReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradebookColumnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradebookColumnReply;
  static deserializeBinaryFromReader(message: UpdateGradebookColumnReply, reader: jspb.BinaryReader): UpdateGradebookColumnReply;
}

export namespace UpdateGradebookColumnReply {
  export type AsObject = {
  }
}

export class UpdateGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnForm(): boolean;
  clearGradebookColumnForm(): void;
  getGradebookColumnForm(): GradebookColumnForm | undefined;
  setGradebookColumnForm(value?: GradebookColumnForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradebookColumnRequest): UpdateGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradebookColumnRequest;
  static deserializeBinaryFromReader(message: UpdateGradebookColumnRequest, reader: jspb.BinaryReader): UpdateGradebookColumnRequest;
}

export namespace UpdateGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnForm?: GradebookColumnForm.AsObject,
  }
}

export class SequenceGradebookColumnsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceGradebookColumnsReply): SequenceGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceGradebookColumnsReply;
  static deserializeBinaryFromReader(message: SequenceGradebookColumnsReply, reader: jspb.BinaryReader): SequenceGradebookColumnsReply;
}

export namespace SequenceGradebookColumnsReply {
  export type AsObject = {
  }
}

export class SequenceGradebookColumnsRequest extends jspb.Message {
  clearGradebookColumnIdsList(): void;
  getGradebookColumnIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookColumnIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookColumnIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceGradebookColumnsRequest): SequenceGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: SequenceGradebookColumnsRequest, reader: jspb.BinaryReader): SequenceGradebookColumnsRequest;
}

export namespace SequenceGradebookColumnsRequest {
  export type AsObject = {
    gradebookColumnIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class MoveGradebookColumnReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveGradebookColumnReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveGradebookColumnReply): MoveGradebookColumnReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveGradebookColumnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveGradebookColumnReply;
  static deserializeBinaryFromReader(message: MoveGradebookColumnReply, reader: jspb.BinaryReader): MoveGradebookColumnReply;
}

export namespace MoveGradebookColumnReply {
  export type AsObject = {
  }
}

export class MoveGradebookColumnRequest extends jspb.Message {
  hasBackGradebookColumnId(): boolean;
  clearBackGradebookColumnId(): void;
  getBackGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBackGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrontGradebookColumnId(): boolean;
  clearFrontGradebookColumnId(): void;
  getFrontGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFrontGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveGradebookColumnRequest): MoveGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveGradebookColumnRequest;
  static deserializeBinaryFromReader(message: MoveGradebookColumnRequest, reader: jspb.BinaryReader): MoveGradebookColumnRequest;
}

export namespace MoveGradebookColumnRequest {
  export type AsObject = {
    backGradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    frontGradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CopyGradebookColumnEntriesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CopyGradebookColumnEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CopyGradebookColumnEntriesReply): CopyGradebookColumnEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CopyGradebookColumnEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CopyGradebookColumnEntriesReply;
  static deserializeBinaryFromReader(message: CopyGradebookColumnEntriesReply, reader: jspb.BinaryReader): CopyGradebookColumnEntriesReply;
}

export namespace CopyGradebookColumnEntriesReply {
  export type AsObject = {
  }
}

export class CopyGradebookColumnEntriesRequest extends jspb.Message {
  hasSourceGradebookColumnId(): boolean;
  clearSourceGradebookColumnId(): void;
  getSourceGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSourceGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTargetGradebookColumnId(): boolean;
  clearTargetGradebookColumnId(): void;
  getTargetGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setTargetGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CopyGradebookColumnEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CopyGradebookColumnEntriesRequest): CopyGradebookColumnEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CopyGradebookColumnEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CopyGradebookColumnEntriesRequest;
  static deserializeBinaryFromReader(message: CopyGradebookColumnEntriesRequest, reader: jspb.BinaryReader): CopyGradebookColumnEntriesRequest;
}

export namespace CopyGradebookColumnEntriesRequest {
  export type AsObject = {
    sourceGradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    targetGradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanDeleteGradebookColumnsReply extends jspb.Message {
  getCanDeleteGradebookColumns(): boolean;
  setCanDeleteGradebookColumns(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradebookColumnsReply): CanDeleteGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradebookColumnsReply;
  static deserializeBinaryFromReader(message: CanDeleteGradebookColumnsReply, reader: jspb.BinaryReader): CanDeleteGradebookColumnsReply;
}

export namespace CanDeleteGradebookColumnsReply {
  export type AsObject = {
    canDeleteGradebookColumns: boolean,
  }
}

export class CanDeleteGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradebookColumnsRequest): CanDeleteGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: CanDeleteGradebookColumnsRequest, reader: jspb.BinaryReader): CanDeleteGradebookColumnsRequest;
}

export namespace CanDeleteGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class DeleteGradebookColumnReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradebookColumnReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradebookColumnReply): DeleteGradebookColumnReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradebookColumnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradebookColumnReply;
  static deserializeBinaryFromReader(message: DeleteGradebookColumnReply, reader: jspb.BinaryReader): DeleteGradebookColumnReply;
}

export namespace DeleteGradebookColumnReply {
  export type AsObject = {
  }
}

export class DeleteGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradebookColumnRequest): DeleteGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradebookColumnRequest;
  static deserializeBinaryFromReader(message: DeleteGradebookColumnRequest, reader: jspb.BinaryReader): DeleteGradebookColumnRequest;
}

export namespace DeleteGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageGradebookColumnAliasesReply extends jspb.Message {
  getCanManageGradebookColumnAliases(): boolean;
  setCanManageGradebookColumnAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradebookColumnAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradebookColumnAliasesReply): CanManageGradebookColumnAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradebookColumnAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradebookColumnAliasesReply;
  static deserializeBinaryFromReader(message: CanManageGradebookColumnAliasesReply, reader: jspb.BinaryReader): CanManageGradebookColumnAliasesReply;
}

export namespace CanManageGradebookColumnAliasesReply {
  export type AsObject = {
    canManageGradebookColumnAliases: boolean,
  }
}

export class CanManageGradebookColumnAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradebookColumnAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradebookColumnAliasesRequest): CanManageGradebookColumnAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradebookColumnAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradebookColumnAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageGradebookColumnAliasesRequest, reader: jspb.BinaryReader): CanManageGradebookColumnAliasesRequest;
}

export namespace CanManageGradebookColumnAliasesRequest {
  export type AsObject = {
  }
}

export class AliasGradebookColumnReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradebookColumnReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradebookColumnReply): AliasGradebookColumnReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradebookColumnReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradebookColumnReply;
  static deserializeBinaryFromReader(message: AliasGradebookColumnReply, reader: jspb.BinaryReader): AliasGradebookColumnReply;
}

export namespace AliasGradebookColumnReply {
  export type AsObject = {
  }
}

export class AliasGradebookColumnRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradebookColumnRequest): AliasGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradebookColumnRequest;
  static deserializeBinaryFromReader(message: AliasGradebookColumnRequest, reader: jspb.BinaryReader): AliasGradebookColumnRequest;
}

export namespace AliasGradebookColumnRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupGradebookColumnGradebookMappingsReply extends jspb.Message {
  getCanLookupGradebookColumnGradebookMappings(): boolean;
  setCanLookupGradebookColumnGradebookMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradebookColumnGradebookMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradebookColumnGradebookMappingsReply): CanLookupGradebookColumnGradebookMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradebookColumnGradebookMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradebookColumnGradebookMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupGradebookColumnGradebookMappingsReply, reader: jspb.BinaryReader): CanLookupGradebookColumnGradebookMappingsReply;
}

export namespace CanLookupGradebookColumnGradebookMappingsReply {
  export type AsObject = {
    canLookupGradebookColumnGradebookMappings: boolean,
  }
}

export class CanLookupGradebookColumnGradebookMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradebookColumnGradebookMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradebookColumnGradebookMappingsRequest): CanLookupGradebookColumnGradebookMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradebookColumnGradebookMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradebookColumnGradebookMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupGradebookColumnGradebookMappingsRequest, reader: jspb.BinaryReader): CanLookupGradebookColumnGradebookMappingsRequest;
}

export namespace CanLookupGradebookColumnGradebookMappingsRequest {
  export type AsObject = {
  }
}

export class GetGradebookColumnIdsByGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnIdsByGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnIdsByGradebookRequest): GetGradebookColumnIdsByGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnIdsByGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnIdsByGradebookRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnIdsByGradebookRequest, reader: jspb.BinaryReader): GetGradebookColumnIdsByGradebookRequest;
}

export namespace GetGradebookColumnIdsByGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookColumnsByGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByGradebookRequest): GetGradebookColumnsByGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByGradebookRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByGradebookRequest, reader: jspb.BinaryReader): GetGradebookColumnsByGradebookRequest;
}

export namespace GetGradebookColumnsByGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookColumnIdsByGradebooksRequest extends jspb.Message {
  clearGradebookIdsList(): void;
  getGradebookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnIdsByGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnIdsByGradebooksRequest): GetGradebookColumnIdsByGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnIdsByGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnIdsByGradebooksRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnIdsByGradebooksRequest, reader: jspb.BinaryReader): GetGradebookColumnIdsByGradebooksRequest;
}

export namespace GetGradebookColumnIdsByGradebooksRequest {
  export type AsObject = {
    gradebookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradebookColumnsByGradebooksRequest extends jspb.Message {
  clearGradebookIdsList(): void;
  getGradebookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookColumnsByGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookColumnsByGradebooksRequest): GetGradebookColumnsByGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookColumnsByGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookColumnsByGradebooksRequest;
  static deserializeBinaryFromReader(message: GetGradebookColumnsByGradebooksRequest, reader: jspb.BinaryReader): GetGradebookColumnsByGradebooksRequest;
}

export namespace GetGradebookColumnsByGradebooksRequest {
  export type AsObject = {
    gradebookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradebookIdsByGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookIdsByGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookIdsByGradebookColumnRequest): GetGradebookIdsByGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookIdsByGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookIdsByGradebookColumnRequest;
  static deserializeBinaryFromReader(message: GetGradebookIdsByGradebookColumnRequest, reader: jspb.BinaryReader): GetGradebookIdsByGradebookColumnRequest;
}

export namespace GetGradebookIdsByGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebooksByGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByGradebookColumnRequest): GetGradebooksByGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByGradebookColumnRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByGradebookColumnRequest, reader: jspb.BinaryReader): GetGradebooksByGradebookColumnRequest;
}

export namespace GetGradebooksByGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignGradebookColumnsReply extends jspb.Message {
  getCanAssignGradebookColumns(): boolean;
  setCanAssignGradebookColumns(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradebookColumnsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradebookColumnsReply): CanAssignGradebookColumnsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradebookColumnsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradebookColumnsReply;
  static deserializeBinaryFromReader(message: CanAssignGradebookColumnsReply, reader: jspb.BinaryReader): CanAssignGradebookColumnsReply;
}

export namespace CanAssignGradebookColumnsReply {
  export type AsObject = {
    canAssignGradebookColumns: boolean,
  }
}

export class CanAssignGradebookColumnsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradebookColumnsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradebookColumnsRequest): CanAssignGradebookColumnsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradebookColumnsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradebookColumnsRequest;
  static deserializeBinaryFromReader(message: CanAssignGradebookColumnsRequest, reader: jspb.BinaryReader): CanAssignGradebookColumnsRequest;
}

export namespace CanAssignGradebookColumnsRequest {
  export type AsObject = {
  }
}

export class CanAssignGradebookColumnsToGradebookReply extends jspb.Message {
  getCanAssignGradebookColumnsToGradebook(): boolean;
  setCanAssignGradebookColumnsToGradebook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradebookColumnsToGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradebookColumnsToGradebookReply): CanAssignGradebookColumnsToGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradebookColumnsToGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradebookColumnsToGradebookReply;
  static deserializeBinaryFromReader(message: CanAssignGradebookColumnsToGradebookReply, reader: jspb.BinaryReader): CanAssignGradebookColumnsToGradebookReply;
}

export namespace CanAssignGradebookColumnsToGradebookReply {
  export type AsObject = {
    canAssignGradebookColumnsToGradebook: boolean,
  }
}

export class CanAssignGradebookColumnsToGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignGradebookColumnsToGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignGradebookColumnsToGradebookRequest): CanAssignGradebookColumnsToGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignGradebookColumnsToGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignGradebookColumnsToGradebookRequest;
  static deserializeBinaryFromReader(message: CanAssignGradebookColumnsToGradebookRequest, reader: jspb.BinaryReader): CanAssignGradebookColumnsToGradebookRequest;
}

export namespace CanAssignGradebookColumnsToGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableGradebookIdsForGradebookColumnRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableGradebookIdsForGradebookColumnRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableGradebookIdsForGradebookColumnRequest): GetAssignableGradebookIdsForGradebookColumnRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableGradebookIdsForGradebookColumnRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableGradebookIdsForGradebookColumnRequest;
  static deserializeBinaryFromReader(message: GetAssignableGradebookIdsForGradebookColumnRequest, reader: jspb.BinaryReader): GetAssignableGradebookIdsForGradebookColumnRequest;
}

export namespace GetAssignableGradebookIdsForGradebookColumnRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignGradebookColumnToGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignGradebookColumnToGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignGradebookColumnToGradebookReply): AssignGradebookColumnToGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignGradebookColumnToGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignGradebookColumnToGradebookReply;
  static deserializeBinaryFromReader(message: AssignGradebookColumnToGradebookReply, reader: jspb.BinaryReader): AssignGradebookColumnToGradebookReply;
}

export namespace AssignGradebookColumnToGradebookReply {
  export type AsObject = {
  }
}

export class AssignGradebookColumnToGradebookRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignGradebookColumnToGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignGradebookColumnToGradebookRequest): AssignGradebookColumnToGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignGradebookColumnToGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignGradebookColumnToGradebookRequest;
  static deserializeBinaryFromReader(message: AssignGradebookColumnToGradebookRequest, reader: jspb.BinaryReader): AssignGradebookColumnToGradebookRequest;
}

export namespace AssignGradebookColumnToGradebookRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignGradebookColumnFromGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignGradebookColumnFromGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignGradebookColumnFromGradebookReply): UnassignGradebookColumnFromGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignGradebookColumnFromGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignGradebookColumnFromGradebookReply;
  static deserializeBinaryFromReader(message: UnassignGradebookColumnFromGradebookReply, reader: jspb.BinaryReader): UnassignGradebookColumnFromGradebookReply;
}

export namespace UnassignGradebookColumnFromGradebookReply {
  export type AsObject = {
  }
}

export class UnassignGradebookColumnFromGradebookRequest extends jspb.Message {
  hasGradebookColumnId(): boolean;
  clearGradebookColumnId(): void;
  getGradebookColumnId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookColumnId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignGradebookColumnFromGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignGradebookColumnFromGradebookRequest): UnassignGradebookColumnFromGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignGradebookColumnFromGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignGradebookColumnFromGradebookRequest;
  static deserializeBinaryFromReader(message: UnassignGradebookColumnFromGradebookRequest, reader: jspb.BinaryReader): UnassignGradebookColumnFromGradebookRequest;
}

export namespace UnassignGradebookColumnFromGradebookRequest {
  export type AsObject = {
    gradebookColumnId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupGradebooksReply extends jspb.Message {
  getCanLookupGradebooks(): boolean;
  setCanLookupGradebooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradebooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradebooksReply): CanLookupGradebooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradebooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradebooksReply;
  static deserializeBinaryFromReader(message: CanLookupGradebooksReply, reader: jspb.BinaryReader): CanLookupGradebooksReply;
}

export namespace CanLookupGradebooksReply {
  export type AsObject = {
    canLookupGradebooks: boolean,
  }
}

export class CanLookupGradebooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupGradebooksRequest): CanLookupGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupGradebooksRequest;
  static deserializeBinaryFromReader(message: CanLookupGradebooksRequest, reader: jspb.BinaryReader): CanLookupGradebooksRequest;
}

export namespace CanLookupGradebooksRequest {
  export type AsObject = {
  }
}

export class GetGradebooksByIdsRequest extends jspb.Message {
  clearGradebookIdsList(): void;
  getGradebookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setGradebookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addGradebookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByIdsRequest): GetGradebooksByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByIdsRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByIdsRequest, reader: jspb.BinaryReader): GetGradebooksByIdsRequest;
}

export namespace GetGradebooksByIdsRequest {
  export type AsObject = {
    gradebookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetGradebooksByGenusTypeRequest extends jspb.Message {
  hasGradebookGenusType(): boolean;
  clearGradebookGenusType(): void;
  getGradebookGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradebookGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByGenusTypeRequest): GetGradebooksByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByGenusTypeRequest, reader: jspb.BinaryReader): GetGradebooksByGenusTypeRequest;
}

export namespace GetGradebooksByGenusTypeRequest {
  export type AsObject = {
    gradebookGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradebooksByParentGenusTypeRequest extends jspb.Message {
  hasGradebookGenusType(): boolean;
  clearGradebookGenusType(): void;
  getGradebookGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradebookGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByParentGenusTypeRequest): GetGradebooksByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByParentGenusTypeRequest, reader: jspb.BinaryReader): GetGradebooksByParentGenusTypeRequest;
}

export namespace GetGradebooksByParentGenusTypeRequest {
  export type AsObject = {
    gradebookGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradebooksByRecordTypeRequest extends jspb.Message {
  hasGradebookRecordType(): boolean;
  clearGradebookRecordType(): void;
  getGradebookRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGradebookRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByRecordTypeRequest): GetGradebooksByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByRecordTypeRequest, reader: jspb.BinaryReader): GetGradebooksByRecordTypeRequest;
}

export namespace GetGradebooksByRecordTypeRequest {
  export type AsObject = {
    gradebookRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetGradebooksByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksByProviderRequest): GetGradebooksByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksByProviderRequest;
  static deserializeBinaryFromReader(message: GetGradebooksByProviderRequest, reader: jspb.BinaryReader): GetGradebooksByProviderRequest;
}

export namespace GetGradebooksByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebooksRequest): GetGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebooksRequest;
  static deserializeBinaryFromReader(message: GetGradebooksRequest, reader: jspb.BinaryReader): GetGradebooksRequest;
}

export namespace GetGradebooksRequest {
  export type AsObject = {
  }
}

export class CanCreateGradebooksReply extends jspb.Message {
  getCanCreateGradebooks(): boolean;
  setCanCreateGradebooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebooksReply): CanCreateGradebooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebooksReply;
  static deserializeBinaryFromReader(message: CanCreateGradebooksReply, reader: jspb.BinaryReader): CanCreateGradebooksReply;
}

export namespace CanCreateGradebooksReply {
  export type AsObject = {
    canCreateGradebooks: boolean,
  }
}

export class CanCreateGradebooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebooksRequest): CanCreateGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebooksRequest;
  static deserializeBinaryFromReader(message: CanCreateGradebooksRequest, reader: jspb.BinaryReader): CanCreateGradebooksRequest;
}

export namespace CanCreateGradebooksRequest {
  export type AsObject = {
  }
}

export class CanCreateGradebookWithRecordTypesReply extends jspb.Message {
  getCanCreateGradebookWithRecordTypes(): boolean;
  setCanCreateGradebookWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebookWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebookWithRecordTypesReply): CanCreateGradebookWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebookWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebookWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateGradebookWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateGradebookWithRecordTypesReply;
}

export namespace CanCreateGradebookWithRecordTypesReply {
  export type AsObject = {
    canCreateGradebookWithRecordTypes: boolean,
  }
}

export class CanCreateGradebookWithRecordTypesRequest extends jspb.Message {
  clearGradebookRecordTypesList(): void;
  getGradebookRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradebookRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradebookRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateGradebookWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateGradebookWithRecordTypesRequest): CanCreateGradebookWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateGradebookWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateGradebookWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateGradebookWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateGradebookWithRecordTypesRequest;
}

export namespace CanCreateGradebookWithRecordTypesRequest {
  export type AsObject = {
    gradebookRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetGradebookFormForCreateReply extends jspb.Message {
  hasGradebookForm(): boolean;
  clearGradebookForm(): void;
  getGradebookForm(): GradebookForm | undefined;
  setGradebookForm(value?: GradebookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookFormForCreateReply): GetGradebookFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookFormForCreateReply;
  static deserializeBinaryFromReader(message: GetGradebookFormForCreateReply, reader: jspb.BinaryReader): GetGradebookFormForCreateReply;
}

export namespace GetGradebookFormForCreateReply {
  export type AsObject = {
    gradebookForm?: GradebookForm.AsObject,
  }
}

export class GetGradebookFormForCreateRequest extends jspb.Message {
  clearGradebookRecordTypesList(): void;
  getGradebookRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setGradebookRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addGradebookRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookFormForCreateRequest): GetGradebookFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetGradebookFormForCreateRequest, reader: jspb.BinaryReader): GetGradebookFormForCreateRequest;
}

export namespace GetGradebookFormForCreateRequest {
  export type AsObject = {
    gradebookRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateGradebookReply extends jspb.Message {
  hasGradebook(): boolean;
  clearGradebook(): void;
  getGradebook(): Gradebook | undefined;
  setGradebook(value?: Gradebook): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradebookReply): CreateGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradebookReply;
  static deserializeBinaryFromReader(message: CreateGradebookReply, reader: jspb.BinaryReader): CreateGradebookReply;
}

export namespace CreateGradebookReply {
  export type AsObject = {
    gradebook?: Gradebook.AsObject,
  }
}

export class CreateGradebookRequest extends jspb.Message {
  hasGradebookForm(): boolean;
  clearGradebookForm(): void;
  getGradebookForm(): GradebookForm | undefined;
  setGradebookForm(value?: GradebookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateGradebookRequest): CreateGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateGradebookRequest;
  static deserializeBinaryFromReader(message: CreateGradebookRequest, reader: jspb.BinaryReader): CreateGradebookRequest;
}

export namespace CreateGradebookRequest {
  export type AsObject = {
    gradebookForm?: GradebookForm.AsObject,
  }
}

export class CanUpdateGradebooksReply extends jspb.Message {
  getCanUpdateGradebooks(): boolean;
  setCanUpdateGradebooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradebooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradebooksReply): CanUpdateGradebooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradebooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradebooksReply;
  static deserializeBinaryFromReader(message: CanUpdateGradebooksReply, reader: jspb.BinaryReader): CanUpdateGradebooksReply;
}

export namespace CanUpdateGradebooksReply {
  export type AsObject = {
    canUpdateGradebooks: boolean,
  }
}

export class CanUpdateGradebooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateGradebooksRequest): CanUpdateGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateGradebooksRequest;
  static deserializeBinaryFromReader(message: CanUpdateGradebooksRequest, reader: jspb.BinaryReader): CanUpdateGradebooksRequest;
}

export namespace CanUpdateGradebooksRequest {
  export type AsObject = {
  }
}

export class GetGradebookFormForUpdateReply extends jspb.Message {
  hasGradebookForm(): boolean;
  clearGradebookForm(): void;
  getGradebookForm(): GradebookForm | undefined;
  setGradebookForm(value?: GradebookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookFormForUpdateReply): GetGradebookFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetGradebookFormForUpdateReply, reader: jspb.BinaryReader): GetGradebookFormForUpdateReply;
}

export namespace GetGradebookFormForUpdateReply {
  export type AsObject = {
    gradebookForm?: GradebookForm.AsObject,
  }
}

export class GetGradebookFormForUpdateRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookFormForUpdateRequest): GetGradebookFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetGradebookFormForUpdateRequest, reader: jspb.BinaryReader): GetGradebookFormForUpdateRequest;
}

export namespace GetGradebookFormForUpdateRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradebookReply): UpdateGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradebookReply;
  static deserializeBinaryFromReader(message: UpdateGradebookReply, reader: jspb.BinaryReader): UpdateGradebookReply;
}

export namespace UpdateGradebookReply {
  export type AsObject = {
  }
}

export class UpdateGradebookRequest extends jspb.Message {
  hasGradebookForm(): boolean;
  clearGradebookForm(): void;
  getGradebookForm(): GradebookForm | undefined;
  setGradebookForm(value?: GradebookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateGradebookRequest): UpdateGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateGradebookRequest;
  static deserializeBinaryFromReader(message: UpdateGradebookRequest, reader: jspb.BinaryReader): UpdateGradebookRequest;
}

export namespace UpdateGradebookRequest {
  export type AsObject = {
    gradebookForm?: GradebookForm.AsObject,
  }
}

export class CanDeleteGradebooksReply extends jspb.Message {
  getCanDeleteGradebooks(): boolean;
  setCanDeleteGradebooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradebooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradebooksReply): CanDeleteGradebooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradebooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradebooksReply;
  static deserializeBinaryFromReader(message: CanDeleteGradebooksReply, reader: jspb.BinaryReader): CanDeleteGradebooksReply;
}

export namespace CanDeleteGradebooksReply {
  export type AsObject = {
    canDeleteGradebooks: boolean,
  }
}

export class CanDeleteGradebooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteGradebooksRequest): CanDeleteGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteGradebooksRequest;
  static deserializeBinaryFromReader(message: CanDeleteGradebooksRequest, reader: jspb.BinaryReader): CanDeleteGradebooksRequest;
}

export namespace CanDeleteGradebooksRequest {
  export type AsObject = {
  }
}

export class DeleteGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradebookReply): DeleteGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradebookReply;
  static deserializeBinaryFromReader(message: DeleteGradebookReply, reader: jspb.BinaryReader): DeleteGradebookReply;
}

export namespace DeleteGradebookReply {
  export type AsObject = {
  }
}

export class DeleteGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteGradebookRequest): DeleteGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteGradebookRequest;
  static deserializeBinaryFromReader(message: DeleteGradebookRequest, reader: jspb.BinaryReader): DeleteGradebookRequest;
}

export namespace DeleteGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageGradebookAliasesReply extends jspb.Message {
  getCanManageGradebookAliases(): boolean;
  setCanManageGradebookAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradebookAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradebookAliasesReply): CanManageGradebookAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradebookAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradebookAliasesReply;
  static deserializeBinaryFromReader(message: CanManageGradebookAliasesReply, reader: jspb.BinaryReader): CanManageGradebookAliasesReply;
}

export namespace CanManageGradebookAliasesReply {
  export type AsObject = {
    canManageGradebookAliases: boolean,
  }
}

export class CanManageGradebookAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageGradebookAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageGradebookAliasesRequest): CanManageGradebookAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageGradebookAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageGradebookAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageGradebookAliasesRequest, reader: jspb.BinaryReader): CanManageGradebookAliasesRequest;
}

export namespace CanManageGradebookAliasesRequest {
  export type AsObject = {
  }
}

export class AliasGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradebookReply): AliasGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradebookReply;
  static deserializeBinaryFromReader(message: AliasGradebookReply, reader: jspb.BinaryReader): AliasGradebookReply;
}

export namespace AliasGradebookReply {
  export type AsObject = {
  }
}

export class AliasGradebookRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasGradebookRequest): AliasGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasGradebookRequest;
  static deserializeBinaryFromReader(message: AliasGradebookRequest, reader: jspb.BinaryReader): AliasGradebookRequest;
}

export namespace AliasGradebookRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookHierarchyIdReply): GetGradebookHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetGradebookHierarchyIdReply, reader: jspb.BinaryReader): GetGradebookHierarchyIdReply;
}

export namespace GetGradebookHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookHierarchyIdRequest): GetGradebookHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetGradebookHierarchyIdRequest, reader: jspb.BinaryReader): GetGradebookHierarchyIdRequest;
}

export namespace GetGradebookHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetGradebookHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookHierarchyReply): GetGradebookHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookHierarchyReply;
  static deserializeBinaryFromReader(message: GetGradebookHierarchyReply, reader: jspb.BinaryReader): GetGradebookHierarchyReply;
}

export namespace GetGradebookHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetGradebookHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookHierarchyRequest): GetGradebookHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookHierarchyRequest;
  static deserializeBinaryFromReader(message: GetGradebookHierarchyRequest, reader: jspb.BinaryReader): GetGradebookHierarchyRequest;
}

export namespace GetGradebookHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessGradebookHierarchyReply extends jspb.Message {
  getCanAccessGradebookHierarchy(): boolean;
  setCanAccessGradebookHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessGradebookHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessGradebookHierarchyReply): CanAccessGradebookHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessGradebookHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessGradebookHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessGradebookHierarchyReply, reader: jspb.BinaryReader): CanAccessGradebookHierarchyReply;
}

export namespace CanAccessGradebookHierarchyReply {
  export type AsObject = {
    canAccessGradebookHierarchy: boolean,
  }
}

export class CanAccessGradebookHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessGradebookHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessGradebookHierarchyRequest): CanAccessGradebookHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessGradebookHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessGradebookHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessGradebookHierarchyRequest, reader: jspb.BinaryReader): CanAccessGradebookHierarchyRequest;
}

export namespace CanAccessGradebookHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootGradebookIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootGradebookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootGradebookIdsRequest): GetRootGradebookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootGradebookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootGradebookIdsRequest;
  static deserializeBinaryFromReader(message: GetRootGradebookIdsRequest, reader: jspb.BinaryReader): GetRootGradebookIdsRequest;
}

export namespace GetRootGradebookIdsRequest {
  export type AsObject = {
  }
}

export class GetRootGradebooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootGradebooksRequest): GetRootGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootGradebooksRequest;
  static deserializeBinaryFromReader(message: GetRootGradebooksRequest, reader: jspb.BinaryReader): GetRootGradebooksRequest;
}

export namespace GetRootGradebooksRequest {
  export type AsObject = {
  }
}

export class HasParentGradebooksReply extends jspb.Message {
  getHasParentGradebooks(): boolean;
  setHasParentGradebooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentGradebooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentGradebooksReply): HasParentGradebooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentGradebooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentGradebooksReply;
  static deserializeBinaryFromReader(message: HasParentGradebooksReply, reader: jspb.BinaryReader): HasParentGradebooksReply;
}

export namespace HasParentGradebooksReply {
  export type AsObject = {
    hasParentGradebooks: boolean,
  }
}

export class HasParentGradebooksRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentGradebooksRequest): HasParentGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentGradebooksRequest;
  static deserializeBinaryFromReader(message: HasParentGradebooksRequest, reader: jspb.BinaryReader): HasParentGradebooksRequest;
}

export namespace HasParentGradebooksRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfGradebookReply extends jspb.Message {
  getIsParentOfGradebook(): boolean;
  setIsParentOfGradebook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfGradebookReply): IsParentOfGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfGradebookReply;
  static deserializeBinaryFromReader(message: IsParentOfGradebookReply, reader: jspb.BinaryReader): IsParentOfGradebookReply;
}

export namespace IsParentOfGradebookReply {
  export type AsObject = {
    isParentOfGradebook: boolean,
  }
}

export class IsParentOfGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfGradebookRequest): IsParentOfGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfGradebookRequest;
  static deserializeBinaryFromReader(message: IsParentOfGradebookRequest, reader: jspb.BinaryReader): IsParentOfGradebookRequest;
}

export namespace IsParentOfGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentGradebookIdsRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentGradebookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentGradebookIdsRequest): GetParentGradebookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentGradebookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentGradebookIdsRequest;
  static deserializeBinaryFromReader(message: GetParentGradebookIdsRequest, reader: jspb.BinaryReader): GetParentGradebookIdsRequest;
}

export namespace GetParentGradebookIdsRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentGradebooksRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentGradebooksRequest): GetParentGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentGradebooksRequest;
  static deserializeBinaryFromReader(message: GetParentGradebooksRequest, reader: jspb.BinaryReader): GetParentGradebooksRequest;
}

export namespace GetParentGradebooksRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfGradebookReply extends jspb.Message {
  getIsAncestorOfGradebook(): boolean;
  setIsAncestorOfGradebook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfGradebookReply): IsAncestorOfGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfGradebookReply;
  static deserializeBinaryFromReader(message: IsAncestorOfGradebookReply, reader: jspb.BinaryReader): IsAncestorOfGradebookReply;
}

export namespace IsAncestorOfGradebookReply {
  export type AsObject = {
    isAncestorOfGradebook: boolean,
  }
}

export class IsAncestorOfGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfGradebookRequest): IsAncestorOfGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfGradebookRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfGradebookRequest, reader: jspb.BinaryReader): IsAncestorOfGradebookRequest;
}

export namespace IsAncestorOfGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildGradebooksReply extends jspb.Message {
  getHasChildGradebooks(): boolean;
  setHasChildGradebooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildGradebooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildGradebooksReply): HasChildGradebooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildGradebooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildGradebooksReply;
  static deserializeBinaryFromReader(message: HasChildGradebooksReply, reader: jspb.BinaryReader): HasChildGradebooksReply;
}

export namespace HasChildGradebooksReply {
  export type AsObject = {
    hasChildGradebooks: boolean,
  }
}

export class HasChildGradebooksRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildGradebooksRequest): HasChildGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildGradebooksRequest;
  static deserializeBinaryFromReader(message: HasChildGradebooksRequest, reader: jspb.BinaryReader): HasChildGradebooksRequest;
}

export namespace HasChildGradebooksRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfGradebookReply extends jspb.Message {
  getIsChildOfGradebook(): boolean;
  setIsChildOfGradebook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfGradebookReply): IsChildOfGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfGradebookReply;
  static deserializeBinaryFromReader(message: IsChildOfGradebookReply, reader: jspb.BinaryReader): IsChildOfGradebookReply;
}

export namespace IsChildOfGradebookReply {
  export type AsObject = {
    isChildOfGradebook: boolean,
  }
}

export class IsChildOfGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfGradebookRequest): IsChildOfGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfGradebookRequest;
  static deserializeBinaryFromReader(message: IsChildOfGradebookRequest, reader: jspb.BinaryReader): IsChildOfGradebookRequest;
}

export namespace IsChildOfGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildGradebookIdsRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildGradebookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildGradebookIdsRequest): GetChildGradebookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildGradebookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildGradebookIdsRequest;
  static deserializeBinaryFromReader(message: GetChildGradebookIdsRequest, reader: jspb.BinaryReader): GetChildGradebookIdsRequest;
}

export namespace GetChildGradebookIdsRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildGradebooksRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildGradebooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildGradebooksRequest): GetChildGradebooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildGradebooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildGradebooksRequest;
  static deserializeBinaryFromReader(message: GetChildGradebooksRequest, reader: jspb.BinaryReader): GetChildGradebooksRequest;
}

export namespace GetChildGradebooksRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfGradebookReply extends jspb.Message {
  getIsDescendantOfGradebook(): boolean;
  setIsDescendantOfGradebook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfGradebookReply): IsDescendantOfGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfGradebookReply;
  static deserializeBinaryFromReader(message: IsDescendantOfGradebookReply, reader: jspb.BinaryReader): IsDescendantOfGradebookReply;
}

export namespace IsDescendantOfGradebookReply {
  export type AsObject = {
    isDescendantOfGradebook: boolean,
  }
}

export class IsDescendantOfGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfGradebookRequest): IsDescendantOfGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfGradebookRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfGradebookRequest, reader: jspb.BinaryReader): IsDescendantOfGradebookRequest;
}

export namespace IsDescendantOfGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradebookNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookNodeIdsReply): GetGradebookNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookNodeIdsReply;
  static deserializeBinaryFromReader(message: GetGradebookNodeIdsReply, reader: jspb.BinaryReader): GetGradebookNodeIdsReply;
}

export namespace GetGradebookNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetGradebookNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookNodeIdsRequest): GetGradebookNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetGradebookNodeIdsRequest, reader: jspb.BinaryReader): GetGradebookNodeIdsRequest;
}

export namespace GetGradebookNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    includeSiblings: boolean,
  }
}

export class GetGradebookNodesReply extends jspb.Message {
  hasGradebookNode(): boolean;
  clearGradebookNode(): void;
  getGradebookNode(): GradebookNode | undefined;
  setGradebookNode(value?: GradebookNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookNodesReply): GetGradebookNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookNodesReply;
  static deserializeBinaryFromReader(message: GetGradebookNodesReply, reader: jspb.BinaryReader): GetGradebookNodesReply;
}

export namespace GetGradebookNodesReply {
  export type AsObject = {
    gradebookNode?: GradebookNode.AsObject,
  }
}

export class GetGradebookNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGradebookNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGradebookNodesRequest): GetGradebookNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGradebookNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGradebookNodesRequest;
  static deserializeBinaryFromReader(message: GetGradebookNodesRequest, reader: jspb.BinaryReader): GetGradebookNodesRequest;
}

export namespace GetGradebookNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    includeSiblings: boolean,
  }
}

export class CanModifyGradebookHierarchyReply extends jspb.Message {
  getCanModifyGradebookHierarchy(): boolean;
  setCanModifyGradebookHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyGradebookHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyGradebookHierarchyReply): CanModifyGradebookHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyGradebookHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyGradebookHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyGradebookHierarchyReply, reader: jspb.BinaryReader): CanModifyGradebookHierarchyReply;
}

export namespace CanModifyGradebookHierarchyReply {
  export type AsObject = {
    canModifyGradebookHierarchy: boolean,
  }
}

export class CanModifyGradebookHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyGradebookHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyGradebookHierarchyRequest): CanModifyGradebookHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyGradebookHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyGradebookHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyGradebookHierarchyRequest, reader: jspb.BinaryReader): CanModifyGradebookHierarchyRequest;
}

export namespace CanModifyGradebookHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootGradebookReply): AddRootGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootGradebookReply;
  static deserializeBinaryFromReader(message: AddRootGradebookReply, reader: jspb.BinaryReader): AddRootGradebookReply;
}

export namespace AddRootGradebookReply {
  export type AsObject = {
  }
}

export class AddRootGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootGradebookRequest): AddRootGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootGradebookRequest;
  static deserializeBinaryFromReader(message: AddRootGradebookRequest, reader: jspb.BinaryReader): AddRootGradebookRequest;
}

export namespace AddRootGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootGradebookReply): RemoveRootGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootGradebookReply;
  static deserializeBinaryFromReader(message: RemoveRootGradebookReply, reader: jspb.BinaryReader): RemoveRootGradebookReply;
}

export namespace RemoveRootGradebookReply {
  export type AsObject = {
  }
}

export class RemoveRootGradebookRequest extends jspb.Message {
  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootGradebookRequest): RemoveRootGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootGradebookRequest;
  static deserializeBinaryFromReader(message: RemoveRootGradebookRequest, reader: jspb.BinaryReader): RemoveRootGradebookRequest;
}

export namespace RemoveRootGradebookRequest {
  export type AsObject = {
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildGradebookReply): AddChildGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildGradebookReply;
  static deserializeBinaryFromReader(message: AddChildGradebookReply, reader: jspb.BinaryReader): AddChildGradebookReply;
}

export namespace AddChildGradebookReply {
  export type AsObject = {
  }
}

export class AddChildGradebookRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildGradebookRequest): AddChildGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildGradebookRequest;
  static deserializeBinaryFromReader(message: AddChildGradebookRequest, reader: jspb.BinaryReader): AddChildGradebookRequest;
}

export namespace AddChildGradebookRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildGradebookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildGradebookReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildGradebookReply): RemoveChildGradebookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildGradebookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildGradebookReply;
  static deserializeBinaryFromReader(message: RemoveChildGradebookReply, reader: jspb.BinaryReader): RemoveChildGradebookReply;
}

export namespace RemoveChildGradebookReply {
  export type AsObject = {
  }
}

export class RemoveChildGradebookRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasGradebookId(): boolean;
  clearGradebookId(): void;
  getGradebookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradebookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildGradebookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildGradebookRequest): RemoveChildGradebookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildGradebookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildGradebookRequest;
  static deserializeBinaryFromReader(message: RemoveChildGradebookRequest, reader: jspb.BinaryReader): RemoveChildGradebookRequest;
}

export namespace RemoveChildGradebookRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    gradebookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

