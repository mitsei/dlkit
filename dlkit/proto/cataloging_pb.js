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
goog.exportSymbol('proto.dlkit.proto.cataloging.AddChildCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.AddChildCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.AddRootCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.AddRootCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.AliasCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.AliasCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanCreateCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanCreateCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanDeleteCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanLookupCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanLookupCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanSearchCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanSearchCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanUpdateCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.Catalog', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogForm', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogList', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogNode', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogNodeList', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CatalogSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CreateCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.CreateCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.DeleteCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.DeleteCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogNodesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogNodesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogQueryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetChildCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetParentCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.GetRootCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.HasChildCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.HasChildCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.HasParentCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.HasParentCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsChildOfCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsChildOfCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsParentOfCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.IsParentOfCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.RemoveChildCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.RemoveChildCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.RemoveChildCatalogsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.RemoveRootCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.RemoveRootCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.UpdateCatalogReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.UpdateCatalogRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest', null, global);

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
proto.dlkit.proto.cataloging.Catalog = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.cataloging.Catalog.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.cataloging.Catalog, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.Catalog.displayName = 'proto.dlkit.proto.cataloging.Catalog';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.cataloging.Catalog.repeatedFields_ = [5];



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
proto.dlkit.proto.cataloging.Catalog.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.Catalog.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.Catalog} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.Catalog.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.Catalog}
 */
proto.dlkit.proto.cataloging.Catalog.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.Catalog;
  return proto.dlkit.proto.cataloging.Catalog.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.Catalog} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.Catalog}
 */
proto.dlkit.proto.cataloging.Catalog.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.Catalog.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.Catalog.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.Catalog} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.Catalog.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.Catalog.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.cataloging.Catalog.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.Catalog.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.cataloging.Catalog.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.Catalog.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.cataloging.Catalog.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.cataloging.Catalog.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.Catalog.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.cataloging.Catalog.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 5;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.cataloging.Catalog.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.Catalog.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.cataloging.Catalog.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.cataloging.CatalogQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogQuery.displayName = 'proto.dlkit.proto.cataloging.CatalogQuery';
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
proto.dlkit.proto.cataloging.CatalogQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogQuery}
 */
proto.dlkit.proto.cataloging.CatalogQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogQuery;
  return proto.dlkit.proto.cataloging.CatalogQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogQuery}
 */
proto.dlkit.proto.cataloging.CatalogQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogQueryInspector.displayName = 'proto.dlkit.proto.cataloging.CatalogQueryInspector';
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
proto.dlkit.proto.cataloging.CatalogQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogQueryInspector}
 */
proto.dlkit.proto.cataloging.CatalogQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogQueryInspector;
  return proto.dlkit.proto.cataloging.CatalogQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogQueryInspector}
 */
proto.dlkit.proto.cataloging.CatalogQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogForm.displayName = 'proto.dlkit.proto.cataloging.CatalogForm';
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
proto.dlkit.proto.cataloging.CatalogForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogForm}
 */
proto.dlkit.proto.cataloging.CatalogForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogForm;
  return proto.dlkit.proto.cataloging.CatalogForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogForm}
 */
proto.dlkit.proto.cataloging.CatalogForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogSearchOrder.displayName = 'proto.dlkit.proto.cataloging.CatalogSearchOrder';
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
proto.dlkit.proto.cataloging.CatalogSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogSearchOrder}
 */
proto.dlkit.proto.cataloging.CatalogSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogSearchOrder;
  return proto.dlkit.proto.cataloging.CatalogSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogSearchOrder}
 */
proto.dlkit.proto.cataloging.CatalogSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogSearch.displayName = 'proto.dlkit.proto.cataloging.CatalogSearch';
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
proto.dlkit.proto.cataloging.CatalogSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogSearch}
 */
proto.dlkit.proto.cataloging.CatalogSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogSearch;
  return proto.dlkit.proto.cataloging.CatalogSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogSearch}
 */
proto.dlkit.proto.cataloging.CatalogSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogSearchResults.displayName = 'proto.dlkit.proto.cataloging.CatalogSearchResults';
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
proto.dlkit.proto.cataloging.CatalogSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogSearchResults}
 */
proto.dlkit.proto.cataloging.CatalogSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogSearchResults;
  return proto.dlkit.proto.cataloging.CatalogSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogSearchResults}
 */
proto.dlkit.proto.cataloging.CatalogSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.cataloging.CatalogList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogList.displayName = 'proto.dlkit.proto.cataloging.CatalogList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.cataloging.CatalogList.repeatedFields_ = [1];



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
proto.dlkit.proto.cataloging.CatalogList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogList.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogsList: jspb.Message.toObjectList(msg.getCatalogsList(),
    proto.dlkit.proto.cataloging.Catalog.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.cataloging.CatalogList}
 */
proto.dlkit.proto.cataloging.CatalogList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogList;
  return proto.dlkit.proto.cataloging.CatalogList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogList}
 */
proto.dlkit.proto.cataloging.CatalogList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.Catalog;
      reader.readMessage(value,proto.dlkit.proto.cataloging.Catalog.deserializeBinaryFromReader);
      msg.addCatalogs(value);
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
proto.dlkit.proto.cataloging.CatalogList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.Catalog.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Catalog catalogs = 1;
 * @return {!Array.<!proto.dlkit.proto.cataloging.Catalog>}
 */
