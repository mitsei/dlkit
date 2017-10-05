// package: dlkit.proto.ontology
// file: dlkit/proto/ontology.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";

export class Subject extends jspb.Message {
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

  hasOntology(): boolean;
  clearOntology(): void;
  getOntology(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setOntology(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Subject.AsObject;
  static toObject(includeInstance: boolean, msg: Subject): Subject.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Subject, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Subject;
  static deserializeBinaryFromReader(message: Subject, reader: jspb.BinaryReader): Subject;
}

export namespace Subject {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    ontology?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class SubjectQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectQuery.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectQuery): SubjectQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectQuery;
  static deserializeBinaryFromReader(message: SubjectQuery, reader: jspb.BinaryReader): SubjectQuery;
}

export namespace SubjectQuery {
  export type AsObject = {
  }
}

export class SubjectQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectQueryInspector): SubjectQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectQueryInspector;
  static deserializeBinaryFromReader(message: SubjectQueryInspector, reader: jspb.BinaryReader): SubjectQueryInspector;
}

export namespace SubjectQueryInspector {
  export type AsObject = {
  }
}

export class SubjectForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectForm.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectForm): SubjectForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectForm;
  static deserializeBinaryFromReader(message: SubjectForm, reader: jspb.BinaryReader): SubjectForm;
}

export namespace SubjectForm {
  export type AsObject = {
  }
}

export class SubjectSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectSearchOrder): SubjectSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectSearchOrder;
  static deserializeBinaryFromReader(message: SubjectSearchOrder, reader: jspb.BinaryReader): SubjectSearchOrder;
}

export namespace SubjectSearchOrder {
  export type AsObject = {
  }
}

export class SubjectSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectSearch.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectSearch): SubjectSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectSearch;
  static deserializeBinaryFromReader(message: SubjectSearch, reader: jspb.BinaryReader): SubjectSearch;
}

export namespace SubjectSearch {
  export type AsObject = {
  }
}

export class SubjectSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectSearchResults): SubjectSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectSearchResults;
  static deserializeBinaryFromReader(message: SubjectSearchResults, reader: jspb.BinaryReader): SubjectSearchResults;
}

export namespace SubjectSearchResults {
  export type AsObject = {
  }
}

export class SubjectList extends jspb.Message {
  clearSubjectsList(): void;
  getSubjectsList(): Array<Subject>;
  setSubjectsList(value: Array<Subject>): void;
  addSubjects(value?: Subject, index?: number): Subject;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectList.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectList): SubjectList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectList;
  static deserializeBinaryFromReader(message: SubjectList, reader: jspb.BinaryReader): SubjectList;
}

export namespace SubjectList {
  export type AsObject = {
    subjectsList: Array<Subject.AsObject>,
  }
}

export class SubjectNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectNode.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectNode): SubjectNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectNode;
  static deserializeBinaryFromReader(message: SubjectNode, reader: jspb.BinaryReader): SubjectNode;
}

export namespace SubjectNode {
  export type AsObject = {
  }
}

export class SubjectNodeList extends jspb.Message {
  clearSubjectNodesList(): void;
  getSubjectNodesList(): Array<SubjectNode>;
  setSubjectNodesList(value: Array<SubjectNode>): void;
  addSubjectNodes(value?: SubjectNode, index?: number): SubjectNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SubjectNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: SubjectNodeList): SubjectNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SubjectNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SubjectNodeList;
  static deserializeBinaryFromReader(message: SubjectNodeList, reader: jspb.BinaryReader): SubjectNodeList;
}

export namespace SubjectNodeList {
  export type AsObject = {
    subjectNodesList: Array<SubjectNode.AsObject>,
  }
}

