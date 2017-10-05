/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var dlkit_primordium_id_primitives_pb = require('../../dlkit/primordium/id/primitives_pb.js');
var dlkit_primordium_locale_primitives_pb = require('../../dlkit/primordium/locale/primitives_pb.js');
var dlkit_primordium_type_primitives_pb = require('../../dlkit/primordium/type/primitives_pb.js');
var dlkit_proto_hierarchy_pb = require('../../dlkit/proto/hierarchy_pb.js');
var dlkit_proto_osid_pb = require('../../dlkit/proto/osid_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
goog.exportSymbol('proto.dlkit.proto.logging.AddChildLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AddChildLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AddRootLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AddRootLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AliasLogEntryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AliasLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AliasLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AliasLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AssignLogEntryToLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.AssignLogEntryToLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanAccessLogHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanAccessLogHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanAssignLogEntriesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanAssignLogEntriesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogEntriesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogEntriesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanCreateLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanDeleteLogEntriesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanDeleteLogEntriesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanDeleteLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanDeleteLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanLookupLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanLookupLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanManageLogAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanManageLogAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanManageLogEntryAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanModifyLogHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanModifyLogHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanReadLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanReadLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanSearchLogEntriesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanSearchLogEntriesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanUpdateLogEntriesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanUpdateLogEntriesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanUpdateLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CanUpdateLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CreateLogEntryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CreateLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CreateLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.CreateLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.DeleteLogEntryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.DeleteLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.DeleteLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.DeleteLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetAssignableLogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetChildLogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetChildLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogByLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntrieByLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesForResourceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntriesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryFormReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryFormRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryQueryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogHierarchyIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogHierarchyIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogNodeIdsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogNodeIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogNodesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogNodesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogsByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogsByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogsByProviderRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogsByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetParentLogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetParentLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetRootLogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.GetRootLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.HasChildLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.HasChildLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.HasParentLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.HasParentLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsAncestorOfLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsAncestorOfLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsChildOfLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsChildOfLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsDescendantOfLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsDescendantOfLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsParentOfLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.IsParentOfLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.Log', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogAtPriorityReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogAtPriorityRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntry', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntryForm', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntryList', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntryQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntryQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntrySearch', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntrySearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogEntrySearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogForm', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogList', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogNode', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogNodeList', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.LogSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.ReassignLogEntryToLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.ReassignLogEntryToLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.RemoveChildLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.RemoveChildLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.RemoveChildLogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.RemoveChildLogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.RemoveRootLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.RemoveRootLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UnassignLogEntryFromLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UpdateLogEntryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UpdateLogEntryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UpdateLogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UpdateLogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseComparativeLogEntryViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseComparativeLogViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseComparativeLogViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseFederatedLogViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseFederatedLogViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseIsolatedLogViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UseIsolatedLogViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UsePlenaryLogViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.logging.UsePlenaryLogViewRequest', null, global);

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntry = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.LogEntry.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntry, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntry.displayName = 'proto.dlkit.proto.logging.LogEntry';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.LogEntry.repeatedFields_ = [8];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntry.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntry.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntry} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntry.toObject = function(includeInstance, msg) {
  var f, obj = {
    agent: (f = msg.getAgent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    log: (f = msg.getLog()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    priority: (f = msg.getPriority()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    timestamp: (f = msg.getTimestamp()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntry}
 */
proto.dlkit.proto.logging.LogEntry.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntry;
  return proto.dlkit.proto.logging.LogEntry.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntry} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntry}
 */
proto.dlkit.proto.logging.LogEntry.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setAgent(value);
      break;
    case 2:
      var value = new dlkit_primordium_locale_primitives_pb.DisplayText;
      reader.readMessage(value,dlkit_primordium_locale_primitives_pb.DisplayText.deserializeBinaryFromReader);
      msg.setDescription(value);
      break;
    case 3:
      var value = new dlkit_primordium_locale_primitives_pb.DisplayText;
      reader.readMessage(value,dlkit_primordium_locale_primitives_pb.DisplayText.deserializeBinaryFromReader);
      msg.setDisplayName(value);
      break;
    case 4:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setGenusTypeId(value);
      break;
    case 5:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 6:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setLog(value);
      break;
    case 7:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setPriority(value);
      break;
    case 8:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 9:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTimestamp(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntry.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntry.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntry} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntry.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAgent();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getDescription();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_locale_primitives_pb.DisplayText.serializeBinaryToWriter
    );
  }
  f = message.getDisplayName();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_locale_primitives_pb.DisplayText.serializeBinaryToWriter
    );
  }
  f = message.getGenusTypeId();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLog();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getPriority();
  if (f != null) {
    writer.writeMessage(
      7,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      8,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getTimestamp();
  if (f != null) {
    writer.writeMessage(
      9,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id agent = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getAgent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setAgent = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearAgent = function() {
  this.setAgent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasAgent = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 3;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 3));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 4;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 4));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 5;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 5));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasId = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional dlkit.proto.osid.OsidCatalog log = 6;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getLog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 6));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setLog = function(value) {
  jspb.Message.setWrapperField(this, 6, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearLog = function() {
  this.setLog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasLog = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type priority = 7;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getPriority = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 7));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setPriority = function(value) {
  jspb.Message.setWrapperField(this, 7, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearPriority = function() {
  this.setPriority(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasPriority = function() {
  return jspb.Message.getField(this, 7) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 8;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 8));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.logging.LogEntry.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 8, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.LogEntry.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 8, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * optional google.protobuf.Timestamp timestamp = 9;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.LogEntry.prototype.getTimestamp = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 9));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.LogEntry.prototype.setTimestamp = function(value) {
  jspb.Message.setWrapperField(this, 9, value);
};


proto.dlkit.proto.logging.LogEntry.prototype.clearTimestamp = function() {
  this.setTimestamp(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogEntry.prototype.hasTimestamp = function() {
  return jspb.Message.getField(this, 9) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntryQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntryQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntryQuery.displayName = 'proto.dlkit.proto.logging.LogEntryQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntryQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntryQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntryQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryQuery.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntryQuery}
 */
proto.dlkit.proto.logging.LogEntryQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntryQuery;
  return proto.dlkit.proto.logging.LogEntryQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntryQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntryQuery}
 */
proto.dlkit.proto.logging.LogEntryQuery.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntryQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntryQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntryQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryQuery.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntryQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntryQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntryQueryInspector.displayName = 'proto.dlkit.proto.logging.LogEntryQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntryQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntryQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntryQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryQueryInspector.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntryQueryInspector}
 */
proto.dlkit.proto.logging.LogEntryQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntryQueryInspector;
  return proto.dlkit.proto.logging.LogEntryQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntryQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntryQueryInspector}
 */
proto.dlkit.proto.logging.LogEntryQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntryQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntryQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntryQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryQueryInspector.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntryForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntryForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntryForm.displayName = 'proto.dlkit.proto.logging.LogEntryForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntryForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntryForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntryForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryForm.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.LogEntryForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntryForm;
  return proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntryForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntryForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntryForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntrySearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntrySearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntrySearchOrder.displayName = 'proto.dlkit.proto.logging.LogEntrySearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntrySearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntrySearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntrySearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntrySearchOrder.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntrySearchOrder}
 */
proto.dlkit.proto.logging.LogEntrySearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntrySearchOrder;
  return proto.dlkit.proto.logging.LogEntrySearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntrySearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntrySearchOrder}
 */
proto.dlkit.proto.logging.LogEntrySearchOrder.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntrySearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntrySearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntrySearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntrySearchOrder.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntrySearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntrySearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntrySearch.displayName = 'proto.dlkit.proto.logging.LogEntrySearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntrySearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntrySearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntrySearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntrySearch.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntrySearch}
 */
proto.dlkit.proto.logging.LogEntrySearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntrySearch;
  return proto.dlkit.proto.logging.LogEntrySearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntrySearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntrySearch}
 */
proto.dlkit.proto.logging.LogEntrySearch.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntrySearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntrySearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntrySearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntrySearch.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntrySearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntrySearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntrySearchResults.displayName = 'proto.dlkit.proto.logging.LogEntrySearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntrySearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntrySearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntrySearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntrySearchResults.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntrySearchResults}
 */
proto.dlkit.proto.logging.LogEntrySearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntrySearchResults;
  return proto.dlkit.proto.logging.LogEntrySearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntrySearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntrySearchResults}
 */
proto.dlkit.proto.logging.LogEntrySearchResults.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntrySearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntrySearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntrySearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntrySearchResults.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogEntryList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.LogEntryList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.LogEntryList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogEntryList.displayName = 'proto.dlkit.proto.logging.LogEntryList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.LogEntryList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogEntryList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogEntryList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogEntryList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryList.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntriesList: jspb.Message.toObjectList(msg.getLogEntriesList(),
    proto.dlkit.proto.logging.LogEntry.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogEntryList}
 */
proto.dlkit.proto.logging.LogEntryList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogEntryList;
  return proto.dlkit.proto.logging.LogEntryList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogEntryList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogEntryList}
 */
proto.dlkit.proto.logging.LogEntryList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntry;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntry.deserializeBinaryFromReader);
      msg.addLogEntries(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogEntryList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogEntryList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogEntryList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogEntryList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntriesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntry.serializeBinaryToWriter
    );
  }
};


/**
 * repeated LogEntry log_entries = 1;
 * @return {!Array.<!proto.dlkit.proto.logging.LogEntry>}
 */
proto.dlkit.proto.logging.LogEntryList.prototype.getLogEntriesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.logging.LogEntry>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.logging.LogEntry, 1));
};


/** @param {!Array.<!proto.dlkit.proto.logging.LogEntry>} value */
proto.dlkit.proto.logging.LogEntryList.prototype.setLogEntriesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.logging.LogEntry=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.logging.LogEntry}
 */
proto.dlkit.proto.logging.LogEntryList.prototype.addLogEntries = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.logging.LogEntry, opt_index);
};


proto.dlkit.proto.logging.LogEntryList.prototype.clearLogEntriesList = function() {
  this.setLogEntriesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.Log = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.Log.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.Log, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.Log.displayName = 'proto.dlkit.proto.logging.Log';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.Log.repeatedFields_ = [5];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.Log.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.Log.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.Log} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.Log.toObject = function(includeInstance, msg) {
  var f, obj = {
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.Log}
 */
proto.dlkit.proto.logging.Log.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.Log;
  return proto.dlkit.proto.logging.Log.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.Log} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.Log}
 */
proto.dlkit.proto.logging.Log.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_locale_primitives_pb.DisplayText;
      reader.readMessage(value,dlkit_primordium_locale_primitives_pb.DisplayText.deserializeBinaryFromReader);
      msg.setDescription(value);
      break;
    case 2:
      var value = new dlkit_primordium_locale_primitives_pb.DisplayText;
      reader.readMessage(value,dlkit_primordium_locale_primitives_pb.DisplayText.deserializeBinaryFromReader);
      msg.setDisplayName(value);
      break;
    case 3:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setGenusTypeId(value);
      break;
    case 4:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 5:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.Log.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.Log.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.Log} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.Log.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDescription();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_locale_primitives_pb.DisplayText.serializeBinaryToWriter
    );
  }
  f = message.getDisplayName();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_locale_primitives_pb.DisplayText.serializeBinaryToWriter
    );
  }
  f = message.getGenusTypeId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      5,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 1;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.logging.Log.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.logging.Log.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.Log.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.Log.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.logging.Log.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.logging.Log.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.Log.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.Log.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.Log.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.Log.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.Log.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.Log.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.Log.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.Log.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.logging.Log.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.Log.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 5;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.logging.Log.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.logging.Log.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.Log.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.logging.Log.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogQuery.displayName = 'proto.dlkit.proto.logging.LogQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogQuery.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogQuery}
 */
