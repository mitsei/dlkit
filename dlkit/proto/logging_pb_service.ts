// package: dlkit.proto.logging
// file: dlkit/proto/logging.proto

import * as dlkit_proto_logging_pb from "../../dlkit/proto/logging_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class LoggingSession {
  static serviceName = "dlkit.proto.logging.LoggingSession";
}
export namespace LoggingSession {
  export class GetLogId {
    static readonly methodName = "GetLogId";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogIdRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogIdReply;
  }
  export class GetLog {
    static readonly methodName = "GetLog";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogReply;
  }
  export class CanLog {
    static readonly methodName = "CanLog";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanLogReply;
  }
  export class Log {
    static readonly methodName = "Log";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.LogRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogReply;
  }
  export class LogAtPriority {
    static readonly methodName = "LogAtPriority";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.LogAtPriorityRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogAtPriorityReply;
  }
  export class GetLogEntryForm {
    static readonly methodName = "GetLogEntryForm";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntryFormRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogEntryFormReply;
  }
  export class CreateLogEntry {
    static readonly methodName = "CreateLogEntry";
    static readonly service = LoggingSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CreateLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.CreateLogEntryReply;
  }
}
export class LogEntryLookupSession {
  static serviceName = "dlkit.proto.logging.LogEntryLookupSession";
}
export namespace LogEntryLookupSession {
  export class GetLogId {
    static readonly methodName = "GetLogId";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogIdRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogIdReply;
  }
  export class GetLog {
    static readonly methodName = "GetLog";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogReply;
  }
  export class CanReadLog {
    static readonly methodName = "CanReadLog";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanReadLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanReadLogReply;
  }
  export class UseComparativeLogEntryView {
    static readonly methodName = "UseComparativeLogEntryView";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseComparativeLogEntryViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseComparativeLogEntryViewReply;
  }
  export class UsePlenaryLogEntryView {
    static readonly methodName = "UsePlenaryLogEntryView";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UsePlenaryLogEntryViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UsePlenaryLogEntryViewReply;
  }
  export class UseFederatedLogView {
    static readonly methodName = "UseFederatedLogView";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseFederatedLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseFederatedLogViewReply;
  }
  export class UseIsolatedLogView {
    static readonly methodName = "UseIsolatedLogView";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseIsolatedLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseIsolatedLogViewReply;
  }
  export class GetLogEntry {
    static readonly methodName = "GetLogEntry";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogEntryReply;
  }
  export class GetLogEntriesByIds {
    static readonly methodName = "GetLogEntriesByIds";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByIdsRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByGenusType {
    static readonly methodName = "GetLogEntriesByGenusType";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByParentGenusType {
    static readonly methodName = "GetLogEntriesByParentGenusType";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByRecordType {
    static readonly methodName = "GetLogEntriesByRecordType";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByPriorityType {
    static readonly methodName = "GetLogEntriesByPriorityType";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByPriorityTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByDate {
    static readonly methodName = "GetLogEntriesByDate";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByDateRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByPriorityTypeAndDate {
    static readonly methodName = "GetLogEntriesByPriorityTypeAndDate";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByPriorityTypeAndDateRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesForResource {
    static readonly methodName = "GetLogEntriesForResource";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesForResourceRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByDateForResource {
    static readonly methodName = "GetLogEntriesByDateForResource";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByDateForResourceRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntriesByPriorityTypeAndDateForResource {
    static readonly methodName = "GetLogEntriesByPriorityTypeAndDateForResource";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByPriorityTypeAndDateForResourceRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntries {
    static readonly methodName = "GetLogEntries";
    static readonly service = LogEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
}
export class LogEntryQuerySession {
  static serviceName = "dlkit.proto.logging.LogEntryQuerySession";
}
export namespace LogEntryQuerySession {
  export class GetLogId {
    static readonly methodName = "GetLogId";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogIdRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogIdReply;
  }
  export class GetLog {
    static readonly methodName = "GetLog";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogReply;
  }
  export class CanSearchLogEntries {
    static readonly methodName = "CanSearchLogEntries";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanSearchLogEntriesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanSearchLogEntriesReply;
  }
  export class UseFederatedLogView {
    static readonly methodName = "UseFederatedLogView";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseFederatedLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseFederatedLogViewReply;
  }
  export class UseIsolatedLogView {
    static readonly methodName = "UseIsolatedLogView";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseIsolatedLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseIsolatedLogViewReply;
  }
  export class GetLogEntryQuery {
    static readonly methodName = "GetLogEntryQuery";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntryQueryRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogEntryQueryReply;
  }
  export class GetLogEntriesByQuery {
    static readonly methodName = "GetLogEntriesByQuery";
    static readonly service = LogEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByQueryRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
}
export class LogEntryAdminSession {
  static serviceName = "dlkit.proto.logging.LogEntryAdminSession";
}
export namespace LogEntryAdminSession {
  export class GetLogId {
    static readonly methodName = "GetLogId";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogIdRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogIdReply;
  }
  export class GetLog {
    static readonly methodName = "GetLog";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogReply;
  }
  export class CanCreateLogEntries {
    static readonly methodName = "CanCreateLogEntries";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanCreateLogEntriesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanCreateLogEntriesReply;
  }
  export class CanCreateLogEntryWithRecordTypes {
    static readonly methodName = "CanCreateLogEntryWithRecordTypes";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanCreateLogEntryWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanCreateLogEntryWithRecordTypesReply;
  }
  export class GetLogEntryFormForCreate {
    static readonly methodName = "GetLogEntryFormForCreate";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntryFormForCreateRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogEntryFormForCreateReply;
  }
  export class CreateLogEntry {
    static readonly methodName = "CreateLogEntry";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CreateLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.CreateLogEntryReply;
  }
  export class CanUpdateLogEntries {
    static readonly methodName = "CanUpdateLogEntries";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanUpdateLogEntriesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanUpdateLogEntriesReply;
  }
  export class GetLogEntryFormForUpdate {
    static readonly methodName = "GetLogEntryFormForUpdate";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntryFormForUpdateRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogEntryFormForUpdateReply;
  }
  export class UpdateLogEntry {
    static readonly methodName = "UpdateLogEntry";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UpdateLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.UpdateLogEntryReply;
  }
  export class CanDeleteLogEntries {
    static readonly methodName = "CanDeleteLogEntries";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanDeleteLogEntriesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanDeleteLogEntriesReply;
  }
  export class DeleteLogEntry {
    static readonly methodName = "DeleteLogEntry";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.DeleteLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.DeleteLogEntryReply;
  }
  export class CanManageLogEntryAliases {
    static readonly methodName = "CanManageLogEntryAliases";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanManageLogEntryAliasesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanManageLogEntryAliasesReply;
  }
  export class AliasLogEntry {
    static readonly methodName = "AliasLogEntry";
    static readonly service = LogEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.AliasLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.AliasLogEntryReply;
  }
}
export class LogEntryLogSession {
  static serviceName = "dlkit.proto.logging.LogEntryLogSession";
}
export namespace LogEntryLogSession {
  export class UseComparativeLogView {
    static readonly methodName = "UseComparativeLogView";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseComparativeLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseComparativeLogViewReply;
  }
  export class UsePlenaryLogView {
    static readonly methodName = "UsePlenaryLogView";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UsePlenaryLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UsePlenaryLogViewReply;
  }
  export class CanLookupLogEntryLogMappings {
    static readonly methodName = "CanLookupLogEntryLogMappings";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanLookupLogEntryLogMappingsRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanLookupLogEntryLogMappingsReply;
  }
  export class GetLogEntryIdsByLog {
    static readonly methodName = "GetLogEntryIdsByLog";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntryIdsByLogRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetLogEntriesByLog {
    static readonly methodName = "GetLogEntriesByLog";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntriesByLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogEntrieByLog {
    static readonly methodName = "GetLogEntrieByLog";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogEntrieByLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.LogEntry;
  }
  export class GetLogIdsByLogEntry {
    static readonly methodName = "GetLogIdsByLogEntry";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogIdsByLogEntryRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetLogByLogEntry {
    static readonly methodName = "GetLogByLogEntry";
    static readonly service = LogEntryLogSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogByLogEntryRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
}
export class LogEntryLogAssignmentSession {
  static serviceName = "dlkit.proto.logging.LogEntryLogAssignmentSession";
}
export namespace LogEntryLogAssignmentSession {
  export class CanAssignLogEntries {
    static readonly methodName = "CanAssignLogEntries";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanAssignLogEntriesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanAssignLogEntriesReply;
  }
  export class CanAssignLogEntriesToLog {
    static readonly methodName = "CanAssignLogEntriesToLog";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanAssignLogEntriesToLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanAssignLogEntriesToLogReply;
  }
  export class GetAssignableLogIds {
    static readonly methodName = "GetAssignableLogIds";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetAssignableLogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableLogIdsForLogEntry {
    static readonly methodName = "GetAssignableLogIdsForLogEntry";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetAssignableLogIdsForLogEntryRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignLogEntryToLog {
    static readonly methodName = "AssignLogEntryToLog";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.AssignLogEntryToLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.AssignLogEntryToLogReply;
  }
  export class UnassignLogEntryFromLog {
    static readonly methodName = "UnassignLogEntryFromLog";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UnassignLogEntryFromLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.UnassignLogEntryFromLogReply;
  }
  export class ReassignLogEntryToLog {
    static readonly methodName = "ReassignLogEntryToLog";
    static readonly service = LogEntryLogAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.ReassignLogEntryToLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.ReassignLogEntryToLogReply;
  }
}
export class LogLookupSession {
  static serviceName = "dlkit.proto.logging.LogLookupSession";
}
export namespace LogLookupSession {
  export class CanLookupLogs {
    static readonly methodName = "CanLookupLogs";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanLookupLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanLookupLogsReply;
  }
  export class UseComparativeLogView {
    static readonly methodName = "UseComparativeLogView";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseComparativeLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseComparativeLogViewReply;
  }
  export class UsePlenaryLogView {
    static readonly methodName = "UsePlenaryLogView";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UsePlenaryLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UsePlenaryLogViewReply;
  }
  export class GetLog {
    static readonly methodName = "GetLog";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogReply;
  }
  export class GetLogsByIds {
    static readonly methodName = "GetLogsByIds";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogsByIdsRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class GetLogsByGenusType {
    static readonly methodName = "GetLogsByGenusType";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class GetLogsByParentGenusType {
    static readonly methodName = "GetLogsByParentGenusType";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class GetLogsByRecordType {
    static readonly methodName = "GetLogsByRecordType";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class GetLogsByProvider {
    static readonly methodName = "GetLogsByProvider";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogsByProviderRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class GetLogs {
    static readonly methodName = "GetLogs";
    static readonly service = LogLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
}
export class LogAdminSession {
  static serviceName = "dlkit.proto.logging.LogAdminSession";
}
export namespace LogAdminSession {
  export class CanCreateLogs {
    static readonly methodName = "CanCreateLogs";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanCreateLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanCreateLogsReply;
  }
  export class CanCreateLogWithRecordTypes {
    static readonly methodName = "CanCreateLogWithRecordTypes";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanCreateLogWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanCreateLogWithRecordTypesReply;
  }
  export class GetLogFormForCreate {
    static readonly methodName = "GetLogFormForCreate";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogFormForCreateRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogFormForCreateReply;
  }
  export class CreateLog {
    static readonly methodName = "CreateLog";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CreateLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.CreateLogReply;
  }
  export class CanUpdateLogs {
    static readonly methodName = "CanUpdateLogs";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanUpdateLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanUpdateLogsReply;
  }
  export class GetLogFormForUpdate {
    static readonly methodName = "GetLogFormForUpdate";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogFormForUpdateRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogFormForUpdateReply;
  }
  export class UpdateLog {
    static readonly methodName = "UpdateLog";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UpdateLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.UpdateLogReply;
  }
  export class CanDeleteLogs {
    static readonly methodName = "CanDeleteLogs";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanDeleteLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanDeleteLogsReply;
  }
  export class DeleteLog {
    static readonly methodName = "DeleteLog";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.DeleteLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.DeleteLogReply;
  }
  export class CanManageLogAliases {
    static readonly methodName = "CanManageLogAliases";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanManageLogAliasesRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanManageLogAliasesReply;
  }
  export class AliasLog {
    static readonly methodName = "AliasLog";
    static readonly service = LogAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.AliasLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.AliasLogReply;
  }
}
export class LogHierarchySession {
  static serviceName = "dlkit.proto.logging.LogHierarchySession";
}
export namespace LogHierarchySession {
  export class GetLogHierarchyId {
    static readonly methodName = "GetLogHierarchyId";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogHierarchyIdRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogHierarchyIdReply;
  }
  export class GetLogHierarchy {
    static readonly methodName = "GetLogHierarchy";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogHierarchyRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogHierarchyReply;
  }
  export class CanAccessLogHierarchy {
    static readonly methodName = "CanAccessLogHierarchy";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanAccessLogHierarchyRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanAccessLogHierarchyReply;
  }
  export class UseComparativeLogView {
    static readonly methodName = "UseComparativeLogView";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UseComparativeLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UseComparativeLogViewReply;
  }
  export class UsePlenaryLogView {
    static readonly methodName = "UsePlenaryLogView";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.UsePlenaryLogViewRequest;
    static readonly responseType = dlkit_proto_logging_pb.UsePlenaryLogViewReply;
  }
  export class GetRootLogIds {
    static readonly methodName = "GetRootLogIds";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetRootLogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootLogs {
    static readonly methodName = "GetRootLogs";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetRootLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class HasParentLogs {
    static readonly methodName = "HasParentLogs";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.HasParentLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.HasParentLogsReply;
  }
  export class IsParentOfLog {
    static readonly methodName = "IsParentOfLog";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.IsParentOfLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.IsParentOfLogReply;
  }
  export class GetParentLogIds {
    static readonly methodName = "GetParentLogIds";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetParentLogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentLogs {
    static readonly methodName = "GetParentLogs";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetParentLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class IsAncestorOfLog {
    static readonly methodName = "IsAncestorOfLog";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.IsAncestorOfLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.IsAncestorOfLogReply;
  }
  export class HasChildLogs {
    static readonly methodName = "HasChildLogs";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.HasChildLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.HasChildLogsReply;
  }
  export class IsChildOfLog {
    static readonly methodName = "IsChildOfLog";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.IsChildOfLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.IsChildOfLogReply;
  }
  export class GetChildLogIds {
    static readonly methodName = "GetChildLogIds";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetChildLogIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildLogs {
    static readonly methodName = "GetChildLogs";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_logging_pb.GetChildLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.Log;
  }
  export class IsDescendantOfLog {
    static readonly methodName = "IsDescendantOfLog";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.IsDescendantOfLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.IsDescendantOfLogReply;
  }
  export class GetLogNodeIds {
    static readonly methodName = "GetLogNodeIds";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogNodeIdsRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogNodeIdsReply;
  }
  export class GetLogNodes {
    static readonly methodName = "GetLogNodes";
    static readonly service = LogHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogNodesRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogNodesReply;
  }
}
export class LogHierarchyDesignSession {
  static serviceName = "dlkit.proto.logging.LogHierarchyDesignSession";
}
export namespace LogHierarchyDesignSession {
  export class GetLogHierarchyId {
    static readonly methodName = "GetLogHierarchyId";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogHierarchyIdRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogHierarchyIdReply;
  }
  export class GetLogHierarchy {
    static readonly methodName = "GetLogHierarchy";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.GetLogHierarchyRequest;
    static readonly responseType = dlkit_proto_logging_pb.GetLogHierarchyReply;
  }
  export class CanModifyLogHierarchy {
    static readonly methodName = "CanModifyLogHierarchy";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.CanModifyLogHierarchyRequest;
    static readonly responseType = dlkit_proto_logging_pb.CanModifyLogHierarchyReply;
  }
  export class AddRootLog {
    static readonly methodName = "AddRootLog";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.AddRootLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.AddRootLogReply;
  }
  export class RemoveRootLog {
    static readonly methodName = "RemoveRootLog";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.RemoveRootLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.RemoveRootLogReply;
  }
  export class AddChildLog {
    static readonly methodName = "AddChildLog";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.AddChildLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.AddChildLogReply;
  }
  export class RemoveChildLog {
    static readonly methodName = "RemoveChildLog";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.RemoveChildLogRequest;
    static readonly responseType = dlkit_proto_logging_pb.RemoveChildLogReply;
  }
  export class RemoveChildLogs {
    static readonly methodName = "RemoveChildLogs";
    static readonly service = LogHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_logging_pb.RemoveChildLogsRequest;
    static readonly responseType = dlkit_proto_logging_pb.RemoveChildLogsReply;
  }
}