proto.dlkit.proto.cataloging.CatalogList.prototype.getCatalogsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.cataloging.Catalog>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.cataloging.Catalog, 1));
};


/** @param {!Array.<!proto.dlkit.proto.cataloging.Catalog>} value */
proto.dlkit.proto.cataloging.CatalogList.prototype.setCatalogsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.cataloging.Catalog=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.cataloging.Catalog}
 */
proto.dlkit.proto.cataloging.CatalogList.prototype.addCatalogs = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.cataloging.Catalog, opt_index);
};


proto.dlkit.proto.cataloging.CatalogList.prototype.clearCatalogsList = function() {
  this.setCatalogsList([]);
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
proto.dlkit.proto.cataloging.CatalogNode = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogNode, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogNode.displayName = 'proto.dlkit.proto.cataloging.CatalogNode';
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
proto.dlkit.proto.cataloging.CatalogNode.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogNode.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogNode} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogNode.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CatalogNode}
 */
proto.dlkit.proto.cataloging.CatalogNode.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogNode;
  return proto.dlkit.proto.cataloging.CatalogNode.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogNode} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogNode}
 */
proto.dlkit.proto.cataloging.CatalogNode.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CatalogNode.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogNode.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogNode} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogNode.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CatalogNodeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.cataloging.CatalogNodeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CatalogNodeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CatalogNodeList.displayName = 'proto.dlkit.proto.cataloging.CatalogNodeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.cataloging.CatalogNodeList.repeatedFields_ = [1];



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
proto.dlkit.proto.cataloging.CatalogNodeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CatalogNodeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CatalogNodeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogNodeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogNodesList: jspb.Message.toObjectList(msg.getCatalogNodesList(),
    proto.dlkit.proto.cataloging.CatalogNode.toObject, includeInstance)
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
 * @return {!proto.dlkit.proto.cataloging.CatalogNodeList}
 */
proto.dlkit.proto.cataloging.CatalogNodeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CatalogNodeList;
  return proto.dlkit.proto.cataloging.CatalogNodeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CatalogNodeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CatalogNodeList}
 */
proto.dlkit.proto.cataloging.CatalogNodeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogNode;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogNode.deserializeBinaryFromReader);
      msg.addCatalogNodes(value);
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
proto.dlkit.proto.cataloging.CatalogNodeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CatalogNodeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CatalogNodeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CatalogNodeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogNodesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogNode.serializeBinaryToWriter
    );
  }
};


/**
 * repeated CatalogNode catalog_nodes = 1;
 * @return {!Array.<!proto.dlkit.proto.cataloging.CatalogNode>}
 */
proto.dlkit.proto.cataloging.CatalogNodeList.prototype.getCatalogNodesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.cataloging.CatalogNode>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.cataloging.CatalogNode, 1));
};


/** @param {!Array.<!proto.dlkit.proto.cataloging.CatalogNode>} value */
proto.dlkit.proto.cataloging.CatalogNodeList.prototype.setCatalogNodesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.cataloging.CatalogNode=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.cataloging.CatalogNode}
 */
proto.dlkit.proto.cataloging.CatalogNodeList.prototype.addCatalogNodes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.cataloging.CatalogNode, opt_index);
};


proto.dlkit.proto.cataloging.CatalogNodeList.prototype.clearCatalogNodesList = function() {
  this.setCatalogNodesList([]);
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
proto.dlkit.proto.cataloging.CanLookupCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanLookupCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanLookupCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.CanLookupCatalogsReply';
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
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanLookupCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanLookupCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanLookupCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanLookupCatalogsReply;
  return proto.dlkit.proto.cataloging.CanLookupCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanLookupCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanLookupCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupCatalogs(value);
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
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanLookupCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanLookupCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.prototype.getCanLookupCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanLookupCatalogsReply.prototype.setCanLookupCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanLookupCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.CanLookupCatalogsRequest';
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
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanLookupCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanLookupCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanLookupCatalogsRequest;
  return proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanLookupCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanLookupCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanLookupCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanLookupCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.displayName = 'proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply';
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
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply}
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply;
  return proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply}
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.displayName = 'proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest';
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
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest}
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest;
  return proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest}
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UseComparativeCatalogViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.displayName = 'proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply';
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
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply}
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply;
  return proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply}
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.displayName = 'proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest';
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
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest}
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest;
  return proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest}
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UsePlenaryCatalogViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogReply';
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
proto.dlkit.proto.cataloging.GetCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalog: (f = msg.getCatalog()) && proto.dlkit.proto.cataloging.Catalog.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogReply}
 */
proto.dlkit.proto.cataloging.GetCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogReply;
  return proto.dlkit.proto.cataloging.GetCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogReply}
 */
proto.dlkit.proto.cataloging.GetCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.Catalog;
      reader.readMessage(value,proto.dlkit.proto.cataloging.Catalog.deserializeBinaryFromReader);
      msg.setCatalog(value);
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
proto.dlkit.proto.cataloging.GetCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalog();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.Catalog.serializeBinaryToWriter
    );
  }
};


/**
 * optional Catalog catalog = 1;
 * @return {?proto.dlkit.proto.cataloging.Catalog}
 */