proto.dlkit.proto.logging.LogQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogQuery;
  return proto.dlkit.proto.logging.LogQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogQuery}
 */
proto.dlkit.proto.logging.LogQuery.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogQuery.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogQueryInspector.displayName = 'proto.dlkit.proto.logging.LogQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogQueryInspector.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogQueryInspector}
 */
proto.dlkit.proto.logging.LogQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogQueryInspector;
  return proto.dlkit.proto.logging.LogQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogQueryInspector}
 */
proto.dlkit.proto.logging.LogQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogQueryInspector.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogForm.displayName = 'proto.dlkit.proto.logging.LogForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogForm.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogForm}
 */
proto.dlkit.proto.logging.LogForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogForm;
  return proto.dlkit.proto.logging.LogForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogForm}
 */
proto.dlkit.proto.logging.LogForm.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogForm.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogSearchOrder.displayName = 'proto.dlkit.proto.logging.LogSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogSearchOrder.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogSearchOrder}
 */
proto.dlkit.proto.logging.LogSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogSearchOrder;
  return proto.dlkit.proto.logging.LogSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogSearchOrder}
 */
proto.dlkit.proto.logging.LogSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogSearchOrder.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogSearch.displayName = 'proto.dlkit.proto.logging.LogSearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogSearch.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogSearch}
 */
proto.dlkit.proto.logging.LogSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogSearch;
  return proto.dlkit.proto.logging.LogSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogSearch}
 */
proto.dlkit.proto.logging.LogSearch.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogSearch.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogSearchResults.displayName = 'proto.dlkit.proto.logging.LogSearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogSearchResults.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogSearchResults}
 */
proto.dlkit.proto.logging.LogSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogSearchResults;
  return proto.dlkit.proto.logging.LogSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogSearchResults}
 */
proto.dlkit.proto.logging.LogSearchResults.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogSearchResults.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.LogList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.LogList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogList.displayName = 'proto.dlkit.proto.logging.LogList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.LogList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogList.toObject = function(includeInstance, msg) {
  var f, obj = {
    logsList: jspb.Message.toObjectList(msg.getLogsList(),
    proto.dlkit.proto.logging.Log.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogList}
 */
proto.dlkit.proto.logging.LogList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogList;
  return proto.dlkit.proto.logging.LogList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogList}
 */
proto.dlkit.proto.logging.LogList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.Log;
      reader.readMessage(value,proto.dlkit.proto.logging.Log.deserializeBinaryFromReader);
      msg.addLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.logging.Log.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Log logs = 1;
 * @return {!Array.<!proto.dlkit.proto.logging.Log>}
 */
proto.dlkit.proto.logging.LogList.prototype.getLogsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.logging.Log>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.logging.Log, 1));
};


/** @param {!Array.<!proto.dlkit.proto.logging.Log>} value */
proto.dlkit.proto.logging.LogList.prototype.setLogsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.logging.Log=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.logging.Log}
 */
proto.dlkit.proto.logging.LogList.prototype.addLogs = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.logging.Log, opt_index);
};


proto.dlkit.proto.logging.LogList.prototype.clearLogsList = function() {
  this.setLogsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogNode = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogNode, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogNode.displayName = 'proto.dlkit.proto.logging.LogNode';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogNode.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogNode.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogNode} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogNode.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogNode}
 */
proto.dlkit.proto.logging.LogNode.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogNode;
  return proto.dlkit.proto.logging.LogNode.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogNode} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogNode}
 */
proto.dlkit.proto.logging.LogNode.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogNode.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogNode.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogNode} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogNode.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogNodeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.LogNodeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.LogNodeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogNodeList.displayName = 'proto.dlkit.proto.logging.LogNodeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.LogNodeList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogNodeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogNodeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogNodeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogNodeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    logNodesList: jspb.Message.toObjectList(msg.getLogNodesList(),
    proto.dlkit.proto.logging.LogNode.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogNodeList}
 */
proto.dlkit.proto.logging.LogNodeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogNodeList;
  return proto.dlkit.proto.logging.LogNodeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogNodeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogNodeList}
 */
proto.dlkit.proto.logging.LogNodeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogNode;
      reader.readMessage(value,proto.dlkit.proto.logging.LogNode.deserializeBinaryFromReader);
      msg.addLogNodes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogNodeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogNodeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogNodeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogNodeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogNodesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogNode.serializeBinaryToWriter
    );
  }
};


/**
 * repeated LogNode log_nodes = 1;
 * @return {!Array.<!proto.dlkit.proto.logging.LogNode>}
 */
proto.dlkit.proto.logging.LogNodeList.prototype.getLogNodesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.logging.LogNode>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.logging.LogNode, 1));
};


/** @param {!Array.<!proto.dlkit.proto.logging.LogNode>} value */
proto.dlkit.proto.logging.LogNodeList.prototype.setLogNodesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.logging.LogNode=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.logging.LogNode}
 */
proto.dlkit.proto.logging.LogNodeList.prototype.addLogNodes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.logging.LogNode, opt_index);
};


proto.dlkit.proto.logging.LogNodeList.prototype.clearLogNodesList = function() {
  this.setLogNodesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogIdReply.displayName = 'proto.dlkit.proto.logging.GetLogIdReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogIdReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogIdReply}
 */
proto.dlkit.proto.logging.GetLogIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogIdReply;
  return proto.dlkit.proto.logging.GetLogIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogIdReply}
 */
proto.dlkit.proto.logging.GetLogIdReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogIdReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogIdReply.prototype.hasId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogIdRequest.displayName = 'proto.dlkit.proto.logging.GetLogIdRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogIdRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogIdRequest}
 */
proto.dlkit.proto.logging.GetLogIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogIdRequest;
  return proto.dlkit.proto.logging.GetLogIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogIdRequest}
 */
proto.dlkit.proto.logging.GetLogIdRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogIdRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogReply.displayName = 'proto.dlkit.proto.logging.GetLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    log: (f = msg.getLog()) && proto.dlkit.proto.logging.Log.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogReply}
 */
proto.dlkit.proto.logging.GetLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogReply;
  return proto.dlkit.proto.logging.GetLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogReply}
 */
proto.dlkit.proto.logging.GetLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.Log;
      reader.readMessage(value,proto.dlkit.proto.logging.Log.deserializeBinaryFromReader);
      msg.setLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLog();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.Log.serializeBinaryToWriter
    );
  }
};


/**
 * optional Log log = 1;
 * @return {?proto.dlkit.proto.logging.Log}
 */
proto.dlkit.proto.logging.GetLogReply.prototype.getLog = function() {
  return /** @type{?proto.dlkit.proto.logging.Log} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.Log, 1));
};


/** @param {?proto.dlkit.proto.logging.Log|undefined} value */
proto.dlkit.proto.logging.GetLogReply.prototype.setLog = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogReply.prototype.clearLog = function() {
  this.setLog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogReply.prototype.hasLog = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogRequest.displayName = 'proto.dlkit.proto.logging.GetLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogRequest}
 */
proto.dlkit.proto.logging.GetLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogRequest;
  return proto.dlkit.proto.logging.GetLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogRequest}
 */
proto.dlkit.proto.logging.GetLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanLogReply.displayName = 'proto.dlkit.proto.logging.CanLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanLogReply}
 */
proto.dlkit.proto.logging.CanLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanLogReply;
  return proto.dlkit.proto.logging.CanLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanLogReply}
 */
proto.dlkit.proto.logging.CanLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanLogReply.prototype.getCanLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanLogReply.prototype.setCanLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanLogRequest.displayName = 'proto.dlkit.proto.logging.CanLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanLogRequest}
 */
proto.dlkit.proto.logging.CanLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanLogRequest;
  return proto.dlkit.proto.logging.CanLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanLogRequest}
 */
proto.dlkit.proto.logging.CanLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogReply.displayName = 'proto.dlkit.proto.logging.LogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogReply}
 */
proto.dlkit.proto.logging.LogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogReply;
  return proto.dlkit.proto.logging.LogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogReply}
 */
proto.dlkit.proto.logging.LogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogRequest.displayName = 'proto.dlkit.proto.logging.LogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    content: msg.getContent_asB64(),
    contentType: (f = msg.getContentType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogRequest}
 */
proto.dlkit.proto.logging.LogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogRequest;
  return proto.dlkit.proto.logging.LogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogRequest}
 */
proto.dlkit.proto.logging.LogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {!Uint8Array} */ (reader.readBytes());
      msg.setContent(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setContentType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getContent_asU8();
  if (f.length > 0) {
    writer.writeBytes(
      1,
      f
    );
  }
  f = message.getContentType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional bytes content = 1;
 * @return {!(string|Uint8Array)}
 */
proto.dlkit.proto.logging.LogRequest.prototype.getContent = function() {
  return /** @type {!(string|Uint8Array)} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * optional bytes content = 1;
 * This is a type-conversion wrapper around `getContent()`
 * @return {string}
 */
proto.dlkit.proto.logging.LogRequest.prototype.getContent_asB64 = function() {
  return /** @type {string} */ (jspb.Message.bytesAsB64(
      this.getContent()));
};


/**
 * optional bytes content = 1;
 * Note that Uint8Array is not supported on all browsers.
 * @see http://caniuse.com/Uint8Array
 * This is a type-conversion wrapper around `getContent()`
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogRequest.prototype.getContent_asU8 = function() {
  return /** @type {!Uint8Array} */ (jspb.Message.bytesAsU8(
      this.getContent()));
};


/** @param {!(string|Uint8Array)} value */
proto.dlkit.proto.logging.LogRequest.prototype.setContent = function(value) {
  jspb.Message.setProto3BytesField(this, 1, value);
};


/**
 * optional dlkit.primordium.type.primitives.Type content_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.LogRequest.prototype.getContentType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.LogRequest.prototype.setContentType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.LogRequest.prototype.clearContentType = function() {
  this.setContentType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogRequest.prototype.hasContentType = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogAtPriorityReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogAtPriorityReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogAtPriorityReply.displayName = 'proto.dlkit.proto.logging.LogAtPriorityReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogAtPriorityReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogAtPriorityReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogAtPriorityReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogAtPriorityReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogAtPriorityReply}
 */
proto.dlkit.proto.logging.LogAtPriorityReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogAtPriorityReply;
  return proto.dlkit.proto.logging.LogAtPriorityReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogAtPriorityReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogAtPriorityReply}
 */
proto.dlkit.proto.logging.LogAtPriorityReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogAtPriorityReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogAtPriorityReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogAtPriorityReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogAtPriorityReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.LogAtPriorityRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.LogAtPriorityRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.LogAtPriorityRequest.displayName = 'proto.dlkit.proto.logging.LogAtPriorityRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.LogAtPriorityRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.LogAtPriorityRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    content: msg.getContent_asB64(),
    contentType: (f = msg.getContentType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    priorityType: (f = msg.getPriorityType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.LogAtPriorityRequest}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.LogAtPriorityRequest;
  return proto.dlkit.proto.logging.LogAtPriorityRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.LogAtPriorityRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.LogAtPriorityRequest}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {!Uint8Array} */ (reader.readBytes());
      msg.setContent(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setContentType(value);
      break;
    case 3:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setPriorityType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.LogAtPriorityRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.LogAtPriorityRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getContent_asU8();
  if (f.length > 0) {
    writer.writeBytes(
      1,
      f
    );
  }
  f = message.getContentType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getPriorityType();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional bytes content = 1;
 * @return {!(string|Uint8Array)}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.getContent = function() {
  return /** @type {!(string|Uint8Array)} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * optional bytes content = 1;
 * This is a type-conversion wrapper around `getContent()`
 * @return {string}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.getContent_asB64 = function() {
  return /** @type {string} */ (jspb.Message.bytesAsB64(
      this.getContent()));
};


/**
 * optional bytes content = 1;
 * Note that Uint8Array is not supported on all browsers.
 * @see http://caniuse.com/Uint8Array
 * This is a type-conversion wrapper around `getContent()`
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.getContent_asU8 = function() {
  return /** @type {!Uint8Array} */ (jspb.Message.bytesAsU8(
      this.getContent()));
};


