// package: dlkit.proto.assessment
// file: dlkit/proto/assessment.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_calendaring_primitives_pb from "../../dlkit/primordium/calendaring/primitives_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_grading_pb from "../../dlkit/proto/grading_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Question extends jspb.Message {
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

  hasItem(): boolean;
  clearItem(): void;
  getItem(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItem(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Question.AsObject;
  static toObject(includeInstance: boolean, msg: Question): Question.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Question, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Question;
  static deserializeBinaryFromReader(message: Question, reader: jspb.BinaryReader): Question;
}

export namespace Question {
  export type AsObject = {
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    item?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class QuestionQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QuestionQuery.AsObject;
  static toObject(includeInstance: boolean, msg: QuestionQuery): QuestionQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QuestionQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QuestionQuery;
  static deserializeBinaryFromReader(message: QuestionQuery, reader: jspb.BinaryReader): QuestionQuery;
}

export namespace QuestionQuery {
  export type AsObject = {
  }
}

export class QuestionQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QuestionQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: QuestionQueryInspector): QuestionQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QuestionQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QuestionQueryInspector;
  static deserializeBinaryFromReader(message: QuestionQueryInspector, reader: jspb.BinaryReader): QuestionQueryInspector;
}

export namespace QuestionQueryInspector {
  export type AsObject = {
  }
}

export class QuestionForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QuestionForm.AsObject;
  static toObject(includeInstance: boolean, msg: QuestionForm): QuestionForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QuestionForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QuestionForm;
  static deserializeBinaryFromReader(message: QuestionForm, reader: jspb.BinaryReader): QuestionForm;
}

export namespace QuestionForm {
  export type AsObject = {
  }
}

export class QuestionSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QuestionSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: QuestionSearchOrder): QuestionSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QuestionSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QuestionSearchOrder;
  static deserializeBinaryFromReader(message: QuestionSearchOrder, reader: jspb.BinaryReader): QuestionSearchOrder;
}

export namespace QuestionSearchOrder {
  export type AsObject = {
  }
}

export class QuestionList extends jspb.Message {
  clearQuestionsList(): void;
  getQuestionsList(): Array<Question>;
  setQuestionsList(value: Array<Question>): void;
  addQuestions(value?: Question, index?: number): Question;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): QuestionList.AsObject;
  static toObject(includeInstance: boolean, msg: QuestionList): QuestionList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: QuestionList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): QuestionList;
  static deserializeBinaryFromReader(message: QuestionList, reader: jspb.BinaryReader): QuestionList;
}

export namespace QuestionList {
  export type AsObject = {
    questionsList: Array<Question.AsObject>,
  }
}

export class Answer extends jspb.Message {
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

  hasItem(): boolean;
  clearItem(): void;
  getItem(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItem(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Answer.AsObject;
  static toObject(includeInstance: boolean, msg: Answer): Answer.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Answer, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Answer;
  static deserializeBinaryFromReader(message: Answer, reader: jspb.BinaryReader): Answer;
}

export namespace Answer {
  export type AsObject = {
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    item?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class AnswerQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AnswerQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AnswerQuery): AnswerQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AnswerQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AnswerQuery;
  static deserializeBinaryFromReader(message: AnswerQuery, reader: jspb.BinaryReader): AnswerQuery;
}

export namespace AnswerQuery {
  export type AsObject = {
  }
}

export class AnswerQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AnswerQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AnswerQueryInspector): AnswerQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AnswerQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AnswerQueryInspector;
  static deserializeBinaryFromReader(message: AnswerQueryInspector, reader: jspb.BinaryReader): AnswerQueryInspector;
}

export namespace AnswerQueryInspector {
  export type AsObject = {
  }
}

export class AnswerForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AnswerForm.AsObject;
  static toObject(includeInstance: boolean, msg: AnswerForm): AnswerForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AnswerForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AnswerForm;
  static deserializeBinaryFromReader(message: AnswerForm, reader: jspb.BinaryReader): AnswerForm;
}

export namespace AnswerForm {
  export type AsObject = {
  }
}

export class AnswerSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AnswerSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AnswerSearchOrder): AnswerSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AnswerSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AnswerSearchOrder;
  static deserializeBinaryFromReader(message: AnswerSearchOrder, reader: jspb.BinaryReader): AnswerSearchOrder;
}

export namespace AnswerSearchOrder {
  export type AsObject = {
  }
}

export class AnswerList extends jspb.Message {
  clearAnswersList(): void;
  getAnswersList(): Array<Answer>;
  setAnswersList(value: Array<Answer>): void;
  addAnswers(value?: Answer, index?: number): Answer;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AnswerList.AsObject;
  static toObject(includeInstance: boolean, msg: AnswerList): AnswerList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AnswerList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AnswerList;
  static deserializeBinaryFromReader(message: AnswerList, reader: jspb.BinaryReader): AnswerList;
}

export namespace AnswerList {
  export type AsObject = {
    answersList: Array<Answer.AsObject>,
  }
}

export class Item extends jspb.Message {
  clearAnswersList(): void;
  getAnswersList(): Array<Answer>;
  setAnswersList(value: Array<Answer>): void;
  addAnswers(value?: Answer, index?: number): Answer;

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

  clearLearningObjectivesList(): void;
  getLearningObjectivesList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setLearningObjectivesList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addLearningObjectives(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Item.AsObject;
  static toObject(includeInstance: boolean, msg: Item): Item.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Item, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Item;
  static deserializeBinaryFromReader(message: Item, reader: jspb.BinaryReader): Item;
}

export namespace Item {
  export type AsObject = {
    answersList: Array<Answer.AsObject>,
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    learningObjectivesList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    question?: Question.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class ItemQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ItemQuery): ItemQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemQuery;
  static deserializeBinaryFromReader(message: ItemQuery, reader: jspb.BinaryReader): ItemQuery;
}

export namespace ItemQuery {
  export type AsObject = {
  }
}

export class ItemQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ItemQueryInspector): ItemQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemQueryInspector;
  static deserializeBinaryFromReader(message: ItemQueryInspector, reader: jspb.BinaryReader): ItemQueryInspector;
}

export namespace ItemQueryInspector {
  export type AsObject = {
  }
}

export class ItemForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemForm.AsObject;
  static toObject(includeInstance: boolean, msg: ItemForm): ItemForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemForm;
  static deserializeBinaryFromReader(message: ItemForm, reader: jspb.BinaryReader): ItemForm;
}

export namespace ItemForm {
  export type AsObject = {
  }
}

export class ItemSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ItemSearchOrder): ItemSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemSearchOrder;
  static deserializeBinaryFromReader(message: ItemSearchOrder, reader: jspb.BinaryReader): ItemSearchOrder;
}

export namespace ItemSearchOrder {
  export type AsObject = {
  }
}

export class ItemSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ItemSearch): ItemSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemSearch;
  static deserializeBinaryFromReader(message: ItemSearch, reader: jspb.BinaryReader): ItemSearch;
}

export namespace ItemSearch {
  export type AsObject = {
  }
}

export class ItemSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ItemSearchResults): ItemSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemSearchResults;
  static deserializeBinaryFromReader(message: ItemSearchResults, reader: jspb.BinaryReader): ItemSearchResults;
}

export namespace ItemSearchResults {
  export type AsObject = {
  }
}

export class ItemList extends jspb.Message {
  clearItemsList(): void;
  getItemsList(): Array<Item>;
  setItemsList(value: Array<Item>): void;
  addItems(value?: Item, index?: number): Item;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ItemList.AsObject;
  static toObject(includeInstance: boolean, msg: ItemList): ItemList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ItemList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ItemList;
  static deserializeBinaryFromReader(message: ItemList, reader: jspb.BinaryReader): ItemList;
}

export namespace ItemList {
  export type AsObject = {
    itemsList: Array<Item.AsObject>,
  }
}

export class Assessment extends jspb.Message {
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

  hasLevel(): boolean;
  clearLevel(): void;
  getLevel(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLevel(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasRubric(): boolean;
  clearRubric(): void;
  getRubric(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRubric(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Assessment.AsObject;
  static toObject(includeInstance: boolean, msg: Assessment): Assessment.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Assessment, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Assessment;
  static deserializeBinaryFromReader(message: Assessment, reader: jspb.BinaryReader): Assessment;
}

export namespace Assessment {
  export type AsObject = {
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    level?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    rubric?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssessmentQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentQuery): AssessmentQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentQuery;
  static deserializeBinaryFromReader(message: AssessmentQuery, reader: jspb.BinaryReader): AssessmentQuery;
}

export namespace AssessmentQuery {
  export type AsObject = {
  }
}

export class AssessmentQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentQueryInspector): AssessmentQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentQueryInspector;
  static deserializeBinaryFromReader(message: AssessmentQueryInspector, reader: jspb.BinaryReader): AssessmentQueryInspector;
}

export namespace AssessmentQueryInspector {
  export type AsObject = {
  }
}

export class AssessmentForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentForm.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentForm): AssessmentForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentForm;
  static deserializeBinaryFromReader(message: AssessmentForm, reader: jspb.BinaryReader): AssessmentForm;
}

export namespace AssessmentForm {
  export type AsObject = {
  }
}

export class AssessmentSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentSearchOrder): AssessmentSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentSearchOrder;
  static deserializeBinaryFromReader(message: AssessmentSearchOrder, reader: jspb.BinaryReader): AssessmentSearchOrder;
}

export namespace AssessmentSearchOrder {
  export type AsObject = {
  }
}

export class AssessmentSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentSearch): AssessmentSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentSearch;
  static deserializeBinaryFromReader(message: AssessmentSearch, reader: jspb.BinaryReader): AssessmentSearch;
}

export namespace AssessmentSearch {
  export type AsObject = {
  }
}

export class AssessmentSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentSearchResults): AssessmentSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentSearchResults;
  static deserializeBinaryFromReader(message: AssessmentSearchResults, reader: jspb.BinaryReader): AssessmentSearchResults;
}

export namespace AssessmentSearchResults {
  export type AsObject = {
  }
}

export class AssessmentList extends jspb.Message {
  clearAssessmentsList(): void;
  getAssessmentsList(): Array<Assessment>;
  setAssessmentsList(value: Array<Assessment>): void;
  addAssessments(value?: Assessment, index?: number): Assessment;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentList.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentList): AssessmentList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentList;
  static deserializeBinaryFromReader(message: AssessmentList, reader: jspb.BinaryReader): AssessmentList;
}

export namespace AssessmentList {
  export type AsObject = {
    assessmentsList: Array<Assessment.AsObject>,
  }
}

export class AssessmentOffered extends jspb.Message {
  hasAssessment(): boolean;
  clearAssessment(): void;
  getAssessment(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessment(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBank(): boolean;
  clearBank(): void;
  getBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasDeadline(): boolean;
  clearDeadline(): void;
  getDeadline(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setDeadline(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDuration(): boolean;
  clearDuration(): void;
  getDuration(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setDuration(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasGradeSystem(): boolean;
  clearGradeSystem(): void;
  getGradeSystem(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGradeSystem(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getItemsSequential(): boolean;
  setItemsSequential(value: boolean): void;

  getItemsShuffled(): boolean;
  setItemsShuffled(value: boolean): void;

  hasLevel(): boolean;
  clearLevel(): void;
  getLevel(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLevel(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasScoreSystem(): boolean;
  clearScoreSystem(): void;
  getScoreSystem(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setScoreSystem(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasStartTime(): boolean;
  clearStartTime(): void;
  getStartTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStartTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOffered.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOffered): AssessmentOffered.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOffered, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOffered;
  static deserializeBinaryFromReader(message: AssessmentOffered, reader: jspb.BinaryReader): AssessmentOffered;
}

export namespace AssessmentOffered {
  export type AsObject = {
    assessment?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    deadline?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    duration?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    gradeSystem?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemsSequential: boolean,
    itemsShuffled: boolean,
    level?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    scoreSystem?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    startTime?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class AssessmentOfferedQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedQuery): AssessmentOfferedQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedQuery;
  static deserializeBinaryFromReader(message: AssessmentOfferedQuery, reader: jspb.BinaryReader): AssessmentOfferedQuery;
}

export namespace AssessmentOfferedQuery {
  export type AsObject = {
  }
}

export class AssessmentOfferedQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedQueryInspector): AssessmentOfferedQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedQueryInspector;
  static deserializeBinaryFromReader(message: AssessmentOfferedQueryInspector, reader: jspb.BinaryReader): AssessmentOfferedQueryInspector;
}

export namespace AssessmentOfferedQueryInspector {
  export type AsObject = {
  }
}

export class AssessmentOfferedForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedForm.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedForm): AssessmentOfferedForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedForm;
  static deserializeBinaryFromReader(message: AssessmentOfferedForm, reader: jspb.BinaryReader): AssessmentOfferedForm;
}

export namespace AssessmentOfferedForm {
  export type AsObject = {
  }
}

export class AssessmentOfferedSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedSearchOrder): AssessmentOfferedSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedSearchOrder;
  static deserializeBinaryFromReader(message: AssessmentOfferedSearchOrder, reader: jspb.BinaryReader): AssessmentOfferedSearchOrder;
}

export namespace AssessmentOfferedSearchOrder {
  export type AsObject = {
  }
}

export class AssessmentOfferedSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedSearch): AssessmentOfferedSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedSearch;
  static deserializeBinaryFromReader(message: AssessmentOfferedSearch, reader: jspb.BinaryReader): AssessmentOfferedSearch;
}

export namespace AssessmentOfferedSearch {
  export type AsObject = {
  }
}

export class AssessmentOfferedSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedSearchResults): AssessmentOfferedSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedSearchResults;
  static deserializeBinaryFromReader(message: AssessmentOfferedSearchResults, reader: jspb.BinaryReader): AssessmentOfferedSearchResults;
}

export namespace AssessmentOfferedSearchResults {
  export type AsObject = {
  }
}

export class AssessmentOfferedList extends jspb.Message {
  clearAssessmentsOfferedList(): void;
  getAssessmentsOfferedList(): Array<AssessmentOffered>;
  setAssessmentsOfferedList(value: Array<AssessmentOffered>): void;
  addAssessmentsOffered(value?: AssessmentOffered, index?: number): AssessmentOffered;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentOfferedList.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentOfferedList): AssessmentOfferedList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentOfferedList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentOfferedList;
  static deserializeBinaryFromReader(message: AssessmentOfferedList, reader: jspb.BinaryReader): AssessmentOfferedList;
}

export namespace AssessmentOfferedList {
  export type AsObject = {
    assessmentsOfferedList: Array<AssessmentOffered.AsObject>,
  }
}

export class AssessmentTaken extends jspb.Message {
  hasActualStartTime(): boolean;
  clearActualStartTime(): void;
  getActualStartTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setActualStartTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasAssessmentOffered(): boolean;
  clearAssessmentOffered(): void;
  getAssessmentOffered(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOffered(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBank(): boolean;
  clearBank(): void;
  getBank(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBank(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasCompletionTime(): boolean;
  clearCompletionTime(): void;
  getCompletionTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCompletionTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

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

  hasGrade(): boolean;
  clearGrade(): void;
  getGrade(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setGrade(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  getScore(): number;
  setScore(value: number): void;

  hasTaker(): boolean;
  clearTaker(): void;
  getTaker(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setTaker(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTaken.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTaken): AssessmentTaken.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTaken, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTaken;
  static deserializeBinaryFromReader(message: AssessmentTaken, reader: jspb.BinaryReader): AssessmentTaken;
}

export namespace AssessmentTaken {
  export type AsObject = {
    actualStartTime?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    assessmentOffered?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bank?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    completionTime?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    grade?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    score: number,
    taker?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssessmentTakenQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenQuery): AssessmentTakenQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenQuery;
  static deserializeBinaryFromReader(message: AssessmentTakenQuery, reader: jspb.BinaryReader): AssessmentTakenQuery;
}

export namespace AssessmentTakenQuery {
  export type AsObject = {
  }
}

export class AssessmentTakenQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenQueryInspector): AssessmentTakenQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenQueryInspector;
  static deserializeBinaryFromReader(message: AssessmentTakenQueryInspector, reader: jspb.BinaryReader): AssessmentTakenQueryInspector;
}

export namespace AssessmentTakenQueryInspector {
  export type AsObject = {
  }
}

export class AssessmentTakenForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenForm.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenForm): AssessmentTakenForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenForm;
  static deserializeBinaryFromReader(message: AssessmentTakenForm, reader: jspb.BinaryReader): AssessmentTakenForm;
}

export namespace AssessmentTakenForm {
  export type AsObject = {
  }
}

export class AssessmentTakenSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenSearchOrder): AssessmentTakenSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenSearchOrder;
  static deserializeBinaryFromReader(message: AssessmentTakenSearchOrder, reader: jspb.BinaryReader): AssessmentTakenSearchOrder;
}

export namespace AssessmentTakenSearchOrder {
  export type AsObject = {
  }
}

export class AssessmentTakenSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenSearch): AssessmentTakenSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenSearch;
  static deserializeBinaryFromReader(message: AssessmentTakenSearch, reader: jspb.BinaryReader): AssessmentTakenSearch;
}

export namespace AssessmentTakenSearch {
  export type AsObject = {
  }
}

export class AssessmentTakenSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenSearchResults): AssessmentTakenSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenSearchResults;
  static deserializeBinaryFromReader(message: AssessmentTakenSearchResults, reader: jspb.BinaryReader): AssessmentTakenSearchResults;
}

export namespace AssessmentTakenSearchResults {
  export type AsObject = {
  }
}

export class AssessmentTakenList extends jspb.Message {
  clearAssessmentsTakenList(): void;
  getAssessmentsTakenList(): Array<AssessmentTaken>;
  setAssessmentsTakenList(value: Array<AssessmentTaken>): void;
  addAssessmentsTaken(value?: AssessmentTaken, index?: number): AssessmentTaken;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentTakenList.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentTakenList): AssessmentTakenList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentTakenList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentTakenList;
  static deserializeBinaryFromReader(message: AssessmentTakenList, reader: jspb.BinaryReader): AssessmentTakenList;
}

export namespace AssessmentTakenList {
  export type AsObject = {
    assessmentsTakenList: Array<AssessmentTaken.AsObject>,
  }
}

export class AssessmentSection extends jspb.Message {
  hasAssessmentTaken(): boolean;
  clearAssessmentTaken(): void;
  getAssessmentTaken(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTaken(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
  toObject(includeInstance?: boolean): AssessmentSection.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentSection): AssessmentSection.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentSection, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentSection;
  static deserializeBinaryFromReader(message: AssessmentSection, reader: jspb.BinaryReader): AssessmentSection;
}

export namespace AssessmentSection {
  export type AsObject = {
    assessmentTaken?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class AssessmentSectionList extends jspb.Message {
  clearAssessmentSectionsList(): void;
  getAssessmentSectionsList(): Array<AssessmentSection>;
  setAssessmentSectionsList(value: Array<AssessmentSection>): void;
  addAssessmentSections(value?: AssessmentSection, index?: number): AssessmentSection;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssessmentSectionList.AsObject;
  static toObject(includeInstance: boolean, msg: AssessmentSectionList): AssessmentSectionList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssessmentSectionList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssessmentSectionList;
  static deserializeBinaryFromReader(message: AssessmentSectionList, reader: jspb.BinaryReader): AssessmentSectionList;
}

export namespace AssessmentSectionList {
  export type AsObject = {
    assessmentSectionsList: Array<AssessmentSection.AsObject>,
  }
}

export class Bank extends jspb.Message {
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
  toObject(includeInstance?: boolean): Bank.AsObject;
  static toObject(includeInstance: boolean, msg: Bank): Bank.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Bank, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Bank;
  static deserializeBinaryFromReader(message: Bank, reader: jspb.BinaryReader): Bank;
}

export namespace Bank {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class BankQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankQuery.AsObject;
  static toObject(includeInstance: boolean, msg: BankQuery): BankQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankQuery;
  static deserializeBinaryFromReader(message: BankQuery, reader: jspb.BinaryReader): BankQuery;
}

export namespace BankQuery {
  export type AsObject = {
  }
}

export class BankQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: BankQueryInspector): BankQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankQueryInspector;
  static deserializeBinaryFromReader(message: BankQueryInspector, reader: jspb.BinaryReader): BankQueryInspector;
}

export namespace BankQueryInspector {
  export type AsObject = {
  }
}

export class BankForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankForm.AsObject;
  static toObject(includeInstance: boolean, msg: BankForm): BankForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankForm;
  static deserializeBinaryFromReader(message: BankForm, reader: jspb.BinaryReader): BankForm;
}

export namespace BankForm {
  export type AsObject = {
  }
}

export class BankSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: BankSearchOrder): BankSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankSearchOrder;
  static deserializeBinaryFromReader(message: BankSearchOrder, reader: jspb.BinaryReader): BankSearchOrder;
}

export namespace BankSearchOrder {
  export type AsObject = {
  }
}

export class BankSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankSearch.AsObject;
  static toObject(includeInstance: boolean, msg: BankSearch): BankSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankSearch;
  static deserializeBinaryFromReader(message: BankSearch, reader: jspb.BinaryReader): BankSearch;
}

export namespace BankSearch {
  export type AsObject = {
  }
}

export class BankSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: BankSearchResults): BankSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankSearchResults;
  static deserializeBinaryFromReader(message: BankSearchResults, reader: jspb.BinaryReader): BankSearchResults;
}

export namespace BankSearchResults {
  export type AsObject = {
  }
}

export class BankList extends jspb.Message {
  clearBanksList(): void;
  getBanksList(): Array<Bank>;
  setBanksList(value: Array<Bank>): void;
  addBanks(value?: Bank, index?: number): Bank;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankList.AsObject;
  static toObject(includeInstance: boolean, msg: BankList): BankList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankList;
  static deserializeBinaryFromReader(message: BankList, reader: jspb.BinaryReader): BankList;
}

export namespace BankList {
  export type AsObject = {
    banksList: Array<Bank.AsObject>,
  }
}

export class BankNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankNode.AsObject;
  static toObject(includeInstance: boolean, msg: BankNode): BankNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankNode;
  static deserializeBinaryFromReader(message: BankNode, reader: jspb.BinaryReader): BankNode;
}

export namespace BankNode {
  export type AsObject = {
  }
}

export class BankNodeList extends jspb.Message {
  clearBankNodesList(): void;
  getBankNodesList(): Array<BankNode>;
  setBankNodesList(value: Array<BankNode>): void;
  addBankNodes(value?: BankNode, index?: number): BankNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BankNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: BankNodeList): BankNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BankNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BankNodeList;
  static deserializeBinaryFromReader(message: BankNodeList, reader: jspb.BinaryReader): BankNodeList;
}

export namespace BankNodeList {
  export type AsObject = {
    bankNodesList: Array<BankNode.AsObject>,
  }
}

export class Response extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Response.AsObject;
  static toObject(includeInstance: boolean, msg: Response): Response.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Response, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Response;
  static deserializeBinaryFromReader(message: Response, reader: jspb.BinaryReader): Response;
}

export namespace Response {
  export type AsObject = {
  }
}

export class ResponseList extends jspb.Message {
  clearResponsesList(): void;
  getResponsesList(): Array<Response>;
  setResponsesList(value: Array<Response>): void;
  addResponses(value?: Response, index?: number): Response;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResponseList.AsObject;
  static toObject(includeInstance: boolean, msg: ResponseList): ResponseList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResponseList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResponseList;
  static deserializeBinaryFromReader(message: ResponseList, reader: jspb.BinaryReader): ResponseList;
}

export namespace ResponseList {
  export type AsObject = {
    responsesList: Array<Response.AsObject>,
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
  getBank(): Bank | undefined;
  setBank(value?: Bank): void;

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
    bank?: Bank.AsObject,
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

export class CanTakeAssessmentsReply extends jspb.Message {
  getCanTakeAssessments(): boolean;
  setCanTakeAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanTakeAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanTakeAssessmentsReply): CanTakeAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanTakeAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanTakeAssessmentsReply;
  static deserializeBinaryFromReader(message: CanTakeAssessmentsReply, reader: jspb.BinaryReader): CanTakeAssessmentsReply;
}

export namespace CanTakeAssessmentsReply {
  export type AsObject = {
    canTakeAssessments: boolean,
  }
}

export class CanTakeAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanTakeAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanTakeAssessmentsRequest): CanTakeAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanTakeAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanTakeAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanTakeAssessmentsRequest, reader: jspb.BinaryReader): CanTakeAssessmentsRequest;
}

export namespace CanTakeAssessmentsRequest {
  export type AsObject = {
  }
}

export class HasAssessmentBegunReply extends jspb.Message {
  getHasAssessmentBegun(): boolean;
  setHasAssessmentBegun(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasAssessmentBegunReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasAssessmentBegunReply): HasAssessmentBegunReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasAssessmentBegunReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasAssessmentBegunReply;
  static deserializeBinaryFromReader(message: HasAssessmentBegunReply, reader: jspb.BinaryReader): HasAssessmentBegunReply;
}

export namespace HasAssessmentBegunReply {
  export type AsObject = {
    hasAssessmentBegun: boolean,
  }
}

export class HasAssessmentBegunRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasAssessmentBegunRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasAssessmentBegunRequest): HasAssessmentBegunRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasAssessmentBegunRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasAssessmentBegunRequest;
  static deserializeBinaryFromReader(message: HasAssessmentBegunRequest, reader: jspb.BinaryReader): HasAssessmentBegunRequest;
}

export namespace HasAssessmentBegunRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAssessmentOverReply extends jspb.Message {
  getIsAssessmentOver(): boolean;
  setIsAssessmentOver(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAssessmentOverReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAssessmentOverReply): IsAssessmentOverReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAssessmentOverReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAssessmentOverReply;
  static deserializeBinaryFromReader(message: IsAssessmentOverReply, reader: jspb.BinaryReader): IsAssessmentOverReply;
}

export namespace IsAssessmentOverReply {
  export type AsObject = {
    isAssessmentOver: boolean,
  }
}

export class IsAssessmentOverRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAssessmentOverRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAssessmentOverRequest): IsAssessmentOverRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAssessmentOverRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAssessmentOverRequest;
  static deserializeBinaryFromReader(message: IsAssessmentOverRequest, reader: jspb.BinaryReader): IsAssessmentOverRequest;
}

