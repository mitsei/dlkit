// package: dlkit.proto.logging
// file: dlkit/proto/logging.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class LogEntry extends jspb.Message {
  hasAgent(): boolean;
  clearAgent(): void;
  getAgent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAgent(value?: dlkit_primordium_id_primitives_pb.Id): void;

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

  hasLog(): boolean;
  clearLog(): void;
  getLog(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setLog(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasPriority(): boolean;
  clearPriority(): void;
  getPriority(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setPriority(value?: dlkit_primordium_type_primitives_pb.Type): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasTimestamp(): boolean;
  clearTimestamp(): void;
  getTimestamp(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTimestamp(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntry.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntry): LogEntry.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntry, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntry;
  static deserializeBinaryFromReader(message: LogEntry, reader: jspb.BinaryReader): LogEntry;
}

export namespace LogEntry {
  export type AsObject = {
    agent?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    log?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    priority?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    timestamp?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class LogEntryQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntryQuery.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntryQuery): LogEntryQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntryQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntryQuery;
  static deserializeBinaryFromReader(message: LogEntryQuery, reader: jspb.BinaryReader): LogEntryQuery;
}

export namespace LogEntryQuery {
  export type AsObject = {
  }
}

export class LogEntryQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntryQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntryQueryInspector): LogEntryQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntryQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntryQueryInspector;
  static deserializeBinaryFromReader(message: LogEntryQueryInspector, reader: jspb.BinaryReader): LogEntryQueryInspector;
}

export namespace LogEntryQueryInspector {
  export type AsObject = {
  }
}

export class LogEntryForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntryForm.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntryForm): LogEntryForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntryForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntryForm;
  static deserializeBinaryFromReader(message: LogEntryForm, reader: jspb.BinaryReader): LogEntryForm;
}

export namespace LogEntryForm {
  export type AsObject = {
  }
}

export class LogEntrySearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntrySearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntrySearchOrder): LogEntrySearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntrySearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntrySearchOrder;
  static deserializeBinaryFromReader(message: LogEntrySearchOrder, reader: jspb.BinaryReader): LogEntrySearchOrder;
}

export namespace LogEntrySearchOrder {
  export type AsObject = {
  }
}

export class LogEntrySearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntrySearch.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntrySearch): LogEntrySearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntrySearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntrySearch;
  static deserializeBinaryFromReader(message: LogEntrySearch, reader: jspb.BinaryReader): LogEntrySearch;
}

export namespace LogEntrySearch {
  export type AsObject = {
  }
}

export class LogEntrySearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntrySearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntrySearchResults): LogEntrySearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntrySearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntrySearchResults;
  static deserializeBinaryFromReader(message: LogEntrySearchResults, reader: jspb.BinaryReader): LogEntrySearchResults;
}

export namespace LogEntrySearchResults {
  export type AsObject = {
  }
}

export class LogEntryList extends jspb.Message {
  clearLogEntriesList(): void;
  getLogEntriesList(): Array<LogEntry>;
  setLogEntriesList(value: Array<LogEntry>): void;
  addLogEntries(value?: LogEntry, index?: number): LogEntry;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogEntryList.AsObject;
  static toObject(includeInstance: boolean, msg: LogEntryList): LogEntryList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogEntryList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogEntryList;
  static deserializeBinaryFromReader(message: LogEntryList, reader: jspb.BinaryReader): LogEntryList;
}

export namespace LogEntryList {
  export type AsObject = {
    logEntriesList: Array<LogEntry.AsObject>,
  }
}

export class Log extends jspb.Message {
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
  toObject(includeInstance?: boolean): Log.AsObject;
  static toObject(includeInstance: boolean, msg: Log): Log.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Log, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Log;
  static deserializeBinaryFromReader(message: Log, reader: jspb.BinaryReader): Log;
}

export namespace Log {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class LogQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogQuery.AsObject;
  static toObject(includeInstance: boolean, msg: LogQuery): LogQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogQuery;
  static deserializeBinaryFromReader(message: LogQuery, reader: jspb.BinaryReader): LogQuery;
}

export namespace LogQuery {
  export type AsObject = {
  }
}

export class LogQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: LogQueryInspector): LogQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogQueryInspector;
  static deserializeBinaryFromReader(message: LogQueryInspector, reader: jspb.BinaryReader): LogQueryInspector;
}

export namespace LogQueryInspector {
  export type AsObject = {
  }
}

export class LogForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogForm.AsObject;
  static toObject(includeInstance: boolean, msg: LogForm): LogForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogForm;
  static deserializeBinaryFromReader(message: LogForm, reader: jspb.BinaryReader): LogForm;
}

export namespace LogForm {
  export type AsObject = {
  }
}

export class LogSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: LogSearchOrder): LogSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogSearchOrder;
  static deserializeBinaryFromReader(message: LogSearchOrder, reader: jspb.BinaryReader): LogSearchOrder;
}

export namespace LogSearchOrder {
  export type AsObject = {
  }
}

export class LogSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogSearch.AsObject;
  static toObject(includeInstance: boolean, msg: LogSearch): LogSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogSearch;
  static deserializeBinaryFromReader(message: LogSearch, reader: jspb.BinaryReader): LogSearch;
}

export namespace LogSearch {
  export type AsObject = {
  }
}

export class LogSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: LogSearchResults): LogSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogSearchResults;
  static deserializeBinaryFromReader(message: LogSearchResults, reader: jspb.BinaryReader): LogSearchResults;
}

export namespace LogSearchResults {
  export type AsObject = {
  }
}

export class LogList extends jspb.Message {
  clearLogsList(): void;
  getLogsList(): Array<Log>;
  setLogsList(value: Array<Log>): void;
  addLogs(value?: Log, index?: number): Log;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogList.AsObject;
  static toObject(includeInstance: boolean, msg: LogList): LogList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogList;
  static deserializeBinaryFromReader(message: LogList, reader: jspb.BinaryReader): LogList;
}

export namespace LogList {
  export type AsObject = {
    logsList: Array<Log.AsObject>,
  }
}

export class LogNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogNode.AsObject;
  static toObject(includeInstance: boolean, msg: LogNode): LogNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogNode;
  static deserializeBinaryFromReader(message: LogNode, reader: jspb.BinaryReader): LogNode;
}

export namespace LogNode {
  export type AsObject = {
  }
}

export class LogNodeList extends jspb.Message {
  clearLogNodesList(): void;
  getLogNodesList(): Array<LogNode>;
  setLogNodesList(value: Array<LogNode>): void;
  addLogNodes(value?: LogNode, index?: number): LogNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: LogNodeList): LogNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogNodeList;
  static deserializeBinaryFromReader(message: LogNodeList, reader: jspb.BinaryReader): LogNodeList;
}

export namespace LogNodeList {
  export type AsObject = {
    logNodesList: Array<LogNode.AsObject>,
  }
}

export class GetLogIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogIdReply): GetLogIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogIdReply;
  static deserializeBinaryFromReader(message: GetLogIdReply, reader: jspb.BinaryReader): GetLogIdReply;
}

export namespace GetLogIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogIdRequest): GetLogIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogIdRequest;
  static deserializeBinaryFromReader(message: GetLogIdRequest, reader: jspb.BinaryReader): GetLogIdRequest;
}

export namespace GetLogIdRequest {
  export type AsObject = {
  }
}

export class GetLogReply extends jspb.Message {
  hasLog(): boolean;
  clearLog(): void;
  getLog(): Log | undefined;
  setLog(value?: Log): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogReply): GetLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogReply;
  static deserializeBinaryFromReader(message: GetLogReply, reader: jspb.BinaryReader): GetLogReply;
}

export namespace GetLogReply {
  export type AsObject = {
    log?: Log.AsObject,
  }
}

export class GetLogRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogRequest): GetLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogRequest;
  static deserializeBinaryFromReader(message: GetLogRequest, reader: jspb.BinaryReader): GetLogRequest;
}

export namespace GetLogRequest {
  export type AsObject = {
  }
}

export class CanLogReply extends jspb.Message {
  getCanLog(): boolean;
  setCanLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLogReply): CanLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLogReply;
  static deserializeBinaryFromReader(message: CanLogReply, reader: jspb.BinaryReader): CanLogReply;
}