/** @param {!(string|Uint8Array)} value */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.setContent = function(value) {
  jspb.Message.setProto3BytesField(this, 1, value);
};


/**
 * optional dlkit.primordium.type.primitives.Type content_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.getContentType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.setContentType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.clearContentType = function() {
  this.setContentType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.hasContentType = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type priority_type = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.getPriorityType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.setPriorityType = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.clearPriorityType = function() {
  this.setPriorityType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.LogAtPriorityRequest.prototype.hasPriorityType = function() {
  return jspb.Message.getField(this, 3) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryFormReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryFormReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryFormReply.displayName = 'proto.dlkit.proto.logging.GetLogEntryFormReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryFormReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryForm: (f = msg.getLogEntryForm()) && proto.dlkit.proto.logging.LogEntryForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormReply}
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryFormReply;
  return proto.dlkit.proto.logging.GetLogEntryFormReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormReply}
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader);
      msg.setLogEntryForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryFormReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryForm log_entry_form = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.prototype.getLogEntryForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryForm|undefined} value */
proto.dlkit.proto.logging.GetLogEntryFormReply.prototype.setLogEntryForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryFormReply.prototype.clearLogEntryForm = function() {
  this.setLogEntryForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryFormReply.prototype.hasLogEntryForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryFormRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryFormRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntryFormRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryFormRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormRequest}
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryFormRequest;
  return proto.dlkit.proto.logging.GetLogEntryFormRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormRequest}
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryFormRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CreateLogEntryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CreateLogEntryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CreateLogEntryReply.displayName = 'proto.dlkit.proto.logging.CreateLogEntryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CreateLogEntryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CreateLogEntryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CreateLogEntryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogEntryReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CreateLogEntryReply}
 */
proto.dlkit.proto.logging.CreateLogEntryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CreateLogEntryReply;
  return proto.dlkit.proto.logging.CreateLogEntryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CreateLogEntryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CreateLogEntryReply}
 */
proto.dlkit.proto.logging.CreateLogEntryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CreateLogEntryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CreateLogEntryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CreateLogEntryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogEntryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CreateLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CreateLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CreateLogEntryRequest.displayName = 'proto.dlkit.proto.logging.CreateLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CreateLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CreateLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryForm: (f = msg.getLogEntryForm()) && proto.dlkit.proto.logging.LogEntryForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CreateLogEntryRequest}
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CreateLogEntryRequest;
  return proto.dlkit.proto.logging.CreateLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CreateLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CreateLogEntryRequest}
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader);
      msg.setLogEntryForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CreateLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CreateLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryForm log_entry_form = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.prototype.getLogEntryForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryForm|undefined} value */
proto.dlkit.proto.logging.CreateLogEntryRequest.prototype.setLogEntryForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.CreateLogEntryRequest.prototype.clearLogEntryForm = function() {
  this.setLogEntryForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.CreateLogEntryRequest.prototype.hasLogEntryForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanReadLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanReadLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanReadLogReply.displayName = 'proto.dlkit.proto.logging.CanReadLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanReadLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanReadLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanReadLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanReadLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canReadLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanReadLogReply}
 */
proto.dlkit.proto.logging.CanReadLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanReadLogReply;
  return proto.dlkit.proto.logging.CanReadLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanReadLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanReadLogReply}
 */
proto.dlkit.proto.logging.CanReadLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanReadLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanReadLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanReadLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanReadLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanReadLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanReadLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_read_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanReadLogReply.prototype.getCanReadLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanReadLogReply.prototype.setCanReadLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanReadLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanReadLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanReadLogRequest.displayName = 'proto.dlkit.proto.logging.CanReadLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanReadLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanReadLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanReadLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanReadLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanReadLogRequest}
 */
proto.dlkit.proto.logging.CanReadLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanReadLogRequest;
  return proto.dlkit.proto.logging.CanReadLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanReadLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanReadLogRequest}
 */
proto.dlkit.proto.logging.CanReadLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanReadLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanReadLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanReadLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanReadLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseComparativeLogEntryViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.displayName = 'proto.dlkit.proto.logging.UseComparativeLogEntryViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseComparativeLogEntryViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogEntryViewReply}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseComparativeLogEntryViewReply;
  return proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogEntryViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogEntryViewReply}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogEntryViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.displayName = 'proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest;
  return proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogEntryViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.displayName = 'proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply;
  return proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.displayName = 'proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest;
  return proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogEntryViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseFederatedLogViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseFederatedLogViewReply.displayName = 'proto.dlkit.proto.logging.UseFederatedLogViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseFederatedLogViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseFederatedLogViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseFederatedLogViewReply}
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseFederatedLogViewReply;
  return proto.dlkit.proto.logging.UseFederatedLogViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseFederatedLogViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseFederatedLogViewReply}
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseFederatedLogViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseFederatedLogViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseFederatedLogViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseFederatedLogViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseFederatedLogViewRequest.displayName = 'proto.dlkit.proto.logging.UseFederatedLogViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseFederatedLogViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseFederatedLogViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseFederatedLogViewRequest}
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseFederatedLogViewRequest;
  return proto.dlkit.proto.logging.UseFederatedLogViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseFederatedLogViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseFederatedLogViewRequest}
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseFederatedLogViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseFederatedLogViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseFederatedLogViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseIsolatedLogViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseIsolatedLogViewReply.displayName = 'proto.dlkit.proto.logging.UseIsolatedLogViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseIsolatedLogViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseIsolatedLogViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseIsolatedLogViewReply}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseIsolatedLogViewReply;
  return proto.dlkit.proto.logging.UseIsolatedLogViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseIsolatedLogViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseIsolatedLogViewReply}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseIsolatedLogViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseIsolatedLogViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseIsolatedLogViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseIsolatedLogViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseIsolatedLogViewRequest.displayName = 'proto.dlkit.proto.logging.UseIsolatedLogViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseIsolatedLogViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseIsolatedLogViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseIsolatedLogViewRequest}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseIsolatedLogViewRequest;
  return proto.dlkit.proto.logging.UseIsolatedLogViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseIsolatedLogViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseIsolatedLogViewRequest}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseIsolatedLogViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseIsolatedLogViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseIsolatedLogViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryReply.displayName = 'proto.dlkit.proto.logging.GetLogEntryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntry: (f = msg.getLogEntry()) && proto.dlkit.proto.logging.LogEntry.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryReply}
 */
proto.dlkit.proto.logging.GetLogEntryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryReply;
  return proto.dlkit.proto.logging.GetLogEntryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryReply}
 */
proto.dlkit.proto.logging.GetLogEntryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntry;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntry.deserializeBinaryFromReader);
      msg.setLogEntry(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntry();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntry.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntry log_entry = 1;
 * @return {?proto.dlkit.proto.logging.LogEntry}
 */
proto.dlkit.proto.logging.GetLogEntryReply.prototype.getLogEntry = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntry} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntry, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntry|undefined} value */
proto.dlkit.proto.logging.GetLogEntryReply.prototype.setLogEntry = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryReply.prototype.clearLogEntry = function() {
  this.setLogEntry(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryReply.prototype.hasLogEntry = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryRequest}
 */
proto.dlkit.proto.logging.GetLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryRequest;
  return proto.dlkit.proto.logging.GetLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryRequest}
 */
