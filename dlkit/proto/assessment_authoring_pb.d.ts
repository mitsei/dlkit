// package: dlkit.proto.assessment_authoring
// file: dlkit/proto/assessment_authoring.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_calendaring_primitives_pb from "../../dlkit/primordium/calendaring/primitives_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_assessment_pb from "../../dlkit/proto/assessment_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";

export class AssessmentPart extends jspb.Message {
  hasAllocatedTime(): boolean;
  clearAllocatedTime(): void;
  getAllocatedTime(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setAllocatedTime(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasAssessment(): boolean;
  clearAssessment(): void;
  getAssessment(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessment(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAssessmentPart(): boolean;
  clearAssessmentPart(): void;
  getAssessmentPart(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPart(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBank(): boolean;
  clearBank(): void;
  getBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

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

  getWeight(): number;
  setWeight(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPart.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPart): AssessmentPart.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPart, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPart;
  static deserializeBinaryFromReader(message: AssessmentPart, reader: jspb.BinaryReader): AssessmentPart;
}

export namespace AssessmentPart {
  export type AsObject = {
    allocatedTime?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    assessment?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentPart?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    weight: number,
  }
}

export class AssessmentPartQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartQuery): AssessmentPartQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartQuery;
  static deserializeBinaryFromReader(message: AssessmentPartQuery, reader: jspb.BinaryReader): AssessmentPartQuery;
}

export namespace AssessmentPartQuery {
  export type AsObject = {
  }
}

export class AssessmentPartQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartQueryInspector): AssessmentPartQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartQueryInspector;
  static deserializeBinaryFromReader(message: AssessmentPartQueryInspector, reader: jspb.BinaryReader): AssessmentPartQueryInspector;
}

export namespace AssessmentPartQueryInspector {
  export type AsObject = {
  }
}

export class AssessmentPartForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartForm.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartForm): AssessmentPartForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartForm;
  static deserializeBinaryFromReader(message: AssessmentPartForm, reader: jspb.BinaryReader): AssessmentPartForm;
}

export namespace AssessmentPartForm {
  export type AsObject = {
  }
}

export class AssessmentPartSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartSearchOrder): AssessmentPartSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartSearchOrder;
  static deserializeBinaryFromReader(message: AssessmentPartSearchOrder, reader: jspb.BinaryReader): AssessmentPartSearchOrder;
}

export namespace AssessmentPartSearchOrder {
  export type AsObject = {
  }
}

export class AssessmentPartSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartSearch): AssessmentPartSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartSearch;
  static deserializeBinaryFromReader(message: AssessmentPartSearch, reader: jspb.BinaryReader): AssessmentPartSearch;
}

export namespace AssessmentPartSearch {
  export type AsObject = {
  }
}

export class AssessmentPartSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartSearchResults): AssessmentPartSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartSearchResults;
  static deserializeBinaryFromReader(message: AssessmentPartSearchResults, reader: jspb.BinaryReader): AssessmentPartSearchResults;
}

export namespace AssessmentPartSearchResults {
  export type AsObject = {
  }
}

export class AssessmentPartList extends jspb.Message {
  clearAssessmentPartsList(): void;
  getAssessmentPartsList(): Array<AssessmentPart>;
  setAssessmentPartsList(value: Array<AssessmentPart>): void;
  addAssessmentParts(value?: AssessmentPart, index?: number): AssessmentPart;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentPartList.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentPartList): AssessmentPartList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentPartList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentPartList;
  static deserializeBinaryFromReader(message: AssessmentPartList, reader: jspb.BinaryReader): AssessmentPartList;
}

export namespace AssessmentPartList {
  export type AsObject = {
    assessmentPartsList: Array<AssessmentPart.AsObject>,
  }
}

export class SequenceRule extends jspb.Message {
  hasAssessmentPart(): boolean;
  clearAssessmentPart(): void;
  getAssessmentPart(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPart(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBank(): boolean;
  clearBank(): void;
  getBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  getCumulative(): boolean;
  setCumulative(value: boolean): void;

  getMaximumScore(): number;
  setMaximumScore(value: number): void;

  getMinimumScore(): number;
  setMinimumScore(value: number): void;

  hasNextAssessmentPart(): boolean;
  clearNextAssessmentPart(): void;
  getNextAssessmentPart(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNextAssessmentPart(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRule.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRule): SequenceRule.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRule, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRule;
  static deserializeBinaryFromReader(message: SequenceRule, reader: jspb.BinaryReader): SequenceRule;
}

export namespace SequenceRule {
  export type AsObject = {
    assessmentPart?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    cumulative: boolean,
    maximumScore: number,
    minimumScore: number,
    nextAssessmentPart?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class SequenceRuleQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleQuery.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleQuery): SequenceRuleQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleQuery;
  static deserializeBinaryFromReader(message: SequenceRuleQuery, reader: jspb.BinaryReader): SequenceRuleQuery;
}

export namespace SequenceRuleQuery {
  export type AsObject = {
  }
}

export class SequenceRuleQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleQueryInspector): SequenceRuleQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleQueryInspector;
  static deserializeBinaryFromReader(message: SequenceRuleQueryInspector, reader: jspb.BinaryReader): SequenceRuleQueryInspector;
}

export namespace SequenceRuleQueryInspector {
  export type AsObject = {
  }
}

export class SequenceRuleForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleForm.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleForm): SequenceRuleForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleForm;
  static deserializeBinaryFromReader(message: SequenceRuleForm, reader: jspb.BinaryReader): SequenceRuleForm;
}

export namespace SequenceRuleForm {
  export type AsObject = {
  }
}

export class SequenceRuleSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleSearchOrder): SequenceRuleSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleSearchOrder;
  static deserializeBinaryFromReader(message: SequenceRuleSearchOrder, reader: jspb.BinaryReader): SequenceRuleSearchOrder;
}

export namespace SequenceRuleSearchOrder {
  export type AsObject = {
  }
}

export class SequenceRuleSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleSearch.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleSearch): SequenceRuleSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleSearch;
  static deserializeBinaryFromReader(message: SequenceRuleSearch, reader: jspb.BinaryReader): SequenceRuleSearch;
}

export namespace SequenceRuleSearch {
  export type AsObject = {
  }
}

export class SequenceRuleSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleSearchResults): SequenceRuleSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleSearchResults;
  static deserializeBinaryFromReader(message: SequenceRuleSearchResults, reader: jspb.BinaryReader): SequenceRuleSearchResults;
}

export namespace SequenceRuleSearchResults {
  export type AsObject = {
  }
}

export class SequenceRuleList extends jspb.Message {
  clearSequenceRulesList(): void;
  getSequenceRulesList(): Array<SequenceRule>;
  setSequenceRulesList(value: Array<SequenceRule>): void;
  addSequenceRules(value?: SequenceRule, index?: number): SequenceRule;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleList.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleList): SequenceRuleList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleList;
  static deserializeBinaryFromReader(message: SequenceRuleList, reader: jspb.BinaryReader): SequenceRuleList;
}

export namespace SequenceRuleList {
  export type AsObject = {
    sequenceRulesList: Array<SequenceRule.AsObject>,
  }
}

export class SequenceRuleEnabler extends jspb.Message {
  hasBank(): boolean;
  clearBank(): void;
  getBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnabler.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnabler): SequenceRuleEnabler.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnabler, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnabler;
  static deserializeBinaryFromReader(message: SequenceRuleEnabler, reader: jspb.BinaryReader): SequenceRuleEnabler;
}

export namespace SequenceRuleEnabler {
  export type AsObject = {
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
  }
}

export class SequenceRuleEnablerQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerQuery.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerQuery): SequenceRuleEnablerQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerQuery;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerQuery, reader: jspb.BinaryReader): SequenceRuleEnablerQuery;
}

export namespace SequenceRuleEnablerQuery {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerQueryInspector): SequenceRuleEnablerQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerQueryInspector;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerQueryInspector, reader: jspb.BinaryReader): SequenceRuleEnablerQueryInspector;
}

export namespace SequenceRuleEnablerQueryInspector {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerForm.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerForm): SequenceRuleEnablerForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerForm;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerForm, reader: jspb.BinaryReader): SequenceRuleEnablerForm;
}

export namespace SequenceRuleEnablerForm {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerFormRecord extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerFormRecord.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerFormRecord): SequenceRuleEnablerFormRecord.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerFormRecord, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerFormRecord;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerFormRecord, reader: jspb.BinaryReader): SequenceRuleEnablerFormRecord;
}

export namespace SequenceRuleEnablerFormRecord {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerSearchOrder): SequenceRuleEnablerSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerSearchOrder;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerSearchOrder, reader: jspb.BinaryReader): SequenceRuleEnablerSearchOrder;
}

export namespace SequenceRuleEnablerSearchOrder {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerSearch.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerSearch): SequenceRuleEnablerSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerSearch;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerSearch, reader: jspb.BinaryReader): SequenceRuleEnablerSearch;
}

export namespace SequenceRuleEnablerSearch {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerSearchResults): SequenceRuleEnablerSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerSearchResults;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerSearchResults, reader: jspb.BinaryReader): SequenceRuleEnablerSearchResults;
}

export namespace SequenceRuleEnablerSearchResults {
  export type AsObject = {
  }
}

export class SequenceRuleEnablerList extends jspb.Message {
  clearSequenceRuleEnablersList(): void;
  getSequenceRuleEnablersList(): Array<SequenceRuleEnabler>;
  setSequenceRuleEnablersList(value: Array<SequenceRuleEnabler>): void;
  addSequenceRuleEnablers(value?: SequenceRuleEnabler, index?: number): SequenceRuleEnabler;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceRuleEnablerList.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceRuleEnablerList): SequenceRuleEnablerList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceRuleEnablerList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceRuleEnablerList;
  static deserializeBinaryFromReader(message: SequenceRuleEnablerList, reader: jspb.BinaryReader): SequenceRuleEnablerList;
}