export namespace CanLogReply {
  export type AsObject = {
    canLog: boolean,
  }
}

export class CanLogRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLogRequest): CanLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLogRequest;
  static deserializeBinaryFromReader(message: CanLogRequest, reader: jspb.BinaryReader): CanLogRequest;
}

export namespace CanLogRequest {
  export type AsObject = {
  }
}

export class LogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogReply.AsObject;
  static toObject(includeInstance: boolean, msg: LogReply): LogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogReply;
  static deserializeBinaryFromReader(message: LogReply, reader: jspb.BinaryReader): LogReply;
}

export namespace LogReply {
  export type AsObject = {
  }
}

export class LogRequest extends jspb.Message {
  getContent(): Uint8Array | string;
  getContent_asU8(): Uint8Array;
  getContent_asB64(): string;
  setContent(value: Uint8Array | string): void;

  hasContentType(): boolean;
  clearContentType(): void;
  getContentType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setContentType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: LogRequest): LogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogRequest;
  static deserializeBinaryFromReader(message: LogRequest, reader: jspb.BinaryReader): LogRequest;
}

export namespace LogRequest {
  export type AsObject = {
    content: Uint8Array | string,
    contentType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class LogAtPriorityReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogAtPriorityReply.AsObject;
  static toObject(includeInstance: boolean, msg: LogAtPriorityReply): LogAtPriorityReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogAtPriorityReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogAtPriorityReply;
  static deserializeBinaryFromReader(message: LogAtPriorityReply, reader: jspb.BinaryReader): LogAtPriorityReply;
}

export namespace LogAtPriorityReply {
  export type AsObject = {
  }
}

export class LogAtPriorityRequest extends jspb.Message {
  getContent(): Uint8Array | string;
  getContent_asU8(): Uint8Array;
  getContent_asB64(): string;
  setContent(value: Uint8Array | string): void;

  hasContentType(): boolean;
  clearContentType(): void;
  getContentType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setContentType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasPriorityType(): boolean;
  clearPriorityType(): void;
  getPriorityType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setPriorityType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogAtPriorityRequest.AsObject;
  static toObject(includeInstance: boolean, msg: LogAtPriorityRequest): LogAtPriorityRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogAtPriorityRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogAtPriorityRequest;
  static deserializeBinaryFromReader(message: LogAtPriorityRequest, reader: jspb.BinaryReader): LogAtPriorityRequest;
}

export namespace LogAtPriorityRequest {
  export type AsObject = {
    content: Uint8Array | string,
    contentType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    priorityType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogEntryFormReply extends jspb.Message {
  hasLogEntryForm(): boolean;
  clearLogEntryForm(): void;
  getLogEntryForm(): LogEntryForm | undefined;
  setLogEntryForm(value?: LogEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryFormReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryFormReply): GetLogEntryFormReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryFormReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryFormReply;
  static deserializeBinaryFromReader(message: GetLogEntryFormReply, reader: jspb.BinaryReader): GetLogEntryFormReply;
}

export namespace GetLogEntryFormReply {
  export type AsObject = {
    logEntryForm?: LogEntryForm.AsObject,
  }
}

export class GetLogEntryFormRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryFormRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryFormRequest): GetLogEntryFormRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryFormRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryFormRequest;
  static deserializeBinaryFromReader(message: GetLogEntryFormRequest, reader: jspb.BinaryReader): GetLogEntryFormRequest;
}

export namespace GetLogEntryFormRequest {
  export type AsObject = {
  }
}

export class CreateLogEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateLogEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateLogEntryReply): CreateLogEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateLogEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateLogEntryReply;
  static deserializeBinaryFromReader(message: CreateLogEntryReply, reader: jspb.BinaryReader): CreateLogEntryReply;
}

export namespace CreateLogEntryReply {
  export type AsObject = {
  }
}

export class CreateLogEntryRequest extends jspb.Message {
  hasLogEntryForm(): boolean;
  clearLogEntryForm(): void;
  getLogEntryForm(): LogEntryForm | undefined;
  setLogEntryForm(value?: LogEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateLogEntryRequest): CreateLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateLogEntryRequest;
  static deserializeBinaryFromReader(message: CreateLogEntryRequest, reader: jspb.BinaryReader): CreateLogEntryRequest;
}

export namespace CreateLogEntryRequest {
  export type AsObject = {
    logEntryForm?: LogEntryForm.AsObject,
  }
}

export class CanReadLogReply extends jspb.Message {
  getCanReadLog(): boolean;
  setCanReadLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanReadLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanReadLogReply): CanReadLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanReadLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanReadLogReply;
  static deserializeBinaryFromReader(message: CanReadLogReply, reader: jspb.BinaryReader): CanReadLogReply;
}

export namespace CanReadLogReply {
  export type AsObject = {
    canReadLog: boolean,
  }
}

export class CanReadLogRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanReadLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanReadLogRequest): CanReadLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanReadLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanReadLogRequest;
  static deserializeBinaryFromReader(message: CanReadLogRequest, reader: jspb.BinaryReader): CanReadLogRequest;
}

export namespace CanReadLogRequest {
  export type AsObject = {
  }
}

export class UseComparativeLogEntryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeLogEntryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeLogEntryViewReply): UseComparativeLogEntryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeLogEntryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeLogEntryViewReply;
  static deserializeBinaryFromReader(message: UseComparativeLogEntryViewReply, reader: jspb.BinaryReader): UseComparativeLogEntryViewReply;
}

export namespace UseComparativeLogEntryViewReply {
  export type AsObject = {
  }
}

export class UseComparativeLogEntryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeLogEntryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeLogEntryViewRequest): UseComparativeLogEntryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeLogEntryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeLogEntryViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeLogEntryViewRequest, reader: jspb.BinaryReader): UseComparativeLogEntryViewRequest;
}

export namespace UseComparativeLogEntryViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryLogEntryViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryLogEntryViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryLogEntryViewReply): UsePlenaryLogEntryViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryLogEntryViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryLogEntryViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryLogEntryViewReply, reader: jspb.BinaryReader): UsePlenaryLogEntryViewReply;
}

export namespace UsePlenaryLogEntryViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryLogEntryViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryLogEntryViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryLogEntryViewRequest): UsePlenaryLogEntryViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryLogEntryViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryLogEntryViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryLogEntryViewRequest, reader: jspb.BinaryReader): UsePlenaryLogEntryViewRequest;
}

export namespace UsePlenaryLogEntryViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedLogViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedLogViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedLogViewReply): UseFederatedLogViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedLogViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedLogViewReply;
  static deserializeBinaryFromReader(message: UseFederatedLogViewReply, reader: jspb.BinaryReader): UseFederatedLogViewReply;
}

export namespace UseFederatedLogViewReply {
  export type AsObject = {
  }
}

export class UseFederatedLogViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedLogViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedLogViewRequest): UseFederatedLogViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedLogViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedLogViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedLogViewRequest, reader: jspb.BinaryReader): UseFederatedLogViewRequest;
}

export namespace UseFederatedLogViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedLogViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedLogViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedLogViewReply): UseIsolatedLogViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedLogViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedLogViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedLogViewReply, reader: jspb.BinaryReader): UseIsolatedLogViewReply;
}

export namespace UseIsolatedLogViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedLogViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedLogViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedLogViewRequest): UseIsolatedLogViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedLogViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedLogViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedLogViewRequest, reader: jspb.BinaryReader): UseIsolatedLogViewRequest;
}

export namespace UseIsolatedLogViewRequest {
  export type AsObject = {
  }
}

export class GetLogEntryReply extends jspb.Message {
  hasLogEntry(): boolean;
  clearLogEntry(): void;
  getLogEntry(): LogEntry | undefined;
  setLogEntry(value?: LogEntry): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryReply): GetLogEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryReply;
  static deserializeBinaryFromReader(message: GetLogEntryReply, reader: jspb.BinaryReader): GetLogEntryReply;
}

export namespace GetLogEntryReply {
  export type AsObject = {
    logEntry?: LogEntry.AsObject,
  }
}

export class GetLogEntryRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryRequest): GetLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryRequest;
  static deserializeBinaryFromReader(message: GetLogEntryRequest, reader: jspb.BinaryReader): GetLogEntryRequest;
}