proto.dlkit.proto.logging.GetLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntryRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntryRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryIdsList: jspb.Message.toObjectList(msg.getLogEntryIdsList(),
    dlkit_primordium_id_primitives_pb.Id.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByIdsRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByIdsRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByIdsRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addLogEntryIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id log_entry_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.prototype.getLogEntryIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.prototype.setLogEntryIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.prototype.addLogEntryIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.logging.GetLogEntriesByIdsRequest.prototype.clearLogEntryIdsList = function() {
  this.setLogEntryIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryGenusType: (f = msg.getLogEntryGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setLogEntryGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type log_entry_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.prototype.getLogEntryGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.prototype.setLogEntryGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.prototype.clearLogEntryGenusType = function() {
  this.setLogEntryGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByGenusTypeRequest.prototype.hasLogEntryGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryGenusType: (f = msg.getLogEntryGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setLogEntryGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type log_entry_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.prototype.getLogEntryGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.prototype.setLogEntryGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.prototype.clearLogEntryGenusType = function() {
  this.setLogEntryGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByParentGenusTypeRequest.prototype.hasLogEntryGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryGenusType: (f = msg.getLogEntryGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setLogEntryGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type log_entry_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.prototype.getLogEntryGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.prototype.setLogEntryGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.prototype.clearLogEntryGenusType = function() {
  this.setLogEntryGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByRecordTypeRequest.prototype.hasLogEntryGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    priorityType: (f = msg.getPriorityType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setPriorityType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getPriorityType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type priority_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.prototype.getPriorityType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.prototype.setPriorityType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.prototype.clearPriorityType = function() {
  this.setPriorityType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeRequest.prototype.hasPriorityType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByDateRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    end: (f = msg.getEnd()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    start: (f = msg.getStart()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByDateRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByDateRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByDateRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setEnd(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setStart(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnd();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getStart();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp end = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.getEnd = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.setEnd = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.clearEnd = function() {
  this.setEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.hasEnd = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp start = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.getStart = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.setStart = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.clearStart = function() {
  this.setStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateRequest.prototype.hasStart = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    end: (f = msg.getEnd()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    priorityType: (f = msg.getPriorityType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    start: (f = msg.getStart()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setEnd(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setPriorityType(value);
      break;
    case 3:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setStart(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnd();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getPriorityType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getStart();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp end = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.getEnd = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.setEnd = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.clearEnd = function() {
  this.setEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.hasEnd = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type priority_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.getPriorityType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.setPriorityType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.clearPriorityType = function() {
  this.setPriorityType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.hasPriorityType = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp start = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.getStart = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.setStart = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.clearStart = function() {
  this.setStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateRequest.prototype.hasStart = function() {
  return jspb.Message.getField(this, 3) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesForResourceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesForResourceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesForResourceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesForResourceRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesForResourceRequest;
  return proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesForResourceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesForResourceRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesForResourceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getResourceId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesForResourceRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    end: (f = msg.getEnd()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    start: (f = msg.getStart()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setEnd(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
      break;
    case 3:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setStart(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnd();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getResourceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getStart();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp end = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.getEnd = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.setEnd = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.clearEnd = function() {
  this.setEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.hasEnd = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp start = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.getStart = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.setStart = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.clearStart = function() {
  this.setStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByDateForResourceRequest.prototype.hasStart = function() {
  return jspb.Message.getField(this, 3) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    end: (f = msg.getEnd()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    priorityType: (f = msg.getPriorityType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    start: (f = msg.getStart()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setEnd(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setPriorityType(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
      break;
    case 4:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setStart(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnd();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getPriorityType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getResourceId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getStart();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp end = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.getEnd = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.setEnd = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.clearEnd = function() {
  this.setEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.hasEnd = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type priority_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.getPriorityType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.setPriorityType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.clearPriorityType = function() {
  this.setPriorityType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.hasPriorityType = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp start = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.getStart = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.setStart = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.clearStart = function() {
  this.setStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByPriorityTypeAndDateForResourceRequest.prototype.hasStart = function() {
  return jspb.Message.getField(this, 4) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesRequest;
  return proto.dlkit.proto.logging.GetLogEntriesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanSearchLogEntriesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanSearchLogEntriesReply.displayName = 'proto.dlkit.proto.logging.CanSearchLogEntriesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanSearchLogEntriesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanSearchLogEntriesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canSearchLogEntries: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanSearchLogEntriesReply}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanSearchLogEntriesReply;
  return proto.dlkit.proto.logging.CanSearchLogEntriesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanSearchLogEntriesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanSearchLogEntriesReply}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanSearchLogEntries(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanSearchLogEntriesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanSearchLogEntriesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanSearchLogEntries();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_search_log_entries = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.prototype.getCanSearchLogEntries = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanSearchLogEntriesReply.prototype.setCanSearchLogEntries = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanSearchLogEntriesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanSearchLogEntriesRequest.displayName = 'proto.dlkit.proto.logging.CanSearchLogEntriesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanSearchLogEntriesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanSearchLogEntriesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanSearchLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanSearchLogEntriesRequest;
  return proto.dlkit.proto.logging.CanSearchLogEntriesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanSearchLogEntriesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanSearchLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanSearchLogEntriesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanSearchLogEntriesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanSearchLogEntriesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryQueryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryQueryReply.displayName = 'proto.dlkit.proto.logging.GetLogEntryQueryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryQueryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryQueryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryQuery: (f = msg.getLogEntryQuery()) && proto.dlkit.proto.logging.LogEntryQuery.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryQueryReply}
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryQueryReply;
  return proto.dlkit.proto.logging.GetLogEntryQueryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryQueryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryQueryReply}
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryQuery;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryQuery.deserializeBinaryFromReader);
      msg.setLogEntryQuery(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryQueryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryQueryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryQuery log_entry_query = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryQuery}
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.prototype.getLogEntryQuery = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryQuery, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryQuery|undefined} value */
proto.dlkit.proto.logging.GetLogEntryQueryReply.prototype.setLogEntryQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryQueryReply.prototype.clearLogEntryQuery = function() {
  this.setLogEntryQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryQueryReply.prototype.hasLogEntryQuery = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryQueryRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntryQueryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryQueryRequest}
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryQueryRequest;
  return proto.dlkit.proto.logging.GetLogEntryQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryQueryRequest}
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByQueryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryQuery: (f = msg.getLogEntryQuery()) && proto.dlkit.proto.logging.LogEntryQuery.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByQueryRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByQueryRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByQueryRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryQuery;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryQuery.deserializeBinaryFromReader);
      msg.setLogEntryQuery(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryQuery log_entry_query = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryQuery}
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.prototype.getLogEntryQuery = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryQuery, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryQuery|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.prototype.setLogEntryQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.prototype.clearLogEntryQuery = function() {
  this.setLogEntryQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByQueryRequest.prototype.hasLogEntryQuery = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogEntriesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogEntriesReply.displayName = 'proto.dlkit.proto.logging.CanCreateLogEntriesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogEntriesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntriesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateLogEntries: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntriesReply}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogEntriesReply;
  return proto.dlkit.proto.logging.CanCreateLogEntriesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntriesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntriesReply}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateLogEntries(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogEntriesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntriesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateLogEntries();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_log_entries = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.prototype.getCanCreateLogEntries = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanCreateLogEntriesReply.prototype.setCanCreateLogEntries = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogEntriesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogEntriesRequest.displayName = 'proto.dlkit.proto.logging.CanCreateLogEntriesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogEntriesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntriesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogEntriesRequest;
  return proto.dlkit.proto.logging.CanCreateLogEntriesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntriesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogEntriesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntriesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntriesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.displayName = 'proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateLogEntryWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply;
  return proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateLogEntryWithRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateLogEntryWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_log_entry_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.prototype.getCanCreateLogEntryWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesReply.prototype.setCanCreateLogEntryWithRecordTypes = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.displayName = 'proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryRecordTypesList: jspb.Message.toObjectList(msg.getLogEntryRecordTypesList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest;
  return proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addLogEntryRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type log_entry_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.prototype.getLogEntryRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.prototype.setLogEntryRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.prototype.addLogEntryRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.logging.CanCreateLogEntryWithRecordTypesRequest.prototype.clearLogEntryRecordTypesList = function() {
  this.setLogEntryRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.displayName = 'proto.dlkit.proto.logging.GetLogEntryFormForCreateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryForm: (f = msg.getLogEntryForm()) && proto.dlkit.proto.logging.LogEntryForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForCreateReply}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryFormForCreateReply;
  return proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForCreateReply}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader);
      msg.setLogEntryForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryForm log_entry_form = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.prototype.getLogEntryForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryForm|undefined} value */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.prototype.setLogEntryForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.prototype.clearLogEntryForm = function() {
  this.setLogEntryForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateReply.prototype.hasLogEntryForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryRecordTypesList: jspb.Message.toObjectList(msg.getLogEntryRecordTypesList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest;
  return proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addLogEntryRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type log_entry_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.prototype.getLogEntryRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.prototype.setLogEntryRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.prototype.addLogEntryRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.logging.GetLogEntryFormForCreateRequest.prototype.clearLogEntryRecordTypesList = function() {
  this.setLogEntryRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanUpdateLogEntriesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanUpdateLogEntriesReply.displayName = 'proto.dlkit.proto.logging.CanUpdateLogEntriesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanUpdateLogEntriesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanUpdateLogEntriesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateLogEntries: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogEntriesReply}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanUpdateLogEntriesReply;
  return proto.dlkit.proto.logging.CanUpdateLogEntriesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogEntriesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogEntriesReply}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateLogEntries(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanUpdateLogEntriesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogEntriesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateLogEntries();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_log_entries = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.prototype.getCanUpdateLogEntries = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanUpdateLogEntriesReply.prototype.setCanUpdateLogEntries = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanUpdateLogEntriesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.displayName = 'proto.dlkit.proto.logging.CanUpdateLogEntriesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanUpdateLogEntriesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanUpdateLogEntriesRequest;
  return proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogEntriesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogEntriesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogEntriesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.displayName = 'proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryForm: (f = msg.getLogEntryForm()) && proto.dlkit.proto.logging.LogEntryForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply;
  return proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader);
      msg.setLogEntryForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryForm log_entry_form = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.prototype.getLogEntryForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryForm|undefined} value */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.prototype.setLogEntryForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.prototype.clearLogEntryForm = function() {
  this.setLogEntryForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateReply.prototype.hasLogEntryForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest;
  return proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryFormForUpdateRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UpdateLogEntryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UpdateLogEntryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UpdateLogEntryReply.displayName = 'proto.dlkit.proto.logging.UpdateLogEntryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UpdateLogEntryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UpdateLogEntryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UpdateLogEntryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogEntryReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UpdateLogEntryReply}
 */
proto.dlkit.proto.logging.UpdateLogEntryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UpdateLogEntryReply;
  return proto.dlkit.proto.logging.UpdateLogEntryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UpdateLogEntryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UpdateLogEntryReply}
 */
proto.dlkit.proto.logging.UpdateLogEntryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UpdateLogEntryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UpdateLogEntryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UpdateLogEntryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogEntryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UpdateLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UpdateLogEntryRequest.displayName = 'proto.dlkit.proto.logging.UpdateLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UpdateLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UpdateLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryForm: (f = msg.getLogEntryForm()) && proto.dlkit.proto.logging.LogEntryForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UpdateLogEntryRequest}
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UpdateLogEntryRequest;
  return proto.dlkit.proto.logging.UpdateLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UpdateLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UpdateLogEntryRequest}
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogEntryForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogEntryForm.deserializeBinaryFromReader);
      msg.setLogEntryForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UpdateLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UpdateLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogEntryForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogEntryForm log_entry_form = 1;
 * @return {?proto.dlkit.proto.logging.LogEntryForm}
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.prototype.getLogEntryForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogEntryForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogEntryForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogEntryForm|undefined} value */
proto.dlkit.proto.logging.UpdateLogEntryRequest.prototype.setLogEntryForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.UpdateLogEntryRequest.prototype.clearLogEntryForm = function() {
  this.setLogEntryForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.UpdateLogEntryRequest.prototype.hasLogEntryForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanDeleteLogEntriesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanDeleteLogEntriesReply.displayName = 'proto.dlkit.proto.logging.CanDeleteLogEntriesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanDeleteLogEntriesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanDeleteLogEntriesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteLogEntries: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogEntriesReply}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanDeleteLogEntriesReply;
  return proto.dlkit.proto.logging.CanDeleteLogEntriesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogEntriesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogEntriesReply}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteLogEntries(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanDeleteLogEntriesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogEntriesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteLogEntries();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_log_entries = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.prototype.getCanDeleteLogEntries = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanDeleteLogEntriesReply.prototype.setCanDeleteLogEntries = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanDeleteLogEntriesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.displayName = 'proto.dlkit.proto.logging.CanDeleteLogEntriesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanDeleteLogEntriesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanDeleteLogEntriesRequest;
  return proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogEntriesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogEntriesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogEntriesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.DeleteLogEntryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.DeleteLogEntryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.DeleteLogEntryReply.displayName = 'proto.dlkit.proto.logging.DeleteLogEntryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.DeleteLogEntryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.DeleteLogEntryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.DeleteLogEntryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogEntryReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.DeleteLogEntryReply}
 */
proto.dlkit.proto.logging.DeleteLogEntryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.DeleteLogEntryReply;
  return proto.dlkit.proto.logging.DeleteLogEntryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.DeleteLogEntryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.DeleteLogEntryReply}
 */
proto.dlkit.proto.logging.DeleteLogEntryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.DeleteLogEntryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.DeleteLogEntryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.DeleteLogEntryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogEntryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.DeleteLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.DeleteLogEntryRequest.displayName = 'proto.dlkit.proto.logging.DeleteLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.DeleteLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.DeleteLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.DeleteLogEntryRequest}
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.DeleteLogEntryRequest;
  return proto.dlkit.proto.logging.DeleteLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.DeleteLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.DeleteLogEntryRequest}
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.DeleteLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.DeleteLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.DeleteLogEntryRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.DeleteLogEntryRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.DeleteLogEntryRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanManageLogEntryAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.displayName = 'proto.dlkit.proto.logging.CanManageLogEntryAliasesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanManageLogEntryAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageLogEntryAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanManageLogEntryAliasesReply}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanManageLogEntryAliasesReply;
  return proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanManageLogEntryAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanManageLogEntryAliasesReply}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageLogEntryAliases(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanManageLogEntryAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageLogEntryAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_log_entry_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.prototype.getCanManageLogEntryAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanManageLogEntryAliasesReply.prototype.setCanManageLogEntryAliases = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.displayName = 'proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest;
  return proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogEntryAliasesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AliasLogEntryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AliasLogEntryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AliasLogEntryReply.displayName = 'proto.dlkit.proto.logging.AliasLogEntryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AliasLogEntryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AliasLogEntryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AliasLogEntryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogEntryReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AliasLogEntryReply}
 */
proto.dlkit.proto.logging.AliasLogEntryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AliasLogEntryReply;
  return proto.dlkit.proto.logging.AliasLogEntryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AliasLogEntryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AliasLogEntryReply}
 */
proto.dlkit.proto.logging.AliasLogEntryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AliasLogEntryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AliasLogEntryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AliasLogEntryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogEntryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AliasLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AliasLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AliasLogEntryRequest.displayName = 'proto.dlkit.proto.logging.AliasLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AliasLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AliasLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AliasLogEntryRequest}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AliasLogEntryRequest;
  return proto.dlkit.proto.logging.AliasLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AliasLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AliasLogEntryRequest}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setAliasId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AliasLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AliasLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id alias_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AliasLogEntryRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseComparativeLogViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseComparativeLogViewReply.displayName = 'proto.dlkit.proto.logging.UseComparativeLogViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseComparativeLogViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseComparativeLogViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogViewReply}
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseComparativeLogViewReply;
  return proto.dlkit.proto.logging.UseComparativeLogViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogViewReply}
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseComparativeLogViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UseComparativeLogViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UseComparativeLogViewRequest.displayName = 'proto.dlkit.proto.logging.UseComparativeLogViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UseComparativeLogViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UseComparativeLogViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogViewRequest}
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UseComparativeLogViewRequest;
  return proto.dlkit.proto.logging.UseComparativeLogViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UseComparativeLogViewRequest}
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UseComparativeLogViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UseComparativeLogViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UseComparativeLogViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UsePlenaryLogViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UsePlenaryLogViewReply.displayName = 'proto.dlkit.proto.logging.UsePlenaryLogViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UsePlenaryLogViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogViewReply}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UsePlenaryLogViewReply;
  return proto.dlkit.proto.logging.UsePlenaryLogViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogViewReply}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UsePlenaryLogViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UsePlenaryLogViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UsePlenaryLogViewRequest.displayName = 'proto.dlkit.proto.logging.UsePlenaryLogViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UsePlenaryLogViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogViewRequest}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UsePlenaryLogViewRequest;
  return proto.dlkit.proto.logging.UsePlenaryLogViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UsePlenaryLogViewRequest}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UsePlenaryLogViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UsePlenaryLogViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UsePlenaryLogViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.displayName = 'proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupLogEntryLogMappings: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply;
  return proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupLogEntryLogMappings(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupLogEntryLogMappings();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_log_entry_log_mappings = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.prototype.getCanLookupLogEntryLogMappings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsReply.prototype.setCanLookupLogEntryLogMappings = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.displayName = 'proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest;
  return proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogEntryLogMappingsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest}
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest;
  return proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest}
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntryIdsByLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntriesByLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntriesByLogRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntriesByLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntriesByLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByLogRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntriesByLogRequest;
  return proto.dlkit.proto.logging.GetLogEntriesByLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntriesByLogRequest}
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntriesByLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntriesByLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogEntriesByLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogEntriesByLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.GetLogEntrieByLogRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogEntrieByLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogEntrieByLogRequest.displayName = 'proto.dlkit.proto.logging.GetLogEntrieByLogRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogEntrieByLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogEntrieByLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logIdsList: jspb.Message.toObjectList(msg.getLogIdsList(),
    dlkit_primordium_id_primitives_pb.Id.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogEntrieByLogRequest}
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogEntrieByLogRequest;
  return proto.dlkit.proto.logging.GetLogEntrieByLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogEntrieByLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogEntrieByLogRequest}
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addLogIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogEntrieByLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogEntrieByLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id log_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.prototype.getLogIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.prototype.setLogIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogEntrieByLogRequest.prototype.addLogIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.logging.GetLogEntrieByLogRequest.prototype.clearLogIdsList = function() {
  this.setLogIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.displayName = 'proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest}
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest;
  return proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest}
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogIdsByLogEntryRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogByLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogByLogEntryRequest.displayName = 'proto.dlkit.proto.logging.GetLogByLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogByLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogByLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogByLogEntryRequest}
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogByLogEntryRequest;
  return proto.dlkit.proto.logging.GetLogByLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogByLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogByLogEntryRequest}
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogByLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogByLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogByLogEntryRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogByLogEntryRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanAssignLogEntriesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanAssignLogEntriesReply.displayName = 'proto.dlkit.proto.logging.CanAssignLogEntriesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanAssignLogEntriesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAssignLogEntries: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesReply}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanAssignLogEntriesReply;
  return proto.dlkit.proto.logging.CanAssignLogEntriesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesReply}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAssignLogEntries(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanAssignLogEntriesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAssignLogEntries();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_assign_log_entries = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.prototype.getCanAssignLogEntries = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanAssignLogEntriesReply.prototype.setCanAssignLogEntries = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanAssignLogEntriesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanAssignLogEntriesRequest.displayName = 'proto.dlkit.proto.logging.CanAssignLogEntriesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanAssignLogEntriesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanAssignLogEntriesRequest;
  return proto.dlkit.proto.logging.CanAssignLogEntriesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesRequest}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanAssignLogEntriesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.displayName = 'proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAssignLogEntriesToLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply;
  return proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAssignLogEntriesToLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAssignLogEntriesToLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_assign_log_entries_to_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.prototype.getCanAssignLogEntriesToLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogReply.prototype.setCanAssignLogEntriesToLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.displayName = 'proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest;
  return proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.CanAssignLogEntriesToLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetAssignableLogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetAssignableLogIdsRequest.displayName = 'proto.dlkit.proto.logging.GetAssignableLogIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetAssignableLogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetAssignableLogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetAssignableLogIdsRequest}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetAssignableLogIdsRequest;
  return proto.dlkit.proto.logging.GetAssignableLogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetAssignableLogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetAssignableLogIdsRequest}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetAssignableLogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetAssignableLogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetAssignableLogIdsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.displayName = 'proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest;
  return proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetAssignableLogIdsForLogEntryRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AssignLogEntryToLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AssignLogEntryToLogReply.displayName = 'proto.dlkit.proto.logging.AssignLogEntryToLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AssignLogEntryToLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AssignLogEntryToLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AssignLogEntryToLogReply}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AssignLogEntryToLogReply;
  return proto.dlkit.proto.logging.AssignLogEntryToLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AssignLogEntryToLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AssignLogEntryToLogReply}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AssignLogEntryToLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AssignLogEntryToLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AssignLogEntryToLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AssignLogEntryToLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AssignLogEntryToLogRequest.displayName = 'proto.dlkit.proto.logging.AssignLogEntryToLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AssignLogEntryToLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AssignLogEntryToLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AssignLogEntryToLogRequest}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AssignLogEntryToLogRequest;
  return proto.dlkit.proto.logging.AssignLogEntryToLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AssignLogEntryToLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AssignLogEntryToLogRequest}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AssignLogEntryToLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AssignLogEntryToLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AssignLogEntryToLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UnassignLogEntryFromLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.displayName = 'proto.dlkit.proto.logging.UnassignLogEntryFromLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UnassignLogEntryFromLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UnassignLogEntryFromLogReply}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UnassignLogEntryFromLogReply;
  return proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UnassignLogEntryFromLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UnassignLogEntryFromLogReply}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UnassignLogEntryFromLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.displayName = 'proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest;
  return proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.UnassignLogEntryFromLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.ReassignLogEntryToLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.ReassignLogEntryToLogReply.displayName = 'proto.dlkit.proto.logging.ReassignLogEntryToLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.ReassignLogEntryToLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.ReassignLogEntryToLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.ReassignLogEntryToLogReply}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.ReassignLogEntryToLogReply;
  return proto.dlkit.proto.logging.ReassignLogEntryToLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.ReassignLogEntryToLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.ReassignLogEntryToLogReply}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.ReassignLogEntryToLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.ReassignLogEntryToLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.ReassignLogEntryToLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.displayName = 'proto.dlkit.proto.logging.ReassignLogEntryToLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.ReassignLogEntryToLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    fromLogId: (f = msg.getFromLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logEntryId: (f = msg.getLogEntryId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    toLogId: (f = msg.getToLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.ReassignLogEntryToLogRequest}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.ReassignLogEntryToLogRequest;
  return proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.ReassignLogEntryToLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.ReassignLogEntryToLogRequest}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFromLogId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogEntryId(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setToLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.ReassignLogEntryToLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFromLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogEntryId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getToLogId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id from_log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.getFromLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.setFromLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.clearFromLogId = function() {
  this.setFromLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.hasFromLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_entry_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.getLogEntryId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.setLogEntryId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.clearLogEntryId = function() {
  this.setLogEntryId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.hasLogEntryId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id to_log_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.getToLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.setToLogId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.clearToLogId = function() {
  this.setToLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.ReassignLogEntryToLogRequest.prototype.hasToLogId = function() {
  return jspb.Message.getField(this, 3) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanLookupLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanLookupLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanLookupLogsReply.displayName = 'proto.dlkit.proto.logging.CanLookupLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanLookupLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanLookupLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanLookupLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupLogs: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanLookupLogsReply}
 */
proto.dlkit.proto.logging.CanLookupLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanLookupLogsReply;
  return proto.dlkit.proto.logging.CanLookupLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanLookupLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanLookupLogsReply}
 */
proto.dlkit.proto.logging.CanLookupLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanLookupLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanLookupLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanLookupLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupLogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_logs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanLookupLogsReply.prototype.getCanLookupLogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanLookupLogsReply.prototype.setCanLookupLogs = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanLookupLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanLookupLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanLookupLogsRequest.displayName = 'proto.dlkit.proto.logging.CanLookupLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanLookupLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanLookupLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanLookupLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanLookupLogsRequest}
 */
proto.dlkit.proto.logging.CanLookupLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanLookupLogsRequest;
  return proto.dlkit.proto.logging.CanLookupLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanLookupLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanLookupLogsRequest}
 */
proto.dlkit.proto.logging.CanLookupLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanLookupLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanLookupLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanLookupLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanLookupLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.GetLogsByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogsByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogsByIdsRequest.displayName = 'proto.dlkit.proto.logging.GetLogsByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogsByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogsByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logIdsList: jspb.Message.toObjectList(msg.getLogIdsList(),
    dlkit_primordium_id_primitives_pb.Id.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogsByIdsRequest}
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogsByIdsRequest;
  return proto.dlkit.proto.logging.GetLogsByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogsByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogsByIdsRequest}
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addLogIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogsByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogsByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id log_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.prototype.getLogIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.logging.GetLogsByIdsRequest.prototype.setLogIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogsByIdsRequest.prototype.addLogIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.logging.GetLogsByIdsRequest.prototype.clearLogIdsList = function() {
  this.setLogIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogsByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogsByGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogsByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logGenusType: (f = msg.getLogGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogsByGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogsByGenusTypeRequest;
  return proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogsByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogsByGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setLogGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogsByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type log_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.prototype.getLogGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.prototype.setLogGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.prototype.clearLogGenusType = function() {
  this.setLogGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogsByGenusTypeRequest.prototype.hasLogGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logGenusType: (f = msg.getLogGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest;
  return proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest}
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setLogGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type log_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.prototype.getLogGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.prototype.setLogGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.prototype.clearLogGenusType = function() {
  this.setLogGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogsByParentGenusTypeRequest.prototype.hasLogGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogsByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.displayName = 'proto.dlkit.proto.logging.GetLogsByRecordTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogsByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logRecordType: (f = msg.getLogRecordType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogsByRecordTypeRequest}
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogsByRecordTypeRequest;
  return proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogsByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogsByRecordTypeRequest}
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setLogRecordType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogsByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogRecordType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type log_record_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.prototype.getLogRecordType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.prototype.setLogRecordType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.prototype.clearLogRecordType = function() {
  this.setLogRecordType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogsByRecordTypeRequest.prototype.hasLogRecordType = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogsByProviderRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogsByProviderRequest.displayName = 'proto.dlkit.proto.logging.GetLogsByProviderRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogsByProviderRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogsByProviderRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogsByProviderRequest}
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogsByProviderRequest;
  return proto.dlkit.proto.logging.GetLogsByProviderRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogsByProviderRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogsByProviderRequest}
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogsByProviderRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogsByProviderRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getResourceId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogsByProviderRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogsByProviderRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogsByProviderRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogsRequest.displayName = 'proto.dlkit.proto.logging.GetLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogsRequest}
 */
proto.dlkit.proto.logging.GetLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogsRequest;
  return proto.dlkit.proto.logging.GetLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogsRequest}
 */
proto.dlkit.proto.logging.GetLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogsReply.displayName = 'proto.dlkit.proto.logging.CanCreateLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateLogs: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogsReply}
 */
proto.dlkit.proto.logging.CanCreateLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogsReply;
  return proto.dlkit.proto.logging.CanCreateLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogsReply}
 */
proto.dlkit.proto.logging.CanCreateLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateLogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_logs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanCreateLogsReply.prototype.getCanCreateLogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanCreateLogsReply.prototype.setCanCreateLogs = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogsRequest.displayName = 'proto.dlkit.proto.logging.CanCreateLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogsRequest}
 */
proto.dlkit.proto.logging.CanCreateLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogsRequest;
  return proto.dlkit.proto.logging.CanCreateLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogsRequest}
 */
proto.dlkit.proto.logging.CanCreateLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.displayName = 'proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateLogWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply;
  return proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateLogWithRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateLogWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_log_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.prototype.getCanCreateLogWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesReply.prototype.setCanCreateLogWithRecordTypes = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.displayName = 'proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logRecordTypesList: jspb.Message.toObjectList(msg.getLogRecordTypesList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest;
  return proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addLogRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type log_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.prototype.getLogRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.prototype.setLogRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.prototype.addLogRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.logging.CanCreateLogWithRecordTypesRequest.prototype.clearLogRecordTypesList = function() {
  this.setLogRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogFormForCreateReply.displayName = 'proto.dlkit.proto.logging.GetLogFormForCreateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logForm: (f = msg.getLogForm()) && proto.dlkit.proto.logging.LogForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogFormForCreateReply}
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogFormForCreateReply;
  return proto.dlkit.proto.logging.GetLogFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogFormForCreateReply}
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogForm.deserializeBinaryFromReader);
      msg.setLogForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogForm log_form = 1;
 * @return {?proto.dlkit.proto.logging.LogForm}
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.prototype.getLogForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogForm|undefined} value */
proto.dlkit.proto.logging.GetLogFormForCreateReply.prototype.setLogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogFormForCreateReply.prototype.clearLogForm = function() {
  this.setLogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogFormForCreateReply.prototype.hasLogForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.logging.GetLogFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogFormForCreateRequest.displayName = 'proto.dlkit.proto.logging.GetLogFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logRecordTypesList: jspb.Message.toObjectList(msg.getLogRecordTypesList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogFormForCreateRequest}
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogFormForCreateRequest;
  return proto.dlkit.proto.logging.GetLogFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogFormForCreateRequest}
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addLogRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type log_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.prototype.getLogRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.prototype.setLogRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.logging.GetLogFormForCreateRequest.prototype.addLogRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.logging.GetLogFormForCreateRequest.prototype.clearLogRecordTypesList = function() {
  this.setLogRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CreateLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CreateLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CreateLogReply.displayName = 'proto.dlkit.proto.logging.CreateLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CreateLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CreateLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CreateLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    log: (f = msg.getLog()) && proto.dlkit.proto.logging.Log.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CreateLogReply}
 */
proto.dlkit.proto.logging.CreateLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CreateLogReply;
  return proto.dlkit.proto.logging.CreateLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CreateLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CreateLogReply}
 */
proto.dlkit.proto.logging.CreateLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.Log;
      reader.readMessage(value,proto.dlkit.proto.logging.Log.deserializeBinaryFromReader);
      msg.setLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CreateLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CreateLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CreateLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLog();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.Log.serializeBinaryToWriter
    );
  }
};


/**
 * optional Log log = 1;
 * @return {?proto.dlkit.proto.logging.Log}
 */
proto.dlkit.proto.logging.CreateLogReply.prototype.getLog = function() {
  return /** @type{?proto.dlkit.proto.logging.Log} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.Log, 1));
};


/** @param {?proto.dlkit.proto.logging.Log|undefined} value */
proto.dlkit.proto.logging.CreateLogReply.prototype.setLog = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.CreateLogReply.prototype.clearLog = function() {
  this.setLog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.CreateLogReply.prototype.hasLog = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CreateLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CreateLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CreateLogRequest.displayName = 'proto.dlkit.proto.logging.CreateLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CreateLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CreateLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CreateLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logForm: (f = msg.getLogForm()) && proto.dlkit.proto.logging.LogForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CreateLogRequest}
 */
proto.dlkit.proto.logging.CreateLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CreateLogRequest;
  return proto.dlkit.proto.logging.CreateLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CreateLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CreateLogRequest}
 */
proto.dlkit.proto.logging.CreateLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogForm.deserializeBinaryFromReader);
      msg.setLogForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CreateLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CreateLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CreateLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CreateLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogForm log_form = 1;
 * @return {?proto.dlkit.proto.logging.LogForm}
 */
proto.dlkit.proto.logging.CreateLogRequest.prototype.getLogForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogForm|undefined} value */
proto.dlkit.proto.logging.CreateLogRequest.prototype.setLogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.CreateLogRequest.prototype.clearLogForm = function() {
  this.setLogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.CreateLogRequest.prototype.hasLogForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanUpdateLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanUpdateLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanUpdateLogsReply.displayName = 'proto.dlkit.proto.logging.CanUpdateLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanUpdateLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanUpdateLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateLogs: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogsReply}
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanUpdateLogsReply;
  return proto.dlkit.proto.logging.CanUpdateLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogsReply}
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanUpdateLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateLogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_logs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanUpdateLogsReply.prototype.getCanUpdateLogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanUpdateLogsReply.prototype.setCanUpdateLogs = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanUpdateLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanUpdateLogsRequest.displayName = 'proto.dlkit.proto.logging.CanUpdateLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanUpdateLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanUpdateLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogsRequest}
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanUpdateLogsRequest;
  return proto.dlkit.proto.logging.CanUpdateLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanUpdateLogsRequest}
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanUpdateLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanUpdateLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanUpdateLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogFormForUpdateReply.displayName = 'proto.dlkit.proto.logging.GetLogFormForUpdateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logForm: (f = msg.getLogForm()) && proto.dlkit.proto.logging.LogForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogFormForUpdateReply}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogFormForUpdateReply;
  return proto.dlkit.proto.logging.GetLogFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogFormForUpdateReply}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogForm.deserializeBinaryFromReader);
      msg.setLogForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogForm log_form = 1;
 * @return {?proto.dlkit.proto.logging.LogForm}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.prototype.getLogForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogForm|undefined} value */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.prototype.setLogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogFormForUpdateReply.prototype.clearLogForm = function() {
  this.setLogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateReply.prototype.hasLogForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogFormForUpdateRequest.displayName = 'proto.dlkit.proto.logging.GetLogFormForUpdateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogFormForUpdateRequest}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogFormForUpdateRequest;
  return proto.dlkit.proto.logging.GetLogFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogFormForUpdateRequest}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogFormForUpdateRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogFormForUpdateRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UpdateLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UpdateLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UpdateLogReply.displayName = 'proto.dlkit.proto.logging.UpdateLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UpdateLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UpdateLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UpdateLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UpdateLogReply}
 */
proto.dlkit.proto.logging.UpdateLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UpdateLogReply;
  return proto.dlkit.proto.logging.UpdateLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UpdateLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UpdateLogReply}
 */
proto.dlkit.proto.logging.UpdateLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UpdateLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UpdateLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UpdateLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.UpdateLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.UpdateLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.UpdateLogRequest.displayName = 'proto.dlkit.proto.logging.UpdateLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.UpdateLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.UpdateLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.UpdateLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logForm: (f = msg.getLogForm()) && proto.dlkit.proto.logging.LogForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.UpdateLogRequest}
 */
proto.dlkit.proto.logging.UpdateLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.UpdateLogRequest;
  return proto.dlkit.proto.logging.UpdateLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.UpdateLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.UpdateLogRequest}
 */
proto.dlkit.proto.logging.UpdateLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogForm;
      reader.readMessage(value,proto.dlkit.proto.logging.LogForm.deserializeBinaryFromReader);
      msg.setLogForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.UpdateLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.UpdateLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.UpdateLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.UpdateLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogForm log_form = 1;
 * @return {?proto.dlkit.proto.logging.LogForm}
 */
proto.dlkit.proto.logging.UpdateLogRequest.prototype.getLogForm = function() {
  return /** @type{?proto.dlkit.proto.logging.LogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogForm, 1));
};


/** @param {?proto.dlkit.proto.logging.LogForm|undefined} value */
proto.dlkit.proto.logging.UpdateLogRequest.prototype.setLogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.UpdateLogRequest.prototype.clearLogForm = function() {
  this.setLogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.UpdateLogRequest.prototype.hasLogForm = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanDeleteLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanDeleteLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanDeleteLogsReply.displayName = 'proto.dlkit.proto.logging.CanDeleteLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanDeleteLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanDeleteLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteLogs: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogsReply}
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanDeleteLogsReply;
  return proto.dlkit.proto.logging.CanDeleteLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogsReply}
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanDeleteLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteLogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_logs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanDeleteLogsReply.prototype.getCanDeleteLogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanDeleteLogsReply.prototype.setCanDeleteLogs = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanDeleteLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanDeleteLogsRequest.displayName = 'proto.dlkit.proto.logging.CanDeleteLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanDeleteLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanDeleteLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogsRequest}
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanDeleteLogsRequest;
  return proto.dlkit.proto.logging.CanDeleteLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanDeleteLogsRequest}
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanDeleteLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanDeleteLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanDeleteLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.DeleteLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.DeleteLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.DeleteLogReply.displayName = 'proto.dlkit.proto.logging.DeleteLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.DeleteLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.DeleteLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.DeleteLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.DeleteLogReply}
 */
proto.dlkit.proto.logging.DeleteLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.DeleteLogReply;
  return proto.dlkit.proto.logging.DeleteLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.DeleteLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.DeleteLogReply}
 */
proto.dlkit.proto.logging.DeleteLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.DeleteLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.DeleteLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.DeleteLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.DeleteLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.DeleteLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.DeleteLogRequest.displayName = 'proto.dlkit.proto.logging.DeleteLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.DeleteLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.DeleteLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.DeleteLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.DeleteLogRequest}
 */
proto.dlkit.proto.logging.DeleteLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.DeleteLogRequest;
  return proto.dlkit.proto.logging.DeleteLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.DeleteLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.DeleteLogRequest}
 */
proto.dlkit.proto.logging.DeleteLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.DeleteLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.DeleteLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.DeleteLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.DeleteLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.DeleteLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.DeleteLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.DeleteLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.DeleteLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanManageLogAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanManageLogAliasesReply.displayName = 'proto.dlkit.proto.logging.CanManageLogAliasesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanManageLogAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanManageLogAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageLogAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanManageLogAliasesReply}
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanManageLogAliasesReply;
  return proto.dlkit.proto.logging.CanManageLogAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanManageLogAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanManageLogAliasesReply}
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageLogAliases(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanManageLogAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanManageLogAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageLogAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_log_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanManageLogAliasesReply.prototype.getCanManageLogAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanManageLogAliasesReply.prototype.setCanManageLogAliases = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanManageLogAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanManageLogAliasesRequest.displayName = 'proto.dlkit.proto.logging.CanManageLogAliasesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanManageLogAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanManageLogAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanManageLogAliasesRequest}
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanManageLogAliasesRequest;
  return proto.dlkit.proto.logging.CanManageLogAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanManageLogAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanManageLogAliasesRequest}
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanManageLogAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanManageLogAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanManageLogAliasesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AliasLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AliasLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AliasLogReply.displayName = 'proto.dlkit.proto.logging.AliasLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AliasLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AliasLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AliasLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AliasLogReply}
 */
proto.dlkit.proto.logging.AliasLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AliasLogReply;
  return proto.dlkit.proto.logging.AliasLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AliasLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AliasLogReply}
 */
