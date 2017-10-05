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

var dlkit_primordium_calendaring_primitives_pb = require('../../dlkit/primordium/calendaring/primitives_pb.js');
var dlkit_primordium_id_primitives_pb = require('../../dlkit/primordium/id/primitives_pb.js');
var dlkit_primordium_locale_primitives_pb = require('../../dlkit/primordium/locale/primitives_pb.js');
var dlkit_primordium_type_primitives_pb = require('../../dlkit/primordium/type/primitives_pb.js');
var dlkit_proto_osid_pb = require('../../dlkit/proto/osid_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
goog.exportSymbol('proto.dlkit.proto.calendaring.Calendar', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarNode', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarNodeList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CalendarSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.Commitment', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.CommitmentSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.DateTimeInterval', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.DateTimeIntervalList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.DateTimeList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.DurationList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.Event', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.EventSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.MeetingTime', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.MeetingTimeList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEvent', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.OffsetEventSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEvent', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.RecurringEventSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.Schedule', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlot', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.ScheduleSlotSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEvent', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.SupersedingEventSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimeList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriod', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodForm', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodList', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.calendaring.TimePeriodSearchResults', null, global);

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
proto.dlkit.proto.calendaring.Event = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.Event.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.Event, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.Event.displayName = 'proto.dlkit.proto.calendaring.Event';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.Event.repeatedFields_ = [8,9];



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
proto.dlkit.proto.calendaring.Event.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.Event.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.Event} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Event.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    location: (f = msg.getLocation()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    locationDescription: jspb.Message.getFieldWithDefault(msg, 7, ""),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    sponsorsList: jspb.Message.toObjectList(msg.getSponsorsList(),
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
 * @return {!proto.dlkit.proto.calendaring.Event}
 */
proto.dlkit.proto.calendaring.Event.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.Event;
  return proto.dlkit.proto.calendaring.Event.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.Event} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.Event}
 */
proto.dlkit.proto.calendaring.Event.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
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
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLocation(value);
      break;
    case 7:
      var value = /** @type {string} */ (reader.readString());
      msg.setLocationDescription(value);
      break;
    case 8:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 9:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addSponsors(value);
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
proto.dlkit.proto.calendaring.Event.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.Event.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.Event} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Event.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
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
  f = message.getLocation();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLocationDescription();
  if (f.length > 0) {
    writer.writeString(
      7,
      f
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
  f = message.getSponsorsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      9,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.Event.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.Event.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.Event.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Event.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.Event.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.Event.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.Event.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Event.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 3;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.Event.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 3));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.Event.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.Event.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Event.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 4;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.Event.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 4));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.calendaring.Event.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.calendaring.Event.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Event.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 5;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Event.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 5));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Event.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.calendaring.Event.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Event.prototype.hasId = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id location = 6;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Event.prototype.getLocation = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 6));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Event.prototype.setLocation = function(value) {
  jspb.Message.setWrapperField(this, 6, value);
};


proto.dlkit.proto.calendaring.Event.prototype.clearLocation = function() {
  this.setLocation(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Event.prototype.hasLocation = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * optional string location_description = 7;
 * @return {string}
 */
proto.dlkit.proto.calendaring.Event.prototype.getLocationDescription = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 7, ""));
};


/** @param {string} value */
proto.dlkit.proto.calendaring.Event.prototype.setLocationDescription = function(value) {
  jspb.Message.setProto3StringField(this, 7, value);
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 8;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.calendaring.Event.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 8));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.calendaring.Event.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 8, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.Event.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 8, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.calendaring.Event.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * repeated dlkit.primordium.id.primitives.Id sponsors = 9;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.calendaring.Event.prototype.getSponsorsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 9));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.calendaring.Event.prototype.setSponsorsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 9, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Event.prototype.addSponsors = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 9, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.calendaring.Event.prototype.clearSponsorsList = function() {
  this.setSponsorsList([]);
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
proto.dlkit.proto.calendaring.EventQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventQuery.displayName = 'proto.dlkit.proto.calendaring.EventQuery';
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
proto.dlkit.proto.calendaring.EventQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.EventQuery}
 */
proto.dlkit.proto.calendaring.EventQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventQuery;
  return proto.dlkit.proto.calendaring.EventQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventQuery}
 */
proto.dlkit.proto.calendaring.EventQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.EventQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.EventQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventQueryInspector.displayName = 'proto.dlkit.proto.calendaring.EventQueryInspector';
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
proto.dlkit.proto.calendaring.EventQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.EventQueryInspector}
 */
proto.dlkit.proto.calendaring.EventQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventQueryInspector;
  return proto.dlkit.proto.calendaring.EventQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventQueryInspector}
 */
proto.dlkit.proto.calendaring.EventQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.EventQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.EventForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventForm.displayName = 'proto.dlkit.proto.calendaring.EventForm';
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
proto.dlkit.proto.calendaring.EventForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.EventForm}
 */
proto.dlkit.proto.calendaring.EventForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventForm;
  return proto.dlkit.proto.calendaring.EventForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventForm}
 */
proto.dlkit.proto.calendaring.EventForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.EventForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.EventSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventSearchOrder.displayName = 'proto.dlkit.proto.calendaring.EventSearchOrder';
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
proto.dlkit.proto.calendaring.EventSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.EventSearchOrder}
 */
proto.dlkit.proto.calendaring.EventSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventSearchOrder;
  return proto.dlkit.proto.calendaring.EventSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventSearchOrder}
 */
proto.dlkit.proto.calendaring.EventSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.EventSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.EventSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventSearch.displayName = 'proto.dlkit.proto.calendaring.EventSearch';
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
proto.dlkit.proto.calendaring.EventSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.EventSearch}
 */
proto.dlkit.proto.calendaring.EventSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventSearch;
  return proto.dlkit.proto.calendaring.EventSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventSearch}
 */
proto.dlkit.proto.calendaring.EventSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.EventSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.EventSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventSearchResults.displayName = 'proto.dlkit.proto.calendaring.EventSearchResults';
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
proto.dlkit.proto.calendaring.EventSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.EventSearchResults}
 */
proto.dlkit.proto.calendaring.EventSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventSearchResults;
  return proto.dlkit.proto.calendaring.EventSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventSearchResults}
 */
proto.dlkit.proto.calendaring.EventSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.EventSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.EventList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.EventList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.EventList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.EventList.displayName = 'proto.dlkit.proto.calendaring.EventList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.EventList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.EventList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.EventList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.EventList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventList.toObject = function(includeInstance, msg) {
  var f, obj = {
    eventsList: jspb.Message.toObjectList(msg.getEventsList(),
    proto.dlkit.proto.calendaring.Event.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.EventList}
 */
proto.dlkit.proto.calendaring.EventList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.EventList;
  return proto.dlkit.proto.calendaring.EventList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.EventList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.EventList}
 */
proto.dlkit.proto.calendaring.EventList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.Event;
      reader.readMessage(value,proto.dlkit.proto.calendaring.Event.deserializeBinaryFromReader);
      msg.addEvents(value);
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
proto.dlkit.proto.calendaring.EventList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.EventList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.EventList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.EventList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEventsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.Event.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Event events = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.Event>}
 */
proto.dlkit.proto.calendaring.EventList.prototype.getEventsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.Event>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.Event, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.Event>} value */
proto.dlkit.proto.calendaring.EventList.prototype.setEventsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.Event=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.Event}
 */
proto.dlkit.proto.calendaring.EventList.prototype.addEvents = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.Event, opt_index);
};


proto.dlkit.proto.calendaring.EventList.prototype.clearEventsList = function() {
  this.setEventsList([]);
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
proto.dlkit.proto.calendaring.RecurringEvent = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.RecurringEvent.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEvent, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEvent.displayName = 'proto.dlkit.proto.calendaring.RecurringEvent';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.RecurringEvent.repeatedFields_ = [2];



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
proto.dlkit.proto.calendaring.RecurringEvent.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEvent.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEvent} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEvent.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    sponsorsList: jspb.Message.toObjectList(msg.getSponsorsList(),
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEvent}
 */
proto.dlkit.proto.calendaring.RecurringEvent.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEvent;
  return proto.dlkit.proto.calendaring.RecurringEvent.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEvent} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEvent}
 */
proto.dlkit.proto.calendaring.RecurringEvent.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addSponsors(value);
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
proto.dlkit.proto.calendaring.RecurringEvent.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEvent.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEvent} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEvent.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getSponsorsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.RecurringEvent.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.RecurringEvent.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.RecurringEvent.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.RecurringEvent.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * repeated dlkit.primordium.id.primitives.Id sponsors = 2;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.calendaring.RecurringEvent.prototype.getSponsorsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.calendaring.RecurringEvent.prototype.setSponsorsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 2, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.RecurringEvent.prototype.addSponsors = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 2, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.calendaring.RecurringEvent.prototype.clearSponsorsList = function() {
  this.setSponsorsList([]);
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
proto.dlkit.proto.calendaring.RecurringEventQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventQuery.displayName = 'proto.dlkit.proto.calendaring.RecurringEventQuery';
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
proto.dlkit.proto.calendaring.RecurringEventQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventQuery}
 */
proto.dlkit.proto.calendaring.RecurringEventQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventQuery;
  return proto.dlkit.proto.calendaring.RecurringEventQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventQuery}
 */
proto.dlkit.proto.calendaring.RecurringEventQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.RecurringEventQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.RecurringEventQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventQueryInspector.displayName = 'proto.dlkit.proto.calendaring.RecurringEventQueryInspector';
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
proto.dlkit.proto.calendaring.RecurringEventQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventQueryInspector}
 */
proto.dlkit.proto.calendaring.RecurringEventQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventQueryInspector;
  return proto.dlkit.proto.calendaring.RecurringEventQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventQueryInspector}
 */
proto.dlkit.proto.calendaring.RecurringEventQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.RecurringEventQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.RecurringEventForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventForm.displayName = 'proto.dlkit.proto.calendaring.RecurringEventForm';
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
proto.dlkit.proto.calendaring.RecurringEventForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventForm}
 */