export namespace GetLogEntryRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogEntriesByIdsRequest extends jspb.Message {
  clearLogEntryIdsList(): void;
  getLogEntryIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setLogEntryIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addLogEntryIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByIdsRequest): GetLogEntriesByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByIdsRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByIdsRequest, reader: jspb.BinaryReader): GetLogEntriesByIdsRequest;
}

export namespace GetLogEntriesByIdsRequest {
  export type AsObject = {
    logEntryIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetLogEntriesByGenusTypeRequest extends jspb.Message {
  hasLogEntryGenusType(): boolean;
  clearLogEntryGenusType(): void;
  getLogEntryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLogEntryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByGenusTypeRequest): GetLogEntriesByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByGenusTypeRequest, reader: jspb.BinaryReader): GetLogEntriesByGenusTypeRequest;
}

export namespace GetLogEntriesByGenusTypeRequest {
  export type AsObject = {
    logEntryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogEntriesByParentGenusTypeRequest extends jspb.Message {
  hasLogEntryGenusType(): boolean;
  clearLogEntryGenusType(): void;
  getLogEntryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLogEntryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByParentGenusTypeRequest): GetLogEntriesByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByParentGenusTypeRequest, reader: jspb.BinaryReader): GetLogEntriesByParentGenusTypeRequest;
}

export namespace GetLogEntriesByParentGenusTypeRequest {
  export type AsObject = {
    logEntryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogEntriesByRecordTypeRequest extends jspb.Message {
  hasLogEntryGenusType(): boolean;
  clearLogEntryGenusType(): void;
  getLogEntryGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLogEntryGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByRecordTypeRequest): GetLogEntriesByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByRecordTypeRequest, reader: jspb.BinaryReader): GetLogEntriesByRecordTypeRequest;
}

export namespace GetLogEntriesByRecordTypeRequest {
  export type AsObject = {
    logEntryGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogEntriesByPriorityTypeRequest extends jspb.Message {
  hasPriorityType(): boolean;
  clearPriorityType(): void;
  getPriorityType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setPriorityType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByPriorityTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByPriorityTypeRequest): GetLogEntriesByPriorityTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByPriorityTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByPriorityTypeRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByPriorityTypeRequest, reader: jspb.BinaryReader): GetLogEntriesByPriorityTypeRequest;
}

export namespace GetLogEntriesByPriorityTypeRequest {
  export type AsObject = {
    priorityType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogEntriesByDateRequest extends jspb.Message {
  hasEnd(): boolean;
  clearEnd(): void;
  getEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasStart(): boolean;
  clearStart(): void;
  getStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByDateRequest): GetLogEntriesByDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByDateRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByDateRequest, reader: jspb.BinaryReader): GetLogEntriesByDateRequest;
}

export namespace GetLogEntriesByDateRequest {
  export type AsObject = {
    end?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    start?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetLogEntriesByPriorityTypeAndDateRequest extends jspb.Message {
  hasEnd(): boolean;
  clearEnd(): void;
  getEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasPriorityType(): boolean;
  clearPriorityType(): void;
  getPriorityType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setPriorityType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasStart(): boolean;
  clearStart(): void;
  getStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByPriorityTypeAndDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByPriorityTypeAndDateRequest): GetLogEntriesByPriorityTypeAndDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByPriorityTypeAndDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByPriorityTypeAndDateRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByPriorityTypeAndDateRequest, reader: jspb.BinaryReader): GetLogEntriesByPriorityTypeAndDateRequest;
}

export namespace GetLogEntriesByPriorityTypeAndDateRequest {
  export type AsObject = {
    end?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    priorityType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    start?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetLogEntriesForResourceRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesForResourceRequest): GetLogEntriesForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesForResourceRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesForResourceRequest, reader: jspb.BinaryReader): GetLogEntriesForResourceRequest;
}

export namespace GetLogEntriesForResourceRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogEntriesByDateForResourceRequest extends jspb.Message {
  hasEnd(): boolean;
  clearEnd(): void;
  getEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasStart(): boolean;
  clearStart(): void;
  getStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByDateForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByDateForResourceRequest): GetLogEntriesByDateForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByDateForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByDateForResourceRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByDateForResourceRequest, reader: jspb.BinaryReader): GetLogEntriesByDateForResourceRequest;
}

export namespace GetLogEntriesByDateForResourceRequest {
  export type AsObject = {
    end?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    start?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetLogEntriesByPriorityTypeAndDateForResourceRequest extends jspb.Message {
  hasEnd(): boolean;
  clearEnd(): void;
  getEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasPriorityType(): boolean;
  clearPriorityType(): void;
  getPriorityType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setPriorityType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasStart(): boolean;
  clearStart(): void;
  getStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByPriorityTypeAndDateForResourceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByPriorityTypeAndDateForResourceRequest): GetLogEntriesByPriorityTypeAndDateForResourceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByPriorityTypeAndDateForResourceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByPriorityTypeAndDateForResourceRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByPriorityTypeAndDateForResourceRequest, reader: jspb.BinaryReader): GetLogEntriesByPriorityTypeAndDateForResourceRequest;
}

export namespace GetLogEntriesByPriorityTypeAndDateForResourceRequest {
  export type AsObject = {
    end?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    priorityType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    start?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetLogEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesRequest): GetLogEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesRequest, reader: jspb.BinaryReader): GetLogEntriesRequest;
}

export namespace GetLogEntriesRequest {
  export type AsObject = {
  }
}

export class CanSearchLogEntriesReply extends jspb.Message {
  getCanSearchLogEntries(): boolean;
  setCanSearchLogEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchLogEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchLogEntriesReply): CanSearchLogEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchLogEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchLogEntriesReply;
  static deserializeBinaryFromReader(message: CanSearchLogEntriesReply, reader: jspb.BinaryReader): CanSearchLogEntriesReply;
}

export namespace CanSearchLogEntriesReply {
  export type AsObject = {
    canSearchLogEntries: boolean,
  }
}

export class CanSearchLogEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchLogEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchLogEntriesRequest): CanSearchLogEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchLogEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchLogEntriesRequest;
  static deserializeBinaryFromReader(message: CanSearchLogEntriesRequest, reader: jspb.BinaryReader): CanSearchLogEntriesRequest;
}

export namespace CanSearchLogEntriesRequest {
  export type AsObject = {
  }
}

export class GetLogEntryQueryReply extends jspb.Message {
  hasLogEntryQuery(): boolean;
  clearLogEntryQuery(): void;
  getLogEntryQuery(): LogEntryQuery | undefined;
  setLogEntryQuery(value?: LogEntryQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryQueryReply): GetLogEntryQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryQueryReply;
  static deserializeBinaryFromReader(message: GetLogEntryQueryReply, reader: jspb.BinaryReader): GetLogEntryQueryReply;
}

export namespace GetLogEntryQueryReply {
  export type AsObject = {
    logEntryQuery?: LogEntryQuery.AsObject,
  }
}

export class GetLogEntryQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryQueryRequest): GetLogEntryQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryQueryRequest;
  static deserializeBinaryFromReader(message: GetLogEntryQueryRequest, reader: jspb.BinaryReader): GetLogEntryQueryRequest;
}

export namespace GetLogEntryQueryRequest {
  export type AsObject = {
  }
}

export class GetLogEntriesByQueryRequest extends jspb.Message {
  hasLogEntryQuery(): boolean;
  clearLogEntryQuery(): void;
  getLogEntryQuery(): LogEntryQuery | undefined;
  setLogEntryQuery(value?: LogEntryQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByQueryRequest): GetLogEntriesByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByQueryRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByQueryRequest, reader: jspb.BinaryReader): GetLogEntriesByQueryRequest;
}

export namespace GetLogEntriesByQueryRequest {
  export type AsObject = {
    logEntryQuery?: LogEntryQuery.AsObject,
  }
}

export class CanCreateLogEntriesReply extends jspb.Message {
  getCanCreateLogEntries(): boolean;
  setCanCreateLogEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogEntriesReply): CanCreateLogEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogEntriesReply;
  static deserializeBinaryFromReader(message: CanCreateLogEntriesReply, reader: jspb.BinaryReader): CanCreateLogEntriesReply;
}

