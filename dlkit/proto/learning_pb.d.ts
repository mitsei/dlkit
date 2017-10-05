// package: dlkit.proto.learning
// file: dlkit/proto/learning.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Objective extends jspb.Message {
  hasAssessment(): boolean;
  clearAssessment(): void;
  getAssessment(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessment(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCognitiveProcess(): boolean;
  clearCognitiveProcess(): void;
  getCognitiveProcess(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCognitiveProcess(value?: dlkit_primordium_id_primitives_pb.Id): void;

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

  hasKnowledgeCategory(): boolean;
  clearKnowledgeCategory(): void;
  getKnowledgeCategory(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setKnowledgeCategory(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBank(): boolean;
  clearObjectiveBank(): void;
  getObjectiveBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setObjectiveBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Objective.AsObject;
  static toObject(includeInstance: boolean, msg: Objective): Objective.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Objective, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Objective;
  static deserializeBinaryFromReader(message: Objective, reader: jspb.BinaryReader): Objective;
}

export namespace Objective {
  export type AsObject = {
    assessment?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    cognitiveProcess?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    knowledgeCategory?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class ObjectiveQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveQuery): ObjectiveQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveQuery;
  static deserializeBinaryFromReader(message: ObjectiveQuery, reader: jspb.BinaryReader): ObjectiveQuery;
}

export namespace ObjectiveQuery {
  export type AsObject = {
  }
}

export class ObjectiveQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveQueryInspector): ObjectiveQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveQueryInspector;
  static deserializeBinaryFromReader(message: ObjectiveQueryInspector, reader: jspb.BinaryReader): ObjectiveQueryInspector;
}

export namespace ObjectiveQueryInspector {
  export type AsObject = {
  }
}

export class ObjectiveForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveForm.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveForm): ObjectiveForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveForm;
  static deserializeBinaryFromReader(message: ObjectiveForm, reader: jspb.BinaryReader): ObjectiveForm;
}

export namespace ObjectiveForm {
  export type AsObject = {
  }
}

export class ObjectiveSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveSearchOrder): ObjectiveSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveSearchOrder;
  static deserializeBinaryFromReader(message: ObjectiveSearchOrder, reader: jspb.BinaryReader): ObjectiveSearchOrder;
}

export namespace ObjectiveSearchOrder {
  export type AsObject = {
  }
}

export class ObjectiveSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveSearch): ObjectiveSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveSearch;
  static deserializeBinaryFromReader(message: ObjectiveSearch, reader: jspb.BinaryReader): ObjectiveSearch;
}

export namespace ObjectiveSearch {
  export type AsObject = {
  }
}

export class ObjectiveSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveSearchResults): ObjectiveSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveSearchResults;
  static deserializeBinaryFromReader(message: ObjectiveSearchResults, reader: jspb.BinaryReader): ObjectiveSearchResults;
}

export namespace ObjectiveSearchResults {
  export type AsObject = {
  }
}

export class ObjectiveList extends jspb.Message {
  clearObjectivesList(): void;
  getObjectivesList(): Array<Objective>;
  setObjectivesList(value: Array<Objective>): void;
  addObjectives(value?: Objective, index?: number): Objective;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveList.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveList): ObjectiveList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveList;
  static deserializeBinaryFromReader(message: ObjectiveList, reader: jspb.BinaryReader): ObjectiveList;
}

export namespace ObjectiveList {
  export type AsObject = {
    objectivesList: Array<Objective.AsObject>,
  }
}

export class ObjectiveNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveNode.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveNode): ObjectiveNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveNode;
  static deserializeBinaryFromReader(message: ObjectiveNode, reader: jspb.BinaryReader): ObjectiveNode;
}

export namespace ObjectiveNode {
  export type AsObject = {
  }
}

export class ObjectiveNodeList extends jspb.Message {
  clearObjectiveNodesList(): void;
  getObjectiveNodesList(): Array<ObjectiveNode>;
  setObjectiveNodesList(value: Array<ObjectiveNode>): void;
  addObjectiveNodes(value?: ObjectiveNode, index?: number): ObjectiveNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveNodeList): ObjectiveNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveNodeList;
  static deserializeBinaryFromReader(message: ObjectiveNodeList, reader: jspb.BinaryReader): ObjectiveNodeList;
}

export namespace ObjectiveNodeList {
  export type AsObject = {
    objectiveNodesList: Array<ObjectiveNode.AsObject>,
  }
}

export class Activity extends jspb.Message {
  clearAssessmentsList(): void;
  getAssessmentsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssessmentsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssessments(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  clearAssetsList(): void;
  getAssetsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssetsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssets(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  clearCoursesList(): void;
  getCoursesList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setCoursesList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addCourses(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

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

  hasObjective(): boolean;
  clearObjective(): void;
  getObjective(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjective(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBank(): boolean;
  clearObjectiveBank(): void;
  getObjectiveBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setObjectiveBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Activity.AsObject;
  static toObject(includeInstance: boolean, msg: Activity): Activity.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Activity, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Activity;
  static deserializeBinaryFromReader(message: Activity, reader: jspb.BinaryReader): Activity;
}

export namespace Activity {
  export type AsObject = {
    assessmentsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    assetsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    coursesList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objective?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class ActivityQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivityQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ActivityQuery): ActivityQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivityQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivityQuery;
  static deserializeBinaryFromReader(message: ActivityQuery, reader: jspb.BinaryReader): ActivityQuery;
}

export namespace ActivityQuery {
  export type AsObject = {
  }
}

export class ActivityQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivityQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ActivityQueryInspector): ActivityQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivityQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivityQueryInspector;
  static deserializeBinaryFromReader(message: ActivityQueryInspector, reader: jspb.BinaryReader): ActivityQueryInspector;
}

export namespace ActivityQueryInspector {
  export type AsObject = {
  }
}

export class ActivityForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivityForm.AsObject;
  static toObject(includeInstance: boolean, msg: ActivityForm): ActivityForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivityForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivityForm;
  static deserializeBinaryFromReader(message: ActivityForm, reader: jspb.BinaryReader): ActivityForm;
}

export namespace ActivityForm {
  export type AsObject = {
  }
}

export class ActivitySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivitySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ActivitySearchOrder): ActivitySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivitySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivitySearchOrder;
  static deserializeBinaryFromReader(message: ActivitySearchOrder, reader: jspb.BinaryReader): ActivitySearchOrder;
}

export namespace ActivitySearchOrder {
  export type AsObject = {
  }
}

export class ActivitySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivitySearch.AsObject;
  static toObject(includeInstance: boolean, msg: ActivitySearch): ActivitySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivitySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivitySearch;
  static deserializeBinaryFromReader(message: ActivitySearch, reader: jspb.BinaryReader): ActivitySearch;
}

export namespace ActivitySearch {
  export type AsObject = {
  }
}

export class ActivitySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivitySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ActivitySearchResults): ActivitySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivitySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivitySearchResults;
  static deserializeBinaryFromReader(message: ActivitySearchResults, reader: jspb.BinaryReader): ActivitySearchResults;
}

export namespace ActivitySearchResults {
  export type AsObject = {
  }
}

export class ActivityList extends jspb.Message {
  clearActivitiesList(): void;
  getActivitiesList(): Array<Activity>;
  setActivitiesList(value: Array<Activity>): void;
  addActivities(value?: Activity, index?: number): Activity;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActivityList.AsObject;
  static toObject(includeInstance: boolean, msg: ActivityList): ActivityList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ActivityList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActivityList;
  static deserializeBinaryFromReader(message: ActivityList, reader: jspb.BinaryReader): ActivityList;
}

export namespace ActivityList {
  export type AsObject = {
    activitiesList: Array<Activity.AsObject>,
  }
}

export class Proficiency extends jspb.Message {
  getCompletion(): number;
  setCompletion(value: number): void;

  hasLevel(): boolean;
  clearLevel(): void;
  getLevel(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLevel(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjective(): boolean;
  clearObjective(): void;
  getObjective(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjective(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBank(): boolean;
  clearObjectiveBank(): void;
  getObjectiveBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setObjectiveBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasResource(): boolean;
  clearResource(): void;
  getResource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Proficiency.AsObject;
  static toObject(includeInstance: boolean, msg: Proficiency): Proficiency.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Proficiency, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Proficiency;
  static deserializeBinaryFromReader(message: Proficiency, reader: jspb.BinaryReader): Proficiency;
}

export namespace Proficiency {
  export type AsObject = {
    completion: number,
    level?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objective?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    resource?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ProficiencyQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencyQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencyQuery): ProficiencyQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencyQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencyQuery;
  static deserializeBinaryFromReader(message: ProficiencyQuery, reader: jspb.BinaryReader): ProficiencyQuery;
}

export namespace ProficiencyQuery {
  export type AsObject = {
  }
}

export class ProficiencyQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencyQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencyQueryInspector): ProficiencyQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencyQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencyQueryInspector;
  static deserializeBinaryFromReader(message: ProficiencyQueryInspector, reader: jspb.BinaryReader): ProficiencyQueryInspector;
}

export namespace ProficiencyQueryInspector {
  export type AsObject = {
  }
}

export class ProficiencyForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencyForm.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencyForm): ProficiencyForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencyForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencyForm;
  static deserializeBinaryFromReader(message: ProficiencyForm, reader: jspb.BinaryReader): ProficiencyForm;
}

export namespace ProficiencyForm {
  export type AsObject = {
  }
}

export class ProficiencySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencySearchOrder): ProficiencySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencySearchOrder;
  static deserializeBinaryFromReader(message: ProficiencySearchOrder, reader: jspb.BinaryReader): ProficiencySearchOrder;
}

export namespace ProficiencySearchOrder {
  export type AsObject = {
  }
}

export class ProficiencySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencySearch.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencySearch): ProficiencySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencySearch;
  static deserializeBinaryFromReader(message: ProficiencySearch, reader: jspb.BinaryReader): ProficiencySearch;
}

export namespace ProficiencySearch {
  export type AsObject = {
  }
}

export class ProficiencySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencySearchResults): ProficiencySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencySearchResults;
  static deserializeBinaryFromReader(message: ProficiencySearchResults, reader: jspb.BinaryReader): ProficiencySearchResults;
}

export namespace ProficiencySearchResults {
  export type AsObject = {
  }
}

export class ProficiencyList extends jspb.Message {
  clearProficienciesList(): void;
  getProficienciesList(): Array<Proficiency>;
  setProficienciesList(value: Array<Proficiency>): void;
  addProficiencies(value?: Proficiency, index?: number): Proficiency;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProficiencyList.AsObject;
  static toObject(includeInstance: boolean, msg: ProficiencyList): ProficiencyList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProficiencyList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProficiencyList;
  static deserializeBinaryFromReader(message: ProficiencyList, reader: jspb.BinaryReader): ProficiencyList;
}

export namespace ProficiencyList {
  export type AsObject = {
    proficienciesList: Array<Proficiency.AsObject>,
  }
}

export class ObjectiveBank extends jspb.Message {
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
  toObject(includeInstance?: boolean): ObjectiveBank.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBank): ObjectiveBank.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBank, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBank;
  static deserializeBinaryFromReader(message: ObjectiveBank, reader: jspb.BinaryReader): ObjectiveBank;
}

export namespace ObjectiveBank {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class ObjectiveBankQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankQuery): ObjectiveBankQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankQuery;
  static deserializeBinaryFromReader(message: ObjectiveBankQuery, reader: jspb.BinaryReader): ObjectiveBankQuery;
}

export namespace ObjectiveBankQuery {
  export type AsObject = {
  }
}

export class ObjectiveBankQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankQueryInspector): ObjectiveBankQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankQueryInspector;
  static deserializeBinaryFromReader(message: ObjectiveBankQueryInspector, reader: jspb.BinaryReader): ObjectiveBankQueryInspector;
}

export namespace ObjectiveBankQueryInspector {
  export type AsObject = {
  }
}

export class ObjectiveBankForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankForm.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankForm): ObjectiveBankForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankForm;
  static deserializeBinaryFromReader(message: ObjectiveBankForm, reader: jspb.BinaryReader): ObjectiveBankForm;
}

export namespace ObjectiveBankForm {
  export type AsObject = {
  }
}

export class ObjectiveBankSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankSearchOrder): ObjectiveBankSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankSearchOrder;
  static deserializeBinaryFromReader(message: ObjectiveBankSearchOrder, reader: jspb.BinaryReader): ObjectiveBankSearchOrder;
}

export namespace ObjectiveBankSearchOrder {
  export type AsObject = {
  }
}

export class ObjectiveBankSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankSearch): ObjectiveBankSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankSearch;
  static deserializeBinaryFromReader(message: ObjectiveBankSearch, reader: jspb.BinaryReader): ObjectiveBankSearch;
}

export namespace ObjectiveBankSearch {
  export type AsObject = {
  }
}

export class ObjectiveBankSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankSearchResults): ObjectiveBankSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankSearchResults;
  static deserializeBinaryFromReader(message: ObjectiveBankSearchResults, reader: jspb.BinaryReader): ObjectiveBankSearchResults;
}

export namespace ObjectiveBankSearchResults {
  export type AsObject = {
  }
}

export class ObjectiveBankList extends jspb.Message {
  clearObjectiveBanksList(): void;
  getObjectiveBanksList(): Array<ObjectiveBank>;
  setObjectiveBanksList(value: Array<ObjectiveBank>): void;
  addObjectiveBanks(value?: ObjectiveBank, index?: number): ObjectiveBank;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankList.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankList): ObjectiveBankList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankList;
  static deserializeBinaryFromReader(message: ObjectiveBankList, reader: jspb.BinaryReader): ObjectiveBankList;
}

export namespace ObjectiveBankList {
  export type AsObject = {
    objectiveBanksList: Array<ObjectiveBank.AsObject>,
  }
}

export class ObjectiveBankNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankNode.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankNode): ObjectiveBankNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankNode;
  static deserializeBinaryFromReader(message: ObjectiveBankNode, reader: jspb.BinaryReader): ObjectiveBankNode;
}

export namespace ObjectiveBankNode {
  export type AsObject = {
  }
}

export class ObjectiveBankNodeList extends jspb.Message {
  clearObjectiveBankNodesList(): void;
  getObjectiveBankNodesList(): Array<ObjectiveBankNode>;
  setObjectiveBankNodesList(value: Array<ObjectiveBankNode>): void;
  addObjectiveBankNodes(value?: ObjectiveBankNode, index?: number): ObjectiveBankNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ObjectiveBankNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: ObjectiveBankNodeList): ObjectiveBankNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ObjectiveBankNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ObjectiveBankNodeList;
  static deserializeBinaryFromReader(message: ObjectiveBankNodeList, reader: jspb.BinaryReader): ObjectiveBankNodeList;
}

export namespace ObjectiveBankNodeList {
  export type AsObject = {
    objectiveBankNodesList: Array<ObjectiveBankNode.AsObject>,
  }
}

export class GetObjectiveBankIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankIdReply): GetObjectiveBankIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankIdReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankIdReply, reader: jspb.BinaryReader): GetObjectiveBankIdReply;
}

export namespace GetObjectiveBankIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBankIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankIdRequest): GetObjectiveBankIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankIdRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankIdRequest, reader: jspb.BinaryReader): GetObjectiveBankIdRequest;
}

export namespace GetObjectiveBankIdRequest {
  export type AsObject = {
  }
}

export class GetObjectiveBankReply extends jspb.Message {
  hasObjectiveBank(): boolean;
  clearObjectiveBank(): void;
  getObjectiveBank(): ObjectiveBank | undefined;
  setObjectiveBank(value?: ObjectiveBank): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankReply): GetObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankReply, reader: jspb.BinaryReader): GetObjectiveBankReply;
}

export namespace GetObjectiveBankReply {
  export type AsObject = {
    objectiveBank?: ObjectiveBank.AsObject,
  }
}

export class GetObjectiveBankRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankRequest): GetObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankRequest, reader: jspb.BinaryReader): GetObjectiveBankRequest;
}

export namespace GetObjectiveBankRequest {
  export type AsObject = {
  }
}

export class CanLookupObjectivesReply extends jspb.Message {
  getCanLookupObjectives(): boolean;
  setCanLookupObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectivesReply): CanLookupObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectivesReply;
  static deserializeBinaryFromReader(message: CanLookupObjectivesReply, reader: jspb.BinaryReader): CanLookupObjectivesReply;
}

export namespace CanLookupObjectivesReply {
  export type AsObject = {
    canLookupObjectives: boolean,
  }
}

export class CanLookupObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectivesRequest): CanLookupObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectivesRequest;
  static deserializeBinaryFromReader(message: CanLookupObjectivesRequest, reader: jspb.BinaryReader): CanLookupObjectivesRequest;
}

export namespace CanLookupObjectivesRequest {
  export type AsObject = {
  }
}

export class UseComparativeObjectiveViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeObjectiveViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeObjectiveViewReply): UseComparativeObjectiveViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeObjectiveViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeObjectiveViewReply;
  static deserializeBinaryFromReader(message: UseComparativeObjectiveViewReply, reader: jspb.BinaryReader): UseComparativeObjectiveViewReply;
}

export namespace UseComparativeObjectiveViewReply {
  export type AsObject = {
  }
}

export class UseComparativeObjectiveViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeObjectiveViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeObjectiveViewRequest): UseComparativeObjectiveViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeObjectiveViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeObjectiveViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeObjectiveViewRequest, reader: jspb.BinaryReader): UseComparativeObjectiveViewRequest;
}

export namespace UseComparativeObjectiveViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryObjectiveViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryObjectiveViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryObjectiveViewReply): UsePlenaryObjectiveViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryObjectiveViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryObjectiveViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryObjectiveViewReply, reader: jspb.BinaryReader): UsePlenaryObjectiveViewReply;
}

export namespace UsePlenaryObjectiveViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryObjectiveViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryObjectiveViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryObjectiveViewRequest): UsePlenaryObjectiveViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryObjectiveViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryObjectiveViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryObjectiveViewRequest, reader: jspb.BinaryReader): UsePlenaryObjectiveViewRequest;
}

export namespace UsePlenaryObjectiveViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedObjectiveBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedObjectiveBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedObjectiveBankViewReply): UseFederatedObjectiveBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedObjectiveBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedObjectiveBankViewReply;
  static deserializeBinaryFromReader(message: UseFederatedObjectiveBankViewReply, reader: jspb.BinaryReader): UseFederatedObjectiveBankViewReply;
}

export namespace UseFederatedObjectiveBankViewReply {
  export type AsObject = {
  }
}

export class UseFederatedObjectiveBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedObjectiveBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedObjectiveBankViewRequest): UseFederatedObjectiveBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedObjectiveBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedObjectiveBankViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedObjectiveBankViewRequest, reader: jspb.BinaryReader): UseFederatedObjectiveBankViewRequest;
}

export namespace UseFederatedObjectiveBankViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedObjectiveBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedObjectiveBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedObjectiveBankViewReply): UseIsolatedObjectiveBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedObjectiveBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedObjectiveBankViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedObjectiveBankViewReply, reader: jspb.BinaryReader): UseIsolatedObjectiveBankViewReply;
}

export namespace UseIsolatedObjectiveBankViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedObjectiveBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedObjectiveBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedObjectiveBankViewRequest): UseIsolatedObjectiveBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedObjectiveBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedObjectiveBankViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedObjectiveBankViewRequest, reader: jspb.BinaryReader): UseIsolatedObjectiveBankViewRequest;
}

export namespace UseIsolatedObjectiveBankViewRequest {
  export type AsObject = {
  }
}

export class GetObjectiveReply extends jspb.Message {
  hasObjective(): boolean;
  clearObjective(): void;
  getObjective(): Objective | undefined;
  setObjective(value?: Objective): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveReply): GetObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveReply;
  static deserializeBinaryFromReader(message: GetObjectiveReply, reader: jspb.BinaryReader): GetObjectiveReply;
}

export namespace GetObjectiveReply {
  export type AsObject = {
    objective?: Objective.AsObject,
  }
}

export class GetObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveRequest): GetObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveRequest;
  static deserializeBinaryFromReader(message: GetObjectiveRequest, reader: jspb.BinaryReader): GetObjectiveRequest;
}

export namespace GetObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectivesByIdsRequest extends jspb.Message {
  clearObjectiveIdsList(): void;
  getObjectiveIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByIdsRequest): GetObjectivesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByIdsRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByIdsRequest, reader: jspb.BinaryReader): GetObjectivesByIdsRequest;
}

export namespace GetObjectivesByIdsRequest {
  export type AsObject = {
    objectiveIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetObjectivesByGenusTypeRequest extends jspb.Message {
  hasObjectiveGenusType(): boolean;
  clearObjectiveGenusType(): void;
  getObjectiveGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setObjectiveGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByGenusTypeRequest): GetObjectivesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByGenusTypeRequest, reader: jspb.BinaryReader): GetObjectivesByGenusTypeRequest;
}

export namespace GetObjectivesByGenusTypeRequest {
  export type AsObject = {
    objectiveGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetObjectivesByParentGenusTypeRequest extends jspb.Message {
  hasObjectiveGenusType(): boolean;
  clearObjectiveGenusType(): void;
  getObjectiveGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setObjectiveGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByParentGenusTypeRequest): GetObjectivesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetObjectivesByParentGenusTypeRequest;
}

export namespace GetObjectivesByParentGenusTypeRequest {
  export type AsObject = {
    objectiveGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetObjectivesByRecordTypeRequest extends jspb.Message {
  hasObjectiveRecordType(): boolean;
  clearObjectiveRecordType(): void;
  getObjectiveRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setObjectiveRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByRecordTypeRequest): GetObjectivesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByRecordTypeRequest, reader: jspb.BinaryReader): GetObjectivesByRecordTypeRequest;
}

export namespace GetObjectivesByRecordTypeRequest {
  export type AsObject = {
    objectiveRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesRequest): GetObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesRequest;
  static deserializeBinaryFromReader(message: GetObjectivesRequest, reader: jspb.BinaryReader): GetObjectivesRequest;
}

export namespace GetObjectivesRequest {
  export type AsObject = {
  }
}

export class CanSearchObjectivesReply extends jspb.Message {
  getCanSearchObjectives(): boolean;
  setCanSearchObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchObjectivesReply): CanSearchObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchObjectivesReply;
  static deserializeBinaryFromReader(message: CanSearchObjectivesReply, reader: jspb.BinaryReader): CanSearchObjectivesReply;
}

export namespace CanSearchObjectivesReply {
  export type AsObject = {
    canSearchObjectives: boolean,
  }
}

export class CanSearchObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchObjectivesRequest): CanSearchObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchObjectivesRequest;
  static deserializeBinaryFromReader(message: CanSearchObjectivesRequest, reader: jspb.BinaryReader): CanSearchObjectivesRequest;
}

export namespace CanSearchObjectivesRequest {
  export type AsObject = {
  }
}

export class GetObjectiveQueryReply extends jspb.Message {
  hasObjectiveQuery(): boolean;
  clearObjectiveQuery(): void;
  getObjectiveQuery(): ObjectiveQuery | undefined;
  setObjectiveQuery(value?: ObjectiveQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveQueryReply): GetObjectiveQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveQueryReply;
  static deserializeBinaryFromReader(message: GetObjectiveQueryReply, reader: jspb.BinaryReader): GetObjectiveQueryReply;
}

export namespace GetObjectiveQueryReply {
  export type AsObject = {
    objectiveQuery?: ObjectiveQuery.AsObject,
  }
}

export class GetObjectiveQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveQueryRequest): GetObjectiveQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveQueryRequest;
  static deserializeBinaryFromReader(message: GetObjectiveQueryRequest, reader: jspb.BinaryReader): GetObjectiveQueryRequest;
}

export namespace GetObjectiveQueryRequest {
  export type AsObject = {
  }
}

export class GetObjectivesByQueryRequest extends jspb.Message {
  hasObjectiveQuery(): boolean;
  clearObjectiveQuery(): void;
  getObjectiveQuery(): ObjectiveQuery | undefined;
  setObjectiveQuery(value?: ObjectiveQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByQueryRequest): GetObjectivesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByQueryRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByQueryRequest, reader: jspb.BinaryReader): GetObjectivesByQueryRequest;
}

export namespace GetObjectivesByQueryRequest {
  export type AsObject = {
    objectiveQuery?: ObjectiveQuery.AsObject,
  }
}

export class CanCreateObjectivesReply extends jspb.Message {
  getCanCreateObjectives(): boolean;
  setCanCreateObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectivesReply): CanCreateObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectivesReply;
  static deserializeBinaryFromReader(message: CanCreateObjectivesReply, reader: jspb.BinaryReader): CanCreateObjectivesReply;
}

export namespace CanCreateObjectivesReply {
  export type AsObject = {
    canCreateObjectives: boolean,
  }
}

export class CanCreateObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectivesRequest): CanCreateObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectivesRequest;
  static deserializeBinaryFromReader(message: CanCreateObjectivesRequest, reader: jspb.BinaryReader): CanCreateObjectivesRequest;
}

export namespace CanCreateObjectivesRequest {
  export type AsObject = {
  }
}

export class CanCreateObjectiveWithRecordTypesReply extends jspb.Message {
  getCanCreateObjectiveWithRecordTypes(): boolean;
  setCanCreateObjectiveWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectiveWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectiveWithRecordTypesReply): CanCreateObjectiveWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectiveWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectiveWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateObjectiveWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateObjectiveWithRecordTypesReply;
}

export namespace CanCreateObjectiveWithRecordTypesReply {
  export type AsObject = {
    canCreateObjectiveWithRecordTypes: boolean,
  }
}

export class CanCreateObjectiveWithRecordTypesRequest extends jspb.Message {
  clearObjectiveRecordTypesList(): void;
  getObjectiveRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setObjectiveRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addObjectiveRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectiveWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectiveWithRecordTypesRequest): CanCreateObjectiveWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectiveWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectiveWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateObjectiveWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateObjectiveWithRecordTypesRequest;
}

export namespace CanCreateObjectiveWithRecordTypesRequest {
  export type AsObject = {
    objectiveRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetObjectiveFormForCreateReply extends jspb.Message {
  hasObjectiveForm(): boolean;
  clearObjectiveForm(): void;
  getObjectiveForm(): ObjectiveForm | undefined;
  setObjectiveForm(value?: ObjectiveForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveFormForCreateReply): GetObjectiveFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveFormForCreateReply;
  static deserializeBinaryFromReader(message: GetObjectiveFormForCreateReply, reader: jspb.BinaryReader): GetObjectiveFormForCreateReply;
}

export namespace GetObjectiveFormForCreateReply {
  export type AsObject = {
    objectiveForm?: ObjectiveForm.AsObject,
  }
}

export class GetObjectiveFormForCreateRequest extends jspb.Message {
  clearObjectiveRecordTypesList(): void;
  getObjectiveRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setObjectiveRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addObjectiveRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveFormForCreateRequest): GetObjectiveFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetObjectiveFormForCreateRequest, reader: jspb.BinaryReader): GetObjectiveFormForCreateRequest;
}

export namespace GetObjectiveFormForCreateRequest {
  export type AsObject = {
    objectiveRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateObjectiveReply extends jspb.Message {
  hasObjective(): boolean;
  clearObjective(): void;
  getObjective(): Objective | undefined;
  setObjective(value?: Objective): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateObjectiveReply): CreateObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateObjectiveReply;
  static deserializeBinaryFromReader(message: CreateObjectiveReply, reader: jspb.BinaryReader): CreateObjectiveReply;
}

export namespace CreateObjectiveReply {
  export type AsObject = {
    objective?: Objective.AsObject,
  }
}

export class CreateObjectiveRequest extends jspb.Message {
  hasObjectiveForm(): boolean;
  clearObjectiveForm(): void;
  getObjectiveForm(): ObjectiveForm | undefined;
  setObjectiveForm(value?: ObjectiveForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateObjectiveRequest): CreateObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateObjectiveRequest;
  static deserializeBinaryFromReader(message: CreateObjectiveRequest, reader: jspb.BinaryReader): CreateObjectiveRequest;
}

export namespace CreateObjectiveRequest {
  export type AsObject = {
    objectiveForm?: ObjectiveForm.AsObject,
  }
}

export class CanUpdateObjectivesReply extends jspb.Message {
  getCanUpdateObjectives(): boolean;
  setCanUpdateObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateObjectivesReply): CanUpdateObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateObjectivesReply;
  static deserializeBinaryFromReader(message: CanUpdateObjectivesReply, reader: jspb.BinaryReader): CanUpdateObjectivesReply;
}

export namespace CanUpdateObjectivesReply {
  export type AsObject = {
    canUpdateObjectives: boolean,
  }
}

export class CanUpdateObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateObjectivesRequest): CanUpdateObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateObjectivesRequest;
  static deserializeBinaryFromReader(message: CanUpdateObjectivesRequest, reader: jspb.BinaryReader): CanUpdateObjectivesRequest;
}

export namespace CanUpdateObjectivesRequest {
  export type AsObject = {
  }
}

export class GetObjectiveFormForUpdateReply extends jspb.Message {
  hasObjectiveForm(): boolean;
  clearObjectiveForm(): void;
  getObjectiveForm(): ObjectiveForm | undefined;
  setObjectiveForm(value?: ObjectiveForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveFormForUpdateReply): GetObjectiveFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetObjectiveFormForUpdateReply, reader: jspb.BinaryReader): GetObjectiveFormForUpdateReply;
}

export namespace GetObjectiveFormForUpdateReply {
  export type AsObject = {
    objectiveForm?: ObjectiveForm.AsObject,
  }
}

export class GetObjectiveFormForUpdateRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveFormForUpdateRequest): GetObjectiveFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetObjectiveFormForUpdateRequest, reader: jspb.BinaryReader): GetObjectiveFormForUpdateRequest;
}

export namespace GetObjectiveFormForUpdateRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateObjectiveReply): UpdateObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateObjectiveReply;
  static deserializeBinaryFromReader(message: UpdateObjectiveReply, reader: jspb.BinaryReader): UpdateObjectiveReply;
}

export namespace UpdateObjectiveReply {
  export type AsObject = {
  }
}

export class UpdateObjectiveRequest extends jspb.Message {
  hasObjectiveForm(): boolean;
  clearObjectiveForm(): void;
  getObjectiveForm(): ObjectiveForm | undefined;
  setObjectiveForm(value?: ObjectiveForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateObjectiveRequest): UpdateObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateObjectiveRequest;
  static deserializeBinaryFromReader(message: UpdateObjectiveRequest, reader: jspb.BinaryReader): UpdateObjectiveRequest;
}

export namespace UpdateObjectiveRequest {
  export type AsObject = {
    objectiveForm?: ObjectiveForm.AsObject,
  }
}

export class CanDeleteObjectivesReply extends jspb.Message {
  getCanDeleteObjectives(): boolean;
  setCanDeleteObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteObjectivesReply): CanDeleteObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteObjectivesReply;
  static deserializeBinaryFromReader(message: CanDeleteObjectivesReply, reader: jspb.BinaryReader): CanDeleteObjectivesReply;
}

export namespace CanDeleteObjectivesReply {
  export type AsObject = {
    canDeleteObjectives: boolean,
  }
}

export class CanDeleteObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteObjectivesRequest): CanDeleteObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteObjectivesRequest;
  static deserializeBinaryFromReader(message: CanDeleteObjectivesRequest, reader: jspb.BinaryReader): CanDeleteObjectivesRequest;
}

export namespace CanDeleteObjectivesRequest {
  export type AsObject = {
  }
}

export class DeleteObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteObjectiveReply): DeleteObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteObjectiveReply;
  static deserializeBinaryFromReader(message: DeleteObjectiveReply, reader: jspb.BinaryReader): DeleteObjectiveReply;
}

export namespace DeleteObjectiveReply {
  export type AsObject = {
  }
}

export class DeleteObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteObjectiveRequest): DeleteObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteObjectiveRequest;
  static deserializeBinaryFromReader(message: DeleteObjectiveRequest, reader: jspb.BinaryReader): DeleteObjectiveRequest;
}

export namespace DeleteObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageObjectiveAliasesReply extends jspb.Message {
  getCanManageObjectiveAliases(): boolean;
  setCanManageObjectiveAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageObjectiveAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageObjectiveAliasesReply): CanManageObjectiveAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageObjectiveAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageObjectiveAliasesReply;
  static deserializeBinaryFromReader(message: CanManageObjectiveAliasesReply, reader: jspb.BinaryReader): CanManageObjectiveAliasesReply;
}

export namespace CanManageObjectiveAliasesReply {
  export type AsObject = {
    canManageObjectiveAliases: boolean,
  }
}

export class CanManageObjectiveAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageObjectiveAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageObjectiveAliasesRequest): CanManageObjectiveAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageObjectiveAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageObjectiveAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageObjectiveAliasesRequest, reader: jspb.BinaryReader): CanManageObjectiveAliasesRequest;
}

export namespace CanManageObjectiveAliasesRequest {
  export type AsObject = {
  }
}

export class AliasObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasObjectiveReply): AliasObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasObjectiveReply;
  static deserializeBinaryFromReader(message: AliasObjectiveReply, reader: jspb.BinaryReader): AliasObjectiveReply;
}

export namespace AliasObjectiveReply {
  export type AsObject = {
  }
}

export class AliasObjectiveRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasObjectiveRequest): AliasObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasObjectiveRequest;
  static deserializeBinaryFromReader(message: AliasObjectiveRequest, reader: jspb.BinaryReader): AliasObjectiveRequest;
}

export namespace AliasObjectiveRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveHierarchyIdReply): GetObjectiveHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetObjectiveHierarchyIdReply, reader: jspb.BinaryReader): GetObjectiveHierarchyIdReply;
}

export namespace GetObjectiveHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveHierarchyIdRequest): GetObjectiveHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetObjectiveHierarchyIdRequest, reader: jspb.BinaryReader): GetObjectiveHierarchyIdRequest;
}

export namespace GetObjectiveHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetObjectiveHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveHierarchyReply): GetObjectiveHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveHierarchyReply;
  static deserializeBinaryFromReader(message: GetObjectiveHierarchyReply, reader: jspb.BinaryReader): GetObjectiveHierarchyReply;
}

export namespace GetObjectiveHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetObjectiveHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveHierarchyRequest): GetObjectiveHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveHierarchyRequest;
  static deserializeBinaryFromReader(message: GetObjectiveHierarchyRequest, reader: jspb.BinaryReader): GetObjectiveHierarchyRequest;
}

export namespace GetObjectiveHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessObjectiveHierarchyReply extends jspb.Message {
  getCanAccessObjectiveHierarchy(): boolean;
  setCanAccessObjectiveHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessObjectiveHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessObjectiveHierarchyReply): CanAccessObjectiveHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessObjectiveHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessObjectiveHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessObjectiveHierarchyReply, reader: jspb.BinaryReader): CanAccessObjectiveHierarchyReply;
}

export namespace CanAccessObjectiveHierarchyReply {
  export type AsObject = {
    canAccessObjectiveHierarchy: boolean,
  }
}

export class CanAccessObjectiveHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessObjectiveHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessObjectiveHierarchyRequest): CanAccessObjectiveHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessObjectiveHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessObjectiveHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessObjectiveHierarchyRequest, reader: jspb.BinaryReader): CanAccessObjectiveHierarchyRequest;
}

export namespace CanAccessObjectiveHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootObjectiveIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootObjectiveIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootObjectiveIdsRequest): GetRootObjectiveIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootObjectiveIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootObjectiveIdsRequest;
  static deserializeBinaryFromReader(message: GetRootObjectiveIdsRequest, reader: jspb.BinaryReader): GetRootObjectiveIdsRequest;
}

export namespace GetRootObjectiveIdsRequest {
  export type AsObject = {
  }
}

export class GetRootObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootObjectivesRequest): GetRootObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootObjectivesRequest;
  static deserializeBinaryFromReader(message: GetRootObjectivesRequest, reader: jspb.BinaryReader): GetRootObjectivesRequest;
}

export namespace GetRootObjectivesRequest {
  export type AsObject = {
  }
}

export class HasParentObjectivesReply extends jspb.Message {
  getHasParentObjectives(): boolean;
  setHasParentObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentObjectivesReply): HasParentObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentObjectivesReply;
  static deserializeBinaryFromReader(message: HasParentObjectivesReply, reader: jspb.BinaryReader): HasParentObjectivesReply;
}

export namespace HasParentObjectivesReply {
  export type AsObject = {
    hasParentObjectives: boolean,
  }
}

export class HasParentObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentObjectivesRequest): HasParentObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentObjectivesRequest;
  static deserializeBinaryFromReader(message: HasParentObjectivesRequest, reader: jspb.BinaryReader): HasParentObjectivesRequest;
}

export namespace HasParentObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfObjectiveReply extends jspb.Message {
  getIsParentOfObjective(): boolean;
  setIsParentOfObjective(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfObjectiveReply): IsParentOfObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfObjectiveReply;
  static deserializeBinaryFromReader(message: IsParentOfObjectiveReply, reader: jspb.BinaryReader): IsParentOfObjectiveReply;
}

export namespace IsParentOfObjectiveReply {
  export type AsObject = {
    isParentOfObjective: boolean,
  }
}

export class IsParentOfObjectiveRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfObjectiveRequest): IsParentOfObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfObjectiveRequest;
  static deserializeBinaryFromReader(message: IsParentOfObjectiveRequest, reader: jspb.BinaryReader): IsParentOfObjectiveRequest;
}

export namespace IsParentOfObjectiveRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentObjectiveIdsRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentObjectiveIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentObjectiveIdsRequest): GetParentObjectiveIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentObjectiveIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentObjectiveIdsRequest;
  static deserializeBinaryFromReader(message: GetParentObjectiveIdsRequest, reader: jspb.BinaryReader): GetParentObjectiveIdsRequest;
}

export namespace GetParentObjectiveIdsRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentObjectivesRequest): GetParentObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentObjectivesRequest;
  static deserializeBinaryFromReader(message: GetParentObjectivesRequest, reader: jspb.BinaryReader): GetParentObjectivesRequest;
}

export namespace GetParentObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfObjectiveReply extends jspb.Message {
  getIsAncestorOfObjective(): boolean;
  setIsAncestorOfObjective(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfObjectiveReply): IsAncestorOfObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfObjectiveReply;
  static deserializeBinaryFromReader(message: IsAncestorOfObjectiveReply, reader: jspb.BinaryReader): IsAncestorOfObjectiveReply;
}

export namespace IsAncestorOfObjectiveReply {
  export type AsObject = {
    isAncestorOfObjective: boolean,
  }
}

export class IsAncestorOfObjectiveRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfObjectiveRequest): IsAncestorOfObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfObjectiveRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfObjectiveRequest, reader: jspb.BinaryReader): IsAncestorOfObjectiveRequest;
}

export namespace IsAncestorOfObjectiveRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildObjectivesReply extends jspb.Message {
  getHasChildObjectives(): boolean;
  setHasChildObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildObjectivesReply): HasChildObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildObjectivesReply;
  static deserializeBinaryFromReader(message: HasChildObjectivesReply, reader: jspb.BinaryReader): HasChildObjectivesReply;
}

export namespace HasChildObjectivesReply {
  export type AsObject = {
    hasChildObjectives: boolean,
  }
}

export class HasChildObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildObjectivesRequest): HasChildObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildObjectivesRequest;
  static deserializeBinaryFromReader(message: HasChildObjectivesRequest, reader: jspb.BinaryReader): HasChildObjectivesRequest;
}

export namespace HasChildObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfObjectiveReply extends jspb.Message {
  getIsChildOfObjective(): boolean;
  setIsChildOfObjective(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfObjectiveReply): IsChildOfObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfObjectiveReply;
  static deserializeBinaryFromReader(message: IsChildOfObjectiveReply, reader: jspb.BinaryReader): IsChildOfObjectiveReply;
}

export namespace IsChildOfObjectiveReply {
  export type AsObject = {
    isChildOfObjective: boolean,
  }
}

export class IsChildOfObjectiveRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfObjectiveRequest): IsChildOfObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfObjectiveRequest;
  static deserializeBinaryFromReader(message: IsChildOfObjectiveRequest, reader: jspb.BinaryReader): IsChildOfObjectiveRequest;
}

export namespace IsChildOfObjectiveRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildObjectiveIdsRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildObjectiveIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildObjectiveIdsRequest): GetChildObjectiveIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildObjectiveIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildObjectiveIdsRequest;
  static deserializeBinaryFromReader(message: GetChildObjectiveIdsRequest, reader: jspb.BinaryReader): GetChildObjectiveIdsRequest;
}

export namespace GetChildObjectiveIdsRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildObjectivesRequest): GetChildObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildObjectivesRequest;
  static deserializeBinaryFromReader(message: GetChildObjectivesRequest, reader: jspb.BinaryReader): GetChildObjectivesRequest;
}

export namespace GetChildObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfObjectiveReply extends jspb.Message {
  getIsDescendantOfObjective(): boolean;
  setIsDescendantOfObjective(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfObjectiveReply): IsDescendantOfObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfObjectiveReply;
  static deserializeBinaryFromReader(message: IsDescendantOfObjectiveReply, reader: jspb.BinaryReader): IsDescendantOfObjectiveReply;
}

export namespace IsDescendantOfObjectiveReply {
  export type AsObject = {
    isDescendantOfObjective: boolean,
  }
}

export class IsDescendantOfObjectiveRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfObjectiveRequest): IsDescendantOfObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfObjectiveRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfObjectiveRequest, reader: jspb.BinaryReader): IsDescendantOfObjectiveRequest;
}

export namespace IsDescendantOfObjectiveRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveNodeIdsReply): GetObjectiveNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveNodeIdsReply;
  static deserializeBinaryFromReader(message: GetObjectiveNodeIdsReply, reader: jspb.BinaryReader): GetObjectiveNodeIdsReply;
}

export namespace GetObjectiveNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetObjectiveNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveNodeIdsRequest): GetObjectiveNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetObjectiveNodeIdsRequest, reader: jspb.BinaryReader): GetObjectiveNodeIdsRequest;
}

export namespace GetObjectiveNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveNodesReply extends jspb.Message {
  hasObjectiveNode(): boolean;
  clearObjectiveNode(): void;
  getObjectiveNode(): ObjectiveNode | undefined;
  setObjectiveNode(value?: ObjectiveNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveNodesReply): GetObjectiveNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveNodesReply;
  static deserializeBinaryFromReader(message: GetObjectiveNodesReply, reader: jspb.BinaryReader): GetObjectiveNodesReply;
}

export namespace GetObjectiveNodesReply {
  export type AsObject = {
    objectiveNode?: ObjectiveNode.AsObject,
  }
}

export class GetObjectiveNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveNodesRequest): GetObjectiveNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveNodesRequest;
  static deserializeBinaryFromReader(message: GetObjectiveNodesRequest, reader: jspb.BinaryReader): GetObjectiveNodesRequest;
}

export namespace GetObjectiveNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanModifyObjectiveHierarchyReply extends jspb.Message {
  getCanModifyObjectiveHierarchy(): boolean;
  setCanModifyObjectiveHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyObjectiveHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyObjectiveHierarchyReply): CanModifyObjectiveHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyObjectiveHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyObjectiveHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyObjectiveHierarchyReply, reader: jspb.BinaryReader): CanModifyObjectiveHierarchyReply;
}

export namespace CanModifyObjectiveHierarchyReply {
  export type AsObject = {
    canModifyObjectiveHierarchy: boolean,
  }
}

export class CanModifyObjectiveHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyObjectiveHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyObjectiveHierarchyRequest): CanModifyObjectiveHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyObjectiveHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyObjectiveHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyObjectiveHierarchyRequest, reader: jspb.BinaryReader): CanModifyObjectiveHierarchyRequest;
}

export namespace CanModifyObjectiveHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootObjectiveReply): AddRootObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootObjectiveReply;
  static deserializeBinaryFromReader(message: AddRootObjectiveReply, reader: jspb.BinaryReader): AddRootObjectiveReply;
}

export namespace AddRootObjectiveReply {
  export type AsObject = {
  }
}

export class AddRootObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootObjectiveRequest): AddRootObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootObjectiveRequest;
  static deserializeBinaryFromReader(message: AddRootObjectiveRequest, reader: jspb.BinaryReader): AddRootObjectiveRequest;
}

export namespace AddRootObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootObjectiveReply): RemoveRootObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootObjectiveReply;
  static deserializeBinaryFromReader(message: RemoveRootObjectiveReply, reader: jspb.BinaryReader): RemoveRootObjectiveReply;
}

export namespace RemoveRootObjectiveReply {
  export type AsObject = {
  }
}

export class RemoveRootObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootObjectiveRequest): RemoveRootObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootObjectiveRequest;
  static deserializeBinaryFromReader(message: RemoveRootObjectiveRequest, reader: jspb.BinaryReader): RemoveRootObjectiveRequest;
}

export namespace RemoveRootObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildObjectiveReply): AddChildObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildObjectiveReply;
  static deserializeBinaryFromReader(message: AddChildObjectiveReply, reader: jspb.BinaryReader): AddChildObjectiveReply;
}

export namespace AddChildObjectiveReply {
  export type AsObject = {
  }
}

export class AddChildObjectiveRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildObjectiveRequest): AddChildObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildObjectiveRequest;
  static deserializeBinaryFromReader(message: AddChildObjectiveRequest, reader: jspb.BinaryReader): AddChildObjectiveRequest;
}

export namespace AddChildObjectiveRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectiveReply): RemoveChildObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectiveReply;
  static deserializeBinaryFromReader(message: RemoveChildObjectiveReply, reader: jspb.BinaryReader): RemoveChildObjectiveReply;
}

export namespace RemoveChildObjectiveReply {
  export type AsObject = {
  }
}

export class RemoveChildObjectiveRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectiveRequest): RemoveChildObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectiveRequest;
  static deserializeBinaryFromReader(message: RemoveChildObjectiveRequest, reader: jspb.BinaryReader): RemoveChildObjectiveRequest;
}

export namespace RemoveChildObjectiveRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildObjectivesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectivesReply): RemoveChildObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectivesReply;
  static deserializeBinaryFromReader(message: RemoveChildObjectivesReply, reader: jspb.BinaryReader): RemoveChildObjectivesReply;
}

export namespace RemoveChildObjectivesReply {
  export type AsObject = {
  }
}

export class RemoveChildObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectivesRequest): RemoveChildObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectivesRequest;
  static deserializeBinaryFromReader(message: RemoveChildObjectivesRequest, reader: jspb.BinaryReader): RemoveChildObjectivesRequest;
}

export namespace RemoveChildObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanSequenceObjectivesReply extends jspb.Message {
  getCanSequenceObjectives(): boolean;
  setCanSequenceObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSequenceObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSequenceObjectivesReply): CanSequenceObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSequenceObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSequenceObjectivesReply;
  static deserializeBinaryFromReader(message: CanSequenceObjectivesReply, reader: jspb.BinaryReader): CanSequenceObjectivesReply;
}

export namespace CanSequenceObjectivesReply {
  export type AsObject = {
    canSequenceObjectives: boolean,
  }
}

export class CanSequenceObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSequenceObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSequenceObjectivesRequest): CanSequenceObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSequenceObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSequenceObjectivesRequest;
  static deserializeBinaryFromReader(message: CanSequenceObjectivesRequest, reader: jspb.BinaryReader): CanSequenceObjectivesRequest;
}

export namespace CanSequenceObjectivesRequest {
  export type AsObject = {
  }
}

export class MoveObjectiveAheadReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveObjectiveAheadReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveObjectiveAheadReply): MoveObjectiveAheadReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveObjectiveAheadReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveObjectiveAheadReply;
  static deserializeBinaryFromReader(message: MoveObjectiveAheadReply, reader: jspb.BinaryReader): MoveObjectiveAheadReply;
}

export namespace MoveObjectiveAheadReply {
  export type AsObject = {
  }
}

export class MoveObjectiveAheadRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasParentObjectiveId(): boolean;
  clearParentObjectiveId(): void;
  getParentObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setParentObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceObjectiveId(): boolean;
  clearReferenceObjectiveId(): void;
  getReferenceObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveObjectiveAheadRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveObjectiveAheadRequest): MoveObjectiveAheadRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveObjectiveAheadRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveObjectiveAheadRequest;
  static deserializeBinaryFromReader(message: MoveObjectiveAheadRequest, reader: jspb.BinaryReader): MoveObjectiveAheadRequest;
}

export namespace MoveObjectiveAheadRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    parentObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveObjectiveBehindReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveObjectiveBehindReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveObjectiveBehindReply): MoveObjectiveBehindReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveObjectiveBehindReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveObjectiveBehindReply;
  static deserializeBinaryFromReader(message: MoveObjectiveBehindReply, reader: jspb.BinaryReader): MoveObjectiveBehindReply;
}

export namespace MoveObjectiveBehindReply {
  export type AsObject = {
  }
}

export class MoveObjectiveBehindRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasParentObjectiveId(): boolean;
  clearParentObjectiveId(): void;
  getParentObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setParentObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReferenceObjectiveId(): boolean;
  clearReferenceObjectiveId(): void;
  getReferenceObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveObjectiveBehindRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveObjectiveBehindRequest): MoveObjectiveBehindRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveObjectiveBehindRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveObjectiveBehindRequest;
  static deserializeBinaryFromReader(message: MoveObjectiveBehindRequest, reader: jspb.BinaryReader): MoveObjectiveBehindRequest;
}

export namespace MoveObjectiveBehindRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    parentObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    referenceObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class SequenceObjectivesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceObjectivesReply): SequenceObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceObjectivesReply;
  static deserializeBinaryFromReader(message: SequenceObjectivesReply, reader: jspb.BinaryReader): SequenceObjectivesReply;
}

export namespace SequenceObjectivesReply {
  export type AsObject = {
  }
}

export class SequenceObjectivesRequest extends jspb.Message {
  clearObjectiveIdsList(): void;
  getObjectiveIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  hasParentObjectiveId(): boolean;
  clearParentObjectiveId(): void;
  getParentObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setParentObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SequenceObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SequenceObjectivesRequest): SequenceObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SequenceObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SequenceObjectivesRequest;
  static deserializeBinaryFromReader(message: SequenceObjectivesRequest, reader: jspb.BinaryReader): SequenceObjectivesRequest;
}

export namespace SequenceObjectivesRequest {
  export type AsObject = {
    objectiveIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    parentObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupObjectiveObjectiveBankMappingsReply extends jspb.Message {
  getCanLookupObjectiveObjectiveBankMappings(): boolean;
  setCanLookupObjectiveObjectiveBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectiveObjectiveBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectiveObjectiveBankMappingsReply): CanLookupObjectiveObjectiveBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectiveObjectiveBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectiveObjectiveBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupObjectiveObjectiveBankMappingsReply, reader: jspb.BinaryReader): CanLookupObjectiveObjectiveBankMappingsReply;
}

export namespace CanLookupObjectiveObjectiveBankMappingsReply {
  export type AsObject = {
    canLookupObjectiveObjectiveBankMappings: boolean,
  }
}

export class CanLookupObjectiveObjectiveBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectiveObjectiveBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectiveObjectiveBankMappingsRequest): CanLookupObjectiveObjectiveBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectiveObjectiveBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectiveObjectiveBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupObjectiveObjectiveBankMappingsRequest, reader: jspb.BinaryReader): CanLookupObjectiveObjectiveBankMappingsRequest;
}

export namespace CanLookupObjectiveObjectiveBankMappingsRequest {
  export type AsObject = {
  }
}

export class UseComparativeObjectiveBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeObjectiveBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeObjectiveBankViewReply): UseComparativeObjectiveBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeObjectiveBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeObjectiveBankViewReply;
  static deserializeBinaryFromReader(message: UseComparativeObjectiveBankViewReply, reader: jspb.BinaryReader): UseComparativeObjectiveBankViewReply;
}

export namespace UseComparativeObjectiveBankViewReply {
  export type AsObject = {
  }
}

export class UseComparativeObjectiveBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeObjectiveBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeObjectiveBankViewRequest): UseComparativeObjectiveBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeObjectiveBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeObjectiveBankViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeObjectiveBankViewRequest, reader: jspb.BinaryReader): UseComparativeObjectiveBankViewRequest;
}

export namespace UseComparativeObjectiveBankViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryObjectiveBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryObjectiveBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryObjectiveBankViewReply): UsePlenaryObjectiveBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryObjectiveBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryObjectiveBankViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryObjectiveBankViewReply, reader: jspb.BinaryReader): UsePlenaryObjectiveBankViewReply;
}

export namespace UsePlenaryObjectiveBankViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryObjectiveBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryObjectiveBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryObjectiveBankViewRequest): UsePlenaryObjectiveBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryObjectiveBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryObjectiveBankViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryObjectiveBankViewRequest, reader: jspb.BinaryReader): UsePlenaryObjectiveBankViewRequest;
}

export namespace UsePlenaryObjectiveBankViewRequest {
  export type AsObject = {
  }
}

export class GetObjectiveIdsByObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveIdsByObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveIdsByObjectiveBankRequest): GetObjectiveIdsByObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveIdsByObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveIdsByObjectiveBankRequest;
  static deserializeBinaryFromReader(message: GetObjectiveIdsByObjectiveBankRequest, reader: jspb.BinaryReader): GetObjectiveIdsByObjectiveBankRequest;
}

export namespace GetObjectiveIdsByObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectivesByObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByObjectiveBankRequest): GetObjectivesByObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByObjectiveBankRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByObjectiveBankRequest, reader: jspb.BinaryReader): GetObjectivesByObjectiveBankRequest;
}

export namespace GetObjectivesByObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveIdsByObjectiveBanksRequest extends jspb.Message {
  clearObjectiveBankIdsList(): void;
  getObjectiveBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveIdsByObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveIdsByObjectiveBanksRequest): GetObjectiveIdsByObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveIdsByObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveIdsByObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetObjectiveIdsByObjectiveBanksRequest, reader: jspb.BinaryReader): GetObjectiveIdsByObjectiveBanksRequest;
}

export namespace GetObjectiveIdsByObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetObjectivesByObjectiveBanksRequest extends jspb.Message {
  clearObjectiveBankIdsList(): void;
  getObjectiveBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectivesByObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectivesByObjectiveBanksRequest): GetObjectivesByObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectivesByObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectivesByObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetObjectivesByObjectiveBanksRequest, reader: jspb.BinaryReader): GetObjectivesByObjectiveBanksRequest;
}

export namespace GetObjectivesByObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetObjectiveBankIdsByObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankIdsByObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankIdsByObjectiveRequest): GetObjectiveBankIdsByObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankIdsByObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankIdsByObjectiveRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankIdsByObjectiveRequest, reader: jspb.BinaryReader): GetObjectiveBankIdsByObjectiveRequest;
}

export namespace GetObjectiveBankIdsByObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBanksByObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByObjectiveRequest): GetObjectiveBanksByObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByObjectiveRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByObjectiveRequest, reader: jspb.BinaryReader): GetObjectiveBanksByObjectiveRequest;
}

export namespace GetObjectiveBanksByObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignObjectivesReply extends jspb.Message {
  getCanAssignObjectives(): boolean;
  setCanAssignObjectives(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignObjectivesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignObjectivesReply): CanAssignObjectivesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignObjectivesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignObjectivesReply;
  static deserializeBinaryFromReader(message: CanAssignObjectivesReply, reader: jspb.BinaryReader): CanAssignObjectivesReply;
}

export namespace CanAssignObjectivesReply {
  export type AsObject = {
    canAssignObjectives: boolean,
  }
}

export class CanAssignObjectivesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignObjectivesRequest): CanAssignObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignObjectivesRequest;
  static deserializeBinaryFromReader(message: CanAssignObjectivesRequest, reader: jspb.BinaryReader): CanAssignObjectivesRequest;
}

export namespace CanAssignObjectivesRequest {
  export type AsObject = {
  }
}

export class CanAssignObjectivesToObjectiveBankReply extends jspb.Message {
  getCanAssignObjectivesToObjectiveBank(): boolean;
  setCanAssignObjectivesToObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignObjectivesToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignObjectivesToObjectiveBankReply): CanAssignObjectivesToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignObjectivesToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignObjectivesToObjectiveBankReply;
  static deserializeBinaryFromReader(message: CanAssignObjectivesToObjectiveBankReply, reader: jspb.BinaryReader): CanAssignObjectivesToObjectiveBankReply;
}

export namespace CanAssignObjectivesToObjectiveBankReply {
  export type AsObject = {
    canAssignObjectivesToObjectiveBank: boolean,
  }
}