proto.dlkit.proto.calendaring.RecurringEventForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventForm;
  return proto.dlkit.proto.calendaring.RecurringEventForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventForm}
 */
proto.dlkit.proto.calendaring.RecurringEventForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.RecurringEventForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.RecurringEventSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventSearchOrder.displayName = 'proto.dlkit.proto.calendaring.RecurringEventSearchOrder';
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
proto.dlkit.proto.calendaring.RecurringEventSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventSearchOrder}
 */
proto.dlkit.proto.calendaring.RecurringEventSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventSearchOrder;
  return proto.dlkit.proto.calendaring.RecurringEventSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventSearchOrder}
 */
proto.dlkit.proto.calendaring.RecurringEventSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.RecurringEventSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.RecurringEventSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventSearch.displayName = 'proto.dlkit.proto.calendaring.RecurringEventSearch';
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
proto.dlkit.proto.calendaring.RecurringEventSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventSearch}
 */
proto.dlkit.proto.calendaring.RecurringEventSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventSearch;
  return proto.dlkit.proto.calendaring.RecurringEventSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventSearch}
 */
proto.dlkit.proto.calendaring.RecurringEventSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.RecurringEventSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.RecurringEventSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventSearchResults.displayName = 'proto.dlkit.proto.calendaring.RecurringEventSearchResults';
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
proto.dlkit.proto.calendaring.RecurringEventSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventSearchResults}
 */
proto.dlkit.proto.calendaring.RecurringEventSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventSearchResults;
  return proto.dlkit.proto.calendaring.RecurringEventSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventSearchResults}
 */
proto.dlkit.proto.calendaring.RecurringEventSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.RecurringEventSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.RecurringEventList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.RecurringEventList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.RecurringEventList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.RecurringEventList.displayName = 'proto.dlkit.proto.calendaring.RecurringEventList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.RecurringEventList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.RecurringEventList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.RecurringEventList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.RecurringEventList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventList.toObject = function(includeInstance, msg) {
  var f, obj = {
    recurringEventsList: jspb.Message.toObjectList(msg.getRecurringEventsList(),
    proto.dlkit.proto.calendaring.RecurringEvent.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.RecurringEventList}
 */
proto.dlkit.proto.calendaring.RecurringEventList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.RecurringEventList;
  return proto.dlkit.proto.calendaring.RecurringEventList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.RecurringEventList}
 */
proto.dlkit.proto.calendaring.RecurringEventList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.RecurringEvent;
      reader.readMessage(value,proto.dlkit.proto.calendaring.RecurringEvent.deserializeBinaryFromReader);
      msg.addRecurringEvents(value);
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
proto.dlkit.proto.calendaring.RecurringEventList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.RecurringEventList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.RecurringEventList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.RecurringEventList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRecurringEventsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.RecurringEvent.serializeBinaryToWriter
    );
  }
};


/**
 * repeated RecurringEvent recurring_events = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.RecurringEvent>}
 */
proto.dlkit.proto.calendaring.RecurringEventList.prototype.getRecurringEventsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.RecurringEvent>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.RecurringEvent, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.RecurringEvent>} value */
proto.dlkit.proto.calendaring.RecurringEventList.prototype.setRecurringEventsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.RecurringEvent=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.RecurringEvent}
 */
proto.dlkit.proto.calendaring.RecurringEventList.prototype.addRecurringEvents = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.RecurringEvent, opt_index);
};


proto.dlkit.proto.calendaring.RecurringEventList.prototype.clearRecurringEventsList = function() {
  this.setRecurringEventsList([]);
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
proto.dlkit.proto.calendaring.SupersedingEvent = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEvent, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEvent.displayName = 'proto.dlkit.proto.calendaring.SupersedingEvent';
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
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEvent.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEvent} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEvent.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    supersededDate: (f = msg.getSupersededDate()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    supersededEvent: (f = msg.getSupersededEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    supersededEventPosition: jspb.Message.getFieldWithDefault(msg, 4, 0),
    supersedingEvent: (f = msg.getSupersedingEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEvent}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEvent;
  return proto.dlkit.proto.calendaring.SupersedingEvent.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEvent} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEvent}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setSupersededDate(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSupersededEvent(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setSupersededEventPosition(value);
      break;
    case 5:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSupersedingEvent(value);
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
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEvent.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEvent} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEvent.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getSupersededDate();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getSupersededEvent();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getSupersededEventPosition();
  if (f !== 0) {
    writer.writeSint32(
      4,
      f
    );
  }
  f = message.getSupersedingEvent();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.SupersedingEvent.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp superseded_date = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.getSupersededDate = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.setSupersededDate = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.SupersedingEvent.prototype.clearSupersededDate = function() {
  this.setSupersededDate(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.hasSupersededDate = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id superseded_event = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.getSupersededEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.setSupersededEvent = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.SupersedingEvent.prototype.clearSupersededEvent = function() {
  this.setSupersededEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.hasSupersededEvent = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional sint32 superseded_event_position = 4;
 * @return {number}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.getSupersededEventPosition = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 4, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.setSupersededEventPosition = function(value) {
  jspb.Message.setProto3IntField(this, 4, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id superseding_event = 5;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.getSupersedingEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 5));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.setSupersedingEvent = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.calendaring.SupersedingEvent.prototype.clearSupersedingEvent = function() {
  this.setSupersedingEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.SupersedingEvent.prototype.hasSupersedingEvent = function() {
  return jspb.Message.getField(this, 5) != null;
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
proto.dlkit.proto.calendaring.SupersedingEventQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventQuery.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventQuery';
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
proto.dlkit.proto.calendaring.SupersedingEventQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventQuery}
 */
proto.dlkit.proto.calendaring.SupersedingEventQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventQuery;
  return proto.dlkit.proto.calendaring.SupersedingEventQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventQuery}
 */
proto.dlkit.proto.calendaring.SupersedingEventQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.SupersedingEventQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventQueryInspector';
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
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventQueryInspector}
 */
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventQueryInspector;
  return proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventQueryInspector}
 */
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.SupersedingEventForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventForm.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventForm';
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
proto.dlkit.proto.calendaring.SupersedingEventForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventForm}
 */
proto.dlkit.proto.calendaring.SupersedingEventForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventForm;
  return proto.dlkit.proto.calendaring.SupersedingEventForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventForm}
 */
proto.dlkit.proto.calendaring.SupersedingEventForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.SupersedingEventForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventSearchOrder';
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
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventSearchOrder}
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventSearchOrder;
  return proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventSearchOrder}
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.SupersedingEventSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventSearch.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventSearch';
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
proto.dlkit.proto.calendaring.SupersedingEventSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventSearch}
 */
proto.dlkit.proto.calendaring.SupersedingEventSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventSearch;
  return proto.dlkit.proto.calendaring.SupersedingEventSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventSearch}
 */
proto.dlkit.proto.calendaring.SupersedingEventSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.SupersedingEventSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.SupersedingEventSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventSearchResults.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventSearchResults';
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
proto.dlkit.proto.calendaring.SupersedingEventSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventSearchResults}
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventSearchResults;
  return proto.dlkit.proto.calendaring.SupersedingEventSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventSearchResults}
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.SupersedingEventSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.SupersedingEventList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.SupersedingEventList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.SupersedingEventList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.SupersedingEventList.displayName = 'proto.dlkit.proto.calendaring.SupersedingEventList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.SupersedingEventList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.SupersedingEventList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.SupersedingEventList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventList.toObject = function(includeInstance, msg) {
  var f, obj = {
    supersedingEventsList: jspb.Message.toObjectList(msg.getSupersedingEventsList(),
    proto.dlkit.proto.calendaring.SupersedingEvent.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventList}
 */
proto.dlkit.proto.calendaring.SupersedingEventList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.SupersedingEventList;
  return proto.dlkit.proto.calendaring.SupersedingEventList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.SupersedingEventList}
 */
proto.dlkit.proto.calendaring.SupersedingEventList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.SupersedingEvent;
      reader.readMessage(value,proto.dlkit.proto.calendaring.SupersedingEvent.deserializeBinaryFromReader);
      msg.addSupersedingEvents(value);
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
proto.dlkit.proto.calendaring.SupersedingEventList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.SupersedingEventList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.SupersedingEventList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.SupersedingEventList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSupersedingEventsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.SupersedingEvent.serializeBinaryToWriter
    );
  }
};


/**
 * repeated SupersedingEvent superseding_events = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.SupersedingEvent>}
 */
proto.dlkit.proto.calendaring.SupersedingEventList.prototype.getSupersedingEventsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.SupersedingEvent>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.SupersedingEvent, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.SupersedingEvent>} value */
proto.dlkit.proto.calendaring.SupersedingEventList.prototype.setSupersedingEventsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.SupersedingEvent=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.SupersedingEvent}
 */
proto.dlkit.proto.calendaring.SupersedingEventList.prototype.addSupersedingEvents = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.SupersedingEvent, opt_index);
};