export namespace CanCreateLogEntriesReply {
  export type AsObject = {
    canCreateLogEntries: boolean,
  }
}

export class CanCreateLogEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogEntriesRequest): CanCreateLogEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogEntriesRequest;
  static deserializeBinaryFromReader(message: CanCreateLogEntriesRequest, reader: jspb.BinaryReader): CanCreateLogEntriesRequest;
}

export namespace CanCreateLogEntriesRequest {
  export type AsObject = {
  }
}

export class CanCreateLogEntryWithRecordTypesReply extends jspb.Message {
  getCanCreateLogEntryWithRecordTypes(): boolean;
  setCanCreateLogEntryWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogEntryWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogEntryWithRecordTypesReply): CanCreateLogEntryWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogEntryWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogEntryWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateLogEntryWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateLogEntryWithRecordTypesReply;
}

export namespace CanCreateLogEntryWithRecordTypesReply {
  export type AsObject = {
    canCreateLogEntryWithRecordTypes: boolean,
  }
}

export class CanCreateLogEntryWithRecordTypesRequest extends jspb.Message {
  clearLogEntryRecordTypesList(): void;
  getLogEntryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setLogEntryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addLogEntryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogEntryWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogEntryWithRecordTypesRequest): CanCreateLogEntryWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogEntryWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogEntryWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateLogEntryWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateLogEntryWithRecordTypesRequest;
}

export namespace CanCreateLogEntryWithRecordTypesRequest {
  export type AsObject = {
    logEntryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetLogEntryFormForCreateReply extends jspb.Message {
  hasLogEntryForm(): boolean;
  clearLogEntryForm(): void;
  getLogEntryForm(): LogEntryForm | undefined;
  setLogEntryForm(value?: LogEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryFormForCreateReply): GetLogEntryFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryFormForCreateReply;
  static deserializeBinaryFromReader(message: GetLogEntryFormForCreateReply, reader: jspb.BinaryReader): GetLogEntryFormForCreateReply;
}

export namespace GetLogEntryFormForCreateReply {
  export type AsObject = {
    logEntryForm?: LogEntryForm.AsObject,
  }
}

export class GetLogEntryFormForCreateRequest extends jspb.Message {
  clearLogEntryRecordTypesList(): void;
  getLogEntryRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setLogEntryRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addLogEntryRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryFormForCreateRequest): GetLogEntryFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetLogEntryFormForCreateRequest, reader: jspb.BinaryReader): GetLogEntryFormForCreateRequest;
}

export namespace GetLogEntryFormForCreateRequest {
  export type AsObject = {
    logEntryRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CanUpdateLogEntriesReply extends jspb.Message {
  getCanUpdateLogEntries(): boolean;
  setCanUpdateLogEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateLogEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateLogEntriesReply): CanUpdateLogEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateLogEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateLogEntriesReply;
  static deserializeBinaryFromReader(message: CanUpdateLogEntriesReply, reader: jspb.BinaryReader): CanUpdateLogEntriesReply;
}

export namespace CanUpdateLogEntriesReply {
  export type AsObject = {
    canUpdateLogEntries: boolean,
  }
}

export class CanUpdateLogEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateLogEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateLogEntriesRequest): CanUpdateLogEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateLogEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateLogEntriesRequest;
  static deserializeBinaryFromReader(message: CanUpdateLogEntriesRequest, reader: jspb.BinaryReader): CanUpdateLogEntriesRequest;
}

export namespace CanUpdateLogEntriesRequest {
  export type AsObject = {
  }
}

export class GetLogEntryFormForUpdateReply extends jspb.Message {
  hasLogEntryForm(): boolean;
  clearLogEntryForm(): void;
  getLogEntryForm(): LogEntryForm | undefined;
  setLogEntryForm(value?: LogEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryFormForUpdateReply): GetLogEntryFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetLogEntryFormForUpdateReply, reader: jspb.BinaryReader): GetLogEntryFormForUpdateReply;
}

export namespace GetLogEntryFormForUpdateReply {
  export type AsObject = {
    logEntryForm?: LogEntryForm.AsObject,
  }
}

export class GetLogEntryFormForUpdateRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryFormForUpdateRequest): GetLogEntryFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetLogEntryFormForUpdateRequest, reader: jspb.BinaryReader): GetLogEntryFormForUpdateRequest;
}

export namespace GetLogEntryFormForUpdateRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateLogEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateLogEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateLogEntryReply): UpdateLogEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateLogEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateLogEntryReply;
  static deserializeBinaryFromReader(message: UpdateLogEntryReply, reader: jspb.BinaryReader): UpdateLogEntryReply;
}

export namespace UpdateLogEntryReply {
  export type AsObject = {
  }
}

export class UpdateLogEntryRequest extends jspb.Message {
  hasLogEntryForm(): boolean;
  clearLogEntryForm(): void;
  getLogEntryForm(): LogEntryForm | undefined;
  setLogEntryForm(value?: LogEntryForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateLogEntryRequest): UpdateLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateLogEntryRequest;
  static deserializeBinaryFromReader(message: UpdateLogEntryRequest, reader: jspb.BinaryReader): UpdateLogEntryRequest;
}

export namespace UpdateLogEntryRequest {
  export type AsObject = {
    logEntryForm?: LogEntryForm.AsObject,
  }
}

export class CanDeleteLogEntriesReply extends jspb.Message {
  getCanDeleteLogEntries(): boolean;
  setCanDeleteLogEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteLogEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteLogEntriesReply): CanDeleteLogEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteLogEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteLogEntriesReply;
  static deserializeBinaryFromReader(message: CanDeleteLogEntriesReply, reader: jspb.BinaryReader): CanDeleteLogEntriesReply;
}

export namespace CanDeleteLogEntriesReply {
  export type AsObject = {
    canDeleteLogEntries: boolean,
  }
}

export class CanDeleteLogEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteLogEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteLogEntriesRequest): CanDeleteLogEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteLogEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteLogEntriesRequest;
  static deserializeBinaryFromReader(message: CanDeleteLogEntriesRequest, reader: jspb.BinaryReader): CanDeleteLogEntriesRequest;
}

export namespace CanDeleteLogEntriesRequest {
  export type AsObject = {
  }
}

export class DeleteLogEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteLogEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteLogEntryReply): DeleteLogEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteLogEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteLogEntryReply;
  static deserializeBinaryFromReader(message: DeleteLogEntryReply, reader: jspb.BinaryReader): DeleteLogEntryReply;
}

export namespace DeleteLogEntryReply {
  export type AsObject = {
  }
}

export class DeleteLogEntryRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteLogEntryRequest): DeleteLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteLogEntryRequest;
  static deserializeBinaryFromReader(message: DeleteLogEntryRequest, reader: jspb.BinaryReader): DeleteLogEntryRequest;
}

export namespace DeleteLogEntryRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageLogEntryAliasesReply extends jspb.Message {
  getCanManageLogEntryAliases(): boolean;
  setCanManageLogEntryAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageLogEntryAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageLogEntryAliasesReply): CanManageLogEntryAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageLogEntryAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageLogEntryAliasesReply;
  static deserializeBinaryFromReader(message: CanManageLogEntryAliasesReply, reader: jspb.BinaryReader): CanManageLogEntryAliasesReply;
}

export namespace CanManageLogEntryAliasesReply {
  export type AsObject = {
    canManageLogEntryAliases: boolean,
  }
}

export class CanManageLogEntryAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageLogEntryAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageLogEntryAliasesRequest): CanManageLogEntryAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageLogEntryAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageLogEntryAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageLogEntryAliasesRequest, reader: jspb.BinaryReader): CanManageLogEntryAliasesRequest;
}

export namespace CanManageLogEntryAliasesRequest {
  export type AsObject = {
  }
}

export class AliasLogEntryReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasLogEntryReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasLogEntryReply): AliasLogEntryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasLogEntryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasLogEntryReply;
  static deserializeBinaryFromReader(message: AliasLogEntryReply, reader: jspb.BinaryReader): AliasLogEntryReply;
}

export namespace AliasLogEntryReply {
  export type AsObject = {
  }
}

export class AliasLogEntryRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasLogEntryRequest): AliasLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasLogEntryRequest;
  static deserializeBinaryFromReader(message: AliasLogEntryRequest, reader: jspb.BinaryReader): AliasLogEntryRequest;
}

