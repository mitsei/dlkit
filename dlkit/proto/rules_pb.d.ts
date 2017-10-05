// package: dlkit.proto.rules
// file: dlkit/proto/rules.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";

export class Rule extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Rule.AsObject;
  static toObject(includeInstance: boolean, msg: Rule): Rule.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Rule, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Rule;
  static deserializeBinaryFromReader(message: Rule, reader: jspb.BinaryReader): Rule;
}

export namespace Rule {
  export type AsObject = {
  }
}

export class RuleQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleQuery.AsObject;
  static toObject(includeInstance: boolean, msg: RuleQuery): RuleQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleQuery;
  static deserializeBinaryFromReader(message: RuleQuery, reader: jspb.BinaryReader): RuleQuery;
}

export namespace RuleQuery {
  export type AsObject = {
  }
}

export class RuleQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: RuleQueryInspector): RuleQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleQueryInspector;
  static deserializeBinaryFromReader(message: RuleQueryInspector, reader: jspb.BinaryReader): RuleQueryInspector;
}

export namespace RuleQueryInspector {
  export type AsObject = {
  }
}

export class RuleForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleForm.AsObject;
  static toObject(includeInstance: boolean, msg: RuleForm): RuleForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleForm;
  static deserializeBinaryFromReader(message: RuleForm, reader: jspb.BinaryReader): RuleForm;
}

export namespace RuleForm {
  export type AsObject = {
  }
}

export class RuleSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: RuleSearchOrder): RuleSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleSearchOrder;
  static deserializeBinaryFromReader(message: RuleSearchOrder, reader: jspb.BinaryReader): RuleSearchOrder;
}

export namespace RuleSearchOrder {
  export type AsObject = {
  }
}

export class RuleSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleSearch.AsObject;
  static toObject(includeInstance: boolean, msg: RuleSearch): RuleSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleSearch;
  static deserializeBinaryFromReader(message: RuleSearch, reader: jspb.BinaryReader): RuleSearch;
}

export namespace RuleSearch {
  export type AsObject = {
  }
}

export class RuleSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: RuleSearchResults): RuleSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleSearchResults;
  static deserializeBinaryFromReader(message: RuleSearchResults, reader: jspb.BinaryReader): RuleSearchResults;
}

export namespace RuleSearchResults {
  export type AsObject = {
  }
}

export class RuleList extends jspb.Message {
  clearRulesList(): void;
  getRulesList(): Array<Rule>;
  setRulesList(value: Array<Rule>): void;
  addRules(value?: Rule, index?: number): Rule;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RuleList.AsObject;
  static toObject(includeInstance: boolean, msg: RuleList): RuleList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RuleList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RuleList;
  static deserializeBinaryFromReader(message: RuleList, reader: jspb.BinaryReader): RuleList;
}

export namespace RuleList {
  export type AsObject = {
    rulesList: Array<Rule.AsObject>,
  }
}

export class Engine extends jspb.Message {
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
  toObject(includeInstance?: boolean): Engine.AsObject;
  static toObject(includeInstance: boolean, msg: Engine): Engine.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Engine, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Engine;
  static deserializeBinaryFromReader(message: Engine, reader: jspb.BinaryReader): Engine;
}

export namespace Engine {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class EngineQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineQuery.AsObject;
  static toObject(includeInstance: boolean, msg: EngineQuery): EngineQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineQuery;
  static deserializeBinaryFromReader(message: EngineQuery, reader: jspb.BinaryReader): EngineQuery;
}

export namespace EngineQuery {
  export type AsObject = {
  }
}

export class EngineQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: EngineQueryInspector): EngineQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineQueryInspector;
  static deserializeBinaryFromReader(message: EngineQueryInspector, reader: jspb.BinaryReader): EngineQueryInspector;
}

export namespace EngineQueryInspector {
  export type AsObject = {
  }
}

export class EngineForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineForm.AsObject;
  static toObject(includeInstance: boolean, msg: EngineForm): EngineForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineForm;
  static deserializeBinaryFromReader(message: EngineForm, reader: jspb.BinaryReader): EngineForm;
}

export namespace EngineForm {
  export type AsObject = {
  }
}

export class EngineSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: EngineSearchOrder): EngineSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineSearchOrder;
  static deserializeBinaryFromReader(message: EngineSearchOrder, reader: jspb.BinaryReader): EngineSearchOrder;
}

export namespace EngineSearchOrder {
  export type AsObject = {
  }
}

export class EngineSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineSearch.AsObject;
  static toObject(includeInstance: boolean, msg: EngineSearch): EngineSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineSearch;
  static deserializeBinaryFromReader(message: EngineSearch, reader: jspb.BinaryReader): EngineSearch;
}

export namespace EngineSearch {
  export type AsObject = {
  }
}

export class EngineSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: EngineSearchResults): EngineSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineSearchResults;
  static deserializeBinaryFromReader(message: EngineSearchResults, reader: jspb.BinaryReader): EngineSearchResults;
}

export namespace EngineSearchResults {
  export type AsObject = {
  }
}

export class EngineList extends jspb.Message {
  clearEnginesList(): void;
  getEnginesList(): Array<Engine>;
  setEnginesList(value: Array<Engine>): void;
  addEngines(value?: Engine, index?: number): Engine;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineList.AsObject;
  static toObject(includeInstance: boolean, msg: EngineList): EngineList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineList;
  static deserializeBinaryFromReader(message: EngineList, reader: jspb.BinaryReader): EngineList;
}

export namespace EngineList {
  export type AsObject = {
    enginesList: Array<Engine.AsObject>,
  }
}

export class EngineNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineNode.AsObject;
  static toObject(includeInstance: boolean, msg: EngineNode): EngineNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineNode;
  static deserializeBinaryFromReader(message: EngineNode, reader: jspb.BinaryReader): EngineNode;
}

export namespace EngineNode {
  export type AsObject = {
  }
}

export class EngineNodeList extends jspb.Message {
  clearEngineNodesList(): void;
  getEngineNodesList(): Array<EngineNode>;
  setEngineNodesList(value: Array<EngineNode>): void;
  addEngineNodes(value?: EngineNode, index?: number): EngineNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EngineNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: EngineNodeList): EngineNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EngineNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EngineNodeList;
  static deserializeBinaryFromReader(message: EngineNodeList, reader: jspb.BinaryReader): EngineNodeList;
}

export namespace EngineNodeList {
  export type AsObject = {
    engineNodesList: Array<EngineNode.AsObject>,
  }
}

export class Condition extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Condition.AsObject;
  static toObject(includeInstance: boolean, msg: Condition): Condition.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Condition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Condition;
  static deserializeBinaryFromReader(message: Condition, reader: jspb.BinaryReader): Condition;
}

export namespace Condition {
  export type AsObject = {
  }
}

export class Result extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Result.AsObject;
  static toObject(includeInstance: boolean, msg: Result): Result.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Result, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Result;
  static deserializeBinaryFromReader(message: Result, reader: jspb.BinaryReader): Result;
}

export namespace Result {
  export type AsObject = {
  }
}