export class CanAssignObjectivesToObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignObjectivesToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignObjectivesToObjectiveBankRequest): CanAssignObjectivesToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignObjectivesToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignObjectivesToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: CanAssignObjectivesToObjectiveBankRequest, reader: jspb.BinaryReader): CanAssignObjectivesToObjectiveBankRequest;
}

export namespace CanAssignObjectivesToObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableObjectiveBankIdsRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableObjectiveBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableObjectiveBankIdsRequest): GetAssignableObjectiveBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableObjectiveBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableObjectiveBankIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableObjectiveBankIdsRequest, reader: jspb.BinaryReader): GetAssignableObjectiveBankIdsRequest;
}

export namespace GetAssignableObjectiveBankIdsRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableObjectiveBankIdsForObjectiveRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableObjectiveBankIdsForObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableObjectiveBankIdsForObjectiveRequest): GetAssignableObjectiveBankIdsForObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableObjectiveBankIdsForObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableObjectiveBankIdsForObjectiveRequest;
  static deserializeBinaryFromReader(message: GetAssignableObjectiveBankIdsForObjectiveRequest, reader: jspb.BinaryReader): GetAssignableObjectiveBankIdsForObjectiveRequest;
}

export namespace GetAssignableObjectiveBankIdsForObjectiveRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignObjectiveToObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignObjectiveToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignObjectiveToObjectiveBankReply): AssignObjectiveToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignObjectiveToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignObjectiveToObjectiveBankReply;
  static deserializeBinaryFromReader(message: AssignObjectiveToObjectiveBankReply, reader: jspb.BinaryReader): AssignObjectiveToObjectiveBankReply;
}

export namespace AssignObjectiveToObjectiveBankReply {
  export type AsObject = {
  }
}

export class AssignObjectiveToObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignObjectiveToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignObjectiveToObjectiveBankRequest): AssignObjectiveToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignObjectiveToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignObjectiveToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: AssignObjectiveToObjectiveBankRequest, reader: jspb.BinaryReader): AssignObjectiveToObjectiveBankRequest;
}

export namespace AssignObjectiveToObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignObjectiveFromObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignObjectiveFromObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignObjectiveFromObjectiveBankReply): UnassignObjectiveFromObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignObjectiveFromObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignObjectiveFromObjectiveBankReply;
  static deserializeBinaryFromReader(message: UnassignObjectiveFromObjectiveBankReply, reader: jspb.BinaryReader): UnassignObjectiveFromObjectiveBankReply;
}

export namespace UnassignObjectiveFromObjectiveBankReply {
  export type AsObject = {
  }
}

export class UnassignObjectiveFromObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignObjectiveFromObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignObjectiveFromObjectiveBankRequest): UnassignObjectiveFromObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignObjectiveFromObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignObjectiveFromObjectiveBankRequest;
  static deserializeBinaryFromReader(message: UnassignObjectiveFromObjectiveBankRequest, reader: jspb.BinaryReader): UnassignObjectiveFromObjectiveBankRequest;
}

export namespace UnassignObjectiveFromObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignProficiencyToObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignProficiencyToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignProficiencyToObjectiveBankReply): ReassignProficiencyToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignProficiencyToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignProficiencyToObjectiveBankReply;
  static deserializeBinaryFromReader(message: ReassignProficiencyToObjectiveBankReply, reader: jspb.BinaryReader): ReassignProficiencyToObjectiveBankReply;
}

export namespace ReassignProficiencyToObjectiveBankReply {
  export type AsObject = {
  }
}

export class ReassignProficiencyToObjectiveBankRequest extends jspb.Message {
  hasFromObjectiveBankId(): boolean;
  clearFromObjectiveBankId(): void;
  getFromObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToObjectiveBankId(): boolean;
  clearToObjectiveBankId(): void;
  getToObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignProficiencyToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignProficiencyToObjectiveBankRequest): ReassignProficiencyToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignProficiencyToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignProficiencyToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: ReassignProficiencyToObjectiveBankRequest, reader: jspb.BinaryReader): ReassignProficiencyToObjectiveBankRequest;
}

export namespace ReassignProficiencyToObjectiveBankRequest {
  export type AsObject = {
    fromObjectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toObjectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupObjectivePrerequisitesReply extends jspb.Message {
  getCanLookupObjectivePrerequisites(): boolean;
  setCanLookupObjectivePrerequisites(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectivePrerequisitesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectivePrerequisitesReply): CanLookupObjectivePrerequisitesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectivePrerequisitesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectivePrerequisitesReply;
  static deserializeBinaryFromReader(message: CanLookupObjectivePrerequisitesReply, reader: jspb.BinaryReader): CanLookupObjectivePrerequisitesReply;
}

export namespace CanLookupObjectivePrerequisitesReply {
  export type AsObject = {
    canLookupObjectivePrerequisites: boolean,
  }
}

export class CanLookupObjectivePrerequisitesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectivePrerequisitesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectivePrerequisitesRequest): CanLookupObjectivePrerequisitesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectivePrerequisitesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectivePrerequisitesRequest;
  static deserializeBinaryFromReader(message: CanLookupObjectivePrerequisitesRequest, reader: jspb.BinaryReader): CanLookupObjectivePrerequisitesRequest;
}

export namespace CanLookupObjectivePrerequisitesRequest {
  export type AsObject = {
  }
}

export class GetRequisiteObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRequisiteObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRequisiteObjectivesRequest): GetRequisiteObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRequisiteObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRequisiteObjectivesRequest;
  static deserializeBinaryFromReader(message: GetRequisiteObjectivesRequest, reader: jspb.BinaryReader): GetRequisiteObjectivesRequest;
}

export namespace GetRequisiteObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAllRequisiteObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAllRequisiteObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAllRequisiteObjectivesRequest): GetAllRequisiteObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAllRequisiteObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAllRequisiteObjectivesRequest;
  static deserializeBinaryFromReader(message: GetAllRequisiteObjectivesRequest, reader: jspb.BinaryReader): GetAllRequisiteObjectivesRequest;
}

export namespace GetAllRequisiteObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetDependentObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetDependentObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetDependentObjectivesRequest): GetDependentObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetDependentObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetDependentObjectivesRequest;
  static deserializeBinaryFromReader(message: GetDependentObjectivesRequest, reader: jspb.BinaryReader): GetDependentObjectivesRequest;
}

export namespace GetDependentObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsObjectiveRequiredReply extends jspb.Message {
  getIsObjectiveRequired(): boolean;
  setIsObjectiveRequired(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsObjectiveRequiredReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsObjectiveRequiredReply): IsObjectiveRequiredReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsObjectiveRequiredReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsObjectiveRequiredReply;
  static deserializeBinaryFromReader(message: IsObjectiveRequiredReply, reader: jspb.BinaryReader): IsObjectiveRequiredReply;
}

export namespace IsObjectiveRequiredReply {
  export type AsObject = {
    isObjectiveRequired: boolean,
  }
}

export class IsObjectiveRequiredRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRequiredObjectiveId(): boolean;
  clearRequiredObjectiveId(): void;
  getRequiredObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRequiredObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsObjectiveRequiredRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsObjectiveRequiredRequest): IsObjectiveRequiredRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsObjectiveRequiredRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsObjectiveRequiredRequest;
  static deserializeBinaryFromReader(message: IsObjectiveRequiredRequest, reader: jspb.BinaryReader): IsObjectiveRequiredRequest;
}

export namespace IsObjectiveRequiredRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    requiredObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetEquivalentObjectivesRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetEquivalentObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetEquivalentObjectivesRequest): GetEquivalentObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetEquivalentObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetEquivalentObjectivesRequest;
  static deserializeBinaryFromReader(message: GetEquivalentObjectivesRequest, reader: jspb.BinaryReader): GetEquivalentObjectivesRequest;
}

export namespace GetEquivalentObjectivesRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignRequisitesReply extends jspb.Message {
  getCanAssignRequisites(): boolean;
  setCanAssignRequisites(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignRequisitesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignRequisitesReply): CanAssignRequisitesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignRequisitesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignRequisitesReply;
  static deserializeBinaryFromReader(message: CanAssignRequisitesReply, reader: jspb.BinaryReader): CanAssignRequisitesReply;
}

export namespace CanAssignRequisitesReply {
  export type AsObject = {
    canAssignRequisites: boolean,
  }
}

export class CanAssignRequisitesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignRequisitesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignRequisitesRequest): CanAssignRequisitesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignRequisitesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignRequisitesRequest;
  static deserializeBinaryFromReader(message: CanAssignRequisitesRequest, reader: jspb.BinaryReader): CanAssignRequisitesRequest;
}

export namespace CanAssignRequisitesRequest {
  export type AsObject = {
  }
}

export class AssignObjectiveRequisiteReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignObjectiveRequisiteReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignObjectiveRequisiteReply): AssignObjectiveRequisiteReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignObjectiveRequisiteReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignObjectiveRequisiteReply;
  static deserializeBinaryFromReader(message: AssignObjectiveRequisiteReply, reader: jspb.BinaryReader): AssignObjectiveRequisiteReply;
}

export namespace AssignObjectiveRequisiteReply {
  export type AsObject = {
  }
}

export class AssignObjectiveRequisiteRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRequisiteObjectiveId(): boolean;
  clearRequisiteObjectiveId(): void;
  getRequisiteObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRequisiteObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignObjectiveRequisiteRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignObjectiveRequisiteRequest): AssignObjectiveRequisiteRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignObjectiveRequisiteRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignObjectiveRequisiteRequest;
  static deserializeBinaryFromReader(message: AssignObjectiveRequisiteRequest, reader: jspb.BinaryReader): AssignObjectiveRequisiteRequest;
}

export namespace AssignObjectiveRequisiteRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    requisiteObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignObjectiveRequisiteReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignObjectiveRequisiteReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignObjectiveRequisiteReply): UnassignObjectiveRequisiteReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignObjectiveRequisiteReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignObjectiveRequisiteReply;
  static deserializeBinaryFromReader(message: UnassignObjectiveRequisiteReply, reader: jspb.BinaryReader): UnassignObjectiveRequisiteReply;
}

export namespace UnassignObjectiveRequisiteReply {
  export type AsObject = {
  }
}

export class UnassignObjectiveRequisiteRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasRequisiteObjectiveId(): boolean;
  clearRequisiteObjectiveId(): void;
  getRequisiteObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRequisiteObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignObjectiveRequisiteRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignObjectiveRequisiteRequest): UnassignObjectiveRequisiteRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignObjectiveRequisiteRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignObjectiveRequisiteRequest;
  static deserializeBinaryFromReader(message: UnassignObjectiveRequisiteRequest, reader: jspb.BinaryReader): UnassignObjectiveRequisiteRequest;
}

export namespace UnassignObjectiveRequisiteRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    requisiteObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignEquivalentObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignEquivalentObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignEquivalentObjectiveReply): AssignEquivalentObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignEquivalentObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignEquivalentObjectiveReply;
  static deserializeBinaryFromReader(message: AssignEquivalentObjectiveReply, reader: jspb.BinaryReader): AssignEquivalentObjectiveReply;
}

export namespace AssignEquivalentObjectiveReply {
  export type AsObject = {
  }
}

export class AssignEquivalentObjectiveRequest extends jspb.Message {
  hasEquivalentObjectiveId(): boolean;
  clearEquivalentObjectiveId(): void;
  getEquivalentObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setEquivalentObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignEquivalentObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignEquivalentObjectiveRequest): AssignEquivalentObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignEquivalentObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignEquivalentObjectiveRequest;
  static deserializeBinaryFromReader(message: AssignEquivalentObjectiveRequest, reader: jspb.BinaryReader): AssignEquivalentObjectiveRequest;
}

export namespace AssignEquivalentObjectiveRequest {
  export type AsObject = {
    equivalentObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignEquivalentObjectiveReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignEquivalentObjectiveReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignEquivalentObjectiveReply): UnassignEquivalentObjectiveReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignEquivalentObjectiveReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignEquivalentObjectiveReply;
  static deserializeBinaryFromReader(message: UnassignEquivalentObjectiveReply, reader: jspb.BinaryReader): UnassignEquivalentObjectiveReply;
}

export namespace UnassignEquivalentObjectiveReply {
  export type AsObject = {
  }
}

export class UnassignEquivalentObjectiveRequest extends jspb.Message {
  hasEquivalentObjectiveId(): boolean;
  clearEquivalentObjectiveId(): void;
  getEquivalentObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setEquivalentObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignEquivalentObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignEquivalentObjectiveRequest): UnassignEquivalentObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignEquivalentObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignEquivalentObjectiveRequest;
  static deserializeBinaryFromReader(message: UnassignEquivalentObjectiveRequest, reader: jspb.BinaryReader): UnassignEquivalentObjectiveRequest;
}

export namespace UnassignEquivalentObjectiveRequest {
  export type AsObject = {
    equivalentObjectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupActivitiesReply extends jspb.Message {
  getCanLookupActivities(): boolean;
  setCanLookupActivities(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupActivitiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupActivitiesReply): CanLookupActivitiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupActivitiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupActivitiesReply;
  static deserializeBinaryFromReader(message: CanLookupActivitiesReply, reader: jspb.BinaryReader): CanLookupActivitiesReply;
}

export namespace CanLookupActivitiesReply {
  export type AsObject = {
    canLookupActivities: boolean,
  }
}

export class CanLookupActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupActivitiesRequest): CanLookupActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupActivitiesRequest;
  static deserializeBinaryFromReader(message: CanLookupActivitiesRequest, reader: jspb.BinaryReader): CanLookupActivitiesRequest;
}

export namespace CanLookupActivitiesRequest {
  export type AsObject = {
  }
}

export class UseComparativeActivityViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeActivityViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeActivityViewReply): UseComparativeActivityViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeActivityViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeActivityViewReply;
  static deserializeBinaryFromReader(message: UseComparativeActivityViewReply, reader: jspb.BinaryReader): UseComparativeActivityViewReply;
}

export namespace UseComparativeActivityViewReply {
  export type AsObject = {
  }
}

export class UseComparativeActivityViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeActivityViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeActivityViewRequest): UseComparativeActivityViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeActivityViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeActivityViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeActivityViewRequest, reader: jspb.BinaryReader): UseComparativeActivityViewRequest;
}

export namespace UseComparativeActivityViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryActivityViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryActivityViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryActivityViewReply): UsePlenaryActivityViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryActivityViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryActivityViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryActivityViewReply, reader: jspb.BinaryReader): UsePlenaryActivityViewReply;
}

export namespace UsePlenaryActivityViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryActivityViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryActivityViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryActivityViewRequest): UsePlenaryActivityViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryActivityViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryActivityViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryActivityViewRequest, reader: jspb.BinaryReader): UsePlenaryActivityViewRequest;
}

export namespace UsePlenaryActivityViewRequest {
  export type AsObject = {
  }
}

export class GetActivityReply extends jspb.Message {
  hasActivity(): boolean;
  clearActivity(): void;
  getActivity(): Activity | undefined;
  setActivity(value?: Activity): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityReply): GetActivityReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityReply;
  static deserializeBinaryFromReader(message: GetActivityReply, reader: jspb.BinaryReader): GetActivityReply;
}

export namespace GetActivityReply {
  export type AsObject = {
    activity?: Activity.AsObject,
  }
}

export class GetActivityRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityRequest): GetActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityRequest;
  static deserializeBinaryFromReader(message: GetActivityRequest, reader: jspb.BinaryReader): GetActivityRequest;
}

export namespace GetActivityRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetActivitiesByIdsRequest extends jspb.Message {
  clearActivityIdsList(): void;
  getActivityIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setActivityIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addActivityIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByIdsRequest): GetActivitiesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByIdsRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByIdsRequest, reader: jspb.BinaryReader): GetActivitiesByIdsRequest;
}

export namespace GetActivitiesByIdsRequest {
  export type AsObject = {
    activityIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetActivitiesByGenusTypeRequest extends jspb.Message {
  hasActivityGenusType(): boolean;
  clearActivityGenusType(): void;
  getActivityGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setActivityGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByGenusTypeRequest): GetActivitiesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByGenusTypeRequest, reader: jspb.BinaryReader): GetActivitiesByGenusTypeRequest;
}

export namespace GetActivitiesByGenusTypeRequest {
  export type AsObject = {
    activityGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetActivitiesByParentGenusTypeRequest extends jspb.Message {
  hasActivityGenusType(): boolean;
  clearActivityGenusType(): void;
  getActivityGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setActivityGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByParentGenusTypeRequest): GetActivitiesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetActivitiesByParentGenusTypeRequest;
}

export namespace GetActivitiesByParentGenusTypeRequest {
  export type AsObject = {
    activityGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetActivitiesByRecordTypeRequest extends jspb.Message {
  hasActivityRecordType(): boolean;
  clearActivityRecordType(): void;
  getActivityRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setActivityRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByRecordTypeRequest): GetActivitiesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByRecordTypeRequest, reader: jspb.BinaryReader): GetActivitiesByRecordTypeRequest;
}

export namespace GetActivitiesByRecordTypeRequest {
  export type AsObject = {
    activityRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetActivitiesForObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesForObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesForObjectiveRequest): GetActivitiesForObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesForObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesForObjectiveRequest;
  static deserializeBinaryFromReader(message: GetActivitiesForObjectiveRequest, reader: jspb.BinaryReader): GetActivitiesForObjectiveRequest;
}

export namespace GetActivitiesForObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetActivitiesForObjectivesRequest extends jspb.Message {
  clearObjectiveIdsList(): void;
  getObjectiveIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesForObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesForObjectivesRequest): GetActivitiesForObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesForObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesForObjectivesRequest;
  static deserializeBinaryFromReader(message: GetActivitiesForObjectivesRequest, reader: jspb.BinaryReader): GetActivitiesForObjectivesRequest;
}

export namespace GetActivitiesForObjectivesRequest {
  export type AsObject = {
    objectiveIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetActivitiesByAssetRequest extends jspb.Message {
  hasAssetId(): boolean;
  clearAssetId(): void;
  getAssetId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssetId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByAssetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByAssetRequest): GetActivitiesByAssetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByAssetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByAssetRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByAssetRequest, reader: jspb.BinaryReader): GetActivitiesByAssetRequest;
}

export namespace GetActivitiesByAssetRequest {
  export type AsObject = {
    assetId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetActivitiesByAssetsRequest extends jspb.Message {
  clearAssetIdsList(): void;
  getAssetIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssetIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssetIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByAssetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByAssetsRequest): GetActivitiesByAssetsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByAssetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByAssetsRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByAssetsRequest, reader: jspb.BinaryReader): GetActivitiesByAssetsRequest;
}

export namespace GetActivitiesByAssetsRequest {
  export type AsObject = {
    assetIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesRequest): GetActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesRequest;
  static deserializeBinaryFromReader(message: GetActivitiesRequest, reader: jspb.BinaryReader): GetActivitiesRequest;
}