export namespace IsAssessmentOverRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RequiresSynchronousSectionsReply extends jspb.Message {
  getRequiresSynchronousSections(): boolean;
  setRequiresSynchronousSections(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RequiresSynchronousSectionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RequiresSynchronousSectionsReply): RequiresSynchronousSectionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RequiresSynchronousSectionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RequiresSynchronousSectionsReply;
  static deserializeBinaryFromReader(message: RequiresSynchronousSectionsReply, reader: jspb.BinaryReader): RequiresSynchronousSectionsReply;
}

export namespace RequiresSynchronousSectionsReply {
  export type AsObject = {
    requiresSynchronousSections: boolean,
  }
}

export class RequiresSynchronousSectionsRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RequiresSynchronousSectionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RequiresSynchronousSectionsRequest): RequiresSynchronousSectionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RequiresSynchronousSectionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RequiresSynchronousSectionsRequest;
  static deserializeBinaryFromReader(message: RequiresSynchronousSectionsRequest, reader: jspb.BinaryReader): RequiresSynchronousSectionsRequest;
}

export namespace RequiresSynchronousSectionsRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFirstAssessmentSectionReply extends jspb.Message {
  hasAssessmentSection(): boolean;
  clearAssessmentSection(): void;
  getAssessmentSection(): AssessmentSection | undefined;
  setAssessmentSection(value?: AssessmentSection): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFirstAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFirstAssessmentSectionReply): GetFirstAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFirstAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFirstAssessmentSectionReply;
  static deserializeBinaryFromReader(message: GetFirstAssessmentSectionReply, reader: jspb.BinaryReader): GetFirstAssessmentSectionReply;
}

export namespace GetFirstAssessmentSectionReply {
  export type AsObject = {
    assessmentSection?: AssessmentSection.AsObject,
  }
}

export class GetFirstAssessmentSectionRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFirstAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFirstAssessmentSectionRequest): GetFirstAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFirstAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFirstAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: GetFirstAssessmentSectionRequest, reader: jspb.BinaryReader): GetFirstAssessmentSectionRequest;
}

export namespace GetFirstAssessmentSectionRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasNextAssessmentSectionReply extends jspb.Message {
  getHasNextAssessmentSection(): boolean;
  setHasNextAssessmentSection(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasNextAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasNextAssessmentSectionReply): HasNextAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasNextAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasNextAssessmentSectionReply;
  static deserializeBinaryFromReader(message: HasNextAssessmentSectionReply, reader: jspb.BinaryReader): HasNextAssessmentSectionReply;
}

export namespace HasNextAssessmentSectionReply {
  export type AsObject = {
    hasNextAssessmentSection: boolean,
  }
}

export class HasNextAssessmentSectionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasNextAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasNextAssessmentSectionRequest): HasNextAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasNextAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasNextAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: HasNextAssessmentSectionRequest, reader: jspb.BinaryReader): HasNextAssessmentSectionRequest;
}

export namespace HasNextAssessmentSectionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetNextAssessmentSectionReply extends jspb.Message {
  hasAssessmentSection(): boolean;
  clearAssessmentSection(): void;
  getAssessmentSection(): AssessmentSection | undefined;
  setAssessmentSection(value?: AssessmentSection): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNextAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetNextAssessmentSectionReply): GetNextAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNextAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNextAssessmentSectionReply;
  static deserializeBinaryFromReader(message: GetNextAssessmentSectionReply, reader: jspb.BinaryReader): GetNextAssessmentSectionReply;
}

export namespace GetNextAssessmentSectionReply {
  export type AsObject = {
    assessmentSection?: AssessmentSection.AsObject,
  }
}

export class GetNextAssessmentSectionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNextAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetNextAssessmentSectionRequest): GetNextAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNextAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNextAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: GetNextAssessmentSectionRequest, reader: jspb.BinaryReader): GetNextAssessmentSectionRequest;
}

export namespace GetNextAssessmentSectionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasPreviousAssessmentSectionReply extends jspb.Message {
  getHasPreviousAssessmentSection(): boolean;
  setHasPreviousAssessmentSection(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasPreviousAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasPreviousAssessmentSectionReply): HasPreviousAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasPreviousAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasPreviousAssessmentSectionReply;
  static deserializeBinaryFromReader(message: HasPreviousAssessmentSectionReply, reader: jspb.BinaryReader): HasPreviousAssessmentSectionReply;
}

export namespace HasPreviousAssessmentSectionReply {
  export type AsObject = {
    hasPreviousAssessmentSection: boolean,
  }
}

export class HasPreviousAssessmentSectionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasPreviousAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasPreviousAssessmentSectionRequest): HasPreviousAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasPreviousAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasPreviousAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: HasPreviousAssessmentSectionRequest, reader: jspb.BinaryReader): HasPreviousAssessmentSectionRequest;
}

export namespace HasPreviousAssessmentSectionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetPreviousAssessmentSectionReply extends jspb.Message {
  hasAssessmentSection(): boolean;
  clearAssessmentSection(): void;
  getAssessmentSection(): AssessmentSection | undefined;
  setAssessmentSection(value?: AssessmentSection): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetPreviousAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetPreviousAssessmentSectionReply): GetPreviousAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetPreviousAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetPreviousAssessmentSectionReply;
  static deserializeBinaryFromReader(message: GetPreviousAssessmentSectionReply, reader: jspb.BinaryReader): GetPreviousAssessmentSectionReply;
}

export namespace GetPreviousAssessmentSectionReply {
  export type AsObject = {
    assessmentSection?: AssessmentSection.AsObject,
  }
}

export class GetPreviousAssessmentSectionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetPreviousAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetPreviousAssessmentSectionRequest): GetPreviousAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetPreviousAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetPreviousAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: GetPreviousAssessmentSectionRequest, reader: jspb.BinaryReader): GetPreviousAssessmentSectionRequest;
}

export namespace GetPreviousAssessmentSectionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentSectionReply extends jspb.Message {
  hasAssessmentSection(): boolean;
  clearAssessmentSection(): void;
  getAssessmentSection(): AssessmentSection | undefined;
  setAssessmentSection(value?: AssessmentSection): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentSectionReply): GetAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentSectionReply;
  static deserializeBinaryFromReader(message: GetAssessmentSectionReply, reader: jspb.BinaryReader): GetAssessmentSectionReply;
}

export namespace GetAssessmentSectionReply {
  export type AsObject = {
    assessmentSection?: AssessmentSection.AsObject,
  }
}

export class GetAssessmentSectionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentSectionRequest): GetAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: GetAssessmentSectionRequest, reader: jspb.BinaryReader): GetAssessmentSectionRequest;
}

export namespace GetAssessmentSectionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentSectionsRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentSectionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentSectionsRequest): GetAssessmentSectionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentSectionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentSectionsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentSectionsRequest, reader: jspb.BinaryReader): GetAssessmentSectionsRequest;
}

export namespace GetAssessmentSectionsRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAssessmentSectionCompleteReply extends jspb.Message {
  getIsAssessmentSectionComplete(): boolean;
  setIsAssessmentSectionComplete(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAssessmentSectionCompleteReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAssessmentSectionCompleteReply): IsAssessmentSectionCompleteReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAssessmentSectionCompleteReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAssessmentSectionCompleteReply;
  static deserializeBinaryFromReader(message: IsAssessmentSectionCompleteReply, reader: jspb.BinaryReader): IsAssessmentSectionCompleteReply;
}

export namespace IsAssessmentSectionCompleteReply {
  export type AsObject = {
    isAssessmentSectionComplete: boolean,
  }
}

export class IsAssessmentSectionCompleteRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAssessmentSectionCompleteRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAssessmentSectionCompleteRequest): IsAssessmentSectionCompleteRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAssessmentSectionCompleteRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAssessmentSectionCompleteRequest;
  static deserializeBinaryFromReader(message: IsAssessmentSectionCompleteRequest, reader: jspb.BinaryReader): IsAssessmentSectionCompleteRequest;
}

export namespace IsAssessmentSectionCompleteRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetIncompleteAssessmentSectionsRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetIncompleteAssessmentSectionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetIncompleteAssessmentSectionsRequest): GetIncompleteAssessmentSectionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetIncompleteAssessmentSectionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetIncompleteAssessmentSectionsRequest;
  static deserializeBinaryFromReader(message: GetIncompleteAssessmentSectionsRequest, reader: jspb.BinaryReader): GetIncompleteAssessmentSectionsRequest;
}

export namespace GetIncompleteAssessmentSectionsRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasAssessmentSectionBegunReply extends jspb.Message {
  getHasAssessmentSectionBegun(): boolean;
  setHasAssessmentSectionBegun(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasAssessmentSectionBegunReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasAssessmentSectionBegunReply): HasAssessmentSectionBegunReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasAssessmentSectionBegunReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasAssessmentSectionBegunReply;
  static deserializeBinaryFromReader(message: HasAssessmentSectionBegunReply, reader: jspb.BinaryReader): HasAssessmentSectionBegunReply;
}

export namespace HasAssessmentSectionBegunReply {
  export type AsObject = {
    hasAssessmentSectionBegun: boolean,
  }
}

export class HasAssessmentSectionBegunRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasAssessmentSectionBegunRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasAssessmentSectionBegunRequest): HasAssessmentSectionBegunRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasAssessmentSectionBegunRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasAssessmentSectionBegunRequest;
  static deserializeBinaryFromReader(message: HasAssessmentSectionBegunRequest, reader: jspb.BinaryReader): HasAssessmentSectionBegunRequest;
}

export namespace HasAssessmentSectionBegunRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAssessmentSectionOverReply extends jspb.Message {
  getIsAssessmentSectionOver(): boolean;
  setIsAssessmentSectionOver(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAssessmentSectionOverReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAssessmentSectionOverReply): IsAssessmentSectionOverReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAssessmentSectionOverReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAssessmentSectionOverReply;
  static deserializeBinaryFromReader(message: IsAssessmentSectionOverReply, reader: jspb.BinaryReader): IsAssessmentSectionOverReply;
}

export namespace IsAssessmentSectionOverReply {
  export type AsObject = {
    isAssessmentSectionOver: boolean,
  }
}

export class IsAssessmentSectionOverRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAssessmentSectionOverRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAssessmentSectionOverRequest): IsAssessmentSectionOverRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAssessmentSectionOverRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAssessmentSectionOverRequest;
  static deserializeBinaryFromReader(message: IsAssessmentSectionOverRequest, reader: jspb.BinaryReader): IsAssessmentSectionOverRequest;
}

export namespace IsAssessmentSectionOverRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RequiresSynchronousResponsesReply extends jspb.Message {
  getRequiresSynchronousResponses(): boolean;
  setRequiresSynchronousResponses(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RequiresSynchronousResponsesReply.AsObject;
  static toObject(includeInstance: boolean, msg: RequiresSynchronousResponsesReply): RequiresSynchronousResponsesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RequiresSynchronousResponsesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RequiresSynchronousResponsesReply;
  static deserializeBinaryFromReader(message: RequiresSynchronousResponsesReply, reader: jspb.BinaryReader): RequiresSynchronousResponsesReply;
}

export namespace RequiresSynchronousResponsesReply {
  export type AsObject = {
    requiresSynchronousResponses: boolean,
  }
}

export class RequiresSynchronousResponsesRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RequiresSynchronousResponsesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RequiresSynchronousResponsesRequest): RequiresSynchronousResponsesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RequiresSynchronousResponsesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RequiresSynchronousResponsesRequest;
  static deserializeBinaryFromReader(message: RequiresSynchronousResponsesRequest, reader: jspb.BinaryReader): RequiresSynchronousResponsesRequest;
}

export namespace RequiresSynchronousResponsesRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFirstQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFirstQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFirstQuestionReply): GetFirstQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFirstQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFirstQuestionReply;
  static deserializeBinaryFromReader(message: GetFirstQuestionReply, reader: jspb.BinaryReader): GetFirstQuestionReply;
}

export namespace GetFirstQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetFirstQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFirstQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFirstQuestionRequest): GetFirstQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFirstQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFirstQuestionRequest;
  static deserializeBinaryFromReader(message: GetFirstQuestionRequest, reader: jspb.BinaryReader): GetFirstQuestionRequest;
}

export namespace GetFirstQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasNextQuestionReply extends jspb.Message {
  getHasNextQuestion(): boolean;
  setHasNextQuestion(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasNextQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasNextQuestionReply): HasNextQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasNextQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasNextQuestionReply;
  static deserializeBinaryFromReader(message: HasNextQuestionReply, reader: jspb.BinaryReader): HasNextQuestionReply;
}

export namespace HasNextQuestionReply {
  export type AsObject = {
    hasNextQuestion: boolean,
  }
}

export class HasNextQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasNextQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasNextQuestionRequest): HasNextQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasNextQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasNextQuestionRequest;
  static deserializeBinaryFromReader(message: HasNextQuestionRequest, reader: jspb.BinaryReader): HasNextQuestionRequest;
}

export namespace HasNextQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetNextQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNextQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetNextQuestionReply): GetNextQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNextQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNextQuestionReply;
  static deserializeBinaryFromReader(message: GetNextQuestionReply, reader: jspb.BinaryReader): GetNextQuestionReply;
}

export namespace GetNextQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetNextQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNextQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetNextQuestionRequest): GetNextQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNextQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNextQuestionRequest;
  static deserializeBinaryFromReader(message: GetNextQuestionRequest, reader: jspb.BinaryReader): GetNextQuestionRequest;
}

export namespace GetNextQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasPreviousQuestionReply extends jspb.Message {
  getHasPreviousQuestion(): boolean;
  setHasPreviousQuestion(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasPreviousQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasPreviousQuestionReply): HasPreviousQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasPreviousQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasPreviousQuestionReply;
  static deserializeBinaryFromReader(message: HasPreviousQuestionReply, reader: jspb.BinaryReader): HasPreviousQuestionReply;
}

export namespace HasPreviousQuestionReply {
  export type AsObject = {
    hasPreviousQuestion: boolean,
  }
}

export class HasPreviousQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasPreviousQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasPreviousQuestionRequest): HasPreviousQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasPreviousQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasPreviousQuestionRequest;
  static deserializeBinaryFromReader(message: HasPreviousQuestionRequest, reader: jspb.BinaryReader): HasPreviousQuestionRequest;
}

export namespace HasPreviousQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetPreviousQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetPreviousQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetPreviousQuestionReply): GetPreviousQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetPreviousQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetPreviousQuestionReply;
  static deserializeBinaryFromReader(message: GetPreviousQuestionReply, reader: jspb.BinaryReader): GetPreviousQuestionReply;
}

export namespace GetPreviousQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetPreviousQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetPreviousQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetPreviousQuestionRequest): GetPreviousQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetPreviousQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetPreviousQuestionRequest;
  static deserializeBinaryFromReader(message: GetPreviousQuestionRequest, reader: jspb.BinaryReader): GetPreviousQuestionRequest;
}

export namespace GetPreviousQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionReply): GetQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionReply;
  static deserializeBinaryFromReader(message: GetQuestionReply, reader: jspb.BinaryReader): GetQuestionReply;
}

export namespace GetQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionRequest): GetQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionRequest;
  static deserializeBinaryFromReader(message: GetQuestionRequest, reader: jspb.BinaryReader): GetQuestionRequest;
}

export namespace GetQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetQuestionsRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionsRequest): GetQuestionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionsRequest;
  static deserializeBinaryFromReader(message: GetQuestionsRequest, reader: jspb.BinaryReader): GetQuestionsRequest;
}

export namespace GetQuestionsRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResponseFormReply extends jspb.Message {
  hasAnswerForm(): boolean;
  clearAnswerForm(): void;
  getAnswerForm(): AnswerForm | undefined;
  setAnswerForm(value?: AnswerForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResponseFormReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResponseFormReply): GetResponseFormReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResponseFormReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResponseFormReply;
  static deserializeBinaryFromReader(message: GetResponseFormReply, reader: jspb.BinaryReader): GetResponseFormReply;
}

export namespace GetResponseFormReply {
  export type AsObject = {
    answerForm?: AnswerForm.AsObject,
  }
}

export class GetResponseFormRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResponseFormRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResponseFormRequest): GetResponseFormRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResponseFormRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResponseFormRequest;
  static deserializeBinaryFromReader(message: GetResponseFormRequest, reader: jspb.BinaryReader): GetResponseFormRequest;
}

export namespace GetResponseFormRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class SubmitResponseReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubmitResponseReply.AsObject;
  static toObject(includeInstance: boolean, msg: SubmitResponseReply): SubmitResponseReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubmitResponseReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubmitResponseReply;
  static deserializeBinaryFromReader(message: SubmitResponseReply, reader: jspb.BinaryReader): SubmitResponseReply;
}

export namespace SubmitResponseReply {
  export type AsObject = {
  }
}

export class SubmitResponseRequest extends jspb.Message {
  hasAnswerForm(): boolean;
  clearAnswerForm(): void;
  getAnswerForm(): AnswerForm | undefined;
  setAnswerForm(value?: AnswerForm): void;

  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubmitResponseRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SubmitResponseRequest): SubmitResponseRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubmitResponseRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubmitResponseRequest;
  static deserializeBinaryFromReader(message: SubmitResponseRequest, reader: jspb.BinaryReader): SubmitResponseRequest;
}

export namespace SubmitResponseRequest {
  export type AsObject = {
    answerForm?: AnswerForm.AsObject,
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class SkipItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SkipItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: SkipItemReply): SkipItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SkipItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SkipItemReply;
  static deserializeBinaryFromReader(message: SkipItemReply, reader: jspb.BinaryReader): SkipItemReply;
}

export namespace SkipItemReply {
  export type AsObject = {
  }
}

export class SkipItemRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SkipItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SkipItemRequest): SkipItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SkipItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SkipItemRequest;
  static deserializeBinaryFromReader(message: SkipItemRequest, reader: jspb.BinaryReader): SkipItemRequest;
}

export namespace SkipItemRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsQuestionAnsweredReply extends jspb.Message {
  getIsQuestionAnswered(): boolean;
  setIsQuestionAnswered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsQuestionAnsweredReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsQuestionAnsweredReply): IsQuestionAnsweredReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsQuestionAnsweredReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsQuestionAnsweredReply;
  static deserializeBinaryFromReader(message: IsQuestionAnsweredReply, reader: jspb.BinaryReader): IsQuestionAnsweredReply;
}

export namespace IsQuestionAnsweredReply {
  export type AsObject = {
    isQuestionAnswered: boolean,
  }
}

export class IsQuestionAnsweredRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsQuestionAnsweredRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsQuestionAnsweredRequest): IsQuestionAnsweredRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsQuestionAnsweredRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsQuestionAnsweredRequest;
  static deserializeBinaryFromReader(message: IsQuestionAnsweredRequest, reader: jspb.BinaryReader): IsQuestionAnsweredRequest;
}

export namespace IsQuestionAnsweredRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetUnansweredQuestionsRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUnansweredQuestionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetUnansweredQuestionsRequest): GetUnansweredQuestionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUnansweredQuestionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUnansweredQuestionsRequest;
  static deserializeBinaryFromReader(message: GetUnansweredQuestionsRequest, reader: jspb.BinaryReader): GetUnansweredQuestionsRequest;
}

export namespace GetUnansweredQuestionsRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasUnansweredQuestionsReply extends jspb.Message {
  getHasUnansweredQuestions(): boolean;
  setHasUnansweredQuestions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasUnansweredQuestionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasUnansweredQuestionsReply): HasUnansweredQuestionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasUnansweredQuestionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasUnansweredQuestionsReply;
  static deserializeBinaryFromReader(message: HasUnansweredQuestionsReply, reader: jspb.BinaryReader): HasUnansweredQuestionsReply;
}

export namespace HasUnansweredQuestionsReply {
  export type AsObject = {
    hasUnansweredQuestions: boolean,
  }
}

export class HasUnansweredQuestionsRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasUnansweredQuestionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasUnansweredQuestionsRequest): HasUnansweredQuestionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasUnansweredQuestionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasUnansweredQuestionsRequest;
  static deserializeBinaryFromReader(message: HasUnansweredQuestionsRequest, reader: jspb.BinaryReader): HasUnansweredQuestionsRequest;
}

export namespace HasUnansweredQuestionsRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetFirstUnansweredQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFirstUnansweredQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetFirstUnansweredQuestionReply): GetFirstUnansweredQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFirstUnansweredQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFirstUnansweredQuestionReply;
  static deserializeBinaryFromReader(message: GetFirstUnansweredQuestionReply, reader: jspb.BinaryReader): GetFirstUnansweredQuestionReply;
}

export namespace GetFirstUnansweredQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetFirstUnansweredQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFirstUnansweredQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFirstUnansweredQuestionRequest): GetFirstUnansweredQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFirstUnansweredQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFirstUnansweredQuestionRequest;
  static deserializeBinaryFromReader(message: GetFirstUnansweredQuestionRequest, reader: jspb.BinaryReader): GetFirstUnansweredQuestionRequest;
}

export namespace GetFirstUnansweredQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasNextUnansweredQuestionReply extends jspb.Message {
  getHasNextUnansweredQuestion(): boolean;
  setHasNextUnansweredQuestion(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasNextUnansweredQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasNextUnansweredQuestionReply): HasNextUnansweredQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasNextUnansweredQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasNextUnansweredQuestionReply;
  static deserializeBinaryFromReader(message: HasNextUnansweredQuestionReply, reader: jspb.BinaryReader): HasNextUnansweredQuestionReply;
}

export namespace HasNextUnansweredQuestionReply {
  export type AsObject = {
    hasNextUnansweredQuestion: boolean,
  }
}

export class HasNextUnansweredQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasNextUnansweredQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasNextUnansweredQuestionRequest): HasNextUnansweredQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasNextUnansweredQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasNextUnansweredQuestionRequest;
  static deserializeBinaryFromReader(message: HasNextUnansweredQuestionRequest, reader: jspb.BinaryReader): HasNextUnansweredQuestionRequest;
}

export namespace HasNextUnansweredQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetNextUnansweredQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNextUnansweredQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetNextUnansweredQuestionReply): GetNextUnansweredQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNextUnansweredQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNextUnansweredQuestionReply;
  static deserializeBinaryFromReader(message: GetNextUnansweredQuestionReply, reader: jspb.BinaryReader): GetNextUnansweredQuestionReply;
}

export namespace GetNextUnansweredQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetNextUnansweredQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetNextUnansweredQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetNextUnansweredQuestionRequest): GetNextUnansweredQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetNextUnansweredQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetNextUnansweredQuestionRequest;
  static deserializeBinaryFromReader(message: GetNextUnansweredQuestionRequest, reader: jspb.BinaryReader): GetNextUnansweredQuestionRequest;
}

export namespace GetNextUnansweredQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasPreviousUnansweredQuestionReply extends jspb.Message {
  getHasPreviousUnansweredQuestion(): boolean;
  setHasPreviousUnansweredQuestion(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasPreviousUnansweredQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasPreviousUnansweredQuestionReply): HasPreviousUnansweredQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasPreviousUnansweredQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasPreviousUnansweredQuestionReply;
  static deserializeBinaryFromReader(message: HasPreviousUnansweredQuestionReply, reader: jspb.BinaryReader): HasPreviousUnansweredQuestionReply;
}

export namespace HasPreviousUnansweredQuestionReply {
  export type AsObject = {
    hasPreviousUnansweredQuestion: boolean,
  }
}

export class HasPreviousUnansweredQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasPreviousUnansweredQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasPreviousUnansweredQuestionRequest): HasPreviousUnansweredQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasPreviousUnansweredQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasPreviousUnansweredQuestionRequest;
  static deserializeBinaryFromReader(message: HasPreviousUnansweredQuestionRequest, reader: jspb.BinaryReader): HasPreviousUnansweredQuestionRequest;
}

export namespace HasPreviousUnansweredQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetPreviousUnansweredQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetPreviousUnansweredQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetPreviousUnansweredQuestionReply): GetPreviousUnansweredQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetPreviousUnansweredQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetPreviousUnansweredQuestionReply;
  static deserializeBinaryFromReader(message: GetPreviousUnansweredQuestionReply, reader: jspb.BinaryReader): GetPreviousUnansweredQuestionReply;
}

export namespace GetPreviousUnansweredQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class GetPreviousUnansweredQuestionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetPreviousUnansweredQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetPreviousUnansweredQuestionRequest): GetPreviousUnansweredQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetPreviousUnansweredQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetPreviousUnansweredQuestionRequest;
  static deserializeBinaryFromReader(message: GetPreviousUnansweredQuestionRequest, reader: jspb.BinaryReader): GetPreviousUnansweredQuestionRequest;
}

export namespace GetPreviousUnansweredQuestionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResponseReply extends jspb.Message {
  hasResponse(): boolean;
  clearResponse(): void;
  getResponse(): Response | undefined;
  setResponse(value?: Response): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResponseReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetResponseReply): GetResponseReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResponseReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResponseReply;
  static deserializeBinaryFromReader(message: GetResponseReply, reader: jspb.BinaryReader): GetResponseReply;
}

export namespace GetResponseReply {
  export type AsObject = {
    response?: Response.AsObject,
  }
}

export class GetResponseRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResponseRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResponseRequest): GetResponseRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResponseRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResponseRequest;
  static deserializeBinaryFromReader(message: GetResponseRequest, reader: jspb.BinaryReader): GetResponseRequest;
}

export namespace GetResponseRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetResponsesRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResponsesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetResponsesRequest): GetResponsesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResponsesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResponsesRequest;
  static deserializeBinaryFromReader(message: GetResponsesRequest, reader: jspb.BinaryReader): GetResponsesRequest;
}

export namespace GetResponsesRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ClearResponseReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ClearResponseReply.AsObject;
  static toObject(includeInstance: boolean, msg: ClearResponseReply): ClearResponseReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ClearResponseReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ClearResponseReply;
  static deserializeBinaryFromReader(message: ClearResponseReply, reader: jspb.BinaryReader): ClearResponseReply;
}

export namespace ClearResponseReply {
  export type AsObject = {
  }
}