proto.dlkit.proto.calendaring.SupersedingEventList.prototype.clearSupersedingEventsList = function() {
  this.setSupersedingEventsList([]);
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
proto.dlkit.proto.calendaring.OffsetEvent = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.OffsetEvent.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEvent, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEvent.displayName = 'proto.dlkit.proto.calendaring.OffsetEvent';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.OffsetEvent.repeatedFields_ = [13];



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
proto.dlkit.proto.calendaring.OffsetEvent.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEvent.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEvent} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEvent.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    endReferenceEvent: (f = msg.getEndReferenceEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    fixedDuration: (f = msg.getFixedDuration()) && dlkit_primordium_calendaring_primitives_pb.Duration.toObject(includeInstance, f),
    fixedEndOffset: (f = msg.getFixedEndOffset()) && dlkit_primordium_calendaring_primitives_pb.Duration.toObject(includeInstance, f),
    fixedStartOffset: (f = msg.getFixedStartOffset()) && dlkit_primordium_calendaring_primitives_pb.Duration.toObject(includeInstance, f),
    fixedStartTime: (f = msg.getFixedStartTime()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    location: (f = msg.getLocation()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    locationDescription: jspb.Message.getFieldWithDefault(msg, 8, ""),
    relativeEndWeekday: jspb.Message.getFieldWithDefault(msg, 9, 0),
    relativeStartWeekday: jspb.Message.getFieldWithDefault(msg, 10, 0),
    relativeWeekdayEndOffset: jspb.Message.getFieldWithDefault(msg, 11, 0),
    relativeWeekdayStartOffset: jspb.Message.getFieldWithDefault(msg, 12, 0),
    sponsorsList: jspb.Message.toObjectList(msg.getSponsorsList(),
    dlkit_primordium_id_primitives_pb.Id.toObject, includeInstance),
    startReferenceEvent: (f = msg.getStartReferenceEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEvent}
 */
proto.dlkit.proto.calendaring.OffsetEvent.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEvent;
  return proto.dlkit.proto.calendaring.OffsetEvent.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEvent} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEvent}
 */
proto.dlkit.proto.calendaring.OffsetEvent.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setEndReferenceEvent(value);
      break;
    case 3:
      var value = new dlkit_primordium_calendaring_primitives_pb.Duration;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Duration.deserializeBinaryFromReader);
      msg.setFixedDuration(value);
      break;
    case 4:
      var value = new dlkit_primordium_calendaring_primitives_pb.Duration;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Duration.deserializeBinaryFromReader);
      msg.setFixedEndOffset(value);
      break;
    case 5:
      var value = new dlkit_primordium_calendaring_primitives_pb.Duration;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Duration.deserializeBinaryFromReader);
      msg.setFixedStartOffset(value);
      break;
    case 6:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFixedStartTime(value);
      break;
    case 7:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLocation(value);
      break;
    case 8:
      var value = /** @type {string} */ (reader.readString());
      msg.setLocationDescription(value);
      break;
    case 9:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setRelativeEndWeekday(value);
      break;
    case 10:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setRelativeStartWeekday(value);
      break;
    case 11:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setRelativeWeekdayEndOffset(value);
      break;
    case 12:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setRelativeWeekdayStartOffset(value);
      break;
    case 13:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addSponsors(value);
      break;
    case 14:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setStartReferenceEvent(value);
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
proto.dlkit.proto.calendaring.OffsetEvent.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEvent.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEvent} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEvent.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getEndReferenceEvent();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFixedDuration();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_calendaring_primitives_pb.Duration.serializeBinaryToWriter
    );
  }
  f = message.getFixedEndOffset();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_calendaring_primitives_pb.Duration.serializeBinaryToWriter
    );
  }
  f = message.getFixedStartOffset();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      dlkit_primordium_calendaring_primitives_pb.Duration.serializeBinaryToWriter
    );
  }
  f = message.getFixedStartTime();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getLocation();
  if (f != null) {
    writer.writeMessage(
      7,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLocationDescription();
  if (f.length > 0) {
    writer.writeString(
      8,
      f
    );
  }
  f = message.getRelativeEndWeekday();
  if (f !== 0) {
    writer.writeSint32(
      9,
      f
    );
  }
  f = message.getRelativeStartWeekday();
  if (f !== 0) {
    writer.writeSint32(
      10,
      f
    );
  }
  f = message.getRelativeWeekdayEndOffset();
  if (f !== 0) {
    writer.writeSint32(
      11,
      f
    );
  }
  f = message.getRelativeWeekdayStartOffset();
  if (f !== 0) {
    writer.writeSint32(
      12,
      f
    );
  }
  f = message.getSponsorsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      13,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getStartReferenceEvent();
  if (f != null) {
    writer.writeMessage(
      14,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id end_reference_event = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getEndReferenceEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setEndReferenceEvent = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearEndReferenceEvent = function() {
  this.setEndReferenceEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasEndReferenceEvent = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.calendaring.primitives.Duration fixed_duration = 3;
 * @return {?proto.dlkit.primordium.calendaring.primitives.Duration}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getFixedDuration = function() {
  return /** @type{?proto.dlkit.primordium.calendaring.primitives.Duration} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Duration, 3));
};


/** @param {?proto.dlkit.primordium.calendaring.primitives.Duration|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setFixedDuration = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearFixedDuration = function() {
  this.setFixedDuration(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasFixedDuration = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.calendaring.primitives.Duration fixed_end_offset = 4;
 * @return {?proto.dlkit.primordium.calendaring.primitives.Duration}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getFixedEndOffset = function() {
  return /** @type{?proto.dlkit.primordium.calendaring.primitives.Duration} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Duration, 4));
};


/** @param {?proto.dlkit.primordium.calendaring.primitives.Duration|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setFixedEndOffset = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearFixedEndOffset = function() {
  this.setFixedEndOffset(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasFixedEndOffset = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.calendaring.primitives.Duration fixed_start_offset = 5;
 * @return {?proto.dlkit.primordium.calendaring.primitives.Duration}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getFixedStartOffset = function() {
  return /** @type{?proto.dlkit.primordium.calendaring.primitives.Duration} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Duration, 5));
};


/** @param {?proto.dlkit.primordium.calendaring.primitives.Duration|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setFixedStartOffset = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearFixedStartOffset = function() {
  this.setFixedStartOffset(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasFixedStartOffset = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional google.protobuf.Timestamp fixed_start_time = 6;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getFixedStartTime = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 6));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setFixedStartTime = function(value) {
  jspb.Message.setWrapperField(this, 6, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearFixedStartTime = function() {
  this.setFixedStartTime(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasFixedStartTime = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id location = 7;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getLocation = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 7));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setLocation = function(value) {
  jspb.Message.setWrapperField(this, 7, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearLocation = function() {
  this.setLocation(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasLocation = function() {
  return jspb.Message.getField(this, 7) != null;
};


/**
 * optional string location_description = 8;
 * @return {string}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getLocationDescription = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 8, ""));
};


/** @param {string} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setLocationDescription = function(value) {
  jspb.Message.setProto3StringField(this, 8, value);
};


/**
 * optional sint32 relative_end_weekday = 9;
 * @return {number}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getRelativeEndWeekday = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 9, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setRelativeEndWeekday = function(value) {
  jspb.Message.setProto3IntField(this, 9, value);
};


/**
 * optional sint32 relative_start_weekday = 10;
 * @return {number}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getRelativeStartWeekday = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 10, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setRelativeStartWeekday = function(value) {
  jspb.Message.setProto3IntField(this, 10, value);
};


/**
 * optional sint32 relative_weekday_end_offset = 11;
 * @return {number}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getRelativeWeekdayEndOffset = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 11, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setRelativeWeekdayEndOffset = function(value) {
  jspb.Message.setProto3IntField(this, 11, value);
};


/**
 * optional sint32 relative_weekday_start_offset = 12;
 * @return {number}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getRelativeWeekdayStartOffset = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 12, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setRelativeWeekdayStartOffset = function(value) {
  jspb.Message.setProto3IntField(this, 12, value);
};


/**
 * repeated dlkit.primordium.id.primitives.Id sponsors = 13;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getSponsorsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 13));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setSponsorsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 13, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.addSponsors = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 13, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearSponsorsList = function() {
  this.setSponsorsList([]);
};


/**
 * optional dlkit.primordium.id.primitives.Id start_reference_event = 14;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.getStartReferenceEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 14));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.setStartReferenceEvent = function(value) {
  jspb.Message.setWrapperField(this, 14, value);
};


proto.dlkit.proto.calendaring.OffsetEvent.prototype.clearStartReferenceEvent = function() {
  this.setStartReferenceEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.OffsetEvent.prototype.hasStartReferenceEvent = function() {
  return jspb.Message.getField(this, 14) != null;
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
proto.dlkit.proto.calendaring.OffsetEventQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventQuery.displayName = 'proto.dlkit.proto.calendaring.OffsetEventQuery';
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
proto.dlkit.proto.calendaring.OffsetEventQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventQuery}
 */
proto.dlkit.proto.calendaring.OffsetEventQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventQuery;
  return proto.dlkit.proto.calendaring.OffsetEventQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventQuery}
 */
proto.dlkit.proto.calendaring.OffsetEventQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.OffsetEventQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.OffsetEventQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventQueryInspector.displayName = 'proto.dlkit.proto.calendaring.OffsetEventQueryInspector';
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
proto.dlkit.proto.calendaring.OffsetEventQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventQueryInspector}
 */
proto.dlkit.proto.calendaring.OffsetEventQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventQueryInspector;
  return proto.dlkit.proto.calendaring.OffsetEventQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventQueryInspector}
 */
proto.dlkit.proto.calendaring.OffsetEventQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.OffsetEventQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.OffsetEventForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventForm.displayName = 'proto.dlkit.proto.calendaring.OffsetEventForm';
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
proto.dlkit.proto.calendaring.OffsetEventForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventForm}
 */
proto.dlkit.proto.calendaring.OffsetEventForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventForm;
  return proto.dlkit.proto.calendaring.OffsetEventForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventForm}
 */
proto.dlkit.proto.calendaring.OffsetEventForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.OffsetEventForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.OffsetEventSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventSearchOrder.displayName = 'proto.dlkit.proto.calendaring.OffsetEventSearchOrder';
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
proto.dlkit.proto.calendaring.OffsetEventSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventSearchOrder}
 */
proto.dlkit.proto.calendaring.OffsetEventSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventSearchOrder;
  return proto.dlkit.proto.calendaring.OffsetEventSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventSearchOrder}
 */
proto.dlkit.proto.calendaring.OffsetEventSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.OffsetEventSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.OffsetEventSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventSearch.displayName = 'proto.dlkit.proto.calendaring.OffsetEventSearch';
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
proto.dlkit.proto.calendaring.OffsetEventSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventSearch}
 */
