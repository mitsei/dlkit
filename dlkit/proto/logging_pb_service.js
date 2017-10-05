// package: dlkit.proto.logging
// file: dlkit/proto/logging.proto

var jspb = require("google-protobuf");
var dlkit_proto_logging_pb = require("../../dlkit/proto/logging_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var LoggingSession = {
  serviceName: "dlkit.proto.logging.LoggingSession"
};
LoggingSession.GetLogId = {
  methodName: "GetLogId",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogIdRequest,
  responseType: dlkit_proto_logging_pb.GetLogIdReply
};
LoggingSession.GetLog = {
  methodName: "GetLog",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogRequest,
  responseType: dlkit_proto_logging_pb.GetLogReply
};
LoggingSession.CanLog = {
  methodName: "CanLog",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanLogRequest,
  responseType: dlkit_proto_logging_pb.CanLogReply
};
LoggingSession.Log = {
  methodName: "Log",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.LogRequest,
  responseType: dlkit_proto_logging_pb.LogReply
};
LoggingSession.LogAtPriority = {
  methodName: "LogAtPriority",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.LogAtPriorityRequest,
  responseType: dlkit_proto_logging_pb.LogAtPriorityReply
};
LoggingSession.GetLogEntryForm = {
  methodName: "GetLogEntryForm",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogEntryFormRequest,
  responseType: dlkit_proto_logging_pb.GetLogEntryFormReply
};
LoggingSession.CreateLogEntry = {
  methodName: "CreateLogEntry",
  service: LoggingSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CreateLogEntryRequest,
  responseType: dlkit_proto_logging_pb.CreateLogEntryReply
};
var LogEntryLookupSession = {
  serviceName: "dlkit.proto.logging.LogEntryLookupSession"
};
LogEntryLookupSession.GetLogId = {
  methodName: "GetLogId",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogIdRequest,
  responseType: dlkit_proto_logging_pb.GetLogIdReply
};
LogEntryLookupSession.GetLog = {
  methodName: "GetLog",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogRequest,
  responseType: dlkit_proto_logging_pb.GetLogReply
};
LogEntryLookupSession.CanReadLog = {
  methodName: "CanReadLog",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanReadLogRequest,
  responseType: dlkit_proto_logging_pb.CanReadLogReply
};
LogEntryLookupSession.UseComparativeLogEntryView = {
  methodName: "UseComparativeLogEntryView",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseComparativeLogEntryViewRequest,
  responseType: dlkit_proto_logging_pb.UseComparativeLogEntryViewReply
};
LogEntryLookupSession.UsePlenaryLogEntryView = {
  methodName: "UsePlenaryLogEntryView",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UsePlenaryLogEntryViewRequest,
  responseType: dlkit_proto_logging_pb.UsePlenaryLogEntryViewReply
};
LogEntryLookupSession.UseFederatedLogView = {
  methodName: "UseFederatedLogView",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseFederatedLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseFederatedLogViewReply
};
LogEntryLookupSession.UseIsolatedLogView = {
  methodName: "UseIsolatedLogView",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseIsolatedLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseIsolatedLogViewReply
};
LogEntryLookupSession.GetLogEntry = {
  methodName: "GetLogEntry",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogEntryRequest,
  responseType: dlkit_proto_logging_pb.GetLogEntryReply
};
LogEntryLookupSession.GetLogEntriesByIds = {
  methodName: "GetLogEntriesByIds",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByIdsRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByGenusType = {
  methodName: "GetLogEntriesByGenusType",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByGenusTypeRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByParentGenusType = {
  methodName: "GetLogEntriesByParentGenusType",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByParentGenusTypeRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByRecordType = {
  methodName: "GetLogEntriesByRecordType",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByRecordTypeRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByPriorityType = {
  methodName: "GetLogEntriesByPriorityType",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByPriorityTypeRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByDate = {
  methodName: "GetLogEntriesByDate",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByDateRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByPriorityTypeAndDate = {
  methodName: "GetLogEntriesByPriorityTypeAndDate",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByPriorityTypeAndDateRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesForResource = {
  methodName: "GetLogEntriesForResource",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesForResourceRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByDateForResource = {
  methodName: "GetLogEntriesByDateForResource",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByDateForResourceRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntriesByPriorityTypeAndDateForResource = {
  methodName: "GetLogEntriesByPriorityTypeAndDateForResource",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByPriorityTypeAndDateForResourceRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLookupSession.GetLogEntries = {
  methodName: "GetLogEntries",
  service: LogEntryLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
var LogEntryQuerySession = {
  serviceName: "dlkit.proto.logging.LogEntryQuerySession"
};
LogEntryQuerySession.GetLogId = {
  methodName: "GetLogId",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogIdRequest,
  responseType: dlkit_proto_logging_pb.GetLogIdReply
};
LogEntryQuerySession.GetLog = {
  methodName: "GetLog",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogRequest,
  responseType: dlkit_proto_logging_pb.GetLogReply
};
LogEntryQuerySession.CanSearchLogEntries = {
  methodName: "CanSearchLogEntries",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanSearchLogEntriesRequest,
  responseType: dlkit_proto_logging_pb.CanSearchLogEntriesReply
};
LogEntryQuerySession.UseFederatedLogView = {
  methodName: "UseFederatedLogView",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseFederatedLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseFederatedLogViewReply
};
LogEntryQuerySession.UseIsolatedLogView = {
  methodName: "UseIsolatedLogView",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseIsolatedLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseIsolatedLogViewReply
};
LogEntryQuerySession.GetLogEntryQuery = {
  methodName: "GetLogEntryQuery",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogEntryQueryRequest,
  responseType: dlkit_proto_logging_pb.GetLogEntryQueryReply
};
LogEntryQuerySession.GetLogEntriesByQuery = {
  methodName: "GetLogEntriesByQuery",
  service: LogEntryQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByQueryRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
var LogEntryAdminSession = {
  serviceName: "dlkit.proto.logging.LogEntryAdminSession"
};
LogEntryAdminSession.GetLogId = {
  methodName: "GetLogId",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogIdRequest,
  responseType: dlkit_proto_logging_pb.GetLogIdReply
};
LogEntryAdminSession.GetLog = {
  methodName: "GetLog",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogRequest,
  responseType: dlkit_proto_logging_pb.GetLogReply
};
LogEntryAdminSession.CanCreateLogEntries = {
  methodName: "CanCreateLogEntries",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanCreateLogEntriesRequest,
  responseType: dlkit_proto_logging_pb.CanCreateLogEntriesReply
};
LogEntryAdminSession.CanCreateLogEntryWithRecordTypes = {
  methodName: "CanCreateLogEntryWithRecordTypes",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanCreateLogEntryWithRecordTypesRequest,
  responseType: dlkit_proto_logging_pb.CanCreateLogEntryWithRecordTypesReply
};
LogEntryAdminSession.GetLogEntryFormForCreate = {
  methodName: "GetLogEntryFormForCreate",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogEntryFormForCreateRequest,
  responseType: dlkit_proto_logging_pb.GetLogEntryFormForCreateReply
};
LogEntryAdminSession.CreateLogEntry = {
  methodName: "CreateLogEntry",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CreateLogEntryRequest,
  responseType: dlkit_proto_logging_pb.CreateLogEntryReply
};
LogEntryAdminSession.CanUpdateLogEntries = {
  methodName: "CanUpdateLogEntries",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanUpdateLogEntriesRequest,
  responseType: dlkit_proto_logging_pb.CanUpdateLogEntriesReply
};
LogEntryAdminSession.GetLogEntryFormForUpdate = {
  methodName: "GetLogEntryFormForUpdate",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogEntryFormForUpdateRequest,
  responseType: dlkit_proto_logging_pb.GetLogEntryFormForUpdateReply
};
LogEntryAdminSession.UpdateLogEntry = {
  methodName: "UpdateLogEntry",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UpdateLogEntryRequest,
  responseType: dlkit_proto_logging_pb.UpdateLogEntryReply
};
LogEntryAdminSession.CanDeleteLogEntries = {
  methodName: "CanDeleteLogEntries",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanDeleteLogEntriesRequest,
  responseType: dlkit_proto_logging_pb.CanDeleteLogEntriesReply
};
LogEntryAdminSession.DeleteLogEntry = {
  methodName: "DeleteLogEntry",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.DeleteLogEntryRequest,
  responseType: dlkit_proto_logging_pb.DeleteLogEntryReply
};
LogEntryAdminSession.CanManageLogEntryAliases = {
  methodName: "CanManageLogEntryAliases",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanManageLogEntryAliasesRequest,
  responseType: dlkit_proto_logging_pb.CanManageLogEntryAliasesReply
};
LogEntryAdminSession.AliasLogEntry = {
  methodName: "AliasLogEntry",
  service: LogEntryAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.AliasLogEntryRequest,
  responseType: dlkit_proto_logging_pb.AliasLogEntryReply
};
var LogEntryLogSession = {
  serviceName: "dlkit.proto.logging.LogEntryLogSession"
};
LogEntryLogSession.UseComparativeLogView = {
  methodName: "UseComparativeLogView",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseComparativeLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseComparativeLogViewReply
};
LogEntryLogSession.UsePlenaryLogView = {
  methodName: "UsePlenaryLogView",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UsePlenaryLogViewRequest,
  responseType: dlkit_proto_logging_pb.UsePlenaryLogViewReply
};
LogEntryLogSession.CanLookupLogEntryLogMappings = {
  methodName: "CanLookupLogEntryLogMappings",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanLookupLogEntryLogMappingsRequest,
  responseType: dlkit_proto_logging_pb.CanLookupLogEntryLogMappingsReply
};
LogEntryLogSession.GetLogEntryIdsByLog = {
  methodName: "GetLogEntryIdsByLog",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntryIdsByLogRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogEntryLogSession.GetLogEntriesByLog = {
  methodName: "GetLogEntriesByLog",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntriesByLogRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLogSession.GetLogEntrieByLog = {
  methodName: "GetLogEntrieByLog",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogEntrieByLogRequest,
  responseType: dlkit_proto_logging_pb.LogEntry
};
LogEntryLogSession.GetLogIdsByLogEntry = {
  methodName: "GetLogIdsByLogEntry",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogIdsByLogEntryRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogEntryLogSession.GetLogByLogEntry = {
  methodName: "GetLogByLogEntry",
  service: LogEntryLogSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogByLogEntryRequest,
  responseType: dlkit_proto_logging_pb.Log
};
var LogEntryLogAssignmentSession = {
  serviceName: "dlkit.proto.logging.LogEntryLogAssignmentSession"
};
LogEntryLogAssignmentSession.CanAssignLogEntries = {
  methodName: "CanAssignLogEntries",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanAssignLogEntriesRequest,
  responseType: dlkit_proto_logging_pb.CanAssignLogEntriesReply
};
LogEntryLogAssignmentSession.CanAssignLogEntriesToLog = {
  methodName: "CanAssignLogEntriesToLog",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanAssignLogEntriesToLogRequest,
  responseType: dlkit_proto_logging_pb.CanAssignLogEntriesToLogReply
};
LogEntryLogAssignmentSession.GetAssignableLogIds = {
  methodName: "GetAssignableLogIds",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetAssignableLogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogEntryLogAssignmentSession.GetAssignableLogIdsForLogEntry = {
  methodName: "GetAssignableLogIdsForLogEntry",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetAssignableLogIdsForLogEntryRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogEntryLogAssignmentSession.AssignLogEntryToLog = {
  methodName: "AssignLogEntryToLog",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.AssignLogEntryToLogRequest,
  responseType: dlkit_proto_logging_pb.AssignLogEntryToLogReply
};
LogEntryLogAssignmentSession.UnassignLogEntryFromLog = {
  methodName: "UnassignLogEntryFromLog",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UnassignLogEntryFromLogRequest,
  responseType: dlkit_proto_logging_pb.UnassignLogEntryFromLogReply
};
LogEntryLogAssignmentSession.ReassignLogEntryToLog = {
  methodName: "ReassignLogEntryToLog",
  service: LogEntryLogAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.ReassignLogEntryToLogRequest,
  responseType: dlkit_proto_logging_pb.ReassignLogEntryToLogReply
};
var LogLookupSession = {
  serviceName: "dlkit.proto.logging.LogLookupSession"
};
LogLookupSession.CanLookupLogs = {
  methodName: "CanLookupLogs",
  service: LogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanLookupLogsRequest,
  responseType: dlkit_proto_logging_pb.CanLookupLogsReply
};
LogLookupSession.UseComparativeLogView = {
  methodName: "UseComparativeLogView",
  service: LogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseComparativeLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseComparativeLogViewReply
};
LogLookupSession.UsePlenaryLogView = {
  methodName: "UsePlenaryLogView",
  service: LogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UsePlenaryLogViewRequest,
  responseType: dlkit_proto_logging_pb.UsePlenaryLogViewReply
};
LogLookupSession.GetLog = {
  methodName: "GetLog",
  service: LogLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogRequest,
  responseType: dlkit_proto_logging_pb.GetLogReply
};
LogLookupSession.GetLogsByIds = {
  methodName: "GetLogsByIds",
  service: LogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogsByIdsRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogLookupSession.GetLogsByGenusType = {
  methodName: "GetLogsByGenusType",
  service: LogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogsByGenusTypeRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogLookupSession.GetLogsByParentGenusType = {
  methodName: "GetLogsByParentGenusType",
  service: LogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogsByParentGenusTypeRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogLookupSession.GetLogsByRecordType = {
  methodName: "GetLogsByRecordType",
  service: LogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogsByRecordTypeRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogLookupSession.GetLogsByProvider = {
  methodName: "GetLogsByProvider",
  service: LogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogsByProviderRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogLookupSession.GetLogs = {
  methodName: "GetLogs",
  service: LogLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetLogsRequest,
  responseType: dlkit_proto_logging_pb.Log
};
var LogAdminSession = {
  serviceName: "dlkit.proto.logging.LogAdminSession"
};
LogAdminSession.CanCreateLogs = {
  methodName: "CanCreateLogs",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanCreateLogsRequest,
  responseType: dlkit_proto_logging_pb.CanCreateLogsReply
};
LogAdminSession.CanCreateLogWithRecordTypes = {
  methodName: "CanCreateLogWithRecordTypes",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanCreateLogWithRecordTypesRequest,
  responseType: dlkit_proto_logging_pb.CanCreateLogWithRecordTypesReply
};
LogAdminSession.GetLogFormForCreate = {
  methodName: "GetLogFormForCreate",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogFormForCreateRequest,
  responseType: dlkit_proto_logging_pb.GetLogFormForCreateReply
};
LogAdminSession.CreateLog = {
  methodName: "CreateLog",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CreateLogRequest,
  responseType: dlkit_proto_logging_pb.CreateLogReply
};
LogAdminSession.CanUpdateLogs = {
  methodName: "CanUpdateLogs",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanUpdateLogsRequest,
  responseType: dlkit_proto_logging_pb.CanUpdateLogsReply
};
LogAdminSession.GetLogFormForUpdate = {
  methodName: "GetLogFormForUpdate",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogFormForUpdateRequest,
  responseType: dlkit_proto_logging_pb.GetLogFormForUpdateReply
};
LogAdminSession.UpdateLog = {
  methodName: "UpdateLog",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UpdateLogRequest,
  responseType: dlkit_proto_logging_pb.UpdateLogReply
};
LogAdminSession.CanDeleteLogs = {
  methodName: "CanDeleteLogs",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanDeleteLogsRequest,
  responseType: dlkit_proto_logging_pb.CanDeleteLogsReply
};
LogAdminSession.DeleteLog = {
  methodName: "DeleteLog",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.DeleteLogRequest,
  responseType: dlkit_proto_logging_pb.DeleteLogReply
};
LogAdminSession.CanManageLogAliases = {
  methodName: "CanManageLogAliases",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanManageLogAliasesRequest,
  responseType: dlkit_proto_logging_pb.CanManageLogAliasesReply
};
LogAdminSession.AliasLog = {
  methodName: "AliasLog",
  service: LogAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.AliasLogRequest,
  responseType: dlkit_proto_logging_pb.AliasLogReply
};
var LogHierarchySession = {
  serviceName: "dlkit.proto.logging.LogHierarchySession"
};
LogHierarchySession.GetLogHierarchyId = {
  methodName: "GetLogHierarchyId",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogHierarchyIdRequest,
  responseType: dlkit_proto_logging_pb.GetLogHierarchyIdReply
};
LogHierarchySession.GetLogHierarchy = {
  methodName: "GetLogHierarchy",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogHierarchyRequest,
  responseType: dlkit_proto_logging_pb.GetLogHierarchyReply
};
LogHierarchySession.CanAccessLogHierarchy = {
  methodName: "CanAccessLogHierarchy",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanAccessLogHierarchyRequest,
  responseType: dlkit_proto_logging_pb.CanAccessLogHierarchyReply
};
LogHierarchySession.UseComparativeLogView = {
  methodName: "UseComparativeLogView",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UseComparativeLogViewRequest,
  responseType: dlkit_proto_logging_pb.UseComparativeLogViewReply
};
LogHierarchySession.UsePlenaryLogView = {
  methodName: "UsePlenaryLogView",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.UsePlenaryLogViewRequest,
  responseType: dlkit_proto_logging_pb.UsePlenaryLogViewReply
};
LogHierarchySession.GetRootLogIds = {
  methodName: "GetRootLogIds",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetRootLogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogHierarchySession.GetRootLogs = {
  methodName: "GetRootLogs",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetRootLogsRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogHierarchySession.HasParentLogs = {
  methodName: "HasParentLogs",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.HasParentLogsRequest,
  responseType: dlkit_proto_logging_pb.HasParentLogsReply
};
LogHierarchySession.IsParentOfLog = {
  methodName: "IsParentOfLog",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.IsParentOfLogRequest,
  responseType: dlkit_proto_logging_pb.IsParentOfLogReply
};
LogHierarchySession.GetParentLogIds = {
  methodName: "GetParentLogIds",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetParentLogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogHierarchySession.GetParentLogs = {
  methodName: "GetParentLogs",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetParentLogsRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogHierarchySession.IsAncestorOfLog = {
  methodName: "IsAncestorOfLog",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.IsAncestorOfLogRequest,
  responseType: dlkit_proto_logging_pb.IsAncestorOfLogReply
};
LogHierarchySession.HasChildLogs = {
  methodName: "HasChildLogs",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.HasChildLogsRequest,
  responseType: dlkit_proto_logging_pb.HasChildLogsReply
};
LogHierarchySession.IsChildOfLog = {
  methodName: "IsChildOfLog",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.IsChildOfLogRequest,
  responseType: dlkit_proto_logging_pb.IsChildOfLogReply
};
LogHierarchySession.GetChildLogIds = {
  methodName: "GetChildLogIds",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetChildLogIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
LogHierarchySession.GetChildLogs = {
  methodName: "GetChildLogs",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_logging_pb.GetChildLogsRequest,
  responseType: dlkit_proto_logging_pb.Log
};
LogHierarchySession.IsDescendantOfLog = {
  methodName: "IsDescendantOfLog",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.IsDescendantOfLogRequest,
  responseType: dlkit_proto_logging_pb.IsDescendantOfLogReply
};
LogHierarchySession.GetLogNodeIds = {
  methodName: "GetLogNodeIds",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogNodeIdsRequest,
  responseType: dlkit_proto_logging_pb.GetLogNodeIdsReply
};
LogHierarchySession.GetLogNodes = {
  methodName: "GetLogNodes",
  service: LogHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogNodesRequest,
  responseType: dlkit_proto_logging_pb.GetLogNodesReply
};
var LogHierarchyDesignSession = {
  serviceName: "dlkit.proto.logging.LogHierarchyDesignSession"
};
LogHierarchyDesignSession.GetLogHierarchyId = {
  methodName: "GetLogHierarchyId",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogHierarchyIdRequest,
  responseType: dlkit_proto_logging_pb.GetLogHierarchyIdReply
};
LogHierarchyDesignSession.GetLogHierarchy = {
  methodName: "GetLogHierarchy",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.GetLogHierarchyRequest,
  responseType: dlkit_proto_logging_pb.GetLogHierarchyReply
};
LogHierarchyDesignSession.CanModifyLogHierarchy = {
  methodName: "CanModifyLogHierarchy",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.CanModifyLogHierarchyRequest,
  responseType: dlkit_proto_logging_pb.CanModifyLogHierarchyReply
};
LogHierarchyDesignSession.AddRootLog = {
  methodName: "AddRootLog",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.AddRootLogRequest,
  responseType: dlkit_proto_logging_pb.AddRootLogReply
};
LogHierarchyDesignSession.RemoveRootLog = {
  methodName: "RemoveRootLog",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.RemoveRootLogRequest,
  responseType: dlkit_proto_logging_pb.RemoveRootLogReply
};
LogHierarchyDesignSession.AddChildLog = {
  methodName: "AddChildLog",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.AddChildLogRequest,
  responseType: dlkit_proto_logging_pb.AddChildLogReply
};
LogHierarchyDesignSession.RemoveChildLog = {
  methodName: "RemoveChildLog",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.RemoveChildLogRequest,
  responseType: dlkit_proto_logging_pb.RemoveChildLogReply
};
LogHierarchyDesignSession.RemoveChildLogs = {
  methodName: "RemoveChildLogs",
  service: LogHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_logging_pb.RemoveChildLogsRequest,
  responseType: dlkit_proto_logging_pb.RemoveChildLogsReply
};
module.exports = {
  LoggingSession: LoggingSession,
  LogEntryLookupSession: LogEntryLookupSession,
  LogEntryQuerySession: LogEntryQuerySession,
  LogEntryAdminSession: LogEntryAdminSession,
  LogEntryLogSession: LogEntryLogSession,
  LogEntryLogAssignmentSession: LogEntryLogAssignmentSession,
  LogLookupSession: LogLookupSession,
  LogAdminSession: LogAdminSession,
  LogHierarchySession: LogHierarchySession,
  LogHierarchyDesignSession: LogHierarchyDesignSession,
};