export class ClearResponseRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ClearResponseRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ClearResponseRequest): ClearResponseRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ClearResponseRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ClearResponseRequest;
  static deserializeBinaryFromReader(message: ClearResponseRequest, reader: jspb.BinaryReader): ClearResponseRequest;
}

export namespace ClearResponseRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class FinishAssessmentSectionReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FinishAssessmentSectionReply.AsObject;
  static toObject(includeInstance: boolean, msg: FinishAssessmentSectionReply): FinishAssessmentSectionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FinishAssessmentSectionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FinishAssessmentSectionReply;
  static deserializeBinaryFromReader(message: FinishAssessmentSectionReply, reader: jspb.BinaryReader): FinishAssessmentSectionReply;
}

export namespace FinishAssessmentSectionReply {
  export type AsObject = {
  }
}

export class FinishAssessmentSectionRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FinishAssessmentSectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: FinishAssessmentSectionRequest): FinishAssessmentSectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FinishAssessmentSectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FinishAssessmentSectionRequest;
  static deserializeBinaryFromReader(message: FinishAssessmentSectionRequest, reader: jspb.BinaryReader): FinishAssessmentSectionRequest;
}

export namespace FinishAssessmentSectionRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAnswerAvailableReply extends jspb.Message {
  getIsAnswerAvailable(): boolean;
  setIsAnswerAvailable(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAnswerAvailableReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAnswerAvailableReply): IsAnswerAvailableReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAnswerAvailableReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAnswerAvailableReply;
  static deserializeBinaryFromReader(message: IsAnswerAvailableReply, reader: jspb.BinaryReader): IsAnswerAvailableReply;
}

export namespace IsAnswerAvailableReply {
  export type AsObject = {
    isAnswerAvailable: boolean,
  }
}

export class IsAnswerAvailableRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAnswerAvailableRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAnswerAvailableRequest): IsAnswerAvailableRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAnswerAvailableRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAnswerAvailableRequest;
  static deserializeBinaryFromReader(message: IsAnswerAvailableRequest, reader: jspb.BinaryReader): IsAnswerAvailableRequest;
}

export namespace IsAnswerAvailableRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAnswersRequest extends jspb.Message {
  hasAssessmentSectionId(): boolean;
  clearAssessmentSectionId(): void;
  getAssessmentSectionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentSectionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAnswersRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAnswersRequest): GetAnswersRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAnswersRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAnswersRequest;
  static deserializeBinaryFromReader(message: GetAnswersRequest, reader: jspb.BinaryReader): GetAnswersRequest;
}

export namespace GetAnswersRequest {
  export type AsObject = {
    assessmentSectionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class FinishAssessmentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FinishAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: FinishAssessmentReply): FinishAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FinishAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FinishAssessmentReply;
  static deserializeBinaryFromReader(message: FinishAssessmentReply, reader: jspb.BinaryReader): FinishAssessmentReply;
}

export namespace FinishAssessmentReply {
  export type AsObject = {
  }
}

export class FinishAssessmentRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FinishAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: FinishAssessmentRequest): FinishAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FinishAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FinishAssessmentRequest;
  static deserializeBinaryFromReader(message: FinishAssessmentRequest, reader: jspb.BinaryReader): FinishAssessmentRequest;
}

export namespace FinishAssessmentRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAccessAssessmentResultsReply extends jspb.Message {
  getCanAccessAssessmentResults(): boolean;
  setCanAccessAssessmentResults(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAssessmentResultsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAssessmentResultsReply): CanAccessAssessmentResultsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAssessmentResultsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAssessmentResultsReply;
  static deserializeBinaryFromReader(message: CanAccessAssessmentResultsReply, reader: jspb.BinaryReader): CanAccessAssessmentResultsReply;
}

export namespace CanAccessAssessmentResultsReply {
  export type AsObject = {
    canAccessAssessmentResults: boolean,
  }
}

export class CanAccessAssessmentResultsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessAssessmentResultsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessAssessmentResultsRequest): CanAccessAssessmentResultsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessAssessmentResultsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessAssessmentResultsRequest;
  static deserializeBinaryFromReader(message: CanAccessAssessmentResultsRequest, reader: jspb.BinaryReader): CanAccessAssessmentResultsRequest;
}

export namespace CanAccessAssessmentResultsRequest {
  export type AsObject = {
  }
}

export class GetItemsRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsRequest): GetItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsRequest;
  static deserializeBinaryFromReader(message: GetItemsRequest, reader: jspb.BinaryReader): GetItemsRequest;
}

export namespace GetItemsRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AreResultsAvailableReply extends jspb.Message {
  getAreResultsAvailable(): boolean;
  setAreResultsAvailable(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AreResultsAvailableReply.AsObject;
  static toObject(includeInstance: boolean, msg: AreResultsAvailableReply): AreResultsAvailableReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AreResultsAvailableReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AreResultsAvailableReply;
  static deserializeBinaryFromReader(message: AreResultsAvailableReply, reader: jspb.BinaryReader): AreResultsAvailableReply;
}

export namespace AreResultsAvailableReply {
  export type AsObject = {
    areResultsAvailable: boolean,
  }
}

export class AreResultsAvailableRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AreResultsAvailableRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AreResultsAvailableRequest): AreResultsAvailableRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AreResultsAvailableRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AreResultsAvailableRequest;
  static deserializeBinaryFromReader(message: AreResultsAvailableRequest, reader: jspb.BinaryReader): AreResultsAvailableRequest;
}

export namespace AreResultsAvailableRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetGradeEntriesRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupItemsReply extends jspb.Message {
  getCanLookupItems(): boolean;
  setCanLookupItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupItemsReply): CanLookupItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupItemsReply;
  static deserializeBinaryFromReader(message: CanLookupItemsReply, reader: jspb.BinaryReader): CanLookupItemsReply;
}

export namespace CanLookupItemsReply {
  export type AsObject = {
    canLookupItems: boolean,
  }
}

export class CanLookupItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupItemsRequest): CanLookupItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupItemsRequest;
  static deserializeBinaryFromReader(message: CanLookupItemsRequest, reader: jspb.BinaryReader): CanLookupItemsRequest;
}

export namespace CanLookupItemsRequest {
  export type AsObject = {
  }
}

export class UseComparativeItemViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeItemViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeItemViewReply): UseComparativeItemViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeItemViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeItemViewReply;
  static deserializeBinaryFromReader(message: UseComparativeItemViewReply, reader: jspb.BinaryReader): UseComparativeItemViewReply;
}

export namespace UseComparativeItemViewReply {
  export type AsObject = {
  }
}

export class UseComparativeItemViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeItemViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeItemViewRequest): UseComparativeItemViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeItemViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeItemViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeItemViewRequest, reader: jspb.BinaryReader): UseComparativeItemViewRequest;
}

export namespace UseComparativeItemViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryItemViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryItemViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryItemViewReply): UsePlenaryItemViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryItemViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryItemViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryItemViewReply, reader: jspb.BinaryReader): UsePlenaryItemViewReply;
}

export namespace UsePlenaryItemViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryItemViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryItemViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryItemViewRequest): UsePlenaryItemViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryItemViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryItemViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryItemViewRequest, reader: jspb.BinaryReader): UsePlenaryItemViewRequest;
}

export namespace UsePlenaryItemViewRequest {
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

export class GetItemReply extends jspb.Message {
  hasItem(): boolean;
  clearItem(): void;
  getItem(): Item | undefined;
  setItem(value?: Item): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemReply): GetItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemReply;
  static deserializeBinaryFromReader(message: GetItemReply, reader: jspb.BinaryReader): GetItemReply;
}

export namespace GetItemReply {
  export type AsObject = {
    item?: Item.AsObject,
  }
}

export class GetItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemRequest): GetItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemRequest;
  static deserializeBinaryFromReader(message: GetItemRequest, reader: jspb.BinaryReader): GetItemRequest;
}

export namespace GetItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetItemsByIdsRequest extends jspb.Message {
  clearItemIdsList(): void;
  getItemIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setItemIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addItemIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByIdsRequest): GetItemsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByIdsRequest;
  static deserializeBinaryFromReader(message: GetItemsByIdsRequest, reader: jspb.BinaryReader): GetItemsByIdsRequest;
}

export namespace GetItemsByIdsRequest {
  export type AsObject = {
    itemIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetItemsByGenusTypeRequest extends jspb.Message {
  hasItemGenusType(): boolean;
  clearItemGenusType(): void;
  getItemGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setItemGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByGenusTypeRequest): GetItemsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetItemsByGenusTypeRequest, reader: jspb.BinaryReader): GetItemsByGenusTypeRequest;
}

export namespace GetItemsByGenusTypeRequest {
  export type AsObject = {
    itemGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetItemsByParentGenusTypeRequest extends jspb.Message {
  hasItemGenusType(): boolean;
  clearItemGenusType(): void;
  getItemGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setItemGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByParentGenusTypeRequest): GetItemsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetItemsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetItemsByParentGenusTypeRequest;
}

export namespace GetItemsByParentGenusTypeRequest {
  export type AsObject = {
    itemGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetItemsByRecordTypeRequest extends jspb.Message {
  hasItemRecordType(): boolean;
  clearItemRecordType(): void;
  getItemRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setItemRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByRecordTypeRequest): GetItemsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetItemsByRecordTypeRequest, reader: jspb.BinaryReader): GetItemsByRecordTypeRequest;
}

export namespace GetItemsByRecordTypeRequest {
  export type AsObject = {
    itemRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetItemsByQuestionRequest extends jspb.Message {
  hasQuestionId(): boolean;
  clearQuestionId(): void;
  getQuestionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQuestionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByQuestionRequest): GetItemsByQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByQuestionRequest;
  static deserializeBinaryFromReader(message: GetItemsByQuestionRequest, reader: jspb.BinaryReader): GetItemsByQuestionRequest;
}

export namespace GetItemsByQuestionRequest {
  export type AsObject = {
    questionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetItemsByAnswerRequest extends jspb.Message {
  hasAnswerId(): boolean;
  clearAnswerId(): void;
  getAnswerId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAnswerId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByAnswerRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByAnswerRequest): GetItemsByAnswerRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByAnswerRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByAnswerRequest;
  static deserializeBinaryFromReader(message: GetItemsByAnswerRequest, reader: jspb.BinaryReader): GetItemsByAnswerRequest;
}

export namespace GetItemsByAnswerRequest {
  export type AsObject = {
    answerId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetItemsByLearningObjectiveRequest extends jspb.Message {
  hasObjectiveId(): boolean;
  clearObjectiveId(): void;
  getObjectiveId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setObjectiveId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByLearningObjectiveRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByLearningObjectiveRequest): GetItemsByLearningObjectiveRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByLearningObjectiveRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByLearningObjectiveRequest;
  static deserializeBinaryFromReader(message: GetItemsByLearningObjectiveRequest, reader: jspb.BinaryReader): GetItemsByLearningObjectiveRequest;
}

export namespace GetItemsByLearningObjectiveRequest {
  export type AsObject = {
    objectiveId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetItemsByLearningObjectivesRequest extends jspb.Message {
  clearObjectiveIdsList(): void;
  getObjectiveIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setObjectiveIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addObjectiveIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByLearningObjectivesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByLearningObjectivesRequest): GetItemsByLearningObjectivesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByLearningObjectivesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByLearningObjectivesRequest;
  static deserializeBinaryFromReader(message: GetItemsByLearningObjectivesRequest, reader: jspb.BinaryReader): GetItemsByLearningObjectivesRequest;
}

export namespace GetItemsByLearningObjectivesRequest {
  export type AsObject = {
    objectiveIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class CanSearchItemsReply extends jspb.Message {
  getCanSearchItems(): boolean;
  setCanSearchItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchItemsReply): CanSearchItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchItemsReply;
  static deserializeBinaryFromReader(message: CanSearchItemsReply, reader: jspb.BinaryReader): CanSearchItemsReply;
}

export namespace CanSearchItemsReply {
  export type AsObject = {
    canSearchItems: boolean,
  }
}

export class CanSearchItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchItemsRequest): CanSearchItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchItemsRequest;
  static deserializeBinaryFromReader(message: CanSearchItemsRequest, reader: jspb.BinaryReader): CanSearchItemsRequest;
}

export namespace CanSearchItemsRequest {
  export type AsObject = {
  }
}

export class GetItemQueryReply extends jspb.Message {
  hasItemQuery(): boolean;
  clearItemQuery(): void;
  getItemQuery(): ItemQuery | undefined;
  setItemQuery(value?: ItemQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemQueryReply): GetItemQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemQueryReply;
  static deserializeBinaryFromReader(message: GetItemQueryReply, reader: jspb.BinaryReader): GetItemQueryReply;
}

export namespace GetItemQueryReply {
  export type AsObject = {
    itemQuery?: ItemQuery.AsObject,
  }
}

export class GetItemQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemQueryRequest): GetItemQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemQueryRequest;
  static deserializeBinaryFromReader(message: GetItemQueryRequest, reader: jspb.BinaryReader): GetItemQueryRequest;
}

export namespace GetItemQueryRequest {
  export type AsObject = {
  }
}

export class GetItemsByQueryRequest extends jspb.Message {
  hasItemQuery(): boolean;
  clearItemQuery(): void;
  getItemQuery(): ItemQuery | undefined;
  setItemQuery(value?: ItemQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByQueryRequest): GetItemsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByQueryRequest;
  static deserializeBinaryFromReader(message: GetItemsByQueryRequest, reader: jspb.BinaryReader): GetItemsByQueryRequest;
}

export namespace GetItemsByQueryRequest {
  export type AsObject = {
    itemQuery?: ItemQuery.AsObject,
  }
}

export class GetItemSearchReply extends jspb.Message {
  hasItemSearch(): boolean;
  clearItemSearch(): void;
  getItemSearch(): ItemSearch | undefined;
  setItemSearch(value?: ItemSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemSearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemSearchReply): GetItemSearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemSearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemSearchReply;
  static deserializeBinaryFromReader(message: GetItemSearchReply, reader: jspb.BinaryReader): GetItemSearchReply;
}

export namespace GetItemSearchReply {
  export type AsObject = {
    itemSearch?: ItemSearch.AsObject,
  }
}

export class GetItemSearchRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemSearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemSearchRequest): GetItemSearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemSearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemSearchRequest;
  static deserializeBinaryFromReader(message: GetItemSearchRequest, reader: jspb.BinaryReader): GetItemSearchRequest;
}

export namespace GetItemSearchRequest {
  export type AsObject = {
  }
}

export class GetItemSearchOrderReply extends jspb.Message {
  hasItemSearchOrder(): boolean;
  clearItemSearchOrder(): void;
  getItemSearchOrder(): ItemSearchOrder | undefined;
  setItemSearchOrder(value?: ItemSearchOrder): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemSearchOrderReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemSearchOrderReply): GetItemSearchOrderReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemSearchOrderReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemSearchOrderReply;
  static deserializeBinaryFromReader(message: GetItemSearchOrderReply, reader: jspb.BinaryReader): GetItemSearchOrderReply;
}

export namespace GetItemSearchOrderReply {
  export type AsObject = {
    itemSearchOrder?: ItemSearchOrder.AsObject,
  }
}

export class GetItemSearchOrderRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemSearchOrderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemSearchOrderRequest): GetItemSearchOrderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemSearchOrderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemSearchOrderRequest;
  static deserializeBinaryFromReader(message: GetItemSearchOrderRequest, reader: jspb.BinaryReader): GetItemSearchOrderRequest;
}

export namespace GetItemSearchOrderRequest {
  export type AsObject = {
  }
}

export class GetItemsBySearchReply extends jspb.Message {
  hasItemSearchResults(): boolean;
  clearItemSearchResults(): void;
  getItemSearchResults(): ItemSearchResults | undefined;
  setItemSearchResults(value?: ItemSearchResults): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsBySearchReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsBySearchReply): GetItemsBySearchReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsBySearchReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsBySearchReply;
  static deserializeBinaryFromReader(message: GetItemsBySearchReply, reader: jspb.BinaryReader): GetItemsBySearchReply;
}

export namespace GetItemsBySearchReply {
  export type AsObject = {
    itemSearchResults?: ItemSearchResults.AsObject,
  }
}

export class GetItemsBySearchRequest extends jspb.Message {
  hasItemQuery(): boolean;
  clearItemQuery(): void;
  getItemQuery(): ItemQuery | undefined;
  setItemQuery(value?: ItemQuery): void;

  hasItemSearch(): boolean;
  clearItemSearch(): void;
  getItemSearch(): ItemSearch | undefined;
  setItemSearch(value?: ItemSearch): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsBySearchRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsBySearchRequest): GetItemsBySearchRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsBySearchRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsBySearchRequest;
  static deserializeBinaryFromReader(message: GetItemsBySearchRequest, reader: jspb.BinaryReader): GetItemsBySearchRequest;
}

export namespace GetItemsBySearchRequest {
  export type AsObject = {
    itemQuery?: ItemQuery.AsObject,
    itemSearch?: ItemSearch.AsObject,
  }
}

export class GetItemQueryFromInspectorReply extends jspb.Message {
  hasItemQuery(): boolean;
  clearItemQuery(): void;
  getItemQuery(): ItemQuery | undefined;
  setItemQuery(value?: ItemQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemQueryFromInspectorReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemQueryFromInspectorReply): GetItemQueryFromInspectorReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemQueryFromInspectorReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemQueryFromInspectorReply;
  static deserializeBinaryFromReader(message: GetItemQueryFromInspectorReply, reader: jspb.BinaryReader): GetItemQueryFromInspectorReply;
}

export namespace GetItemQueryFromInspectorReply {
  export type AsObject = {
    itemQuery?: ItemQuery.AsObject,
  }
}

export class GetItemQueryFromInspectorRequest extends jspb.Message {
  hasItemQueryInspector(): boolean;
  clearItemQueryInspector(): void;
  getItemQueryInspector(): ItemQueryInspector | undefined;
  setItemQueryInspector(value?: ItemQueryInspector): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemQueryFromInspectorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemQueryFromInspectorRequest): GetItemQueryFromInspectorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemQueryFromInspectorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemQueryFromInspectorRequest;
  static deserializeBinaryFromReader(message: GetItemQueryFromInspectorRequest, reader: jspb.BinaryReader): GetItemQueryFromInspectorRequest;
}

export namespace GetItemQueryFromInspectorRequest {
  export type AsObject = {
    itemQueryInspector?: ItemQueryInspector.AsObject,
  }
}

export class CanCreateItemsReply extends jspb.Message {
  getCanCreateItems(): boolean;
  setCanCreateItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateItemsReply): CanCreateItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateItemsReply;
  static deserializeBinaryFromReader(message: CanCreateItemsReply, reader: jspb.BinaryReader): CanCreateItemsReply;
}

export namespace CanCreateItemsReply {
  export type AsObject = {
    canCreateItems: boolean,
  }
}

export class CanCreateItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateItemsRequest): CanCreateItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateItemsRequest;
  static deserializeBinaryFromReader(message: CanCreateItemsRequest, reader: jspb.BinaryReader): CanCreateItemsRequest;
}

export namespace CanCreateItemsRequest {
  export type AsObject = {
  }
}

export class CanCreateItemWithRecordTypesReply extends jspb.Message {
  getCanCreateItemWithRecordTypes(): boolean;
  setCanCreateItemWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateItemWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateItemWithRecordTypesReply): CanCreateItemWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateItemWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateItemWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateItemWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateItemWithRecordTypesReply;
}

export namespace CanCreateItemWithRecordTypesReply {
  export type AsObject = {
    canCreateItemWithRecordTypes: boolean,
  }
}

export class CanCreateItemWithRecordTypesRequest extends jspb.Message {
  clearItemRecordTypesList(): void;
  getItemRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setItemRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addItemRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateItemWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateItemWithRecordTypesRequest): CanCreateItemWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateItemWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateItemWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateItemWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateItemWithRecordTypesRequest;
}

export namespace CanCreateItemWithRecordTypesRequest {
  export type AsObject = {
    itemRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetItemFormForCreateReply extends jspb.Message {
  hasItemForm(): boolean;
  clearItemForm(): void;
  getItemForm(): ItemForm | undefined;
  setItemForm(value?: ItemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemFormForCreateReply): GetItemFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemFormForCreateReply;
  static deserializeBinaryFromReader(message: GetItemFormForCreateReply, reader: jspb.BinaryReader): GetItemFormForCreateReply;
}

export namespace GetItemFormForCreateReply {
  export type AsObject = {
    itemForm?: ItemForm.AsObject,
  }
}

export class GetItemFormForCreateRequest extends jspb.Message {
  clearItemRecordTypesList(): void;
  getItemRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setItemRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addItemRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemFormForCreateRequest): GetItemFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetItemFormForCreateRequest, reader: jspb.BinaryReader): GetItemFormForCreateRequest;
}

export namespace GetItemFormForCreateRequest {
  export type AsObject = {
    itemRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateItemReply extends jspb.Message {
  hasItem(): boolean;
  clearItem(): void;
  getItem(): Item | undefined;
  setItem(value?: Item): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateItemReply): CreateItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateItemReply;
  static deserializeBinaryFromReader(message: CreateItemReply, reader: jspb.BinaryReader): CreateItemReply;
}

export namespace CreateItemReply {
  export type AsObject = {
    item?: Item.AsObject,
  }
}

export class CreateItemRequest extends jspb.Message {
  hasItemForm(): boolean;
  clearItemForm(): void;
  getItemForm(): ItemForm | undefined;
  setItemForm(value?: ItemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateItemRequest): CreateItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateItemRequest;
  static deserializeBinaryFromReader(message: CreateItemRequest, reader: jspb.BinaryReader): CreateItemRequest;
}

export namespace CreateItemRequest {
  export type AsObject = {
    itemForm?: ItemForm.AsObject,
  }
}

export class CanUpdateItemsReply extends jspb.Message {
  getCanUpdateItems(): boolean;
  setCanUpdateItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateItemsReply): CanUpdateItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateItemsReply;
  static deserializeBinaryFromReader(message: CanUpdateItemsReply, reader: jspb.BinaryReader): CanUpdateItemsReply;
}

export namespace CanUpdateItemsReply {
  export type AsObject = {
    canUpdateItems: boolean,
  }
}

export class CanUpdateItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateItemsRequest): CanUpdateItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateItemsRequest;
  static deserializeBinaryFromReader(message: CanUpdateItemsRequest, reader: jspb.BinaryReader): CanUpdateItemsRequest;
}

export namespace CanUpdateItemsRequest {
  export type AsObject = {
  }
}

export class GetItemFormForUpdateReply extends jspb.Message {
  hasItemForm(): boolean;
  clearItemForm(): void;
  getItemForm(): ItemForm | undefined;
  setItemForm(value?: ItemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemFormForUpdateReply): GetItemFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetItemFormForUpdateReply, reader: jspb.BinaryReader): GetItemFormForUpdateReply;
}

export namespace GetItemFormForUpdateReply {
  export type AsObject = {
    itemForm?: ItemForm.AsObject,
  }
}

export class GetItemFormForUpdateRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemFormForUpdateRequest): GetItemFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetItemFormForUpdateRequest, reader: jspb.BinaryReader): GetItemFormForUpdateRequest;
}

export namespace GetItemFormForUpdateRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateItemReply): UpdateItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateItemReply;
  static deserializeBinaryFromReader(message: UpdateItemReply, reader: jspb.BinaryReader): UpdateItemReply;
}

export namespace UpdateItemReply {
  export type AsObject = {
  }
}

export class UpdateItemRequest extends jspb.Message {
  hasItemForm(): boolean;
  clearItemForm(): void;
  getItemForm(): ItemForm | undefined;
  setItemForm(value?: ItemForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateItemRequest): UpdateItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateItemRequest;
  static deserializeBinaryFromReader(message: UpdateItemRequest, reader: jspb.BinaryReader): UpdateItemRequest;
}

export namespace UpdateItemRequest {
  export type AsObject = {
    itemForm?: ItemForm.AsObject,
  }
}

export class CanDeleteItemsReply extends jspb.Message {
  getCanDeleteItems(): boolean;
  setCanDeleteItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteItemsReply): CanDeleteItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteItemsReply;
  static deserializeBinaryFromReader(message: CanDeleteItemsReply, reader: jspb.BinaryReader): CanDeleteItemsReply;
}

export namespace CanDeleteItemsReply {
  export type AsObject = {
    canDeleteItems: boolean,
  }
}

export class CanDeleteItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteItemsRequest): CanDeleteItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteItemsRequest;
  static deserializeBinaryFromReader(message: CanDeleteItemsRequest, reader: jspb.BinaryReader): CanDeleteItemsRequest;
}

export namespace CanDeleteItemsRequest {
  export type AsObject = {
  }
}

export class DeleteItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteItemReply): DeleteItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteItemReply;
  static deserializeBinaryFromReader(message: DeleteItemReply, reader: jspb.BinaryReader): DeleteItemReply;
}

export namespace DeleteItemReply {
  export type AsObject = {
  }
}

export class DeleteItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteItemRequest): DeleteItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteItemRequest;
  static deserializeBinaryFromReader(message: DeleteItemRequest, reader: jspb.BinaryReader): DeleteItemRequest;
}

export namespace DeleteItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageItemAliasesReply extends jspb.Message {
  getCanManageItemAliases(): boolean;
  setCanManageItemAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageItemAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageItemAliasesReply): CanManageItemAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageItemAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageItemAliasesReply;
  static deserializeBinaryFromReader(message: CanManageItemAliasesReply, reader: jspb.BinaryReader): CanManageItemAliasesReply;
}

export namespace CanManageItemAliasesReply {
  export type AsObject = {
    canManageItemAliases: boolean,
  }
}

export class CanManageItemAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageItemAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageItemAliasesRequest): CanManageItemAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageItemAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageItemAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageItemAliasesRequest, reader: jspb.BinaryReader): CanManageItemAliasesRequest;
}

export namespace CanManageItemAliasesRequest {
  export type AsObject = {
  }
}

export class AliasItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasItemReply): AliasItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasItemReply;
  static deserializeBinaryFromReader(message: AliasItemReply, reader: jspb.BinaryReader): AliasItemReply;
}

export namespace AliasItemReply {
  export type AsObject = {
  }
}