proto.dlkit.proto.calendaring.OffsetEventSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventSearch;
  return proto.dlkit.proto.calendaring.OffsetEventSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventSearch}
 */
proto.dlkit.proto.calendaring.OffsetEventSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.OffsetEventSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.OffsetEventSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventSearchResults.displayName = 'proto.dlkit.proto.calendaring.OffsetEventSearchResults';
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
proto.dlkit.proto.calendaring.OffsetEventSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventSearchResults}
 */
proto.dlkit.proto.calendaring.OffsetEventSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventSearchResults;
  return proto.dlkit.proto.calendaring.OffsetEventSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventSearchResults}
 */
proto.dlkit.proto.calendaring.OffsetEventSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.OffsetEventSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.OffsetEventList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.OffsetEventList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.OffsetEventList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.OffsetEventList.displayName = 'proto.dlkit.proto.calendaring.OffsetEventList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.OffsetEventList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.OffsetEventList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.OffsetEventList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.OffsetEventList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventList.toObject = function(includeInstance, msg) {
  var f, obj = {
    offsetEventsList: jspb.Message.toObjectList(msg.getOffsetEventsList(),
    proto.dlkit.proto.calendaring.OffsetEvent.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.OffsetEventList}
 */
proto.dlkit.proto.calendaring.OffsetEventList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.OffsetEventList;
  return proto.dlkit.proto.calendaring.OffsetEventList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.OffsetEventList}
 */
proto.dlkit.proto.calendaring.OffsetEventList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.OffsetEvent;
      reader.readMessage(value,proto.dlkit.proto.calendaring.OffsetEvent.deserializeBinaryFromReader);
      msg.addOffsetEvents(value);
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
proto.dlkit.proto.calendaring.OffsetEventList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.OffsetEventList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.OffsetEventList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.OffsetEventList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getOffsetEventsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.OffsetEvent.serializeBinaryToWriter
    );
  }
};


/**
 * repeated OffsetEvent offset_events = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.OffsetEvent>}
 */
proto.dlkit.proto.calendaring.OffsetEventList.prototype.getOffsetEventsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.OffsetEvent>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.OffsetEvent, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.OffsetEvent>} value */
proto.dlkit.proto.calendaring.OffsetEventList.prototype.setOffsetEventsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.OffsetEvent=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.OffsetEvent}
 */
proto.dlkit.proto.calendaring.OffsetEventList.prototype.addOffsetEvents = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.OffsetEvent, opt_index);
};


proto.dlkit.proto.calendaring.OffsetEventList.prototype.clearOffsetEventsList = function() {
  this.setOffsetEventsList([]);
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
proto.dlkit.proto.calendaring.Schedule = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.Schedule.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.Schedule, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.Schedule.displayName = 'proto.dlkit.proto.calendaring.Schedule';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.Schedule.repeatedFields_ = [6,9];



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
proto.dlkit.proto.calendaring.Schedule.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.Schedule.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.Schedule} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Schedule.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    limitList: jspb.Message.getRepeatedField(msg, 6),
    location: (f = msg.getLocation()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    locationDescription: jspb.Message.getFieldWithDefault(msg, 8, ""),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    scheduleEnd: (f = msg.getScheduleEnd()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    scheduleSlot: (f = msg.getScheduleSlot()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    scheduleStart: (f = msg.getScheduleStart()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    timePeriod: (f = msg.getTimePeriod()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.calendaring.Schedule}
 */
proto.dlkit.proto.calendaring.Schedule.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.Schedule;
  return proto.dlkit.proto.calendaring.Schedule.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.Schedule} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.Schedule}
 */
proto.dlkit.proto.calendaring.Schedule.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
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
      var value = /** @type {!Array.<number>} */ (reader.readPackedSint32());
      msg.setLimitList(value);
      break;
    case 7:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setLocation(value);
      break;
    case 8:
      var value = /** @type {string} */ (reader.readString());
      msg.setLocationDescription(value);
      break;
    case 9:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 10:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setScheduleEnd(value);
      break;
    case 11:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setScheduleSlot(value);
      break;
    case 12:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setScheduleStart(value);
      break;
    case 13:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setTimePeriod(value);
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
proto.dlkit.proto.calendaring.Schedule.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.Schedule.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.Schedule} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Schedule.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
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
  f = message.getLimitList();
  if (f.length > 0) {
    writer.writePackedSint32(
      6,
      f
    );
  }
  f = message.getLocation();
  if (f != null) {
    writer.writeMessage(
      7,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getLocationDescription();
  if (f.length > 0) {
    writer.writeString(
      8,
      f
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      9,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getScheduleEnd();
  if (f != null) {
    writer.writeMessage(
      10,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getScheduleSlot();
  if (f != null) {
    writer.writeMessage(
      11,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getScheduleStart();
  if (f != null) {
    writer.writeMessage(
      12,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getTimePeriod();
  if (f != null) {
    writer.writeMessage(
      13,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 3;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 3));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 4;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 4));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 5;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 5));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasId = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * repeated sint32 limit = 6;
 * @return {!Array.<number>}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getLimitList = function() {
  return /** @type {!Array.<number>} */ (jspb.Message.getRepeatedField(this, 6));
};


/** @param {!Array.<number>} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setLimitList = function(value) {
  jspb.Message.setField(this, 6, value || []);
};


/**
 * @param {!number} value
 * @param {number=} opt_index
 */
proto.dlkit.proto.calendaring.Schedule.prototype.addLimit = function(value, opt_index) {
  jspb.Message.addToRepeatedField(this, 6, value, opt_index);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearLimitList = function() {
  this.setLimitList([]);
};


/**
 * optional dlkit.primordium.id.primitives.Id location = 7;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getLocation = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 7));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setLocation = function(value) {
  jspb.Message.setWrapperField(this, 7, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearLocation = function() {
  this.setLocation(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasLocation = function() {
  return jspb.Message.getField(this, 7) != null;
};


/**
 * optional string location_description = 8;
 * @return {string}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getLocationDescription = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 8, ""));
};


/** @param {string} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setLocationDescription = function(value) {
  jspb.Message.setProto3StringField(this, 8, value);
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 9;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 9));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 9, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 9, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * optional google.protobuf.Timestamp schedule_end = 10;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getScheduleEnd = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 10));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setScheduleEnd = function(value) {
  jspb.Message.setWrapperField(this, 10, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearScheduleEnd = function() {
  this.setScheduleEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasScheduleEnd = function() {
  return jspb.Message.getField(this, 10) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id schedule_slot = 11;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getScheduleSlot = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 11));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setScheduleSlot = function(value) {
  jspb.Message.setWrapperField(this, 11, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearScheduleSlot = function() {
  this.setScheduleSlot(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasScheduleSlot = function() {
  return jspb.Message.getField(this, 11) != null;
};


/**
 * optional google.protobuf.Timestamp schedule_start = 12;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getScheduleStart = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 12));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setScheduleStart = function(value) {
  jspb.Message.setWrapperField(this, 12, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearScheduleStart = function() {
  this.setScheduleStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasScheduleStart = function() {
  return jspb.Message.getField(this, 12) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id time_period = 13;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.getTimePeriod = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 13));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Schedule.prototype.setTimePeriod = function(value) {
  jspb.Message.setWrapperField(this, 13, value);
};


proto.dlkit.proto.calendaring.Schedule.prototype.clearTimePeriod = function() {
  this.setTimePeriod(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Schedule.prototype.hasTimePeriod = function() {
  return jspb.Message.getField(this, 13) != null;
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
proto.dlkit.proto.calendaring.ScheduleQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleQuery.displayName = 'proto.dlkit.proto.calendaring.ScheduleQuery';
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
proto.dlkit.proto.calendaring.ScheduleQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleQuery}
 */
proto.dlkit.proto.calendaring.ScheduleQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleQuery;
  return proto.dlkit.proto.calendaring.ScheduleQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleQuery}
 */
proto.dlkit.proto.calendaring.ScheduleQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleQueryInspector.displayName = 'proto.dlkit.proto.calendaring.ScheduleQueryInspector';
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
proto.dlkit.proto.calendaring.ScheduleQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleQueryInspector}
 */
proto.dlkit.proto.calendaring.ScheduleQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleQueryInspector;
  return proto.dlkit.proto.calendaring.ScheduleQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleQueryInspector}
 */
proto.dlkit.proto.calendaring.ScheduleQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleForm.displayName = 'proto.dlkit.proto.calendaring.ScheduleForm';
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
proto.dlkit.proto.calendaring.ScheduleForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleForm}
 */
proto.dlkit.proto.calendaring.ScheduleForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleForm;
  return proto.dlkit.proto.calendaring.ScheduleForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleForm}
 */
proto.dlkit.proto.calendaring.ScheduleForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSearchOrder.displayName = 'proto.dlkit.proto.calendaring.ScheduleSearchOrder';
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
proto.dlkit.proto.calendaring.ScheduleSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSearchOrder}
 */
proto.dlkit.proto.calendaring.ScheduleSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSearchOrder;
  return proto.dlkit.proto.calendaring.ScheduleSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSearchOrder}
 */
proto.dlkit.proto.calendaring.ScheduleSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSearch.displayName = 'proto.dlkit.proto.calendaring.ScheduleSearch';
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
proto.dlkit.proto.calendaring.ScheduleSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSearch}
 */
proto.dlkit.proto.calendaring.ScheduleSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSearch;
  return proto.dlkit.proto.calendaring.ScheduleSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSearch}
 */
proto.dlkit.proto.calendaring.ScheduleSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSearchResults.displayName = 'proto.dlkit.proto.calendaring.ScheduleSearchResults';
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
proto.dlkit.proto.calendaring.ScheduleSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSearchResults}
 */
proto.dlkit.proto.calendaring.ScheduleSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSearchResults;
  return proto.dlkit.proto.calendaring.ScheduleSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSearchResults}
 */