proto.dlkit.proto.logging.AliasLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AliasLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AliasLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AliasLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AliasLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AliasLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AliasLogRequest.displayName = 'proto.dlkit.proto.logging.AliasLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AliasLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AliasLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AliasLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AliasLogRequest}
 */
proto.dlkit.proto.logging.AliasLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AliasLogRequest;
  return proto.dlkit.proto.logging.AliasLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AliasLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AliasLogRequest}
 */
proto.dlkit.proto.logging.AliasLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setAliasId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AliasLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AliasLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AliasLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AliasLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id alias_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AliasLogRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AliasLogRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.AliasLogRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AliasLogRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AliasLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AliasLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.AliasLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AliasLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogHierarchyIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogHierarchyIdReply.displayName = 'proto.dlkit.proto.logging.GetLogHierarchyIdReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogHierarchyIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyIdReply}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogHierarchyIdReply;
  return proto.dlkit.proto.logging.GetLogHierarchyIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyIdReply}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogHierarchyIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogHierarchyIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdReply.prototype.hasId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogHierarchyIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogHierarchyIdRequest.displayName = 'proto.dlkit.proto.logging.GetLogHierarchyIdRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogHierarchyIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyIdRequest}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogHierarchyIdRequest;
  return proto.dlkit.proto.logging.GetLogHierarchyIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyIdRequest}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogHierarchyIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyIdRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogHierarchyReply.displayName = 'proto.dlkit.proto.logging.GetLogHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hierarchy: (f = msg.getHierarchy()) && dlkit_proto_hierarchy_pb.Hierarchy.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyReply}
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogHierarchyReply;
  return proto.dlkit.proto.logging.GetLogHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyReply}
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_hierarchy_pb.Hierarchy;
      reader.readMessage(value,dlkit_proto_hierarchy_pb.Hierarchy.deserializeBinaryFromReader);
      msg.setHierarchy(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHierarchy();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_hierarchy_pb.Hierarchy.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.hierarchy.Hierarchy hierarchy = 1;
 * @return {?proto.dlkit.proto.hierarchy.Hierarchy}
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.prototype.getHierarchy = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Hierarchy} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Hierarchy, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Hierarchy|undefined} value */
proto.dlkit.proto.logging.GetLogHierarchyReply.prototype.setHierarchy = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogHierarchyReply.prototype.clearHierarchy = function() {
  this.setHierarchy(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogHierarchyReply.prototype.hasHierarchy = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogHierarchyRequest.displayName = 'proto.dlkit.proto.logging.GetLogHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyRequest}
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogHierarchyRequest;
  return proto.dlkit.proto.logging.GetLogHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogHierarchyRequest}
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanAccessLogHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanAccessLogHierarchyReply.displayName = 'proto.dlkit.proto.logging.CanAccessLogHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanAccessLogHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanAccessLogHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAccessLogHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanAccessLogHierarchyReply}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanAccessLogHierarchyReply;
  return proto.dlkit.proto.logging.CanAccessLogHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanAccessLogHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanAccessLogHierarchyReply}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAccessLogHierarchy(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanAccessLogHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanAccessLogHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAccessLogHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_access_log_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.prototype.getCanAccessLogHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanAccessLogHierarchyReply.prototype.setCanAccessLogHierarchy = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanAccessLogHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.displayName = 'proto.dlkit.proto.logging.CanAccessLogHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanAccessLogHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanAccessLogHierarchyRequest}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanAccessLogHierarchyRequest;
  return proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanAccessLogHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanAccessLogHierarchyRequest}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanAccessLogHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanAccessLogHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetRootLogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetRootLogIdsRequest.displayName = 'proto.dlkit.proto.logging.GetRootLogIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetRootLogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetRootLogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetRootLogIdsRequest}
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetRootLogIdsRequest;
  return proto.dlkit.proto.logging.GetRootLogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetRootLogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetRootLogIdsRequest}
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetRootLogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetRootLogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetRootLogIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetRootLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetRootLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetRootLogsRequest.displayName = 'proto.dlkit.proto.logging.GetRootLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetRootLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetRootLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetRootLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetRootLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetRootLogsRequest}
 */