proto.dlkit.proto.cataloging.GetCatalogReply.prototype.getCatalog = function() {
  return /** @type{?proto.dlkit.proto.cataloging.Catalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.Catalog, 1));
};


/** @param {?proto.dlkit.proto.cataloging.Catalog|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogReply.prototype.setCatalog = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogReply.prototype.clearCatalog = function() {
  this.setCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogReply.prototype.hasCatalog = function() {
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
proto.dlkit.proto.cataloging.GetCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogRequest';
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
proto.dlkit.proto.cataloging.GetCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogRequest;
  return proto.dlkit.proto.cataloging.GetCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.GetCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.repeatedFields_ = [1];



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
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogIdsList: jspb.Message.toObjectList(msg.getCatalogIdsList(),
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addCatalogIds(value);
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
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id catalog_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.prototype.getCatalogIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.prototype.setCatalogIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.prototype.addCatalogIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.cataloging.GetCatalogsByIdsRequest.prototype.clearCatalogIdsList = function() {
  this.setCatalogIdsList([]);
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
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest';
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
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogGenusType: (f = msg.getCatalogGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCatalogGenusType(value);
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
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type catalog_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.prototype.getCatalogGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.prototype.setCatalogGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.prototype.clearCatalogGenusType = function() {
  this.setCatalogGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogsByGenusTypeRequest.prototype.hasCatalogGenusType = function() {
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
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest';
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
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogGenusType: (f = msg.getCatalogGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCatalogGenusType(value);
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
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type catalog_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.prototype.getCatalogGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.prototype.setCatalogGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.prototype.clearCatalogGenusType = function() {
  this.setCatalogGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogsByParentGenusTypeRequest.prototype.hasCatalogGenusType = function() {
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
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest';
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
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogRecordType: (f = msg.getCatalogRecordType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCatalogRecordType(value);
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
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogRecordType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type catalog_record_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.prototype.getCatalogRecordType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.prototype.setCatalogRecordType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.prototype.clearCatalogRecordType = function() {
  this.setCatalogRecordType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogsByRecordTypeRequest.prototype.hasCatalogRecordType = function() {
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
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest';
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
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogsByProviderRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.cataloging.GetCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsRequest';
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
proto.dlkit.proto.cataloging.GetCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CanSearchCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanSearchCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanSearchCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.CanSearchCatalogsReply';
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
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanSearchCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanSearchCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canSearchCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanSearchCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanSearchCatalogsReply;
  return proto.dlkit.proto.cataloging.CanSearchCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanSearchCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanSearchCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanSearchCatalogs(value);
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
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanSearchCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanSearchCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanSearchCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_search_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.prototype.getCanSearchCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanSearchCatalogsReply.prototype.setCanSearchCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanSearchCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.CanSearchCatalogsRequest';
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
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanSearchCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanSearchCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanSearchCatalogsRequest;
  return proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanSearchCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanSearchCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanSearchCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanSearchCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogQueryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogQueryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogQueryReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogQueryReply';
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
proto.dlkit.proto.cataloging.GetCatalogQueryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogQueryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogQueryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogQuery: (f = msg.getCatalogQuery()) && proto.dlkit.proto.cataloging.CatalogQuery.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogQueryReply}
 */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogQueryReply;
  return proto.dlkit.proto.cataloging.GetCatalogQueryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogQueryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogQueryReply}
 */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogQuery;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogQuery.deserializeBinaryFromReader);
      msg.setCatalogQuery(value);
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
proto.dlkit.proto.cataloging.GetCatalogQueryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogQueryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogQueryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogQuery catalog_query = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogQuery}
 */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.prototype.getCatalogQuery = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogQuery, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogQuery|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.prototype.setCatalogQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogQueryReply.prototype.clearCatalogQuery = function() {
  this.setCatalogQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogQueryReply.prototype.hasCatalogQuery = function() {
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
proto.dlkit.proto.cataloging.GetCatalogQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogQueryRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogQueryRequest';
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
proto.dlkit.proto.cataloging.GetCatalogQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogQueryRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogQueryRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogQueryRequest;
  return proto.dlkit.proto.cataloging.GetCatalogQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogQueryRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogQueryRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest';
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
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogQuery: (f = msg.getCatalogQuery()) && proto.dlkit.proto.cataloging.CatalogQuery.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest;
  return proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogQuery;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogQuery.deserializeBinaryFromReader);
      msg.setCatalogQuery(value);
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
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogQuery catalog_query = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogQuery}
 */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.prototype.getCatalogQuery = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogQuery, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogQuery|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.prototype.setCatalogQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.prototype.clearCatalogQuery = function() {
  this.setCatalogQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogsByQueryRequest.prototype.hasCatalogQuery = function() {
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
proto.dlkit.proto.cataloging.CanCreateCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanCreateCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanCreateCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.CanCreateCatalogsReply';
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
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanCreateCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanCreateCatalogsReply;
  return proto.dlkit.proto.cataloging.CanCreateCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateCatalogs(value);
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
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanCreateCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.prototype.getCanCreateCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanCreateCatalogsReply.prototype.setCanCreateCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanCreateCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.CanCreateCatalogsRequest';
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
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanCreateCatalogsRequest;
  return proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.displayName = 'proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply';
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
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateCatalogWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply;
  return proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateCatalogWithRecordTypes(value);
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
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateCatalogWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_catalog_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.prototype.getCanCreateCatalogWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesReply.prototype.setCanCreateCatalogWithRecordTypes = function(value) {
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
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.displayName = 'proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.repeatedFields_ = [1];



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
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogRecordTypesList: jspb.Message.toObjectList(msg.getCatalogRecordTypesList(),
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
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest;
  return proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addCatalogRecordTypes(value);
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
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type catalog_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.prototype.getCatalogRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.prototype.setCatalogRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.prototype.addCatalogRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.cataloging.CanCreateCatalogWithRecordTypesRequest.prototype.clearCatalogRecordTypesList = function() {
  this.setCatalogRecordTypesList([]);
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
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply';
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
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogForm: (f = msg.getCatalogForm()) && proto.dlkit.proto.cataloging.CatalogForm.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply;
  return proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogForm;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogForm.deserializeBinaryFromReader);
      msg.setCatalogForm(value);
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
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogForm catalog_form = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogForm}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.prototype.getCatalogForm = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogForm, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogForm|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.prototype.setCatalogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.prototype.clearCatalogForm = function() {
  this.setCatalogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateReply.prototype.hasCatalogForm = function() {
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
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.repeatedFields_ = [1];



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
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogRecordTypesList: jspb.Message.toObjectList(msg.getCatalogRecordTypesList(),
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest;
  return proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addCatalogRecordTypes(value);
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
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type catalog_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.prototype.getCatalogRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.prototype.setCatalogRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.prototype.addCatalogRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.cataloging.GetCatalogFormForCreateRequest.prototype.clearCatalogRecordTypesList = function() {
  this.setCatalogRecordTypesList([]);
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
proto.dlkit.proto.cataloging.CreateCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CreateCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CreateCatalogReply.displayName = 'proto.dlkit.proto.cataloging.CreateCatalogReply';
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
proto.dlkit.proto.cataloging.CreateCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CreateCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CreateCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CreateCatalogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalog: (f = msg.getCatalog()) && proto.dlkit.proto.cataloging.Catalog.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.CreateCatalogReply}
 */
proto.dlkit.proto.cataloging.CreateCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CreateCatalogReply;
  return proto.dlkit.proto.cataloging.CreateCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CreateCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CreateCatalogReply}
 */
proto.dlkit.proto.cataloging.CreateCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.Catalog;
      reader.readMessage(value,proto.dlkit.proto.cataloging.Catalog.deserializeBinaryFromReader);
      msg.setCatalog(value);
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
proto.dlkit.proto.cataloging.CreateCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CreateCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CreateCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CreateCatalogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalog();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.Catalog.serializeBinaryToWriter
    );
  }
};


/**
 * optional Catalog catalog = 1;
 * @return {?proto.dlkit.proto.cataloging.Catalog}
 */
proto.dlkit.proto.cataloging.CreateCatalogReply.prototype.getCatalog = function() {
  return /** @type{?proto.dlkit.proto.cataloging.Catalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.Catalog, 1));
};


/** @param {?proto.dlkit.proto.cataloging.Catalog|undefined} value */
proto.dlkit.proto.cataloging.CreateCatalogReply.prototype.setCatalog = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.CreateCatalogReply.prototype.clearCatalog = function() {
  this.setCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.CreateCatalogReply.prototype.hasCatalog = function() {
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
proto.dlkit.proto.cataloging.CreateCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CreateCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CreateCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.CreateCatalogRequest';
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
proto.dlkit.proto.cataloging.CreateCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CreateCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CreateCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CreateCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogForm: (f = msg.getCatalogForm()) && proto.dlkit.proto.cataloging.CatalogForm.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.CreateCatalogRequest}
 */
proto.dlkit.proto.cataloging.CreateCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CreateCatalogRequest;
  return proto.dlkit.proto.cataloging.CreateCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CreateCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CreateCatalogRequest}
 */
proto.dlkit.proto.cataloging.CreateCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogForm;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogForm.deserializeBinaryFromReader);
      msg.setCatalogForm(value);
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
proto.dlkit.proto.cataloging.CreateCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CreateCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CreateCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CreateCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogForm catalog_form = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogForm}
 */
proto.dlkit.proto.cataloging.CreateCatalogRequest.prototype.getCatalogForm = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogForm, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogForm|undefined} value */
proto.dlkit.proto.cataloging.CreateCatalogRequest.prototype.setCatalogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.CreateCatalogRequest.prototype.clearCatalogForm = function() {
  this.setCatalogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.CreateCatalogRequest.prototype.hasCatalogForm = function() {
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
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanUpdateCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.CanUpdateCatalogsReply';
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
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanUpdateCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanUpdateCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanUpdateCatalogsReply;
  return proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanUpdateCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanUpdateCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateCatalogs(value);
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
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanUpdateCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.prototype.getCanUpdateCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanUpdateCatalogsReply.prototype.setCanUpdateCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest';
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
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest;
  return proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanUpdateCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply';
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
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogForm: (f = msg.getCatalogForm()) && proto.dlkit.proto.cataloging.CatalogForm.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply;
  return proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogForm;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogForm.deserializeBinaryFromReader);
      msg.setCatalogForm(value);
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
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogForm catalog_form = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogForm}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.prototype.getCatalogForm = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogForm, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogForm|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.prototype.setCatalogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.prototype.clearCatalogForm = function() {
  this.setCatalogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateReply.prototype.hasCatalogForm = function() {
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
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest';
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
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest;
  return proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogFormForUpdateRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.UpdateCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.UpdateCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.UpdateCatalogReply.displayName = 'proto.dlkit.proto.cataloging.UpdateCatalogReply';
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
proto.dlkit.proto.cataloging.UpdateCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.UpdateCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.UpdateCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UpdateCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.UpdateCatalogReply}
 */
proto.dlkit.proto.cataloging.UpdateCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.UpdateCatalogReply;
  return proto.dlkit.proto.cataloging.UpdateCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.UpdateCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.UpdateCatalogReply}
 */