export namespace SequenceRuleEnablerList {
  export type AsObject = {
    sequenceRuleEnablersList: Array<SequenceRuleEnabler.AsObject>,
  }
}

export class GetBankIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdReply): GetBankIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdReply;
  static deserializeBinaryFromReader(message: GetBankIdReply, reader: jspb.BinaryReader): GetBankIdReply;
}

export namespace GetBankIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBankIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdRequest): GetBankIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdRequest;
  static deserializeBinaryFromReader(message: GetBankIdRequest, reader: jspb.BinaryReader): GetBankIdRequest;
}

export namespace GetBankIdRequest {
  export type AsObject = {
  }
}

export class GetBankReply extends jspb.Message {
  hasBank(): boolean;
  clearBank(): void;
  getBank(): dlkit_proto_assessment_pb.Bank | undefined;
  setBank(value?: dlkit_proto_assessment_pb.Bank): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankReply): GetBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankReply;
  static deserializeBinaryFromReader(message: GetBankReply, reader: jspb.BinaryReader): GetBankReply;
}

export namespace GetBankReply {
  export type AsObject = {
    bank?: dlkit_proto_assessment_pb.Bank.AsObject,
  }
}

export class GetBankRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankRequest): GetBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankRequest;
  static deserializeBinaryFromReader(message: GetBankRequest, reader: jspb.BinaryReader): GetBankRequest;
}

export namespace GetBankRequest {
  export type AsObject = {
  }
}

export class CanLookupAssessmentPartsReply extends jspb.Message {
  getCanLookupAssessmentParts(): boolean;
  setCanLookupAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentPartsReply): CanLookupAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentPartsReply, reader: jspb.BinaryReader): CanLookupAssessmentPartsReply;
}

export namespace CanLookupAssessmentPartsReply {
  export type AsObject = {
    canLookupAssessmentParts: boolean,
  }
}

export class CanLookupAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentPartsRequest): CanLookupAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentPartsRequest, reader: jspb.BinaryReader): CanLookupAssessmentPartsRequest;
}

export namespace CanLookupAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentPartViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentPartViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentPartViewReply): UseComparativeAssessmentPartViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentPartViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentPartViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentPartViewReply, reader: jspb.BinaryReader): UseComparativeAssessmentPartViewReply;
}

export namespace UseComparativeAssessmentPartViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentPartViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentPartViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentPartViewRequest): UseComparativeAssessmentPartViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentPartViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentPartViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentPartViewRequest, reader: jspb.BinaryReader): UseComparativeAssessmentPartViewRequest;
}

export namespace UseComparativeAssessmentPartViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentPartViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentPartViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentPartViewReply): UsePlenaryAssessmentPartViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentPartViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentPartViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentPartViewReply, reader: jspb.BinaryReader): UsePlenaryAssessmentPartViewReply;
}

export namespace UsePlenaryAssessmentPartViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentPartViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentPartViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentPartViewRequest): UsePlenaryAssessmentPartViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentPartViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentPartViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentPartViewRequest, reader: jspb.BinaryReader): UsePlenaryAssessmentPartViewRequest;
}

export namespace UsePlenaryAssessmentPartViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedBankViewReply): UseFederatedBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedBankViewReply;
  static deserializeBinaryFromReader(message: UseFederatedBankViewReply, reader: jspb.BinaryReader): UseFederatedBankViewReply;
}

export namespace UseFederatedBankViewReply {
  export type AsObject = {
  }
}

export class UseFederatedBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedBankViewRequest): UseFederatedBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedBankViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedBankViewRequest, reader: jspb.BinaryReader): UseFederatedBankViewRequest;
}

export namespace UseFederatedBankViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedBankViewReply): UseIsolatedBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedBankViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedBankViewReply, reader: jspb.BinaryReader): UseIsolatedBankViewReply;
}

export namespace UseIsolatedBankViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedBankViewRequest): UseIsolatedBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedBankViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedBankViewRequest, reader: jspb.BinaryReader): UseIsolatedBankViewRequest;
}

export namespace UseIsolatedBankViewRequest {
  export type AsObject = {
  }
}

export class UseActiveAssessmentPartViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseActiveAssessmentPartViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseActiveAssessmentPartViewReply): UseActiveAssessmentPartViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseActiveAssessmentPartViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseActiveAssessmentPartViewReply;
  static deserializeBinaryFromReader(message: UseActiveAssessmentPartViewReply, reader: jspb.BinaryReader): UseActiveAssessmentPartViewReply;
}

export namespace UseActiveAssessmentPartViewReply {
  export type AsObject = {
  }
}

export class UseActiveAssessmentPartViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseActiveAssessmentPartViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseActiveAssessmentPartViewRequest): UseActiveAssessmentPartViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseActiveAssessmentPartViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseActiveAssessmentPartViewRequest;
  static deserializeBinaryFromReader(message: UseActiveAssessmentPartViewRequest, reader: jspb.BinaryReader): UseActiveAssessmentPartViewRequest;
}

export namespace UseActiveAssessmentPartViewRequest {
  export type AsObject = {
  }
}

export class UseAnyStatusAssessmentPartViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyStatusAssessmentPartViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyStatusAssessmentPartViewReply): UseAnyStatusAssessmentPartViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyStatusAssessmentPartViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyStatusAssessmentPartViewReply;
  static deserializeBinaryFromReader(message: UseAnyStatusAssessmentPartViewReply, reader: jspb.BinaryReader): UseAnyStatusAssessmentPartViewReply;
}

export namespace UseAnyStatusAssessmentPartViewReply {
  export type AsObject = {
  }
}

export class UseAnyStatusAssessmentPartViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyStatusAssessmentPartViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyStatusAssessmentPartViewRequest): UseAnyStatusAssessmentPartViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyStatusAssessmentPartViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyStatusAssessmentPartViewRequest;
  static deserializeBinaryFromReader(message: UseAnyStatusAssessmentPartViewRequest, reader: jspb.BinaryReader): UseAnyStatusAssessmentPartViewRequest;
}

export namespace UseAnyStatusAssessmentPartViewRequest {
  export type AsObject = {
  }
}

export class UseSequesteredAssessmentPartViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseSequesteredAssessmentPartViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseSequesteredAssessmentPartViewReply): UseSequesteredAssessmentPartViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseSequesteredAssessmentPartViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseSequesteredAssessmentPartViewReply;
  static deserializeBinaryFromReader(message: UseSequesteredAssessmentPartViewReply, reader: jspb.BinaryReader): UseSequesteredAssessmentPartViewReply;
}

export namespace UseSequesteredAssessmentPartViewReply {
  export type AsObject = {
  }
}

export class UseSequesteredAssessmentPartViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseSequesteredAssessmentPartViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseSequesteredAssessmentPartViewRequest): UseSequesteredAssessmentPartViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseSequesteredAssessmentPartViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseSequesteredAssessmentPartViewRequest;
  static deserializeBinaryFromReader(message: UseSequesteredAssessmentPartViewRequest, reader: jspb.BinaryReader): UseSequesteredAssessmentPartViewRequest;
}

export namespace UseSequesteredAssessmentPartViewRequest {
  export type AsObject = {
  }
}

export class UseUnsequesteredAssessmentPartViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseUnsequesteredAssessmentPartViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseUnsequesteredAssessmentPartViewReply): UseUnsequesteredAssessmentPartViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseUnsequesteredAssessmentPartViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseUnsequesteredAssessmentPartViewReply;
  static deserializeBinaryFromReader(message: UseUnsequesteredAssessmentPartViewReply, reader: jspb.BinaryReader): UseUnsequesteredAssessmentPartViewReply;
}

export namespace UseUnsequesteredAssessmentPartViewReply {
  export type AsObject = {
  }
}

export class UseUnsequesteredAssessmentPartViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseUnsequesteredAssessmentPartViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseUnsequesteredAssessmentPartViewRequest): UseUnsequesteredAssessmentPartViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseUnsequesteredAssessmentPartViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseUnsequesteredAssessmentPartViewRequest;
  static deserializeBinaryFromReader(message: UseUnsequesteredAssessmentPartViewRequest, reader: jspb.BinaryReader): UseUnsequesteredAssessmentPartViewRequest;
}

export namespace UseUnsequesteredAssessmentPartViewRequest {
  export type AsObject = {
  }
}

export class GetAssessmentPartReply extends jspb.Message {
  hasAssessmentPart(): boolean;
  clearAssessmentPart(): void;
  getAssessmentPart(): AssessmentPart | undefined;
  setAssessmentPart(value?: AssessmentPart): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartReply): GetAssessmentPartReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartReply;
  static deserializeBinaryFromReader(message: GetAssessmentPartReply, reader: jspb.BinaryReader): GetAssessmentPartReply;
}

export namespace GetAssessmentPartReply {
  export type AsObject = {
    assessmentPart?: AssessmentPart.AsObject,
  }
}

export class GetAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartRequest): GetAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartRequest, reader: jspb.BinaryReader): GetAssessmentPartRequest;
}

export namespace GetAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentPartsByIdsRequest extends jspb.Message {
  clearAssessmentPartIdsList(): void;
  getAssessmentPartIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssessmentPartIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssessmentPartIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByIdsRequest): GetAssessmentPartsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByIdsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByIdsRequest, reader: jspb.BinaryReader): GetAssessmentPartsByIdsRequest;
}