proto.dlkit.proto.logging.GetRootLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetRootLogsRequest;
  return proto.dlkit.proto.logging.GetRootLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetRootLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetRootLogsRequest}
 */
proto.dlkit.proto.logging.GetRootLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetRootLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetRootLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetRootLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetRootLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.HasParentLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.HasParentLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.HasParentLogsReply.displayName = 'proto.dlkit.proto.logging.HasParentLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.HasParentLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.HasParentLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.HasParentLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasParentLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasParentLogs: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.HasParentLogsReply}
 */
proto.dlkit.proto.logging.HasParentLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.HasParentLogsReply;
  return proto.dlkit.proto.logging.HasParentLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.HasParentLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.HasParentLogsReply}
 */
proto.dlkit.proto.logging.HasParentLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasParentLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.HasParentLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.HasParentLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.HasParentLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasParentLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasParentLogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_parent_logs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.HasParentLogsReply.prototype.getHasParentLogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.HasParentLogsReply.prototype.setHasParentLogs = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.HasParentLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.HasParentLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.HasParentLogsRequest.displayName = 'proto.dlkit.proto.logging.HasParentLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.HasParentLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.HasParentLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.HasParentLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasParentLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.HasParentLogsRequest}
 */
proto.dlkit.proto.logging.HasParentLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.HasParentLogsRequest;
  return proto.dlkit.proto.logging.HasParentLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.HasParentLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.HasParentLogsRequest}
 */