export class AliasItemRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasItemRequest): AliasItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasItemRequest;
  static deserializeBinaryFromReader(message: AliasItemRequest, reader: jspb.BinaryReader): AliasItemRequest;
}

export namespace AliasItemRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanCreateQuestionsReply extends jspb.Message {
  getCanCreateQuestions(): boolean;
  setCanCreateQuestions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateQuestionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateQuestionsReply): CanCreateQuestionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateQuestionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateQuestionsReply;
  static deserializeBinaryFromReader(message: CanCreateQuestionsReply, reader: jspb.BinaryReader): CanCreateQuestionsReply;
}

export namespace CanCreateQuestionsReply {
  export type AsObject = {
    canCreateQuestions: boolean,
  }
}

export class CanCreateQuestionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateQuestionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateQuestionsRequest): CanCreateQuestionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateQuestionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateQuestionsRequest;
  static deserializeBinaryFromReader(message: CanCreateQuestionsRequest, reader: jspb.BinaryReader): CanCreateQuestionsRequest;
}

export namespace CanCreateQuestionsRequest {
  export type AsObject = {
  }
}

export class CanCreateQuestionWithRecordTypesReply extends jspb.Message {
  getCanCreateQuestionWithRecordTypes(): boolean;
  setCanCreateQuestionWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateQuestionWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateQuestionWithRecordTypesReply): CanCreateQuestionWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateQuestionWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateQuestionWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateQuestionWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateQuestionWithRecordTypesReply;
}

export namespace CanCreateQuestionWithRecordTypesReply {
  export type AsObject = {
    canCreateQuestionWithRecordTypes: boolean,
  }
}

export class CanCreateQuestionWithRecordTypesRequest extends jspb.Message {
  clearQuestionRecordTypesList(): void;
  getQuestionRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setQuestionRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addQuestionRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateQuestionWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateQuestionWithRecordTypesRequest): CanCreateQuestionWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateQuestionWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateQuestionWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateQuestionWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateQuestionWithRecordTypesRequest;
}

export namespace CanCreateQuestionWithRecordTypesRequest {
  export type AsObject = {
    questionRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetQuestionFormForCreateReply extends jspb.Message {
  hasQuestionForm(): boolean;
  clearQuestionForm(): void;
  getQuestionForm(): QuestionForm | undefined;
  setQuestionForm(value?: QuestionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionFormForCreateReply): GetQuestionFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionFormForCreateReply;
  static deserializeBinaryFromReader(message: GetQuestionFormForCreateReply, reader: jspb.BinaryReader): GetQuestionFormForCreateReply;
}

export namespace GetQuestionFormForCreateReply {
  export type AsObject = {
    questionForm?: QuestionForm.AsObject,
  }
}

export class GetQuestionFormForCreateRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearQuestionRecordTypesList(): void;
  getQuestionRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setQuestionRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addQuestionRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionFormForCreateRequest): GetQuestionFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetQuestionFormForCreateRequest, reader: jspb.BinaryReader): GetQuestionFormForCreateRequest;
}

export namespace GetQuestionFormForCreateRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    questionRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateQuestionReply extends jspb.Message {
  hasQuestion(): boolean;
  clearQuestion(): void;
  getQuestion(): Question | undefined;
  setQuestion(value?: Question): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateQuestionReply): CreateQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateQuestionReply;
  static deserializeBinaryFromReader(message: CreateQuestionReply, reader: jspb.BinaryReader): CreateQuestionReply;
}

export namespace CreateQuestionReply {
  export type AsObject = {
    question?: Question.AsObject,
  }
}

export class CreateQuestionRequest extends jspb.Message {
  hasQuestionForm(): boolean;
  clearQuestionForm(): void;
  getQuestionForm(): QuestionForm | undefined;
  setQuestionForm(value?: QuestionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateQuestionRequest): CreateQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateQuestionRequest;
  static deserializeBinaryFromReader(message: CreateQuestionRequest, reader: jspb.BinaryReader): CreateQuestionRequest;
}

export namespace CreateQuestionRequest {
  export type AsObject = {
    questionForm?: QuestionForm.AsObject,
  }
}

export class CanUpdateQuestionsReply extends jspb.Message {
  getCanUpdateQuestions(): boolean;
  setCanUpdateQuestions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateQuestionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateQuestionsReply): CanUpdateQuestionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateQuestionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateQuestionsReply;
  static deserializeBinaryFromReader(message: CanUpdateQuestionsReply, reader: jspb.BinaryReader): CanUpdateQuestionsReply;
}

export namespace CanUpdateQuestionsReply {
  export type AsObject = {
    canUpdateQuestions: boolean,
  }
}

export class CanUpdateQuestionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateQuestionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateQuestionsRequest): CanUpdateQuestionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateQuestionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateQuestionsRequest;
  static deserializeBinaryFromReader(message: CanUpdateQuestionsRequest, reader: jspb.BinaryReader): CanUpdateQuestionsRequest;
}

export namespace CanUpdateQuestionsRequest {
  export type AsObject = {
  }
}

export class GetQuestionFormForUpdateReply extends jspb.Message {
  hasQuestionForm(): boolean;
  clearQuestionForm(): void;
  getQuestionForm(): QuestionForm | undefined;
  setQuestionForm(value?: QuestionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionFormForUpdateReply): GetQuestionFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetQuestionFormForUpdateReply, reader: jspb.BinaryReader): GetQuestionFormForUpdateReply;
}

export namespace GetQuestionFormForUpdateReply {
  export type AsObject = {
    questionForm?: QuestionForm.AsObject,
  }
}

export class GetQuestionFormForUpdateRequest extends jspb.Message {
  hasQuestionId(): boolean;
  clearQuestionId(): void;
  getQuestionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQuestionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetQuestionFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetQuestionFormForUpdateRequest): GetQuestionFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetQuestionFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetQuestionFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetQuestionFormForUpdateRequest, reader: jspb.BinaryReader): GetQuestionFormForUpdateRequest;
}

export namespace GetQuestionFormForUpdateRequest {
  export type AsObject = {
    questionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateQuestionReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateQuestionReply): UpdateQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateQuestionReply;
  static deserializeBinaryFromReader(message: UpdateQuestionReply, reader: jspb.BinaryReader): UpdateQuestionReply;
}

export namespace UpdateQuestionReply {
  export type AsObject = {
  }
}

export class UpdateQuestionRequest extends jspb.Message {
  hasQuestionForm(): boolean;
  clearQuestionForm(): void;
  getQuestionForm(): QuestionForm | undefined;
  setQuestionForm(value?: QuestionForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateQuestionRequest): UpdateQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateQuestionRequest;
  static deserializeBinaryFromReader(message: UpdateQuestionRequest, reader: jspb.BinaryReader): UpdateQuestionRequest;
}

export namespace UpdateQuestionRequest {
  export type AsObject = {
    questionForm?: QuestionForm.AsObject,
  }
}

export class CanDeleteQuestionsReply extends jspb.Message {
  getCanDeleteQuestions(): boolean;
  setCanDeleteQuestions(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteQuestionsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteQuestionsReply): CanDeleteQuestionsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteQuestionsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteQuestionsReply;
  static deserializeBinaryFromReader(message: CanDeleteQuestionsReply, reader: jspb.BinaryReader): CanDeleteQuestionsReply;
}

export namespace CanDeleteQuestionsReply {
  export type AsObject = {
    canDeleteQuestions: boolean,
  }
}

export class CanDeleteQuestionsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteQuestionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteQuestionsRequest): CanDeleteQuestionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteQuestionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteQuestionsRequest;
  static deserializeBinaryFromReader(message: CanDeleteQuestionsRequest, reader: jspb.BinaryReader): CanDeleteQuestionsRequest;
}

export namespace CanDeleteQuestionsRequest {
  export type AsObject = {
  }
}

export class DeleteQuestionReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteQuestionReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteQuestionReply): DeleteQuestionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteQuestionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteQuestionReply;
  static deserializeBinaryFromReader(message: DeleteQuestionReply, reader: jspb.BinaryReader): DeleteQuestionReply;
}

export namespace DeleteQuestionReply {
  export type AsObject = {
  }
}

export class DeleteQuestionRequest extends jspb.Message {
  hasQuestionId(): boolean;
  clearQuestionId(): void;
  getQuestionId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setQuestionId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteQuestionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteQuestionRequest): DeleteQuestionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteQuestionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteQuestionRequest;
  static deserializeBinaryFromReader(message: DeleteQuestionRequest, reader: jspb.BinaryReader): DeleteQuestionRequest;
}

export namespace DeleteQuestionRequest {
  export type AsObject = {
    questionId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanCreateAnswersReply extends jspb.Message {
  getCanCreateAnswers(): boolean;
  setCanCreateAnswers(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAnswersReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAnswersReply): CanCreateAnswersReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAnswersReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAnswersReply;
  static deserializeBinaryFromReader(message: CanCreateAnswersReply, reader: jspb.BinaryReader): CanCreateAnswersReply;
}

export namespace CanCreateAnswersReply {
  export type AsObject = {
    canCreateAnswers: boolean,
  }
}

export class CanCreateAnswersRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAnswersRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAnswersRequest): CanCreateAnswersRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAnswersRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAnswersRequest;
  static deserializeBinaryFromReader(message: CanCreateAnswersRequest, reader: jspb.BinaryReader): CanCreateAnswersRequest;
}

export namespace CanCreateAnswersRequest {
  export type AsObject = {
  }
}

export class CanCreateAnswersWithRecordTypesReply extends jspb.Message {
  getCanCreateAnswersWithRecordTypes(): boolean;
  setCanCreateAnswersWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAnswersWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAnswersWithRecordTypesReply): CanCreateAnswersWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAnswersWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAnswersWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAnswersWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAnswersWithRecordTypesReply;
}

export namespace CanCreateAnswersWithRecordTypesReply {
  export type AsObject = {
    canCreateAnswersWithRecordTypes: boolean,
  }
}

export class CanCreateAnswersWithRecordTypesRequest extends jspb.Message {
  clearAnswerRecordTypesList(): void;
  getAnswerRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAnswerRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAnswerRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAnswersWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAnswersWithRecordTypesRequest): CanCreateAnswersWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAnswersWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAnswersWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAnswersWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAnswersWithRecordTypesRequest;
}

export namespace CanCreateAnswersWithRecordTypesRequest {
  export type AsObject = {
    answerRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAnswerFormForCreateReply extends jspb.Message {
  hasAnswerForm(): boolean;
  clearAnswerForm(): void;
  getAnswerForm(): AnswerForm | undefined;
  setAnswerForm(value?: AnswerForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAnswerFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAnswerFormForCreateReply): GetAnswerFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAnswerFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAnswerFormForCreateReply;
  static deserializeBinaryFromReader(message: GetAnswerFormForCreateReply, reader: jspb.BinaryReader): GetAnswerFormForCreateReply;
}

export namespace GetAnswerFormForCreateReply {
  export type AsObject = {
    answerForm?: AnswerForm.AsObject,
  }
}

export class GetAnswerFormForCreateRequest extends jspb.Message {
  clearAnswerRecordTypesList(): void;
  getAnswerRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAnswerRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAnswerRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAnswerFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAnswerFormForCreateRequest): GetAnswerFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAnswerFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAnswerFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetAnswerFormForCreateRequest, reader: jspb.BinaryReader): GetAnswerFormForCreateRequest;
}

export namespace GetAnswerFormForCreateRequest {
  export type AsObject = {
    answerRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateAnswerReply extends jspb.Message {
  hasAnswer(): boolean;
  clearAnswer(): void;
  getAnswer(): Answer | undefined;
  setAnswer(value?: Answer): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAnswerReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAnswerReply): CreateAnswerReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAnswerReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAnswerReply;
  static deserializeBinaryFromReader(message: CreateAnswerReply, reader: jspb.BinaryReader): CreateAnswerReply;
}

export namespace CreateAnswerReply {
  export type AsObject = {
    answer?: Answer.AsObject,
  }
}

export class CreateAnswerRequest extends jspb.Message {
  hasAnswerForm(): boolean;
  clearAnswerForm(): void;
  getAnswerForm(): AnswerForm | undefined;
  setAnswerForm(value?: AnswerForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAnswerRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAnswerRequest): CreateAnswerRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAnswerRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAnswerRequest;
  static deserializeBinaryFromReader(message: CreateAnswerRequest, reader: jspb.BinaryReader): CreateAnswerRequest;
}

export namespace CreateAnswerRequest {
  export type AsObject = {
    answerForm?: AnswerForm.AsObject,
  }
}

export class CanUpdateAnswersReply extends jspb.Message {
  getCanUpdateAnswers(): boolean;
  setCanUpdateAnswers(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAnswersReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAnswersReply): CanUpdateAnswersReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAnswersReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAnswersReply;
  static deserializeBinaryFromReader(message: CanUpdateAnswersReply, reader: jspb.BinaryReader): CanUpdateAnswersReply;
}

export namespace CanUpdateAnswersReply {
  export type AsObject = {
    canUpdateAnswers: boolean,
  }
}

export class CanUpdateAnswersRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAnswersRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAnswersRequest): CanUpdateAnswersRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAnswersRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAnswersRequest;
  static deserializeBinaryFromReader(message: CanUpdateAnswersRequest, reader: jspb.BinaryReader): CanUpdateAnswersRequest;
}

export namespace CanUpdateAnswersRequest {
  export type AsObject = {
  }
}

export class GetAnswerFormForUpdateReply extends jspb.Message {
  hasAnswerForm(): boolean;
  clearAnswerForm(): void;
  getAnswerForm(): AnswerForm | undefined;
  setAnswerForm(value?: AnswerForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAnswerFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAnswerFormForUpdateReply): GetAnswerFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAnswerFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAnswerFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAnswerFormForUpdateReply, reader: jspb.BinaryReader): GetAnswerFormForUpdateReply;
}

export namespace GetAnswerFormForUpdateReply {
  export type AsObject = {
    answerForm?: AnswerForm.AsObject,
  }
}

export class GetAnswerFormForUpdateRequest extends jspb.Message {
  hasAnswerId(): boolean;
  clearAnswerId(): void;
  getAnswerId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAnswerId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAnswerFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAnswerFormForUpdateRequest): GetAnswerFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAnswerFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAnswerFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAnswerFormForUpdateRequest, reader: jspb.BinaryReader): GetAnswerFormForUpdateRequest;
}

export namespace GetAnswerFormForUpdateRequest {
  export type AsObject = {
    answerId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAnswerReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAnswerReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAnswerReply): UpdateAnswerReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAnswerReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAnswerReply;
  static deserializeBinaryFromReader(message: UpdateAnswerReply, reader: jspb.BinaryReader): UpdateAnswerReply;
}

export namespace UpdateAnswerReply {
  export type AsObject = {
  }
}

export class UpdateAnswerRequest extends jspb.Message {
  hasAnswerForm(): boolean;
  clearAnswerForm(): void;
  getAnswerForm(): AnswerForm | undefined;
  setAnswerForm(value?: AnswerForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAnswerRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAnswerRequest): UpdateAnswerRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAnswerRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAnswerRequest;
  static deserializeBinaryFromReader(message: UpdateAnswerRequest, reader: jspb.BinaryReader): UpdateAnswerRequest;
}

export namespace UpdateAnswerRequest {
  export type AsObject = {
    answerForm?: AnswerForm.AsObject,
  }
}

export class CanDeleteAnswersReply extends jspb.Message {
  getCanDeleteAnswers(): boolean;
  setCanDeleteAnswers(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAnswersReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAnswersReply): CanDeleteAnswersReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAnswersReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAnswersReply;
  static deserializeBinaryFromReader(message: CanDeleteAnswersReply, reader: jspb.BinaryReader): CanDeleteAnswersReply;
}

export namespace CanDeleteAnswersReply {
  export type AsObject = {
    canDeleteAnswers: boolean,
  }
}

export class CanDeleteAnswersRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAnswersRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAnswersRequest): CanDeleteAnswersRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAnswersRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAnswersRequest;
  static deserializeBinaryFromReader(message: CanDeleteAnswersRequest, reader: jspb.BinaryReader): CanDeleteAnswersRequest;
}

export namespace CanDeleteAnswersRequest {
  export type AsObject = {
  }
}

export class DeleteAnswerReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAnswerReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAnswerReply): DeleteAnswerReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAnswerReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAnswerReply;
  static deserializeBinaryFromReader(message: DeleteAnswerReply, reader: jspb.BinaryReader): DeleteAnswerReply;
}

export namespace DeleteAnswerReply {
  export type AsObject = {
  }
}

export class DeleteAnswerRequest extends jspb.Message {
  hasAnswerId(): boolean;
  clearAnswerId(): void;
  getAnswerId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAnswerId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAnswerRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAnswerRequest): DeleteAnswerRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAnswerRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAnswerRequest;
  static deserializeBinaryFromReader(message: DeleteAnswerRequest, reader: jspb.BinaryReader): DeleteAnswerRequest;
}

export namespace DeleteAnswerRequest {
  export type AsObject = {
    answerId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanRegisterForItemNotificationsReply extends jspb.Message {
  getCanRegisterForItemNotifications(): boolean;
  setCanRegisterForItemNotifications(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanRegisterForItemNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanRegisterForItemNotificationsReply): CanRegisterForItemNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanRegisterForItemNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanRegisterForItemNotificationsReply;
  static deserializeBinaryFromReader(message: CanRegisterForItemNotificationsReply, reader: jspb.BinaryReader): CanRegisterForItemNotificationsReply;
}

export namespace CanRegisterForItemNotificationsReply {
  export type AsObject = {
    canRegisterForItemNotifications: boolean,
  }
}

export class CanRegisterForItemNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanRegisterForItemNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanRegisterForItemNotificationsRequest): CanRegisterForItemNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanRegisterForItemNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanRegisterForItemNotificationsRequest;
  static deserializeBinaryFromReader(message: CanRegisterForItemNotificationsRequest, reader: jspb.BinaryReader): CanRegisterForItemNotificationsRequest;
}

export namespace CanRegisterForItemNotificationsRequest {
  export type AsObject = {
  }
}

export class ReliableItemNotificationsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReliableItemNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReliableItemNotificationsReply): ReliableItemNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReliableItemNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReliableItemNotificationsReply;
  static deserializeBinaryFromReader(message: ReliableItemNotificationsReply, reader: jspb.BinaryReader): ReliableItemNotificationsReply;
}

export namespace ReliableItemNotificationsReply {
  export type AsObject = {
  }
}

export class ReliableItemNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReliableItemNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReliableItemNotificationsRequest): ReliableItemNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReliableItemNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReliableItemNotificationsRequest;
  static deserializeBinaryFromReader(message: ReliableItemNotificationsRequest, reader: jspb.BinaryReader): ReliableItemNotificationsRequest;
}

export namespace ReliableItemNotificationsRequest {
  export type AsObject = {
  }
}

export class UnreliableItemNotificationsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnreliableItemNotificationsReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnreliableItemNotificationsReply): UnreliableItemNotificationsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnreliableItemNotificationsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnreliableItemNotificationsReply;
  static deserializeBinaryFromReader(message: UnreliableItemNotificationsReply, reader: jspb.BinaryReader): UnreliableItemNotificationsReply;
}

export namespace UnreliableItemNotificationsReply {
  export type AsObject = {
  }
}

export class UnreliableItemNotificationsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnreliableItemNotificationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnreliableItemNotificationsRequest): UnreliableItemNotificationsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnreliableItemNotificationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnreliableItemNotificationsRequest;
  static deserializeBinaryFromReader(message: UnreliableItemNotificationsRequest, reader: jspb.BinaryReader): UnreliableItemNotificationsRequest;
}

export namespace UnreliableItemNotificationsRequest {
  export type AsObject = {
  }
}

export class AcknowledgeItemNotificationReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AcknowledgeItemNotificationReply.AsObject;
  static toObject(includeInstance: boolean, msg: AcknowledgeItemNotificationReply): AcknowledgeItemNotificationReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AcknowledgeItemNotificationReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AcknowledgeItemNotificationReply;
  static deserializeBinaryFromReader(message: AcknowledgeItemNotificationReply, reader: jspb.BinaryReader): AcknowledgeItemNotificationReply;
}

export namespace AcknowledgeItemNotificationReply {
  export type AsObject = {
  }
}

export class AcknowledgeItemNotificationRequest extends jspb.Message {
  hasNotificationId(): boolean;
  clearNotificationId(): void;
  getNotificationId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setNotificationId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AcknowledgeItemNotificationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AcknowledgeItemNotificationRequest): AcknowledgeItemNotificationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AcknowledgeItemNotificationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AcknowledgeItemNotificationRequest;
  static deserializeBinaryFromReader(message: AcknowledgeItemNotificationRequest, reader: jspb.BinaryReader): AcknowledgeItemNotificationRequest;
}

export namespace AcknowledgeItemNotificationRequest {
  export type AsObject = {
    notificationId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RegisterForNewItemsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewItemsReply): RegisterForNewItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewItemsReply;
  static deserializeBinaryFromReader(message: RegisterForNewItemsReply, reader: jspb.BinaryReader): RegisterForNewItemsReply;
}

export namespace RegisterForNewItemsReply {
  export type AsObject = {
  }
}

export class RegisterForNewItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForNewItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForNewItemsRequest): RegisterForNewItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForNewItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForNewItemsRequest;
  static deserializeBinaryFromReader(message: RegisterForNewItemsRequest, reader: jspb.BinaryReader): RegisterForNewItemsRequest;
}

export namespace RegisterForNewItemsRequest {
  export type AsObject = {
  }
}

export class RegisterForChangedItemsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedItemsReply): RegisterForChangedItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedItemsReply;
  static deserializeBinaryFromReader(message: RegisterForChangedItemsReply, reader: jspb.BinaryReader): RegisterForChangedItemsReply;
}

export namespace RegisterForChangedItemsReply {
  export type AsObject = {
  }
}

export class RegisterForChangedItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedItemsRequest): RegisterForChangedItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedItemsRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedItemsRequest, reader: jspb.BinaryReader): RegisterForChangedItemsRequest;
}

export namespace RegisterForChangedItemsRequest {
  export type AsObject = {
  }
}

export class RegisterForChangedItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedItemReply): RegisterForChangedItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedItemReply;
  static deserializeBinaryFromReader(message: RegisterForChangedItemReply, reader: jspb.BinaryReader): RegisterForChangedItemReply;
}

export namespace RegisterForChangedItemReply {
  export type AsObject = {
  }
}

export class RegisterForChangedItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForChangedItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForChangedItemRequest): RegisterForChangedItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForChangedItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForChangedItemRequest;
  static deserializeBinaryFromReader(message: RegisterForChangedItemRequest, reader: jspb.BinaryReader): RegisterForChangedItemRequest;
}

export namespace RegisterForChangedItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RegisterForDeletedItemsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedItemsReply): RegisterForDeletedItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedItemsReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedItemsReply, reader: jspb.BinaryReader): RegisterForDeletedItemsReply;
}

export namespace RegisterForDeletedItemsReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedItemsRequest): RegisterForDeletedItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedItemsRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedItemsRequest, reader: jspb.BinaryReader): RegisterForDeletedItemsRequest;
}

export namespace RegisterForDeletedItemsRequest {
  export type AsObject = {
  }
}

export class RegisterForDeletedItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedItemReply): RegisterForDeletedItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedItemReply;
  static deserializeBinaryFromReader(message: RegisterForDeletedItemReply, reader: jspb.BinaryReader): RegisterForDeletedItemReply;
}

export namespace RegisterForDeletedItemReply {
  export type AsObject = {
  }
}

export class RegisterForDeletedItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterForDeletedItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterForDeletedItemRequest): RegisterForDeletedItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterForDeletedItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterForDeletedItemRequest;
  static deserializeBinaryFromReader(message: RegisterForDeletedItemRequest, reader: jspb.BinaryReader): RegisterForDeletedItemRequest;
}

export namespace RegisterForDeletedItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupItemBankMappingsReply extends jspb.Message {
  getCanLookupItemBankMappings(): boolean;
  setCanLookupItemBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupItemBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupItemBankMappingsReply): CanLookupItemBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupItemBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupItemBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupItemBankMappingsReply, reader: jspb.BinaryReader): CanLookupItemBankMappingsReply;
}

export namespace CanLookupItemBankMappingsReply {
  export type AsObject = {
    canLookupItemBankMappings: boolean,
  }
}

export class CanLookupItemBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupItemBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupItemBankMappingsRequest): CanLookupItemBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupItemBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupItemBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupItemBankMappingsRequest, reader: jspb.BinaryReader): CanLookupItemBankMappingsRequest;
}

export namespace CanLookupItemBankMappingsRequest {
  export type AsObject = {
  }
}

export class UseComparativeBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeBankViewReply): UseComparativeBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeBankViewReply;
  static deserializeBinaryFromReader(message: UseComparativeBankViewReply, reader: jspb.BinaryReader): UseComparativeBankViewReply;
}

export namespace UseComparativeBankViewReply {
  export type AsObject = {
  }
}

export class UseComparativeBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeBankViewRequest): UseComparativeBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeBankViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeBankViewRequest, reader: jspb.BinaryReader): UseComparativeBankViewRequest;
}

export namespace UseComparativeBankViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryBankViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryBankViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryBankViewReply): UsePlenaryBankViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryBankViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryBankViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryBankViewReply, reader: jspb.BinaryReader): UsePlenaryBankViewReply;
}

export namespace UsePlenaryBankViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryBankViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryBankViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryBankViewRequest): UsePlenaryBankViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryBankViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryBankViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryBankViewRequest, reader: jspb.BinaryReader): UsePlenaryBankViewRequest;
}

export namespace UsePlenaryBankViewRequest {
  export type AsObject = {
  }
}

export class GetItemIdsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemIdsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemIdsByBankRequest): GetItemIdsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemIdsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemIdsByBankRequest;
  static deserializeBinaryFromReader(message: GetItemIdsByBankRequest, reader: jspb.BinaryReader): GetItemIdsByBankRequest;
}

export namespace GetItemIdsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetItemsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByBankRequest): GetItemsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByBankRequest;
  static deserializeBinaryFromReader(message: GetItemsByBankRequest, reader: jspb.BinaryReader): GetItemsByBankRequest;
}