export class Relevancy extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasMapped(): boolean;
  clearMapped(): void;
  getMapped(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setMapped(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasOntology(): boolean;
  clearOntology(): void;
  getOntology(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setOntology(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasSubject(): boolean;
  clearSubject(): void;
  getSubject(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSubject(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Relevancy.AsObject;
  static toObject(includeInstance: boolean, msg: Relevancy): Relevancy.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Relevancy, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Relevancy;
  static deserializeBinaryFromReader(message: Relevancy, reader: jspb.BinaryReader): Relevancy;
}

export namespace Relevancy {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    mapped?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    ontology?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    subject?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RelevancyQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancyQuery.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancyQuery): RelevancyQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancyQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancyQuery;
  static deserializeBinaryFromReader(message: RelevancyQuery, reader: jspb.BinaryReader): RelevancyQuery;
}

export namespace RelevancyQuery {
  export type AsObject = {
  }
}

export class RelevancyQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancyQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancyQueryInspector): RelevancyQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancyQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancyQueryInspector;
  static deserializeBinaryFromReader(message: RelevancyQueryInspector, reader: jspb.BinaryReader): RelevancyQueryInspector;
}

export namespace RelevancyQueryInspector {
  export type AsObject = {
  }
}

export class RelevancyForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancyForm.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancyForm): RelevancyForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancyForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancyForm;
  static deserializeBinaryFromReader(message: RelevancyForm, reader: jspb.BinaryReader): RelevancyForm;
}

export namespace RelevancyForm {
  export type AsObject = {
  }
}

export class RelevancySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancySearchOrder): RelevancySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancySearchOrder;
  static deserializeBinaryFromReader(message: RelevancySearchOrder, reader: jspb.BinaryReader): RelevancySearchOrder;
}

export namespace RelevancySearchOrder {
  export type AsObject = {
  }
}

export class RelevancySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancySearch.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancySearch): RelevancySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancySearch;
  static deserializeBinaryFromReader(message: RelevancySearch, reader: jspb.BinaryReader): RelevancySearch;
}

export namespace RelevancySearch {
  export type AsObject = {
  }
}

export class RelevancySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancySearchResults): RelevancySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancySearchResults;
  static deserializeBinaryFromReader(message: RelevancySearchResults, reader: jspb.BinaryReader): RelevancySearchResults;
}

export namespace RelevancySearchResults {
  export type AsObject = {
  }
}

export class RelevancyList extends jspb.Message {
  clearRelevancysList(): void;
  getRelevancysList(): Array<Relevancy>;
  setRelevancysList(value: Array<Relevancy>): void;
  addRelevancys(value?: Relevancy, index?: number): Relevancy;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RelevancyList.AsObject;
  static toObject(includeInstance: boolean, msg: RelevancyList): RelevancyList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RelevancyList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RelevancyList;
  static deserializeBinaryFromReader(message: RelevancyList, reader: jspb.BinaryReader): RelevancyList;
}

export namespace RelevancyList {
  export type AsObject = {
    relevancysList: Array<Relevancy.AsObject>,
  }
}

export class Ontology extends jspb.Message {
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
  toObject(includeInstance?: boolean): Ontology.AsObject;
  static toObject(includeInstance: boolean, msg: Ontology): Ontology.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Ontology, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Ontology;
  static deserializeBinaryFromReader(message: Ontology, reader: jspb.BinaryReader): Ontology;
}

export namespace Ontology {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class OntologyQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologyQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OntologyQuery): OntologyQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologyQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologyQuery;
  static deserializeBinaryFromReader(message: OntologyQuery, reader: jspb.BinaryReader): OntologyQuery;
}

export namespace OntologyQuery {
  export type AsObject = {
  }
}

export class OntologyQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologyQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OntologyQueryInspector): OntologyQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologyQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologyQueryInspector;
  static deserializeBinaryFromReader(message: OntologyQueryInspector, reader: jspb.BinaryReader): OntologyQueryInspector;
}

export namespace OntologyQueryInspector {
  export type AsObject = {
  }
}

export class OntologyForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologyForm.AsObject;
  static toObject(includeInstance: boolean, msg: OntologyForm): OntologyForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologyForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologyForm;
  static deserializeBinaryFromReader(message: OntologyForm, reader: jspb.BinaryReader): OntologyForm;
}

export namespace OntologyForm {
  export type AsObject = {
  }
}

export class OntologySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OntologySearchOrder): OntologySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologySearchOrder;
  static deserializeBinaryFromReader(message: OntologySearchOrder, reader: jspb.BinaryReader): OntologySearchOrder;
}

export namespace OntologySearchOrder {
  export type AsObject = {
  }
}