export namespace GetAssessmentPartsByIdsRequest {
  export type AsObject = {
    assessmentPartIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentPartsByGenusTypeRequest extends jspb.Message {
  hasAssessmentPartGenusType(): boolean;
  clearAssessmentPartGenusType(): void;
  getAssessmentPartGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentPartGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByGenusTypeRequest): GetAssessmentPartsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentPartsByGenusTypeRequest;
}

export namespace GetAssessmentPartsByGenusTypeRequest {
  export type AsObject = {
    assessmentPartGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentPartsByParentGenusTypeRequest extends jspb.Message {
  hasAssessmentGenusType(): boolean;
  clearAssessmentGenusType(): void;
  getAssessmentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByParentGenusTypeRequest): GetAssessmentPartsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentPartsByParentGenusTypeRequest;
}

export namespace GetAssessmentPartsByParentGenusTypeRequest {
  export type AsObject = {
    assessmentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentPartsByRecordTypeRequest extends jspb.Message {
  hasAssessmentPartRecordType(): boolean;
  clearAssessmentPartRecordType(): void;
  getAssessmentPartRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentPartRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByRecordTypeRequest): GetAssessmentPartsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByRecordTypeRequest, reader: jspb.BinaryReader): GetAssessmentPartsByRecordTypeRequest;
}

export namespace GetAssessmentPartsByRecordTypeRequest {
  export type AsObject = {
    assessmentPartRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentPartsForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsForAssessmentRequest): GetAssessmentPartsForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsForAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentPartsForAssessmentRequest;
}

export namespace GetAssessmentPartsForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsRequest): GetAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsRequest, reader: jspb.BinaryReader): GetAssessmentPartsRequest;
}

export namespace GetAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class CanSearchAssessmentPartsReply extends jspb.Message {
  getCanSearchAssessmentParts(): boolean;
  setCanSearchAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentPartsReply): CanSearchAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanSearchAssessmentPartsReply, reader: jspb.BinaryReader): CanSearchAssessmentPartsReply;
}

export namespace CanSearchAssessmentPartsReply {
  export type AsObject = {
    canSearchAssessmentParts: boolean,
  }
}

export class CanSearchAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentPartsRequest): CanSearchAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanSearchAssessmentPartsRequest, reader: jspb.BinaryReader): CanSearchAssessmentPartsRequest;
}

export namespace CanSearchAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentPartQueryReply extends jspb.Message {
  hasAssessmentPartQuery(): boolean;
  clearAssessmentPartQuery(): void;
  getAssessmentPartQuery(): AssessmentPartQuery | undefined;
  setAssessmentPartQuery(value?: AssessmentPartQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartQueryReply): GetAssessmentPartQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartQueryReply;
  static deserializeBinaryFromReader(message: GetAssessmentPartQueryReply, reader: jspb.BinaryReader): GetAssessmentPartQueryReply;
}

export namespace GetAssessmentPartQueryReply {
  export type AsObject = {
    assessmentPartQuery?: AssessmentPartQuery.AsObject,
  }
}

export class GetAssessmentPartQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartQueryRequest): GetAssessmentPartQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartQueryRequest, reader: jspb.BinaryReader): GetAssessmentPartQueryRequest;
}

export namespace GetAssessmentPartQueryRequest {
  export type AsObject = {
  }
}

export class GetAssessmentPartsByQueryRequest extends jspb.Message {
  hasAssessmentPartQuery(): boolean;
  clearAssessmentPartQuery(): void;
  getAssessmentPartQuery(): AssessmentPartQuery | undefined;
  setAssessmentPartQuery(value?: AssessmentPartQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByQueryRequest): GetAssessmentPartsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByQueryRequest, reader: jspb.BinaryReader): GetAssessmentPartsByQueryRequest;
}

export namespace GetAssessmentPartsByQueryRequest {
  export type AsObject = {
    assessmentPartQuery?: AssessmentPartQuery.AsObject,
  }
}

export class CanCreateAssessmentPartsReply extends jspb.Message {
  getCanCreateAssessmentParts(): boolean;
  setCanCreateAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentPartsReply): CanCreateAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentPartsReply, reader: jspb.BinaryReader): CanCreateAssessmentPartsReply;
}

export namespace CanCreateAssessmentPartsReply {
  export type AsObject = {
    canCreateAssessmentParts: boolean,
  }
}

export class CanCreateAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentPartsRequest): CanCreateAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentPartsRequest, reader: jspb.BinaryReader): CanCreateAssessmentPartsRequest;
}

export namespace CanCreateAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class CanCreateAssessmentPartWithRecordTypesReply extends jspb.Message {
  getCanCreateAssessmentPartWithRecordTypes(): boolean;
  setCanCreateAssessmentPartWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentPartWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentPartWithRecordTypesReply): CanCreateAssessmentPartWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentPartWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentPartWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentPartWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAssessmentPartWithRecordTypesReply;
}

export namespace CanCreateAssessmentPartWithRecordTypesReply {
  export type AsObject = {
    canCreateAssessmentPartWithRecordTypes: boolean,
  }
}

export class CanCreateAssessmentPartWithRecordTypesRequest extends jspb.Message {
  clearAssessmentPartRecordTypesList(): void;
  getAssessmentPartRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentPartRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentPartRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentPartWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentPartWithRecordTypesRequest): CanCreateAssessmentPartWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentPartWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentPartWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentPartWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAssessmentPartWithRecordTypesRequest;
}

export namespace CanCreateAssessmentPartWithRecordTypesRequest {
  export type AsObject = {
    assessmentPartRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAssessmentPartFormForCreateForAssessmentReply extends jspb.Message {
  hasAssessmentPartForm(): boolean;
  clearAssessmentPartForm(): void;
  getAssessmentPartForm(): AssessmentPartForm | undefined;
  setAssessmentPartForm(value?: AssessmentPartForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartFormForCreateForAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartFormForCreateForAssessmentReply): GetAssessmentPartFormForCreateForAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartFormForCreateForAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartFormForCreateForAssessmentReply;
  static deserializeBinaryFromReader(message: GetAssessmentPartFormForCreateForAssessmentReply, reader: jspb.BinaryReader): GetAssessmentPartFormForCreateForAssessmentReply;
}

export namespace GetAssessmentPartFormForCreateForAssessmentReply {
  export type AsObject = {
    assessmentPartForm?: AssessmentPartForm.AsObject,
  }
}

export class GetAssessmentPartFormForCreateForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearAssessmentPartRecordTypesList(): void;
  getAssessmentPartRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentPartRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentPartRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartFormForCreateForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartFormForCreateForAssessmentRequest): GetAssessmentPartFormForCreateForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartFormForCreateForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartFormForCreateForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartFormForCreateForAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentPartFormForCreateForAssessmentRequest;
}

export namespace GetAssessmentPartFormForCreateForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentPartRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateAssessmentPartForAssessmentReply extends jspb.Message {
  hasAssessmentPart(): boolean;
  clearAssessmentPart(): void;
  getAssessmentPart(): AssessmentPart | undefined;
  setAssessmentPart(value?: AssessmentPart): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentPartForAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentPartForAssessmentReply): CreateAssessmentPartForAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentPartForAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentPartForAssessmentReply;
  static deserializeBinaryFromReader(message: CreateAssessmentPartForAssessmentReply, reader: jspb.BinaryReader): CreateAssessmentPartForAssessmentReply;
}

export namespace CreateAssessmentPartForAssessmentReply {
  export type AsObject = {
    assessmentPart?: AssessmentPart.AsObject,
  }
}

export class CreateAssessmentPartForAssessmentRequest extends jspb.Message {
  hasAssessmentPartForm(): boolean;
  clearAssessmentPartForm(): void;
  getAssessmentPartForm(): AssessmentPartForm | undefined;
  setAssessmentPartForm(value?: AssessmentPartForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentPartForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentPartForAssessmentRequest): CreateAssessmentPartForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentPartForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentPartForAssessmentRequest;
  static deserializeBinaryFromReader(message: CreateAssessmentPartForAssessmentRequest, reader: jspb.BinaryReader): CreateAssessmentPartForAssessmentRequest;
}

export namespace CreateAssessmentPartForAssessmentRequest {
  export type AsObject = {
    assessmentPartForm?: AssessmentPartForm.AsObject,
  }
}

export class GetAssessmentPartFormForCreateForAssessmentPartReply extends jspb.Message {
  hasAssessmentPartForm(): boolean;
  clearAssessmentPartForm(): void;
  getAssessmentPartForm(): AssessmentPartForm | undefined;
  setAssessmentPartForm(value?: AssessmentPartForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartFormForCreateForAssessmentPartReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartFormForCreateForAssessmentPartReply): GetAssessmentPartFormForCreateForAssessmentPartReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartFormForCreateForAssessmentPartReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartFormForCreateForAssessmentPartReply;
  static deserializeBinaryFromReader(message: GetAssessmentPartFormForCreateForAssessmentPartReply, reader: jspb.BinaryReader): GetAssessmentPartFormForCreateForAssessmentPartReply;
}

export namespace GetAssessmentPartFormForCreateForAssessmentPartReply {
  export type AsObject = {
    assessmentPartForm?: AssessmentPartForm.AsObject,
  }
}

export class GetAssessmentPartFormForCreateForAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearAssessmentPartRecordTypesList(): void;
  getAssessmentPartRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentPartRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentPartRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartFormForCreateForAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartFormForCreateForAssessmentPartRequest): GetAssessmentPartFormForCreateForAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartFormForCreateForAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartFormForCreateForAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartFormForCreateForAssessmentPartRequest, reader: jspb.BinaryReader): GetAssessmentPartFormForCreateForAssessmentPartRequest;
}

export namespace GetAssessmentPartFormForCreateForAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentPartRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateAssessmentPartForAssessmentPartReply extends jspb.Message {
  hasAssessmentPart(): boolean;
  clearAssessmentPart(): void;
  getAssessmentPart(): AssessmentPart | undefined;
  setAssessmentPart(value?: AssessmentPart): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentPartForAssessmentPartReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentPartForAssessmentPartReply): CreateAssessmentPartForAssessmentPartReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentPartForAssessmentPartReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentPartForAssessmentPartReply;
  static deserializeBinaryFromReader(message: CreateAssessmentPartForAssessmentPartReply, reader: jspb.BinaryReader): CreateAssessmentPartForAssessmentPartReply;
}

export namespace CreateAssessmentPartForAssessmentPartReply {
  export type AsObject = {
    assessmentPart?: AssessmentPart.AsObject,
  }
}

export class CreateAssessmentPartForAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartForm(): boolean;
  clearAssessmentPartForm(): void;
  getAssessmentPartForm(): AssessmentPartForm | undefined;
  setAssessmentPartForm(value?: AssessmentPartForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentPartForAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentPartForAssessmentPartRequest): CreateAssessmentPartForAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentPartForAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentPartForAssessmentPartRequest;
  static deserializeBinaryFromReader(message: CreateAssessmentPartForAssessmentPartRequest, reader: jspb.BinaryReader): CreateAssessmentPartForAssessmentPartRequest;
}

export namespace CreateAssessmentPartForAssessmentPartRequest {
  export type AsObject = {
    assessmentPartForm?: AssessmentPartForm.AsObject,
  }
}

export class CanUpdateAssessmentPartsReply extends jspb.Message {
  getCanUpdateAssessmentParts(): boolean;
  setCanUpdateAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentPartsReply): CanUpdateAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentPartsReply, reader: jspb.BinaryReader): CanUpdateAssessmentPartsReply;
}

export namespace CanUpdateAssessmentPartsReply {
  export type AsObject = {
    canUpdateAssessmentParts: boolean,
  }
}

export class CanUpdateAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentPartsRequest): CanUpdateAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentPartsRequest, reader: jspb.BinaryReader): CanUpdateAssessmentPartsRequest;
}

export namespace CanUpdateAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentPartFormForUpdateReply extends jspb.Message {
  hasAssessmentPartForm(): boolean;
  clearAssessmentPartForm(): void;
  getAssessmentPartForm(): AssessmentPartForm | undefined;
  setAssessmentPartForm(value?: AssessmentPartForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartFormForUpdateReply): GetAssessmentPartFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAssessmentPartFormForUpdateReply, reader: jspb.BinaryReader): GetAssessmentPartFormForUpdateReply;
}

export namespace GetAssessmentPartFormForUpdateReply {
  export type AsObject = {
    assessmentPartForm?: AssessmentPartForm.AsObject,
  }
}

export class GetAssessmentPartFormForUpdateRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartFormForUpdateRequest): GetAssessmentPartFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartFormForUpdateRequest, reader: jspb.BinaryReader): GetAssessmentPartFormForUpdateRequest;
}

export namespace GetAssessmentPartFormForUpdateRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAssessmentPartReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentPartReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentPartReply): UpdateAssessmentPartReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentPartReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentPartReply;
  static deserializeBinaryFromReader(message: UpdateAssessmentPartReply, reader: jspb.BinaryReader): UpdateAssessmentPartReply;
}

export namespace UpdateAssessmentPartReply {
  export type AsObject = {
  }
}

export class UpdateAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartForm(): boolean;
  clearAssessmentPartForm(): void;
  getAssessmentPartForm(): AssessmentPartForm | undefined;
  setAssessmentPartForm(value?: AssessmentPartForm): void;

  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentPartRequest): UpdateAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentPartRequest;
  static deserializeBinaryFromReader(message: UpdateAssessmentPartRequest, reader: jspb.BinaryReader): UpdateAssessmentPartRequest;
}

export namespace UpdateAssessmentPartRequest {
  export type AsObject = {
    assessmentPartForm?: AssessmentPartForm.AsObject,
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanDeleteAssessmentPartsReply extends jspb.Message {
  getCanDeleteAssessmentParts(): boolean;
  setCanDeleteAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentPartsReply): CanDeleteAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentPartsReply, reader: jspb.BinaryReader): CanDeleteAssessmentPartsReply;
}

export namespace CanDeleteAssessmentPartsReply {
  export type AsObject = {
    canDeleteAssessmentParts: boolean,
  }
}

export class CanDeleteAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentPartsRequest): CanDeleteAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentPartsRequest, reader: jspb.BinaryReader): CanDeleteAssessmentPartsRequest;
}

export namespace CanDeleteAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class DeleteAssessmentPartReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentPartReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentPartReply): DeleteAssessmentPartReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentPartReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentPartReply;
  static deserializeBinaryFromReader(message: DeleteAssessmentPartReply, reader: jspb.BinaryReader): DeleteAssessmentPartReply;
}

export namespace DeleteAssessmentPartReply {
  export type AsObject = {
  }
}

export class DeleteAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentPartRequest): DeleteAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentPartRequest;
  static deserializeBinaryFromReader(message: DeleteAssessmentPartRequest, reader: jspb.BinaryReader): DeleteAssessmentPartRequest;
}

export namespace DeleteAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageAssessmentPartAliasesReply extends jspb.Message {
  getCanManageAssessmentPartAliases(): boolean;
  setCanManageAssessmentPartAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentPartAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentPartAliasesReply): CanManageAssessmentPartAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentPartAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentPartAliasesReply;
  static deserializeBinaryFromReader(message: CanManageAssessmentPartAliasesReply, reader: jspb.BinaryReader): CanManageAssessmentPartAliasesReply;
}

export namespace CanManageAssessmentPartAliasesReply {
  export type AsObject = {
    canManageAssessmentPartAliases: boolean,
  }
}

export class CanManageAssessmentPartAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentPartAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentPartAliasesRequest): CanManageAssessmentPartAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentPartAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentPartAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageAssessmentPartAliasesRequest, reader: jspb.BinaryReader): CanManageAssessmentPartAliasesRequest;
}

export namespace CanManageAssessmentPartAliasesRequest {
  export type AsObject = {
  }
}

export class AliasAssessmentPartReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentPartReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentPartReply): AliasAssessmentPartReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentPartReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentPartReply;
  static deserializeBinaryFromReader(message: AliasAssessmentPartReply, reader: jspb.BinaryReader): AliasAssessmentPartReply;
}

export namespace AliasAssessmentPartReply {
  export type AsObject = {
  }
}

export class AliasAssessmentPartRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentPartRequest): AliasAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentPartRequest;
  static deserializeBinaryFromReader(message: AliasAssessmentPartRequest, reader: jspb.BinaryReader): AliasAssessmentPartRequest;
}

export namespace AliasAssessmentPartRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssessmentPartBankMappingsReply extends jspb.Message {
  getCanLookupAssessmentPartBankMappings(): boolean;
  setCanLookupAssessmentPartBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentPartBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentPartBankMappingsReply): CanLookupAssessmentPartBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentPartBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentPartBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentPartBankMappingsReply, reader: jspb.BinaryReader): CanLookupAssessmentPartBankMappingsReply;
}

export namespace CanLookupAssessmentPartBankMappingsReply {
  export type AsObject = {
    canLookupAssessmentPartBankMappings: boolean,
  }
}

export class CanLookupAssessmentPartBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentPartBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentPartBankMappingsRequest): CanLookupAssessmentPartBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentPartBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentPartBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentPartBankMappingsRequest, reader: jspb.BinaryReader): CanLookupAssessmentPartBankMappingsRequest;
}

export namespace CanLookupAssessmentPartBankMappingsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentPartBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentPartBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentPartBankViewReply): UseComparativeAssessmentPartBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentPartBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentPartBankViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentPartBankViewReply, reader: jspb.BinaryReader): UseComparativeAssessmentPartBankViewReply;
}

export namespace UseComparativeAssessmentPartBankViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentPartBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentPartBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentPartBankViewRequest): UseComparativeAssessmentPartBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentPartBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentPartBankViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentPartBankViewRequest, reader: jspb.BinaryReader): UseComparativeAssessmentPartBankViewRequest;
}

export namespace UseComparativeAssessmentPartBankViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentPartBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentPartBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentPartBankViewReply): UsePlenaryAssessmentPartBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentPartBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentPartBankViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentPartBankViewReply, reader: jspb.BinaryReader): UsePlenaryAssessmentPartBankViewReply;
}

export namespace UsePlenaryAssessmentPartBankViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentPartBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentPartBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentPartBankViewRequest): UsePlenaryAssessmentPartBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentPartBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentPartBankViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentPartBankViewRequest, reader: jspb.BinaryReader): UsePlenaryAssessmentPartBankViewRequest;
}

export namespace UsePlenaryAssessmentPartBankViewRequest {
  export type AsObject = {
  }
}

export class GetAssessmentPartIdsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartIdsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartIdsByBankRequest): GetAssessmentPartIdsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartIdsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartIdsByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartIdsByBankRequest, reader: jspb.BinaryReader): GetAssessmentPartIdsByBankRequest;
}

export namespace GetAssessmentPartIdsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentPartsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByBankRequest): GetAssessmentPartsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByBankRequest, reader: jspb.BinaryReader): GetAssessmentPartsByBankRequest;
}

export namespace GetAssessmentPartsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentPartIdsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartIdsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartIdsByBanksRequest): GetAssessmentPartIdsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartIdsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartIdsByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartIdsByBanksRequest, reader: jspb.BinaryReader): GetAssessmentPartIdsByBanksRequest;
}

export namespace GetAssessmentPartIdsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentPartsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByBanksRequest): GetAssessmentPartsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByBanksRequest, reader: jspb.BinaryReader): GetAssessmentPartsByBanksRequest;
}