proto.dlkit.proto.cataloging.UpdateCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.UpdateCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.UpdateCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.UpdateCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UpdateCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.UpdateCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.UpdateCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.UpdateCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.UpdateCatalogRequest';
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
proto.dlkit.proto.cataloging.UpdateCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.UpdateCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.UpdateCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogForm: (f = msg.getCatalogForm()) && proto.dlkit.proto.cataloging.CatalogForm.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.UpdateCatalogRequest}
 */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.UpdateCatalogRequest;
  return proto.dlkit.proto.cataloging.UpdateCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.UpdateCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.UpdateCatalogRequest}
 */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogForm;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogForm.deserializeBinaryFromReader);
      msg.setCatalogForm(value);
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
proto.dlkit.proto.cataloging.UpdateCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.UpdateCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.UpdateCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogForm catalog_form = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogForm}
 */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.prototype.getCatalogForm = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogForm, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogForm|undefined} value */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.prototype.setCatalogForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.UpdateCatalogRequest.prototype.clearCatalogForm = function() {
  this.setCatalogForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.UpdateCatalogRequest.prototype.hasCatalogForm = function() {
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
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanDeleteCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.CanDeleteCatalogsReply';
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
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanDeleteCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanDeleteCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanDeleteCatalogsReply;
  return proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanDeleteCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanDeleteCatalogsReply}
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteCatalogs(value);
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
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanDeleteCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.prototype.getCanDeleteCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanDeleteCatalogsReply.prototype.setCanDeleteCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest';
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
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest;
  return proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest}
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanDeleteCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.DeleteCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.DeleteCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.DeleteCatalogReply.displayName = 'proto.dlkit.proto.cataloging.DeleteCatalogReply';
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
proto.dlkit.proto.cataloging.DeleteCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.DeleteCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.DeleteCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.DeleteCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.DeleteCatalogReply}
 */