export class OntologySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologySearch.AsObject;
  static toObject(includeInstance: boolean, msg: OntologySearch): OntologySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologySearch;
  static deserializeBinaryFromReader(message: OntologySearch, reader: jspb.BinaryReader): OntologySearch;
}

export namespace OntologySearch {
  export type AsObject = {
  }
}

export class OntologySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: OntologySearchResults): OntologySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologySearchResults;
  static deserializeBinaryFromReader(message: OntologySearchResults, reader: jspb.BinaryReader): OntologySearchResults;
}

export namespace OntologySearchResults {
  export type AsObject = {
  }
}

export class OntologyList extends jspb.Message {
  clearOntologiesList(): void;
  getOntologiesList(): Array<Ontology>;
  setOntologiesList(value: Array<Ontology>): void;
  addOntologies(value?: Ontology, index?: number): Ontology;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologyList.AsObject;
  static toObject(includeInstance: boolean, msg: OntologyList): OntologyList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologyList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologyList;
  static deserializeBinaryFromReader(message: OntologyList, reader: jspb.BinaryReader): OntologyList;
}

export namespace OntologyList {
  export type AsObject = {
    ontologiesList: Array<Ontology.AsObject>,
  }
}

export class OntologyNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologyNode.AsObject;
  static toObject(includeInstance: boolean, msg: OntologyNode): OntologyNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologyNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologyNode;
  static deserializeBinaryFromReader(message: OntologyNode, reader: jspb.BinaryReader): OntologyNode;
}

export namespace OntologyNode {
  export type AsObject = {
  }
}

export class OntologyNodeList extends jspb.Message {
  clearOntologyNodesList(): void;
  getOntologyNodesList(): Array<OntologyNode>;
  setOntologyNodesList(value: Array<OntologyNode>): void;
  addOntologyNodes(value?: OntologyNode, index?: number): OntologyNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OntologyNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: OntologyNodeList): OntologyNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OntologyNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OntologyNodeList;
  static deserializeBinaryFromReader(message: OntologyNodeList, reader: jspb.BinaryReader): OntologyNodeList;
}

export namespace OntologyNodeList {
  export type AsObject = {
    ontologyNodesList: Array<OntologyNode.AsObject>,
  }
}

export class GetSubjectHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubjectHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubjectHierarchyIdReply): GetSubjectHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubjectHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubjectHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetSubjectHierarchyIdReply, reader: jspb.BinaryReader): GetSubjectHierarchyIdReply;
}

export namespace GetSubjectHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetSubjectHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubjectHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubjectHierarchyIdRequest): GetSubjectHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubjectHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubjectHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetSubjectHierarchyIdRequest, reader: jspb.BinaryReader): GetSubjectHierarchyIdRequest;
}

export namespace GetSubjectHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetSubjectHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubjectHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubjectHierarchyReply): GetSubjectHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubjectHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubjectHierarchyReply;
  static deserializeBinaryFromReader(message: GetSubjectHierarchyReply, reader: jspb.BinaryReader): GetSubjectHierarchyReply;
}

export namespace GetSubjectHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetSubjectHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubjectHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubjectHierarchyRequest): GetSubjectHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubjectHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubjectHierarchyRequest;
  static deserializeBinaryFromReader(message: GetSubjectHierarchyRequest, reader: jspb.BinaryReader): GetSubjectHierarchyRequest;
}

export namespace GetSubjectHierarchyRequest {
  export type AsObject = {
  }
}

export class CanModifySubjectHierarchyReply extends jspb.Message {
  getCanModifySubjectHierarchy(): boolean;
  setCanModifySubjectHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifySubjectHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifySubjectHierarchyReply): CanModifySubjectHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifySubjectHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifySubjectHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifySubjectHierarchyReply, reader: jspb.BinaryReader): CanModifySubjectHierarchyReply;
}

export namespace CanModifySubjectHierarchyReply {
  export type AsObject = {
    canModifySubjectHierarchy: boolean,
  }
}

export class CanModifySubjectHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifySubjectHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifySubjectHierarchyRequest): CanModifySubjectHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifySubjectHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifySubjectHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifySubjectHierarchyRequest, reader: jspb.BinaryReader): CanModifySubjectHierarchyRequest;
}