export namespace GetItemsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetItemIdsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemIdsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemIdsByBanksRequest): GetItemIdsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemIdsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemIdsByBanksRequest;
  static deserializeBinaryFromReader(message: GetItemIdsByBanksRequest, reader: jspb.BinaryReader): GetItemIdsByBanksRequest;
}

export namespace GetItemIdsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetItemsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItemsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItemsByBanksRequest): GetItemsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItemsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItemsByBanksRequest;
  static deserializeBinaryFromReader(message: GetItemsByBanksRequest, reader: jspb.BinaryReader): GetItemsByBanksRequest;
}

export namespace GetItemsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBankIdsByItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdsByItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdsByItemRequest): GetBankIdsByItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdsByItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdsByItemRequest;
  static deserializeBinaryFromReader(message: GetBankIdsByItemRequest, reader: jspb.BinaryReader): GetBankIdsByItemRequest;
}

export namespace GetBankIdsByItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBanksByItemRequest extends jspb.Message {
  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByItemRequest): GetBanksByItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByItemRequest;
  static deserializeBinaryFromReader(message: GetBanksByItemRequest, reader: jspb.BinaryReader): GetBanksByItemRequest;
}

export namespace GetBanksByItemRequest {
  export type AsObject = {
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignItemsReply extends jspb.Message {
  getCanAssignItems(): boolean;
  setCanAssignItems(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignItemsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignItemsReply): CanAssignItemsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignItemsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignItemsReply;
  static deserializeBinaryFromReader(message: CanAssignItemsReply, reader: jspb.BinaryReader): CanAssignItemsReply;
}

export namespace CanAssignItemsReply {
  export type AsObject = {
    canAssignItems: boolean,
  }
}

export class CanAssignItemsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignItemsRequest): CanAssignItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignItemsRequest;
  static deserializeBinaryFromReader(message: CanAssignItemsRequest, reader: jspb.BinaryReader): CanAssignItemsRequest;
}

export namespace CanAssignItemsRequest {
  export type AsObject = {
  }
}

export class CanAssignItemsToBankReply extends jspb.Message {
  getCanAssignItemsToBank(): boolean;
  setCanAssignItemsToBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignItemsToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignItemsToBankReply): CanAssignItemsToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignItemsToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignItemsToBankReply;
  static deserializeBinaryFromReader(message: CanAssignItemsToBankReply, reader: jspb.BinaryReader): CanAssignItemsToBankReply;
}

export namespace CanAssignItemsToBankReply {
  export type AsObject = {
    canAssignItemsToBank: boolean,
  }
}

export class CanAssignItemsToBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignItemsToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignItemsToBankRequest): CanAssignItemsToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignItemsToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignItemsToBankRequest;
  static deserializeBinaryFromReader(message: CanAssignItemsToBankRequest, reader: jspb.BinaryReader): CanAssignItemsToBankRequest;
}

export namespace CanAssignItemsToBankRequest {
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

export class GetAssignableBankIdsForItemRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBankIdsForItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBankIdsForItemRequest): GetAssignableBankIdsForItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBankIdsForItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBankIdsForItemRequest;
  static deserializeBinaryFromReader(message: GetAssignableBankIdsForItemRequest, reader: jspb.BinaryReader): GetAssignableBankIdsForItemRequest;
}

export namespace GetAssignableBankIdsForItemRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignItemToBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignItemToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignItemToBankReply): AssignItemToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignItemToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignItemToBankReply;
  static deserializeBinaryFromReader(message: AssignItemToBankReply, reader: jspb.BinaryReader): AssignItemToBankReply;
}

export namespace AssignItemToBankReply {
  export type AsObject = {
  }
}

export class AssignItemToBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignItemToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignItemToBankRequest): AssignItemToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignItemToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignItemToBankRequest;
  static deserializeBinaryFromReader(message: AssignItemToBankRequest, reader: jspb.BinaryReader): AssignItemToBankRequest;
}

export namespace AssignItemToBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignItemFromBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignItemFromBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignItemFromBankReply): UnassignItemFromBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignItemFromBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignItemFromBankReply;
  static deserializeBinaryFromReader(message: UnassignItemFromBankReply, reader: jspb.BinaryReader): UnassignItemFromBankReply;
}

export namespace UnassignItemFromBankReply {
  export type AsObject = {
  }
}

export class UnassignItemFromBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignItemFromBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignItemFromBankRequest): UnassignItemFromBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignItemFromBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignItemFromBankRequest;
  static deserializeBinaryFromReader(message: UnassignItemFromBankRequest, reader: jspb.BinaryReader): UnassignItemFromBankRequest;
}

export namespace UnassignItemFromBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignItemToBillingReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignItemToBillingReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignItemToBillingReply): ReassignItemToBillingReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignItemToBillingReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignItemToBillingReply;
  static deserializeBinaryFromReader(message: ReassignItemToBillingReply, reader: jspb.BinaryReader): ReassignItemToBillingReply;
}

export namespace ReassignItemToBillingReply {
  export type AsObject = {
  }
}

export class ReassignItemToBillingRequest extends jspb.Message {
  hasFromBankId(): boolean;
  clearFromBankId(): void;
  getFromBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToBankId(): boolean;
  clearToBankId(): void;
  getToBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignItemToBillingRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignItemToBillingRequest): ReassignItemToBillingRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignItemToBillingRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignItemToBillingRequest;
  static deserializeBinaryFromReader(message: ReassignItemToBillingRequest, reader: jspb.BinaryReader): ReassignItemToBillingRequest;
}

export namespace ReassignItemToBillingRequest {
  export type AsObject = {
    fromBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssessmentsReply extends jspb.Message {
  getCanLookupAssessments(): boolean;
  setCanLookupAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentsReply): CanLookupAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentsReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentsReply, reader: jspb.BinaryReader): CanLookupAssessmentsReply;
}

export namespace CanLookupAssessmentsReply {
  export type AsObject = {
    canLookupAssessments: boolean,
  }
}

export class CanLookupAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentsRequest): CanLookupAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentsRequest, reader: jspb.BinaryReader): CanLookupAssessmentsRequest;
}

export namespace CanLookupAssessmentsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentViewReply): UseComparativeAssessmentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentViewReply, reader: jspb.BinaryReader): UseComparativeAssessmentViewReply;
}

export namespace UseComparativeAssessmentViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentViewRequest): UseComparativeAssessmentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentViewRequest, reader: jspb.BinaryReader): UseComparativeAssessmentViewRequest;
}

export namespace UseComparativeAssessmentViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentViewReply): UsePlenaryAssessmentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentViewReply, reader: jspb.BinaryReader): UsePlenaryAssessmentViewReply;
}

export namespace UsePlenaryAssessmentViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentViewRequest): UsePlenaryAssessmentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentViewRequest, reader: jspb.BinaryReader): UsePlenaryAssessmentViewRequest;
}

export namespace UsePlenaryAssessmentViewRequest {
  export type AsObject = {
  }
}

export class GetAssessmentReply extends jspb.Message {
  hasAssessment(): boolean;
  clearAssessment(): void;
  getAssessment(): Assessment | undefined;
  setAssessment(value?: Assessment): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentReply): GetAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentReply;
  static deserializeBinaryFromReader(message: GetAssessmentReply, reader: jspb.BinaryReader): GetAssessmentReply;
}

export namespace GetAssessmentReply {
  export type AsObject = {
    assessment?: Assessment.AsObject,
  }
}

export class GetAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentRequest): GetAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentRequest;
}

export namespace GetAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsByIdsRequest extends jspb.Message {
  clearAssessmentIdsList(): void;
  getAssessmentIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssessmentIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssessmentIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByIdsRequest): GetAssessmentsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByIdsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByIdsRequest, reader: jspb.BinaryReader): GetAssessmentsByIdsRequest;
}

export namespace GetAssessmentsByIdsRequest {
  export type AsObject = {
    assessmentIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentsByGenusTypeRequest extends jspb.Message {
  hasAssessmentGenusType(): boolean;
  clearAssessmentGenusType(): void;
  getAssessmentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByGenusTypeRequest): GetAssessmentsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentsByGenusTypeRequest;
}

export namespace GetAssessmentsByGenusTypeRequest {
  export type AsObject = {
    assessmentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsByParentGenusTypeRequest extends jspb.Message {
  hasAssessmentGenusType(): boolean;
  clearAssessmentGenusType(): void;
  getAssessmentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByParentGenusTypeRequest): GetAssessmentsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentsByParentGenusTypeRequest;
}

export namespace GetAssessmentsByParentGenusTypeRequest {
  export type AsObject = {
    assessmentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsByRecordTypeRequest extends jspb.Message {
  hasAssessmentRecordType(): boolean;
  clearAssessmentRecordType(): void;
  getAssessmentRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByRecordTypeRequest): GetAssessmentsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByRecordTypeRequest, reader: jspb.BinaryReader): GetAssessmentsByRecordTypeRequest;
}

export namespace GetAssessmentsByRecordTypeRequest {
  export type AsObject = {
    assessmentRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsRequest): GetAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsRequest, reader: jspb.BinaryReader): GetAssessmentsRequest;
}

export namespace GetAssessmentsRequest {
  export type AsObject = {
  }
}

export class CanSearchAssessmentsReply extends jspb.Message {
  getCanSearchAssessments(): boolean;
  setCanSearchAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentsReply): CanSearchAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentsReply;
  static deserializeBinaryFromReader(message: CanSearchAssessmentsReply, reader: jspb.BinaryReader): CanSearchAssessmentsReply;
}

export namespace CanSearchAssessmentsReply {
  export type AsObject = {
    canSearchAssessments: boolean,
  }
}

export class CanSearchAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentsRequest): CanSearchAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanSearchAssessmentsRequest, reader: jspb.BinaryReader): CanSearchAssessmentsRequest;
}

export namespace CanSearchAssessmentsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentQueryReply extends jspb.Message {
  hasAssessmentQuery(): boolean;
  clearAssessmentQuery(): void;
  getAssessmentQuery(): AssessmentQuery | undefined;
  setAssessmentQuery(value?: AssessmentQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentQueryReply): GetAssessmentQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentQueryReply;
  static deserializeBinaryFromReader(message: GetAssessmentQueryReply, reader: jspb.BinaryReader): GetAssessmentQueryReply;
}

export namespace GetAssessmentQueryReply {
  export type AsObject = {
    assessmentQuery?: AssessmentQuery.AsObject,
  }
}

export class GetAssessmentQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentQueryRequest): GetAssessmentQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentQueryRequest, reader: jspb.BinaryReader): GetAssessmentQueryRequest;
}

export namespace GetAssessmentQueryRequest {
  export type AsObject = {
  }
}

export class GetAssessmentsByQueryRequest extends jspb.Message {
  hasAssessmentQuery(): boolean;
  clearAssessmentQuery(): void;
  getAssessmentQuery(): AssessmentQuery | undefined;
  setAssessmentQuery(value?: AssessmentQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByQueryRequest): GetAssessmentsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByQueryRequest, reader: jspb.BinaryReader): GetAssessmentsByQueryRequest;
}

export namespace GetAssessmentsByQueryRequest {
  export type AsObject = {
    assessmentQuery?: AssessmentQuery.AsObject,
  }
}

export class CanCreateAssessmentsReply extends jspb.Message {
  getCanCreateAssessments(): boolean;
  setCanCreateAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentsReply): CanCreateAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentsReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentsReply, reader: jspb.BinaryReader): CanCreateAssessmentsReply;
}

export namespace CanCreateAssessmentsReply {
  export type AsObject = {
    canCreateAssessments: boolean,
  }
}

export class CanCreateAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentsRequest): CanCreateAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentsRequest, reader: jspb.BinaryReader): CanCreateAssessmentsRequest;
}

export namespace CanCreateAssessmentsRequest {
  export type AsObject = {
  }
}

export class CanCreateAssessmentWithRecordTypesReply extends jspb.Message {
  getCanCreateAssessmentWithRecordTypes(): boolean;
  setCanCreateAssessmentWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentWithRecordTypesReply): CanCreateAssessmentWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAssessmentWithRecordTypesReply;
}

export namespace CanCreateAssessmentWithRecordTypesReply {
  export type AsObject = {
    canCreateAssessmentWithRecordTypes: boolean,
  }
}

export class CanCreateAssessmentWithRecordTypesRequest extends jspb.Message {
  clearAssessmentRecordTypesList(): void;
  getAssessmentRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentWithRecordTypesRequest): CanCreateAssessmentWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAssessmentWithRecordTypesRequest;
}

export namespace CanCreateAssessmentWithRecordTypesRequest {
  export type AsObject = {
    assessmentRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAssessmentFormForCreateReply extends jspb.Message {
  hasAssessmentForm(): boolean;
  clearAssessmentForm(): void;
  getAssessmentForm(): AssessmentForm | undefined;
  setAssessmentForm(value?: AssessmentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentFormForCreateReply): GetAssessmentFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentFormForCreateReply;
  static deserializeBinaryFromReader(message: GetAssessmentFormForCreateReply, reader: jspb.BinaryReader): GetAssessmentFormForCreateReply;
}

export namespace GetAssessmentFormForCreateReply {
  export type AsObject = {
    assessmentForm?: AssessmentForm.AsObject,
  }
}

export class GetAssessmentFormForCreateRequest extends jspb.Message {
  clearAssessmentRecordTypesList(): void;
  getAssessmentRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentFormForCreateRequest): GetAssessmentFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentFormForCreateRequest, reader: jspb.BinaryReader): GetAssessmentFormForCreateRequest;
}

export namespace GetAssessmentFormForCreateRequest {
  export type AsObject = {
    assessmentRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateAssessmentReply extends jspb.Message {
  hasAssessment(): boolean;
  clearAssessment(): void;
  getAssessment(): Assessment | undefined;
  setAssessment(value?: Assessment): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentReply): CreateAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentReply;
  static deserializeBinaryFromReader(message: CreateAssessmentReply, reader: jspb.BinaryReader): CreateAssessmentReply;
}

export namespace CreateAssessmentReply {
  export type AsObject = {
    assessment?: Assessment.AsObject,
  }
}

export class CreateAssessmentRequest extends jspb.Message {
  hasAssessmentForm(): boolean;
  clearAssessmentForm(): void;
  getAssessmentForm(): AssessmentForm | undefined;
  setAssessmentForm(value?: AssessmentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentRequest): CreateAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentRequest;
  static deserializeBinaryFromReader(message: CreateAssessmentRequest, reader: jspb.BinaryReader): CreateAssessmentRequest;
}

export namespace CreateAssessmentRequest {
  export type AsObject = {
    assessmentForm?: AssessmentForm.AsObject,
  }
}

export class CanUpdateAssessmentsReply extends jspb.Message {
  getCanUpdateAssessments(): boolean;
  setCanUpdateAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentsReply): CanUpdateAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentsReply;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentsReply, reader: jspb.BinaryReader): CanUpdateAssessmentsReply;
}

export namespace CanUpdateAssessmentsReply {
  export type AsObject = {
    canUpdateAssessments: boolean,
  }
}

export class CanUpdateAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentsRequest): CanUpdateAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentsRequest, reader: jspb.BinaryReader): CanUpdateAssessmentsRequest;
}

export namespace CanUpdateAssessmentsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentFormForUpdateReply extends jspb.Message {
  hasAssessmentForm(): boolean;
  clearAssessmentForm(): void;
  getAssessmentForm(): AssessmentForm | undefined;
  setAssessmentForm(value?: AssessmentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentFormForUpdateReply): GetAssessmentFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAssessmentFormForUpdateReply, reader: jspb.BinaryReader): GetAssessmentFormForUpdateReply;
}

export namespace GetAssessmentFormForUpdateReply {
  export type AsObject = {
    assessmentForm?: AssessmentForm.AsObject,
  }
}

export class GetAssessmentFormForUpdateRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentFormForUpdateRequest): GetAssessmentFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentFormForUpdateRequest, reader: jspb.BinaryReader): GetAssessmentFormForUpdateRequest;
}

export namespace GetAssessmentFormForUpdateRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAssessmentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentReply): UpdateAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentReply;
  static deserializeBinaryFromReader(message: UpdateAssessmentReply, reader: jspb.BinaryReader): UpdateAssessmentReply;
}

export namespace UpdateAssessmentReply {
  export type AsObject = {
  }
}

export class UpdateAssessmentRequest extends jspb.Message {
  hasAssessmentForm(): boolean;
  clearAssessmentForm(): void;
  getAssessmentForm(): AssessmentForm | undefined;
  setAssessmentForm(value?: AssessmentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentRequest): UpdateAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentRequest;
  static deserializeBinaryFromReader(message: UpdateAssessmentRequest, reader: jspb.BinaryReader): UpdateAssessmentRequest;
}

export namespace UpdateAssessmentRequest {
  export type AsObject = {
    assessmentForm?: AssessmentForm.AsObject,
  }
}

export class CanDeleteAssessmentsReply extends jspb.Message {
  getCanDeleteAssessments(): boolean;
  setCanDeleteAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentsReply): CanDeleteAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentsReply;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentsReply, reader: jspb.BinaryReader): CanDeleteAssessmentsReply;
}

export namespace CanDeleteAssessmentsReply {
  export type AsObject = {
    canDeleteAssessments: boolean,
  }
}

export class CanDeleteAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentsRequest): CanDeleteAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentsRequest, reader: jspb.BinaryReader): CanDeleteAssessmentsRequest;
}

export namespace CanDeleteAssessmentsRequest {
  export type AsObject = {
  }
}

export class DeleteAssessmentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentReply): DeleteAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentReply;
  static deserializeBinaryFromReader(message: DeleteAssessmentReply, reader: jspb.BinaryReader): DeleteAssessmentReply;
}

export namespace DeleteAssessmentReply {
  export type AsObject = {
  }
}

export class DeleteAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentRequest): DeleteAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentRequest;
  static deserializeBinaryFromReader(message: DeleteAssessmentRequest, reader: jspb.BinaryReader): DeleteAssessmentRequest;
}

export namespace DeleteAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageAssessmentAliasesReply extends jspb.Message {
  getCanManageAssessmentAliases(): boolean;
  setCanManageAssessmentAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentAliasesReply): CanManageAssessmentAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentAliasesReply;
  static deserializeBinaryFromReader(message: CanManageAssessmentAliasesReply, reader: jspb.BinaryReader): CanManageAssessmentAliasesReply;
}

export namespace CanManageAssessmentAliasesReply {
  export type AsObject = {
    canManageAssessmentAliases: boolean,
  }
}

export class CanManageAssessmentAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentAliasesRequest): CanManageAssessmentAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageAssessmentAliasesRequest, reader: jspb.BinaryReader): CanManageAssessmentAliasesRequest;
}

export namespace CanManageAssessmentAliasesRequest {
  export type AsObject = {
  }
}

export class AliasAssessmentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentReply): AliasAssessmentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentReply;
  static deserializeBinaryFromReader(message: AliasAssessmentReply, reader: jspb.BinaryReader): AliasAssessmentReply;
}

export namespace AliasAssessmentReply {
  export type AsObject = {
  }
}

export class AliasAssessmentRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentRequest): AliasAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentRequest;
  static deserializeBinaryFromReader(message: AliasAssessmentRequest, reader: jspb.BinaryReader): AliasAssessmentRequest;
}

export namespace AliasAssessmentRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssessmentBankMappingsReply extends jspb.Message {
  getCanLookupAssessmentBankMappings(): boolean;
  setCanLookupAssessmentBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentBankMappingsReply): CanLookupAssessmentBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentBankMappingsReply, reader: jspb.BinaryReader): CanLookupAssessmentBankMappingsReply;
}

export namespace CanLookupAssessmentBankMappingsReply {
  export type AsObject = {
    canLookupAssessmentBankMappings: boolean,
  }
}

export class CanLookupAssessmentBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentBankMappingsRequest): CanLookupAssessmentBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentBankMappingsRequest, reader: jspb.BinaryReader): CanLookupAssessmentBankMappingsRequest;
}

export namespace CanLookupAssessmentBankMappingsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentIdsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentIdsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentIdsByBankRequest): GetAssessmentIdsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentIdsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentIdsByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentIdsByBankRequest, reader: jspb.BinaryReader): GetAssessmentIdsByBankRequest;
}

export namespace GetAssessmentIdsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByBankRequest): GetAssessmentsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByBankRequest, reader: jspb.BinaryReader): GetAssessmentsByBankRequest;
}

export namespace GetAssessmentsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentIdsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentIdsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentIdsByBanksRequest): GetAssessmentIdsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentIdsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentIdsByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentIdsByBanksRequest, reader: jspb.BinaryReader): GetAssessmentIdsByBanksRequest;
}

export namespace GetAssessmentIdsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsByBanksRequest): GetAssessmentsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsByBanksRequest, reader: jspb.BinaryReader): GetAssessmentsByBanksRequest;
}

export namespace GetAssessmentsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBankIdsByAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdsByAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdsByAssessmentRequest): GetBankIdsByAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdsByAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdsByAssessmentRequest;
  static deserializeBinaryFromReader(message: GetBankIdsByAssessmentRequest, reader: jspb.BinaryReader): GetBankIdsByAssessmentRequest;
}

export namespace GetBankIdsByAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBanksByAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByAssessmentRequest): GetBanksByAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByAssessmentRequest;
  static deserializeBinaryFromReader(message: GetBanksByAssessmentRequest, reader: jspb.BinaryReader): GetBanksByAssessmentRequest;
}

export namespace GetBanksByAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAssessmentsReply extends jspb.Message {
  getCanAssignAssessments(): boolean;
  setCanAssignAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsReply): CanAssignAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsReply, reader: jspb.BinaryReader): CanAssignAssessmentsReply;
}

export namespace CanAssignAssessmentsReply {
  export type AsObject = {
    canAssignAssessments: boolean,
  }
}

export class CanAssignAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsRequest): CanAssignAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsRequest, reader: jspb.BinaryReader): CanAssignAssessmentsRequest;
}

export namespace CanAssignAssessmentsRequest {
  export type AsObject = {
  }
}

export class CanAssignAssessmentsToBankReply extends jspb.Message {
  getCanAssignAssessmentsToBank(): boolean;
  setCanAssignAssessmentsToBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsToBankReply): CanAssignAssessmentsToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsToBankReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsToBankReply, reader: jspb.BinaryReader): CanAssignAssessmentsToBankReply;
}

export namespace CanAssignAssessmentsToBankReply {
  export type AsObject = {
    canAssignAssessmentsToBank: boolean,
  }
}

export class CanAssignAssessmentsToBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsToBankRequest): CanAssignAssessmentsToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsToBankRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsToBankRequest, reader: jspb.BinaryReader): CanAssignAssessmentsToBankRequest;
}

export namespace CanAssignAssessmentsToBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBankIdsForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBankIdsForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBankIdsForAssessmentRequest): GetAssignableBankIdsForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBankIdsForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBankIdsForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssignableBankIdsForAssessmentRequest, reader: jspb.BinaryReader): GetAssignableBankIdsForAssessmentRequest;
}

export namespace GetAssignableBankIdsForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAssessmentToBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentToBankReply): AssignAssessmentToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentToBankReply;
  static deserializeBinaryFromReader(message: AssignAssessmentToBankReply, reader: jspb.BinaryReader): AssignAssessmentToBankReply;
}

export namespace AssignAssessmentToBankReply {
  export type AsObject = {
  }
}

export class AssignAssessmentToBankRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentToBankRequest): AssignAssessmentToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentToBankRequest;
  static deserializeBinaryFromReader(message: AssignAssessmentToBankRequest, reader: jspb.BinaryReader): AssignAssessmentToBankRequest;
}

export namespace AssignAssessmentToBankRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAssessmentFromBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentFromBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentFromBankReply): UnassignAssessmentFromBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentFromBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentFromBankReply;
  static deserializeBinaryFromReader(message: UnassignAssessmentFromBankReply, reader: jspb.BinaryReader): UnassignAssessmentFromBankReply;
}

export namespace UnassignAssessmentFromBankReply {
  export type AsObject = {
  }
}

export class UnassignAssessmentFromBankRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentFromBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentFromBankRequest): UnassignAssessmentFromBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentFromBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentFromBankRequest;
  static deserializeBinaryFromReader(message: UnassignAssessmentFromBankRequest, reader: jspb.BinaryReader): UnassignAssessmentFromBankRequest;
}

export namespace UnassignAssessmentFromBankRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignAssessmentToBillingReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentToBillingReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentToBillingReply): ReassignAssessmentToBillingReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentToBillingReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentToBillingReply;
  static deserializeBinaryFromReader(message: ReassignAssessmentToBillingReply, reader: jspb.BinaryReader): ReassignAssessmentToBillingReply;
}

export namespace ReassignAssessmentToBillingReply {
  export type AsObject = {
  }
}

export class ReassignAssessmentToBillingRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromBankId(): boolean;
  clearFromBankId(): void;
  getFromBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToBankId(): boolean;
  clearToBankId(): void;
  getToBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentToBillingRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentToBillingRequest): ReassignAssessmentToBillingRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentToBillingRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentToBillingRequest;
  static deserializeBinaryFromReader(message: ReassignAssessmentToBillingRequest, reader: jspb.BinaryReader): ReassignAssessmentToBillingRequest;
}

export namespace ReassignAssessmentToBillingRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAuthorAssessmentsReply extends jspb.Message {
  getCanAuthorAssessments(): boolean;
  setCanAuthorAssessments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAuthorAssessmentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAuthorAssessmentsReply): CanAuthorAssessmentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAuthorAssessmentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAuthorAssessmentsReply;
  static deserializeBinaryFromReader(message: CanAuthorAssessmentsReply, reader: jspb.BinaryReader): CanAuthorAssessmentsReply;
}

export namespace CanAuthorAssessmentsReply {
  export type AsObject = {
    canAuthorAssessments: boolean,
  }
}

export class CanAuthorAssessmentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAuthorAssessmentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAuthorAssessmentsRequest): CanAuthorAssessmentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAuthorAssessmentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAuthorAssessmentsRequest;
  static deserializeBinaryFromReader(message: CanAuthorAssessmentsRequest, reader: jspb.BinaryReader): CanAuthorAssessmentsRequest;
}