proto.dlkit.proto.cataloging.DeleteCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.DeleteCatalogReply;
  return proto.dlkit.proto.cataloging.DeleteCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.DeleteCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.DeleteCatalogReply}
 */
proto.dlkit.proto.cataloging.DeleteCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.DeleteCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.DeleteCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.DeleteCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.DeleteCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.DeleteCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.DeleteCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.DeleteCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.DeleteCatalogRequest';
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
proto.dlkit.proto.cataloging.DeleteCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.DeleteCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.DeleteCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.DeleteCatalogRequest}
 */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.DeleteCatalogRequest;
  return proto.dlkit.proto.cataloging.DeleteCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.DeleteCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.DeleteCatalogRequest}
 */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.DeleteCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.DeleteCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.DeleteCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.DeleteCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.DeleteCatalogRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.displayName = 'proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply';
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
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageCatalogAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply}
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply;
  return proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply}
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageCatalogAliases(value);
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
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageCatalogAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_catalog_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.prototype.getCanManageCatalogAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesReply.prototype.setCanManageCatalogAliases = function(value) {
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
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.displayName = 'proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest';
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
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest}
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest;
  return proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest}
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanManageCatalogAliasesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.AliasCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.AliasCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.AliasCatalogReply.displayName = 'proto.dlkit.proto.cataloging.AliasCatalogReply';
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
proto.dlkit.proto.cataloging.AliasCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.AliasCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.AliasCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AliasCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.AliasCatalogReply}
 */
proto.dlkit.proto.cataloging.AliasCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.AliasCatalogReply;
  return proto.dlkit.proto.cataloging.AliasCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.AliasCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.AliasCatalogReply}
 */