export namespace GetAssessmentPartsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBankIdsByAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdsByAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdsByAssessmentPartRequest): GetBankIdsByAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdsByAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdsByAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetBankIdsByAssessmentPartRequest, reader: jspb.BinaryReader): GetBankIdsByAssessmentPartRequest;
}

export namespace GetBankIdsByAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBanksByAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByAssessmentPartRequest): GetBanksByAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetBanksByAssessmentPartRequest, reader: jspb.BinaryReader): GetBanksByAssessmentPartRequest;
}

export namespace GetBanksByAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAssessmentPartsReply extends jspb.Message {
  getCanAssignAssessmentParts(): boolean;
  setCanAssignAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentPartsReply): CanAssignAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentPartsReply, reader: jspb.BinaryReader): CanAssignAssessmentPartsReply;
}

export namespace CanAssignAssessmentPartsReply {
  export type AsObject = {
    canAssignAssessmentParts: boolean,
  }
}

export class CanAssignAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentPartsRequest): CanAssignAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentPartsRequest, reader: jspb.BinaryReader): CanAssignAssessmentPartsRequest;
}

export namespace CanAssignAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class CanAssignAssessmentPartsToBankReply extends jspb.Message {
  getCanAssignAssessmentPartsToBank(): boolean;
  setCanAssignAssessmentPartsToBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentPartsToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentPartsToBankReply): CanAssignAssessmentPartsToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentPartsToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentPartsToBankReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentPartsToBankReply, reader: jspb.BinaryReader): CanAssignAssessmentPartsToBankReply;
}

export namespace CanAssignAssessmentPartsToBankReply {
  export type AsObject = {
    canAssignAssessmentPartsToBank: boolean,
  }
}

export class CanAssignAssessmentPartsToBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentPartsToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentPartsToBankRequest): CanAssignAssessmentPartsToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentPartsToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentPartsToBankRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentPartsToBankRequest, reader: jspb.BinaryReader): CanAssignAssessmentPartsToBankRequest;
}

export namespace CanAssignAssessmentPartsToBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBankIdsRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBankIdsRequest): GetAssignableBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBankIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableBankIdsRequest, reader: jspb.BinaryReader): GetAssignableBankIdsRequest;
}

export namespace GetAssignableBankIdsRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBankIdsForAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBankIdsForAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBankIdsForAssessmentPartRequest): GetAssignableBankIdsForAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBankIdsForAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBankIdsForAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetAssignableBankIdsForAssessmentPartRequest, reader: jspb.BinaryReader): GetAssignableBankIdsForAssessmentPartRequest;
}

export namespace GetAssignableBankIdsForAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAssessmentPartToBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentPartToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentPartToBankReply): AssignAssessmentPartToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentPartToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentPartToBankReply;
  static deserializeBinaryFromReader(message: AssignAssessmentPartToBankReply, reader: jspb.BinaryReader): AssignAssessmentPartToBankReply;
}

export namespace AssignAssessmentPartToBankReply {
  export type AsObject = {
  }
}

export class AssignAssessmentPartToBankRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentPartToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentPartToBankRequest): AssignAssessmentPartToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentPartToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentPartToBankRequest;
  static deserializeBinaryFromReader(message: AssignAssessmentPartToBankRequest, reader: jspb.BinaryReader): AssignAssessmentPartToBankRequest;
}

export namespace AssignAssessmentPartToBankRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAssessmentPartFromBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentPartFromBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentPartFromBankReply): UnassignAssessmentPartFromBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentPartFromBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentPartFromBankReply;
  static deserializeBinaryFromReader(message: UnassignAssessmentPartFromBankReply, reader: jspb.BinaryReader): UnassignAssessmentPartFromBankReply;
}

export namespace UnassignAssessmentPartFromBankReply {
  export type AsObject = {
  }
}

export class UnassignAssessmentPartFromBankRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentPartFromBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentPartFromBankRequest): UnassignAssessmentPartFromBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentPartFromBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentPartFromBankRequest;
  static deserializeBinaryFromReader(message: UnassignAssessmentPartFromBankRequest, reader: jspb.BinaryReader): UnassignAssessmentPartFromBankRequest;
}

export namespace UnassignAssessmentPartFromBankRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignAssessmentPartToBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentPartToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentPartToBankReply): ReassignAssessmentPartToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentPartToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentPartToBankReply;
  static deserializeBinaryFromReader(message: ReassignAssessmentPartToBankReply, reader: jspb.BinaryReader): ReassignAssessmentPartToBankReply;
}

export namespace ReassignAssessmentPartToBankReply {
  export type AsObject = {
  }
}

export class ReassignAssessmentPartToBankRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromBiankId(): boolean;
  clearFromBiankId(): void;
  getFromBiankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromBiankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToBankId(): boolean;
  clearToBankId(): void;
  getToBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentPartToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentPartToBankRequest): ReassignAssessmentPartToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentPartToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentPartToBankRequest;
  static deserializeBinaryFromReader(message: ReassignAssessmentPartToBankRequest, reader: jspb.BinaryReader): ReassignAssessmentPartToBankRequest;
}

export namespace ReassignAssessmentPartToBankRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromBiankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAccessAssessmentPartItemsReply extends jspb.Message {
  getCanAccessAssessmentPartItems(): boolean;
  setCanAccessAssessmentPartItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAssessmentPartItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAssessmentPartItemsReply): CanAccessAssessmentPartItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAssessmentPartItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAssessmentPartItemsReply;
  static deserializeBinaryFromReader(message: CanAccessAssessmentPartItemsReply, reader: jspb.BinaryReader): CanAccessAssessmentPartItemsReply;
}

export namespace CanAccessAssessmentPartItemsReply {
  export type AsObject = {
    canAccessAssessmentPartItems: boolean,
  }
}

export class CanAccessAssessmentPartItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAssessmentPartItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAssessmentPartItemsRequest): CanAccessAssessmentPartItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAssessmentPartItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAssessmentPartItemsRequest;
  static deserializeBinaryFromReader(message: CanAccessAssessmentPartItemsRequest, reader: jspb.BinaryReader): CanAccessAssessmentPartItemsRequest;
}

export namespace CanAccessAssessmentPartItemsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAsseessmentPartItemViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAsseessmentPartItemViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAsseessmentPartItemViewReply): UseComparativeAsseessmentPartItemViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAsseessmentPartItemViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAsseessmentPartItemViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAsseessmentPartItemViewReply, reader: jspb.BinaryReader): UseComparativeAsseessmentPartItemViewReply;
}

export namespace UseComparativeAsseessmentPartItemViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAsseessmentPartItemViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAsseessmentPartItemViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAsseessmentPartItemViewRequest): UseComparativeAsseessmentPartItemViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAsseessmentPartItemViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAsseessmentPartItemViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAsseessmentPartItemViewRequest, reader: jspb.BinaryReader): UseComparativeAsseessmentPartItemViewRequest;
}

export namespace UseComparativeAsseessmentPartItemViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentPartItemViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentPartItemViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentPartItemViewReply): UsePlenaryAssessmentPartItemViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentPartItemViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentPartItemViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentPartItemViewReply, reader: jspb.BinaryReader): UsePlenaryAssessmentPartItemViewReply;
}

export namespace UsePlenaryAssessmentPartItemViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentPartItemViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentPartItemViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentPartItemViewRequest): UsePlenaryAssessmentPartItemViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentPartItemViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentPartItemViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentPartItemViewRequest, reader: jspb.BinaryReader): UsePlenaryAssessmentPartItemViewRequest;
}

export namespace UsePlenaryAssessmentPartItemViewRequest {
  export type AsObject = {
  }
}

export class GetAssessmentPartItemsRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartItemsRequest): GetAssessmentPartItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartItemsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartItemsRequest, reader: jspb.BinaryReader): GetAssessmentPartItemsRequest;
}

export namespace GetAssessmentPartItemsRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentPartsByItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentPartsByItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentPartsByItemRequest): GetAssessmentPartsByItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentPartsByItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentPartsByItemRequest;
  static deserializeBinaryFromReader(message: GetAssessmentPartsByItemRequest, reader: jspb.BinaryReader): GetAssessmentPartsByItemRequest;
}

export namespace GetAssessmentPartsByItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanDesignAssessmentPartsReply extends jspb.Message {
  getCanDesignAssessmentParts(): boolean;
  setCanDesignAssessmentParts(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDesignAssessmentPartsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDesignAssessmentPartsReply): CanDesignAssessmentPartsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDesignAssessmentPartsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDesignAssessmentPartsReply;
  static deserializeBinaryFromReader(message: CanDesignAssessmentPartsReply, reader: jspb.BinaryReader): CanDesignAssessmentPartsReply;
}

export namespace CanDesignAssessmentPartsReply {
  export type AsObject = {
    canDesignAssessmentParts: boolean,
  }
}

export class CanDesignAssessmentPartsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDesignAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDesignAssessmentPartsRequest): CanDesignAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDesignAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDesignAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: CanDesignAssessmentPartsRequest, reader: jspb.BinaryReader): CanDesignAssessmentPartsRequest;
}

export namespace CanDesignAssessmentPartsRequest {
  export type AsObject = {
  }
}

export class AddItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddItemReply): AddItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddItemReply;
  static deserializeBinaryFromReader(message: AddItemReply, reader: jspb.BinaryReader): AddItemReply;
}

export namespace AddItemReply {
  export type AsObject = {
  }
}

export class AddItemRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddItemRequest): AddItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddItemRequest;
  static deserializeBinaryFromReader(message: AddItemRequest, reader: jspb.BinaryReader): AddItemRequest;
}