proto.dlkit.proto.logging.HasParentLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.HasParentLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.HasParentLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.HasParentLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasParentLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.HasParentLogsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.HasParentLogsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.HasParentLogsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.HasParentLogsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsParentOfLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsParentOfLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsParentOfLogReply.displayName = 'proto.dlkit.proto.logging.IsParentOfLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsParentOfLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsParentOfLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsParentOfLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsParentOfLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isParentOfLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsParentOfLogReply}
 */
proto.dlkit.proto.logging.IsParentOfLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsParentOfLogReply;
  return proto.dlkit.proto.logging.IsParentOfLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsParentOfLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsParentOfLogReply}
 */
proto.dlkit.proto.logging.IsParentOfLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsParentOfLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsParentOfLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsParentOfLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsParentOfLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsParentOfLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsParentOfLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_parent_of_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.IsParentOfLogReply.prototype.getIsParentOfLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.IsParentOfLogReply.prototype.setIsParentOfLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsParentOfLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsParentOfLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsParentOfLogRequest.displayName = 'proto.dlkit.proto.logging.IsParentOfLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsParentOfLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsParentOfLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsParentOfLogRequest}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsParentOfLogRequest;
  return proto.dlkit.proto.logging.IsParentOfLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsParentOfLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsParentOfLogRequest}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsParentOfLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsParentOfLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.hasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsParentOfLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetParentLogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetParentLogIdsRequest.displayName = 'proto.dlkit.proto.logging.GetParentLogIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetParentLogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetParentLogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetParentLogIdsRequest}
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetParentLogIdsRequest;
  return proto.dlkit.proto.logging.GetParentLogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetParentLogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetParentLogIdsRequest}
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetParentLogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetParentLogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetParentLogIdsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetParentLogIdsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetParentLogIdsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetParentLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetParentLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetParentLogsRequest.displayName = 'proto.dlkit.proto.logging.GetParentLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetParentLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetParentLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetParentLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetParentLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetParentLogsRequest}
 */
proto.dlkit.proto.logging.GetParentLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetParentLogsRequest;
  return proto.dlkit.proto.logging.GetParentLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetParentLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetParentLogsRequest}
 */
proto.dlkit.proto.logging.GetParentLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetParentLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetParentLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetParentLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetParentLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetParentLogsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetParentLogsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetParentLogsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetParentLogsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsAncestorOfLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsAncestorOfLogReply.displayName = 'proto.dlkit.proto.logging.IsAncestorOfLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsAncestorOfLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsAncestorOfLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isAncestorOfLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsAncestorOfLogReply}
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsAncestorOfLogReply;
  return proto.dlkit.proto.logging.IsAncestorOfLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsAncestorOfLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsAncestorOfLogReply}
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsAncestorOfLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsAncestorOfLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsAncestorOfLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsAncestorOfLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_ancestor_of_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.IsAncestorOfLogReply.prototype.getIsAncestorOfLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.IsAncestorOfLogReply.prototype.setIsAncestorOfLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsAncestorOfLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsAncestorOfLogRequest.displayName = 'proto.dlkit.proto.logging.IsAncestorOfLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsAncestorOfLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsAncestorOfLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsAncestorOfLogRequest}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsAncestorOfLogRequest;
  return proto.dlkit.proto.logging.IsAncestorOfLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsAncestorOfLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsAncestorOfLogRequest}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsAncestorOfLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsAncestorOfLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.hasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsAncestorOfLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.HasChildLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.HasChildLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.HasChildLogsReply.displayName = 'proto.dlkit.proto.logging.HasChildLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.HasChildLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.HasChildLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.HasChildLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasChildLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasChildLogs: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.HasChildLogsReply}
 */
proto.dlkit.proto.logging.HasChildLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.HasChildLogsReply;
  return proto.dlkit.proto.logging.HasChildLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.HasChildLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.HasChildLogsReply}
 */
proto.dlkit.proto.logging.HasChildLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasChildLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.HasChildLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.HasChildLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.HasChildLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasChildLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasChildLogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_child_logs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.HasChildLogsReply.prototype.getHasChildLogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.HasChildLogsReply.prototype.setHasChildLogs = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.HasChildLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.HasChildLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.HasChildLogsRequest.displayName = 'proto.dlkit.proto.logging.HasChildLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.HasChildLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.HasChildLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.HasChildLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasChildLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.HasChildLogsRequest}
 */
proto.dlkit.proto.logging.HasChildLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.HasChildLogsRequest;
  return proto.dlkit.proto.logging.HasChildLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.HasChildLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.HasChildLogsRequest}
 */
proto.dlkit.proto.logging.HasChildLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.HasChildLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.HasChildLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.HasChildLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.HasChildLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.HasChildLogsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.HasChildLogsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.HasChildLogsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.HasChildLogsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsChildOfLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsChildOfLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsChildOfLogReply.displayName = 'proto.dlkit.proto.logging.IsChildOfLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsChildOfLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsChildOfLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsChildOfLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsChildOfLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isChildOfLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsChildOfLogReply}
 */
proto.dlkit.proto.logging.IsChildOfLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsChildOfLogReply;
  return proto.dlkit.proto.logging.IsChildOfLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsChildOfLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsChildOfLogReply}
 */
proto.dlkit.proto.logging.IsChildOfLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsChildOfLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsChildOfLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsChildOfLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsChildOfLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsChildOfLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsChildOfLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_child_of_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.IsChildOfLogReply.prototype.getIsChildOfLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.IsChildOfLogReply.prototype.setIsChildOfLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsChildOfLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsChildOfLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsChildOfLogRequest.displayName = 'proto.dlkit.proto.logging.IsChildOfLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsChildOfLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsChildOfLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsChildOfLogRequest}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsChildOfLogRequest;
  return proto.dlkit.proto.logging.IsChildOfLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsChildOfLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsChildOfLogRequest}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsChildOfLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsChildOfLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.hasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsChildOfLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetChildLogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetChildLogIdsRequest.displayName = 'proto.dlkit.proto.logging.GetChildLogIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetChildLogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetChildLogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetChildLogIdsRequest}
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetChildLogIdsRequest;
  return proto.dlkit.proto.logging.GetChildLogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetChildLogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetChildLogIdsRequest}
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetChildLogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetChildLogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetChildLogIdsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetChildLogIdsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetChildLogIdsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetChildLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetChildLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetChildLogsRequest.displayName = 'proto.dlkit.proto.logging.GetChildLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetChildLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetChildLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetChildLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetChildLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetChildLogsRequest}
 */
proto.dlkit.proto.logging.GetChildLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetChildLogsRequest;
  return proto.dlkit.proto.logging.GetChildLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetChildLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetChildLogsRequest}
 */