export namespace GetActivitiesRequest {
  export type AsObject = {
  }
}

export class CanSearchActivitiesReply extends jspb.Message {
  getCanSearchActivities(): boolean;
  setCanSearchActivities(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchActivitiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchActivitiesReply): CanSearchActivitiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchActivitiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchActivitiesReply;
  static deserializeBinaryFromReader(message: CanSearchActivitiesReply, reader: jspb.BinaryReader): CanSearchActivitiesReply;
}

export namespace CanSearchActivitiesReply {
  export type AsObject = {
    canSearchActivities: boolean,
  }
}

export class CanSearchActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchActivitiesRequest): CanSearchActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchActivitiesRequest;
  static deserializeBinaryFromReader(message: CanSearchActivitiesRequest, reader: jspb.BinaryReader): CanSearchActivitiesRequest;
}

export namespace CanSearchActivitiesRequest {
  export type AsObject = {
  }
}

export class GetActivityQueryReply extends jspb.Message {
  hasActivityQuery(): boolean;
  clearActivityQuery(): void;
  getActivityQuery(): ActivityQuery | undefined;
  setActivityQuery(value?: ActivityQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityQueryReply): GetActivityQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityQueryReply;
  static deserializeBinaryFromReader(message: GetActivityQueryReply, reader: jspb.BinaryReader): GetActivityQueryReply;
}

export namespace GetActivityQueryReply {
  export type AsObject = {
    activityQuery?: ActivityQuery.AsObject,
  }
}

export class GetActivityQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityQueryRequest): GetActivityQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityQueryRequest;
  static deserializeBinaryFromReader(message: GetActivityQueryRequest, reader: jspb.BinaryReader): GetActivityQueryRequest;
}

export namespace GetActivityQueryRequest {
  export type AsObject = {
  }
}

export class GetActivitiesByQueryRequest extends jspb.Message {
  hasActivityQuery(): boolean;
  clearActivityQuery(): void;
  getActivityQuery(): ActivityQuery | undefined;
  setActivityQuery(value?: ActivityQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByQueryRequest): GetActivitiesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByQueryRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByQueryRequest, reader: jspb.BinaryReader): GetActivitiesByQueryRequest;
}

export namespace GetActivitiesByQueryRequest {
  export type AsObject = {
    activityQuery?: ActivityQuery.AsObject,
  }
}

export class CanCreateActivitiesReply extends jspb.Message {
  getCanCreateActivities(): boolean;
  setCanCreateActivities(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateActivitiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateActivitiesReply): CanCreateActivitiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateActivitiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateActivitiesReply;
  static deserializeBinaryFromReader(message: CanCreateActivitiesReply, reader: jspb.BinaryReader): CanCreateActivitiesReply;
}

export namespace CanCreateActivitiesReply {
  export type AsObject = {
    canCreateActivities: boolean,
  }
}

export class CanCreateActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateActivitiesRequest): CanCreateActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateActivitiesRequest;
  static deserializeBinaryFromReader(message: CanCreateActivitiesRequest, reader: jspb.BinaryReader): CanCreateActivitiesRequest;
}

export namespace CanCreateActivitiesRequest {
  export type AsObject = {
  }
}

export class CanCreateActivityWithRecordTypesReply extends jspb.Message {
  getCanCreateActivityWithRecordTypes(): boolean;
  setCanCreateActivityWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateActivityWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateActivityWithRecordTypesReply): CanCreateActivityWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateActivityWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateActivityWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateActivityWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateActivityWithRecordTypesReply;
}

export namespace CanCreateActivityWithRecordTypesReply {
  export type AsObject = {
    canCreateActivityWithRecordTypes: boolean,
  }
}

export class CanCreateActivityWithRecordTypesRequest extends jspb.Message {
  clearActivityRecordTypesList(): void;
  getActivityRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setActivityRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addActivityRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateActivityWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateActivityWithRecordTypesRequest): CanCreateActivityWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateActivityWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateActivityWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateActivityWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateActivityWithRecordTypesRequest;
}

export namespace CanCreateActivityWithRecordTypesRequest {
  export type AsObject = {
    activityRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetActivityFormForCreateReply extends jspb.Message {
  hasActivityForm(): boolean;
  clearActivityForm(): void;
  getActivityForm(): ActivityForm | undefined;
  setActivityForm(value?: ActivityForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityFormForCreateReply): GetActivityFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityFormForCreateReply;
  static deserializeBinaryFromReader(message: GetActivityFormForCreateReply, reader: jspb.BinaryReader): GetActivityFormForCreateReply;
}

export namespace GetActivityFormForCreateReply {
  export type AsObject = {
    activityForm?: ActivityForm.AsObject,
  }
}

export class GetActivityFormForCreateRequest extends jspb.Message {
  clearActivityRecordTypesList(): void;
  getActivityRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setActivityRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addActivityRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityFormForCreateRequest): GetActivityFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetActivityFormForCreateRequest, reader: jspb.BinaryReader): GetActivityFormForCreateRequest;
}

export namespace GetActivityFormForCreateRequest {
  export type AsObject = {
    activityRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateActivityReply extends jspb.Message {
  hasActivity(): boolean;
  clearActivity(): void;
  getActivity(): Activity | undefined;
  setActivity(value?: Activity): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateActivityReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateActivityReply): CreateActivityReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateActivityReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateActivityReply;
  static deserializeBinaryFromReader(message: CreateActivityReply, reader: jspb.BinaryReader): CreateActivityReply;
}

export namespace CreateActivityReply {
  export type AsObject = {
    activity?: Activity.AsObject,
  }
}

export class CreateActivityRequest extends jspb.Message {
  hasActivityForm(): boolean;
  clearActivityForm(): void;
  getActivityForm(): ActivityForm | undefined;
  setActivityForm(value?: ActivityForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateActivityRequest): CreateActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateActivityRequest;
  static deserializeBinaryFromReader(message: CreateActivityRequest, reader: jspb.BinaryReader): CreateActivityRequest;
}

export namespace CreateActivityRequest {
  export type AsObject = {
    activityForm?: ActivityForm.AsObject,
  }
}

export class CanUpdateActivitiesReply extends jspb.Message {
  getCanUpdateActivities(): boolean;
  setCanUpdateActivities(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateActivitiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateActivitiesReply): CanUpdateActivitiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateActivitiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateActivitiesReply;
  static deserializeBinaryFromReader(message: CanUpdateActivitiesReply, reader: jspb.BinaryReader): CanUpdateActivitiesReply;
}

export namespace CanUpdateActivitiesReply {
  export type AsObject = {
    canUpdateActivities: boolean,
  }
}

export class CanUpdateActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateActivitiesRequest): CanUpdateActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateActivitiesRequest;
  static deserializeBinaryFromReader(message: CanUpdateActivitiesRequest, reader: jspb.BinaryReader): CanUpdateActivitiesRequest;
}

export namespace CanUpdateActivitiesRequest {
  export type AsObject = {
  }
}

export class GetActivityFormForUpdateReply extends jspb.Message {
  hasActivityForm(): boolean;
  clearActivityForm(): void;
  getActivityForm(): ActivityForm | undefined;
  setActivityForm(value?: ActivityForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityFormForUpdateReply): GetActivityFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetActivityFormForUpdateReply, reader: jspb.BinaryReader): GetActivityFormForUpdateReply;
}

export namespace GetActivityFormForUpdateReply {
  export type AsObject = {
    activityForm?: ActivityForm.AsObject,
  }
}

export class GetActivityFormForUpdateRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityFormForUpdateRequest): GetActivityFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetActivityFormForUpdateRequest, reader: jspb.BinaryReader): GetActivityFormForUpdateRequest;
}

export namespace GetActivityFormForUpdateRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateActivityReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateActivityReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateActivityReply): UpdateActivityReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateActivityReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateActivityReply;
  static deserializeBinaryFromReader(message: UpdateActivityReply, reader: jspb.BinaryReader): UpdateActivityReply;
}

export namespace UpdateActivityReply {
  export type AsObject = {
  }
}

export class UpdateActivityRequest extends jspb.Message {
  hasActivityForm(): boolean;
  clearActivityForm(): void;
  getActivityForm(): ActivityForm | undefined;
  setActivityForm(value?: ActivityForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateActivityRequest): UpdateActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateActivityRequest;
  static deserializeBinaryFromReader(message: UpdateActivityRequest, reader: jspb.BinaryReader): UpdateActivityRequest;
}

export namespace UpdateActivityRequest {
  export type AsObject = {
    activityForm?: ActivityForm.AsObject,
  }
}

export class CanDeleteActivitiesReply extends jspb.Message {
  getCanDeleteActivities(): boolean;
  setCanDeleteActivities(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteActivitiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteActivitiesReply): CanDeleteActivitiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteActivitiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteActivitiesReply;
  static deserializeBinaryFromReader(message: CanDeleteActivitiesReply, reader: jspb.BinaryReader): CanDeleteActivitiesReply;
}

export namespace CanDeleteActivitiesReply {
  export type AsObject = {
    canDeleteActivities: boolean,
  }
}

export class CanDeleteActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteActivitiesRequest): CanDeleteActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteActivitiesRequest;
  static deserializeBinaryFromReader(message: CanDeleteActivitiesRequest, reader: jspb.BinaryReader): CanDeleteActivitiesRequest;
}

export namespace CanDeleteActivitiesRequest {
  export type AsObject = {
  }
}

export class DeleteActivityReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteActivityReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteActivityReply): DeleteActivityReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteActivityReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteActivityReply;
  static deserializeBinaryFromReader(message: DeleteActivityReply, reader: jspb.BinaryReader): DeleteActivityReply;
}

export namespace DeleteActivityReply {
  export type AsObject = {
  }
}

export class DeleteActivityRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteActivityRequest): DeleteActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteActivityRequest;
  static deserializeBinaryFromReader(message: DeleteActivityRequest, reader: jspb.BinaryReader): DeleteActivityRequest;
}

export namespace DeleteActivityRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageActivityAliasesReply extends jspb.Message {
  getCanManageActivityAliases(): boolean;
  setCanManageActivityAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageActivityAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageActivityAliasesReply): CanManageActivityAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageActivityAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageActivityAliasesReply;
  static deserializeBinaryFromReader(message: CanManageActivityAliasesReply, reader: jspb.BinaryReader): CanManageActivityAliasesReply;
}

export namespace CanManageActivityAliasesReply {
  export type AsObject = {
    canManageActivityAliases: boolean,
  }
}

export class CanManageActivityAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageActivityAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageActivityAliasesRequest): CanManageActivityAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageActivityAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageActivityAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageActivityAliasesRequest, reader: jspb.BinaryReader): CanManageActivityAliasesRequest;
}

export namespace CanManageActivityAliasesRequest {
  export type AsObject = {
  }
}

export class AliasActivityReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasActivityReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasActivityReply): AliasActivityReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasActivityReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasActivityReply;
  static deserializeBinaryFromReader(message: AliasActivityReply, reader: jspb.BinaryReader): AliasActivityReply;
}

export namespace AliasActivityReply {
  export type AsObject = {
  }
}

export class AliasActivityRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasActivityRequest): AliasActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasActivityRequest;
  static deserializeBinaryFromReader(message: AliasActivityRequest, reader: jspb.BinaryReader): AliasActivityRequest;
}

export namespace AliasActivityRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupActivityObjectiveBankMappingsReply extends jspb.Message {
  getCanLookupActivityObjectiveBankMappings(): boolean;
  setCanLookupActivityObjectiveBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupActivityObjectiveBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupActivityObjectiveBankMappingsReply): CanLookupActivityObjectiveBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupActivityObjectiveBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupActivityObjectiveBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupActivityObjectiveBankMappingsReply, reader: jspb.BinaryReader): CanLookupActivityObjectiveBankMappingsReply;
}

export namespace CanLookupActivityObjectiveBankMappingsReply {
  export type AsObject = {
    canLookupActivityObjectiveBankMappings: boolean,
  }
}

export class CanLookupActivityObjectiveBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupActivityObjectiveBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupActivityObjectiveBankMappingsRequest): CanLookupActivityObjectiveBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupActivityObjectiveBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupActivityObjectiveBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupActivityObjectiveBankMappingsRequest, reader: jspb.BinaryReader): CanLookupActivityObjectiveBankMappingsRequest;
}

export namespace CanLookupActivityObjectiveBankMappingsRequest {
  export type AsObject = {
  }
}

export class GetActivityIdsByObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityIdsByObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityIdsByObjectiveBankRequest): GetActivityIdsByObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityIdsByObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityIdsByObjectiveBankRequest;
  static deserializeBinaryFromReader(message: GetActivityIdsByObjectiveBankRequest, reader: jspb.BinaryReader): GetActivityIdsByObjectiveBankRequest;
}

export namespace GetActivityIdsByObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetActivitiesByObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByObjectiveBankRequest): GetActivitiesByObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByObjectiveBankRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByObjectiveBankRequest, reader: jspb.BinaryReader): GetActivitiesByObjectiveBankRequest;
}

export namespace GetActivitiesByObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetActivityIdsByObjectiveBanksRequest extends jspb.Message {
  clearObjectiveBankIdsList(): void;
  getObjectiveBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivityIdsByObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivityIdsByObjectiveBanksRequest): GetActivityIdsByObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivityIdsByObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivityIdsByObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetActivityIdsByObjectiveBanksRequest, reader: jspb.BinaryReader): GetActivityIdsByObjectiveBanksRequest;
}

export namespace GetActivityIdsByObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetActivitiesByObjectiveBanksRequest extends jspb.Message {
  clearObjectiveBankIdsList(): void;
  getObjectiveBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetActivitiesByObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetActivitiesByObjectiveBanksRequest): GetActivitiesByObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetActivitiesByObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetActivitiesByObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetActivitiesByObjectiveBanksRequest, reader: jspb.BinaryReader): GetActivitiesByObjectiveBanksRequest;
}

export namespace GetActivitiesByObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetObjectiveBankIdsByActivityRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankIdsByActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankIdsByActivityRequest): GetObjectiveBankIdsByActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankIdsByActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankIdsByActivityRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankIdsByActivityRequest, reader: jspb.BinaryReader): GetObjectiveBankIdsByActivityRequest;
}

export namespace GetObjectiveBankIdsByActivityRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBanksByActivityRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByActivityRequest): GetObjectiveBanksByActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByActivityRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByActivityRequest, reader: jspb.BinaryReader): GetObjectiveBanksByActivityRequest;
}

export namespace GetObjectiveBanksByActivityRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignActivitiesReply extends jspb.Message {
  getCanAssignActivities(): boolean;
  setCanAssignActivities(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignActivitiesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignActivitiesReply): CanAssignActivitiesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignActivitiesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignActivitiesReply;
  static deserializeBinaryFromReader(message: CanAssignActivitiesReply, reader: jspb.BinaryReader): CanAssignActivitiesReply;
}

export namespace CanAssignActivitiesReply {
  export type AsObject = {
    canAssignActivities: boolean,
  }
}

export class CanAssignActivitiesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignActivitiesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignActivitiesRequest): CanAssignActivitiesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignActivitiesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignActivitiesRequest;
  static deserializeBinaryFromReader(message: CanAssignActivitiesRequest, reader: jspb.BinaryReader): CanAssignActivitiesRequest;
}

export namespace CanAssignActivitiesRequest {
  export type AsObject = {
  }
}

export class CanAssignActivitiesToObjectiveBankReply extends jspb.Message {
  getCanAssignActivitiesToObjectiveBank(): boolean;
  setCanAssignActivitiesToObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignActivitiesToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignActivitiesToObjectiveBankReply): CanAssignActivitiesToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignActivitiesToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignActivitiesToObjectiveBankReply;
  static deserializeBinaryFromReader(message: CanAssignActivitiesToObjectiveBankReply, reader: jspb.BinaryReader): CanAssignActivitiesToObjectiveBankReply;
}

export namespace CanAssignActivitiesToObjectiveBankReply {
  export type AsObject = {
    canAssignActivitiesToObjectiveBank: boolean,
  }
}

export class CanAssignActivitiesToObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignActivitiesToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignActivitiesToObjectiveBankRequest): CanAssignActivitiesToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignActivitiesToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignActivitiesToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: CanAssignActivitiesToObjectiveBankRequest, reader: jspb.BinaryReader): CanAssignActivitiesToObjectiveBankRequest;
}

export namespace CanAssignActivitiesToObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableObjectiveBankIdsForActivityRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableObjectiveBankIdsForActivityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableObjectiveBankIdsForActivityRequest): GetAssignableObjectiveBankIdsForActivityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableObjectiveBankIdsForActivityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableObjectiveBankIdsForActivityRequest;
  static deserializeBinaryFromReader(message: GetAssignableObjectiveBankIdsForActivityRequest, reader: jspb.BinaryReader): GetAssignableObjectiveBankIdsForActivityRequest;
}

export namespace GetAssignableObjectiveBankIdsForActivityRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignActivityToObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignActivityToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignActivityToObjectiveBankReply): AssignActivityToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignActivityToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignActivityToObjectiveBankReply;
  static deserializeBinaryFromReader(message: AssignActivityToObjectiveBankReply, reader: jspb.BinaryReader): AssignActivityToObjectiveBankReply;
}

export namespace AssignActivityToObjectiveBankReply {
  export type AsObject = {
  }
}

export class AssignActivityToObjectiveBankRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignActivityToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignActivityToObjectiveBankRequest): AssignActivityToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignActivityToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignActivityToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: AssignActivityToObjectiveBankRequest, reader: jspb.BinaryReader): AssignActivityToObjectiveBankRequest;
}

export namespace AssignActivityToObjectiveBankRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignActivityFromObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignActivityFromObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignActivityFromObjectiveBankReply): UnassignActivityFromObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignActivityFromObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignActivityFromObjectiveBankReply;
  static deserializeBinaryFromReader(message: UnassignActivityFromObjectiveBankReply, reader: jspb.BinaryReader): UnassignActivityFromObjectiveBankReply;
}

export namespace UnassignActivityFromObjectiveBankReply {
  export type AsObject = {
  }
}

export class UnassignActivityFromObjectiveBankRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignActivityFromObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignActivityFromObjectiveBankRequest): UnassignActivityFromObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignActivityFromObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignActivityFromObjectiveBankRequest;
  static deserializeBinaryFromReader(message: UnassignActivityFromObjectiveBankRequest, reader: jspb.BinaryReader): UnassignActivityFromObjectiveBankRequest;
}

export namespace UnassignActivityFromObjectiveBankRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignActivityToObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignActivityToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignActivityToObjectiveBankReply): ReassignActivityToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignActivityToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignActivityToObjectiveBankReply;
  static deserializeBinaryFromReader(message: ReassignActivityToObjectiveBankReply, reader: jspb.BinaryReader): ReassignActivityToObjectiveBankReply;
}

export namespace ReassignActivityToObjectiveBankReply {
  export type AsObject = {
  }
}