export namespace CanModifySubjectHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootSubjectReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootSubjectReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootSubjectReply): AddRootSubjectReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootSubjectReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootSubjectReply;
  static deserializeBinaryFromReader(message: AddRootSubjectReply, reader: jspb.BinaryReader): AddRootSubjectReply;
}

export namespace AddRootSubjectReply {
  export type AsObject = {
  }
}

export class AddRootSubjectRequest extends jspb.Message {
  hasSubjectId(): boolean;
  clearSubjectId(): void;
  getSubjectId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSubjectId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootSubjectRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootSubjectRequest): AddRootSubjectRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootSubjectRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootSubjectRequest;
  static deserializeBinaryFromReader(message: AddRootSubjectRequest, reader: jspb.BinaryReader): AddRootSubjectRequest;
}

export namespace AddRootSubjectRequest {
  export type AsObject = {
    subjectId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootSubjectReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootSubjectReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootSubjectReply): RemoveRootSubjectReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootSubjectReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootSubjectReply;
  static deserializeBinaryFromReader(message: RemoveRootSubjectReply, reader: jspb.BinaryReader): RemoveRootSubjectReply;
}

export namespace RemoveRootSubjectReply {
  export type AsObject = {
  }
}

export class RemoveRootSubjectRequest extends jspb.Message {
  hasSubjectId(): boolean;
  clearSubjectId(): void;
  getSubjectId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSubjectId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootSubjectRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootSubjectRequest): RemoveRootSubjectRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootSubjectRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootSubjectRequest;
  static deserializeBinaryFromReader(message: RemoveRootSubjectRequest, reader: jspb.BinaryReader): RemoveRootSubjectRequest;
}

export namespace RemoveRootSubjectRequest {
  export type AsObject = {
    subjectId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildSubjectReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildSubjectReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildSubjectReply): AddChildSubjectReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildSubjectReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildSubjectReply;
  static deserializeBinaryFromReader(message: AddChildSubjectReply, reader: jspb.BinaryReader): AddChildSubjectReply;
}

export namespace AddChildSubjectReply {
  export type AsObject = {
  }
}

export class AddChildSubjectRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSubjectId(): boolean;
  clearSubjectId(): void;
  getSubjectId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSubjectId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildSubjectRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildSubjectRequest): AddChildSubjectRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildSubjectRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildSubjectRequest;
  static deserializeBinaryFromReader(message: AddChildSubjectRequest, reader: jspb.BinaryReader): AddChildSubjectRequest;
}

export namespace AddChildSubjectRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    subjectId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildSubjectReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildSubjectReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildSubjectReply): RemoveChildSubjectReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildSubjectReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildSubjectReply;
  static deserializeBinaryFromReader(message: RemoveChildSubjectReply, reader: jspb.BinaryReader): RemoveChildSubjectReply;
}

export namespace RemoveChildSubjectReply {
  export type AsObject = {
  }
}

export class RemoveChildSubjectRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasSubjectId(): boolean;
  clearSubjectId(): void;
  getSubjectId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSubjectId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildSubjectRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildSubjectRequest): RemoveChildSubjectRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildSubjectRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildSubjectRequest;
  static deserializeBinaryFromReader(message: RemoveChildSubjectRequest, reader: jspb.BinaryReader): RemoveChildSubjectRequest;
}

export namespace RemoveChildSubjectRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    subjectId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildSubjectsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildSubjectsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildSubjectsReply): RemoveChildSubjectsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildSubjectsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildSubjectsReply;
  static deserializeBinaryFromReader(message: RemoveChildSubjectsReply, reader: jspb.BinaryReader): RemoveChildSubjectsReply;
}

export namespace RemoveChildSubjectsReply {
  export type AsObject = {
  }
}

export class RemoveChildSubjectsRequest extends jspb.Message {
  hasSubjectId(): boolean;
  clearSubjectId(): void;
  getSubjectId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSubjectId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildSubjectsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildSubjectsRequest): RemoveChildSubjectsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildSubjectsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildSubjectsRequest;
  static deserializeBinaryFromReader(message: RemoveChildSubjectsRequest, reader: jspb.BinaryReader): RemoveChildSubjectsRequest;
}

export namespace RemoveChildSubjectsRequest {
  export type AsObject = {
    subjectId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