proto.dlkit.proto.cataloging.AliasCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.AliasCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.AliasCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.AliasCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AliasCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.AliasCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.AliasCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.AliasCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.AliasCatalogRequest';
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
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.AliasCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.AliasCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.AliasCatalogRequest}
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.AliasCatalogRequest;
  return proto.dlkit.proto.cataloging.AliasCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.AliasCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.AliasCatalogRequest}
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.AliasCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.AliasCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getCatalogId();
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
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.AliasCatalogRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply';
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply;
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdReply.prototype.hasId = function() {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest';
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest;
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyIdRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogHierarchyReply';
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyReply}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogHierarchyReply;
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyReply}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.prototype.getHierarchy = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Hierarchy} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Hierarchy, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Hierarchy|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.prototype.setHierarchy = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.prototype.clearHierarchy = function() {
  this.setHierarchy(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyReply.prototype.hasHierarchy = function() {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest';
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest;
  return proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.displayName = 'proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply';
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
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAccessCatalogHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply}
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply;
  return proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply}
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAccessCatalogHierarchy(value);
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
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAccessCatalogHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_access_catalog_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.prototype.getCanAccessCatalogHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyReply.prototype.setCanAccessCatalogHierarchy = function(value) {
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
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.displayName = 'proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest';
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
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest}
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest;
  return proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest}
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanAccessCatalogHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.displayName = 'proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest';
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
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest}
 */
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest;
  return proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest}
 */
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetRootCatalogIdsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetRootCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetRootCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetRootCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.GetRootCatalogsRequest';
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
proto.dlkit.proto.cataloging.GetRootCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetRootCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetRootCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetRootCatalogsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetRootCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetRootCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetRootCatalogsRequest;
  return proto.dlkit.proto.cataloging.GetRootCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetRootCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetRootCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetRootCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetRootCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetRootCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetRootCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetRootCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.HasParentCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.HasParentCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.HasParentCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.HasParentCatalogsReply';
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
proto.dlkit.proto.cataloging.HasParentCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.HasParentCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.HasParentCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasParentCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasParentCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.HasParentCatalogsReply}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.HasParentCatalogsReply;
  return proto.dlkit.proto.cataloging.HasParentCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.HasParentCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.HasParentCatalogsReply}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasParentCatalogs(value);
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
proto.dlkit.proto.cataloging.HasParentCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.HasParentCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.HasParentCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasParentCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasParentCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_parent_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsReply.prototype.getHasParentCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.HasParentCatalogsReply.prototype.setHasParentCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.HasParentCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.HasParentCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.HasParentCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.HasParentCatalogsRequest';
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
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.HasParentCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.HasParentCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.HasParentCatalogsRequest}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.HasParentCatalogsRequest;
  return proto.dlkit.proto.cataloging.HasParentCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.HasParentCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.HasParentCatalogsRequest}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.HasParentCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.HasParentCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.HasParentCatalogsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.HasParentCatalogsRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.IsParentOfCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsParentOfCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsParentOfCatalogReply.displayName = 'proto.dlkit.proto.cataloging.IsParentOfCatalogReply';
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
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsParentOfCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsParentOfCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isParentOfCatalog: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.IsParentOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsParentOfCatalogReply;
  return proto.dlkit.proto.cataloging.IsParentOfCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsParentOfCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsParentOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsParentOfCatalog(value);
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
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsParentOfCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsParentOfCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsParentOfCatalog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_parent_of_catalog = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.prototype.getIsParentOfCatalog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.IsParentOfCatalogReply.prototype.setIsParentOfCatalog = function(value) {
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
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsParentOfCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.IsParentOfCatalogRequest';
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
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsParentOfCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.cataloging.IsParentOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsParentOfCatalogRequest;
  return proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsParentOfCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsParentOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 2:
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
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsParentOfCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsParentOfCatalogRequest.prototype.hasId = function() {
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
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.displayName = 'proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest';
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
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest}
 */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest;
  return proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest}
 */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetParentCatalogIdsRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.GetParentCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetParentCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetParentCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.GetParentCatalogsRequest';
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
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetParentCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetParentCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetParentCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetParentCatalogsRequest;
  return proto.dlkit.proto.cataloging.GetParentCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetParentCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetParentCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetParentCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetParentCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetParentCatalogsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetParentCatalogsRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.displayName = 'proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply';
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
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isAncestorOfCatalog: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply;
  return proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsAncestorOfCatalog(value);
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
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsAncestorOfCatalog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_ancestor_of_catalog = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.prototype.getIsAncestorOfCatalog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogReply.prototype.setIsAncestorOfCatalog = function(value) {
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
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest';
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
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest;
  return proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 2:
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
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsAncestorOfCatalogRequest.prototype.hasId = function() {
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
proto.dlkit.proto.cataloging.HasChildCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.HasChildCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.HasChildCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.HasChildCatalogsReply';
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
proto.dlkit.proto.cataloging.HasChildCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.HasChildCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.HasChildCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasChildCatalogsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasChildCatalogs: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.HasChildCatalogsReply}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.HasChildCatalogsReply;
  return proto.dlkit.proto.cataloging.HasChildCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.HasChildCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.HasChildCatalogsReply}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasChildCatalogs(value);
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
proto.dlkit.proto.cataloging.HasChildCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.HasChildCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.HasChildCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasChildCatalogsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasChildCatalogs();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_child_catalogs = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsReply.prototype.getHasChildCatalogs = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.HasChildCatalogsReply.prototype.setHasChildCatalogs = function(value) {
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
proto.dlkit.proto.cataloging.HasChildCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.HasChildCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.HasChildCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.HasChildCatalogsRequest';
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
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.HasChildCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.HasChildCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.HasChildCatalogsRequest}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.HasChildCatalogsRequest;
  return proto.dlkit.proto.cataloging.HasChildCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.HasChildCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.HasChildCatalogsRequest}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.HasChildCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.HasChildCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.HasChildCatalogsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.HasChildCatalogsRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.IsChildOfCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsChildOfCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsChildOfCatalogReply.displayName = 'proto.dlkit.proto.cataloging.IsChildOfCatalogReply';
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
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsChildOfCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsChildOfCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isChildOfCatalog: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.IsChildOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsChildOfCatalogReply;
  return proto.dlkit.proto.cataloging.IsChildOfCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsChildOfCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsChildOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsChildOfCatalog(value);
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
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsChildOfCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsChildOfCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsChildOfCatalog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_child_of_catalog = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.prototype.getIsChildOfCatalog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.IsChildOfCatalogReply.prototype.setIsChildOfCatalog = function(value) {
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
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsChildOfCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.IsChildOfCatalogRequest';
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
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsChildOfCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.cataloging.IsChildOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsChildOfCatalogRequest;
  return proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsChildOfCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsChildOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 2:
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
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsChildOfCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsChildOfCatalogRequest.prototype.hasId = function() {
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
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.displayName = 'proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest';
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
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest}
 */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest;
  return proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest}
 */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetChildCatalogIdsRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.GetChildCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetChildCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetChildCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.GetChildCatalogsRequest';
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
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetChildCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetChildCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetChildCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetChildCatalogsRequest;
  return proto.dlkit.proto.cataloging.GetChildCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetChildCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetChildCatalogsRequest}
 */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetChildCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetChildCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetChildCatalogsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetChildCatalogsRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.displayName = 'proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply';
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
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isDescendantOfCatalog: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply;
  return proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsDescendantOfCatalog(value);
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
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsDescendantOfCatalog();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_descendant_of_catalog = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.prototype.getIsDescendantOfCatalog = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogReply.prototype.setIsDescendantOfCatalog = function(value) {
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
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest';
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
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest;
  return proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 2:
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
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.IsDescendantOfCatalogRequest.prototype.hasId = function() {
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply';
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply;
  return proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.prototype.getNode = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Node} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Node, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Node|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.prototype.setNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.prototype.clearNode = function() {
  this.setNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsReply.prototype.hasNode = function() {
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest';
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    descendantLevels: jspb.Message.getFieldWithDefault(msg, 3, 0),
    includeSiblings: jspb.Message.getFieldWithDefault(msg, 4, false)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest;
  return proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setDescendantLevels(value);
      break;
    case 4:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIncludeSiblings(value);
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
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAncestorLevels();
  if (f !== 0) {
    writer.writeSint32(
      1,
      f
    );
  }
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getDescendantLevels();
  if (f !== 0) {
    writer.writeSint32(
      3,
      f
    );
  }
  f = message.getIncludeSiblings();
  if (f) {
    writer.writeBool(
      4,
      f
    );
  }
};


/**
 * optional sint32 ancestor_levels = 1;
 * @return {number}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional sint32 descendant_levels = 3;
 * @return {number}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/** @param {number} value */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional bool include_siblings = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.GetCatalogNodeIdsRequest.prototype.setIncludeSiblings = function(value) {
  jspb.Message.setProto3BooleanField(this, 4, value);
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
proto.dlkit.proto.cataloging.GetCatalogNodesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogNodesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogNodesReply.displayName = 'proto.dlkit.proto.cataloging.GetCatalogNodesReply';
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
proto.dlkit.proto.cataloging.GetCatalogNodesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogNodesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogNode: (f = msg.getCatalogNode()) && proto.dlkit.proto.cataloging.CatalogNode.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodesReply}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogNodesReply;
  return proto.dlkit.proto.cataloging.GetCatalogNodesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodesReply}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.cataloging.CatalogNode;
      reader.readMessage(value,proto.dlkit.proto.cataloging.CatalogNode.deserializeBinaryFromReader);
      msg.setCatalogNode(value);
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
proto.dlkit.proto.cataloging.GetCatalogNodesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogNodesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogNode();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.cataloging.CatalogNode.serializeBinaryToWriter
    );
  }
};