export class ReassignActivityToObjectiveBankRequest extends jspb.Message {
  hasActivityId(): boolean;
  clearActivityId(): void;
  getActivityId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setActivityId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromObjectiveBankId(): boolean;
  clearFromObjectiveBankId(): void;
  getFromObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToObjectiveBankId(): boolean;
  clearToObjectiveBankId(): void;
  getToObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignActivityToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignActivityToObjectiveBankRequest): ReassignActivityToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignActivityToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignActivityToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: ReassignActivityToObjectiveBankRequest, reader: jspb.BinaryReader): ReassignActivityToObjectiveBankRequest;
}

export namespace ReassignActivityToObjectiveBankRequest {
  export type AsObject = {
    activityId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromObjectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toObjectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupProficienciesReply extends jspb.Message {
  getCanLookupProficiencies(): boolean;
  setCanLookupProficiencies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupProficienciesReply): CanLookupProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupProficienciesReply;
  static deserializeBinaryFromReader(message: CanLookupProficienciesReply, reader: jspb.BinaryReader): CanLookupProficienciesReply;
}

export namespace CanLookupProficienciesReply {
  export type AsObject = {
    canLookupProficiencies: boolean,
  }
}

export class CanLookupProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupProficienciesRequest): CanLookupProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupProficienciesRequest;
  static deserializeBinaryFromReader(message: CanLookupProficienciesRequest, reader: jspb.BinaryReader): CanLookupProficienciesRequest;
}

export namespace CanLookupProficienciesRequest {
  export type AsObject = {
  }
}

export class UseComparativeProficiencyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeProficiencyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeProficiencyViewReply): UseComparativeProficiencyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeProficiencyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeProficiencyViewReply;
  static deserializeBinaryFromReader(message: UseComparativeProficiencyViewReply, reader: jspb.BinaryReader): UseComparativeProficiencyViewReply;
}

export namespace UseComparativeProficiencyViewReply {
  export type AsObject = {
  }
}

export class UseComparativeProficiencyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeProficiencyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeProficiencyViewRequest): UseComparativeProficiencyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeProficiencyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeProficiencyViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeProficiencyViewRequest, reader: jspb.BinaryReader): UseComparativeProficiencyViewRequest;
}

export namespace UseComparativeProficiencyViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryProficiencyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryProficiencyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryProficiencyViewReply): UsePlenaryProficiencyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryProficiencyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryProficiencyViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryProficiencyViewReply, reader: jspb.BinaryReader): UsePlenaryProficiencyViewReply;
}

export namespace UsePlenaryProficiencyViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryProficiencyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryProficiencyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryProficiencyViewRequest): UsePlenaryProficiencyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryProficiencyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryProficiencyViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryProficiencyViewRequest, reader: jspb.BinaryReader): UsePlenaryProficiencyViewRequest;
}

export namespace UsePlenaryProficiencyViewRequest {
  export type AsObject = {
  }
}

export class UseEffectiveProficiencyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveProficiencyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveProficiencyViewReply): UseEffectiveProficiencyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveProficiencyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveProficiencyViewReply;
  static deserializeBinaryFromReader(message: UseEffectiveProficiencyViewReply, reader: jspb.BinaryReader): UseEffectiveProficiencyViewReply;
}

export namespace UseEffectiveProficiencyViewReply {
  export type AsObject = {
  }
}

export class UseEffectiveProficiencyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveProficiencyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveProficiencyViewRequest): UseEffectiveProficiencyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveProficiencyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveProficiencyViewRequest;
  static deserializeBinaryFromReader(message: UseEffectiveProficiencyViewRequest, reader: jspb.BinaryReader): UseEffectiveProficiencyViewRequest;
}

export namespace UseEffectiveProficiencyViewRequest {
  export type AsObject = {
  }
}

export class UseAnyEffectiveProficiencyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveProficiencyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveProficiencyViewReply): UseAnyEffectiveProficiencyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveProficiencyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveProficiencyViewReply;
  static deserializeBinaryFromReader(message: UseAnyEffectiveProficiencyViewReply, reader: jspb.BinaryReader): UseAnyEffectiveProficiencyViewReply;
}

export namespace UseAnyEffectiveProficiencyViewReply {
  export type AsObject = {
  }
}

export class UseAnyEffectiveProficiencyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveProficiencyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveProficiencyViewRequest): UseAnyEffectiveProficiencyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveProficiencyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveProficiencyViewRequest;
  static deserializeBinaryFromReader(message: UseAnyEffectiveProficiencyViewRequest, reader: jspb.BinaryReader): UseAnyEffectiveProficiencyViewRequest;
}

export namespace UseAnyEffectiveProficiencyViewRequest {
  export type AsObject = {
  }
}

export class GetProficiencyReply extends jspb.Message {
  hasProficiency(): boolean;
  clearProficiency(): void;
  getProficiency(): Proficiency | undefined;
  setProficiency(value?: Proficiency): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyReply): GetProficiencyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyReply;
  static deserializeBinaryFromReader(message: GetProficiencyReply, reader: jspb.BinaryReader): GetProficiencyReply;
}

export namespace GetProficiencyReply {
  export type AsObject = {
    proficiency?: Proficiency.AsObject,
  }
}

export class GetProficiencyRequest extends jspb.Message {
  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyRequest): GetProficiencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyRequest;
  static deserializeBinaryFromReader(message: GetProficiencyRequest, reader: jspb.BinaryReader): GetProficiencyRequest;
}

export namespace GetProficiencyRequest {
  export type AsObject = {
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetProficienciesByIdsRequest extends jspb.Message {
  clearProficiencyIdsList(): void;
  getProficiencyIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setProficiencyIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addProficiencyIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByIdsRequest): GetProficienciesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByIdsRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByIdsRequest, reader: jspb.BinaryReader): GetProficienciesByIdsRequest;
}

export namespace GetProficienciesByIdsRequest {
  export type AsObject = {
    proficiencyIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetProficienciesByGenusTypeRequest extends jspb.Message {
  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeRequest): GetProficienciesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeRequest;
}

export namespace GetProficienciesByGenusTypeRequest {
  export type AsObject = {
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetProficienciesByParentGenusTypeRequest extends jspb.Message {
  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByParentGenusTypeRequest): GetProficienciesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetProficienciesByParentGenusTypeRequest;
}

export namespace GetProficienciesByParentGenusTypeRequest {
  export type AsObject = {
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetProficienciesByRecordTypeRequest extends jspb.Message {
  hasProficiencyRecordType(): boolean;
  clearProficiencyRecordType(): void;
  getProficiencyRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByRecordTypeRequest): GetProficienciesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByRecordTypeRequest, reader: jspb.BinaryReader): GetProficienciesByRecordTypeRequest;
}

export namespace GetProficienciesByRecordTypeRequest {
  export type AsObject = {
    proficiencyRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetProficienciesOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesOnDateRequest): GetProficienciesOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesOnDateRequest, reader: jspb.BinaryReader): GetProficienciesOnDateRequest;
}

export namespace GetProficienciesOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesByGenusTypeOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeOnDateRequest): GetProficienciesByGenusTypeOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeOnDateRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeOnDateRequest;
}

export namespace GetProficienciesByGenusTypeOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesForObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForObjectiveRequest): GetProficienciesForObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForObjectiveRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForObjectiveRequest, reader: jspb.BinaryReader): GetProficienciesForObjectiveRequest;
}

export namespace GetProficienciesForObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetProficienciesForObjectiveOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForObjectiveOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForObjectiveOnDateRequest): GetProficienciesForObjectiveOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForObjectiveOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForObjectiveOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForObjectiveOnDateRequest, reader: jspb.BinaryReader): GetProficienciesForObjectiveOnDateRequest;
}

export namespace GetProficienciesForObjectiveOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesByGenusTypeForObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeForObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeForObjectiveRequest): GetProficienciesByGenusTypeForObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeForObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeForObjectiveRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeForObjectiveRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeForObjectiveRequest;
}

export namespace GetProficienciesByGenusTypeForObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetProficienciesByGenusTypeForObjectiveOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeForObjectiveOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeForObjectiveOnDateRequest): GetProficienciesByGenusTypeForObjectiveOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeForObjectiveOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeForObjectiveOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeForObjectiveOnDateRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeForObjectiveOnDateRequest;
}

export namespace GetProficienciesByGenusTypeForObjectiveOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesForObjectivesRequest extends jspb.Message {
  clearObjectiveIdsList(): void;
  getObjectiveIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForObjectivesRequest): GetProficienciesForObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForObjectivesRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForObjectivesRequest, reader: jspb.BinaryReader): GetProficienciesForObjectivesRequest;
}

export namespace GetProficienciesForObjectivesRequest {
  export type AsObject = {
    objectiveIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetProficienciesForResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForResourceRequest): GetProficienciesForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForResourceRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForResourceRequest, reader: jspb.BinaryReader): GetProficienciesForResourceRequest;
}

export namespace GetProficienciesForResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetProficienciesForResourceOnDateRequest extends jspb.Message {
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
  toObject(includeInstance?: boolean): GetProficienciesForResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForResourceOnDateRequest): GetProficienciesForResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForResourceOnDateRequest, reader: jspb.BinaryReader): GetProficienciesForResourceOnDateRequest;
}

export namespace GetProficienciesForResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesByGenusTypeForResourceRequest extends jspb.Message {
  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeForResourceRequest): GetProficienciesByGenusTypeForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeForResourceRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeForResourceRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeForResourceRequest;
}

export namespace GetProficienciesByGenusTypeForResourceRequest {
  export type AsObject = {
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetProficienciesByGenusTypeForResourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeForResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeForResourceOnDateRequest): GetProficienciesByGenusTypeForResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeForResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeForResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeForResourceOnDateRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeForResourceOnDateRequest;
}

export namespace GetProficienciesByGenusTypeForResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesForResourcesRequest extends jspb.Message {
  clearResourceIdsList(): void;
  getResourceIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setResourceIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addResourceIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForResourcesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForResourcesRequest): GetProficienciesForResourcesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForResourcesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForResourcesRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForResourcesRequest, reader: jspb.BinaryReader): GetProficienciesForResourcesRequest;
}

export namespace GetProficienciesForResourcesRequest {
  export type AsObject = {
    resourceIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetProficienciesForObjectiveAndResourceRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForObjectiveAndResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForObjectiveAndResourceRequest): GetProficienciesForObjectiveAndResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForObjectiveAndResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForObjectiveAndResourceRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForObjectiveAndResourceRequest, reader: jspb.BinaryReader): GetProficienciesForObjectiveAndResourceRequest;
}

export namespace GetProficienciesForObjectiveAndResourceRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetProficienciesForObjectiveAndResourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesForObjectiveAndResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesForObjectiveAndResourceOnDateRequest): GetProficienciesForObjectiveAndResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesForObjectiveAndResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesForObjectiveAndResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesForObjectiveAndResourceOnDateRequest, reader: jspb.BinaryReader): GetProficienciesForObjectiveAndResourceOnDateRequest;
}

export namespace GetProficienciesForObjectiveAndResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesByGenusTypeForObjectiveAndResourceRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeForObjectiveAndResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeForObjectiveAndResourceRequest): GetProficienciesByGenusTypeForObjectiveAndResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeForObjectiveAndResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeForObjectiveAndResourceRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeForObjectiveAndResourceRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeForObjectiveAndResourceRequest;
}

export namespace GetProficienciesByGenusTypeForObjectiveAndResourceRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyGenusType(): boolean;
  clearProficiencyGenusType(): void;
  getProficiencyGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setProficiencyGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest): GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest, reader: jspb.BinaryReader): GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest;
}

export namespace GetProficienciesByGenusTypeForObjectiveAndResourceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesRequest): GetProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesRequest;
  static deserializeBinaryFromReader(message: GetProficienciesRequest, reader: jspb.BinaryReader): GetProficienciesRequest;
}

export namespace GetProficienciesRequest {
  export type AsObject = {
  }
}

export class CanSearchProficienciesReply extends jspb.Message {
  getCanSearchProficiencies(): boolean;
  setCanSearchProficiencies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchProficienciesReply): CanSearchProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchProficienciesReply;
  static deserializeBinaryFromReader(message: CanSearchProficienciesReply, reader: jspb.BinaryReader): CanSearchProficienciesReply;
}

export namespace CanSearchProficienciesReply {
  export type AsObject = {
    canSearchProficiencies: boolean,
  }
}

export class CanSearchProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchProficienciesRequest): CanSearchProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchProficienciesRequest;
  static deserializeBinaryFromReader(message: CanSearchProficienciesRequest, reader: jspb.BinaryReader): CanSearchProficienciesRequest;
}

export namespace CanSearchProficienciesRequest {
  export type AsObject = {
  }
}

export class GetProficiencyQueryReply extends jspb.Message {
  hasProficiencyQuery(): boolean;
  clearProficiencyQuery(): void;
  getProficiencyQuery(): ProficiencyQuery | undefined;
  setProficiencyQuery(value?: ProficiencyQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyQueryReply): GetProficiencyQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyQueryReply;
  static deserializeBinaryFromReader(message: GetProficiencyQueryReply, reader: jspb.BinaryReader): GetProficiencyQueryReply;
}

export namespace GetProficiencyQueryReply {
  export type AsObject = {
    proficiencyQuery?: ProficiencyQuery.AsObject,
  }
}

export class GetProficiencyQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyQueryRequest): GetProficiencyQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyQueryRequest;
  static deserializeBinaryFromReader(message: GetProficiencyQueryRequest, reader: jspb.BinaryReader): GetProficiencyQueryRequest;
}

export namespace GetProficiencyQueryRequest {
  export type AsObject = {
  }
}

export class GetProficienciesByQueryRequest extends jspb.Message {
  hasProficiencyQuery(): boolean;
  clearProficiencyQuery(): void;
  getProficiencyQuery(): ProficiencyQuery | undefined;
  setProficiencyQuery(value?: ProficiencyQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficienciesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficienciesByQueryRequest): GetProficienciesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficienciesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficienciesByQueryRequest;
  static deserializeBinaryFromReader(message: GetProficienciesByQueryRequest, reader: jspb.BinaryReader): GetProficienciesByQueryRequest;
}

export namespace GetProficienciesByQueryRequest {
  export type AsObject = {
    proficiencyQuery?: ProficiencyQuery.AsObject,
  }
}

export class CanCreateProficienciesReply extends jspb.Message {
  getCanCreateProficiencies(): boolean;
  setCanCreateProficiencies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateProficienciesReply): CanCreateProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateProficienciesReply;
  static deserializeBinaryFromReader(message: CanCreateProficienciesReply, reader: jspb.BinaryReader): CanCreateProficienciesReply;
}

export namespace CanCreateProficienciesReply {
  export type AsObject = {
    canCreateProficiencies: boolean,
  }
}

export class CanCreateProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateProficienciesRequest): CanCreateProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateProficienciesRequest;
  static deserializeBinaryFromReader(message: CanCreateProficienciesRequest, reader: jspb.BinaryReader): CanCreateProficienciesRequest;
}

export namespace CanCreateProficienciesRequest {
  export type AsObject = {
  }
}

export class CanCreateProficiencyWithRecordTypesReply extends jspb.Message {
  getCanCreateProficiencyWithRecordTypes(): boolean;
  setCanCreateProficiencyWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateProficiencyWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateProficiencyWithRecordTypesReply): CanCreateProficiencyWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateProficiencyWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateProficiencyWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateProficiencyWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateProficiencyWithRecordTypesReply;
}

export namespace CanCreateProficiencyWithRecordTypesReply {
  export type AsObject = {
    canCreateProficiencyWithRecordTypes: boolean,
  }
}

export class CanCreateProficiencyWithRecordTypesRequest extends jspb.Message {
  clearProficiencyRecordTypesList(): void;
  getProficiencyRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setProficiencyRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addProficiencyRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateProficiencyWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateProficiencyWithRecordTypesRequest): CanCreateProficiencyWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateProficiencyWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateProficiencyWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateProficiencyWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateProficiencyWithRecordTypesRequest;
}

export namespace CanCreateProficiencyWithRecordTypesRequest {
  export type AsObject = {
    proficiencyRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetProficiencyFormForCreateReply extends jspb.Message {
  hasProficiencyForm(): boolean;
  clearProficiencyForm(): void;
  getProficiencyForm(): ProficiencyForm | undefined;
  setProficiencyForm(value?: ProficiencyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyFormForCreateReply): GetProficiencyFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyFormForCreateReply;
  static deserializeBinaryFromReader(message: GetProficiencyFormForCreateReply, reader: jspb.BinaryReader): GetProficiencyFormForCreateReply;
}

export namespace GetProficiencyFormForCreateReply {
  export type AsObject = {
    proficiencyForm?: ProficiencyForm.AsObject,
  }
}

export class GetProficiencyFormForCreateRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearProficiencyRecordTypesList(): void;
  getProficiencyRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setProficiencyRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addProficiencyRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyFormForCreateRequest): GetProficiencyFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetProficiencyFormForCreateRequest, reader: jspb.BinaryReader): GetProficiencyFormForCreateRequest;
}

export namespace GetProficiencyFormForCreateRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateProficiencyReply extends jspb.Message {
  hasProficiency(): boolean;
  clearProficiency(): void;
  getProficiency(): Proficiency | undefined;
  setProficiency(value?: Proficiency): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateProficiencyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateProficiencyReply): CreateProficiencyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateProficiencyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateProficiencyReply;
  static deserializeBinaryFromReader(message: CreateProficiencyReply, reader: jspb.BinaryReader): CreateProficiencyReply;
}

export namespace CreateProficiencyReply {
  export type AsObject = {
    proficiency?: Proficiency.AsObject,
  }
}

export class CreateProficiencyRequest extends jspb.Message {
  hasProficiencyForm(): boolean;
  clearProficiencyForm(): void;
  getProficiencyForm(): ProficiencyForm | undefined;
  setProficiencyForm(value?: ProficiencyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateProficiencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateProficiencyRequest): CreateProficiencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateProficiencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateProficiencyRequest;
  static deserializeBinaryFromReader(message: CreateProficiencyRequest, reader: jspb.BinaryReader): CreateProficiencyRequest;
}

export namespace CreateProficiencyRequest {
  export type AsObject = {
    proficiencyForm?: ProficiencyForm.AsObject,
  }
}

export class CanUpdateProficienciesReply extends jspb.Message {
  getCanUpdateProficiencies(): boolean;
  setCanUpdateProficiencies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateProficienciesReply): CanUpdateProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateProficienciesReply;
  static deserializeBinaryFromReader(message: CanUpdateProficienciesReply, reader: jspb.BinaryReader): CanUpdateProficienciesReply;
}

export namespace CanUpdateProficienciesReply {
  export type AsObject = {
    canUpdateProficiencies: boolean,
  }
}

export class CanUpdateProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateProficienciesRequest): CanUpdateProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateProficienciesRequest;
  static deserializeBinaryFromReader(message: CanUpdateProficienciesRequest, reader: jspb.BinaryReader): CanUpdateProficienciesRequest;
}

export namespace CanUpdateProficienciesRequest {
  export type AsObject = {
  }
}