export namespace AliasLogEntryRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UseComparativeLogViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeLogViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeLogViewReply): UseComparativeLogViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeLogViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeLogViewReply;
  static deserializeBinaryFromReader(message: UseComparativeLogViewReply, reader: jspb.BinaryReader): UseComparativeLogViewReply;
}

export namespace UseComparativeLogViewReply {
  export type AsObject = {
  }
}

export class UseComparativeLogViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeLogViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeLogViewRequest): UseComparativeLogViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeLogViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeLogViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeLogViewRequest, reader: jspb.BinaryReader): UseComparativeLogViewRequest;
}

export namespace UseComparativeLogViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryLogViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryLogViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryLogViewReply): UsePlenaryLogViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryLogViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryLogViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryLogViewReply, reader: jspb.BinaryReader): UsePlenaryLogViewReply;
}

export namespace UsePlenaryLogViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryLogViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryLogViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryLogViewRequest): UsePlenaryLogViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryLogViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryLogViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryLogViewRequest, reader: jspb.BinaryReader): UsePlenaryLogViewRequest;
}

export namespace UsePlenaryLogViewRequest {
  export type AsObject = {
  }
}

export class CanLookupLogEntryLogMappingsReply extends jspb.Message {
  getCanLookupLogEntryLogMappings(): boolean;
  setCanLookupLogEntryLogMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupLogEntryLogMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupLogEntryLogMappingsReply): CanLookupLogEntryLogMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupLogEntryLogMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupLogEntryLogMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupLogEntryLogMappingsReply, reader: jspb.BinaryReader): CanLookupLogEntryLogMappingsReply;
}

export namespace CanLookupLogEntryLogMappingsReply {
  export type AsObject = {
    canLookupLogEntryLogMappings: boolean,
  }
}

export class CanLookupLogEntryLogMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupLogEntryLogMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupLogEntryLogMappingsRequest): CanLookupLogEntryLogMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupLogEntryLogMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupLogEntryLogMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupLogEntryLogMappingsRequest, reader: jspb.BinaryReader): CanLookupLogEntryLogMappingsRequest;
}

export namespace CanLookupLogEntryLogMappingsRequest {
  export type AsObject = {
  }
}

export class GetLogEntryIdsByLogRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntryIdsByLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntryIdsByLogRequest): GetLogEntryIdsByLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntryIdsByLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntryIdsByLogRequest;
  static deserializeBinaryFromReader(message: GetLogEntryIdsByLogRequest, reader: jspb.BinaryReader): GetLogEntryIdsByLogRequest;
}

export namespace GetLogEntryIdsByLogRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogEntriesByLogRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntriesByLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntriesByLogRequest): GetLogEntriesByLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntriesByLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntriesByLogRequest;
  static deserializeBinaryFromReader(message: GetLogEntriesByLogRequest, reader: jspb.BinaryReader): GetLogEntriesByLogRequest;
}

export namespace GetLogEntriesByLogRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogEntrieByLogRequest extends jspb.Message {
  clearLogIdsList(): void;
  getLogIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setLogIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addLogIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogEntrieByLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogEntrieByLogRequest): GetLogEntrieByLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogEntrieByLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogEntrieByLogRequest;
  static deserializeBinaryFromReader(message: GetLogEntrieByLogRequest, reader: jspb.BinaryReader): GetLogEntrieByLogRequest;
}

export namespace GetLogEntrieByLogRequest {
  export type AsObject = {
    logIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetLogIdsByLogEntryRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogIdsByLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogIdsByLogEntryRequest): GetLogIdsByLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogIdsByLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogIdsByLogEntryRequest;
  static deserializeBinaryFromReader(message: GetLogIdsByLogEntryRequest, reader: jspb.BinaryReader): GetLogIdsByLogEntryRequest;
}

export namespace GetLogIdsByLogEntryRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogByLogEntryRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogByLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogByLogEntryRequest): GetLogByLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogByLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogByLogEntryRequest;
  static deserializeBinaryFromReader(message: GetLogByLogEntryRequest, reader: jspb.BinaryReader): GetLogByLogEntryRequest;
}

export namespace GetLogByLogEntryRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignLogEntriesReply extends jspb.Message {
  getCanAssignLogEntries(): boolean;
  setCanAssignLogEntries(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignLogEntriesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignLogEntriesReply): CanAssignLogEntriesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignLogEntriesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignLogEntriesReply;
  static deserializeBinaryFromReader(message: CanAssignLogEntriesReply, reader: jspb.BinaryReader): CanAssignLogEntriesReply;
}

export namespace CanAssignLogEntriesReply {
  export type AsObject = {
    canAssignLogEntries: boolean,
  }
}

export class CanAssignLogEntriesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignLogEntriesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignLogEntriesRequest): CanAssignLogEntriesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignLogEntriesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignLogEntriesRequest;
  static deserializeBinaryFromReader(message: CanAssignLogEntriesRequest, reader: jspb.BinaryReader): CanAssignLogEntriesRequest;
}

export namespace CanAssignLogEntriesRequest {
  export type AsObject = {
  }
}

export class CanAssignLogEntriesToLogReply extends jspb.Message {
  getCanAssignLogEntriesToLog(): boolean;
  setCanAssignLogEntriesToLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignLogEntriesToLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignLogEntriesToLogReply): CanAssignLogEntriesToLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignLogEntriesToLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignLogEntriesToLogReply;
  static deserializeBinaryFromReader(message: CanAssignLogEntriesToLogReply, reader: jspb.BinaryReader): CanAssignLogEntriesToLogReply;
}

export namespace CanAssignLogEntriesToLogReply {
  export type AsObject = {
    canAssignLogEntriesToLog: boolean,
  }
}

export class CanAssignLogEntriesToLogRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignLogEntriesToLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignLogEntriesToLogRequest): CanAssignLogEntriesToLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignLogEntriesToLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignLogEntriesToLogRequest;
  static deserializeBinaryFromReader(message: CanAssignLogEntriesToLogRequest, reader: jspb.BinaryReader): CanAssignLogEntriesToLogRequest;
}

export namespace CanAssignLogEntriesToLogRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableLogIdsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableLogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableLogIdsRequest): GetAssignableLogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableLogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableLogIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableLogIdsRequest, reader: jspb.BinaryReader): GetAssignableLogIdsRequest;
}

export namespace GetAssignableLogIdsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableLogIdsForLogEntryRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableLogIdsForLogEntryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableLogIdsForLogEntryRequest): GetAssignableLogIdsForLogEntryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableLogIdsForLogEntryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableLogIdsForLogEntryRequest;
  static deserializeBinaryFromReader(message: GetAssignableLogIdsForLogEntryRequest, reader: jspb.BinaryReader): GetAssignableLogIdsForLogEntryRequest;
}

export namespace GetAssignableLogIdsForLogEntryRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignLogEntryToLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignLogEntryToLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignLogEntryToLogReply): AssignLogEntryToLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignLogEntryToLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignLogEntryToLogReply;
  static deserializeBinaryFromReader(message: AssignLogEntryToLogReply, reader: jspb.BinaryReader): AssignLogEntryToLogReply;
}

export namespace AssignLogEntryToLogReply {
  export type AsObject = {
  }
}

export class AssignLogEntryToLogRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignLogEntryToLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignLogEntryToLogRequest): AssignLogEntryToLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignLogEntryToLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignLogEntryToLogRequest;
  static deserializeBinaryFromReader(message: AssignLogEntryToLogRequest, reader: jspb.BinaryReader): AssignLogEntryToLogRequest;
}

export namespace AssignLogEntryToLogRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignLogEntryFromLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignLogEntryFromLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignLogEntryFromLogReply): UnassignLogEntryFromLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignLogEntryFromLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignLogEntryFromLogReply;
  static deserializeBinaryFromReader(message: UnassignLogEntryFromLogReply, reader: jspb.BinaryReader): UnassignLogEntryFromLogReply;
}

export namespace UnassignLogEntryFromLogReply {
  export type AsObject = {
  }
}