proto.dlkit.proto.calendaring.ScheduleSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.ScheduleList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleList.displayName = 'proto.dlkit.proto.calendaring.ScheduleList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.ScheduleList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.ScheduleList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleList.toObject = function(includeInstance, msg) {
  var f, obj = {
    schedulesList: jspb.Message.toObjectList(msg.getSchedulesList(),
    proto.dlkit.proto.calendaring.Schedule.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleList}
 */
proto.dlkit.proto.calendaring.ScheduleList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleList;
  return proto.dlkit.proto.calendaring.ScheduleList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleList}
 */
proto.dlkit.proto.calendaring.ScheduleList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.Schedule;
      reader.readMessage(value,proto.dlkit.proto.calendaring.Schedule.deserializeBinaryFromReader);
      msg.addSchedules(value);
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
proto.dlkit.proto.calendaring.ScheduleList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSchedulesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.Schedule.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Schedule schedules = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.Schedule>}
 */
proto.dlkit.proto.calendaring.ScheduleList.prototype.getSchedulesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.Schedule>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.Schedule, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.Schedule>} value */
proto.dlkit.proto.calendaring.ScheduleList.prototype.setSchedulesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.Schedule=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.Schedule}
 */
proto.dlkit.proto.calendaring.ScheduleList.prototype.addSchedules = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.Schedule, opt_index);
};


proto.dlkit.proto.calendaring.ScheduleList.prototype.clearSchedulesList = function() {
  this.setSchedulesList([]);
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
proto.dlkit.proto.calendaring.ScheduleSlot = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.ScheduleSlot.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlot, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlot.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlot';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.ScheduleSlot.repeatedFields_ = [8,11];



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
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlot.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlot} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlot.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    duration: (f = msg.getDuration()) && dlkit_primordium_calendaring_primitives_pb.Duration.toObject(includeInstance, f),
    fixedInterval: (f = msg.getFixedInterval()) && dlkit_primordium_calendaring_primitives_pb.Duration.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    weekOfMonth: jspb.Message.getFieldWithDefault(msg, 9, 0),
    weekdayTime: (f = msg.getWeekdayTime()) && dlkit_primordium_calendaring_primitives_pb.Time.toObject(includeInstance, f),
    weekdaysList: jspb.Message.getRepeatedField(msg, 11),
    weeklyInterval: jspb.Message.getFieldWithDefault(msg, 12, 0)
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlot}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlot;
  return proto.dlkit.proto.calendaring.ScheduleSlot.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlot} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlot}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
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
      var value = new dlkit_primordium_calendaring_primitives_pb.Duration;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Duration.deserializeBinaryFromReader);
      msg.setDuration(value);
      break;
    case 5:
      var value = new dlkit_primordium_calendaring_primitives_pb.Duration;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Duration.deserializeBinaryFromReader);
      msg.setFixedInterval(value);
      break;
    case 6:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setGenusTypeId(value);
      break;
    case 7:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 8:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 9:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setWeekOfMonth(value);
      break;
    case 10:
      var value = new dlkit_primordium_calendaring_primitives_pb.Time;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Time.deserializeBinaryFromReader);
      msg.setWeekdayTime(value);
      break;
    case 11:
      var value = /** @type {!Array.<number>} */ (reader.readPackedSint32());
      msg.setWeekdaysList(value);
      break;
    case 12:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setWeeklyInterval(value);
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
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlot.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlot} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlot.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
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
  f = message.getDuration();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_calendaring_primitives_pb.Duration.serializeBinaryToWriter
    );
  }
  f = message.getFixedInterval();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      dlkit_primordium_calendaring_primitives_pb.Duration.serializeBinaryToWriter
    );
  }
  f = message.getGenusTypeId();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      7,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
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
  f = message.getWeekOfMonth();
  if (f !== 0) {
    writer.writeSint32(
      9,
      f
    );
  }
  f = message.getWeekdayTime();
  if (f != null) {
    writer.writeMessage(
      10,
      f,
      dlkit_primordium_calendaring_primitives_pb.Time.serializeBinaryToWriter
    );
  }
  f = message.getWeekdaysList();
  if (f.length > 0) {
    writer.writePackedSint32(
      11,
      f
    );
  }
  f = message.getWeeklyInterval();
  if (f !== 0) {
    writer.writeSint32(
      12,
      f
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 3;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 3));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.calendaring.primitives.Duration duration = 4;
 * @return {?proto.dlkit.primordium.calendaring.primitives.Duration}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getDuration = function() {
  return /** @type{?proto.dlkit.primordium.calendaring.primitives.Duration} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Duration, 4));
};


/** @param {?proto.dlkit.primordium.calendaring.primitives.Duration|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setDuration = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearDuration = function() {
  this.setDuration(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasDuration = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.calendaring.primitives.Duration fixed_interval = 5;
 * @return {?proto.dlkit.primordium.calendaring.primitives.Duration}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getFixedInterval = function() {
  return /** @type{?proto.dlkit.primordium.calendaring.primitives.Duration} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Duration, 5));
};


/** @param {?proto.dlkit.primordium.calendaring.primitives.Duration|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setFixedInterval = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearFixedInterval = function() {
  this.setFixedInterval(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasFixedInterval = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 6;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 6));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 6, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 7;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 7));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 7, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasId = function() {
  return jspb.Message.getField(this, 7) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 8;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 8));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 8, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 8, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * optional sint32 week_of_month = 9;
 * @return {number}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getWeekOfMonth = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 9, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setWeekOfMonth = function(value) {
  jspb.Message.setProto3IntField(this, 9, value);
};


/**
 * optional dlkit.primordium.calendaring.primitives.Time weekday_time = 10;
 * @return {?proto.dlkit.primordium.calendaring.primitives.Time}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getWeekdayTime = function() {
  return /** @type{?proto.dlkit.primordium.calendaring.primitives.Time} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Time, 10));
};


/** @param {?proto.dlkit.primordium.calendaring.primitives.Time|undefined} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setWeekdayTime = function(value) {
  jspb.Message.setWrapperField(this, 10, value);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearWeekdayTime = function() {
  this.setWeekdayTime(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.hasWeekdayTime = function() {
  return jspb.Message.getField(this, 10) != null;
};


/**
 * repeated sint32 weekdays = 11;
 * @return {!Array.<number>}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getWeekdaysList = function() {
  return /** @type {!Array.<number>} */ (jspb.Message.getRepeatedField(this, 11));
};


/** @param {!Array.<number>} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setWeekdaysList = function(value) {
  jspb.Message.setField(this, 11, value || []);
};


/**
 * @param {!number} value
 * @param {number=} opt_index
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.addWeekdays = function(value, opt_index) {
  jspb.Message.addToRepeatedField(this, 11, value, opt_index);
};


proto.dlkit.proto.calendaring.ScheduleSlot.prototype.clearWeekdaysList = function() {
  this.setWeekdaysList([]);
};


/**
 * optional sint32 weekly_interval = 12;
 * @return {number}
 */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.getWeeklyInterval = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 12, 0));
};


/** @param {number} value */
proto.dlkit.proto.calendaring.ScheduleSlot.prototype.setWeeklyInterval = function(value) {
  jspb.Message.setProto3IntField(this, 12, value);
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
proto.dlkit.proto.calendaring.ScheduleSlotQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotQuery.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotQuery';
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
proto.dlkit.proto.calendaring.ScheduleSlotQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotQuery}
 */
proto.dlkit.proto.calendaring.ScheduleSlotQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotQuery;
  return proto.dlkit.proto.calendaring.ScheduleSlotQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotQuery}
 */
proto.dlkit.proto.calendaring.ScheduleSlotQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSlotQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector';
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
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector}
 */
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector;
  return proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector}
 */
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSlotForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotForm.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotForm';
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
proto.dlkit.proto.calendaring.ScheduleSlotForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotForm}
 */
proto.dlkit.proto.calendaring.ScheduleSlotForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotForm;
  return proto.dlkit.proto.calendaring.ScheduleSlotForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotForm}
 */
proto.dlkit.proto.calendaring.ScheduleSlotForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSlotForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder';
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
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder}
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder;
  return proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder}
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSlotSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotSearch.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotSearch';
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
proto.dlkit.proto.calendaring.ScheduleSlotSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotSearch}
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotSearch;
  return proto.dlkit.proto.calendaring.ScheduleSlotSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotSearch}
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSlotSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotSearchResults';
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
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotSearchResults}
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotSearchResults;
  return proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotSearchResults}
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.ScheduleSlotList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.ScheduleSlotList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.ScheduleSlotList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.ScheduleSlotList.displayName = 'proto.dlkit.proto.calendaring.ScheduleSlotList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.ScheduleSlotList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.ScheduleSlotList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.toObject = function(includeInstance, msg) {
  var f, obj = {
    scheduleSlotsList: jspb.Message.toObjectList(msg.getScheduleSlotsList(),
    proto.dlkit.proto.calendaring.ScheduleSlot.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotList}
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.ScheduleSlotList;
  return proto.dlkit.proto.calendaring.ScheduleSlotList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlotList}
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.ScheduleSlot;
      reader.readMessage(value,proto.dlkit.proto.calendaring.ScheduleSlot.deserializeBinaryFromReader);
      msg.addScheduleSlots(value);
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
proto.dlkit.proto.calendaring.ScheduleSlotList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.ScheduleSlotList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlotList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getScheduleSlotsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.ScheduleSlot.serializeBinaryToWriter
    );
  }
};


/**
 * repeated ScheduleSlot schedule_slots = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.ScheduleSlot>}
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.prototype.getScheduleSlotsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.ScheduleSlot>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.ScheduleSlot, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.ScheduleSlot>} value */
proto.dlkit.proto.calendaring.ScheduleSlotList.prototype.setScheduleSlotsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.ScheduleSlot=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.ScheduleSlot}
 */
proto.dlkit.proto.calendaring.ScheduleSlotList.prototype.addScheduleSlots = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.ScheduleSlot, opt_index);
};