export class GetProficiencyFormForUpdateReply extends jspb.Message {
  hasProficiencyForm(): boolean;
  clearProficiencyForm(): void;
  getProficiencyForm(): ProficiencyForm | undefined;
  setProficiencyForm(value?: ProficiencyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyFormForUpdateReply): GetProficiencyFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetProficiencyFormForUpdateReply, reader: jspb.BinaryReader): GetProficiencyFormForUpdateReply;
}

export namespace GetProficiencyFormForUpdateReply {
  export type AsObject = {
    proficiencyForm?: ProficiencyForm.AsObject,
  }
}

export class GetProficiencyFormForUpdateRequest extends jspb.Message {
  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProficiencyFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProficiencyFormForUpdateRequest): GetProficiencyFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProficiencyFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProficiencyFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetProficiencyFormForUpdateRequest, reader: jspb.BinaryReader): GetProficiencyFormForUpdateRequest;
}

export namespace GetProficiencyFormForUpdateRequest {
  export type AsObject = {
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateProficiencyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateProficiencyReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateProficiencyReply): UpdateProficiencyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateProficiencyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateProficiencyReply;
  static deserializeBinaryFromReader(message: UpdateProficiencyReply, reader: jspb.BinaryReader): UpdateProficiencyReply;
}

export namespace UpdateProficiencyReply {
  export type AsObject = {
  }
}

export class UpdateProficiencyRequest extends jspb.Message {
  hasProficiencyForm(): boolean;
  clearProficiencyForm(): void;
  getProficiencyForm(): ProficiencyForm | undefined;
  setProficiencyForm(value?: ProficiencyForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateProficiencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateProficiencyRequest): UpdateProficiencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateProficiencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateProficiencyRequest;
  static deserializeBinaryFromReader(message: UpdateProficiencyRequest, reader: jspb.BinaryReader): UpdateProficiencyRequest;
}

export namespace UpdateProficiencyRequest {
  export type AsObject = {
    proficiencyForm?: ProficiencyForm.AsObject,
  }
}

export class CanDeleteProficienciesReply extends jspb.Message {
  getCanDeleteProficiencies(): boolean;
  setCanDeleteProficiencies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteProficienciesReply): CanDeleteProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteProficienciesReply;
  static deserializeBinaryFromReader(message: CanDeleteProficienciesReply, reader: jspb.BinaryReader): CanDeleteProficienciesReply;
}

export namespace CanDeleteProficienciesReply {
  export type AsObject = {
    canDeleteProficiencies: boolean,
  }
}

export class CanDeleteProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteProficienciesRequest): CanDeleteProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteProficienciesRequest;
  static deserializeBinaryFromReader(message: CanDeleteProficienciesRequest, reader: jspb.BinaryReader): CanDeleteProficienciesRequest;
}

export namespace CanDeleteProficienciesRequest {
  export type AsObject = {
  }
}

export class DeleteProficiencyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteProficiencyReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteProficiencyReply): DeleteProficiencyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteProficiencyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteProficiencyReply;
  static deserializeBinaryFromReader(message: DeleteProficiencyReply, reader: jspb.BinaryReader): DeleteProficiencyReply;
}

export namespace DeleteProficiencyReply {
  export type AsObject = {
  }
}

export class DeleteProficiencyRequest extends jspb.Message {
  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteProficiencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteProficiencyRequest): DeleteProficiencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteProficiencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteProficiencyRequest;
  static deserializeBinaryFromReader(message: DeleteProficiencyRequest, reader: jspb.BinaryReader): DeleteProficiencyRequest;
}

export namespace DeleteProficiencyRequest {
  export type AsObject = {
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class DeleteProficienciesReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteProficienciesReply): DeleteProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteProficienciesReply;
  static deserializeBinaryFromReader(message: DeleteProficienciesReply, reader: jspb.BinaryReader): DeleteProficienciesReply;
}

export namespace DeleteProficienciesReply {
  export type AsObject = {
  }
}

export class DeleteProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteProficienciesRequest): DeleteProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteProficienciesRequest;
  static deserializeBinaryFromReader(message: DeleteProficienciesRequest, reader: jspb.BinaryReader): DeleteProficienciesRequest;
}

export namespace DeleteProficienciesRequest {
  export type AsObject = {
  }
}

export class CanManageProficiencyAliasesReply extends jspb.Message {
  getCanManageProficiencyAliases(): boolean;
  setCanManageProficiencyAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageProficiencyAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageProficiencyAliasesReply): CanManageProficiencyAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageProficiencyAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageProficiencyAliasesReply;
  static deserializeBinaryFromReader(message: CanManageProficiencyAliasesReply, reader: jspb.BinaryReader): CanManageProficiencyAliasesReply;
}

export namespace CanManageProficiencyAliasesReply {
  export type AsObject = {
    canManageProficiencyAliases: boolean,
  }
}

export class CanManageProficiencyAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageProficiencyAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageProficiencyAliasesRequest): CanManageProficiencyAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageProficiencyAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageProficiencyAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageProficiencyAliasesRequest, reader: jspb.BinaryReader): CanManageProficiencyAliasesRequest;
}

export namespace CanManageProficiencyAliasesRequest {
  export type AsObject = {
  }
}

export class AliasProficiencyReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasProficiencyReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasProficiencyReply): AliasProficiencyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasProficiencyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasProficiencyReply;
  static deserializeBinaryFromReader(message: AliasProficiencyReply, reader: jspb.BinaryReader): AliasProficiencyReply;
}

export namespace AliasProficiencyReply {
  export type AsObject = {
  }
}

export class AliasProficiencyRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasProficiencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasProficiencyRequest): AliasProficiencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasProficiencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasProficiencyRequest;
  static deserializeBinaryFromReader(message: AliasProficiencyRequest, reader: jspb.BinaryReader): AliasProficiencyRequest;
}

export namespace AliasProficiencyRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignProficienciesReply extends jspb.Message {
  getCanAssignProficiencies(): boolean;
  setCanAssignProficiencies(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignProficienciesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignProficienciesReply): CanAssignProficienciesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignProficienciesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignProficienciesReply;
  static deserializeBinaryFromReader(message: CanAssignProficienciesReply, reader: jspb.BinaryReader): CanAssignProficienciesReply;
}

export namespace CanAssignProficienciesReply {
  export type AsObject = {
    canAssignProficiencies: boolean,
  }
}

export class CanAssignProficienciesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignProficienciesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignProficienciesRequest): CanAssignProficienciesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignProficienciesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignProficienciesRequest;
  static deserializeBinaryFromReader(message: CanAssignProficienciesRequest, reader: jspb.BinaryReader): CanAssignProficienciesRequest;
}

export namespace CanAssignProficienciesRequest {
  export type AsObject = {
  }
}

export class CanAssignProficienciesToObjectiveBankReply extends jspb.Message {
  getCanAssignProficienciesToObjectiveBank(): boolean;
  setCanAssignProficienciesToObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignProficienciesToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignProficienciesToObjectiveBankReply): CanAssignProficienciesToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignProficienciesToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignProficienciesToObjectiveBankReply;
  static deserializeBinaryFromReader(message: CanAssignProficienciesToObjectiveBankReply, reader: jspb.BinaryReader): CanAssignProficienciesToObjectiveBankReply;
}

export namespace CanAssignProficienciesToObjectiveBankReply {
  export type AsObject = {
    canAssignProficienciesToObjectiveBank: boolean,
  }
}

export class CanAssignProficienciesToObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignProficienciesToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignProficienciesToObjectiveBankRequest): CanAssignProficienciesToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignProficienciesToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignProficienciesToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: CanAssignProficienciesToObjectiveBankRequest, reader: jspb.BinaryReader): CanAssignProficienciesToObjectiveBankRequest;
}

export namespace CanAssignProficienciesToObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableObjectiveBankIdsForProficiencyRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableObjectiveBankIdsForProficiencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableObjectiveBankIdsForProficiencyRequest): GetAssignableObjectiveBankIdsForProficiencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableObjectiveBankIdsForProficiencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableObjectiveBankIdsForProficiencyRequest;
  static deserializeBinaryFromReader(message: GetAssignableObjectiveBankIdsForProficiencyRequest, reader: jspb.BinaryReader): GetAssignableObjectiveBankIdsForProficiencyRequest;
}

export namespace GetAssignableObjectiveBankIdsForProficiencyRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignProficiencyToObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignProficiencyToObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignProficiencyToObjectiveBankReply): AssignProficiencyToObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignProficiencyToObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignProficiencyToObjectiveBankReply;
  static deserializeBinaryFromReader(message: AssignProficiencyToObjectiveBankReply, reader: jspb.BinaryReader): AssignProficiencyToObjectiveBankReply;
}

export namespace AssignProficiencyToObjectiveBankReply {
  export type AsObject = {
  }
}

export class AssignProficiencyToObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignProficiencyToObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignProficiencyToObjectiveBankRequest): AssignProficiencyToObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignProficiencyToObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignProficiencyToObjectiveBankRequest;
  static deserializeBinaryFromReader(message: AssignProficiencyToObjectiveBankRequest, reader: jspb.BinaryReader): AssignProficiencyToObjectiveBankRequest;
}

export namespace AssignProficiencyToObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignProficiencyFromObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignProficiencyFromObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignProficiencyFromObjectiveBankReply): UnassignProficiencyFromObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignProficiencyFromObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignProficiencyFromObjectiveBankReply;
  static deserializeBinaryFromReader(message: UnassignProficiencyFromObjectiveBankReply, reader: jspb.BinaryReader): UnassignProficiencyFromObjectiveBankReply;
}

export namespace UnassignProficiencyFromObjectiveBankReply {
  export type AsObject = {
  }
}

export class UnassignProficiencyFromObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasProficiencyId(): boolean;
  clearProficiencyId(): void;
  getProficiencyId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setProficiencyId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignProficiencyFromObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignProficiencyFromObjectiveBankRequest): UnassignProficiencyFromObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignProficiencyFromObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignProficiencyFromObjectiveBankRequest;
  static deserializeBinaryFromReader(message: UnassignProficiencyFromObjectiveBankRequest, reader: jspb.BinaryReader): UnassignProficiencyFromObjectiveBankRequest;
}

export namespace UnassignProficiencyFromObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    proficiencyId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupObjectiveBanksReply extends jspb.Message {
  getCanLookupObjectiveBanks(): boolean;
  setCanLookupObjectiveBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectiveBanksReply): CanLookupObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectiveBanksReply;
  static deserializeBinaryFromReader(message: CanLookupObjectiveBanksReply, reader: jspb.BinaryReader): CanLookupObjectiveBanksReply;
}

export namespace CanLookupObjectiveBanksReply {
  export type AsObject = {
    canLookupObjectiveBanks: boolean,
  }
}

export class CanLookupObjectiveBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupObjectiveBanksRequest): CanLookupObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: CanLookupObjectiveBanksRequest, reader: jspb.BinaryReader): CanLookupObjectiveBanksRequest;
}

export namespace CanLookupObjectiveBanksRequest {
  export type AsObject = {
  }
}

export class GetObjectiveBanksByIdsRequest extends jspb.Message {
  clearObjectiveBankIdsList(): void;
  getObjectiveBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByIdsRequest): GetObjectiveBanksByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByIdsRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByIdsRequest, reader: jspb.BinaryReader): GetObjectiveBanksByIdsRequest;
}

export namespace GetObjectiveBanksByIdsRequest {
  export type AsObject = {
    objectiveBankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetObjectiveBanksByGenusTypeRequest extends jspb.Message {
  hasObjectiveBankGenusType(): boolean;
  clearObjectiveBankGenusType(): void;
  getObjectiveBankGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setObjectiveBankGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByGenusTypeRequest): GetObjectiveBanksByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByGenusTypeRequest, reader: jspb.BinaryReader): GetObjectiveBanksByGenusTypeRequest;
}

export namespace GetObjectiveBanksByGenusTypeRequest {
  export type AsObject = {
    objectiveBankGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetObjectiveBanksByParentGenusTypeRequest extends jspb.Message {
  hasObjectiveBankGenusType(): boolean;
  clearObjectiveBankGenusType(): void;
  getObjectiveBankGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setObjectiveBankGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByParentGenusTypeRequest): GetObjectiveBanksByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByParentGenusTypeRequest, reader: jspb.BinaryReader): GetObjectiveBanksByParentGenusTypeRequest;
}

export namespace GetObjectiveBanksByParentGenusTypeRequest {
  export type AsObject = {
    objectiveBankGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetObjectiveBanksByRecordTypeRequest extends jspb.Message {
  hasObjectiveBankRecordType(): boolean;
  clearObjectiveBankRecordType(): void;
  getObjectiveBankRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setObjectiveBankRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByRecordTypeRequest): GetObjectiveBanksByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByRecordTypeRequest, reader: jspb.BinaryReader): GetObjectiveBanksByRecordTypeRequest;
}

export namespace GetObjectiveBanksByRecordTypeRequest {
  export type AsObject = {
    objectiveBankRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetObjectiveBanksByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksByProviderRequest): GetObjectiveBanksByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksByProviderRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksByProviderRequest, reader: jspb.BinaryReader): GetObjectiveBanksByProviderRequest;
}

export namespace GetObjectiveBanksByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBanksRequest): GetObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBanksRequest, reader: jspb.BinaryReader): GetObjectiveBanksRequest;
}

export namespace GetObjectiveBanksRequest {
  export type AsObject = {
  }
}

export class CanCreateObjectiveBanksReply extends jspb.Message {
  getCanCreateObjectiveBanks(): boolean;
  setCanCreateObjectiveBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectiveBanksReply): CanCreateObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectiveBanksReply;
  static deserializeBinaryFromReader(message: CanCreateObjectiveBanksReply, reader: jspb.BinaryReader): CanCreateObjectiveBanksReply;
}

export namespace CanCreateObjectiveBanksReply {
  export type AsObject = {
    canCreateObjectiveBanks: boolean,
  }
}

export class CanCreateObjectiveBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectiveBanksRequest): CanCreateObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: CanCreateObjectiveBanksRequest, reader: jspb.BinaryReader): CanCreateObjectiveBanksRequest;
}

export namespace CanCreateObjectiveBanksRequest {
  export type AsObject = {
  }
}

export class CanCreateObjectiveBankWithRecordTypesReply extends jspb.Message {
  getCanCreateObjectiveBankWithRecordTypes(): boolean;
  setCanCreateObjectiveBankWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectiveBankWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectiveBankWithRecordTypesReply): CanCreateObjectiveBankWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectiveBankWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectiveBankWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateObjectiveBankWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateObjectiveBankWithRecordTypesReply;
}

export namespace CanCreateObjectiveBankWithRecordTypesReply {
  export type AsObject = {
    canCreateObjectiveBankWithRecordTypes: boolean,
  }
}

export class CanCreateObjectiveBankWithRecordTypesRequest extends jspb.Message {
  clearObjectiveBankRecordTypesList(): void;
  getObjectiveBankRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setObjectiveBankRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addObjectiveBankRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateObjectiveBankWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateObjectiveBankWithRecordTypesRequest): CanCreateObjectiveBankWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateObjectiveBankWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateObjectiveBankWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateObjectiveBankWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateObjectiveBankWithRecordTypesRequest;
}

export namespace CanCreateObjectiveBankWithRecordTypesRequest {
  export type AsObject = {
    objectiveBankRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetObjectiveBankFormForCreateReply extends jspb.Message {
  hasObjectiveBankForm(): boolean;
  clearObjectiveBankForm(): void;
  getObjectiveBankForm(): ObjectiveBankForm | undefined;
  setObjectiveBankForm(value?: ObjectiveBankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankFormForCreateReply): GetObjectiveBankFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankFormForCreateReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankFormForCreateReply, reader: jspb.BinaryReader): GetObjectiveBankFormForCreateReply;
}

export namespace GetObjectiveBankFormForCreateReply {
  export type AsObject = {
    objectiveBankForm?: ObjectiveBankForm.AsObject,
  }
}

export class GetObjectiveBankFormForCreateRequest extends jspb.Message {
  clearObjectiveBankRecordTypesList(): void;
  getObjectiveBankRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setObjectiveBankRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addObjectiveBankRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankFormForCreateRequest): GetObjectiveBankFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankFormForCreateRequest, reader: jspb.BinaryReader): GetObjectiveBankFormForCreateRequest;
}

export namespace GetObjectiveBankFormForCreateRequest {
  export type AsObject = {
    objectiveBankRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateObjectiveBankReply extends jspb.Message {
  hasObjectiveBank(): boolean;
  clearObjectiveBank(): void;
  getObjectiveBank(): ObjectiveBank | undefined;
  setObjectiveBank(value?: ObjectiveBank): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateObjectiveBankReply): CreateObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateObjectiveBankReply;
  static deserializeBinaryFromReader(message: CreateObjectiveBankReply, reader: jspb.BinaryReader): CreateObjectiveBankReply;
}

export namespace CreateObjectiveBankReply {
  export type AsObject = {
    objectiveBank?: ObjectiveBank.AsObject,
  }
}

export class CreateObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankForm(): boolean;
  clearObjectiveBankForm(): void;
  getObjectiveBankForm(): ObjectiveBankForm | undefined;
  setObjectiveBankForm(value?: ObjectiveBankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateObjectiveBankRequest): CreateObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateObjectiveBankRequest;
  static deserializeBinaryFromReader(message: CreateObjectiveBankRequest, reader: jspb.BinaryReader): CreateObjectiveBankRequest;
}

export namespace CreateObjectiveBankRequest {
  export type AsObject = {
    objectiveBankForm?: ObjectiveBankForm.AsObject,
  }
}

export class CanUpdateObjectiveBanksReply extends jspb.Message {
  getCanUpdateObjectiveBanks(): boolean;
  setCanUpdateObjectiveBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateObjectiveBanksReply): CanUpdateObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateObjectiveBanksReply;
  static deserializeBinaryFromReader(message: CanUpdateObjectiveBanksReply, reader: jspb.BinaryReader): CanUpdateObjectiveBanksReply;
}

export namespace CanUpdateObjectiveBanksReply {
  export type AsObject = {
    canUpdateObjectiveBanks: boolean,
  }
}

export class CanUpdateObjectiveBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateObjectiveBanksRequest): CanUpdateObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: CanUpdateObjectiveBanksRequest, reader: jspb.BinaryReader): CanUpdateObjectiveBanksRequest;
}

export namespace CanUpdateObjectiveBanksRequest {
  export type AsObject = {
  }
}

export class GetObjectiveBankFormForUpdateReply extends jspb.Message {
  hasObjectiveBankForm(): boolean;
  clearObjectiveBankForm(): void;
  getObjectiveBankForm(): ObjectiveBankForm | undefined;
  setObjectiveBankForm(value?: ObjectiveBankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankFormForUpdateReply): GetObjectiveBankFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankFormForUpdateReply, reader: jspb.BinaryReader): GetObjectiveBankFormForUpdateReply;
}