export class UnassignLogEntryFromLogRequest extends jspb.Message {
  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignLogEntryFromLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignLogEntryFromLogRequest): UnassignLogEntryFromLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignLogEntryFromLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignLogEntryFromLogRequest;
  static deserializeBinaryFromReader(message: UnassignLogEntryFromLogRequest, reader: jspb.BinaryReader): UnassignLogEntryFromLogRequest;
}

export namespace UnassignLogEntryFromLogRequest {
  export type AsObject = {
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignLogEntryToLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignLogEntryToLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignLogEntryToLogReply): ReassignLogEntryToLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignLogEntryToLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignLogEntryToLogReply;
  static deserializeBinaryFromReader(message: ReassignLogEntryToLogReply, reader: jspb.BinaryReader): ReassignLogEntryToLogReply;
}

export namespace ReassignLogEntryToLogReply {
  export type AsObject = {
  }
}

export class ReassignLogEntryToLogRequest extends jspb.Message {
  hasFromLogId(): boolean;
  clearFromLogId(): void;
  getFromLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogEntryId(): boolean;
  clearLogEntryId(): void;
  getLogEntryId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogEntryId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToLogId(): boolean;
  clearToLogId(): void;
  getToLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignLogEntryToLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignLogEntryToLogRequest): ReassignLogEntryToLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignLogEntryToLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignLogEntryToLogRequest;
  static deserializeBinaryFromReader(message: ReassignLogEntryToLogRequest, reader: jspb.BinaryReader): ReassignLogEntryToLogRequest;
}

export namespace ReassignLogEntryToLogRequest {
  export type AsObject = {
    fromLogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logEntryId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toLogId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupLogsReply extends jspb.Message {
  getCanLookupLogs(): boolean;
  setCanLookupLogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupLogsReply): CanLookupLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupLogsReply;
  static deserializeBinaryFromReader(message: CanLookupLogsReply, reader: jspb.BinaryReader): CanLookupLogsReply;
}

export namespace CanLookupLogsReply {
  export type AsObject = {
    canLookupLogs: boolean,
  }
}

export class CanLookupLogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupLogsRequest): CanLookupLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupLogsRequest;
  static deserializeBinaryFromReader(message: CanLookupLogsRequest, reader: jspb.BinaryReader): CanLookupLogsRequest;
}

export namespace CanLookupLogsRequest {
  export type AsObject = {
  }
}

export class GetLogsByIdsRequest extends jspb.Message {
  clearLogIdsList(): void;
  getLogIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setLogIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addLogIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogsByIdsRequest): GetLogsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogsByIdsRequest;
  static deserializeBinaryFromReader(message: GetLogsByIdsRequest, reader: jspb.BinaryReader): GetLogsByIdsRequest;
}

export namespace GetLogsByIdsRequest {
  export type AsObject = {
    logIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetLogsByGenusTypeRequest extends jspb.Message {
  hasLogGenusType(): boolean;
  clearLogGenusType(): void;
  getLogGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLogGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogsByGenusTypeRequest): GetLogsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetLogsByGenusTypeRequest, reader: jspb.BinaryReader): GetLogsByGenusTypeRequest;
}

export namespace GetLogsByGenusTypeRequest {
  export type AsObject = {
    logGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogsByParentGenusTypeRequest extends jspb.Message {
  hasLogGenusType(): boolean;
  clearLogGenusType(): void;
  getLogGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLogGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogsByParentGenusTypeRequest): GetLogsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetLogsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetLogsByParentGenusTypeRequest;
}

export namespace GetLogsByParentGenusTypeRequest {
  export type AsObject = {
    logGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogsByRecordTypeRequest extends jspb.Message {
  hasLogRecordType(): boolean;
  clearLogRecordType(): void;
  getLogRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setLogRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogsByRecordTypeRequest): GetLogsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetLogsByRecordTypeRequest, reader: jspb.BinaryReader): GetLogsByRecordTypeRequest;
}

export namespace GetLogsByRecordTypeRequest {
  export type AsObject = {
    logRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetLogsByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogsByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogsByProviderRequest): GetLogsByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogsByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogsByProviderRequest;
  static deserializeBinaryFromReader(message: GetLogsByProviderRequest, reader: jspb.BinaryReader): GetLogsByProviderRequest;
}

export namespace GetLogsByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogsRequest): GetLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogsRequest;
  static deserializeBinaryFromReader(message: GetLogsRequest, reader: jspb.BinaryReader): GetLogsRequest;
}

export namespace GetLogsRequest {
  export type AsObject = {
  }
}

export class CanCreateLogsReply extends jspb.Message {
  getCanCreateLogs(): boolean;
  setCanCreateLogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogsReply): CanCreateLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogsReply;
  static deserializeBinaryFromReader(message: CanCreateLogsReply, reader: jspb.BinaryReader): CanCreateLogsReply;
}

export namespace CanCreateLogsReply {
  export type AsObject = {
    canCreateLogs: boolean,
  }
}

export class CanCreateLogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogsRequest): CanCreateLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogsRequest;
  static deserializeBinaryFromReader(message: CanCreateLogsRequest, reader: jspb.BinaryReader): CanCreateLogsRequest;
}

export namespace CanCreateLogsRequest {
  export type AsObject = {
  }
}

export class CanCreateLogWithRecordTypesReply extends jspb.Message {
  getCanCreateLogWithRecordTypes(): boolean;
  setCanCreateLogWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogWithRecordTypesReply): CanCreateLogWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateLogWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateLogWithRecordTypesReply;
}

export namespace CanCreateLogWithRecordTypesReply {
  export type AsObject = {
    canCreateLogWithRecordTypes: boolean,
  }
}

export class CanCreateLogWithRecordTypesRequest extends jspb.Message {
  clearLogRecordTypesList(): void;
  getLogRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setLogRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addLogRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateLogWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateLogWithRecordTypesRequest): CanCreateLogWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateLogWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateLogWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateLogWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateLogWithRecordTypesRequest;
}

export namespace CanCreateLogWithRecordTypesRequest {
  export type AsObject = {
    logRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetLogFormForCreateReply extends jspb.Message {
  hasLogForm(): boolean;
  clearLogForm(): void;
  getLogForm(): LogForm | undefined;
  setLogForm(value?: LogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogFormForCreateReply): GetLogFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogFormForCreateReply;
  static deserializeBinaryFromReader(message: GetLogFormForCreateReply, reader: jspb.BinaryReader): GetLogFormForCreateReply;
}

export namespace GetLogFormForCreateReply {
  export type AsObject = {
    logForm?: LogForm.AsObject,
  }
}

export class GetLogFormForCreateRequest extends jspb.Message {
  clearLogRecordTypesList(): void;
  getLogRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setLogRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addLogRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogFormForCreateRequest): GetLogFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetLogFormForCreateRequest, reader: jspb.BinaryReader): GetLogFormForCreateRequest;
}

export namespace GetLogFormForCreateRequest {
  export type AsObject = {
    logRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateLogReply extends jspb.Message {
  hasLog(): boolean;
  clearLog(): void;
  getLog(): Log | undefined;
  setLog(value?: Log): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateLogReply): CreateLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateLogReply;
  static deserializeBinaryFromReader(message: CreateLogReply, reader: jspb.BinaryReader): CreateLogReply;
}

export namespace CreateLogReply {
  export type AsObject = {
    log?: Log.AsObject,
  }
}

export class CreateLogRequest extends jspb.Message {
  hasLogForm(): boolean;
  clearLogForm(): void;
  getLogForm(): LogForm | undefined;
  setLogForm(value?: LogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateLogRequest): CreateLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateLogRequest;
  static deserializeBinaryFromReader(message: CreateLogRequest, reader: jspb.BinaryReader): CreateLogRequest;
}

export namespace CreateLogRequest {
  export type AsObject = {
    logForm?: LogForm.AsObject,
  }
}

export class CanUpdateLogsReply extends jspb.Message {
  getCanUpdateLogs(): boolean;
  setCanUpdateLogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateLogsReply): CanUpdateLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateLogsReply;
  static deserializeBinaryFromReader(message: CanUpdateLogsReply, reader: jspb.BinaryReader): CanUpdateLogsReply;
}

export namespace CanUpdateLogsReply {
  export type AsObject = {
    canUpdateLogs: boolean,
  }
}