/**
 * optional CatalogNode catalog_node = 1;
 * @return {?proto.dlkit.proto.cataloging.CatalogNode}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.prototype.getCatalogNode = function() {
  return /** @type{?proto.dlkit.proto.cataloging.CatalogNode} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.cataloging.CatalogNode, 1));
};


/** @param {?proto.dlkit.proto.cataloging.CatalogNode|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.prototype.setCatalogNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.GetCatalogNodesReply.prototype.clearCatalogNode = function() {
  this.setCatalogNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesReply.prototype.hasCatalogNode = function() {
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
proto.dlkit.proto.cataloging.GetCatalogNodesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.GetCatalogNodesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.GetCatalogNodesRequest.displayName = 'proto.dlkit.proto.cataloging.GetCatalogNodesRequest';
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
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.GetCatalogNodesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    descendantLevels: jspb.Message.getFieldWithDefault(msg, 3, 0),
    includeSiblings: jspb.Message.getFieldWithDefault(msg, 4, false)
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
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodesRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.GetCatalogNodesRequest;
  return proto.dlkit.proto.cataloging.GetCatalogNodesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.GetCatalogNodesRequest}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readSint32());
      msg.setDescendantLevels(value);
      break;
    case 4:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIncludeSiblings(value);
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
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.GetCatalogNodesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.GetCatalogNodesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAncestorLevels();
  if (f !== 0) {
    writer.writeSint32(
      1,
      f
    );
  }
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getDescendantLevels();
  if (f !== 0) {
    writer.writeSint32(
      3,
      f
    );
  }
  f = message.getIncludeSiblings();
  if (f) {
    writer.writeBool(
      4,
      f
    );
  }
};


/**
 * optional sint32 ancestor_levels = 1;
 * @return {number}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional sint32 descendant_levels = 3;
 * @return {number}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/** @param {number} value */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional bool include_siblings = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.GetCatalogNodesRequest.prototype.setIncludeSiblings = function(value) {
  jspb.Message.setProto3BooleanField(this, 4, value);
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
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.displayName = 'proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply';
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
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canModifyCatalogHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
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
 * @return {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply}
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply;
  return proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply}
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanModifyCatalogHierarchy(value);
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
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanModifyCatalogHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_modify_catalog_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.prototype.getCanModifyCatalogHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyReply.prototype.setCanModifyCatalogHierarchy = function(value) {
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
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.displayName = 'proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest';
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
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest}
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest;
  return proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest}
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.CanModifyCatalogHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.AddRootCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.AddRootCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.AddRootCatalogReply.displayName = 'proto.dlkit.proto.cataloging.AddRootCatalogReply';
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
proto.dlkit.proto.cataloging.AddRootCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.AddRootCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.AddRootCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddRootCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.AddRootCatalogReply}
 */