proto.dlkit.proto.calendaring.ScheduleSlotList.prototype.clearScheduleSlotsList = function() {
  this.setScheduleSlotsList([]);
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
proto.dlkit.proto.calendaring.TimePeriod = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.TimePeriod.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriod, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriod.displayName = 'proto.dlkit.proto.calendaring.TimePeriod';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.TimePeriod.repeatedFields_ = [7];



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
proto.dlkit.proto.calendaring.TimePeriod.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriod.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriod} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriod.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    end: (f = msg.getEnd()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriod}
 */
proto.dlkit.proto.calendaring.TimePeriod.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriod;
  return proto.dlkit.proto.calendaring.TimePeriod.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriod} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriod}
 */
proto.dlkit.proto.calendaring.TimePeriod.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
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
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setEnd(value);
      break;
    case 5:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setGenusTypeId(value);
      break;
    case 6:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setId(value);
      break;
    case 7:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 8:
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
proto.dlkit.proto.calendaring.TimePeriod.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriod.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriod} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriod.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
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
  f = message.getEnd();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getGenusTypeId();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      7,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getStart();
  if (f != null) {
    writer.writeMessage(
      8,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 3;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 3));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp end = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getEnd = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setEnd = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearEnd = function() {
  this.setEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasEnd = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 5;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 6;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 6));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 6, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasId = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 7;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 7));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 7, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 7, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * optional google.protobuf.Timestamp start = 8;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.getStart = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 8));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.calendaring.TimePeriod.prototype.setStart = function(value) {
  jspb.Message.setWrapperField(this, 8, value);
};


proto.dlkit.proto.calendaring.TimePeriod.prototype.clearStart = function() {
  this.setStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.TimePeriod.prototype.hasStart = function() {
  return jspb.Message.getField(this, 8) != null;
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
proto.dlkit.proto.calendaring.TimePeriodQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodQuery.displayName = 'proto.dlkit.proto.calendaring.TimePeriodQuery';
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
proto.dlkit.proto.calendaring.TimePeriodQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodQuery}
 */
proto.dlkit.proto.calendaring.TimePeriodQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodQuery;
  return proto.dlkit.proto.calendaring.TimePeriodQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodQuery}
 */
proto.dlkit.proto.calendaring.TimePeriodQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.TimePeriodQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.TimePeriodQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodQueryInspector.displayName = 'proto.dlkit.proto.calendaring.TimePeriodQueryInspector';
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
proto.dlkit.proto.calendaring.TimePeriodQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodQueryInspector}
 */
proto.dlkit.proto.calendaring.TimePeriodQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodQueryInspector;
  return proto.dlkit.proto.calendaring.TimePeriodQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodQueryInspector}
 */
proto.dlkit.proto.calendaring.TimePeriodQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.TimePeriodQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.TimePeriodForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodForm.displayName = 'proto.dlkit.proto.calendaring.TimePeriodForm';
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
proto.dlkit.proto.calendaring.TimePeriodForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodForm}
 */
proto.dlkit.proto.calendaring.TimePeriodForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodForm;
  return proto.dlkit.proto.calendaring.TimePeriodForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodForm}
 */
proto.dlkit.proto.calendaring.TimePeriodForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.TimePeriodForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.TimePeriodSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodSearchOrder.displayName = 'proto.dlkit.proto.calendaring.TimePeriodSearchOrder';
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
proto.dlkit.proto.calendaring.TimePeriodSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodSearchOrder}
 */
proto.dlkit.proto.calendaring.TimePeriodSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodSearchOrder;
  return proto.dlkit.proto.calendaring.TimePeriodSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodSearchOrder}
 */
proto.dlkit.proto.calendaring.TimePeriodSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.TimePeriodSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.TimePeriodSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodSearch.displayName = 'proto.dlkit.proto.calendaring.TimePeriodSearch';
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
proto.dlkit.proto.calendaring.TimePeriodSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodSearch}
 */
proto.dlkit.proto.calendaring.TimePeriodSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodSearch;
  return proto.dlkit.proto.calendaring.TimePeriodSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodSearch}
 */
proto.dlkit.proto.calendaring.TimePeriodSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.TimePeriodSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.TimePeriodSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodSearchResults.displayName = 'proto.dlkit.proto.calendaring.TimePeriodSearchResults';
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
proto.dlkit.proto.calendaring.TimePeriodSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodSearchResults}
 */
proto.dlkit.proto.calendaring.TimePeriodSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodSearchResults;
  return proto.dlkit.proto.calendaring.TimePeriodSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodSearchResults}
 */
proto.dlkit.proto.calendaring.TimePeriodSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.TimePeriodSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.TimePeriodList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.TimePeriodList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimePeriodList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimePeriodList.displayName = 'proto.dlkit.proto.calendaring.TimePeriodList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.TimePeriodList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.TimePeriodList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimePeriodList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimePeriodList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodList.toObject = function(includeInstance, msg) {
  var f, obj = {
    timePeriodsList: jspb.Message.toObjectList(msg.getTimePeriodsList(),
    proto.dlkit.proto.calendaring.TimePeriod.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.TimePeriodList}
 */
proto.dlkit.proto.calendaring.TimePeriodList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimePeriodList;
  return proto.dlkit.proto.calendaring.TimePeriodList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimePeriodList}
 */
proto.dlkit.proto.calendaring.TimePeriodList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.TimePeriod;
      reader.readMessage(value,proto.dlkit.proto.calendaring.TimePeriod.deserializeBinaryFromReader);
      msg.addTimePeriods(value);
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
proto.dlkit.proto.calendaring.TimePeriodList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimePeriodList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimePeriodList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimePeriodList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getTimePeriodsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.TimePeriod.serializeBinaryToWriter
    );
  }
};


/**
 * repeated TimePeriod time_periods = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.TimePeriod>}
 */
proto.dlkit.proto.calendaring.TimePeriodList.prototype.getTimePeriodsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.TimePeriod>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.TimePeriod, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.TimePeriod>} value */
proto.dlkit.proto.calendaring.TimePeriodList.prototype.setTimePeriodsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.TimePeriod=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.TimePeriod}
 */
proto.dlkit.proto.calendaring.TimePeriodList.prototype.addTimePeriods = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.TimePeriod, opt_index);
};


proto.dlkit.proto.calendaring.TimePeriodList.prototype.clearTimePeriodsList = function() {
  this.setTimePeriodsList([]);
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
proto.dlkit.proto.calendaring.Commitment = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.Commitment, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.Commitment.displayName = 'proto.dlkit.proto.calendaring.Commitment';
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
proto.dlkit.proto.calendaring.Commitment.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.Commitment.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.Commitment} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Commitment.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendar: (f = msg.getCalendar()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    event: (f = msg.getEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    resource: (f = msg.getResource()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.calendaring.Commitment}
 */
proto.dlkit.proto.calendaring.Commitment.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.Commitment;
  return proto.dlkit.proto.calendaring.Commitment.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.Commitment} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.Commitment}
 */
proto.dlkit.proto.calendaring.Commitment.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setCalendar(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setEvent(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResource(value);
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
proto.dlkit.proto.calendaring.Commitment.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.Commitment.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.Commitment} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Commitment.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getEvent();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getResource();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog calendar = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.calendaring.Commitment.prototype.getCalendar = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.calendaring.Commitment.prototype.setCalendar = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.Commitment.prototype.clearCalendar = function() {
  this.setCalendar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Commitment.prototype.hasCalendar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id event = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Commitment.prototype.getEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Commitment.prototype.setEvent = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.Commitment.prototype.clearEvent = function() {
  this.setEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Commitment.prototype.hasEvent = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Commitment.prototype.getResource = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Commitment.prototype.setResource = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.Commitment.prototype.clearResource = function() {
  this.setResource(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Commitment.prototype.hasResource = function() {
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
proto.dlkit.proto.calendaring.CommitmentQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentQuery.displayName = 'proto.dlkit.proto.calendaring.CommitmentQuery';
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
proto.dlkit.proto.calendaring.CommitmentQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentQuery}
 */
proto.dlkit.proto.calendaring.CommitmentQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentQuery;
  return proto.dlkit.proto.calendaring.CommitmentQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentQuery}
 */
proto.dlkit.proto.calendaring.CommitmentQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CommitmentQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CommitmentQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentQueryInspector.displayName = 'proto.dlkit.proto.calendaring.CommitmentQueryInspector';
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
proto.dlkit.proto.calendaring.CommitmentQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentQueryInspector}
 */
proto.dlkit.proto.calendaring.CommitmentQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentQueryInspector;
  return proto.dlkit.proto.calendaring.CommitmentQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentQueryInspector}
 */
proto.dlkit.proto.calendaring.CommitmentQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CommitmentQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CommitmentForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentForm.displayName = 'proto.dlkit.proto.calendaring.CommitmentForm';
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
proto.dlkit.proto.calendaring.CommitmentForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentForm}
 */
proto.dlkit.proto.calendaring.CommitmentForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentForm;
  return proto.dlkit.proto.calendaring.CommitmentForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentForm}
 */
proto.dlkit.proto.calendaring.CommitmentForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CommitmentForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CommitmentSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentSearchOrder.displayName = 'proto.dlkit.proto.calendaring.CommitmentSearchOrder';
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
proto.dlkit.proto.calendaring.CommitmentSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentSearchOrder}
 */
proto.dlkit.proto.calendaring.CommitmentSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentSearchOrder;
  return proto.dlkit.proto.calendaring.CommitmentSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentSearchOrder}
 */
proto.dlkit.proto.calendaring.CommitmentSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CommitmentSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CommitmentSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentSearch.displayName = 'proto.dlkit.proto.calendaring.CommitmentSearch';
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
proto.dlkit.proto.calendaring.CommitmentSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentSearch}
 */
proto.dlkit.proto.calendaring.CommitmentSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentSearch;
  return proto.dlkit.proto.calendaring.CommitmentSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentSearch}
 */