export namespace AddItemRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveItemAheadReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveItemAheadReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveItemAheadReply): MoveItemAheadReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveItemAheadReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveItemAheadReply;
  static deserializeBinaryFromReader(message: MoveItemAheadReply, reader: jspb.BinaryReader): MoveItemAheadReply;
}

export namespace MoveItemAheadReply {
  export type AsObject = {
  }
}

export class MoveItemAheadRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveItemAheadRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveItemAheadRequest): MoveItemAheadRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveItemAheadRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveItemAheadRequest;
  static deserializeBinaryFromReader(message: MoveItemAheadRequest, reader: jspb.BinaryReader): MoveItemAheadRequest;
}

export namespace MoveItemAheadRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveItemBehindReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveItemBehindReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveItemBehindReply): MoveItemBehindReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveItemBehindReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveItemBehindReply;
  static deserializeBinaryFromReader(message: MoveItemBehindReply, reader: jspb.BinaryReader): MoveItemBehindReply;
}

export namespace MoveItemBehindReply {
  export type AsObject = {
  }
}

export class MoveItemBehindRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveItemBehindRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveItemBehindRequest): MoveItemBehindRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveItemBehindRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveItemBehindRequest;
  static deserializeBinaryFromReader(message: MoveItemBehindRequest, reader: jspb.BinaryReader): MoveItemBehindRequest;
}

export namespace MoveItemBehindRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class OrderItemsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: OrderItemsReply): OrderItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderItemsReply;
  static deserializeBinaryFromReader(message: OrderItemsReply, reader: jspb.BinaryReader): OrderItemsReply;
}

export namespace OrderItemsReply {
  export type AsObject = {
  }
}

export class OrderItemsRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearItemIdsList(): void;
  getItemIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setItemIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addItemIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: OrderItemsRequest): OrderItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderItemsRequest;
  static deserializeBinaryFromReader(message: OrderItemsRequest, reader: jspb.BinaryReader): OrderItemsRequest;
}

export namespace OrderItemsRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class RemoveItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveItemReply): RemoveItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveItemReply;
  static deserializeBinaryFromReader(message: RemoveItemReply, reader: jspb.BinaryReader): RemoveItemReply;
}

export namespace RemoveItemReply {
  export type AsObject = {
  }
}

export class RemoveItemRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveItemRequest): RemoveItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveItemRequest;
  static deserializeBinaryFromReader(message: RemoveItemRequest, reader: jspb.BinaryReader): RemoveItemRequest;
}

export namespace RemoveItemRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupSequenceRulesReply extends jspb.Message {
  getCanLookupSequenceRules(): boolean;
  setCanLookupSequenceRules(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupSequenceRulesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupSequenceRulesReply): CanLookupSequenceRulesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupSequenceRulesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupSequenceRulesReply;
  static deserializeBinaryFromReader(message: CanLookupSequenceRulesReply, reader: jspb.BinaryReader): CanLookupSequenceRulesReply;
}

export namespace CanLookupSequenceRulesReply {
  export type AsObject = {
    canLookupSequenceRules: boolean,
  }
}

export class CanLookupSequenceRulesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupSequenceRulesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupSequenceRulesRequest): CanLookupSequenceRulesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupSequenceRulesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupSequenceRulesRequest;
  static deserializeBinaryFromReader(message: CanLookupSequenceRulesRequest, reader: jspb.BinaryReader): CanLookupSequenceRulesRequest;
}

export namespace CanLookupSequenceRulesRequest {
  export type AsObject = {
  }
}

export class UseComparativeSequenceRuleViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeSequenceRuleViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeSequenceRuleViewReply): UseComparativeSequenceRuleViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeSequenceRuleViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeSequenceRuleViewReply;
  static deserializeBinaryFromReader(message: UseComparativeSequenceRuleViewReply, reader: jspb.BinaryReader): UseComparativeSequenceRuleViewReply;
}

export namespace UseComparativeSequenceRuleViewReply {
  export type AsObject = {
  }
}

export class UseComparativeSequenceRuleViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeSequenceRuleViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeSequenceRuleViewRequest): UseComparativeSequenceRuleViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeSequenceRuleViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeSequenceRuleViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeSequenceRuleViewRequest, reader: jspb.BinaryReader): UseComparativeSequenceRuleViewRequest;
}

export namespace UseComparativeSequenceRuleViewRequest {
  export type AsObject = {
  }
}

export class UsePlenarySequenceRuleViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenarySequenceRuleViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenarySequenceRuleViewReply): UsePlenarySequenceRuleViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenarySequenceRuleViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenarySequenceRuleViewReply;
  static deserializeBinaryFromReader(message: UsePlenarySequenceRuleViewReply, reader: jspb.BinaryReader): UsePlenarySequenceRuleViewReply;
}

export namespace UsePlenarySequenceRuleViewReply {
  export type AsObject = {
  }
}

export class UsePlenarySequenceRuleViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenarySequenceRuleViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenarySequenceRuleViewRequest): UsePlenarySequenceRuleViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenarySequenceRuleViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenarySequenceRuleViewRequest;
  static deserializeBinaryFromReader(message: UsePlenarySequenceRuleViewRequest, reader: jspb.BinaryReader): UsePlenarySequenceRuleViewRequest;
}

export namespace UsePlenarySequenceRuleViewRequest {
  export type AsObject = {
  }
}

export class UseActiveSequenceRuleViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseActiveSequenceRuleViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseActiveSequenceRuleViewReply): UseActiveSequenceRuleViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseActiveSequenceRuleViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseActiveSequenceRuleViewReply;
  static deserializeBinaryFromReader(message: UseActiveSequenceRuleViewReply, reader: jspb.BinaryReader): UseActiveSequenceRuleViewReply;
}

export namespace UseActiveSequenceRuleViewReply {
  export type AsObject = {
  }
}

export class UseActiveSequenceRuleViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseActiveSequenceRuleViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseActiveSequenceRuleViewRequest): UseActiveSequenceRuleViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseActiveSequenceRuleViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseActiveSequenceRuleViewRequest;
  static deserializeBinaryFromReader(message: UseActiveSequenceRuleViewRequest, reader: jspb.BinaryReader): UseActiveSequenceRuleViewRequest;
}

export namespace UseActiveSequenceRuleViewRequest {
  export type AsObject = {
  }
}

export class UseAnyStatusSequenceRuleViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyStatusSequenceRuleViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyStatusSequenceRuleViewReply): UseAnyStatusSequenceRuleViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyStatusSequenceRuleViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyStatusSequenceRuleViewReply;
  static deserializeBinaryFromReader(message: UseAnyStatusSequenceRuleViewReply, reader: jspb.BinaryReader): UseAnyStatusSequenceRuleViewReply;
}

export namespace UseAnyStatusSequenceRuleViewReply {
  export type AsObject = {
  }
}

export class UseAnyStatusSequenceRuleViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyStatusSequenceRuleViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyStatusSequenceRuleViewRequest): UseAnyStatusSequenceRuleViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyStatusSequenceRuleViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyStatusSequenceRuleViewRequest;
  static deserializeBinaryFromReader(message: UseAnyStatusSequenceRuleViewRequest, reader: jspb.BinaryReader): UseAnyStatusSequenceRuleViewRequest;
}

export namespace UseAnyStatusSequenceRuleViewRequest {
  export type AsObject = {
  }
}

export class GetSequenceRuleReply extends jspb.Message {
  hasSequenceRule(): boolean;
  clearSequenceRule(): void;
  getSequenceRule(): SequenceRule | undefined;
  setSequenceRule(value?: SequenceRule): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRuleReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRuleReply): GetSequenceRuleReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRuleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRuleReply;
  static deserializeBinaryFromReader(message: GetSequenceRuleReply, reader: jspb.BinaryReader): GetSequenceRuleReply;
}

export namespace GetSequenceRuleReply {
  export type AsObject = {
    sequenceRule?: SequenceRule.AsObject,
  }
}

export class GetSequenceRuleRequest extends jspb.Message {
  hasSequenceRuleId(): boolean;
  clearSequenceRuleId(): void;
  getSequenceRuleId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSequenceRuleId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRuleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRuleRequest): GetSequenceRuleRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRuleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRuleRequest;
  static deserializeBinaryFromReader(message: GetSequenceRuleRequest, reader: jspb.BinaryReader): GetSequenceRuleRequest;
}

export namespace GetSequenceRuleRequest {
  export type AsObject = {
    sequenceRuleId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetSequenceRulesByIdsRequest extends jspb.Message {
  clearSequenceRuleIdsList(): void;
  getSequenceRuleIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setSequenceRuleIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addSequenceRuleIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesByIdsRequest): GetSequenceRulesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesByIdsRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesByIdsRequest, reader: jspb.BinaryReader): GetSequenceRulesByIdsRequest;
}

export namespace GetSequenceRulesByIdsRequest {
  export type AsObject = {
    sequenceRuleIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetSequenceRulesByGenusTypeRequest extends jspb.Message {
  hasSequenceRuleGenusType(): boolean;
  clearSequenceRuleGenusType(): void;
  getSequenceRuleGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setSequenceRuleGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesByGenusTypeRequest): GetSequenceRulesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesByGenusTypeRequest, reader: jspb.BinaryReader): GetSequenceRulesByGenusTypeRequest;
}