export class CanUpdateLogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateLogsRequest): CanUpdateLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateLogsRequest;
  static deserializeBinaryFromReader(message: CanUpdateLogsRequest, reader: jspb.BinaryReader): CanUpdateLogsRequest;
}

export namespace CanUpdateLogsRequest {
  export type AsObject = {
  }
}

export class GetLogFormForUpdateReply extends jspb.Message {
  hasLogForm(): boolean;
  clearLogForm(): void;
  getLogForm(): LogForm | undefined;
  setLogForm(value?: LogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogFormForUpdateReply): GetLogFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetLogFormForUpdateReply, reader: jspb.BinaryReader): GetLogFormForUpdateReply;
}

export namespace GetLogFormForUpdateReply {
  export type AsObject = {
    logForm?: LogForm.AsObject,
  }
}

export class GetLogFormForUpdateRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogFormForUpdateRequest): GetLogFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetLogFormForUpdateRequest, reader: jspb.BinaryReader): GetLogFormForUpdateRequest;
}

export namespace GetLogFormForUpdateRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateLogReply): UpdateLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateLogReply;
  static deserializeBinaryFromReader(message: UpdateLogReply, reader: jspb.BinaryReader): UpdateLogReply;
}

export namespace UpdateLogReply {
  export type AsObject = {
  }
}

export class UpdateLogRequest extends jspb.Message {
  hasLogForm(): boolean;
  clearLogForm(): void;
  getLogForm(): LogForm | undefined;
  setLogForm(value?: LogForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateLogRequest): UpdateLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateLogRequest;
  static deserializeBinaryFromReader(message: UpdateLogRequest, reader: jspb.BinaryReader): UpdateLogRequest;
}

export namespace UpdateLogRequest {
  export type AsObject = {
    logForm?: LogForm.AsObject,
  }
}

export class CanDeleteLogsReply extends jspb.Message {
  getCanDeleteLogs(): boolean;
  setCanDeleteLogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteLogsReply): CanDeleteLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteLogsReply;
  static deserializeBinaryFromReader(message: CanDeleteLogsReply, reader: jspb.BinaryReader): CanDeleteLogsReply;
}

export namespace CanDeleteLogsReply {
  export type AsObject = {
    canDeleteLogs: boolean,
  }
}

export class CanDeleteLogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteLogsRequest): CanDeleteLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteLogsRequest;
  static deserializeBinaryFromReader(message: CanDeleteLogsRequest, reader: jspb.BinaryReader): CanDeleteLogsRequest;
}

export namespace CanDeleteLogsRequest {
  export type AsObject = {
  }
}

export class DeleteLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteLogReply): DeleteLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteLogReply;
  static deserializeBinaryFromReader(message: DeleteLogReply, reader: jspb.BinaryReader): DeleteLogReply;
}

export namespace DeleteLogReply {
  export type AsObject = {
  }
}

export class DeleteLogRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteLogRequest): DeleteLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteLogRequest;
  static deserializeBinaryFromReader(message: DeleteLogRequest, reader: jspb.BinaryReader): DeleteLogRequest;
}

export namespace DeleteLogRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageLogAliasesReply extends jspb.Message {
  getCanManageLogAliases(): boolean;
  setCanManageLogAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageLogAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageLogAliasesReply): CanManageLogAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageLogAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageLogAliasesReply;
  static deserializeBinaryFromReader(message: CanManageLogAliasesReply, reader: jspb.BinaryReader): CanManageLogAliasesReply;
}

export namespace CanManageLogAliasesReply {
  export type AsObject = {
    canManageLogAliases: boolean,
  }
}

export class CanManageLogAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageLogAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageLogAliasesRequest): CanManageLogAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageLogAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageLogAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageLogAliasesRequest, reader: jspb.BinaryReader): CanManageLogAliasesRequest;
}

export namespace CanManageLogAliasesRequest {
  export type AsObject = {
  }
}

export class AliasLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasLogReply): AliasLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasLogReply;
  static deserializeBinaryFromReader(message: AliasLogReply, reader: jspb.BinaryReader): AliasLogReply;
}

export namespace AliasLogReply {
  export type AsObject = {
  }
}

export class AliasLogRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasLogRequest): AliasLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasLogRequest;
  static deserializeBinaryFromReader(message: AliasLogRequest, reader: jspb.BinaryReader): AliasLogRequest;
}

export namespace AliasLogRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogHierarchyIdReply): GetLogHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetLogHierarchyIdReply, reader: jspb.BinaryReader): GetLogHierarchyIdReply;
}

export namespace GetLogHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogHierarchyIdRequest): GetLogHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetLogHierarchyIdRequest, reader: jspb.BinaryReader): GetLogHierarchyIdRequest;
}

export namespace GetLogHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetLogHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogHierarchyReply): GetLogHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogHierarchyReply;
  static deserializeBinaryFromReader(message: GetLogHierarchyReply, reader: jspb.BinaryReader): GetLogHierarchyReply;
}

export namespace GetLogHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetLogHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogHierarchyRequest): GetLogHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogHierarchyRequest;
  static deserializeBinaryFromReader(message: GetLogHierarchyRequest, reader: jspb.BinaryReader): GetLogHierarchyRequest;
}

export namespace GetLogHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessLogHierarchyReply extends jspb.Message {
  getCanAccessLogHierarchy(): boolean;
  setCanAccessLogHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessLogHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessLogHierarchyReply): CanAccessLogHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessLogHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessLogHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessLogHierarchyReply, reader: jspb.BinaryReader): CanAccessLogHierarchyReply;
}

export namespace CanAccessLogHierarchyReply {
  export type AsObject = {
    canAccessLogHierarchy: boolean,
  }
}

export class CanAccessLogHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessLogHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessLogHierarchyRequest): CanAccessLogHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessLogHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessLogHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessLogHierarchyRequest, reader: jspb.BinaryReader): CanAccessLogHierarchyRequest;
}

export namespace CanAccessLogHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootLogIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootLogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootLogIdsRequest): GetRootLogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootLogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootLogIdsRequest;
  static deserializeBinaryFromReader(message: GetRootLogIdsRequest, reader: jspb.BinaryReader): GetRootLogIdsRequest;
}

export namespace GetRootLogIdsRequest {
  export type AsObject = {
  }
}

export class GetRootLogsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootLogsRequest): GetRootLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootLogsRequest;
  static deserializeBinaryFromReader(message: GetRootLogsRequest, reader: jspb.BinaryReader): GetRootLogsRequest;
}

export namespace GetRootLogsRequest {
  export type AsObject = {
  }
}

export class HasParentLogsReply extends jspb.Message {
  getHasParentLogs(): boolean;
  setHasParentLogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentLogsReply): HasParentLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentLogsReply;
  static deserializeBinaryFromReader(message: HasParentLogsReply, reader: jspb.BinaryReader): HasParentLogsReply;
}

export namespace HasParentLogsReply {
  export type AsObject = {
    hasParentLogs: boolean,
  }
}

export class HasParentLogsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentLogsRequest): HasParentLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentLogsRequest;
  static deserializeBinaryFromReader(message: HasParentLogsRequest, reader: jspb.BinaryReader): HasParentLogsRequest;
}

export namespace HasParentLogsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfLogReply extends jspb.Message {
  getIsParentOfLog(): boolean;
  setIsParentOfLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfLogReply): IsParentOfLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfLogReply;
  static deserializeBinaryFromReader(message: IsParentOfLogReply, reader: jspb.BinaryReader): IsParentOfLogReply;
}

export namespace IsParentOfLogReply {
  export type AsObject = {
    isParentOfLog: boolean,
  }
}

export class IsParentOfLogRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfLogRequest): IsParentOfLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfLogRequest;
  static deserializeBinaryFromReader(message: IsParentOfLogRequest, reader: jspb.BinaryReader): IsParentOfLogRequest;
}

export namespace IsParentOfLogRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentLogIdsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentLogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentLogIdsRequest): GetParentLogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentLogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentLogIdsRequest;
  static deserializeBinaryFromReader(message: GetParentLogIdsRequest, reader: jspb.BinaryReader): GetParentLogIdsRequest;
}

export namespace GetParentLogIdsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentLogsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentLogsRequest): GetParentLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentLogsRequest;
  static deserializeBinaryFromReader(message: GetParentLogsRequest, reader: jspb.BinaryReader): GetParentLogsRequest;
}