proto.dlkit.proto.calendaring.CommitmentSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CommitmentSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CommitmentSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentSearchResults.displayName = 'proto.dlkit.proto.calendaring.CommitmentSearchResults';
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
proto.dlkit.proto.calendaring.CommitmentSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentSearchResults}
 */
proto.dlkit.proto.calendaring.CommitmentSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentSearchResults;
  return proto.dlkit.proto.calendaring.CommitmentSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentSearchResults}
 */
proto.dlkit.proto.calendaring.CommitmentSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CommitmentSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CommitmentList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.CommitmentList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CommitmentList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CommitmentList.displayName = 'proto.dlkit.proto.calendaring.CommitmentList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.CommitmentList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.CommitmentList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CommitmentList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CommitmentList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentList.toObject = function(includeInstance, msg) {
  var f, obj = {
    commitmentsList: jspb.Message.toObjectList(msg.getCommitmentsList(),
    proto.dlkit.proto.calendaring.Commitment.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.CommitmentList}
 */
proto.dlkit.proto.calendaring.CommitmentList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CommitmentList;
  return proto.dlkit.proto.calendaring.CommitmentList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CommitmentList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CommitmentList}
 */
proto.dlkit.proto.calendaring.CommitmentList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.Commitment;
      reader.readMessage(value,proto.dlkit.proto.calendaring.Commitment.deserializeBinaryFromReader);
      msg.addCommitments(value);
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
proto.dlkit.proto.calendaring.CommitmentList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CommitmentList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CommitmentList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CommitmentList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommitmentsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.Commitment.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Commitment commitments = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.Commitment>}
 */
proto.dlkit.proto.calendaring.CommitmentList.prototype.getCommitmentsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.Commitment>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.Commitment, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.Commitment>} value */
proto.dlkit.proto.calendaring.CommitmentList.prototype.setCommitmentsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.Commitment=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.Commitment}
 */
proto.dlkit.proto.calendaring.CommitmentList.prototype.addCommitments = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.Commitment, opt_index);
};


proto.dlkit.proto.calendaring.CommitmentList.prototype.clearCommitmentsList = function() {
  this.setCommitmentsList([]);
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
proto.dlkit.proto.calendaring.Calendar = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.Calendar.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.Calendar, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.Calendar.displayName = 'proto.dlkit.proto.calendaring.Calendar';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.Calendar.repeatedFields_ = [5];



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
proto.dlkit.proto.calendaring.Calendar.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.Calendar.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.Calendar} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Calendar.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.Calendar}
 */
proto.dlkit.proto.calendaring.Calendar.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.Calendar;
  return proto.dlkit.proto.calendaring.Calendar.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.Calendar} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.Calendar}
 */
proto.dlkit.proto.calendaring.Calendar.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.Calendar.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.Calendar.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.Calendar} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.Calendar.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.Calendar.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.Calendar.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.calendaring.Calendar.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.calendaring.Calendar.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.calendaring.Calendar.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.calendaring.Calendar.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.calendaring.Calendar.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.calendaring.Calendar.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.calendaring.Calendar.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 5;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.calendaring.Calendar.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.calendaring.Calendar.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.calendaring.Calendar.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.calendaring.CalendarQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarQuery.displayName = 'proto.dlkit.proto.calendaring.CalendarQuery';
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
proto.dlkit.proto.calendaring.CalendarQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarQuery}
 */
proto.dlkit.proto.calendaring.CalendarQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarQuery;
  return proto.dlkit.proto.calendaring.CalendarQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarQuery}
 */
proto.dlkit.proto.calendaring.CalendarQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarQueryInspector.displayName = 'proto.dlkit.proto.calendaring.CalendarQueryInspector';
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
proto.dlkit.proto.calendaring.CalendarQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarQueryInspector}
 */
proto.dlkit.proto.calendaring.CalendarQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarQueryInspector;
  return proto.dlkit.proto.calendaring.CalendarQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarQueryInspector}
 */
proto.dlkit.proto.calendaring.CalendarQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarForm.displayName = 'proto.dlkit.proto.calendaring.CalendarForm';
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
proto.dlkit.proto.calendaring.CalendarForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarForm}
 */
proto.dlkit.proto.calendaring.CalendarForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarForm;
  return proto.dlkit.proto.calendaring.CalendarForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarForm}
 */
proto.dlkit.proto.calendaring.CalendarForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarSearchOrder.displayName = 'proto.dlkit.proto.calendaring.CalendarSearchOrder';
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
proto.dlkit.proto.calendaring.CalendarSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarSearchOrder}
 */
proto.dlkit.proto.calendaring.CalendarSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarSearchOrder;
  return proto.dlkit.proto.calendaring.CalendarSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarSearchOrder}
 */
proto.dlkit.proto.calendaring.CalendarSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarSearch.displayName = 'proto.dlkit.proto.calendaring.CalendarSearch';
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
proto.dlkit.proto.calendaring.CalendarSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarSearch}
 */
proto.dlkit.proto.calendaring.CalendarSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarSearch;
  return proto.dlkit.proto.calendaring.CalendarSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarSearch}
 */
proto.dlkit.proto.calendaring.CalendarSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarSearchResults.displayName = 'proto.dlkit.proto.calendaring.CalendarSearchResults';
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
proto.dlkit.proto.calendaring.CalendarSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarSearchResults}
 */
proto.dlkit.proto.calendaring.CalendarSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarSearchResults;
  return proto.dlkit.proto.calendaring.CalendarSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarSearchResults}
 */
proto.dlkit.proto.calendaring.CalendarSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.CalendarList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarList.displayName = 'proto.dlkit.proto.calendaring.CalendarList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.CalendarList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.CalendarList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarList.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendarsList: jspb.Message.toObjectList(msg.getCalendarsList(),
    proto.dlkit.proto.calendaring.Calendar.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.CalendarList}
 */
proto.dlkit.proto.calendaring.CalendarList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarList;
  return proto.dlkit.proto.calendaring.CalendarList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarList}
 */
proto.dlkit.proto.calendaring.CalendarList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.Calendar;
      reader.readMessage(value,proto.dlkit.proto.calendaring.Calendar.deserializeBinaryFromReader);
      msg.addCalendars(value);
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
proto.dlkit.proto.calendaring.CalendarList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendarsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.Calendar.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Calendar calendars = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.Calendar>}
 */
proto.dlkit.proto.calendaring.CalendarList.prototype.getCalendarsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.Calendar>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.Calendar, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.Calendar>} value */
proto.dlkit.proto.calendaring.CalendarList.prototype.setCalendarsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.Calendar=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.Calendar}
 */
proto.dlkit.proto.calendaring.CalendarList.prototype.addCalendars = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.Calendar, opt_index);
};


proto.dlkit.proto.calendaring.CalendarList.prototype.clearCalendarsList = function() {
  this.setCalendarsList([]);
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
proto.dlkit.proto.calendaring.CalendarNode = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarNode, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarNode.displayName = 'proto.dlkit.proto.calendaring.CalendarNode';
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
proto.dlkit.proto.calendaring.CalendarNode.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarNode.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarNode} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarNode.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.CalendarNode}
 */
proto.dlkit.proto.calendaring.CalendarNode.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarNode;
  return proto.dlkit.proto.calendaring.CalendarNode.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarNode} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarNode}
 */
proto.dlkit.proto.calendaring.CalendarNode.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.CalendarNode.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarNode.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarNode} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarNode.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.CalendarNodeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.CalendarNodeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.CalendarNodeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.CalendarNodeList.displayName = 'proto.dlkit.proto.calendaring.CalendarNodeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.CalendarNodeList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.CalendarNodeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.CalendarNodeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.CalendarNodeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarNodeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    calendarNodesList: jspb.Message.toObjectList(msg.getCalendarNodesList(),
    proto.dlkit.proto.calendaring.CalendarNode.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.CalendarNodeList}
 */
proto.dlkit.proto.calendaring.CalendarNodeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.CalendarNodeList;
  return proto.dlkit.proto.calendaring.CalendarNodeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.CalendarNodeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.CalendarNodeList}
 */
proto.dlkit.proto.calendaring.CalendarNodeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.CalendarNode;
      reader.readMessage(value,proto.dlkit.proto.calendaring.CalendarNode.deserializeBinaryFromReader);
      msg.addCalendarNodes(value);
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
proto.dlkit.proto.calendaring.CalendarNodeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.CalendarNodeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.CalendarNodeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.CalendarNodeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCalendarNodesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.CalendarNode.serializeBinaryToWriter
    );
  }
};


/**
 * repeated CalendarNode calendar_nodes = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.CalendarNode>}
 */
proto.dlkit.proto.calendaring.CalendarNodeList.prototype.getCalendarNodesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.CalendarNode>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.CalendarNode, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.CalendarNode>} value */
proto.dlkit.proto.calendaring.CalendarNodeList.prototype.setCalendarNodesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.CalendarNode=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.CalendarNode}
 */
proto.dlkit.proto.calendaring.CalendarNodeList.prototype.addCalendarNodes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.CalendarNode, opt_index);
};


proto.dlkit.proto.calendaring.CalendarNodeList.prototype.clearCalendarNodesList = function() {
  this.setCalendarNodesList([]);
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
proto.dlkit.proto.calendaring.MeetingTime = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.MeetingTime, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.MeetingTime.displayName = 'proto.dlkit.proto.calendaring.MeetingTime';
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
proto.dlkit.proto.calendaring.MeetingTime.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.MeetingTime.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.MeetingTime} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.MeetingTime.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.MeetingTime}
 */
proto.dlkit.proto.calendaring.MeetingTime.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.MeetingTime;
  return proto.dlkit.proto.calendaring.MeetingTime.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.MeetingTime} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.MeetingTime}
 */
proto.dlkit.proto.calendaring.MeetingTime.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.MeetingTime.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.MeetingTime.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.MeetingTime} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.MeetingTime.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.MeetingTimeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.MeetingTimeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.MeetingTimeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.MeetingTimeList.displayName = 'proto.dlkit.proto.calendaring.MeetingTimeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.MeetingTimeList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.MeetingTimeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.MeetingTimeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.MeetingTimeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.MeetingTimeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    meetingTimesList: jspb.Message.toObjectList(msg.getMeetingTimesList(),
    proto.dlkit.proto.calendaring.MeetingTime.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.MeetingTimeList}
 */