export namespace GetObjectiveBankFormForUpdateReply {
  export type AsObject = {
    objectiveBankForm?: ObjectiveBankForm.AsObject,
  }
}

export class GetObjectiveBankFormForUpdateRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankFormForUpdateRequest): GetObjectiveBankFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankFormForUpdateRequest, reader: jspb.BinaryReader): GetObjectiveBankFormForUpdateRequest;
}

export namespace GetObjectiveBankFormForUpdateRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateObjectiveBankReply): UpdateObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateObjectiveBankReply;
  static deserializeBinaryFromReader(message: UpdateObjectiveBankReply, reader: jspb.BinaryReader): UpdateObjectiveBankReply;
}

export namespace UpdateObjectiveBankReply {
  export type AsObject = {
  }
}

export class UpdateObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankForm(): boolean;
  clearObjectiveBankForm(): void;
  getObjectiveBankForm(): ObjectiveBankForm | undefined;
  setObjectiveBankForm(value?: ObjectiveBankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateObjectiveBankRequest): UpdateObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateObjectiveBankRequest;
  static deserializeBinaryFromReader(message: UpdateObjectiveBankRequest, reader: jspb.BinaryReader): UpdateObjectiveBankRequest;
}

export namespace UpdateObjectiveBankRequest {
  export type AsObject = {
    objectiveBankForm?: ObjectiveBankForm.AsObject,
  }
}

export class CanDeleteObjectiveBanksReply extends jspb.Message {
  getCanDeleteObjectiveBanks(): boolean;
  setCanDeleteObjectiveBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteObjectiveBanksReply): CanDeleteObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteObjectiveBanksReply;
  static deserializeBinaryFromReader(message: CanDeleteObjectiveBanksReply, reader: jspb.BinaryReader): CanDeleteObjectiveBanksReply;
}

export namespace CanDeleteObjectiveBanksReply {
  export type AsObject = {
    canDeleteObjectiveBanks: boolean,
  }
}

export class CanDeleteObjectiveBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteObjectiveBanksRequest): CanDeleteObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: CanDeleteObjectiveBanksRequest, reader: jspb.BinaryReader): CanDeleteObjectiveBanksRequest;
}

export namespace CanDeleteObjectiveBanksRequest {
  export type AsObject = {
  }
}

export class DeleteObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteObjectiveBankReply): DeleteObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteObjectiveBankReply;
  static deserializeBinaryFromReader(message: DeleteObjectiveBankReply, reader: jspb.BinaryReader): DeleteObjectiveBankReply;
}

export namespace DeleteObjectiveBankReply {
  export type AsObject = {
  }
}

export class DeleteObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteObjectiveBankRequest): DeleteObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteObjectiveBankRequest;
  static deserializeBinaryFromReader(message: DeleteObjectiveBankRequest, reader: jspb.BinaryReader): DeleteObjectiveBankRequest;
}

export namespace DeleteObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageObjectiveBankAliasesReply extends jspb.Message {
  getCanManageObjectiveBankAliases(): boolean;
  setCanManageObjectiveBankAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageObjectiveBankAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageObjectiveBankAliasesReply): CanManageObjectiveBankAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageObjectiveBankAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageObjectiveBankAliasesReply;
  static deserializeBinaryFromReader(message: CanManageObjectiveBankAliasesReply, reader: jspb.BinaryReader): CanManageObjectiveBankAliasesReply;
}

export namespace CanManageObjectiveBankAliasesReply {
  export type AsObject = {
    canManageObjectiveBankAliases: boolean,
  }
}

export class CanManageObjectiveBankAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageObjectiveBankAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageObjectiveBankAliasesRequest): CanManageObjectiveBankAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageObjectiveBankAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageObjectiveBankAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageObjectiveBankAliasesRequest, reader: jspb.BinaryReader): CanManageObjectiveBankAliasesRequest;
}

export namespace CanManageObjectiveBankAliasesRequest {
  export type AsObject = {
  }
}

export class AliasObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasObjectiveBankReply): AliasObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasObjectiveBankReply;
  static deserializeBinaryFromReader(message: AliasObjectiveBankReply, reader: jspb.BinaryReader): AliasObjectiveBankReply;
}

export namespace AliasObjectiveBankReply {
  export type AsObject = {
  }
}

export class AliasObjectiveBankRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasObjectiveBankRequest): AliasObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasObjectiveBankRequest;
  static deserializeBinaryFromReader(message: AliasObjectiveBankRequest, reader: jspb.BinaryReader): AliasObjectiveBankRequest;
}

export namespace AliasObjectiveBankRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBankHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankHierarchyIdReply): GetObjectiveBankHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankHierarchyIdReply, reader: jspb.BinaryReader): GetObjectiveBankHierarchyIdReply;
}

export namespace GetObjectiveBankHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBankHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankHierarchyIdRequest): GetObjectiveBankHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankHierarchyIdRequest, reader: jspb.BinaryReader): GetObjectiveBankHierarchyIdRequest;
}

export namespace GetObjectiveBankHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetObjectiveBankHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankHierarchyReply): GetObjectiveBankHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankHierarchyReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankHierarchyReply, reader: jspb.BinaryReader): GetObjectiveBankHierarchyReply;
}

export namespace GetObjectiveBankHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetObjectiveBankHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankHierarchyRequest): GetObjectiveBankHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankHierarchyRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankHierarchyRequest, reader: jspb.BinaryReader): GetObjectiveBankHierarchyRequest;
}

export namespace GetObjectiveBankHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessObjectiveBankHierarchyReply extends jspb.Message {
  getCanAccessObjectiveBankHierarchy(): boolean;
  setCanAccessObjectiveBankHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessObjectiveBankHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessObjectiveBankHierarchyReply): CanAccessObjectiveBankHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessObjectiveBankHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessObjectiveBankHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessObjectiveBankHierarchyReply, reader: jspb.BinaryReader): CanAccessObjectiveBankHierarchyReply;
}

export namespace CanAccessObjectiveBankHierarchyReply {
  export type AsObject = {
    canAccessObjectiveBankHierarchy: boolean,
  }
}

export class CanAccessObjectiveBankHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessObjectiveBankHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessObjectiveBankHierarchyRequest): CanAccessObjectiveBankHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessObjectiveBankHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessObjectiveBankHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessObjectiveBankHierarchyRequest, reader: jspb.BinaryReader): CanAccessObjectiveBankHierarchyRequest;
}

export namespace CanAccessObjectiveBankHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootObjectiveBankIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootObjectiveBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootObjectiveBankIdsRequest): GetRootObjectiveBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootObjectiveBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootObjectiveBankIdsRequest;
  static deserializeBinaryFromReader(message: GetRootObjectiveBankIdsRequest, reader: jspb.BinaryReader): GetRootObjectiveBankIdsRequest;
}

export namespace GetRootObjectiveBankIdsRequest {
  export type AsObject = {
  }
}

export class GetRootObjectiveBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootObjectiveBanksRequest): GetRootObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetRootObjectiveBanksRequest, reader: jspb.BinaryReader): GetRootObjectiveBanksRequest;
}

export namespace GetRootObjectiveBanksRequest {
  export type AsObject = {
  }
}

export class HasParentObjectiveBanksReply extends jspb.Message {
  getHasParentObjectiveBanks(): boolean;
  setHasParentObjectiveBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentObjectiveBanksReply): HasParentObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentObjectiveBanksReply;
  static deserializeBinaryFromReader(message: HasParentObjectiveBanksReply, reader: jspb.BinaryReader): HasParentObjectiveBanksReply;
}

export namespace HasParentObjectiveBanksReply {
  export type AsObject = {
    hasParentObjectiveBanks: boolean,
  }
}

export class HasParentObjectiveBanksRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentObjectiveBanksRequest): HasParentObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: HasParentObjectiveBanksRequest, reader: jspb.BinaryReader): HasParentObjectiveBanksRequest;
}

export namespace HasParentObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfObjectiveBankReply extends jspb.Message {
  getIsParentOfObjectiveBank(): boolean;
  setIsParentOfObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfObjectiveBankReply): IsParentOfObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfObjectiveBankReply;
  static deserializeBinaryFromReader(message: IsParentOfObjectiveBankReply, reader: jspb.BinaryReader): IsParentOfObjectiveBankReply;
}

export namespace IsParentOfObjectiveBankReply {
  export type AsObject = {
    isParentOfObjectiveBank: boolean,
  }
}

export class IsParentOfObjectiveBankRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfObjectiveBankRequest): IsParentOfObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfObjectiveBankRequest;
  static deserializeBinaryFromReader(message: IsParentOfObjectiveBankRequest, reader: jspb.BinaryReader): IsParentOfObjectiveBankRequest;
}

export namespace IsParentOfObjectiveBankRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentObjectiveBankIdsRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentObjectiveBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentObjectiveBankIdsRequest): GetParentObjectiveBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentObjectiveBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentObjectiveBankIdsRequest;
  static deserializeBinaryFromReader(message: GetParentObjectiveBankIdsRequest, reader: jspb.BinaryReader): GetParentObjectiveBankIdsRequest;
}

export namespace GetParentObjectiveBankIdsRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentObjectiveBanksRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentObjectiveBanksRequest): GetParentObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetParentObjectiveBanksRequest, reader: jspb.BinaryReader): GetParentObjectiveBanksRequest;
}

export namespace GetParentObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfObjectiveBankReply extends jspb.Message {
  getIsAncestorOfObjectiveBank(): boolean;
  setIsAncestorOfObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfObjectiveBankReply): IsAncestorOfObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfObjectiveBankReply;
  static deserializeBinaryFromReader(message: IsAncestorOfObjectiveBankReply, reader: jspb.BinaryReader): IsAncestorOfObjectiveBankReply;
}

export namespace IsAncestorOfObjectiveBankReply {
  export type AsObject = {
    isAncestorOfObjectiveBank: boolean,
  }
}

export class IsAncestorOfObjectiveBankRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfObjectiveBankRequest): IsAncestorOfObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfObjectiveBankRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfObjectiveBankRequest, reader: jspb.BinaryReader): IsAncestorOfObjectiveBankRequest;
}

export namespace IsAncestorOfObjectiveBankRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildObjectiveBanksReply extends jspb.Message {
  getHasChildObjectiveBanks(): boolean;
  setHasChildObjectiveBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildObjectiveBanksReply): HasChildObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildObjectiveBanksReply;
  static deserializeBinaryFromReader(message: HasChildObjectiveBanksReply, reader: jspb.BinaryReader): HasChildObjectiveBanksReply;
}

export namespace HasChildObjectiveBanksReply {
  export type AsObject = {
    hasChildObjectiveBanks: boolean,
  }
}

export class HasChildObjectiveBanksRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildObjectiveBanksRequest): HasChildObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: HasChildObjectiveBanksRequest, reader: jspb.BinaryReader): HasChildObjectiveBanksRequest;
}

export namespace HasChildObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfObjectiveBankReply extends jspb.Message {
  getIsChildOfObjectiveBank(): boolean;
  setIsChildOfObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfObjectiveBankReply): IsChildOfObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfObjectiveBankReply;
  static deserializeBinaryFromReader(message: IsChildOfObjectiveBankReply, reader: jspb.BinaryReader): IsChildOfObjectiveBankReply;
}

export namespace IsChildOfObjectiveBankReply {
  export type AsObject = {
    isChildOfObjectiveBank: boolean,
  }
}

export class IsChildOfObjectiveBankRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfObjectiveBankRequest): IsChildOfObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfObjectiveBankRequest;
  static deserializeBinaryFromReader(message: IsChildOfObjectiveBankRequest, reader: jspb.BinaryReader): IsChildOfObjectiveBankRequest;
}

export namespace IsChildOfObjectiveBankRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildObjectiveBankIdsRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildObjectiveBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildObjectiveBankIdsRequest): GetChildObjectiveBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildObjectiveBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildObjectiveBankIdsRequest;
  static deserializeBinaryFromReader(message: GetChildObjectiveBankIdsRequest, reader: jspb.BinaryReader): GetChildObjectiveBankIdsRequest;
}

export namespace GetChildObjectiveBankIdsRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildObjectiveBanksRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildObjectiveBanksRequest): GetChildObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: GetChildObjectiveBanksRequest, reader: jspb.BinaryReader): GetChildObjectiveBanksRequest;
}

export namespace GetChildObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfObjectiveBankReply extends jspb.Message {
  getIsDescendantOfObjectiveBank(): boolean;
  setIsDescendantOfObjectiveBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfObjectiveBankReply): IsDescendantOfObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfObjectiveBankReply;
  static deserializeBinaryFromReader(message: IsDescendantOfObjectiveBankReply, reader: jspb.BinaryReader): IsDescendantOfObjectiveBankReply;
}

export namespace IsDescendantOfObjectiveBankReply {
  export type AsObject = {
    isDescendantOfObjectiveBank: boolean,
  }
}

export class IsDescendantOfObjectiveBankRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfObjectiveBankRequest): IsDescendantOfObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfObjectiveBankRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfObjectiveBankRequest, reader: jspb.BinaryReader): IsDescendantOfObjectiveBankRequest;
}

export namespace IsDescendantOfObjectiveBankRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBankNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankNodeIdsReply): GetObjectiveBankNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankNodeIdsReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankNodeIdsReply, reader: jspb.BinaryReader): GetObjectiveBankNodeIdsReply;
}

export namespace GetObjectiveBankNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetObjectiveBankNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankNodeIdsRequest): GetObjectiveBankNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankNodeIdsRequest, reader: jspb.BinaryReader): GetObjectiveBankNodeIdsRequest;
}

export namespace GetObjectiveBankNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetObjectiveBankNodesReply extends jspb.Message {
  hasObjectiveBankNode(): boolean;
  clearObjectiveBankNode(): void;
  getObjectiveBankNode(): ObjectiveBankNode | undefined;
  setObjectiveBankNode(value?: ObjectiveBankNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankNodesReply): GetObjectiveBankNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankNodesReply;
  static deserializeBinaryFromReader(message: GetObjectiveBankNodesReply, reader: jspb.BinaryReader): GetObjectiveBankNodesReply;
}

export namespace GetObjectiveBankNodesReply {
  export type AsObject = {
    objectiveBankNode?: ObjectiveBankNode.AsObject,
  }
}

export class GetObjectiveBankNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetObjectiveBankNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetObjectiveBankNodesRequest): GetObjectiveBankNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetObjectiveBankNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetObjectiveBankNodesRequest;
  static deserializeBinaryFromReader(message: GetObjectiveBankNodesRequest, reader: jspb.BinaryReader): GetObjectiveBankNodesRequest;
}

export namespace GetObjectiveBankNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanModifyObjectiveBankHierarchyReply extends jspb.Message {
  getCanModifyObjectiveBankHierarchy(): boolean;
  setCanModifyObjectiveBankHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyObjectiveBankHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyObjectiveBankHierarchyReply): CanModifyObjectiveBankHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyObjectiveBankHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyObjectiveBankHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyObjectiveBankHierarchyReply, reader: jspb.BinaryReader): CanModifyObjectiveBankHierarchyReply;
}

export namespace CanModifyObjectiveBankHierarchyReply {
  export type AsObject = {
    canModifyObjectiveBankHierarchy: boolean,
  }
}

export class CanModifyObjectiveBankHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyObjectiveBankHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyObjectiveBankHierarchyRequest): CanModifyObjectiveBankHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyObjectiveBankHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyObjectiveBankHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyObjectiveBankHierarchyRequest, reader: jspb.BinaryReader): CanModifyObjectiveBankHierarchyRequest;
}

export namespace CanModifyObjectiveBankHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootObjectiveBankReply): AddRootObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootObjectiveBankReply;
  static deserializeBinaryFromReader(message: AddRootObjectiveBankReply, reader: jspb.BinaryReader): AddRootObjectiveBankReply;
}

export namespace AddRootObjectiveBankReply {
  export type AsObject = {
  }
}

export class AddRootObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootObjectiveBankRequest): AddRootObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootObjectiveBankRequest;
  static deserializeBinaryFromReader(message: AddRootObjectiveBankRequest, reader: jspb.BinaryReader): AddRootObjectiveBankRequest;
}

export namespace AddRootObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootObjectiveBankReply): RemoveRootObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootObjectiveBankReply;
  static deserializeBinaryFromReader(message: RemoveRootObjectiveBankReply, reader: jspb.BinaryReader): RemoveRootObjectiveBankReply;
}

export namespace RemoveRootObjectiveBankReply {
  export type AsObject = {
  }
}

export class RemoveRootObjectiveBankRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootObjectiveBankRequest): RemoveRootObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootObjectiveBankRequest;
  static deserializeBinaryFromReader(message: RemoveRootObjectiveBankRequest, reader: jspb.BinaryReader): RemoveRootObjectiveBankRequest;
}

export namespace RemoveRootObjectiveBankRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildObjectiveBankReply): AddChildObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildObjectiveBankReply;
  static deserializeBinaryFromReader(message: AddChildObjectiveBankReply, reader: jspb.BinaryReader): AddChildObjectiveBankReply;
}

export namespace AddChildObjectiveBankReply {
  export type AsObject = {
  }
}

export class AddChildObjectiveBankRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildObjectiveBankRequest): AddChildObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildObjectiveBankRequest;
  static deserializeBinaryFromReader(message: AddChildObjectiveBankRequest, reader: jspb.BinaryReader): AddChildObjectiveBankRequest;
}

export namespace AddChildObjectiveBankRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildObjectiveBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectiveBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectiveBankReply): RemoveChildObjectiveBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectiveBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectiveBankReply;
  static deserializeBinaryFromReader(message: RemoveChildObjectiveBankReply, reader: jspb.BinaryReader): RemoveChildObjectiveBankReply;
}

export namespace RemoveChildObjectiveBankReply {
  export type AsObject = {
  }
}

export class RemoveChildObjectiveBankRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectiveBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectiveBankRequest): RemoveChildObjectiveBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectiveBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectiveBankRequest;
  static deserializeBinaryFromReader(message: RemoveChildObjectiveBankRequest, reader: jspb.BinaryReader): RemoveChildObjectiveBankRequest;
}

export namespace RemoveChildObjectiveBankRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildObjectiveBanksReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectiveBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectiveBanksReply): RemoveChildObjectiveBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectiveBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectiveBanksReply;
  static deserializeBinaryFromReader(message: RemoveChildObjectiveBanksReply, reader: jspb.BinaryReader): RemoveChildObjectiveBanksReply;
}

export namespace RemoveChildObjectiveBanksReply {
  export type AsObject = {
  }
}

export class RemoveChildObjectiveBanksRequest extends jspb.Message {
  hasObjectiveBankId(): boolean;
  clearObjectiveBankId(): void;
  getObjectiveBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildObjectiveBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildObjectiveBanksRequest): RemoveChildObjectiveBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildObjectiveBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildObjectiveBanksRequest;
  static deserializeBinaryFromReader(message: RemoveChildObjectiveBanksRequest, reader: jspb.BinaryReader): RemoveChildObjectiveBanksRequest;
}

export namespace RemoveChildObjectiveBanksRequest {
  export type AsObject = {
    objectiveBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

