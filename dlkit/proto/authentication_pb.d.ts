// package: dlkit.proto.authentication
// file: dlkit/proto/authentication.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";

export class Agent extends jspb.Message {
  hasAgency(): boolean;
  clearAgency(): void;
  getAgency(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setAgency(value?: dlkit_proto_osid_pb.OsidCatalog): void;

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
  toObject(includeInstance?: boolean): Agent.AsObject;
  static toObject(includeInstance: boolean, msg: Agent): Agent.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Agent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Agent;
  static deserializeBinaryFromReader(message: Agent, reader: jspb.BinaryReader): Agent;
}

export namespace Agent {
  export type AsObject = {
    agency?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class AgentQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AgentQuery): AgentQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentQuery;
  static deserializeBinaryFromReader(message: AgentQuery, reader: jspb.BinaryReader): AgentQuery;
}

export namespace AgentQuery {
  export type AsObject = {
  }
}

export class AgentQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AgentQueryInspector): AgentQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentQueryInspector;
  static deserializeBinaryFromReader(message: AgentQueryInspector, reader: jspb.BinaryReader): AgentQueryInspector;
}

export namespace AgentQueryInspector {
  export type AsObject = {
  }
}

export class AgentForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentForm.AsObject;
  static toObject(includeInstance: boolean, msg: AgentForm): AgentForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentForm;
  static deserializeBinaryFromReader(message: AgentForm, reader: jspb.BinaryReader): AgentForm;
}

export namespace AgentForm {
  export type AsObject = {
  }
}

export class AgentSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AgentSearchOrder): AgentSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentSearchOrder;
  static deserializeBinaryFromReader(message: AgentSearchOrder, reader: jspb.BinaryReader): AgentSearchOrder;
}

export namespace AgentSearchOrder {
  export type AsObject = {
  }
}

export class AgentSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentSearch.AsObject;
  static toObject(includeInstance: boolean, msg: AgentSearch): AgentSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentSearch;
  static deserializeBinaryFromReader(message: AgentSearch, reader: jspb.BinaryReader): AgentSearch;
}

export namespace AgentSearch {
  export type AsObject = {
  }
}

export class AgentSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AgentSearchResults): AgentSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentSearchResults;
  static deserializeBinaryFromReader(message: AgentSearchResults, reader: jspb.BinaryReader): AgentSearchResults;
}

export namespace AgentSearchResults {
  export type AsObject = {
  }
}

export class AgentList extends jspb.Message {
  clearAgentsList(): void;
  getAgentsList(): Array<Agent>;
  setAgentsList(value: Array<Agent>): void;
  addAgents(value?: Agent, index?: number): Agent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgentList.AsObject;
  static toObject(includeInstance: boolean, msg: AgentList): AgentList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgentList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgentList;
  static deserializeBinaryFromReader(message: AgentList, reader: jspb.BinaryReader): AgentList;
}

export namespace AgentList {
  export type AsObject = {
    agentsList: Array<Agent.AsObject>,
  }
}

export class Agency extends jspb.Message {
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
  toObject(includeInstance?: boolean): Agency.AsObject;
  static toObject(includeInstance: boolean, msg: Agency): Agency.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Agency, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Agency;
  static deserializeBinaryFromReader(message: Agency, reader: jspb.BinaryReader): Agency;
}

export namespace Agency {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class AgencyQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencyQuery.AsObject;
  static toObject(includeInstance: boolean, msg: AgencyQuery): AgencyQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencyQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencyQuery;
  static deserializeBinaryFromReader(message: AgencyQuery, reader: jspb.BinaryReader): AgencyQuery;
}

export namespace AgencyQuery {
  export type AsObject = {
  }
}

export class AgencyQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencyQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: AgencyQueryInspector): AgencyQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencyQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencyQueryInspector;
  static deserializeBinaryFromReader(message: AgencyQueryInspector, reader: jspb.BinaryReader): AgencyQueryInspector;
}

export namespace AgencyQueryInspector {
  export type AsObject = {
  }
}

export class AgencyForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencyForm.AsObject;
  static toObject(includeInstance: boolean, msg: AgencyForm): AgencyForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencyForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencyForm;
  static deserializeBinaryFromReader(message: AgencyForm, reader: jspb.BinaryReader): AgencyForm;
}

export namespace AgencyForm {
  export type AsObject = {
  }
}

export class AgencySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: AgencySearchOrder): AgencySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencySearchOrder;
  static deserializeBinaryFromReader(message: AgencySearchOrder, reader: jspb.BinaryReader): AgencySearchOrder;
}

export namespace AgencySearchOrder {
  export type AsObject = {
  }
}