proto.dlkit.proto.calendaring.MeetingTimeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.MeetingTimeList;
  return proto.dlkit.proto.calendaring.MeetingTimeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.MeetingTimeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.MeetingTimeList}
 */
proto.dlkit.proto.calendaring.MeetingTimeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.calendaring.MeetingTime;
      reader.readMessage(value,proto.dlkit.proto.calendaring.MeetingTime.deserializeBinaryFromReader);
      msg.addMeetingTimes(value);
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
proto.dlkit.proto.calendaring.MeetingTimeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.MeetingTimeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.MeetingTimeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.MeetingTimeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getMeetingTimesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.calendaring.MeetingTime.serializeBinaryToWriter
    );
  }
};


/**
 * repeated MeetingTime meeting_times = 1;
 * @return {!Array.<!proto.dlkit.proto.calendaring.MeetingTime>}
 */
proto.dlkit.proto.calendaring.MeetingTimeList.prototype.getMeetingTimesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.calendaring.MeetingTime>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.calendaring.MeetingTime, 1));
};


/** @param {!Array.<!proto.dlkit.proto.calendaring.MeetingTime>} value */
proto.dlkit.proto.calendaring.MeetingTimeList.prototype.setMeetingTimesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.calendaring.MeetingTime=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.calendaring.MeetingTime}
 */
proto.dlkit.proto.calendaring.MeetingTimeList.prototype.addMeetingTimes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.calendaring.MeetingTime, opt_index);
};


proto.dlkit.proto.calendaring.MeetingTimeList.prototype.clearMeetingTimesList = function() {
  this.setMeetingTimesList([]);
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
proto.dlkit.proto.calendaring.TimeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.TimeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.TimeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.TimeList.displayName = 'proto.dlkit.proto.calendaring.TimeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.TimeList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.TimeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.TimeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.TimeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    timesList: jspb.Message.toObjectList(msg.getTimesList(),
    dlkit_primordium_calendaring_primitives_pb.Time.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.TimeList}
 */
proto.dlkit.proto.calendaring.TimeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.TimeList;
  return proto.dlkit.proto.calendaring.TimeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.TimeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.TimeList}
 */
proto.dlkit.proto.calendaring.TimeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_calendaring_primitives_pb.Time;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Time.deserializeBinaryFromReader);
      msg.addTimes(value);
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
proto.dlkit.proto.calendaring.TimeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.TimeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.TimeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.TimeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getTimesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_calendaring_primitives_pb.Time.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.calendaring.primitives.Time times = 1;
 * @return {!Array.<!proto.dlkit.primordium.calendaring.primitives.Time>}
 */
proto.dlkit.proto.calendaring.TimeList.prototype.getTimesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.calendaring.primitives.Time>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Time, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.calendaring.primitives.Time>} value */
proto.dlkit.proto.calendaring.TimeList.prototype.setTimesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.calendaring.primitives.Time=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.calendaring.primitives.Time}
 */
proto.dlkit.proto.calendaring.TimeList.prototype.addTimes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.calendaring.primitives.Time, opt_index);
};


proto.dlkit.proto.calendaring.TimeList.prototype.clearTimesList = function() {
  this.setTimesList([]);
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
proto.dlkit.proto.calendaring.DateTimeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.DateTimeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.DateTimeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.DateTimeList.displayName = 'proto.dlkit.proto.calendaring.DateTimeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.DateTimeList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.DateTimeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.DateTimeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.DateTimeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DateTimeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    dateTimesList: jspb.Message.toObjectList(msg.getDateTimesList(),
    google_protobuf_timestamp_pb.Timestamp.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.DateTimeList}
 */
proto.dlkit.proto.calendaring.DateTimeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.DateTimeList;
  return proto.dlkit.proto.calendaring.DateTimeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.DateTimeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.DateTimeList}
 */
proto.dlkit.proto.calendaring.DateTimeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.addDateTimes(value);
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
proto.dlkit.proto.calendaring.DateTimeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.DateTimeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.DateTimeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DateTimeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDateTimesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * repeated google.protobuf.Timestamp date_times = 1;
 * @return {!Array.<!proto.google.protobuf.Timestamp>}
 */
proto.dlkit.proto.calendaring.DateTimeList.prototype.getDateTimesList = function() {
  return /** @type{!Array.<!proto.google.protobuf.Timestamp>} */ (
    jspb.Message.getRepeatedWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {!Array.<!proto.google.protobuf.Timestamp>} value */
proto.dlkit.proto.calendaring.DateTimeList.prototype.setDateTimesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.google.protobuf.Timestamp=} opt_value
 * @param {number=} opt_index
 * @return {!proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.calendaring.DateTimeList.prototype.addDateTimes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.google.protobuf.Timestamp, opt_index);
};


proto.dlkit.proto.calendaring.DateTimeList.prototype.clearDateTimesList = function() {
  this.setDateTimesList([]);
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
proto.dlkit.proto.calendaring.DurationList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.DurationList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.DurationList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.DurationList.displayName = 'proto.dlkit.proto.calendaring.DurationList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.DurationList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.DurationList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.DurationList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.DurationList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DurationList.toObject = function(includeInstance, msg) {
  var f, obj = {
    durationsList: jspb.Message.toObjectList(msg.getDurationsList(),
    dlkit_primordium_calendaring_primitives_pb.Duration.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.DurationList}
 */
proto.dlkit.proto.calendaring.DurationList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.DurationList;
  return proto.dlkit.proto.calendaring.DurationList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.DurationList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.DurationList}
 */
proto.dlkit.proto.calendaring.DurationList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_calendaring_primitives_pb.Duration;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.Duration.deserializeBinaryFromReader);
      msg.addDurations(value);
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
proto.dlkit.proto.calendaring.DurationList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.DurationList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.DurationList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DurationList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDurationsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_calendaring_primitives_pb.Duration.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.calendaring.primitives.Duration durations = 1;
 * @return {!Array.<!proto.dlkit.primordium.calendaring.primitives.Duration>}
 */
proto.dlkit.proto.calendaring.DurationList.prototype.getDurationsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.calendaring.primitives.Duration>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_calendaring_primitives_pb.Duration, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.calendaring.primitives.Duration>} value */
proto.dlkit.proto.calendaring.DurationList.prototype.setDurationsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.calendaring.primitives.Duration=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.calendaring.primitives.Duration}
 */
proto.dlkit.proto.calendaring.DurationList.prototype.addDurations = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.calendaring.primitives.Duration, opt_index);
};


proto.dlkit.proto.calendaring.DurationList.prototype.clearDurationsList = function() {
  this.setDurationsList([]);
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
proto.dlkit.proto.calendaring.DateTimeInterval = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.calendaring.DateTimeInterval, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.DateTimeInterval.displayName = 'proto.dlkit.proto.calendaring.DateTimeInterval';
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
proto.dlkit.proto.calendaring.DateTimeInterval.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.DateTimeInterval.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.DateTimeInterval} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DateTimeInterval.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.calendaring.DateTimeInterval}
 */
proto.dlkit.proto.calendaring.DateTimeInterval.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.DateTimeInterval;
  return proto.dlkit.proto.calendaring.DateTimeInterval.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.DateTimeInterval} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.DateTimeInterval}
 */
proto.dlkit.proto.calendaring.DateTimeInterval.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.calendaring.DateTimeInterval.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.DateTimeInterval.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.DateTimeInterval} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DateTimeInterval.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.calendaring.DateTimeIntervalList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.calendaring.DateTimeIntervalList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.calendaring.DateTimeIntervalList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.calendaring.DateTimeIntervalList.displayName = 'proto.dlkit.proto.calendaring.DateTimeIntervalList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.repeatedFields_ = [1];



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
proto.dlkit.proto.calendaring.DateTimeIntervalList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.calendaring.DateTimeIntervalList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.calendaring.DateTimeIntervalList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.toObject = function(includeInstance, msg) {
  var f, obj = {
    dateTimeIntervalsList: jspb.Message.toObjectList(msg.getDateTimeIntervalsList(),
    dlkit_primordium_calendaring_primitives_pb.DateTimeInterval.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.calendaring.DateTimeIntervalList}
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.calendaring.DateTimeIntervalList;
  return proto.dlkit.proto.calendaring.DateTimeIntervalList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.calendaring.DateTimeIntervalList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.calendaring.DateTimeIntervalList}
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_calendaring_primitives_pb.DateTimeInterval;
      reader.readMessage(value,dlkit_primordium_calendaring_primitives_pb.DateTimeInterval.deserializeBinaryFromReader);
      msg.addDateTimeIntervals(value);
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
proto.dlkit.proto.calendaring.DateTimeIntervalList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.calendaring.DateTimeIntervalList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.calendaring.DateTimeIntervalList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDateTimeIntervalsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_calendaring_primitives_pb.DateTimeInterval.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.calendaring.primitives.DateTimeInterval date_time_intervals = 1;
 * @return {!Array.<!proto.dlkit.primordium.calendaring.primitives.DateTimeInterval>}
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.prototype.getDateTimeIntervalsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.calendaring.primitives.DateTimeInterval>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_calendaring_primitives_pb.DateTimeInterval, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.calendaring.primitives.DateTimeInterval>} value */
proto.dlkit.proto.calendaring.DateTimeIntervalList.prototype.setDateTimeIntervalsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.calendaring.primitives.DateTimeInterval=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.calendaring.primitives.DateTimeInterval}
 */
proto.dlkit.proto.calendaring.DateTimeIntervalList.prototype.addDateTimeIntervals = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.calendaring.primitives.DateTimeInterval, opt_index);
};


proto.dlkit.proto.calendaring.DateTimeIntervalList.prototype.clearDateTimeIntervalsList = function() {
  this.setDateTimeIntervalsList([]);
};


goog.object.extend(exports, proto.dlkit.proto.calendaring);