export namespace GetParentLogsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfLogReply extends jspb.Message {
  getIsAncestorOfLog(): boolean;
  setIsAncestorOfLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfLogReply): IsAncestorOfLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfLogReply;
  static deserializeBinaryFromReader(message: IsAncestorOfLogReply, reader: jspb.BinaryReader): IsAncestorOfLogReply;
}

export namespace IsAncestorOfLogReply {
  export type AsObject = {
    isAncestorOfLog: boolean,
  }
}

export class IsAncestorOfLogRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfLogRequest): IsAncestorOfLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfLogRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfLogRequest, reader: jspb.BinaryReader): IsAncestorOfLogRequest;
}

export namespace IsAncestorOfLogRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildLogsReply extends jspb.Message {
  getHasChildLogs(): boolean;
  setHasChildLogs(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildLogsReply): HasChildLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildLogsReply;
  static deserializeBinaryFromReader(message: HasChildLogsReply, reader: jspb.BinaryReader): HasChildLogsReply;
}

export namespace HasChildLogsReply {
  export type AsObject = {
    hasChildLogs: boolean,
  }
}

export class HasChildLogsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildLogsRequest): HasChildLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildLogsRequest;
  static deserializeBinaryFromReader(message: HasChildLogsRequest, reader: jspb.BinaryReader): HasChildLogsRequest;
}

export namespace HasChildLogsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfLogReply extends jspb.Message {
  getIsChildOfLog(): boolean;
  setIsChildOfLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfLogReply): IsChildOfLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfLogReply;
  static deserializeBinaryFromReader(message: IsChildOfLogReply, reader: jspb.BinaryReader): IsChildOfLogReply;
}

export namespace IsChildOfLogReply {
  export type AsObject = {
    isChildOfLog: boolean,
  }
}

export class IsChildOfLogRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfLogRequest): IsChildOfLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfLogRequest;
  static deserializeBinaryFromReader(message: IsChildOfLogRequest, reader: jspb.BinaryReader): IsChildOfLogRequest;
}

export namespace IsChildOfLogRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildLogIdsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildLogIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildLogIdsRequest): GetChildLogIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildLogIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildLogIdsRequest;
  static deserializeBinaryFromReader(message: GetChildLogIdsRequest, reader: jspb.BinaryReader): GetChildLogIdsRequest;
}

export namespace GetChildLogIdsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildLogsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildLogsRequest): GetChildLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildLogsRequest;
  static deserializeBinaryFromReader(message: GetChildLogsRequest, reader: jspb.BinaryReader): GetChildLogsRequest;
}

export namespace GetChildLogsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfLogReply extends jspb.Message {
  getIsDescendantOfLog(): boolean;
  setIsDescendantOfLog(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfLogReply): IsDescendantOfLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfLogReply;
  static deserializeBinaryFromReader(message: IsDescendantOfLogReply, reader: jspb.BinaryReader): IsDescendantOfLogReply;
}

export namespace IsDescendantOfLogReply {
  export type AsObject = {
    isDescendantOfLog: boolean,
  }
}

export class IsDescendantOfLogRequest extends jspb.Message {
  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfLogRequest): IsDescendantOfLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfLogRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfLogRequest, reader: jspb.BinaryReader): IsDescendantOfLogRequest;
}

export namespace IsDescendantOfLogRequest {
  export type AsObject = {
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogNodeIdsReply): GetLogNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogNodeIdsReply;
  static deserializeBinaryFromReader(message: GetLogNodeIdsReply, reader: jspb.BinaryReader): GetLogNodeIdsReply;
}

export namespace GetLogNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetLogNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogNodeIdsRequest): GetLogNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetLogNodeIdsRequest, reader: jspb.BinaryReader): GetLogNodeIdsRequest;
}

export namespace GetLogNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetLogNodesReply extends jspb.Message {
  hasLogNode(): boolean;
  clearLogNode(): void;
  getLogNode(): LogNode | undefined;
  setLogNode(value?: LogNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogNodesReply): GetLogNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogNodesReply;
  static deserializeBinaryFromReader(message: GetLogNodesReply, reader: jspb.BinaryReader): GetLogNodesReply;
}

export namespace GetLogNodesReply {
  export type AsObject = {
    logNode?: LogNode.AsObject,
  }
}

export class GetLogNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetLogNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetLogNodesRequest): GetLogNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetLogNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetLogNodesRequest;
  static deserializeBinaryFromReader(message: GetLogNodesRequest, reader: jspb.BinaryReader): GetLogNodesRequest;
}

export namespace GetLogNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    descendantLevels: number,
    includeSiblings: boolean,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanModifyLogHierarchyReply extends jspb.Message {
  getCanModifyLogHierarchy(): boolean;
  setCanModifyLogHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyLogHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyLogHierarchyReply): CanModifyLogHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyLogHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyLogHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyLogHierarchyReply, reader: jspb.BinaryReader): CanModifyLogHierarchyReply;
}

export namespace CanModifyLogHierarchyReply {
  export type AsObject = {
    canModifyLogHierarchy: boolean,
  }
}

export class CanModifyLogHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyLogHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyLogHierarchyRequest): CanModifyLogHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyLogHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyLogHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyLogHierarchyRequest, reader: jspb.BinaryReader): CanModifyLogHierarchyRequest;
}

export namespace CanModifyLogHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootLogReply): AddRootLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootLogReply;
  static deserializeBinaryFromReader(message: AddRootLogReply, reader: jspb.BinaryReader): AddRootLogReply;
}

export namespace AddRootLogReply {
  export type AsObject = {
  }
}

export class AddRootLogRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootLogRequest): AddRootLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootLogRequest;
  static deserializeBinaryFromReader(message: AddRootLogRequest, reader: jspb.BinaryReader): AddRootLogRequest;
}

export namespace AddRootLogRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootLogReply): RemoveRootLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootLogReply;
  static deserializeBinaryFromReader(message: RemoveRootLogReply, reader: jspb.BinaryReader): RemoveRootLogReply;
}

export namespace RemoveRootLogReply {
  export type AsObject = {
  }
}

export class RemoveRootLogRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootLogRequest): RemoveRootLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootLogRequest;
  static deserializeBinaryFromReader(message: RemoveRootLogRequest, reader: jspb.BinaryReader): RemoveRootLogRequest;
}

export namespace RemoveRootLogRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildLogReply): AddChildLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildLogReply;
  static deserializeBinaryFromReader(message: AddChildLogReply, reader: jspb.BinaryReader): AddChildLogReply;
}

export namespace AddChildLogReply {
  export type AsObject = {
  }
}

export class AddChildLogRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildLogRequest): AddChildLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildLogRequest;
  static deserializeBinaryFromReader(message: AddChildLogRequest, reader: jspb.BinaryReader): AddChildLogRequest;
}

export namespace AddChildLogRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildLogReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildLogReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildLogReply): RemoveChildLogReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildLogReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildLogReply;
  static deserializeBinaryFromReader(message: RemoveChildLogReply, reader: jspb.BinaryReader): RemoveChildLogReply;
}

export namespace RemoveChildLogReply {
  export type AsObject = {
  }
}

export class RemoveChildLogRequest extends jspb.Message {
  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildLogRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildLogRequest): RemoveChildLogRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildLogRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildLogRequest;
  static deserializeBinaryFromReader(message: RemoveChildLogRequest, reader: jspb.BinaryReader): RemoveChildLogRequest;
}

export namespace RemoveChildLogRequest {
  export type AsObject = {
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildLogsReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildLogsReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildLogsReply): RemoveChildLogsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildLogsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildLogsReply;
  static deserializeBinaryFromReader(message: RemoveChildLogsReply, reader: jspb.BinaryReader): RemoveChildLogsReply;
}

export namespace RemoveChildLogsReply {
  export type AsObject = {
  }
}

export class RemoveChildLogsRequest extends jspb.Message {
  hasLogId(): boolean;
  clearLogId(): void;
  getLogId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLogId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildLogsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildLogsRequest): RemoveChildLogsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildLogsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildLogsRequest;
  static deserializeBinaryFromReader(message: RemoveChildLogsRequest, reader: jspb.BinaryReader): RemoveChildLogsRequest;
}

export namespace RemoveChildLogsRequest {
  export type AsObject = {
    logId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