export class AgencySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencySearch.AsObject;
  static toObject(includeInstance: boolean, msg: AgencySearch): AgencySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencySearch;
  static deserializeBinaryFromReader(message: AgencySearch, reader: jspb.BinaryReader): AgencySearch;
}

export namespace AgencySearch {
  export type AsObject = {
  }
}

export class AgencySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: AgencySearchResults): AgencySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencySearchResults;
  static deserializeBinaryFromReader(message: AgencySearchResults, reader: jspb.BinaryReader): AgencySearchResults;
}

export namespace AgencySearchResults {
  export type AsObject = {
  }
}

export class AgencyList extends jspb.Message {
  clearAgenciesList(): void;
  getAgenciesList(): Array<Agency>;
  setAgenciesList(value: Array<Agency>): void;
  addAgencies(value?: Agency, index?: number): Agency;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencyList.AsObject;
  static toObject(includeInstance: boolean, msg: AgencyList): AgencyList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencyList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencyList;
  static deserializeBinaryFromReader(message: AgencyList, reader: jspb.BinaryReader): AgencyList;
}

export namespace AgencyList {
  export type AsObject = {
    agenciesList: Array<Agency.AsObject>,
  }
}

export class AgencyNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencyNode.AsObject;
  static toObject(includeInstance: boolean, msg: AgencyNode): AgencyNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencyNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencyNode;
  static deserializeBinaryFromReader(message: AgencyNode, reader: jspb.BinaryReader): AgencyNode;
}

export namespace AgencyNode {
  export type AsObject = {
  }
}

export class AgencyNodeList extends jspb.Message {
  clearAgencyNodesList(): void;
  getAgencyNodesList(): Array<AgencyNode>;
  setAgencyNodesList(value: Array<AgencyNode>): void;
  addAgencyNodes(value?: AgencyNode, index?: number): AgencyNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AgencyNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: AgencyNodeList): AgencyNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AgencyNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AgencyNodeList;
  static deserializeBinaryFromReader(message: AgencyNodeList, reader: jspb.BinaryReader): AgencyNodeList;
}

export namespace AgencyNodeList {
  export type AsObject = {
    agencyNodesList: Array<AgencyNode.AsObject>,
  }
}

export class GetAgencyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgencyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgencyIdReply): GetAgencyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgencyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgencyIdReply;
  static deserializeBinaryFromReader(message: GetAgencyIdReply, reader: jspb.BinaryReader): GetAgencyIdReply;
}

export namespace GetAgencyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAgencyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgencyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgencyIdRequest): GetAgencyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgencyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgencyIdRequest;
  static deserializeBinaryFromReader(message: GetAgencyIdRequest, reader: jspb.BinaryReader): GetAgencyIdRequest;
}

export namespace GetAgencyIdRequest {
  export type AsObject = {
  }
}

export class GetAgencyReply extends jspb.Message {
  hasAgency(): boolean;
  clearAgency(): void;
  getAgency(): Agency | undefined;
  setAgency(value?: Agency): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgencyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgencyReply): GetAgencyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgencyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgencyReply;
  static deserializeBinaryFromReader(message: GetAgencyReply, reader: jspb.BinaryReader): GetAgencyReply;
}

export namespace GetAgencyReply {
  export type AsObject = {
    agency?: Agency.AsObject,
  }
}

export class GetAgencyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgencyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgencyRequest): GetAgencyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgencyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgencyRequest;
  static deserializeBinaryFromReader(message: GetAgencyRequest, reader: jspb.BinaryReader): GetAgencyRequest;
}

export namespace GetAgencyRequest {
  export type AsObject = {
  }
}

export class CanLookupAgentsReply extends jspb.Message {
  getCanLookupAgents(): boolean;
  setCanLookupAgents(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAgentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAgentsReply): CanLookupAgentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAgentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAgentsReply;
  static deserializeBinaryFromReader(message: CanLookupAgentsReply, reader: jspb.BinaryReader): CanLookupAgentsReply;
}

export namespace CanLookupAgentsReply {
  export type AsObject = {
    canLookupAgents: boolean,
  }
}

export class CanLookupAgentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupAgentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupAgentsRequest): CanLookupAgentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupAgentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupAgentsRequest;
  static deserializeBinaryFromReader(message: CanLookupAgentsRequest, reader: jspb.BinaryReader): CanLookupAgentsRequest;
}

export namespace CanLookupAgentsRequest {
  export type AsObject = {
  }
}

export class UseComparativeAgentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAgentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAgentViewReply): UseComparativeAgentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAgentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAgentViewReply;
  static deserializeBinaryFromReader(message: UseComparativeAgentViewReply, reader: jspb.BinaryReader): UseComparativeAgentViewReply;
}

export namespace UseComparativeAgentViewReply {
  export type AsObject = {
  }
}

export class UseComparativeAgentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeAgentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeAgentViewRequest): UseComparativeAgentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeAgentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeAgentViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeAgentViewRequest, reader: jspb.BinaryReader): UseComparativeAgentViewRequest;
}