proto.dlkit.proto.logging.GetChildLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetChildLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetChildLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetChildLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetChildLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetChildLogsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetChildLogsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetChildLogsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetChildLogsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsDescendantOfLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsDescendantOfLogReply.displayName = 'proto.dlkit.proto.logging.IsDescendantOfLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsDescendantOfLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsDescendantOfLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isDescendantOfLog: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsDescendantOfLogReply}
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsDescendantOfLogReply;
  return proto.dlkit.proto.logging.IsDescendantOfLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsDescendantOfLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsDescendantOfLogReply}
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsDescendantOfLog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsDescendantOfLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsDescendantOfLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsDescendantOfLog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_descendant_of_log = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.IsDescendantOfLogReply.prototype.getIsDescendantOfLog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.IsDescendantOfLogReply.prototype.setIsDescendantOfLog = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.IsDescendantOfLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.IsDescendantOfLogRequest.displayName = 'proto.dlkit.proto.logging.IsDescendantOfLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.IsDescendantOfLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.IsDescendantOfLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.IsDescendantOfLogRequest}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.IsDescendantOfLogRequest;
  return proto.dlkit.proto.logging.IsDescendantOfLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.IsDescendantOfLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.IsDescendantOfLogRequest}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.IsDescendantOfLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.IsDescendantOfLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.hasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.IsDescendantOfLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogNodeIdsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogNodeIdsReply.displayName = 'proto.dlkit.proto.logging.GetLogNodeIdsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogNodeIdsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogNodeIdsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    node: (f = msg.getNode()) && dlkit_proto_hierarchy_pb.Node.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogNodeIdsReply}
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogNodeIdsReply;
  return proto.dlkit.proto.logging.GetLogNodeIdsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogNodeIdsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogNodeIdsReply}
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_hierarchy_pb.Node;
      reader.readMessage(value,dlkit_proto_hierarchy_pb.Node.deserializeBinaryFromReader);
      msg.setNode(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogNodeIdsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogNodeIdsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getNode();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_hierarchy_pb.Node.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.hierarchy.Node node = 1;
 * @return {?proto.dlkit.proto.hierarchy.Node}
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.prototype.getNode = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Node} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Node, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Node|undefined} value */
proto.dlkit.proto.logging.GetLogNodeIdsReply.prototype.setNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogNodeIdsReply.prototype.clearNode = function() {
  this.setNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogNodeIdsReply.prototype.hasNode = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogNodeIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogNodeIdsRequest.displayName = 'proto.dlkit.proto.logging.GetLogNodeIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogNodeIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogNodeIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    descendantLevels: jspb.Message.getFieldWithDefault(msg, 2, 0),
    includeSiblings: jspb.Message.getFieldWithDefault(msg, 3, false),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogNodeIdsRequest}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogNodeIdsRequest;
  return proto.dlkit.proto.logging.GetLogNodeIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogNodeIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogNodeIdsRequest}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setAncestorLevels(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setDescendantLevels(value);
      break;
    case 3:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIncludeSiblings(value);
      break;
    case 4:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogNodeIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogNodeIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAncestorLevels();
  if (f !== 0) {
    writer.writeSint32(
      1,
      f
    );
  }
  f = message.getDescendantLevels();
  if (f !== 0) {
    writer.writeSint32(
      2,
      f
    );
  }
  f = message.getIncludeSiblings();
  if (f) {
    writer.writeBool(
      3,
      f
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional sint32 ancestor_levels = 1;
 * @return {number}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional sint32 descendant_levels = 2;
 * @return {number}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional bool include_siblings = 3;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 3, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.setIncludeSiblings = function(value) {
  jspb.Message.setProto3BooleanField(this, 3, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogNodeIdsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 4) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogNodesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogNodesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogNodesReply.displayName = 'proto.dlkit.proto.logging.GetLogNodesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogNodesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogNodesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogNodesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    logNode: (f = msg.getLogNode()) && proto.dlkit.proto.logging.LogNode.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogNodesReply}
 */
proto.dlkit.proto.logging.GetLogNodesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogNodesReply;
  return proto.dlkit.proto.logging.GetLogNodesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogNodesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogNodesReply}
 */
proto.dlkit.proto.logging.GetLogNodesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.logging.LogNode;
      reader.readMessage(value,proto.dlkit.proto.logging.LogNode.deserializeBinaryFromReader);
      msg.setLogNode(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogNodesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogNodesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogNodesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogNode();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.logging.LogNode.serializeBinaryToWriter
    );
  }
};


/**
 * optional LogNode log_node = 1;
 * @return {?proto.dlkit.proto.logging.LogNode}
 */
proto.dlkit.proto.logging.GetLogNodesReply.prototype.getLogNode = function() {
  return /** @type{?proto.dlkit.proto.logging.LogNode} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.logging.LogNode, 1));
};


/** @param {?proto.dlkit.proto.logging.LogNode|undefined} value */
proto.dlkit.proto.logging.GetLogNodesReply.prototype.setLogNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.GetLogNodesReply.prototype.clearLogNode = function() {
  this.setLogNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogNodesReply.prototype.hasLogNode = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.GetLogNodesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.GetLogNodesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.GetLogNodesRequest.displayName = 'proto.dlkit.proto.logging.GetLogNodesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.GetLogNodesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.GetLogNodesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    descendantLevels: jspb.Message.getFieldWithDefault(msg, 2, 0),
    includeSiblings: jspb.Message.getFieldWithDefault(msg, 3, false),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.GetLogNodesRequest}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.GetLogNodesRequest;
  return proto.dlkit.proto.logging.GetLogNodesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.GetLogNodesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.GetLogNodesRequest}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setAncestorLevels(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setDescendantLevels(value);
      break;
    case 3:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIncludeSiblings(value);
      break;
    case 4:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.GetLogNodesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.GetLogNodesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.GetLogNodesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAncestorLevels();
  if (f !== 0) {
    writer.writeSint32(
      1,
      f
    );
  }
  f = message.getDescendantLevels();
  if (f !== 0) {
    writer.writeSint32(
      2,
      f
    );
  }
  f = message.getIncludeSiblings();
  if (f) {
    writer.writeBool(
      3,
      f
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional sint32 ancestor_levels = 1;
 * @return {number}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional sint32 descendant_levels = 2;
 * @return {number}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional bool include_siblings = 3;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 3, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.setIncludeSiblings = function(value) {
  jspb.Message.setProto3BooleanField(this, 3, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.logging.GetLogNodesRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.GetLogNodesRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 4) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanModifyLogHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanModifyLogHierarchyReply.displayName = 'proto.dlkit.proto.logging.CanModifyLogHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanModifyLogHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanModifyLogHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canModifyLogHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanModifyLogHierarchyReply}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanModifyLogHierarchyReply;
  return proto.dlkit.proto.logging.CanModifyLogHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanModifyLogHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanModifyLogHierarchyReply}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanModifyLogHierarchy(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanModifyLogHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanModifyLogHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanModifyLogHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_modify_log_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.prototype.getCanModifyLogHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.logging.CanModifyLogHierarchyReply.prototype.setCanModifyLogHierarchy = function(value) {
  jspb.Message.setProto3BooleanField(this, 1, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.CanModifyLogHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.displayName = 'proto.dlkit.proto.logging.CanModifyLogHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.CanModifyLogHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.CanModifyLogHierarchyRequest}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.CanModifyLogHierarchyRequest;
  return proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.CanModifyLogHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.CanModifyLogHierarchyRequest}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.CanModifyLogHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.CanModifyLogHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AddRootLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AddRootLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AddRootLogReply.displayName = 'proto.dlkit.proto.logging.AddRootLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AddRootLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AddRootLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AddRootLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddRootLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AddRootLogReply}
 */
proto.dlkit.proto.logging.AddRootLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AddRootLogReply;
  return proto.dlkit.proto.logging.AddRootLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AddRootLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AddRootLogReply}
 */
proto.dlkit.proto.logging.AddRootLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AddRootLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AddRootLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AddRootLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddRootLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AddRootLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AddRootLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AddRootLogRequest.displayName = 'proto.dlkit.proto.logging.AddRootLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AddRootLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AddRootLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AddRootLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddRootLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AddRootLogRequest}
 */
proto.dlkit.proto.logging.AddRootLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AddRootLogRequest;
  return proto.dlkit.proto.logging.AddRootLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AddRootLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AddRootLogRequest}
 */
proto.dlkit.proto.logging.AddRootLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AddRootLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AddRootLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AddRootLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddRootLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AddRootLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AddRootLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.AddRootLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AddRootLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.RemoveRootLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.RemoveRootLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.RemoveRootLogReply.displayName = 'proto.dlkit.proto.logging.RemoveRootLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.RemoveRootLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.RemoveRootLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.RemoveRootLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveRootLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.RemoveRootLogReply}
 */
proto.dlkit.proto.logging.RemoveRootLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.RemoveRootLogReply;
  return proto.dlkit.proto.logging.RemoveRootLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.RemoveRootLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.RemoveRootLogReply}
 */
proto.dlkit.proto.logging.RemoveRootLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.RemoveRootLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.RemoveRootLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.RemoveRootLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveRootLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.RemoveRootLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.RemoveRootLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.RemoveRootLogRequest.displayName = 'proto.dlkit.proto.logging.RemoveRootLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.RemoveRootLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.RemoveRootLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.RemoveRootLogRequest}
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.RemoveRootLogRequest;
  return proto.dlkit.proto.logging.RemoveRootLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.RemoveRootLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.RemoveRootLogRequest}
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.RemoveRootLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.RemoveRootLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.RemoveRootLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.RemoveRootLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.RemoveRootLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AddChildLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AddChildLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AddChildLogReply.displayName = 'proto.dlkit.proto.logging.AddChildLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AddChildLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AddChildLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AddChildLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddChildLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AddChildLogReply}
 */
proto.dlkit.proto.logging.AddChildLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AddChildLogReply;
  return proto.dlkit.proto.logging.AddChildLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AddChildLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AddChildLogReply}
 */
proto.dlkit.proto.logging.AddChildLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AddChildLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AddChildLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AddChildLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddChildLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.AddChildLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.AddChildLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.AddChildLogRequest.displayName = 'proto.dlkit.proto.logging.AddChildLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.AddChildLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.AddChildLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddChildLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    childId: (f = msg.getChildId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.AddChildLogRequest}
 */
proto.dlkit.proto.logging.AddChildLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.AddChildLogRequest;
  return proto.dlkit.proto.logging.AddChildLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.AddChildLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.AddChildLogRequest}
 */
proto.dlkit.proto.logging.AddChildLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setChildId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.AddChildLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.AddChildLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.AddChildLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getChildId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id child_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.AddChildLogRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.hasChildId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.AddChildLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.AddChildLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.RemoveChildLogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.RemoveChildLogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.RemoveChildLogReply.displayName = 'proto.dlkit.proto.logging.RemoveChildLogReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.RemoveChildLogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.RemoveChildLogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.RemoveChildLogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogReply}
 */
proto.dlkit.proto.logging.RemoveChildLogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.RemoveChildLogReply;
  return proto.dlkit.proto.logging.RemoveChildLogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogReply}
 */
proto.dlkit.proto.logging.RemoveChildLogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.RemoveChildLogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.RemoveChildLogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.RemoveChildLogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.RemoveChildLogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.RemoveChildLogRequest.displayName = 'proto.dlkit.proto.logging.RemoveChildLogRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.RemoveChildLogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.RemoveChildLogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    childId: (f = msg.getChildId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogRequest}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.RemoveChildLogRequest;
  return proto.dlkit.proto.logging.RemoveChildLogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogRequest}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setChildId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.RemoveChildLogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getChildId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id child_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.hasChildId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.RemoveChildLogRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.RemoveChildLogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.RemoveChildLogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.RemoveChildLogsReply.displayName = 'proto.dlkit.proto.logging.RemoveChildLogsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.RemoveChildLogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.RemoveChildLogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.RemoveChildLogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogsReply}
 */
proto.dlkit.proto.logging.RemoveChildLogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.RemoveChildLogsReply;
  return proto.dlkit.proto.logging.RemoveChildLogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogsReply}
 */
proto.dlkit.proto.logging.RemoveChildLogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.RemoveChildLogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.RemoveChildLogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.logging.RemoveChildLogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.logging.RemoveChildLogsRequest.displayName = 'proto.dlkit.proto.logging.RemoveChildLogsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.logging.RemoveChildLogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.logging.RemoveChildLogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    logId: (f = msg.getLogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogsRequest}
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.logging.RemoveChildLogsRequest;
  return proto.dlkit.proto.logging.RemoveChildLogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.logging.RemoveChildLogsRequest}
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLogId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.logging.RemoveChildLogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.logging.RemoveChildLogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id log_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.prototype.getLogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.logging.RemoveChildLogsRequest.prototype.setLogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.logging.RemoveChildLogsRequest.prototype.clearLogId = function() {
  this.setLogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.logging.RemoveChildLogsRequest.prototype.hasLogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


goog.object.extend(exports, proto.dlkit.proto.logging);