proto.dlkit.proto.cataloging.AddRootCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.AddRootCatalogReply;
  return proto.dlkit.proto.cataloging.AddRootCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.AddRootCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.AddRootCatalogReply}
 */
proto.dlkit.proto.cataloging.AddRootCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.AddRootCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.AddRootCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.AddRootCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddRootCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.AddRootCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.AddRootCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.AddRootCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.AddRootCatalogRequest';
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
proto.dlkit.proto.cataloging.AddRootCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.AddRootCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.AddRootCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.AddRootCatalogRequest}
 */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.AddRootCatalogRequest;
  return proto.dlkit.proto.cataloging.AddRootCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.AddRootCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.AddRootCatalogRequest}
 */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.AddRootCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.AddRootCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.AddRootCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.AddRootCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.AddRootCatalogRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.RemoveRootCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.RemoveRootCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.RemoveRootCatalogReply.displayName = 'proto.dlkit.proto.cataloging.RemoveRootCatalogReply';
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
proto.dlkit.proto.cataloging.RemoveRootCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.RemoveRootCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.RemoveRootCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.RemoveRootCatalogReply}
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.RemoveRootCatalogReply;
  return proto.dlkit.proto.cataloging.RemoveRootCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.RemoveRootCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.RemoveRootCatalogReply}
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.RemoveRootCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.RemoveRootCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.RemoveRootCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.RemoveRootCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.RemoveRootCatalogRequest';
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
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.RemoveRootCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.RemoveRootCatalogRequest}
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.RemoveRootCatalogRequest;
  return proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.RemoveRootCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.RemoveRootCatalogRequest}
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.RemoveRootCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.RemoveRootCatalogRequest.prototype.hasCatalogId = function() {
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
proto.dlkit.proto.cataloging.AddChildCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.AddChildCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.AddChildCatalogReply.displayName = 'proto.dlkit.proto.cataloging.AddChildCatalogReply';
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
proto.dlkit.proto.cataloging.AddChildCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.AddChildCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.AddChildCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddChildCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.AddChildCatalogReply}
 */
proto.dlkit.proto.cataloging.AddChildCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.AddChildCatalogReply;
  return proto.dlkit.proto.cataloging.AddChildCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.AddChildCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.AddChildCatalogReply}
 */
proto.dlkit.proto.cataloging.AddChildCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.AddChildCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.AddChildCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.AddChildCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddChildCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.AddChildCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.AddChildCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.AddChildCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.AddChildCatalogRequest';
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
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.AddChildCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.AddChildCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    childId: (f = msg.getChildId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.AddChildCatalogRequest}
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.AddChildCatalogRequest;
  return proto.dlkit.proto.cataloging.AddChildCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.AddChildCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.AddChildCatalogRequest}
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setChildId(value);
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
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.AddChildCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.AddChildCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getChildId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id child_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.AddChildCatalogRequest.prototype.hasChildId = function() {
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
proto.dlkit.proto.cataloging.RemoveChildCatalogReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.RemoveChildCatalogReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.RemoveChildCatalogReply.displayName = 'proto.dlkit.proto.cataloging.RemoveChildCatalogReply';
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
proto.dlkit.proto.cataloging.RemoveChildCatalogReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.RemoveChildCatalogReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogReply}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.RemoveChildCatalogReply;
  return proto.dlkit.proto.cataloging.RemoveChildCatalogReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogReply}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.RemoveChildCatalogReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.RemoveChildCatalogReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.RemoveChildCatalogRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.displayName = 'proto.dlkit.proto.cataloging.RemoveChildCatalogRequest';
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
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    childId: (f = msg.getChildId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogRequest}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.RemoveChildCatalogRequest;
  return proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogRequest}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setChildId(value);
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
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getChildId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id child_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogRequest.prototype.hasChildId = function() {
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
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.RemoveChildCatalogsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.displayName = 'proto.dlkit.proto.cataloging.RemoveChildCatalogsReply';
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
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogsReply}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.RemoveChildCatalogsReply;
  return proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogsReply}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.displayName = 'proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest';
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
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    catalogId: (f = msg.getCatalogId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
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
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest;
  return proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCatalogId(value);
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
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCatalogId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id catalog_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.prototype.getCatalogId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.prototype.setCatalogId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.prototype.clearCatalogId = function() {
  this.setCatalogId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.cataloging.RemoveChildCatalogsRequest.prototype.hasCatalogId = function() {
  return jspb.Message.getField(this, 1) != null;
};


goog.object.extend(exports, proto.dlkit.proto.cataloging);