export namespace UseComparativeAgentViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryAgentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAgentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAgentViewReply): UsePlenaryAgentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAgentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAgentViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryAgentViewReply, reader: jspb.BinaryReader): UsePlenaryAgentViewReply;
}

export namespace UsePlenaryAgentViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryAgentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryAgentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryAgentViewRequest): UsePlenaryAgentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryAgentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryAgentViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryAgentViewRequest, reader: jspb.BinaryReader): UsePlenaryAgentViewRequest;
}

export namespace UsePlenaryAgentViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedAgencyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedAgencyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedAgencyViewReply): UseFederatedAgencyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedAgencyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedAgencyViewReply;
  static deserializeBinaryFromReader(message: UseFederatedAgencyViewReply, reader: jspb.BinaryReader): UseFederatedAgencyViewReply;
}

export namespace UseFederatedAgencyViewReply {
  export type AsObject = {
  }
}

export class UseFederatedAgencyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedAgencyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedAgencyViewRequest): UseFederatedAgencyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedAgencyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedAgencyViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedAgencyViewRequest, reader: jspb.BinaryReader): UseFederatedAgencyViewRequest;
}

export namespace UseFederatedAgencyViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedAgencyViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedAgencyViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedAgencyViewReply): UseIsolatedAgencyViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedAgencyViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedAgencyViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedAgencyViewReply, reader: jspb.BinaryReader): UseIsolatedAgencyViewReply;
}

export namespace UseIsolatedAgencyViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedAgencyViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedAgencyViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedAgencyViewRequest): UseIsolatedAgencyViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedAgencyViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedAgencyViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedAgencyViewRequest, reader: jspb.BinaryReader): UseIsolatedAgencyViewRequest;
}

export namespace UseIsolatedAgencyViewRequest {
  export type AsObject = {
  }
}

export class GetAgentReply extends jspb.Message {
  hasAgent(): boolean;
  clearAgent(): void;
  getAgent(): Agent | undefined;
  setAgent(value?: Agent): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentReply): GetAgentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentReply;
  static deserializeBinaryFromReader(message: GetAgentReply, reader: jspb.BinaryReader): GetAgentReply;
}

export namespace GetAgentReply {
  export type AsObject = {
    agent?: Agent.AsObject,
  }
}

export class GetAgentRequest extends jspb.Message {
  hasAgentId(): boolean;
  clearAgentId(): void;
  getAgentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentRequest): GetAgentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentRequest;
  static deserializeBinaryFromReader(message: GetAgentRequest, reader: jspb.BinaryReader): GetAgentRequest;
}

export namespace GetAgentRequest {
  export type AsObject = {
    agentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAgentsByIdsRequest extends jspb.Message {
  clearAgentIdsList(): void;
  getAgentIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setAgentIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addAgentIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentsByIdsRequest): GetAgentsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentsByIdsRequest;
  static deserializeBinaryFromReader(message: GetAgentsByIdsRequest, reader: jspb.BinaryReader): GetAgentsByIdsRequest;
}

export namespace GetAgentsByIdsRequest {
  export type AsObject = {
    agentIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetAgentsByGenusTypeRequest extends jspb.Message {
  hasAgentGenusType(): boolean;
  clearAgentGenusType(): void;
  getAgentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAgentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentsByGenusTypeRequest): GetAgentsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAgentsByGenusTypeRequest, reader: jspb.BinaryReader): GetAgentsByGenusTypeRequest;
}

export namespace GetAgentsByGenusTypeRequest {
  export type AsObject = {
    agentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAgentsByParentGenusTypeRequest extends jspb.Message {
  hasAgentGenusType(): boolean;
  clearAgentGenusType(): void;
  getAgentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAgentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentsByParentGenusTypeRequest): GetAgentsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetAgentsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetAgentsByParentGenusTypeRequest;
}

export namespace GetAgentsByParentGenusTypeRequest {
  export type AsObject = {
    agentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAgentsByRecordTypeRequest extends jspb.Message {
  hasAgentRecordType(): boolean;
  clearAgentRecordType(): void;
  getAgentRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setAgentRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentsByRecordTypeRequest): GetAgentsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetAgentsByRecordTypeRequest, reader: jspb.BinaryReader): GetAgentsByRecordTypeRequest;
}

export namespace GetAgentsByRecordTypeRequest {
  export type AsObject = {
    agentRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetAgentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAgentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAgentsRequest): GetAgentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAgentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAgentsRequest;
  static deserializeBinaryFromReader(message: GetAgentsRequest, reader: jspb.BinaryReader): GetAgentsRequest;
}

export namespace GetAgentsRequest {
  export type AsObject = {
  }
}