export namespace GetSequenceRulesByGenusTypeRequest {
  export type AsObject = {
    sequenceRuleGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetSequenceRulesByParentGenusTypeRequest extends jspb.Message {
  hasSequenceRuleGenusType(): boolean;
  clearSequenceRuleGenusType(): void;
  getSequenceRuleGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setSequenceRuleGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesByParentGenusTypeRequest): GetSequenceRulesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetSequenceRulesByParentGenusTypeRequest;
}

export namespace GetSequenceRulesByParentGenusTypeRequest {
  export type AsObject = {
    sequenceRuleGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetSequenceRulesByRecordTypeRequest extends jspb.Message {
  hasSequenceRuleRecordType(): boolean;
  clearSequenceRuleRecordType(): void;
  getSequenceRuleRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setSequenceRuleRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesByRecordTypeRequest): GetSequenceRulesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesByRecordTypeRequest, reader: jspb.BinaryReader): GetSequenceRulesByRecordTypeRequest;
}

export namespace GetSequenceRulesByRecordTypeRequest {
  export type AsObject = {
    sequenceRuleRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetSequenceRulesForAssessmentPartRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesForAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesForAssessmentPartRequest): GetSequenceRulesForAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesForAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesForAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesForAssessmentPartRequest, reader: jspb.BinaryReader): GetSequenceRulesForAssessmentPartRequest;
}

export namespace GetSequenceRulesForAssessmentPartRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetSequenceRulesForNextAssessmentPartRequest extends jspb.Message {
  hasNextAssessmentPartId(): boolean;
  clearNextAssessmentPartId(): void;
  getNextAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNextAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesForNextAssessmentPartRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesForNextAssessmentPartRequest): GetSequenceRulesForNextAssessmentPartRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesForNextAssessmentPartRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesForNextAssessmentPartRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesForNextAssessmentPartRequest, reader: jspb.BinaryReader): GetSequenceRulesForNextAssessmentPartRequest;
}

export namespace GetSequenceRulesForNextAssessmentPartRequest {
  export type AsObject = {
    nextAssessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetSequenceRulesForAssessmentPartsRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasNextAssessmentPartId(): boolean;
  clearNextAssessmentPartId(): void;
  getNextAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNextAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesForAssessmentPartsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesForAssessmentPartsRequest): GetSequenceRulesForAssessmentPartsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesForAssessmentPartsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesForAssessmentPartsRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesForAssessmentPartsRequest, reader: jspb.BinaryReader): GetSequenceRulesForAssessmentPartsRequest;
}

export namespace GetSequenceRulesForAssessmentPartsRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    nextAssessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetSequenceRulesForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesForAssessmentRequest): GetSequenceRulesForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesForAssessmentRequest, reader: jspb.BinaryReader): GetSequenceRulesForAssessmentRequest;
}

export namespace GetSequenceRulesForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetSequenceRulesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRulesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRulesRequest): GetSequenceRulesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRulesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRulesRequest;
  static deserializeBinaryFromReader(message: GetSequenceRulesRequest, reader: jspb.BinaryReader): GetSequenceRulesRequest;
}

export namespace GetSequenceRulesRequest {
  export type AsObject = {
  }
}

export class CanCreateSequenceRuleReply extends jspb.Message {
  getCanCreateSequenceRule(): boolean;
  setCanCreateSequenceRule(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateSequenceRuleReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateSequenceRuleReply): CanCreateSequenceRuleReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateSequenceRuleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateSequenceRuleReply;
  static deserializeBinaryFromReader(message: CanCreateSequenceRuleReply, reader: jspb.BinaryReader): CanCreateSequenceRuleReply;
}

export namespace CanCreateSequenceRuleReply {
  export type AsObject = {
    canCreateSequenceRule: boolean,
  }
}

export class CanCreateSequenceRuleRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateSequenceRuleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateSequenceRuleRequest): CanCreateSequenceRuleRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateSequenceRuleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateSequenceRuleRequest;
  static deserializeBinaryFromReader(message: CanCreateSequenceRuleRequest, reader: jspb.BinaryReader): CanCreateSequenceRuleRequest;
}

export namespace CanCreateSequenceRuleRequest {
  export type AsObject = {
  }
}

export class CanCreateSequenceRuleWithRecordTypesReply extends jspb.Message {
  getCanCreateSequenceRuleWithRecordTypes(): boolean;
  setCanCreateSequenceRuleWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateSequenceRuleWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateSequenceRuleWithRecordTypesReply): CanCreateSequenceRuleWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateSequenceRuleWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateSequenceRuleWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateSequenceRuleWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateSequenceRuleWithRecordTypesReply;
}

export namespace CanCreateSequenceRuleWithRecordTypesReply {
  export type AsObject = {
    canCreateSequenceRuleWithRecordTypes: boolean,
  }
}

export class CanCreateSequenceRuleWithRecordTypesRequest extends jspb.Message {
  clearSequenceRuleRecordTypesList(): void;
  getSequenceRuleRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setSequenceRuleRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addSequenceRuleRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateSequenceRuleWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateSequenceRuleWithRecordTypesRequest): CanCreateSequenceRuleWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateSequenceRuleWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateSequenceRuleWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateSequenceRuleWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateSequenceRuleWithRecordTypesRequest;
}

export namespace CanCreateSequenceRuleWithRecordTypesRequest {
  export type AsObject = {
    sequenceRuleRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetSequenceRuleFormForCreateReply extends jspb.Message {
  hasSequenceRuleForm(): boolean;
  clearSequenceRuleForm(): void;
  getSequenceRuleForm(): SequenceRuleForm | undefined;
  setSequenceRuleForm(value?: SequenceRuleForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRuleFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRuleFormForCreateReply): GetSequenceRuleFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRuleFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRuleFormForCreateReply;
  static deserializeBinaryFromReader(message: GetSequenceRuleFormForCreateReply, reader: jspb.BinaryReader): GetSequenceRuleFormForCreateReply;
}

export namespace GetSequenceRuleFormForCreateReply {
  export type AsObject = {
    sequenceRuleForm?: SequenceRuleForm.AsObject,
  }
}

export class GetSequenceRuleFormForCreateRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasNextAssessmentPartId(): boolean;
  clearNextAssessmentPartId(): void;
  getNextAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNextAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearSequenceRuleRecordTypesList(): void;
  getSequenceRuleRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setSequenceRuleRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addSequenceRuleRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRuleFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRuleFormForCreateRequest): GetSequenceRuleFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRuleFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRuleFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetSequenceRuleFormForCreateRequest, reader: jspb.BinaryReader): GetSequenceRuleFormForCreateRequest;
}

export namespace GetSequenceRuleFormForCreateRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    nextAssessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sequenceRuleRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateSequenceRuleReply extends jspb.Message {
  hasSequenceRule(): boolean;
  clearSequenceRule(): void;
  getSequenceRule(): SequenceRule | undefined;
  setSequenceRule(value?: SequenceRule): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateSequenceRuleReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateSequenceRuleReply): CreateSequenceRuleReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateSequenceRuleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateSequenceRuleReply;
  static deserializeBinaryFromReader(message: CreateSequenceRuleReply, reader: jspb.BinaryReader): CreateSequenceRuleReply;
}

export namespace CreateSequenceRuleReply {
  export type AsObject = {
    sequenceRule?: SequenceRule.AsObject,
  }
}

export class CreateSequenceRuleRequest extends jspb.Message {
  hasSequenceRuleForm(): boolean;
  clearSequenceRuleForm(): void;
  getSequenceRuleForm(): SequenceRuleForm | undefined;
  setSequenceRuleForm(value?: SequenceRuleForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateSequenceRuleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateSequenceRuleRequest): CreateSequenceRuleRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateSequenceRuleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateSequenceRuleRequest;
  static deserializeBinaryFromReader(message: CreateSequenceRuleRequest, reader: jspb.BinaryReader): CreateSequenceRuleRequest;
}

export namespace CreateSequenceRuleRequest {
  export type AsObject = {
    sequenceRuleForm?: SequenceRuleForm.AsObject,
  }
}

export class CanUpdateSequenceRulesReply extends jspb.Message {
  getCanUpdateSequenceRules(): boolean;
  setCanUpdateSequenceRules(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateSequenceRulesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateSequenceRulesReply): CanUpdateSequenceRulesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateSequenceRulesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateSequenceRulesReply;
  static deserializeBinaryFromReader(message: CanUpdateSequenceRulesReply, reader: jspb.BinaryReader): CanUpdateSequenceRulesReply;
}

export namespace CanUpdateSequenceRulesReply {
  export type AsObject = {
    canUpdateSequenceRules: boolean,
  }
}

export class CanUpdateSequenceRulesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateSequenceRulesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateSequenceRulesRequest): CanUpdateSequenceRulesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateSequenceRulesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateSequenceRulesRequest;
  static deserializeBinaryFromReader(message: CanUpdateSequenceRulesRequest, reader: jspb.BinaryReader): CanUpdateSequenceRulesRequest;
}

export namespace CanUpdateSequenceRulesRequest {
  export type AsObject = {
  }
}

export class GetSequenceRuleFormForUpdateReply extends jspb.Message {
  hasSequenceRuleForm(): boolean;
  clearSequenceRuleForm(): void;
  getSequenceRuleForm(): SequenceRuleForm | undefined;
  setSequenceRuleForm(value?: SequenceRuleForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRuleFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRuleFormForUpdateReply): GetSequenceRuleFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRuleFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRuleFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetSequenceRuleFormForUpdateReply, reader: jspb.BinaryReader): GetSequenceRuleFormForUpdateReply;
}

export namespace GetSequenceRuleFormForUpdateReply {
  export type AsObject = {
    sequenceRuleForm?: SequenceRuleForm.AsObject,
  }
}

export class GetSequenceRuleFormForUpdateRequest extends jspb.Message {
  hasSequenceRuleId(): boolean;
  clearSequenceRuleId(): void;
  getSequenceRuleId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSequenceRuleId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSequenceRuleFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSequenceRuleFormForUpdateRequest): GetSequenceRuleFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSequenceRuleFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSequenceRuleFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetSequenceRuleFormForUpdateRequest, reader: jspb.BinaryReader): GetSequenceRuleFormForUpdateRequest;
}