export namespace CanAuthorAssessmentsRequest {
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
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
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
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class MoveItemReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveItemReply.AsObject;
  static toObject(includeInstance: boolean, msg: MoveItemReply): MoveItemReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveItemReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveItemReply;
  static deserializeBinaryFromReader(message: MoveItemReply, reader: jspb.BinaryReader): MoveItemReply;
}

export namespace MoveItemReply {
  export type AsObject = {
  }
}

export class MoveItemRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasItemId(): boolean;
  clearItemId(): void;
  getItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasPreceedingItemId(): boolean;
  clearPreceedingItemId(): void;
  getPreceedingItemId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setPreceedingItemId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MoveItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: MoveItemRequest): MoveItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MoveItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MoveItemRequest;
  static deserializeBinaryFromReader(message: MoveItemRequest, reader: jspb.BinaryReader): MoveItemRequest;
}

export namespace MoveItemRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    preceedingItemId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
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
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    itemIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class CanLookupAssessmentsOfferedReply extends jspb.Message {
  getCanLookupAssessmentsOffered(): boolean;
  setCanLookupAssessmentsOffered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentsOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentsOfferedReply): CanLookupAssessmentsOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentsOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentsOfferedReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentsOfferedReply, reader: jspb.BinaryReader): CanLookupAssessmentsOfferedReply;
}

export namespace CanLookupAssessmentsOfferedReply {
  export type AsObject = {
    canLookupAssessmentsOffered: boolean,
  }
}

export class CanLookupAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentsOfferedRequest): CanLookupAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentsOfferedRequest, reader: jspb.BinaryReader): CanLookupAssessmentsOfferedRequest;
}

export namespace CanLookupAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentOfferedViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentOfferedViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentOfferedViewReply): UseComparativeAssessmentOfferedViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentOfferedViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentOfferedViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentOfferedViewReply, reader: jspb.BinaryReader): UseComparativeAssessmentOfferedViewReply;
}

export namespace UseComparativeAssessmentOfferedViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentOfferedViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentOfferedViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentOfferedViewRequest): UseComparativeAssessmentOfferedViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentOfferedViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentOfferedViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentOfferedViewRequest, reader: jspb.BinaryReader): UseComparativeAssessmentOfferedViewRequest;
}

export namespace UseComparativeAssessmentOfferedViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentOfferedViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentOfferedViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentOfferedViewReply): UsePlenaryAssessmentOfferedViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentOfferedViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentOfferedViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentOfferedViewReply, reader: jspb.BinaryReader): UsePlenaryAssessmentOfferedViewReply;
}

export namespace UsePlenaryAssessmentOfferedViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentOfferedViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentOfferedViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentOfferedViewRequest): UsePlenaryAssessmentOfferedViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentOfferedViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentOfferedViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentOfferedViewRequest, reader: jspb.BinaryReader): UsePlenaryAssessmentOfferedViewRequest;
}

export namespace UsePlenaryAssessmentOfferedViewRequest {
  export type AsObject = {
  }
}

export class GetAssessmentOfferedReply extends jspb.Message {
  hasAssessmentOffered(): boolean;
  clearAssessmentOffered(): void;
  getAssessmentOffered(): AssessmentOffered | undefined;
  setAssessmentOffered(value?: AssessmentOffered): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedReply): GetAssessmentOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedReply;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedReply, reader: jspb.BinaryReader): GetAssessmentOfferedReply;
}

export namespace GetAssessmentOfferedReply {
  export type AsObject = {
    assessmentOffered?: AssessmentOffered.AsObject,
  }
}

export class GetAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedRequest): GetAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedRequest, reader: jspb.BinaryReader): GetAssessmentOfferedRequest;
}

export namespace GetAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsOfferedByIdsRequest extends jspb.Message {
  clearAssessmentOfferedIdsList(): void;
  getAssessmentOfferedIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssessmentOfferedIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssessmentOfferedIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByIdsRequest): GetAssessmentsOfferedByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByIdsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByIdsRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByIdsRequest;
}

export namespace GetAssessmentsOfferedByIdsRequest {
  export type AsObject = {
    assessmentOfferedIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentsOfferedByGenusTypeRequest extends jspb.Message {
  hasAssessmentOfferedGenusType(): boolean;
  clearAssessmentOfferedGenusType(): void;
  getAssessmentOfferedGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentOfferedGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByGenusTypeRequest): GetAssessmentsOfferedByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByGenusTypeRequest;
}

export namespace GetAssessmentsOfferedByGenusTypeRequest {
  export type AsObject = {
    assessmentOfferedGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsOfferedByParentGenusTypeRequest extends jspb.Message {
  hasAssessmentOfferedGenusType(): boolean;
  clearAssessmentOfferedGenusType(): void;
  getAssessmentOfferedGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentOfferedGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByParentGenusTypeRequest): GetAssessmentsOfferedByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByParentGenusTypeRequest;
}

export namespace GetAssessmentsOfferedByParentGenusTypeRequest {
  export type AsObject = {
    assessmentOfferedGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsOfferedByRecordTypeRequest extends jspb.Message {
  hasAssessmentRecordType(): boolean;
  clearAssessmentRecordType(): void;
  getAssessmentRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByRecordTypeRequest): GetAssessmentsOfferedByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByRecordTypeRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByRecordTypeRequest;
}

export namespace GetAssessmentsOfferedByRecordTypeRequest {
  export type AsObject = {
    assessmentRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsOfferedByDateRequest extends jspb.Message {
  hasEnd(): boolean;
  clearEnd(): void;
  getEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasStart(): boolean;
  clearStart(): void;
  getStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByDateRequest): GetAssessmentsOfferedByDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByDateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByDateRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByDateRequest;
}

export namespace GetAssessmentsOfferedByDateRequest {
  export type AsObject = {
    end?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    start?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsOfferedForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedForAssessmentRequest): GetAssessmentsOfferedForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedForAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedForAssessmentRequest;
}

export namespace GetAssessmentsOfferedForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedRequest): GetAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedRequest;
}

export namespace GetAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class CanSearchAssessmentsOfferedReply extends jspb.Message {
  getCanSearchAssessmentsOffered(): boolean;
  setCanSearchAssessmentsOffered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentsOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentsOfferedReply): CanSearchAssessmentsOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentsOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentsOfferedReply;
  static deserializeBinaryFromReader(message: CanSearchAssessmentsOfferedReply, reader: jspb.BinaryReader): CanSearchAssessmentsOfferedReply;
}

export namespace CanSearchAssessmentsOfferedReply {
  export type AsObject = {
    canSearchAssessmentsOffered: boolean,
  }
}

export class CanSearchAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentsOfferedRequest): CanSearchAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: CanSearchAssessmentsOfferedRequest, reader: jspb.BinaryReader): CanSearchAssessmentsOfferedRequest;
}

export namespace CanSearchAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class GetAssessmentOfferedQueryReply extends jspb.Message {
  hasAssessmentOfferedQuery(): boolean;
  clearAssessmentOfferedQuery(): void;
  getAssessmentOfferedQuery(): AssessmentOfferedQuery | undefined;
  setAssessmentOfferedQuery(value?: AssessmentOfferedQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedQueryReply): GetAssessmentOfferedQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedQueryReply;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedQueryReply, reader: jspb.BinaryReader): GetAssessmentOfferedQueryReply;
}

export namespace GetAssessmentOfferedQueryReply {
  export type AsObject = {
    assessmentOfferedQuery?: AssessmentOfferedQuery.AsObject,
  }
}

export class GetAssessmentOfferedQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedQueryRequest): GetAssessmentOfferedQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedQueryRequest, reader: jspb.BinaryReader): GetAssessmentOfferedQueryRequest;
}

export namespace GetAssessmentOfferedQueryRequest {
  export type AsObject = {
  }
}

export class GetAssessmentsOfferedByQueryRequest extends jspb.Message {
  hasAssessmentOfferedQuery(): boolean;
  clearAssessmentOfferedQuery(): void;
  getAssessmentOfferedQuery(): AssessmentOfferedQuery | undefined;
  setAssessmentOfferedQuery(value?: AssessmentOfferedQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByQueryRequest): GetAssessmentsOfferedByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByQueryRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByQueryRequest;
}

export namespace GetAssessmentsOfferedByQueryRequest {
  export type AsObject = {
    assessmentOfferedQuery?: AssessmentOfferedQuery.AsObject,
  }
}

export class CanCreateAssessmentsOfferedReply extends jspb.Message {
  getCanCreateAssessmentsOffered(): boolean;
  setCanCreateAssessmentsOffered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentsOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentsOfferedReply): CanCreateAssessmentsOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentsOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentsOfferedReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentsOfferedReply, reader: jspb.BinaryReader): CanCreateAssessmentsOfferedReply;
}

export namespace CanCreateAssessmentsOfferedReply {
  export type AsObject = {
    canCreateAssessmentsOffered: boolean,
  }
}

export class CanCreateAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentsOfferedRequest): CanCreateAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentsOfferedRequest, reader: jspb.BinaryReader): CanCreateAssessmentsOfferedRequest;
}

export namespace CanCreateAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class CanCreateAssessmentOfferedWithRecordTypesReply extends jspb.Message {
  getCanCreateAssessmentOfferedWithRecordTypes(): boolean;
  setCanCreateAssessmentOfferedWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentOfferedWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentOfferedWithRecordTypesReply): CanCreateAssessmentOfferedWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentOfferedWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentOfferedWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentOfferedWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAssessmentOfferedWithRecordTypesReply;
}

export namespace CanCreateAssessmentOfferedWithRecordTypesReply {
  export type AsObject = {
    canCreateAssessmentOfferedWithRecordTypes: boolean,
  }
}

export class CanCreateAssessmentOfferedWithRecordTypesRequest extends jspb.Message {
  clearAssessmentOfferedRecordTypesList(): void;
  getAssessmentOfferedRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentOfferedRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentOfferedRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentOfferedWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentOfferedWithRecordTypesRequest): CanCreateAssessmentOfferedWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentOfferedWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentOfferedWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentOfferedWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAssessmentOfferedWithRecordTypesRequest;
}

export namespace CanCreateAssessmentOfferedWithRecordTypesRequest {
  export type AsObject = {
    assessmentOfferedRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAssessmentOfferedFormForCreateReply extends jspb.Message {
  hasAssessmentOfferedForm(): boolean;
  clearAssessmentOfferedForm(): void;
  getAssessmentOfferedForm(): AssessmentOfferedForm | undefined;
  setAssessmentOfferedForm(value?: AssessmentOfferedForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedFormForCreateReply): GetAssessmentOfferedFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedFormForCreateReply;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedFormForCreateReply, reader: jspb.BinaryReader): GetAssessmentOfferedFormForCreateReply;
}

export namespace GetAssessmentOfferedFormForCreateReply {
  export type AsObject = {
    assessmentOfferedForm?: AssessmentOfferedForm.AsObject,
  }
}

export class GetAssessmentOfferedFormForCreateRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearAssessmentOfferedRecordTypesList(): void;
  getAssessmentOfferedRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentOfferedRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentOfferedRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedFormForCreateRequest): GetAssessmentOfferedFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedFormForCreateRequest, reader: jspb.BinaryReader): GetAssessmentOfferedFormForCreateRequest;
}

export namespace GetAssessmentOfferedFormForCreateRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentOfferedRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateAssessmentOfferedReply extends jspb.Message {
  hasAssessmentOffered(): boolean;
  clearAssessmentOffered(): void;
  getAssessmentOffered(): AssessmentOffered | undefined;
  setAssessmentOffered(value?: AssessmentOffered): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentOfferedReply): CreateAssessmentOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentOfferedReply;
  static deserializeBinaryFromReader(message: CreateAssessmentOfferedReply, reader: jspb.BinaryReader): CreateAssessmentOfferedReply;
}

export namespace CreateAssessmentOfferedReply {
  export type AsObject = {
    assessmentOffered?: AssessmentOffered.AsObject,
  }
}

export class CreateAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedForm(): boolean;
  clearAssessmentOfferedForm(): void;
  getAssessmentOfferedForm(): AssessmentOfferedForm | undefined;
  setAssessmentOfferedForm(value?: AssessmentOfferedForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentOfferedRequest): CreateAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: CreateAssessmentOfferedRequest, reader: jspb.BinaryReader): CreateAssessmentOfferedRequest;
}

export namespace CreateAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedForm?: AssessmentOfferedForm.AsObject,
  }
}

export class CanUpdateAssessmentsOfferedReply extends jspb.Message {
  getCanUpdateAssessmentsOffered(): boolean;
  setCanUpdateAssessmentsOffered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentsOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentsOfferedReply): CanUpdateAssessmentsOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentsOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentsOfferedReply;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentsOfferedReply, reader: jspb.BinaryReader): CanUpdateAssessmentsOfferedReply;
}

export namespace CanUpdateAssessmentsOfferedReply {
  export type AsObject = {
    canUpdateAssessmentsOffered: boolean,
  }
}

export class CanUpdateAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentsOfferedRequest): CanUpdateAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentsOfferedRequest, reader: jspb.BinaryReader): CanUpdateAssessmentsOfferedRequest;
}

export namespace CanUpdateAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class GetAssessmentOfferedFormForUpdateReply extends jspb.Message {
  hasAssessmentOfferedForm(): boolean;
  clearAssessmentOfferedForm(): void;
  getAssessmentOfferedForm(): AssessmentOfferedForm | undefined;
  setAssessmentOfferedForm(value?: AssessmentOfferedForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedFormForUpdateReply): GetAssessmentOfferedFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedFormForUpdateReply, reader: jspb.BinaryReader): GetAssessmentOfferedFormForUpdateReply;
}

export namespace GetAssessmentOfferedFormForUpdateReply {
  export type AsObject = {
    assessmentOfferedForm?: AssessmentOfferedForm.AsObject,
  }
}

export class GetAssessmentOfferedFormForUpdateRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedFormForUpdateRequest): GetAssessmentOfferedFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedFormForUpdateRequest, reader: jspb.BinaryReader): GetAssessmentOfferedFormForUpdateRequest;
}

export namespace GetAssessmentOfferedFormForUpdateRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAssessmentOfferedReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentOfferedReply): UpdateAssessmentOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentOfferedReply;
  static deserializeBinaryFromReader(message: UpdateAssessmentOfferedReply, reader: jspb.BinaryReader): UpdateAssessmentOfferedReply;
}

export namespace UpdateAssessmentOfferedReply {
  export type AsObject = {
  }
}

export class UpdateAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedForm(): boolean;
  clearAssessmentOfferedForm(): void;
  getAssessmentOfferedForm(): AssessmentOfferedForm | undefined;
  setAssessmentOfferedForm(value?: AssessmentOfferedForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentOfferedRequest): UpdateAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: UpdateAssessmentOfferedRequest, reader: jspb.BinaryReader): UpdateAssessmentOfferedRequest;
}

export namespace UpdateAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedForm?: AssessmentOfferedForm.AsObject,
  }
}

export class CanDeleteAssessmentsOfferedReply extends jspb.Message {
  getCanDeleteAssessmentsOffered(): boolean;
  setCanDeleteAssessmentsOffered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentsOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentsOfferedReply): CanDeleteAssessmentsOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentsOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentsOfferedReply;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentsOfferedReply, reader: jspb.BinaryReader): CanDeleteAssessmentsOfferedReply;
}

export namespace CanDeleteAssessmentsOfferedReply {
  export type AsObject = {
    canDeleteAssessmentsOffered: boolean,
  }
}

export class CanDeleteAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentsOfferedRequest): CanDeleteAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentsOfferedRequest, reader: jspb.BinaryReader): CanDeleteAssessmentsOfferedRequest;
}

export namespace CanDeleteAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class DeleteAssessmentOfferedReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentOfferedReply): DeleteAssessmentOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentOfferedReply;
  static deserializeBinaryFromReader(message: DeleteAssessmentOfferedReply, reader: jspb.BinaryReader): DeleteAssessmentOfferedReply;
}

export namespace DeleteAssessmentOfferedReply {
  export type AsObject = {
  }
}

export class DeleteAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentOfferedRequest): DeleteAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: DeleteAssessmentOfferedRequest, reader: jspb.BinaryReader): DeleteAssessmentOfferedRequest;
}

export namespace DeleteAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageAssessmentOfferedAliasesReply extends jspb.Message {
  getCanManageAssessmentOfferedAliases(): boolean;
  setCanManageAssessmentOfferedAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentOfferedAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentOfferedAliasesReply): CanManageAssessmentOfferedAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentOfferedAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentOfferedAliasesReply;
  static deserializeBinaryFromReader(message: CanManageAssessmentOfferedAliasesReply, reader: jspb.BinaryReader): CanManageAssessmentOfferedAliasesReply;
}

export namespace CanManageAssessmentOfferedAliasesReply {
  export type AsObject = {
    canManageAssessmentOfferedAliases: boolean,
  }
}

export class CanManageAssessmentOfferedAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentOfferedAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentOfferedAliasesRequest): CanManageAssessmentOfferedAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentOfferedAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentOfferedAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageAssessmentOfferedAliasesRequest, reader: jspb.BinaryReader): CanManageAssessmentOfferedAliasesRequest;
}

export namespace CanManageAssessmentOfferedAliasesRequest {
  export type AsObject = {
  }
}

export class AliasAssessmentOfferedReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentOfferedReply): AliasAssessmentOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentOfferedReply;
  static deserializeBinaryFromReader(message: AliasAssessmentOfferedReply, reader: jspb.BinaryReader): AliasAssessmentOfferedReply;
}

export namespace AliasAssessmentOfferedReply {
  export type AsObject = {
  }
}

export class AliasAssessmentOfferedRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentOfferedRequest): AliasAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: AliasAssessmentOfferedRequest, reader: jspb.BinaryReader): AliasAssessmentOfferedRequest;
}

export namespace AliasAssessmentOfferedRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssessmentOfferedBankMappingsReply extends jspb.Message {
  getCanLookupAssessmentOfferedBankMappings(): boolean;
  setCanLookupAssessmentOfferedBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentOfferedBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentOfferedBankMappingsReply): CanLookupAssessmentOfferedBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentOfferedBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentOfferedBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentOfferedBankMappingsReply, reader: jspb.BinaryReader): CanLookupAssessmentOfferedBankMappingsReply;
}

export namespace CanLookupAssessmentOfferedBankMappingsReply {
  export type AsObject = {
    canLookupAssessmentOfferedBankMappings: boolean,
  }
}

export class CanLookupAssessmentOfferedBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentOfferedBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentOfferedBankMappingsRequest): CanLookupAssessmentOfferedBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentOfferedBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentOfferedBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentOfferedBankMappingsRequest, reader: jspb.BinaryReader): CanLookupAssessmentOfferedBankMappingsRequest;
}

export namespace CanLookupAssessmentOfferedBankMappingsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentOfferedIdsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedIdsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedIdsByBankRequest): GetAssessmentOfferedIdsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedIdsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedIdsByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedIdsByBankRequest, reader: jspb.BinaryReader): GetAssessmentOfferedIdsByBankRequest;
}

export namespace GetAssessmentOfferedIdsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsOfferedByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByBankRequest): GetAssessmentsOfferedByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByBankRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByBankRequest;
}

export namespace GetAssessmentsOfferedByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentOfferedIdsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentOfferedIdsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentOfferedIdsByBanksRequest): GetAssessmentOfferedIdsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentOfferedIdsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentOfferedIdsByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentOfferedIdsByBanksRequest, reader: jspb.BinaryReader): GetAssessmentOfferedIdsByBanksRequest;
}

export namespace GetAssessmentOfferedIdsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentsOfferedByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsOfferedByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsOfferedByBanksRequest): GetAssessmentsOfferedByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsOfferedByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsOfferedByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsOfferedByBanksRequest, reader: jspb.BinaryReader): GetAssessmentsOfferedByBanksRequest;
}

export namespace GetAssessmentsOfferedByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBankIdsByAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdsByAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdsByAssessmentOfferedRequest): GetBankIdsByAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdsByAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdsByAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetBankIdsByAssessmentOfferedRequest, reader: jspb.BinaryReader): GetBankIdsByAssessmentOfferedRequest;
}

export namespace GetBankIdsByAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBanksByAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByAssessmentOfferedRequest): GetBanksByAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetBanksByAssessmentOfferedRequest, reader: jspb.BinaryReader): GetBanksByAssessmentOfferedRequest;
}

export namespace GetBanksByAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAssessmentsOfferedReply extends jspb.Message {
  getCanAssignAssessmentsOffered(): boolean;
  setCanAssignAssessmentsOffered(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsOfferedReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsOfferedReply): CanAssignAssessmentsOfferedReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsOfferedReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsOfferedReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsOfferedReply, reader: jspb.BinaryReader): CanAssignAssessmentsOfferedReply;
}

export namespace CanAssignAssessmentsOfferedReply {
  export type AsObject = {
    canAssignAssessmentsOffered: boolean,
  }
}

export class CanAssignAssessmentsOfferedRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsOfferedRequest): CanAssignAssessmentsOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsOfferedRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsOfferedRequest, reader: jspb.BinaryReader): CanAssignAssessmentsOfferedRequest;
}

export namespace CanAssignAssessmentsOfferedRequest {
  export type AsObject = {
  }
}

export class CanAssignAssessmentsOfferedToBankReply extends jspb.Message {
  getCanAssignAssessmentsOfferedToBank(): boolean;
  setCanAssignAssessmentsOfferedToBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsOfferedToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsOfferedToBankReply): CanAssignAssessmentsOfferedToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsOfferedToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsOfferedToBankReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsOfferedToBankReply, reader: jspb.BinaryReader): CanAssignAssessmentsOfferedToBankReply;
}

export namespace CanAssignAssessmentsOfferedToBankReply {
  export type AsObject = {
    canAssignAssessmentsOfferedToBank: boolean,
  }
}

export class CanAssignAssessmentsOfferedToBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsOfferedToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsOfferedToBankRequest): CanAssignAssessmentsOfferedToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsOfferedToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsOfferedToBankRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsOfferedToBankRequest, reader: jspb.BinaryReader): CanAssignAssessmentsOfferedToBankRequest;
}

export namespace CanAssignAssessmentsOfferedToBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBankIdsForAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBankIdsForAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBankIdsForAssessmentOfferedRequest): GetAssignableBankIdsForAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBankIdsForAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBankIdsForAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssignableBankIdsForAssessmentOfferedRequest, reader: jspb.BinaryReader): GetAssignableBankIdsForAssessmentOfferedRequest;
}

export namespace GetAssignableBankIdsForAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAssessmentOfferedToBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentOfferedToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentOfferedToBankReply): AssignAssessmentOfferedToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentOfferedToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentOfferedToBankReply;
  static deserializeBinaryFromReader(message: AssignAssessmentOfferedToBankReply, reader: jspb.BinaryReader): AssignAssessmentOfferedToBankReply;
}

export namespace AssignAssessmentOfferedToBankReply {
  export type AsObject = {
  }
}

export class AssignAssessmentOfferedToBankRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentOfferedToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentOfferedToBankRequest): AssignAssessmentOfferedToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentOfferedToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentOfferedToBankRequest;
  static deserializeBinaryFromReader(message: AssignAssessmentOfferedToBankRequest, reader: jspb.BinaryReader): AssignAssessmentOfferedToBankRequest;
}

export namespace AssignAssessmentOfferedToBankRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAssessmentOfferedFromBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentOfferedFromBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentOfferedFromBankReply): UnassignAssessmentOfferedFromBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentOfferedFromBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentOfferedFromBankReply;
  static deserializeBinaryFromReader(message: UnassignAssessmentOfferedFromBankReply, reader: jspb.BinaryReader): UnassignAssessmentOfferedFromBankReply;
}

export namespace UnassignAssessmentOfferedFromBankReply {
  export type AsObject = {
  }
}

export class UnassignAssessmentOfferedFromBankRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentOfferedFromBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentOfferedFromBankRequest): UnassignAssessmentOfferedFromBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentOfferedFromBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentOfferedFromBankRequest;
  static deserializeBinaryFromReader(message: UnassignAssessmentOfferedFromBankRequest, reader: jspb.BinaryReader): UnassignAssessmentOfferedFromBankRequest;
}

export namespace UnassignAssessmentOfferedFromBankRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignAssessmentOfferedToBillingReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentOfferedToBillingReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentOfferedToBillingReply): ReassignAssessmentOfferedToBillingReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentOfferedToBillingReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentOfferedToBillingReply;
  static deserializeBinaryFromReader(message: ReassignAssessmentOfferedToBillingReply, reader: jspb.BinaryReader): ReassignAssessmentOfferedToBillingReply;
}

export namespace ReassignAssessmentOfferedToBillingReply {
  export type AsObject = {
  }
}

export class ReassignAssessmentOfferedToBillingRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromBankId(): boolean;
  clearFromBankId(): void;
  getFromBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToBankId(): boolean;
  clearToBankId(): void;
  getToBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentOfferedToBillingRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentOfferedToBillingRequest): ReassignAssessmentOfferedToBillingRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentOfferedToBillingRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentOfferedToBillingRequest;
  static deserializeBinaryFromReader(message: ReassignAssessmentOfferedToBillingRequest, reader: jspb.BinaryReader): ReassignAssessmentOfferedToBillingRequest;
}

export namespace ReassignAssessmentOfferedToBillingRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssessmentsTakenReply extends jspb.Message {
  getCanLookupAssessmentsTaken(): boolean;
  setCanLookupAssessmentsTaken(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentsTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentsTakenReply): CanLookupAssessmentsTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentsTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentsTakenReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentsTakenReply, reader: jspb.BinaryReader): CanLookupAssessmentsTakenReply;
}

export namespace CanLookupAssessmentsTakenReply {
  export type AsObject = {
    canLookupAssessmentsTaken: boolean,
  }
}

export class CanLookupAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentsTakenRequest): CanLookupAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentsTakenRequest, reader: jspb.BinaryReader): CanLookupAssessmentsTakenRequest;
}

export namespace CanLookupAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentTakenViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentTakenViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentTakenViewReply): UseComparativeAssessmentTakenViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentTakenViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentTakenViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentTakenViewReply, reader: jspb.BinaryReader): UseComparativeAssessmentTakenViewReply;
}

export namespace UseComparativeAssessmentTakenViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAssessmentTakenViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAssessmentTakenViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAssessmentTakenViewRequest): UseComparativeAssessmentTakenViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAssessmentTakenViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAssessmentTakenViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAssessmentTakenViewRequest, reader: jspb.BinaryReader): UseComparativeAssessmentTakenViewRequest;
}

export namespace UseComparativeAssessmentTakenViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentTakenViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentTakenViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentTakenViewReply): UsePlenaryAssessmentTakenViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentTakenViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentTakenViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentTakenViewReply, reader: jspb.BinaryReader): UsePlenaryAssessmentTakenViewReply;
}

export namespace UsePlenaryAssessmentTakenViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAssessmentTakenViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAssessmentTakenViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAssessmentTakenViewRequest): UsePlenaryAssessmentTakenViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAssessmentTakenViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAssessmentTakenViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAssessmentTakenViewRequest, reader: jspb.BinaryReader): UsePlenaryAssessmentTakenViewRequest;
}

export namespace UsePlenaryAssessmentTakenViewRequest {
  export type AsObject = {
  }
}

export class GetAssessmentTakenReply extends jspb.Message {
  hasAssessmentTaken(): boolean;
  clearAssessmentTaken(): void;
  getAssessmentTaken(): AssessmentTaken | undefined;
  setAssessmentTaken(value?: AssessmentTaken): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenReply): GetAssessmentTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenReply;
  static deserializeBinaryFromReader(message: GetAssessmentTakenReply, reader: jspb.BinaryReader): GetAssessmentTakenReply;
}

export namespace GetAssessmentTakenReply {
  export type AsObject = {
    assessmentTaken?: AssessmentTaken.AsObject,
  }
}

export class GetAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenRequest): GetAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: GetAssessmentTakenRequest, reader: jspb.BinaryReader): GetAssessmentTakenRequest;
}

export namespace GetAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByIdsRequest extends jspb.Message {
  clearAssessmentTakenIdsList(): void;
  getAssessmentTakenIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAssessmentTakenIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAssessmentTakenIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByIdsRequest): GetAssessmentsTakenByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByIdsRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByIdsRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByIdsRequest;
}

export namespace GetAssessmentsTakenByIdsRequest {
  export type AsObject = {
    assessmentTakenIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentsTakenByGenusTypeRequest extends jspb.Message {
  hasAssessmentTakenGenusType(): boolean;
  clearAssessmentTakenGenusType(): void;
  getAssessmentTakenGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentTakenGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByGenusTypeRequest): GetAssessmentsTakenByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByGenusTypeRequest;
}

export namespace GetAssessmentsTakenByGenusTypeRequest {
  export type AsObject = {
    assessmentTakenGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsTakenByParentGenusTypeRequest extends jspb.Message {
  hasAssessmentTakenGenusType(): boolean;
  clearAssessmentTakenGenusType(): void;
  getAssessmentTakenGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentTakenGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByParentGenusTypeRequest): GetAssessmentsTakenByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByParentGenusTypeRequest;
}

export namespace GetAssessmentsTakenByParentGenusTypeRequest {
  export type AsObject = {
    assessmentTakenGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsTakenByRecordTypeRequest extends jspb.Message {
  hasAssessmentTakenRecordType(): boolean;
  clearAssessmentTakenRecordType(): void;
  getAssessmentTakenRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAssessmentTakenRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByRecordTypeRequest): GetAssessmentsTakenByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByRecordTypeRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByRecordTypeRequest;
}

export namespace GetAssessmentsTakenByRecordTypeRequest {
  export type AsObject = {
    assessmentTakenRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAssessmentsTakenByDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByDateRequest): GetAssessmentsTakenByDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByDateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByDateRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByDateRequest;
}

export namespace GetAssessmentsTakenByDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsTakenForTakerRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenForTakerRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenForTakerRequest): GetAssessmentsTakenForTakerRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenForTakerRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenForTakerRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenForTakerRequest, reader: jspb.BinaryReader): GetAssessmentsTakenForTakerRequest;
}

export namespace GetAssessmentsTakenForTakerRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByDateForTakerRequest extends jspb.Message {
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
  toObject(includeInstance?: boolean): GetAssessmentsTakenByDateForTakerRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByDateForTakerRequest): GetAssessmentsTakenByDateForTakerRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByDateForTakerRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByDateForTakerRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByDateForTakerRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByDateForTakerRequest;
}

export namespace GetAssessmentsTakenByDateForTakerRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsTakenForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenForAssessmentRequest): GetAssessmentsTakenForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenForAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentsTakenForAssessmentRequest;
}

export namespace GetAssessmentsTakenForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByDateForAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByDateForAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByDateForAssessmentRequest): GetAssessmentsTakenByDateForAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByDateForAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByDateForAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByDateForAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByDateForAssessmentRequest;
}

export namespace GetAssessmentsTakenByDateForAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsTakenForTakerAndAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenForTakerAndAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenForTakerAndAssessmentRequest): GetAssessmentsTakenForTakerAndAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenForTakerAndAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenForTakerAndAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenForTakerAndAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentsTakenForTakerAndAssessmentRequest;
}

export namespace GetAssessmentsTakenForTakerAndAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByDateForTakerAndAssessmentRequest extends jspb.Message {
  hasAssessmentId(): boolean;
  clearAssessmentId(): void;
  getAssessmentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
  toObject(includeInstance?: boolean): GetAssessmentsTakenByDateForTakerAndAssessmentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByDateForTakerAndAssessmentRequest): GetAssessmentsTakenByDateForTakerAndAssessmentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByDateForTakerAndAssessmentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByDateForTakerAndAssessmentRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByDateForTakerAndAssessmentRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByDateForTakerAndAssessmentRequest;
}

export namespace GetAssessmentsTakenByDateForTakerAndAssessmentRequest {
  export type AsObject = {
    assessmentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsTakenForAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenForAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenForAssessmentOfferedRequest): GetAssessmentsTakenForAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenForAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenForAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenForAssessmentOfferedRequest, reader: jspb.BinaryReader): GetAssessmentsTakenForAssessmentOfferedRequest;
}

export namespace GetAssessmentsTakenForAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByDateForAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByDateForAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByDateForAssessmentOfferedRequest): GetAssessmentsTakenByDateForAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByDateForAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByDateForAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByDateForAssessmentOfferedRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByDateForAssessmentOfferedRequest;
}

export namespace GetAssessmentsTakenByDateForAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsTakenForTakerAndAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenForTakerAndAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenForTakerAndAssessmentOfferedRequest): GetAssessmentsTakenForTakerAndAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenForTakerAndAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenForTakerAndAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenForTakerAndAssessmentOfferedRequest, reader: jspb.BinaryReader): GetAssessmentsTakenForTakerAndAssessmentOfferedRequest;
}

export namespace GetAssessmentsTakenForTakerAndAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

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
  toObject(includeInstance?: boolean): GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest): GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest;
}

export namespace GetAssessmentsTakenByDateForTakerAndAssessmentOfferedRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenRequest): GetAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenRequest, reader: jspb.BinaryReader): GetAssessmentsTakenRequest;
}

export namespace GetAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class CanSearchAssessmentsTakenReply extends jspb.Message {
  getCanSearchAssessmentsTaken(): boolean;
  setCanSearchAssessmentsTaken(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentsTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentsTakenReply): CanSearchAssessmentsTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentsTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentsTakenReply;
  static deserializeBinaryFromReader(message: CanSearchAssessmentsTakenReply, reader: jspb.BinaryReader): CanSearchAssessmentsTakenReply;
}

export namespace CanSearchAssessmentsTakenReply {
  export type AsObject = {
    canSearchAssessmentsTaken: boolean,
  }
}

export class CanSearchAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchAssessmentsTakenRequest): CanSearchAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: CanSearchAssessmentsTakenRequest, reader: jspb.BinaryReader): CanSearchAssessmentsTakenRequest;
}

export namespace CanSearchAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class GetAssessmentTakenQueryReply extends jspb.Message {
  hasAssessmentTakenQuery(): boolean;
  clearAssessmentTakenQuery(): void;
  getAssessmentTakenQuery(): AssessmentTakenQuery | undefined;
  setAssessmentTakenQuery(value?: AssessmentTakenQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenQueryReply): GetAssessmentTakenQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenQueryReply;
  static deserializeBinaryFromReader(message: GetAssessmentTakenQueryReply, reader: jspb.BinaryReader): GetAssessmentTakenQueryReply;
}

export namespace GetAssessmentTakenQueryReply {
  export type AsObject = {
    assessmentTakenQuery?: AssessmentTakenQuery.AsObject,
  }
}

export class GetAssessmentTakenQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenQueryRequest): GetAssessmentTakenQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentTakenQueryRequest, reader: jspb.BinaryReader): GetAssessmentTakenQueryRequest;
}

export namespace GetAssessmentTakenQueryRequest {
  export type AsObject = {
  }
}

export class GetAssessmentsTakenByQueryRequest extends jspb.Message {
  hasAssessmentTakenQuery(): boolean;
  clearAssessmentTakenQuery(): void;
  getAssessmentTakenQuery(): AssessmentTakenQuery | undefined;
  setAssessmentTakenQuery(value?: AssessmentTakenQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByQueryRequest): GetAssessmentsTakenByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByQueryRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByQueryRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByQueryRequest;
}

export namespace GetAssessmentsTakenByQueryRequest {
  export type AsObject = {
    assessmentTakenQuery?: AssessmentTakenQuery.AsObject,
  }
}

export class CanCreateAssessmentsTakenReply extends jspb.Message {
  getCanCreateAssessmentsTaken(): boolean;
  setCanCreateAssessmentsTaken(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentsTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentsTakenReply): CanCreateAssessmentsTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentsTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentsTakenReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentsTakenReply, reader: jspb.BinaryReader): CanCreateAssessmentsTakenReply;
}

export namespace CanCreateAssessmentsTakenReply {
  export type AsObject = {
    canCreateAssessmentsTaken: boolean,
  }
}

export class CanCreateAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentsTakenRequest): CanCreateAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentsTakenRequest, reader: jspb.BinaryReader): CanCreateAssessmentsTakenRequest;
}

export namespace CanCreateAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class CanCreateAssessmentTakenWithRecordTypesReply extends jspb.Message {
  getCanCreateAssessmentTakenWithRecordTypes(): boolean;
  setCanCreateAssessmentTakenWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentTakenWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentTakenWithRecordTypesReply): CanCreateAssessmentTakenWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentTakenWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentTakenWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateAssessmentTakenWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateAssessmentTakenWithRecordTypesReply;
}

export namespace CanCreateAssessmentTakenWithRecordTypesReply {
  export type AsObject = {
    canCreateAssessmentTakenWithRecordTypes: boolean,
  }
}

export class CanCreateAssessmentTakenWithRecordTypesRequest extends jspb.Message {
  clearAssessmentTakenRecordTypesList(): void;
  getAssessmentTakenRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentTakenRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentTakenRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateAssessmentTakenWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateAssessmentTakenWithRecordTypesRequest): CanCreateAssessmentTakenWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateAssessmentTakenWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateAssessmentTakenWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateAssessmentTakenWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateAssessmentTakenWithRecordTypesRequest;
}

export namespace CanCreateAssessmentTakenWithRecordTypesRequest {
  export type AsObject = {
    assessmentTakenRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetAssessmentTakenFormForCreateReply extends jspb.Message {
  hasAssessmentTakenForm(): boolean;
  clearAssessmentTakenForm(): void;
  getAssessmentTakenForm(): AssessmentTakenForm | undefined;
  setAssessmentTakenForm(value?: AssessmentTakenForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenFormForCreateReply): GetAssessmentTakenFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenFormForCreateReply;
  static deserializeBinaryFromReader(message: GetAssessmentTakenFormForCreateReply, reader: jspb.BinaryReader): GetAssessmentTakenFormForCreateReply;
}

export namespace GetAssessmentTakenFormForCreateReply {
  export type AsObject = {
    assessmentTakenForm?: AssessmentTakenForm.AsObject,
  }
}

export class GetAssessmentTakenFormForCreateRequest extends jspb.Message {
  hasAssessmentOfferedId(): boolean;
  clearAssessmentOfferedId(): void;
  getAssessmentOfferedId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentOfferedId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearAssessmentTakenRecordTypesList(): void;
  getAssessmentTakenRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setAssessmentTakenRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addAssessmentTakenRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenFormForCreateRequest): GetAssessmentTakenFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentTakenFormForCreateRequest, reader: jspb.BinaryReader): GetAssessmentTakenFormForCreateRequest;
}

export namespace GetAssessmentTakenFormForCreateRequest {
  export type AsObject = {
    assessmentOfferedId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentTakenRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateAssessmentTakenReply extends jspb.Message {
  hasAssessmentTaken(): boolean;
  clearAssessmentTaken(): void;
  getAssessmentTaken(): AssessmentTaken | undefined;
  setAssessmentTaken(value?: AssessmentTaken): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentTakenReply): CreateAssessmentTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentTakenReply;
  static deserializeBinaryFromReader(message: CreateAssessmentTakenReply, reader: jspb.BinaryReader): CreateAssessmentTakenReply;
}

export namespace CreateAssessmentTakenReply {
  export type AsObject = {
    assessmentTaken?: AssessmentTaken.AsObject,
  }
}

export class CreateAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenForm(): boolean;
  clearAssessmentTakenForm(): void;
  getAssessmentTakenForm(): AssessmentTakenForm | undefined;
  setAssessmentTakenForm(value?: AssessmentTakenForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateAssessmentTakenRequest): CreateAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: CreateAssessmentTakenRequest, reader: jspb.BinaryReader): CreateAssessmentTakenRequest;
}

export namespace CreateAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenForm?: AssessmentTakenForm.AsObject,
  }
}

export class CanUpdateAssessmentsTakenReply extends jspb.Message {
  getCanUpdateAssessmentsTaken(): boolean;
  setCanUpdateAssessmentsTaken(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentsTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentsTakenReply): CanUpdateAssessmentsTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentsTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentsTakenReply;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentsTakenReply, reader: jspb.BinaryReader): CanUpdateAssessmentsTakenReply;
}

export namespace CanUpdateAssessmentsTakenReply {
  export type AsObject = {
    canUpdateAssessmentsTaken: boolean,
  }
}

export class CanUpdateAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateAssessmentsTakenRequest): CanUpdateAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: CanUpdateAssessmentsTakenRequest, reader: jspb.BinaryReader): CanUpdateAssessmentsTakenRequest;
}

export namespace CanUpdateAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class GetAssessmentTakenFormForUpdateReply extends jspb.Message {
  hasAssessmentTakenForm(): boolean;
  clearAssessmentTakenForm(): void;
  getAssessmentTakenForm(): AssessmentTakenForm | undefined;
  setAssessmentTakenForm(value?: AssessmentTakenForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenFormForUpdateReply): GetAssessmentTakenFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetAssessmentTakenFormForUpdateReply, reader: jspb.BinaryReader): GetAssessmentTakenFormForUpdateReply;
}

export namespace GetAssessmentTakenFormForUpdateReply {
  export type AsObject = {
    assessmentTakenForm?: AssessmentTakenForm.AsObject,
  }
}

export class GetAssessmentTakenFormForUpdateRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenFormForUpdateRequest): GetAssessmentTakenFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetAssessmentTakenFormForUpdateRequest, reader: jspb.BinaryReader): GetAssessmentTakenFormForUpdateRequest;
}

export namespace GetAssessmentTakenFormForUpdateRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateAssessmentTakenReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentTakenReply): UpdateAssessmentTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentTakenReply;
  static deserializeBinaryFromReader(message: UpdateAssessmentTakenReply, reader: jspb.BinaryReader): UpdateAssessmentTakenReply;
}

export namespace UpdateAssessmentTakenReply {
  export type AsObject = {
  }
}

export class UpdateAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenForm(): boolean;
  clearAssessmentTakenForm(): void;
  getAssessmentTakenForm(): AssessmentTakenForm | undefined;
  setAssessmentTakenForm(value?: AssessmentTakenForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateAssessmentTakenRequest): UpdateAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: UpdateAssessmentTakenRequest, reader: jspb.BinaryReader): UpdateAssessmentTakenRequest;
}

export namespace UpdateAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenForm?: AssessmentTakenForm.AsObject,
  }
}

export class CanDeleteAssessmentsTakenReply extends jspb.Message {
  getCanDeleteAssessmentsTaken(): boolean;
  setCanDeleteAssessmentsTaken(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentsTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentsTakenReply): CanDeleteAssessmentsTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentsTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentsTakenReply;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentsTakenReply, reader: jspb.BinaryReader): CanDeleteAssessmentsTakenReply;
}

export namespace CanDeleteAssessmentsTakenReply {
  export type AsObject = {
    canDeleteAssessmentsTaken: boolean,
  }
}

export class CanDeleteAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteAssessmentsTakenRequest): CanDeleteAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: CanDeleteAssessmentsTakenRequest, reader: jspb.BinaryReader): CanDeleteAssessmentsTakenRequest;
}

export namespace CanDeleteAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class DeleteAssessmentTakenReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentTakenReply): DeleteAssessmentTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentTakenReply;
  static deserializeBinaryFromReader(message: DeleteAssessmentTakenReply, reader: jspb.BinaryReader): DeleteAssessmentTakenReply;
}

export namespace DeleteAssessmentTakenReply {
  export type AsObject = {
  }
}

export class DeleteAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteAssessmentTakenRequest): DeleteAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: DeleteAssessmentTakenRequest, reader: jspb.BinaryReader): DeleteAssessmentTakenRequest;
}

export namespace DeleteAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageAssessmentTakenAliasesReply extends jspb.Message {
  getCanManageAssessmentTakenAliases(): boolean;
  setCanManageAssessmentTakenAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentTakenAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentTakenAliasesReply): CanManageAssessmentTakenAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentTakenAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentTakenAliasesReply;
  static deserializeBinaryFromReader(message: CanManageAssessmentTakenAliasesReply, reader: jspb.BinaryReader): CanManageAssessmentTakenAliasesReply;
}

export namespace CanManageAssessmentTakenAliasesReply {
  export type AsObject = {
    canManageAssessmentTakenAliases: boolean,
  }
}

export class CanManageAssessmentTakenAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageAssessmentTakenAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageAssessmentTakenAliasesRequest): CanManageAssessmentTakenAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageAssessmentTakenAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageAssessmentTakenAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageAssessmentTakenAliasesRequest, reader: jspb.BinaryReader): CanManageAssessmentTakenAliasesRequest;
}

export namespace CanManageAssessmentTakenAliasesRequest {
  export type AsObject = {
  }
}

export class AliasAssessmentTakenReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentTakenReply): AliasAssessmentTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentTakenReply;
  static deserializeBinaryFromReader(message: AliasAssessmentTakenReply, reader: jspb.BinaryReader): AliasAssessmentTakenReply;
}

export namespace AliasAssessmentTakenReply {
  export type AsObject = {
  }
}

export class AliasAssessmentTakenRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasAssessmentTakenRequest): AliasAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: AliasAssessmentTakenRequest, reader: jspb.BinaryReader): AliasAssessmentTakenRequest;
}

export namespace AliasAssessmentTakenRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupAssessmentTakenBankMappingsReply extends jspb.Message {
  getCanLookupAssessmentTakenBankMappings(): boolean;
  setCanLookupAssessmentTakenBankMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentTakenBankMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentTakenBankMappingsReply): CanLookupAssessmentTakenBankMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentTakenBankMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentTakenBankMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupAssessmentTakenBankMappingsReply, reader: jspb.BinaryReader): CanLookupAssessmentTakenBankMappingsReply;
}

export namespace CanLookupAssessmentTakenBankMappingsReply {
  export type AsObject = {
    canLookupAssessmentTakenBankMappings: boolean,
  }
}

export class CanLookupAssessmentTakenBankMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAssessmentTakenBankMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAssessmentTakenBankMappingsRequest): CanLookupAssessmentTakenBankMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAssessmentTakenBankMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAssessmentTakenBankMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupAssessmentTakenBankMappingsRequest, reader: jspb.BinaryReader): CanLookupAssessmentTakenBankMappingsRequest;
}

export namespace CanLookupAssessmentTakenBankMappingsRequest {
  export type AsObject = {
  }
}

export class GetAssessmentTakenIdsByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenIdsByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenIdsByBankRequest): GetAssessmentTakenIdsByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenIdsByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenIdsByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentTakenIdsByBankRequest, reader: jspb.BinaryReader): GetAssessmentTakenIdsByBankRequest;
}

export namespace GetAssessmentTakenIdsByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentsTakenByBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByBankRequest): GetAssessmentsTakenByBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByBankRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByBankRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByBankRequest;
}

export namespace GetAssessmentsTakenByBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssessmentTakenIdsByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentTakenIdsByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentTakenIdsByBanksRequest): GetAssessmentTakenIdsByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentTakenIdsByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentTakenIdsByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentTakenIdsByBanksRequest, reader: jspb.BinaryReader): GetAssessmentTakenIdsByBanksRequest;
}

export namespace GetAssessmentTakenIdsByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAssessmentsTakenByBanksRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssessmentsTakenByBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssessmentsTakenByBanksRequest): GetAssessmentsTakenByBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssessmentsTakenByBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssessmentsTakenByBanksRequest;
  static deserializeBinaryFromReader(message: GetAssessmentsTakenByBanksRequest, reader: jspb.BinaryReader): GetAssessmentsTakenByBanksRequest;
}

export namespace GetAssessmentsTakenByBanksRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBankIdsByAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankIdsByAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankIdsByAssessmentTakenRequest): GetBankIdsByAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankIdsByAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankIdsByAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: GetBankIdsByAssessmentTakenRequest, reader: jspb.BinaryReader): GetBankIdsByAssessmentTakenRequest;
}

export namespace GetBankIdsByAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBanksByAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByAssessmentTakenRequest): GetBanksByAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: GetBanksByAssessmentTakenRequest, reader: jspb.BinaryReader): GetBanksByAssessmentTakenRequest;
}

export namespace GetBanksByAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignAssessmentsTakenReply extends jspb.Message {
  getCanAssignAssessmentsTaken(): boolean;
  setCanAssignAssessmentsTaken(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsTakenReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsTakenReply): CanAssignAssessmentsTakenReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsTakenReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsTakenReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsTakenReply, reader: jspb.BinaryReader): CanAssignAssessmentsTakenReply;
}

export namespace CanAssignAssessmentsTakenReply {
  export type AsObject = {
    canAssignAssessmentsTaken: boolean,
  }
}

export class CanAssignAssessmentsTakenRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsTakenRequest): CanAssignAssessmentsTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsTakenRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsTakenRequest, reader: jspb.BinaryReader): CanAssignAssessmentsTakenRequest;
}

export namespace CanAssignAssessmentsTakenRequest {
  export type AsObject = {
  }
}

export class CanAssignAssessmentsTakenToBankReply extends jspb.Message {
  getCanAssignAssessmentsTakenToBank(): boolean;
  setCanAssignAssessmentsTakenToBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsTakenToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsTakenToBankReply): CanAssignAssessmentsTakenToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsTakenToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsTakenToBankReply;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsTakenToBankReply, reader: jspb.BinaryReader): CanAssignAssessmentsTakenToBankReply;
}

export namespace CanAssignAssessmentsTakenToBankReply {
  export type AsObject = {
    canAssignAssessmentsTakenToBank: boolean,
  }
}

export class CanAssignAssessmentsTakenToBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignAssessmentsTakenToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignAssessmentsTakenToBankRequest): CanAssignAssessmentsTakenToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignAssessmentsTakenToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignAssessmentsTakenToBankRequest;
  static deserializeBinaryFromReader(message: CanAssignAssessmentsTakenToBankRequest, reader: jspb.BinaryReader): CanAssignAssessmentsTakenToBankRequest;
}

export namespace CanAssignAssessmentsTakenToBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBankIdsForAssessmentTakenRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBankIdsForAssessmentTakenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBankIdsForAssessmentTakenRequest): GetAssignableBankIdsForAssessmentTakenRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBankIdsForAssessmentTakenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBankIdsForAssessmentTakenRequest;
  static deserializeBinaryFromReader(message: GetAssignableBankIdsForAssessmentTakenRequest, reader: jspb.BinaryReader): GetAssignableBankIdsForAssessmentTakenRequest;
}

export namespace GetAssignableBankIdsForAssessmentTakenRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignAssessmentTakenToBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentTakenToBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentTakenToBankReply): AssignAssessmentTakenToBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentTakenToBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentTakenToBankReply;
  static deserializeBinaryFromReader(message: AssignAssessmentTakenToBankReply, reader: jspb.BinaryReader): AssignAssessmentTakenToBankReply;
}

export namespace AssignAssessmentTakenToBankReply {
  export type AsObject = {
  }
}

export class AssignAssessmentTakenToBankRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignAssessmentTakenToBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignAssessmentTakenToBankRequest): AssignAssessmentTakenToBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignAssessmentTakenToBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignAssessmentTakenToBankRequest;
  static deserializeBinaryFromReader(message: AssignAssessmentTakenToBankRequest, reader: jspb.BinaryReader): AssignAssessmentTakenToBankRequest;
}

export namespace AssignAssessmentTakenToBankRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignAssessmentTakenFromBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentTakenFromBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentTakenFromBankReply): UnassignAssessmentTakenFromBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentTakenFromBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentTakenFromBankReply;
  static deserializeBinaryFromReader(message: UnassignAssessmentTakenFromBankReply, reader: jspb.BinaryReader): UnassignAssessmentTakenFromBankReply;
}

export namespace UnassignAssessmentTakenFromBankReply {
  export type AsObject = {
  }
}

export class UnassignAssessmentTakenFromBankRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignAssessmentTakenFromBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignAssessmentTakenFromBankRequest): UnassignAssessmentTakenFromBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignAssessmentTakenFromBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignAssessmentTakenFromBankRequest;
  static deserializeBinaryFromReader(message: UnassignAssessmentTakenFromBankRequest, reader: jspb.BinaryReader): UnassignAssessmentTakenFromBankRequest;
}

export namespace UnassignAssessmentTakenFromBankRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignAssessmentTakenToBillingReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentTakenToBillingReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentTakenToBillingReply): ReassignAssessmentTakenToBillingReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentTakenToBillingReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentTakenToBillingReply;
  static deserializeBinaryFromReader(message: ReassignAssessmentTakenToBillingReply, reader: jspb.BinaryReader): ReassignAssessmentTakenToBillingReply;
}

export namespace ReassignAssessmentTakenToBillingReply {
  export type AsObject = {
  }
}

export class ReassignAssessmentTakenToBillingRequest extends jspb.Message {
  hasAssessmentTakenId(): boolean;
  clearAssessmentTakenId(): void;
  getAssessmentTakenId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAssessmentTakenId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromBankId(): boolean;
  clearFromBankId(): void;
  getFromBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToBankId(): boolean;
  clearToBankId(): void;
  getToBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignAssessmentTakenToBillingRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignAssessmentTakenToBillingRequest): ReassignAssessmentTakenToBillingRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignAssessmentTakenToBillingRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignAssessmentTakenToBillingRequest;
  static deserializeBinaryFromReader(message: ReassignAssessmentTakenToBillingRequest, reader: jspb.BinaryReader): ReassignAssessmentTakenToBillingRequest;
}

export namespace ReassignAssessmentTakenToBillingRequest {
  export type AsObject = {
    assessmentTakenId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toBankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupBanksReply extends jspb.Message {
  getCanLookupBanks(): boolean;
  setCanLookupBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupBanksReply): CanLookupBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupBanksReply;
  static deserializeBinaryFromReader(message: CanLookupBanksReply, reader: jspb.BinaryReader): CanLookupBanksReply;
}

export namespace CanLookupBanksReply {
  export type AsObject = {
    canLookupBanks: boolean,
  }
}

export class CanLookupBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupBanksRequest): CanLookupBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupBanksRequest;
  static deserializeBinaryFromReader(message: CanLookupBanksRequest, reader: jspb.BinaryReader): CanLookupBanksRequest;
}

export namespace CanLookupBanksRequest {
  export type AsObject = {
  }
}

export class GetBanksByIdsRequest extends jspb.Message {
  clearBankIdsList(): void;
  getBankIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBankIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBankIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByIdsRequest): GetBanksByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByIdsRequest;
  static deserializeBinaryFromReader(message: GetBanksByIdsRequest, reader: jspb.BinaryReader): GetBanksByIdsRequest;
}

export namespace GetBanksByIdsRequest {
  export type AsObject = {
    bankIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBanksByGenusTypeRequest extends jspb.Message {
  hasBankGenusType(): boolean;
  clearBankGenusType(): void;
  getBankGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBankGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByGenusTypeRequest): GetBanksByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetBanksByGenusTypeRequest, reader: jspb.BinaryReader): GetBanksByGenusTypeRequest;
}

export namespace GetBanksByGenusTypeRequest {
  export type AsObject = {
    bankGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBanksByParentGenusTypeRequest extends jspb.Message {
  hasBankGenusType(): boolean;
  clearBankGenusType(): void;
  getBankGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBankGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByParentGenusTypeRequest): GetBanksByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetBanksByParentGenusTypeRequest, reader: jspb.BinaryReader): GetBanksByParentGenusTypeRequest;
}

export namespace GetBanksByParentGenusTypeRequest {
  export type AsObject = {
    bankGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBanksByRecordTypeRequest extends jspb.Message {
  hasBankRecordType(): boolean;
  clearBankRecordType(): void;
  getBankRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBankRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByRecordTypeRequest): GetBanksByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetBanksByRecordTypeRequest, reader: jspb.BinaryReader): GetBanksByRecordTypeRequest;
}

export namespace GetBanksByRecordTypeRequest {
  export type AsObject = {
    bankRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBanksByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByProviderRequest): GetBanksByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByProviderRequest;
  static deserializeBinaryFromReader(message: GetBanksByProviderRequest, reader: jspb.BinaryReader): GetBanksByProviderRequest;
}

export namespace GetBanksByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksRequest): GetBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksRequest;
  static deserializeBinaryFromReader(message: GetBanksRequest, reader: jspb.BinaryReader): GetBanksRequest;
}

export namespace GetBanksRequest {
  export type AsObject = {
  }
}

export class CanSearchBanksReply extends jspb.Message {
  getCanSearchBanks(): boolean;
  setCanSearchBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchBanksReply): CanSearchBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchBanksReply;
  static deserializeBinaryFromReader(message: CanSearchBanksReply, reader: jspb.BinaryReader): CanSearchBanksReply;
}

export namespace CanSearchBanksReply {
  export type AsObject = {
    canSearchBanks: boolean,
  }
}

export class CanSearchBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchBanksRequest): CanSearchBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchBanksRequest;
  static deserializeBinaryFromReader(message: CanSearchBanksRequest, reader: jspb.BinaryReader): CanSearchBanksRequest;
}

export namespace CanSearchBanksRequest {
  export type AsObject = {
  }
}

export class GetBankQueryReply extends jspb.Message {
  hasBankQuery(): boolean;
  clearBankQuery(): void;
  getBankQuery(): BankQuery | undefined;
  setBankQuery(value?: BankQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankQueryReply): GetBankQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankQueryReply;
  static deserializeBinaryFromReader(message: GetBankQueryReply, reader: jspb.BinaryReader): GetBankQueryReply;
}

export namespace GetBankQueryReply {
  export type AsObject = {
    bankQuery?: BankQuery.AsObject,
  }
}

export class GetBankQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankQueryRequest): GetBankQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankQueryRequest;
  static deserializeBinaryFromReader(message: GetBankQueryRequest, reader: jspb.BinaryReader): GetBankQueryRequest;
}

export namespace GetBankQueryRequest {
  export type AsObject = {
  }
}

export class GetBanksByQueryRequest extends jspb.Message {
  hasBankQuery(): boolean;
  clearBankQuery(): void;
  getBankQuery(): BankQuery | undefined;
  setBankQuery(value?: BankQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBanksByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBanksByQueryRequest): GetBanksByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBanksByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBanksByQueryRequest;
  static deserializeBinaryFromReader(message: GetBanksByQueryRequest, reader: jspb.BinaryReader): GetBanksByQueryRequest;
}

export namespace GetBanksByQueryRequest {
  export type AsObject = {
    bankQuery?: BankQuery.AsObject,
  }
}

export class CanCreateBanksReply extends jspb.Message {
  getCanCreateBanks(): boolean;
  setCanCreateBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBanksReply): CanCreateBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBanksReply;
  static deserializeBinaryFromReader(message: CanCreateBanksReply, reader: jspb.BinaryReader): CanCreateBanksReply;
}

export namespace CanCreateBanksReply {
  export type AsObject = {
    canCreateBanks: boolean,
  }
}

export class CanCreateBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBanksRequest): CanCreateBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBanksRequest;
  static deserializeBinaryFromReader(message: CanCreateBanksRequest, reader: jspb.BinaryReader): CanCreateBanksRequest;
}

export namespace CanCreateBanksRequest {
  export type AsObject = {
  }
}

export class CanCreateBankWithRecordTypesReply extends jspb.Message {
  getCanCreateBankWithRecordTypes(): boolean;
  setCanCreateBankWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBankWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBankWithRecordTypesReply): CanCreateBankWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBankWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBankWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateBankWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateBankWithRecordTypesReply;
}

export namespace CanCreateBankWithRecordTypesReply {
  export type AsObject = {
    canCreateBankWithRecordTypes: boolean,
  }
}

export class CanCreateBankWithRecordTypesRequest extends jspb.Message {
  clearBankRecordTypesList(): void;
  getBankRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setBankRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addBankRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBankWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBankWithRecordTypesRequest): CanCreateBankWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBankWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBankWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateBankWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateBankWithRecordTypesRequest;
}

export namespace CanCreateBankWithRecordTypesRequest {
  export type AsObject = {
    bankRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetBankFormForCreateReply extends jspb.Message {
  hasBankForm(): boolean;
  clearBankForm(): void;
  getBankForm(): BankForm | undefined;
  setBankForm(value?: BankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankFormForCreateReply): GetBankFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankFormForCreateReply;
  static deserializeBinaryFromReader(message: GetBankFormForCreateReply, reader: jspb.BinaryReader): GetBankFormForCreateReply;
}

export namespace GetBankFormForCreateReply {
  export type AsObject = {
    bankForm?: BankForm.AsObject,
  }
}

export class GetBankFormForCreateRequest extends jspb.Message {
  clearBankRecordTypesList(): void;
  getBankRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setBankRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addBankRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankFormForCreateRequest): GetBankFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetBankFormForCreateRequest, reader: jspb.BinaryReader): GetBankFormForCreateRequest;
}

export namespace GetBankFormForCreateRequest {
  export type AsObject = {
    bankRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateBankReply extends jspb.Message {
  hasBank(): boolean;
  clearBank(): void;
  getBank(): Bank | undefined;
  setBank(value?: Bank): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateBankReply): CreateBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateBankReply;
  static deserializeBinaryFromReader(message: CreateBankReply, reader: jspb.BinaryReader): CreateBankReply;
}

export namespace CreateBankReply {
  export type AsObject = {
    bank?: Bank.AsObject,
  }
}

export class CreateBankRequest extends jspb.Message {
  hasBankForm(): boolean;
  clearBankForm(): void;
  getBankForm(): BankForm | undefined;
  setBankForm(value?: BankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateBankRequest): CreateBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateBankRequest;
  static deserializeBinaryFromReader(message: CreateBankRequest, reader: jspb.BinaryReader): CreateBankRequest;
}

export namespace CreateBankRequest {
  export type AsObject = {
    bankForm?: BankForm.AsObject,
  }
}

export class CanUpdateBanksReply extends jspb.Message {
  getCanUpdateBanks(): boolean;
  setCanUpdateBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateBanksReply): CanUpdateBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateBanksReply;
  static deserializeBinaryFromReader(message: CanUpdateBanksReply, reader: jspb.BinaryReader): CanUpdateBanksReply;
}

export namespace CanUpdateBanksReply {
  export type AsObject = {
    canUpdateBanks: boolean,
  }
}

export class CanUpdateBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateBanksRequest): CanUpdateBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateBanksRequest;
  static deserializeBinaryFromReader(message: CanUpdateBanksRequest, reader: jspb.BinaryReader): CanUpdateBanksRequest;
}

export namespace CanUpdateBanksRequest {
  export type AsObject = {
  }
}

export class GetBankFormForUpdateReply extends jspb.Message {
  hasBankForm(): boolean;
  clearBankForm(): void;
  getBankForm(): BankForm | undefined;
  setBankForm(value?: BankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankFormForUpdateReply): GetBankFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetBankFormForUpdateReply, reader: jspb.BinaryReader): GetBankFormForUpdateReply;
}

export namespace GetBankFormForUpdateReply {
  export type AsObject = {
    bankForm?: BankForm.AsObject,
  }
}

export class GetBankFormForUpdateRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankFormForUpdateRequest): GetBankFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetBankFormForUpdateRequest, reader: jspb.BinaryReader): GetBankFormForUpdateRequest;
}

export namespace GetBankFormForUpdateRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateBankReply): UpdateBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateBankReply;
  static deserializeBinaryFromReader(message: UpdateBankReply, reader: jspb.BinaryReader): UpdateBankReply;
}

export namespace UpdateBankReply {
  export type AsObject = {
  }
}

export class UpdateBankRequest extends jspb.Message {
  hasBankForm(): boolean;
  clearBankForm(): void;
  getBankForm(): BankForm | undefined;
  setBankForm(value?: BankForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateBankRequest): UpdateBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateBankRequest;
  static deserializeBinaryFromReader(message: UpdateBankRequest, reader: jspb.BinaryReader): UpdateBankRequest;
}

export namespace UpdateBankRequest {
  export type AsObject = {
    bankForm?: BankForm.AsObject,
  }
}

export class CanDeleteBanksReply extends jspb.Message {
  getCanDeleteBanks(): boolean;
  setCanDeleteBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteBanksReply): CanDeleteBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteBanksReply;
  static deserializeBinaryFromReader(message: CanDeleteBanksReply, reader: jspb.BinaryReader): CanDeleteBanksReply;
}

export namespace CanDeleteBanksReply {
  export type AsObject = {
    canDeleteBanks: boolean,
  }
}

export class CanDeleteBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteBanksRequest): CanDeleteBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteBanksRequest;
  static deserializeBinaryFromReader(message: CanDeleteBanksRequest, reader: jspb.BinaryReader): CanDeleteBanksRequest;
}

export namespace CanDeleteBanksRequest {
  export type AsObject = {
  }
}

export class DeleteBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteBankReply): DeleteBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteBankReply;
  static deserializeBinaryFromReader(message: DeleteBankReply, reader: jspb.BinaryReader): DeleteBankReply;
}

export namespace DeleteBankReply {
  export type AsObject = {
  }
}

export class DeleteBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteBankRequest): DeleteBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteBankRequest;
  static deserializeBinaryFromReader(message: DeleteBankRequest, reader: jspb.BinaryReader): DeleteBankRequest;
}

export namespace DeleteBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageBankAliasesReply extends jspb.Message {
  getCanManageBankAliases(): boolean;
  setCanManageBankAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageBankAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageBankAliasesReply): CanManageBankAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageBankAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageBankAliasesReply;
  static deserializeBinaryFromReader(message: CanManageBankAliasesReply, reader: jspb.BinaryReader): CanManageBankAliasesReply;
}

export namespace CanManageBankAliasesReply {
  export type AsObject = {
    canManageBankAliases: boolean,
  }
}

export class CanManageBankAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageBankAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageBankAliasesRequest): CanManageBankAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageBankAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageBankAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageBankAliasesRequest, reader: jspb.BinaryReader): CanManageBankAliasesRequest;
}

export namespace CanManageBankAliasesRequest {
  export type AsObject = {
  }
}

export class AliasBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasBankReply): AliasBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasBankReply;
  static deserializeBinaryFromReader(message: AliasBankReply, reader: jspb.BinaryReader): AliasBankReply;
}

export namespace AliasBankReply {
  export type AsObject = {
  }
}

export class AliasBankRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasBankRequest): AliasBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasBankRequest;
  static deserializeBinaryFromReader(message: AliasBankRequest, reader: jspb.BinaryReader): AliasBankRequest;
}

export namespace AliasBankRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBankHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankHierarchyIdReply): GetBankHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetBankHierarchyIdReply, reader: jspb.BinaryReader): GetBankHierarchyIdReply;
}

export namespace GetBankHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBankHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankHierarchyIdRequest): GetBankHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetBankHierarchyIdRequest, reader: jspb.BinaryReader): GetBankHierarchyIdRequest;
}

export namespace GetBankHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetBankHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankHierarchyReply): GetBankHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankHierarchyReply;
  static deserializeBinaryFromReader(message: GetBankHierarchyReply, reader: jspb.BinaryReader): GetBankHierarchyReply;
}

export namespace GetBankHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetBankHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankHierarchyRequest): GetBankHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankHierarchyRequest;
  static deserializeBinaryFromReader(message: GetBankHierarchyRequest, reader: jspb.BinaryReader): GetBankHierarchyRequest;
}

export namespace GetBankHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessBankHierarchyReply extends jspb.Message {
  getCanAccessBankHierarchy(): boolean;
  setCanAccessBankHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessBankHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessBankHierarchyReply): CanAccessBankHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessBankHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessBankHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessBankHierarchyReply, reader: jspb.BinaryReader): CanAccessBankHierarchyReply;
}

export namespace CanAccessBankHierarchyReply {
  export type AsObject = {
    canAccessBankHierarchy: boolean,
  }
}

export class CanAccessBankHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessBankHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessBankHierarchyRequest): CanAccessBankHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessBankHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessBankHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessBankHierarchyRequest, reader: jspb.BinaryReader): CanAccessBankHierarchyRequest;
}

export namespace CanAccessBankHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootBankIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootBankIdsRequest): GetRootBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootBankIdsRequest;
  static deserializeBinaryFromReader(message: GetRootBankIdsRequest, reader: jspb.BinaryReader): GetRootBankIdsRequest;
}

export namespace GetRootBankIdsRequest {
  export type AsObject = {
  }
}

export class GetRootBanksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootBanksRequest): GetRootBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootBanksRequest;
  static deserializeBinaryFromReader(message: GetRootBanksRequest, reader: jspb.BinaryReader): GetRootBanksRequest;
}

export namespace GetRootBanksRequest {
  export type AsObject = {
  }
}

export class HasParentBanksReply extends jspb.Message {
  getHasParentBanks(): boolean;
  setHasParentBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentBanksReply): HasParentBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentBanksReply;
  static deserializeBinaryFromReader(message: HasParentBanksReply, reader: jspb.BinaryReader): HasParentBanksReply;
}

export namespace HasParentBanksReply {
  export type AsObject = {
    hasParentBanks: boolean,
  }
}

export class HasParentBanksRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentBanksRequest): HasParentBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentBanksRequest;
  static deserializeBinaryFromReader(message: HasParentBanksRequest, reader: jspb.BinaryReader): HasParentBanksRequest;
}

export namespace HasParentBanksRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfBankReply extends jspb.Message {
  getIsParentOfBank(): boolean;
  setIsParentOfBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfBankReply): IsParentOfBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfBankReply;
  static deserializeBinaryFromReader(message: IsParentOfBankReply, reader: jspb.BinaryReader): IsParentOfBankReply;
}

export namespace IsParentOfBankReply {
  export type AsObject = {
    isParentOfBank: boolean,
  }
}

export class IsParentOfBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfBankRequest): IsParentOfBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfBankRequest;
  static deserializeBinaryFromReader(message: IsParentOfBankRequest, reader: jspb.BinaryReader): IsParentOfBankRequest;
}

export namespace IsParentOfBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentBankIdsRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentBankIdsRequest): GetParentBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentBankIdsRequest;
  static deserializeBinaryFromReader(message: GetParentBankIdsRequest, reader: jspb.BinaryReader): GetParentBankIdsRequest;
}

export namespace GetParentBankIdsRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentBanksRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentBanksRequest): GetParentBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentBanksRequest;
  static deserializeBinaryFromReader(message: GetParentBanksRequest, reader: jspb.BinaryReader): GetParentBanksRequest;
}

export namespace GetParentBanksRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfBankReply extends jspb.Message {
  getIsAncestorOfBank(): boolean;
  setIsAncestorOfBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfBankReply): IsAncestorOfBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfBankReply;
  static deserializeBinaryFromReader(message: IsAncestorOfBankReply, reader: jspb.BinaryReader): IsAncestorOfBankReply;
}

export namespace IsAncestorOfBankReply {
  export type AsObject = {
    isAncestorOfBank: boolean,
  }
}

export class IsAncestorOfBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfBankRequest): IsAncestorOfBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfBankRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfBankRequest, reader: jspb.BinaryReader): IsAncestorOfBankRequest;
}

export namespace IsAncestorOfBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildBanksReply extends jspb.Message {
  getHasChildBanks(): boolean;
  setHasChildBanks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildBanksReply): HasChildBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildBanksReply;
  static deserializeBinaryFromReader(message: HasChildBanksReply, reader: jspb.BinaryReader): HasChildBanksReply;
}

export namespace HasChildBanksReply {
  export type AsObject = {
    hasChildBanks: boolean,
  }
}

export class HasChildBanksRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildBanksRequest): HasChildBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildBanksRequest;
  static deserializeBinaryFromReader(message: HasChildBanksRequest, reader: jspb.BinaryReader): HasChildBanksRequest;
}

export namespace HasChildBanksRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfBankReply extends jspb.Message {
  getIsChildOfBank(): boolean;
  setIsChildOfBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfBankReply): IsChildOfBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfBankReply;
  static deserializeBinaryFromReader(message: IsChildOfBankReply, reader: jspb.BinaryReader): IsChildOfBankReply;
}

export namespace IsChildOfBankReply {
  export type AsObject = {
    isChildOfBank: boolean,
  }
}

export class IsChildOfBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfBankRequest): IsChildOfBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfBankRequest;
  static deserializeBinaryFromReader(message: IsChildOfBankRequest, reader: jspb.BinaryReader): IsChildOfBankRequest;
}

export namespace IsChildOfBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildBankIdsRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildBankIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildBankIdsRequest): GetChildBankIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildBankIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildBankIdsRequest;
  static deserializeBinaryFromReader(message: GetChildBankIdsRequest, reader: jspb.BinaryReader): GetChildBankIdsRequest;
}

export namespace GetChildBankIdsRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildBanksRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildBanksRequest): GetChildBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildBanksRequest;
  static deserializeBinaryFromReader(message: GetChildBanksRequest, reader: jspb.BinaryReader): GetChildBanksRequest;
}

export namespace GetChildBanksRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfBankReply extends jspb.Message {
  getIsDescendantOfBank(): boolean;
  setIsDescendantOfBank(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfBankReply): IsDescendantOfBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfBankReply;
  static deserializeBinaryFromReader(message: IsDescendantOfBankReply, reader: jspb.BinaryReader): IsDescendantOfBankReply;
}

export namespace IsDescendantOfBankReply {
  export type AsObject = {
    isDescendantOfBank: boolean,
  }
}

export class IsDescendantOfBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfBankRequest): IsDescendantOfBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfBankRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfBankRequest, reader: jspb.BinaryReader): IsDescendantOfBankRequest;
}

export namespace IsDescendantOfBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBankNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankNodeIdsReply): GetBankNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankNodeIdsReply;
  static deserializeBinaryFromReader(message: GetBankNodeIdsReply, reader: jspb.BinaryReader): GetBankNodeIdsReply;
}

export namespace GetBankNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetBankNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankNodeIdsRequest): GetBankNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetBankNodeIdsRequest, reader: jspb.BinaryReader): GetBankNodeIdsRequest;
}

export namespace GetBankNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class GetBankNodesReply extends jspb.Message {
  hasBankNode(): boolean;
  clearBankNode(): void;
  getBankNode(): BankNode | undefined;
  setBankNode(value?: BankNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankNodesReply): GetBankNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankNodesReply;
  static deserializeBinaryFromReader(message: GetBankNodesReply, reader: jspb.BinaryReader): GetBankNodesReply;
}

export namespace GetBankNodesReply {
  export type AsObject = {
    bankNode?: BankNode.AsObject,
  }
}

export class GetBankNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBankNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBankNodesRequest): GetBankNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBankNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBankNodesRequest;
  static deserializeBinaryFromReader(message: GetBankNodesRequest, reader: jspb.BinaryReader): GetBankNodesRequest;
}

export namespace GetBankNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class CanModifyBankHierarchyReply extends jspb.Message {
  getCanModifyBankHierarchy(): boolean;
  setCanModifyBankHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyBankHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyBankHierarchyReply): CanModifyBankHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyBankHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyBankHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyBankHierarchyReply, reader: jspb.BinaryReader): CanModifyBankHierarchyReply;
}

export namespace CanModifyBankHierarchyReply {
  export type AsObject = {
    canModifyBankHierarchy: boolean,
  }
}

export class CanModifyBankHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyBankHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyBankHierarchyRequest): CanModifyBankHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyBankHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyBankHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyBankHierarchyRequest, reader: jspb.BinaryReader): CanModifyBankHierarchyRequest;
}

export namespace CanModifyBankHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootBankReply): AddRootBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootBankReply;
  static deserializeBinaryFromReader(message: AddRootBankReply, reader: jspb.BinaryReader): AddRootBankReply;
}

export namespace AddRootBankReply {
  export type AsObject = {
  }
}

export class AddRootBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootBankRequest): AddRootBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootBankRequest;
  static deserializeBinaryFromReader(message: AddRootBankRequest, reader: jspb.BinaryReader): AddRootBankRequest;
}

export namespace AddRootBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootBankReply): RemoveRootBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootBankReply;
  static deserializeBinaryFromReader(message: RemoveRootBankReply, reader: jspb.BinaryReader): RemoveRootBankReply;
}

export namespace RemoveRootBankReply {
  export type AsObject = {
  }
}

export class RemoveRootBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootBankRequest): RemoveRootBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootBankRequest;
  static deserializeBinaryFromReader(message: RemoveRootBankRequest, reader: jspb.BinaryReader): RemoveRootBankRequest;
}

export namespace RemoveRootBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildBankReply): AddChildBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildBankReply;
  static deserializeBinaryFromReader(message: AddChildBankReply, reader: jspb.BinaryReader): AddChildBankReply;
}

export namespace AddChildBankReply {
  export type AsObject = {
  }
}

export class AddChildBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildBankRequest): AddChildBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildBankRequest;
  static deserializeBinaryFromReader(message: AddChildBankRequest, reader: jspb.BinaryReader): AddChildBankRequest;
}

export namespace AddChildBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildBankReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBankReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBankReply): RemoveChildBankReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBankReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBankReply;
  static deserializeBinaryFromReader(message: RemoveChildBankReply, reader: jspb.BinaryReader): RemoveChildBankReply;
}

export namespace RemoveChildBankReply {
  export type AsObject = {
  }
}

export class RemoveChildBankRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBankRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBankRequest): RemoveChildBankRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBankRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBankRequest;
  static deserializeBinaryFromReader(message: RemoveChildBankRequest, reader: jspb.BinaryReader): RemoveChildBankRequest;
}

export namespace RemoveChildBankRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildBanksReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBanksReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBanksReply): RemoveChildBanksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBanksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBanksReply;
  static deserializeBinaryFromReader(message: RemoveChildBanksReply, reader: jspb.BinaryReader): RemoveChildBanksReply;
}

export namespace RemoveChildBanksReply {
  export type AsObject = {
  }
}

export class RemoveChildBanksRequest extends jspb.Message {
  hasBankId(): boolean;
  clearBankId(): void;
  getBankId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBankId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBanksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBanksRequest): RemoveChildBanksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBanksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBanksRequest;
  static deserializeBinaryFromReader(message: RemoveChildBanksRequest, reader: jspb.BinaryReader): RemoveChildBanksRequest;
}

export namespace RemoveChildBanksRequest {
  export type AsObject = {
    bankId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