export namespace GetSequenceRuleFormForUpdateRequest {
  export type AsObject = {
    sequenceRuleId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateSequenceRuleReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateSequenceRuleReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateSequenceRuleReply): UpdateSequenceRuleReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateSequenceRuleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateSequenceRuleReply;
  static deserializeBinaryFromReader(message: UpdateSequenceRuleReply, reader: jspb.BinaryReader): UpdateSequenceRuleReply;
}

export namespace UpdateSequenceRuleReply {
  export type AsObject = {
  }
}

export class UpdateSequenceRuleRequest extends jspb.Message {
  hasSequenceRuleForm(): boolean;
  clearSequenceRuleForm(): void;
  getSequenceRuleForm(): SequenceRuleForm | undefined;
  setSequenceRuleForm(value?: SequenceRuleForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateSequenceRuleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateSequenceRuleRequest): UpdateSequenceRuleRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateSequenceRuleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateSequenceRuleRequest;
  static deserializeBinaryFromReader(message: UpdateSequenceRuleRequest, reader: jspb.BinaryReader): UpdateSequenceRuleRequest;
}

export namespace UpdateSequenceRuleRequest {
  export type AsObject = {
    sequenceRuleForm?: SequenceRuleForm.AsObject,
  }
}

export class CanDeleteSequenceRulesReply extends jspb.Message {
  getCanDeleteSequenceRules(): boolean;
  setCanDeleteSequenceRules(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteSequenceRulesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteSequenceRulesReply): CanDeleteSequenceRulesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteSequenceRulesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteSequenceRulesReply;
  static deserializeBinaryFromReader(message: CanDeleteSequenceRulesReply, reader: jspb.BinaryReader): CanDeleteSequenceRulesReply;
}

export namespace CanDeleteSequenceRulesReply {
  export type AsObject = {
    canDeleteSequenceRules: boolean,
  }
}

export class CanDeleteSequenceRulesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteSequenceRulesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteSequenceRulesRequest): CanDeleteSequenceRulesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteSequenceRulesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteSequenceRulesRequest;
  static deserializeBinaryFromReader(message: CanDeleteSequenceRulesRequest, reader: jspb.BinaryReader): CanDeleteSequenceRulesRequest;
}

export namespace CanDeleteSequenceRulesRequest {
  export type AsObject = {
  }
}

export class DeleteSequenceRuleReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteSequenceRuleReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteSequenceRuleReply): DeleteSequenceRuleReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteSequenceRuleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteSequenceRuleReply;
  static deserializeBinaryFromReader(message: DeleteSequenceRuleReply, reader: jspb.BinaryReader): DeleteSequenceRuleReply;
}

export namespace DeleteSequenceRuleReply {
  export type AsObject = {
  }
}

export class DeleteSequenceRuleRequest extends jspb.Message {
  hasSequenceRuleId(): boolean;
  clearSequenceRuleId(): void;
  getSequenceRuleId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSequenceRuleId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteSequenceRuleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteSequenceRuleRequest): DeleteSequenceRuleRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteSequenceRuleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteSequenceRuleRequest;
  static deserializeBinaryFromReader(message: DeleteSequenceRuleRequest, reader: jspb.BinaryReader): DeleteSequenceRuleRequest;
}

export namespace DeleteSequenceRuleRequest {
  export type AsObject = {
    sequenceRuleId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageSequenceRuleAliasesReply extends jspb.Message {
  getCanManageSequenceRuleAliases(): boolean;
  setCanManageSequenceRuleAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageSequenceRuleAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageSequenceRuleAliasesReply): CanManageSequenceRuleAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageSequenceRuleAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageSequenceRuleAliasesReply;
  static deserializeBinaryFromReader(message: CanManageSequenceRuleAliasesReply, reader: jspb.BinaryReader): CanManageSequenceRuleAliasesReply;
}

export namespace CanManageSequenceRuleAliasesReply {
  export type AsObject = {
    canManageSequenceRuleAliases: boolean,
  }
}

export class CanManageSequenceRuleAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageSequenceRuleAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageSequenceRuleAliasesRequest): CanManageSequenceRuleAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageSequenceRuleAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageSequenceRuleAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageSequenceRuleAliasesRequest, reader: jspb.BinaryReader): CanManageSequenceRuleAliasesRequest;
}

export namespace CanManageSequenceRuleAliasesRequest {
  export type AsObject = {
  }
}

export class AliasSequenceRuleReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasSequenceRuleReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasSequenceRuleReply): AliasSequenceRuleReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasSequenceRuleReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasSequenceRuleReply;
  static deserializeBinaryFromReader(message: AliasSequenceRuleReply, reader: jspb.BinaryReader): AliasSequenceRuleReply;
}

export namespace AliasSequenceRuleReply {
  export type AsObject = {
  }
}

export class AliasSequenceRuleRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSequenceRuleId(): boolean;
  clearSequenceRuleId(): void;
  getSequenceRuleId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSequenceRuleId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasSequenceRuleRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasSequenceRuleRequest): AliasSequenceRuleRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasSequenceRuleRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasSequenceRuleRequest;
  static deserializeBinaryFromReader(message: AliasSequenceRuleRequest, reader: jspb.BinaryReader): AliasSequenceRuleRequest;
}

export namespace AliasSequenceRuleRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sequenceRuleId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanSequenceSequenceRulesReply extends jspb.Message {
  getCanSequenceSequenceRules(): boolean;
  setCanSequenceSequenceRules(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSequenceSequenceRulesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSequenceSequenceRulesReply): CanSequenceSequenceRulesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSequenceSequenceRulesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSequenceSequenceRulesReply;
  static deserializeBinaryFromReader(message: CanSequenceSequenceRulesReply, reader: jspb.BinaryReader): CanSequenceSequenceRulesReply;
}

export namespace CanSequenceSequenceRulesReply {
  export type AsObject = {
    canSequenceSequenceRules: boolean,
  }
}

export class CanSequenceSequenceRulesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSequenceSequenceRulesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSequenceSequenceRulesRequest): CanSequenceSequenceRulesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSequenceSequenceRulesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSequenceSequenceRulesRequest;
  static deserializeBinaryFromReader(message: CanSequenceSequenceRulesRequest, reader: jspb.BinaryReader): CanSequenceSequenceRulesRequest;
}

export namespace CanSequenceSequenceRulesRequest {
  export type AsObject = {
  }
}

export class MoveSequenceRuleAheadReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveSequenceRuleAheadReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveSequenceRuleAheadReply): MoveSequenceRuleAheadReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveSequenceRuleAheadReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveSequenceRuleAheadReply;
  static deserializeBinaryFromReader(message: MoveSequenceRuleAheadReply, reader: jspb.BinaryReader): MoveSequenceRuleAheadReply;
}

export namespace MoveSequenceRuleAheadReply {
  export type AsObject = {
  }
}

export class MoveSequenceRuleAheadRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSequenceRuleId(): boolean;
  clearSequenceRuleId(): void;
  getSequenceRuleId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSequenceRuleId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveSequenceRuleAheadRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveSequenceRuleAheadRequest): MoveSequenceRuleAheadRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveSequenceRuleAheadRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveSequenceRuleAheadRequest;
  static deserializeBinaryFromReader(message: MoveSequenceRuleAheadRequest, reader: jspb.BinaryReader): MoveSequenceRuleAheadRequest;
}

export namespace MoveSequenceRuleAheadRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sequenceRuleId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveSequenceRuleBehindReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveSequenceRuleBehindReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveSequenceRuleBehindReply): MoveSequenceRuleBehindReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveSequenceRuleBehindReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveSequenceRuleBehindReply;
  static deserializeBinaryFromReader(message: MoveSequenceRuleBehindReply, reader: jspb.BinaryReader): MoveSequenceRuleBehindReply;
}

export namespace MoveSequenceRuleBehindReply {
  export type AsObject = {
  }
}

export class MoveSequenceRuleBehindRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSequenceRuleId(): boolean;
  clearSequenceRuleId(): void;
  getSequenceRuleId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSequenceRuleId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveSequenceRuleBehindRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveSequenceRuleBehindRequest): MoveSequenceRuleBehindRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveSequenceRuleBehindRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveSequenceRuleBehindRequest;
  static deserializeBinaryFromReader(message: MoveSequenceRuleBehindRequest, reader: jspb.BinaryReader): MoveSequenceRuleBehindRequest;
}

export namespace MoveSequenceRuleBehindRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sequenceRuleId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class OrderSequenceRulesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderSequenceRulesReply.AsObject;
  static toObject(includeInstance: boolean, msg: OrderSequenceRulesReply): OrderSequenceRulesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderSequenceRulesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderSequenceRulesReply;
  static deserializeBinaryFromReader(message: OrderSequenceRulesReply, reader: jspb.BinaryReader): OrderSequenceRulesReply;
}

export namespace OrderSequenceRulesReply {
  export type AsObject = {
  }
}

export class OrderSequenceRulesRequest extends jspb.Message {
  hasAssessmentPartId(): boolean;
  clearAssessmentPartId(): void;
  getAssessmentPartId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentPartId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearSequenceRuleIdsList(): void;
  getSequenceRuleIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setSequenceRuleIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addSequenceRuleIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderSequenceRulesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: OrderSequenceRulesRequest): OrderSequenceRulesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderSequenceRulesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderSequenceRulesRequest;
  static deserializeBinaryFromReader(message: OrderSequenceRulesRequest, reader: jspb.BinaryReader): OrderSequenceRulesRequest;
}

export namespace OrderSequenceRulesRequest {
  export type AsObject = {
    assessmentPartId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    sequenceRuleIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

