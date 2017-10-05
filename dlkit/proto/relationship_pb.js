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
goog.exportSymbol('proto.dlkit.proto.relationship.AddChildFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AddChildFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AddRootFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AddRootFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AliasFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AliasFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AliasRelationshipReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.AliasRelationshipRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateRelationshipsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanCreateRelationshipsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanDeleteFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanDeleteFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanDeleteRelationshipsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanLookupFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanLookupFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanLookupRelationshipsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanLookupRelationshipsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanManageFamilyAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanSearchRelationshipsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanSearchRelationshipsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanUpdateFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanUpdateFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanUpdateRelationshipsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CreateFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CreateFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CreateRelationshipReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.CreateRelationshipRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.DeleteFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.DeleteFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.DeleteRelationshipReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.DeleteRelationshipRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.Family', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilyForm', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilyList', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilyNode', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilyNodeList', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilyQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilyQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilySearch', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilySearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.FamilySearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetChildFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetChildFamilyIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamiliesByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamiliesByProviderRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyNodeIdsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyNodesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyNodesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetParentFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetParentFamilyIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipQueryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRelationshipsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRootFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.GetRootFamilyIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.HasChildFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.HasChildFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.HasParentFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.HasParentFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsAncestorOfFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsChildOfFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsChildOfFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsDescendantOfFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsParentOfFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.IsParentOfFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.Relationship', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipForm', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipList', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RelationshipSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RemoveChildFamiliesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RemoveChildFamiliesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RemoveChildFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RemoveChildFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RemoveRootFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.RemoveRootFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UpdateFamilyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UpdateFamilyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UpdateRelationshipReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UpdateRelationshipRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseComparativeFamilyViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseFederatedFamilyViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest', null, global);

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.Relationship = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.Relationship, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.Relationship.displayName = 'proto.dlkit.proto.relationship.Relationship';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.Relationship.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.Relationship.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.Relationship} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.Relationship.toObject = function(includeInstance, msg) {
  var f, obj = {
    destination: (f = msg.getDestination()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    family: (f = msg.getFamily()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    source: (f = msg.getSource()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.Relationship}
 */
proto.dlkit.proto.relationship.Relationship.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.Relationship;
  return proto.dlkit.proto.relationship.Relationship.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.Relationship} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.Relationship}
 */
proto.dlkit.proto.relationship.Relationship.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestination(value);
      break;
    case 2:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setFamily(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSource(value);
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
proto.dlkit.proto.relationship.Relationship.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.Relationship.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.Relationship} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.Relationship.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestination();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFamily();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getSource();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.Relationship.prototype.getDestination = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.Relationship.prototype.setDestination = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.Relationship.prototype.clearDestination = function() {
  this.setDestination(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Relationship.prototype.hasDestination = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.proto.osid.OsidCatalog family = 2;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.relationship.Relationship.prototype.getFamily = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 2));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.relationship.Relationship.prototype.setFamily = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.Relationship.prototype.clearFamily = function() {
  this.setFamily(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Relationship.prototype.hasFamily = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.Relationship.prototype.getSource = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.Relationship.prototype.setSource = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.Relationship.prototype.clearSource = function() {
  this.setSource(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Relationship.prototype.hasSource = function() {
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
proto.dlkit.proto.relationship.RelationshipQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipQuery.displayName = 'proto.dlkit.proto.relationship.RelationshipQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RelationshipQuery}
 */
proto.dlkit.proto.relationship.RelationshipQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipQuery;
  return proto.dlkit.proto.relationship.RelationshipQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipQuery}
 */
proto.dlkit.proto.relationship.RelationshipQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RelationshipQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RelationshipQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipQueryInspector.displayName = 'proto.dlkit.proto.relationship.RelationshipQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RelationshipQueryInspector}
 */
proto.dlkit.proto.relationship.RelationshipQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipQueryInspector;
  return proto.dlkit.proto.relationship.RelationshipQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipQueryInspector}
 */
proto.dlkit.proto.relationship.RelationshipQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RelationshipQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RelationshipForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipForm.displayName = 'proto.dlkit.proto.relationship.RelationshipForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RelationshipForm}
 */
proto.dlkit.proto.relationship.RelationshipForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipForm;
  return proto.dlkit.proto.relationship.RelationshipForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipForm}
 */
proto.dlkit.proto.relationship.RelationshipForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RelationshipForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RelationshipSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipSearchOrder.displayName = 'proto.dlkit.proto.relationship.RelationshipSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RelationshipSearchOrder}
 */
proto.dlkit.proto.relationship.RelationshipSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipSearchOrder;
  return proto.dlkit.proto.relationship.RelationshipSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipSearchOrder}
 */
proto.dlkit.proto.relationship.RelationshipSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RelationshipSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RelationshipSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipSearch.displayName = 'proto.dlkit.proto.relationship.RelationshipSearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RelationshipSearch}
 */
proto.dlkit.proto.relationship.RelationshipSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipSearch;
  return proto.dlkit.proto.relationship.RelationshipSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipSearch}
 */
proto.dlkit.proto.relationship.RelationshipSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RelationshipSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RelationshipSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipSearchResults.displayName = 'proto.dlkit.proto.relationship.RelationshipSearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RelationshipSearchResults}
 */
proto.dlkit.proto.relationship.RelationshipSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipSearchResults;
  return proto.dlkit.proto.relationship.RelationshipSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipSearchResults}
 */
proto.dlkit.proto.relationship.RelationshipSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RelationshipSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RelationshipList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.RelationshipList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.RelationshipList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RelationshipList.displayName = 'proto.dlkit.proto.relationship.RelationshipList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.RelationshipList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RelationshipList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RelationshipList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RelationshipList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipList.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipsList: jspb.Message.toObjectList(msg.getRelationshipsList(),
    proto.dlkit.proto.relationship.Relationship.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.RelationshipList}
 */
proto.dlkit.proto.relationship.RelationshipList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RelationshipList;
  return proto.dlkit.proto.relationship.RelationshipList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RelationshipList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RelationshipList}
 */
proto.dlkit.proto.relationship.RelationshipList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.Relationship;
      reader.readMessage(value,proto.dlkit.proto.relationship.Relationship.deserializeBinaryFromReader);
      msg.addRelationships(value);
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
proto.dlkit.proto.relationship.RelationshipList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RelationshipList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RelationshipList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RelationshipList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.relationship.Relationship.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Relationship relationships = 1;
 * @return {!Array.<!proto.dlkit.proto.relationship.Relationship>}
 */
proto.dlkit.proto.relationship.RelationshipList.prototype.getRelationshipsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.relationship.Relationship>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.relationship.Relationship, 1));
};


/** @param {!Array.<!proto.dlkit.proto.relationship.Relationship>} value */
proto.dlkit.proto.relationship.RelationshipList.prototype.setRelationshipsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.relationship.Relationship=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.relationship.Relationship}
 */
proto.dlkit.proto.relationship.RelationshipList.prototype.addRelationships = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.relationship.Relationship, opt_index);
};


proto.dlkit.proto.relationship.RelationshipList.prototype.clearRelationshipsList = function() {
  this.setRelationshipsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.Family = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.Family.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.Family, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.Family.displayName = 'proto.dlkit.proto.relationship.Family';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.Family.repeatedFields_ = [5];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.Family.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.Family.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.Family} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.Family.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.Family}
 */
proto.dlkit.proto.relationship.Family.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.Family;
  return proto.dlkit.proto.relationship.Family.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.Family} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.Family}
 */
proto.dlkit.proto.relationship.Family.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.Family.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.Family.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.Family} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.Family.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.Family.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.relationship.Family.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.Family.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Family.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.relationship.Family.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.relationship.Family.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.Family.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Family.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.Family.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.Family.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.Family.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Family.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.Family.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.Family.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.relationship.Family.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.Family.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 5;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.relationship.Family.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.relationship.Family.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.Family.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.relationship.Family.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.relationship.FamilyQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilyQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilyQuery.displayName = 'proto.dlkit.proto.relationship.FamilyQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilyQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilyQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilyQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilyQuery}
 */
proto.dlkit.proto.relationship.FamilyQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilyQuery;
  return proto.dlkit.proto.relationship.FamilyQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilyQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilyQuery}
 */
proto.dlkit.proto.relationship.FamilyQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilyQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilyQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilyQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilyQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilyQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilyQueryInspector.displayName = 'proto.dlkit.proto.relationship.FamilyQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilyQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilyQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilyQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilyQueryInspector}
 */
proto.dlkit.proto.relationship.FamilyQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilyQueryInspector;
  return proto.dlkit.proto.relationship.FamilyQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilyQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilyQueryInspector}
 */
proto.dlkit.proto.relationship.FamilyQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilyQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilyQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilyQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilyForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilyForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilyForm.displayName = 'proto.dlkit.proto.relationship.FamilyForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilyForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilyForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilyForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilyForm}
 */
proto.dlkit.proto.relationship.FamilyForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilyForm;
  return proto.dlkit.proto.relationship.FamilyForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilyForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilyForm}
 */
proto.dlkit.proto.relationship.FamilyForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilyForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilyForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilyForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilySearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilySearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilySearchOrder.displayName = 'proto.dlkit.proto.relationship.FamilySearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilySearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilySearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilySearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilySearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilySearchOrder}
 */
proto.dlkit.proto.relationship.FamilySearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilySearchOrder;
  return proto.dlkit.proto.relationship.FamilySearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilySearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilySearchOrder}
 */
proto.dlkit.proto.relationship.FamilySearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilySearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilySearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilySearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilySearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilySearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilySearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilySearch.displayName = 'proto.dlkit.proto.relationship.FamilySearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilySearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilySearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilySearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilySearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilySearch}
 */
proto.dlkit.proto.relationship.FamilySearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilySearch;
  return proto.dlkit.proto.relationship.FamilySearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilySearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilySearch}
 */
proto.dlkit.proto.relationship.FamilySearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilySearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilySearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilySearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilySearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilySearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilySearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilySearchResults.displayName = 'proto.dlkit.proto.relationship.FamilySearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilySearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilySearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilySearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilySearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilySearchResults}
 */
proto.dlkit.proto.relationship.FamilySearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilySearchResults;
  return proto.dlkit.proto.relationship.FamilySearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilySearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilySearchResults}
 */
proto.dlkit.proto.relationship.FamilySearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilySearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilySearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilySearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilySearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilyList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.FamilyList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilyList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilyList.displayName = 'proto.dlkit.proto.relationship.FamilyList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.FamilyList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilyList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilyList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilyList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyList.toObject = function(includeInstance, msg) {
  var f, obj = {
    familiesList: jspb.Message.toObjectList(msg.getFamiliesList(),
    proto.dlkit.proto.relationship.Family.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.FamilyList}
 */
proto.dlkit.proto.relationship.FamilyList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilyList;
  return proto.dlkit.proto.relationship.FamilyList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilyList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilyList}
 */
proto.dlkit.proto.relationship.FamilyList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.Family;
      reader.readMessage(value,proto.dlkit.proto.relationship.Family.deserializeBinaryFromReader);
      msg.addFamilies(value);
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
proto.dlkit.proto.relationship.FamilyList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilyList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilyList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamiliesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.relationship.Family.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Family families = 1;
 * @return {!Array.<!proto.dlkit.proto.relationship.Family>}
 */
proto.dlkit.proto.relationship.FamilyList.prototype.getFamiliesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.relationship.Family>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.relationship.Family, 1));
};


/** @param {!Array.<!proto.dlkit.proto.relationship.Family>} value */
proto.dlkit.proto.relationship.FamilyList.prototype.setFamiliesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.relationship.Family=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.relationship.Family}
 */
proto.dlkit.proto.relationship.FamilyList.prototype.addFamilies = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.relationship.Family, opt_index);
};


proto.dlkit.proto.relationship.FamilyList.prototype.clearFamiliesList = function() {
  this.setFamiliesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.FamilyNode = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilyNode, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilyNode.displayName = 'proto.dlkit.proto.relationship.FamilyNode';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilyNode.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilyNode.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilyNode} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyNode.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.FamilyNode}
 */
proto.dlkit.proto.relationship.FamilyNode.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilyNode;
  return proto.dlkit.proto.relationship.FamilyNode.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilyNode} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilyNode}
 */
proto.dlkit.proto.relationship.FamilyNode.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.FamilyNode.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilyNode.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilyNode} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyNode.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.FamilyNodeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.FamilyNodeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.FamilyNodeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.FamilyNodeList.displayName = 'proto.dlkit.proto.relationship.FamilyNodeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.FamilyNodeList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.FamilyNodeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.FamilyNodeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.FamilyNodeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyNodeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyNodesList: jspb.Message.toObjectList(msg.getFamilyNodesList(),
    proto.dlkit.proto.relationship.FamilyNode.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.FamilyNodeList}
 */
proto.dlkit.proto.relationship.FamilyNodeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.FamilyNodeList;
  return proto.dlkit.proto.relationship.FamilyNodeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.FamilyNodeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.FamilyNodeList}
 */
proto.dlkit.proto.relationship.FamilyNodeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.FamilyNode;
      reader.readMessage(value,proto.dlkit.proto.relationship.FamilyNode.deserializeBinaryFromReader);
      msg.addFamilyNodes(value);
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
proto.dlkit.proto.relationship.FamilyNodeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.FamilyNodeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.FamilyNodeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.FamilyNodeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyNodesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.relationship.FamilyNode.serializeBinaryToWriter
    );
  }
};


/**
 * repeated FamilyNode family_nodes = 1;
 * @return {!Array.<!proto.dlkit.proto.relationship.FamilyNode>}
 */
proto.dlkit.proto.relationship.FamilyNodeList.prototype.getFamilyNodesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.relationship.FamilyNode>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.relationship.FamilyNode, 1));
};


/** @param {!Array.<!proto.dlkit.proto.relationship.FamilyNode>} value */
proto.dlkit.proto.relationship.FamilyNodeList.prototype.setFamilyNodesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.relationship.FamilyNode=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.relationship.FamilyNode}
 */
proto.dlkit.proto.relationship.FamilyNodeList.prototype.addFamilyNodes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.relationship.FamilyNode, opt_index);
};


proto.dlkit.proto.relationship.FamilyNodeList.prototype.clearFamilyNodesList = function() {
  this.setFamilyNodesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.GetFamilyIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyIdReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyIdReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyIdReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyIdReply}
 */
proto.dlkit.proto.relationship.GetFamilyIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyIdReply;
  return proto.dlkit.proto.relationship.GetFamilyIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyIdReply}
 */
proto.dlkit.proto.relationship.GetFamilyIdReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyIdReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetFamilyIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyIdReply.prototype.hasId = function() {
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
proto.dlkit.proto.relationship.GetFamilyIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyIdRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyIdRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyIdRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyIdRequest}
 */
proto.dlkit.proto.relationship.GetFamilyIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyIdRequest;
  return proto.dlkit.proto.relationship.GetFamilyIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyIdRequest}
 */
proto.dlkit.proto.relationship.GetFamilyIdRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyIdRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    family: (f = msg.getFamily()) && proto.dlkit.proto.relationship.Family.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamilyReply}
 */
proto.dlkit.proto.relationship.GetFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyReply;
  return proto.dlkit.proto.relationship.GetFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyReply}
 */
proto.dlkit.proto.relationship.GetFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.Family;
      reader.readMessage(value,proto.dlkit.proto.relationship.Family.deserializeBinaryFromReader);
      msg.setFamily(value);
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
proto.dlkit.proto.relationship.GetFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamily();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.Family.serializeBinaryToWriter
    );
  }
};


/**
 * optional Family family = 1;
 * @return {?proto.dlkit.proto.relationship.Family}
 */
proto.dlkit.proto.relationship.GetFamilyReply.prototype.getFamily = function() {
  return /** @type{?proto.dlkit.proto.relationship.Family} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.Family, 1));
};


/** @param {?proto.dlkit.proto.relationship.Family|undefined} value */
proto.dlkit.proto.relationship.GetFamilyReply.prototype.setFamily = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyReply.prototype.clearFamily = function() {
  this.setFamily(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyReply.prototype.hasFamily = function() {
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
proto.dlkit.proto.relationship.GetFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyRequest}
 */
proto.dlkit.proto.relationship.GetFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyRequest;
  return proto.dlkit.proto.relationship.GetFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyRequest}
 */
proto.dlkit.proto.relationship.GetFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.CanLookupRelationshipsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanLookupRelationshipsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanLookupRelationshipsReply.displayName = 'proto.dlkit.proto.relationship.CanLookupRelationshipsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanLookupRelationshipsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanLookupRelationshipsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupRelationships: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanLookupRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanLookupRelationshipsReply;
  return proto.dlkit.proto.relationship.CanLookupRelationshipsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanLookupRelationshipsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanLookupRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupRelationships(value);
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
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanLookupRelationshipsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanLookupRelationshipsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupRelationships();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_relationships = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.prototype.getCanLookupRelationships = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanLookupRelationshipsReply.prototype.setCanLookupRelationships = function(value) {
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
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanLookupRelationshipsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.displayName = 'proto.dlkit.proto.relationship.CanLookupRelationshipsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanLookupRelationshipsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanLookupRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanLookupRelationshipsRequest;
  return proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanLookupRelationshipsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanLookupRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanLookupRelationshipsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupRelationshipsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.displayName = 'proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply;
  return proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.displayName = 'proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest;
  return proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeRelationshipViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.displayName = 'proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply;
  return proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.displayName = 'proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest;
  return proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryRelationshipViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseFederatedFamilyViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.displayName = 'proto.dlkit.proto.relationship.UseFederatedFamilyViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseFederatedFamilyViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseFederatedFamilyViewReply}
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseFederatedFamilyViewReply;
  return proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseFederatedFamilyViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseFederatedFamilyViewReply}
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseFederatedFamilyViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.displayName = 'proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest;
  return proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseFederatedFamilyViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.displayName = 'proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply}
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply;
  return proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply}
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.displayName = 'proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest;
  return proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseIsolatedFamilyViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.displayName = 'proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply;
  return proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.displayName = 'proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest;
  return proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseEffectiveRelationshipViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.displayName = 'proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply;
  return proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply}
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.displayName = 'proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest;
  return proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest}
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseAnyEffectiveRelationshipViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetRelationshipReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipReply.displayName = 'proto.dlkit.proto.relationship.GetRelationshipReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationship: (f = msg.getRelationship()) && proto.dlkit.proto.relationship.Relationship.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipReply}
 */
proto.dlkit.proto.relationship.GetRelationshipReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipReply;
  return proto.dlkit.proto.relationship.GetRelationshipReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipReply}
 */
proto.dlkit.proto.relationship.GetRelationshipReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.Relationship;
      reader.readMessage(value,proto.dlkit.proto.relationship.Relationship.deserializeBinaryFromReader);
      msg.setRelationship(value);
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
proto.dlkit.proto.relationship.GetRelationshipReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationship();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.Relationship.serializeBinaryToWriter
    );
  }
};


/**
 * optional Relationship relationship = 1;
 * @return {?proto.dlkit.proto.relationship.Relationship}
 */
proto.dlkit.proto.relationship.GetRelationshipReply.prototype.getRelationship = function() {
  return /** @type{?proto.dlkit.proto.relationship.Relationship} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.Relationship, 1));
};


/** @param {?proto.dlkit.proto.relationship.Relationship|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipReply.prototype.setRelationship = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipReply.prototype.clearRelationship = function() {
  this.setRelationship(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipReply.prototype.hasRelationship = function() {
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
proto.dlkit.proto.relationship.GetRelationshipRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipId: (f = msg.getRelationshipId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipRequest;
  return proto.dlkit.proto.relationship.GetRelationshipRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setRelationshipId(value);
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
proto.dlkit.proto.relationship.GetRelationshipRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id relationship_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.prototype.getRelationshipId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipRequest.prototype.setRelationshipId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipRequest.prototype.clearRelationshipId = function() {
  this.setRelationshipId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipRequest.prototype.hasRelationshipId = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipIdsList: jspb.Message.toObjectList(msg.getRelationshipIdsList(),
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
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addRelationshipIds(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id relationship_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.prototype.getRelationshipIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.prototype.setRelationshipIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.prototype.addRelationshipIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.relationship.GetRelationshipsByIdsRequest.prototype.clearRelationshipIdsList = function() {
  this.setRelationshipIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeRequest.prototype.hasRelationshipGenusType = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByParentGenusTypeRequest.prototype.hasRelationshipGenusType = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipRecordType: (f = msg.getRelationshipRecordType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipRecordType(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipRecordType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_record_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.prototype.getRelationshipRecordType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.prototype.setRelationshipRecordType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.prototype.clearRelationshipRecordType = function() {
  this.setRelationshipRecordType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByRecordTypeRequest.prototype.hasRelationshipRecordType = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp from_ = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp to = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
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
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceRequest.prototype.hasSourceId = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
      break;
    case 3:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp from_ = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.hasSourceId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp to = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForSourceOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.hasRelationshipGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceRequest.prototype.hasSourceId = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
      break;
    case 4:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional google.protobuf.Timestamp from_ = 1;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.hasRelationshipGenusType = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.hasSourceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp to = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForSourceOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
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
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationRequest.prototype.hasDestinationId = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp to = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForDestinationOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationRequest.prototype.hasRelationshipGenusType = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
      break;
    case 4:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.hasRelationshipGenusType = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp to = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForDestinationOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
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
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersRequest.prototype.hasSourceId = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
      break;
    case 4:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.hasSourceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp to = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsForPeersOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 2;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.hasRelationshipGenusType = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersRequest.prototype.hasSourceId = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    relationshipGenusType: (f = msg.getRelationshipGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    to: (f = msg.getTo()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setRelationshipGenusType(value);
      break;
    case 4:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
      break;
    case 5:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setTo(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipGenusType();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getTo();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type relationship_genus_type = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.getRelationshipGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.setRelationshipGenusType = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.clearRelationshipGenusType = function() {
  this.setRelationshipGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.hasRelationshipGenusType = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.hasSourceId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional google.protobuf.Timestamp to = 5;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 5));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByGenusTypeForPeersOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.relationship.GetRelationshipsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetRelationshipsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.CanSearchRelationshipsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanSearchRelationshipsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanSearchRelationshipsReply.displayName = 'proto.dlkit.proto.relationship.CanSearchRelationshipsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanSearchRelationshipsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanSearchRelationshipsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canSearchRelationships: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanSearchRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanSearchRelationshipsReply;
  return proto.dlkit.proto.relationship.CanSearchRelationshipsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanSearchRelationshipsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanSearchRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanSearchRelationships(value);
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
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanSearchRelationshipsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanSearchRelationshipsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanSearchRelationships();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_search_relationships = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.prototype.getCanSearchRelationships = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanSearchRelationshipsReply.prototype.setCanSearchRelationships = function(value) {
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
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanSearchRelationshipsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.displayName = 'proto.dlkit.proto.relationship.CanSearchRelationshipsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanSearchRelationshipsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanSearchRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanSearchRelationshipsRequest;
  return proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanSearchRelationshipsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanSearchRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanSearchRelationshipsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanSearchRelationshipsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetRelationshipQueryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipQueryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipQueryReply.displayName = 'proto.dlkit.proto.relationship.GetRelationshipQueryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipQueryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipQueryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipQuery: (f = msg.getRelationshipQuery()) && proto.dlkit.proto.relationship.RelationshipQuery.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipQueryReply}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipQueryReply;
  return proto.dlkit.proto.relationship.GetRelationshipQueryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipQueryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipQueryReply}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.RelationshipQuery;
      reader.readMessage(value,proto.dlkit.proto.relationship.RelationshipQuery.deserializeBinaryFromReader);
      msg.setRelationshipQuery(value);
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
proto.dlkit.proto.relationship.GetRelationshipQueryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipQueryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipQueryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.RelationshipQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional RelationshipQuery relationship_query = 1;
 * @return {?proto.dlkit.proto.relationship.RelationshipQuery}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.prototype.getRelationshipQuery = function() {
  return /** @type{?proto.dlkit.proto.relationship.RelationshipQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.RelationshipQuery, 1));
};


/** @param {?proto.dlkit.proto.relationship.RelationshipQuery|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.prototype.setRelationshipQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipQueryReply.prototype.clearRelationshipQuery = function() {
  this.setRelationshipQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryReply.prototype.hasRelationshipQuery = function() {
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
proto.dlkit.proto.relationship.GetRelationshipQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipQueryRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipQueryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipQueryRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetRelationshipQueryRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipQueryRequest;
  return proto.dlkit.proto.relationship.GetRelationshipQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipQueryRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetRelationshipQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipQueryRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipQuery: (f = msg.getRelationshipQuery()) && proto.dlkit.proto.relationship.RelationshipQuery.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest;
  return proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.RelationshipQuery;
      reader.readMessage(value,proto.dlkit.proto.relationship.RelationshipQuery.deserializeBinaryFromReader);
      msg.setRelationshipQuery(value);
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
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.RelationshipQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional RelationshipQuery relationship_query = 1;
 * @return {?proto.dlkit.proto.relationship.RelationshipQuery}
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.prototype.getRelationshipQuery = function() {
  return /** @type{?proto.dlkit.proto.relationship.RelationshipQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.RelationshipQuery, 1));
};


/** @param {?proto.dlkit.proto.relationship.RelationshipQuery|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.prototype.setRelationshipQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.prototype.clearRelationshipQuery = function() {
  this.setRelationshipQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipsByQueryRequest.prototype.hasRelationshipQuery = function() {
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
proto.dlkit.proto.relationship.CanCreateRelationshipsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateRelationshipsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateRelationshipsReply.displayName = 'proto.dlkit.proto.relationship.CanCreateRelationshipsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateRelationshipsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateRelationships: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateRelationshipsReply;
  return proto.dlkit.proto.relationship.CanCreateRelationshipsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateRelationships(value);
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
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateRelationshipsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateRelationships();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_relationships = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.prototype.getCanCreateRelationships = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanCreateRelationshipsReply.prototype.setCanCreateRelationships = function(value) {
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
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateRelationshipsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.displayName = 'proto.dlkit.proto.relationship.CanCreateRelationshipsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateRelationshipsRequest;
  return proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.displayName = 'proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateRelationshipWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply;
  return proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateRelationshipWithRecordTypes(value);
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
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateRelationshipWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_relationship_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.prototype.getCanCreateRelationshipWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesReply.prototype.setCanCreateRelationshipWithRecordTypes = function(value) {
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
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.displayName = 'proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipRecordTypesList: jspb.Message.toObjectList(msg.getRelationshipRecordTypesList(),
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
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest;
  return proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRelationshipRecordTypes(value);
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
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type relationship_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.prototype.getRelationshipRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.prototype.setRelationshipRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.prototype.addRelationshipRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.relationship.CanCreateRelationshipWithRecordTypesRequest.prototype.clearRelationshipRecordTypesList = function() {
  this.setRelationshipRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.displayName = 'proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipForm: (f = msg.getRelationshipForm()) && proto.dlkit.proto.relationship.RelationshipForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply;
  return proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.RelationshipForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.RelationshipForm.deserializeBinaryFromReader);
      msg.setRelationshipForm(value);
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
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.RelationshipForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional RelationshipForm relationship_form = 1;
 * @return {?proto.dlkit.proto.relationship.RelationshipForm}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.prototype.getRelationshipForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.RelationshipForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.RelationshipForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.RelationshipForm|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.prototype.setRelationshipForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.prototype.clearRelationshipForm = function() {
  this.setRelationshipForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateReply.prototype.hasRelationshipForm = function() {
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
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.repeatedFields_ = [2];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    destinationId: (f = msg.getDestinationId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    relationshipRecordTypesList: jspb.Message.toObjectList(msg.getRelationshipRecordTypesList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    sourceId: (f = msg.getSourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDestinationId(value);
      break;
    case 2:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRelationshipRecordTypes(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSourceId(value);
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
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDestinationId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      2,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getSourceId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id destination_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.getDestinationId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.setDestinationId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.clearDestinationId = function() {
  this.setDestinationId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.hasDestinationId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type relationship_record_types = 2;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.getRelationshipRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 2));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.setRelationshipRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 2, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.addRelationshipRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 2, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.clearRelationshipRecordTypesList = function() {
  this.setRelationshipRecordTypesList([]);
};


/**
 * optional dlkit.primordium.id.primitives.Id source_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.getSourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.setSourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.clearSourceId = function() {
  this.setSourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForCreateRequest.prototype.hasSourceId = function() {
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
proto.dlkit.proto.relationship.CreateRelationshipReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CreateRelationshipReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CreateRelationshipReply.displayName = 'proto.dlkit.proto.relationship.CreateRelationshipReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CreateRelationshipReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CreateRelationshipReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationship: (f = msg.getRelationship()) && proto.dlkit.proto.relationship.Relationship.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CreateRelationshipReply}
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CreateRelationshipReply;
  return proto.dlkit.proto.relationship.CreateRelationshipReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CreateRelationshipReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CreateRelationshipReply}
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.Relationship;
      reader.readMessage(value,proto.dlkit.proto.relationship.Relationship.deserializeBinaryFromReader);
      msg.setRelationship(value);
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
proto.dlkit.proto.relationship.CreateRelationshipReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CreateRelationshipReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CreateRelationshipReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationship();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.Relationship.serializeBinaryToWriter
    );
  }
};


/**
 * optional Relationship relationship = 1;
 * @return {?proto.dlkit.proto.relationship.Relationship}
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.prototype.getRelationship = function() {
  return /** @type{?proto.dlkit.proto.relationship.Relationship} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.Relationship, 1));
};


/** @param {?proto.dlkit.proto.relationship.Relationship|undefined} value */
proto.dlkit.proto.relationship.CreateRelationshipReply.prototype.setRelationship = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.CreateRelationshipReply.prototype.clearRelationship = function() {
  this.setRelationship(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.CreateRelationshipReply.prototype.hasRelationship = function() {
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
proto.dlkit.proto.relationship.CreateRelationshipRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CreateRelationshipRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CreateRelationshipRequest.displayName = 'proto.dlkit.proto.relationship.CreateRelationshipRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CreateRelationshipRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CreateRelationshipRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipForm: (f = msg.getRelationshipForm()) && proto.dlkit.proto.relationship.RelationshipForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CreateRelationshipRequest}
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CreateRelationshipRequest;
  return proto.dlkit.proto.relationship.CreateRelationshipRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CreateRelationshipRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CreateRelationshipRequest}
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.RelationshipForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.RelationshipForm.deserializeBinaryFromReader);
      msg.setRelationshipForm(value);
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
proto.dlkit.proto.relationship.CreateRelationshipRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CreateRelationshipRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CreateRelationshipRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.RelationshipForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional RelationshipForm relationship_form = 1;
 * @return {?proto.dlkit.proto.relationship.RelationshipForm}
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.prototype.getRelationshipForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.RelationshipForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.RelationshipForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.RelationshipForm|undefined} value */
proto.dlkit.proto.relationship.CreateRelationshipRequest.prototype.setRelationshipForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.CreateRelationshipRequest.prototype.clearRelationshipForm = function() {
  this.setRelationshipForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.CreateRelationshipRequest.prototype.hasRelationshipForm = function() {
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
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanUpdateRelationshipsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.displayName = 'proto.dlkit.proto.relationship.CanUpdateRelationshipsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanUpdateRelationshipsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateRelationships: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanUpdateRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanUpdateRelationshipsReply;
  return proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanUpdateRelationshipsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanUpdateRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateRelationships(value);
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
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanUpdateRelationshipsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateRelationships();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_relationships = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.prototype.getCanUpdateRelationships = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanUpdateRelationshipsReply.prototype.setCanUpdateRelationships = function(value) {
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
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.displayName = 'proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest;
  return proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateRelationshipsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.displayName = 'proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipForm: (f = msg.getRelationshipForm()) && proto.dlkit.proto.relationship.RelationshipForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply;
  return proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.RelationshipForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.RelationshipForm.deserializeBinaryFromReader);
      msg.setRelationshipForm(value);
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
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.RelationshipForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional RelationshipForm relationship_form = 1;
 * @return {?proto.dlkit.proto.relationship.RelationshipForm}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.prototype.getRelationshipForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.RelationshipForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.RelationshipForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.RelationshipForm|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.prototype.setRelationshipForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.prototype.clearRelationshipForm = function() {
  this.setRelationshipForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateReply.prototype.hasRelationshipForm = function() {
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
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.displayName = 'proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipId: (f = msg.getRelationshipId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest;
  return proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setRelationshipId(value);
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
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id relationship_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.prototype.getRelationshipId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.prototype.setRelationshipId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.prototype.clearRelationshipId = function() {
  this.setRelationshipId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetRelationshipFormForUpdateRequest.prototype.hasRelationshipId = function() {
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
proto.dlkit.proto.relationship.UpdateRelationshipReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UpdateRelationshipReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UpdateRelationshipReply.displayName = 'proto.dlkit.proto.relationship.UpdateRelationshipReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UpdateRelationshipReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UpdateRelationshipReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UpdateRelationshipReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateRelationshipReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UpdateRelationshipReply}
 */
proto.dlkit.proto.relationship.UpdateRelationshipReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UpdateRelationshipReply;
  return proto.dlkit.proto.relationship.UpdateRelationshipReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UpdateRelationshipReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UpdateRelationshipReply}
 */
proto.dlkit.proto.relationship.UpdateRelationshipReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UpdateRelationshipReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UpdateRelationshipReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UpdateRelationshipReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateRelationshipReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UpdateRelationshipRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UpdateRelationshipRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UpdateRelationshipRequest.displayName = 'proto.dlkit.proto.relationship.UpdateRelationshipRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UpdateRelationshipRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UpdateRelationshipRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipForm: (f = msg.getRelationshipForm()) && proto.dlkit.proto.relationship.RelationshipForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.UpdateRelationshipRequest}
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UpdateRelationshipRequest;
  return proto.dlkit.proto.relationship.UpdateRelationshipRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UpdateRelationshipRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UpdateRelationshipRequest}
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.RelationshipForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.RelationshipForm.deserializeBinaryFromReader);
      msg.setRelationshipForm(value);
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
proto.dlkit.proto.relationship.UpdateRelationshipRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UpdateRelationshipRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UpdateRelationshipRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.RelationshipForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional RelationshipForm relationship_form = 1;
 * @return {?proto.dlkit.proto.relationship.RelationshipForm}
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.prototype.getRelationshipForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.RelationshipForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.RelationshipForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.RelationshipForm|undefined} value */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.prototype.setRelationshipForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.UpdateRelationshipRequest.prototype.clearRelationshipForm = function() {
  this.setRelationshipForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.UpdateRelationshipRequest.prototype.hasRelationshipForm = function() {
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
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanDeleteRelationshipsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.displayName = 'proto.dlkit.proto.relationship.CanDeleteRelationshipsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanDeleteRelationshipsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteRelationships: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanDeleteRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanDeleteRelationshipsReply;
  return proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanDeleteRelationshipsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanDeleteRelationshipsReply}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteRelationships(value);
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
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanDeleteRelationshipsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteRelationships();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_relationships = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.prototype.getCanDeleteRelationships = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanDeleteRelationshipsReply.prototype.setCanDeleteRelationships = function(value) {
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
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.displayName = 'proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest;
  return proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest}
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteRelationshipsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.DeleteRelationshipReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.DeleteRelationshipReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.DeleteRelationshipReply.displayName = 'proto.dlkit.proto.relationship.DeleteRelationshipReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.DeleteRelationshipReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.DeleteRelationshipReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.DeleteRelationshipReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteRelationshipReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.DeleteRelationshipReply}
 */
proto.dlkit.proto.relationship.DeleteRelationshipReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.DeleteRelationshipReply;
  return proto.dlkit.proto.relationship.DeleteRelationshipReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.DeleteRelationshipReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.DeleteRelationshipReply}
 */
proto.dlkit.proto.relationship.DeleteRelationshipReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.DeleteRelationshipReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.DeleteRelationshipReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.DeleteRelationshipReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteRelationshipReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.DeleteRelationshipRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.DeleteRelationshipRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.DeleteRelationshipRequest.displayName = 'proto.dlkit.proto.relationship.DeleteRelationshipRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.DeleteRelationshipRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.DeleteRelationshipRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    relationshipId: (f = msg.getRelationshipId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.DeleteRelationshipRequest}
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.DeleteRelationshipRequest;
  return proto.dlkit.proto.relationship.DeleteRelationshipRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.DeleteRelationshipRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.DeleteRelationshipRequest}
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setRelationshipId(value);
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
proto.dlkit.proto.relationship.DeleteRelationshipRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.DeleteRelationshipRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.DeleteRelationshipRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRelationshipId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id relationship_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.prototype.getRelationshipId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.prototype.setRelationshipId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.DeleteRelationshipRequest.prototype.clearRelationshipId = function() {
  this.setRelationshipId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.DeleteRelationshipRequest.prototype.hasRelationshipId = function() {
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
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.displayName = 'proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageRelationshipAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply;
  return proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageRelationshipAliases(value);
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
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageRelationshipAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_relationship_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.prototype.getCanManageRelationshipAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesReply.prototype.setCanManageRelationshipAliases = function(value) {
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
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.displayName = 'proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest;
  return proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest}
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageRelationshipAliasesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AliasRelationshipReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AliasRelationshipReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AliasRelationshipReply.displayName = 'proto.dlkit.proto.relationship.AliasRelationshipReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AliasRelationshipReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AliasRelationshipReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AliasRelationshipReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasRelationshipReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.AliasRelationshipReply}
 */
proto.dlkit.proto.relationship.AliasRelationshipReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AliasRelationshipReply;
  return proto.dlkit.proto.relationship.AliasRelationshipReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AliasRelationshipReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AliasRelationshipReply}
 */
proto.dlkit.proto.relationship.AliasRelationshipReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.AliasRelationshipReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AliasRelationshipReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AliasRelationshipReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasRelationshipReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AliasRelationshipRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AliasRelationshipRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AliasRelationshipRequest.displayName = 'proto.dlkit.proto.relationship.AliasRelationshipRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AliasRelationshipRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AliasRelationshipRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    relationshipId: (f = msg.getRelationshipId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.AliasRelationshipRequest}
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AliasRelationshipRequest;
  return proto.dlkit.proto.relationship.AliasRelationshipRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AliasRelationshipRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AliasRelationshipRequest}
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setRelationshipId(value);
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
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AliasRelationshipRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AliasRelationshipRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getRelationshipId();
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
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id relationship_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.getRelationshipId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.setRelationshipId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.clearRelationshipId = function() {
  this.setRelationshipId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AliasRelationshipRequest.prototype.hasRelationshipId = function() {
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
proto.dlkit.proto.relationship.CanLookupFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanLookupFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanLookupFamiliesReply.displayName = 'proto.dlkit.proto.relationship.CanLookupFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanLookupFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanLookupFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupFamilies: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanLookupFamiliesReply}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanLookupFamiliesReply;
  return proto.dlkit.proto.relationship.CanLookupFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanLookupFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanLookupFamiliesReply}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupFamilies(value);
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
proto.dlkit.proto.relationship.CanLookupFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanLookupFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanLookupFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupFamilies();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_families = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.prototype.getCanLookupFamilies = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanLookupFamiliesReply.prototype.setCanLookupFamilies = function(value) {
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
proto.dlkit.proto.relationship.CanLookupFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanLookupFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanLookupFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.CanLookupFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanLookupFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanLookupFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupFamiliesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanLookupFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanLookupFamiliesRequest;
  return proto.dlkit.proto.relationship.CanLookupFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanLookupFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanLookupFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanLookupFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanLookupFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanLookupFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanLookupFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanLookupFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseComparativeFamilyViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.displayName = 'proto.dlkit.proto.relationship.UseComparativeFamilyViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseComparativeFamilyViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseComparativeFamilyViewReply}
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseComparativeFamilyViewReply;
  return proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseComparativeFamilyViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseComparativeFamilyViewReply}
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseComparativeFamilyViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.displayName = 'proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest;
  return proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UseComparativeFamilyViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.displayName = 'proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply}
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply;
  return proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply}
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.displayName = 'proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest;
  return proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest}
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UsePlenaryFamilyViewRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamiliesByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.displayName = 'proto.dlkit.proto.relationship.GetFamiliesByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyIdsList: jspb.Message.toObjectList(msg.getFamilyIdsList(),
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
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByIdsRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamiliesByIdsRequest;
  return proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByIdsRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addFamilyIds(value);
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
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id family_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.prototype.getFamilyIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.prototype.setFamilyIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.prototype.addFamilyIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.relationship.GetFamiliesByIdsRequest.prototype.clearFamilyIdsList = function() {
  this.setFamilyIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.displayName = 'proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyGenusType: (f = msg.getFamilyGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest;
  return proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setFamilyGenusType(value);
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
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type family_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.prototype.getFamilyGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.prototype.setFamilyGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.prototype.clearFamilyGenusType = function() {
  this.setFamilyGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamiliesByGenusTypeRequest.prototype.hasFamilyGenusType = function() {
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
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyGenusType: (f = msg.getFamilyGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest;
  return proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setFamilyGenusType(value);
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
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type family_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.prototype.getFamilyGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.prototype.setFamilyGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.prototype.clearFamilyGenusType = function() {
  this.setFamilyGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamiliesByParentGenusTypeRequest.prototype.hasFamilyGenusType = function() {
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
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.displayName = 'proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyRecordType: (f = msg.getFamilyRecordType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest;
  return proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setFamilyRecordType(value);
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
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyRecordType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type family_record_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.prototype.getFamilyRecordType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.prototype.setFamilyRecordType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.prototype.clearFamilyRecordType = function() {
  this.setFamilyRecordType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamiliesByRecordTypeRequest.prototype.hasFamilyRecordType = function() {
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
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamiliesByProviderRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.displayName = 'proto.dlkit.proto.relationship.GetFamiliesByProviderRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByProviderRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByProviderRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamiliesByProviderRequest;
  return proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByProviderRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesByProviderRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesByProviderRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamiliesByProviderRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.relationship.GetFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.GetFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamiliesRequest;
  return proto.dlkit.proto.relationship.GetFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.CanCreateFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateFamiliesReply.displayName = 'proto.dlkit.proto.relationship.CanCreateFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateFamilies: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanCreateFamiliesReply}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateFamiliesReply;
  return proto.dlkit.proto.relationship.CanCreateFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateFamiliesReply}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateFamilies(value);
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
proto.dlkit.proto.relationship.CanCreateFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateFamilies();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_families = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.prototype.getCanCreateFamilies = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanCreateFamiliesReply.prototype.setCanCreateFamilies = function(value) {
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
proto.dlkit.proto.relationship.CanCreateFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.CanCreateFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamiliesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanCreateFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateFamiliesRequest;
  return proto.dlkit.proto.relationship.CanCreateFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanCreateFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanCreateFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.displayName = 'proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateFamilyWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply;
  return proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateFamilyWithRecordTypes(value);
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
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateFamilyWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_family_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.prototype.getCanCreateFamilyWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesReply.prototype.setCanCreateFamilyWithRecordTypes = function(value) {
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
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.displayName = 'proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyRecordTypesList: jspb.Message.toObjectList(msg.getFamilyRecordTypesList(),
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
 * @return {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest;
  return proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addFamilyRecordTypes(value);
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
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type family_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.prototype.getFamilyRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.prototype.setFamilyRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.prototype.addFamilyRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.relationship.CanCreateFamilyWithRecordTypesRequest.prototype.clearFamilyRecordTypesList = function() {
  this.setFamilyRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyFormForCreateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyForm: (f = msg.getFamilyForm()) && proto.dlkit.proto.relationship.FamilyForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForCreateReply}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyFormForCreateReply;
  return proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForCreateReply}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.FamilyForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.FamilyForm.deserializeBinaryFromReader);
      msg.setFamilyForm(value);
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
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.FamilyForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional FamilyForm family_form = 1;
 * @return {?proto.dlkit.proto.relationship.FamilyForm}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.prototype.getFamilyForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.FamilyForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.FamilyForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.FamilyForm|undefined} value */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.prototype.setFamilyForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.prototype.clearFamilyForm = function() {
  this.setFamilyForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateReply.prototype.hasFamilyForm = function() {
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
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyRecordTypesList: jspb.Message.toObjectList(msg.getFamilyRecordTypesList(),
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest;
  return proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addFamilyRecordTypes(value);
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
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type family_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.prototype.getFamilyRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.prototype.setFamilyRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.prototype.addFamilyRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.relationship.GetFamilyFormForCreateRequest.prototype.clearFamilyRecordTypesList = function() {
  this.setFamilyRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.relationship.CreateFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CreateFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CreateFamilyReply.displayName = 'proto.dlkit.proto.relationship.CreateFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CreateFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CreateFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CreateFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateFamilyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    family: (f = msg.getFamily()) && proto.dlkit.proto.relationship.Family.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CreateFamilyReply}
 */
proto.dlkit.proto.relationship.CreateFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CreateFamilyReply;
  return proto.dlkit.proto.relationship.CreateFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CreateFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CreateFamilyReply}
 */
proto.dlkit.proto.relationship.CreateFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.Family;
      reader.readMessage(value,proto.dlkit.proto.relationship.Family.deserializeBinaryFromReader);
      msg.setFamily(value);
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
proto.dlkit.proto.relationship.CreateFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CreateFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CreateFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateFamilyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamily();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.Family.serializeBinaryToWriter
    );
  }
};


/**
 * optional Family family = 1;
 * @return {?proto.dlkit.proto.relationship.Family}
 */
proto.dlkit.proto.relationship.CreateFamilyReply.prototype.getFamily = function() {
  return /** @type{?proto.dlkit.proto.relationship.Family} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.Family, 1));
};


/** @param {?proto.dlkit.proto.relationship.Family|undefined} value */
proto.dlkit.proto.relationship.CreateFamilyReply.prototype.setFamily = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.CreateFamilyReply.prototype.clearFamily = function() {
  this.setFamily(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.CreateFamilyReply.prototype.hasFamily = function() {
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
proto.dlkit.proto.relationship.CreateFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CreateFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CreateFamilyRequest.displayName = 'proto.dlkit.proto.relationship.CreateFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CreateFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CreateFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyForm: (f = msg.getFamilyForm()) && proto.dlkit.proto.relationship.FamilyForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CreateFamilyRequest}
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CreateFamilyRequest;
  return proto.dlkit.proto.relationship.CreateFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CreateFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CreateFamilyRequest}
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.FamilyForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.FamilyForm.deserializeBinaryFromReader);
      msg.setFamilyForm(value);
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
proto.dlkit.proto.relationship.CreateFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CreateFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CreateFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.FamilyForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional FamilyForm family_form = 1;
 * @return {?proto.dlkit.proto.relationship.FamilyForm}
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.prototype.getFamilyForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.FamilyForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.FamilyForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.FamilyForm|undefined} value */
proto.dlkit.proto.relationship.CreateFamilyRequest.prototype.setFamilyForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.CreateFamilyRequest.prototype.clearFamilyForm = function() {
  this.setFamilyForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.CreateFamilyRequest.prototype.hasFamilyForm = function() {
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
proto.dlkit.proto.relationship.CanUpdateFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanUpdateFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanUpdateFamiliesReply.displayName = 'proto.dlkit.proto.relationship.CanUpdateFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanUpdateFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanUpdateFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateFamilies: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanUpdateFamiliesReply}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanUpdateFamiliesReply;
  return proto.dlkit.proto.relationship.CanUpdateFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanUpdateFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanUpdateFamiliesReply}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateFamilies(value);
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
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanUpdateFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanUpdateFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateFamilies();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_families = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.prototype.getCanUpdateFamilies = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanUpdateFamiliesReply.prototype.setCanUpdateFamilies = function(value) {
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
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanUpdateFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.CanUpdateFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanUpdateFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanUpdateFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanUpdateFamiliesRequest;
  return proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanUpdateFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanUpdateFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanUpdateFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanUpdateFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyForm: (f = msg.getFamilyForm()) && proto.dlkit.proto.relationship.FamilyForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply;
  return proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.FamilyForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.FamilyForm.deserializeBinaryFromReader);
      msg.setFamilyForm(value);
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
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.FamilyForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional FamilyForm family_form = 1;
 * @return {?proto.dlkit.proto.relationship.FamilyForm}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.prototype.getFamilyForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.FamilyForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.FamilyForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.FamilyForm|undefined} value */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.prototype.setFamilyForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.prototype.clearFamilyForm = function() {
  this.setFamilyForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateReply.prototype.hasFamilyForm = function() {
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
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest;
  return proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyFormForUpdateRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.UpdateFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UpdateFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UpdateFamilyReply.displayName = 'proto.dlkit.proto.relationship.UpdateFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UpdateFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UpdateFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UpdateFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.UpdateFamilyReply}
 */
proto.dlkit.proto.relationship.UpdateFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UpdateFamilyReply;
  return proto.dlkit.proto.relationship.UpdateFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UpdateFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UpdateFamilyReply}
 */
proto.dlkit.proto.relationship.UpdateFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.UpdateFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UpdateFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UpdateFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.UpdateFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.UpdateFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.UpdateFamilyRequest.displayName = 'proto.dlkit.proto.relationship.UpdateFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.UpdateFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.UpdateFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyForm: (f = msg.getFamilyForm()) && proto.dlkit.proto.relationship.FamilyForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.UpdateFamilyRequest}
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.UpdateFamilyRequest;
  return proto.dlkit.proto.relationship.UpdateFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.UpdateFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.UpdateFamilyRequest}
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.FamilyForm;
      reader.readMessage(value,proto.dlkit.proto.relationship.FamilyForm.deserializeBinaryFromReader);
      msg.setFamilyForm(value);
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
proto.dlkit.proto.relationship.UpdateFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.UpdateFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.UpdateFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.FamilyForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional FamilyForm family_form = 1;
 * @return {?proto.dlkit.proto.relationship.FamilyForm}
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.prototype.getFamilyForm = function() {
  return /** @type{?proto.dlkit.proto.relationship.FamilyForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.FamilyForm, 1));
};


/** @param {?proto.dlkit.proto.relationship.FamilyForm|undefined} value */
proto.dlkit.proto.relationship.UpdateFamilyRequest.prototype.setFamilyForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.UpdateFamilyRequest.prototype.clearFamilyForm = function() {
  this.setFamilyForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.UpdateFamilyRequest.prototype.hasFamilyForm = function() {
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
proto.dlkit.proto.relationship.CanDeleteFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanDeleteFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanDeleteFamiliesReply.displayName = 'proto.dlkit.proto.relationship.CanDeleteFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanDeleteFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanDeleteFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteFamilies: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanDeleteFamiliesReply}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanDeleteFamiliesReply;
  return proto.dlkit.proto.relationship.CanDeleteFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanDeleteFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanDeleteFamiliesReply}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteFamilies(value);
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
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanDeleteFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanDeleteFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteFamilies();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_families = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.prototype.getCanDeleteFamilies = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanDeleteFamiliesReply.prototype.setCanDeleteFamilies = function(value) {
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
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanDeleteFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.CanDeleteFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanDeleteFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanDeleteFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanDeleteFamiliesRequest;
  return proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanDeleteFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanDeleteFamiliesRequest}
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanDeleteFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanDeleteFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.DeleteFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.DeleteFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.DeleteFamilyReply.displayName = 'proto.dlkit.proto.relationship.DeleteFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.DeleteFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.DeleteFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.DeleteFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.DeleteFamilyReply}
 */
proto.dlkit.proto.relationship.DeleteFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.DeleteFamilyReply;
  return proto.dlkit.proto.relationship.DeleteFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.DeleteFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.DeleteFamilyReply}
 */
proto.dlkit.proto.relationship.DeleteFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.DeleteFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.DeleteFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.DeleteFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.DeleteFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.DeleteFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.DeleteFamilyRequest.displayName = 'proto.dlkit.proto.relationship.DeleteFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.DeleteFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.DeleteFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.DeleteFamilyRequest}
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.DeleteFamilyRequest;
  return proto.dlkit.proto.relationship.DeleteFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.DeleteFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.DeleteFamilyRequest}
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.DeleteFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.DeleteFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.DeleteFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.DeleteFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.DeleteFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.DeleteFamilyRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanManageFamilyAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.displayName = 'proto.dlkit.proto.relationship.CanManageFamilyAliasesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanManageFamilyAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageFamilyAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanManageFamilyAliasesReply}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanManageFamilyAliasesReply;
  return proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanManageFamilyAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanManageFamilyAliasesReply}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageFamilyAliases(value);
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
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanManageFamilyAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageFamilyAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_family_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.prototype.getCanManageFamilyAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanManageFamilyAliasesReply.prototype.setCanManageFamilyAliases = function(value) {
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
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.displayName = 'proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest;
  return proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest}
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanManageFamilyAliasesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AliasFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AliasFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AliasFamilyReply.displayName = 'proto.dlkit.proto.relationship.AliasFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AliasFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AliasFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AliasFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.AliasFamilyReply}
 */
proto.dlkit.proto.relationship.AliasFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AliasFamilyReply;
  return proto.dlkit.proto.relationship.AliasFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AliasFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AliasFamilyReply}
 */
proto.dlkit.proto.relationship.AliasFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.AliasFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AliasFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AliasFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AliasFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AliasFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AliasFamilyRequest.displayName = 'proto.dlkit.proto.relationship.AliasFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AliasFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AliasFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.AliasFamilyRequest}
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AliasFamilyRequest;
  return proto.dlkit.proto.relationship.AliasFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AliasFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AliasFamilyRequest}
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AliasFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AliasFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFamilyId();
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
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AliasFamilyRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply;
  return proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdReply.prototype.hasId = function() {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest;
  return proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyIdRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyHierarchyReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyReply}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyHierarchyReply;
  return proto.dlkit.proto.relationship.GetFamilyHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyReply}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.prototype.getHierarchy = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Hierarchy} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Hierarchy, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Hierarchy|undefined} value */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.prototype.setHierarchy = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyHierarchyReply.prototype.clearHierarchy = function() {
  this.setHierarchy(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyReply.prototype.hasHierarchy = function() {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyRequest}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyHierarchyRequest;
  return proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyHierarchyRequest}
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.displayName = 'proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAccessFamilyHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply;
  return proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAccessFamilyHierarchy(value);
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
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAccessFamilyHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_access_family_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.prototype.getCanAccessFamilyHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyReply.prototype.setCanAccessFamilyHierarchy = function(value) {
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
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.displayName = 'proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest;
  return proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest}
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanAccessFamilyHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRootFamilyIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.displayName = 'proto.dlkit.proto.relationship.GetRootFamilyIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRootFamilyIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetRootFamilyIdsRequest}
 */
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRootFamilyIdsRequest;
  return proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRootFamilyIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRootFamilyIdsRequest}
 */
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRootFamilyIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRootFamilyIdsRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetRootFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetRootFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetRootFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.GetRootFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetRootFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetRootFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetRootFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRootFamiliesRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetRootFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetRootFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetRootFamiliesRequest;
  return proto.dlkit.proto.relationship.GetRootFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetRootFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetRootFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetRootFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetRootFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetRootFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetRootFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetRootFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.HasParentFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.HasParentFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.HasParentFamiliesReply.displayName = 'proto.dlkit.proto.relationship.HasParentFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.HasParentFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.HasParentFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.HasParentFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasParentFamiliesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasParentFamilies: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.HasParentFamiliesReply}
 */
proto.dlkit.proto.relationship.HasParentFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.HasParentFamiliesReply;
  return proto.dlkit.proto.relationship.HasParentFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.HasParentFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.HasParentFamiliesReply}
 */
proto.dlkit.proto.relationship.HasParentFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasParentFamilies(value);
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
proto.dlkit.proto.relationship.HasParentFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.HasParentFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.HasParentFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasParentFamiliesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasParentFamilies();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_parent_families = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.HasParentFamiliesReply.prototype.getHasParentFamilies = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.HasParentFamiliesReply.prototype.setHasParentFamilies = function(value) {
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
proto.dlkit.proto.relationship.HasParentFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.HasParentFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.HasParentFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.HasParentFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.HasParentFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.HasParentFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.HasParentFamiliesRequest}
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.HasParentFamiliesRequest;
  return proto.dlkit.proto.relationship.HasParentFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.HasParentFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.HasParentFamiliesRequest}
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.HasParentFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.HasParentFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.HasParentFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.HasParentFamiliesRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.HasParentFamiliesRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.IsParentOfFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsParentOfFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsParentOfFamilyReply.displayName = 'proto.dlkit.proto.relationship.IsParentOfFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsParentOfFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsParentOfFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isParentOfFamily: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.IsParentOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsParentOfFamilyReply;
  return proto.dlkit.proto.relationship.IsParentOfFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsParentOfFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsParentOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsParentOfFamily(value);
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
proto.dlkit.proto.relationship.IsParentOfFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsParentOfFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsParentOfFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsParentOfFamily();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_parent_of_family = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.prototype.getIsParentOfFamily = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.IsParentOfFamilyReply.prototype.setIsParentOfFamily = function(value) {
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
proto.dlkit.proto.relationship.IsParentOfFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsParentOfFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsParentOfFamilyRequest.displayName = 'proto.dlkit.proto.relationship.IsParentOfFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsParentOfFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsParentOfFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.relationship.IsParentOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsParentOfFamilyRequest;
  return proto.dlkit.proto.relationship.IsParentOfFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsParentOfFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsParentOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsParentOfFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsParentOfFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
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
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsParentOfFamilyRequest.prototype.hasId = function() {
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
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetParentFamilyIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.displayName = 'proto.dlkit.proto.relationship.GetParentFamilyIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetParentFamilyIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetParentFamilyIdsRequest}
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetParentFamilyIdsRequest;
  return proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetParentFamilyIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetParentFamilyIdsRequest}
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetParentFamilyIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetParentFamilyIdsRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.GetParentFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetParentFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetParentFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.GetParentFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetParentFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetParentFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetParentFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetParentFamiliesRequest;
  return proto.dlkit.proto.relationship.GetParentFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetParentFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetParentFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetParentFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetParentFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetParentFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetParentFamiliesRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetParentFamiliesRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsAncestorOfFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.displayName = 'proto.dlkit.proto.relationship.IsAncestorOfFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsAncestorOfFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isAncestorOfFamily: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.IsAncestorOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsAncestorOfFamilyReply;
  return proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsAncestorOfFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsAncestorOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsAncestorOfFamily(value);
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
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsAncestorOfFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsAncestorOfFamily();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_ancestor_of_family = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.prototype.getIsAncestorOfFamily = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.IsAncestorOfFamilyReply.prototype.setIsAncestorOfFamily = function(value) {
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
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.displayName = 'proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest;
  return proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
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
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsAncestorOfFamilyRequest.prototype.hasId = function() {
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
proto.dlkit.proto.relationship.HasChildFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.HasChildFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.HasChildFamiliesReply.displayName = 'proto.dlkit.proto.relationship.HasChildFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.HasChildFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.HasChildFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.HasChildFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasChildFamiliesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasChildFamilies: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.HasChildFamiliesReply}
 */
proto.dlkit.proto.relationship.HasChildFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.HasChildFamiliesReply;
  return proto.dlkit.proto.relationship.HasChildFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.HasChildFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.HasChildFamiliesReply}
 */
proto.dlkit.proto.relationship.HasChildFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasChildFamilies(value);
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
proto.dlkit.proto.relationship.HasChildFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.HasChildFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.HasChildFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasChildFamiliesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasChildFamilies();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_child_families = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.HasChildFamiliesReply.prototype.getHasChildFamilies = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.HasChildFamiliesReply.prototype.setHasChildFamilies = function(value) {
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
proto.dlkit.proto.relationship.HasChildFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.HasChildFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.HasChildFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.HasChildFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.HasChildFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.HasChildFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.HasChildFamiliesRequest}
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.HasChildFamiliesRequest;
  return proto.dlkit.proto.relationship.HasChildFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.HasChildFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.HasChildFamiliesRequest}
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.HasChildFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.HasChildFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.HasChildFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.HasChildFamiliesRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.HasChildFamiliesRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.IsChildOfFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsChildOfFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsChildOfFamilyReply.displayName = 'proto.dlkit.proto.relationship.IsChildOfFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsChildOfFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsChildOfFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isChildOfFamily: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.IsChildOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsChildOfFamilyReply;
  return proto.dlkit.proto.relationship.IsChildOfFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsChildOfFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsChildOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsChildOfFamily(value);
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
proto.dlkit.proto.relationship.IsChildOfFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsChildOfFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsChildOfFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsChildOfFamily();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_child_of_family = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.prototype.getIsChildOfFamily = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.IsChildOfFamilyReply.prototype.setIsChildOfFamily = function(value) {
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
proto.dlkit.proto.relationship.IsChildOfFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsChildOfFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsChildOfFamilyRequest.displayName = 'proto.dlkit.proto.relationship.IsChildOfFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsChildOfFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsChildOfFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.relationship.IsChildOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsChildOfFamilyRequest;
  return proto.dlkit.proto.relationship.IsChildOfFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsChildOfFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsChildOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsChildOfFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsChildOfFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
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
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsChildOfFamilyRequest.prototype.hasId = function() {
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
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetChildFamilyIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.displayName = 'proto.dlkit.proto.relationship.GetChildFamilyIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetChildFamilyIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetChildFamilyIdsRequest}
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetChildFamilyIdsRequest;
  return proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetChildFamilyIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetChildFamilyIdsRequest}
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetChildFamilyIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetChildFamilyIdsRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.GetChildFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetChildFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetChildFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.GetChildFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetChildFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetChildFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetChildFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetChildFamiliesRequest;
  return proto.dlkit.proto.relationship.GetChildFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetChildFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetChildFamiliesRequest}
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetChildFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetChildFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetChildFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetChildFamiliesRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetChildFamiliesRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsDescendantOfFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.displayName = 'proto.dlkit.proto.relationship.IsDescendantOfFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsDescendantOfFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isDescendantOfFamily: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.IsDescendantOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsDescendantOfFamilyReply;
  return proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsDescendantOfFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsDescendantOfFamilyReply}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsDescendantOfFamily(value);
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
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsDescendantOfFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsDescendantOfFamily();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_descendant_of_family = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.prototype.getIsDescendantOfFamily = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.IsDescendantOfFamilyReply.prototype.setIsDescendantOfFamily = function(value) {
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
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.displayName = 'proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest;
  return proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
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
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.IsDescendantOfFamilyRequest.prototype.hasId = function() {
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
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyNodeIdsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyNodeIdsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodeIdsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodeIdsReply}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyNodeIdsReply;
  return proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodeIdsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodeIdsReply}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodeIdsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.prototype.getNode = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Node} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Node, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Node|undefined} value */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.prototype.setNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.prototype.clearNode = function() {
  this.setNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsReply.prototype.hasNode = function() {
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
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    descendantLevels: jspb.Message.getFieldWithDefault(msg, 2, 0),
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest;
  return proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
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
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional sint32 descendant_levels = 2;
 * @return {number}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional bool include_siblings = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.GetFamilyNodeIdsRequest.prototype.setIncludeSiblings = function(value) {
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
proto.dlkit.proto.relationship.GetFamilyNodesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyNodesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyNodesReply.displayName = 'proto.dlkit.proto.relationship.GetFamilyNodesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyNodesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyNode: (f = msg.getFamilyNode()) && proto.dlkit.proto.relationship.FamilyNode.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodesReply}
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyNodesReply;
  return proto.dlkit.proto.relationship.GetFamilyNodesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodesReply}
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.relationship.FamilyNode;
      reader.readMessage(value,proto.dlkit.proto.relationship.FamilyNode.deserializeBinaryFromReader);
      msg.setFamilyNode(value);
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
proto.dlkit.proto.relationship.GetFamilyNodesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyNodesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyNode();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.relationship.FamilyNode.serializeBinaryToWriter
    );
  }
};


/**
 * optional FamilyNode family_node = 1;
 * @return {?proto.dlkit.proto.relationship.FamilyNode}
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.prototype.getFamilyNode = function() {
  return /** @type{?proto.dlkit.proto.relationship.FamilyNode} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.relationship.FamilyNode, 1));
};


/** @param {?proto.dlkit.proto.relationship.FamilyNode|undefined} value */
proto.dlkit.proto.relationship.GetFamilyNodesReply.prototype.setFamilyNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.GetFamilyNodesReply.prototype.clearFamilyNode = function() {
  this.setFamilyNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyNodesReply.prototype.hasFamilyNode = function() {
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
proto.dlkit.proto.relationship.GetFamilyNodesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.GetFamilyNodesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.GetFamilyNodesRequest.displayName = 'proto.dlkit.proto.relationship.GetFamilyNodesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.GetFamilyNodesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    descendantLevels: jspb.Message.getFieldWithDefault(msg, 2, 0),
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodesRequest}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.GetFamilyNodesRequest;
  return proto.dlkit.proto.relationship.GetFamilyNodesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.GetFamilyNodesRequest}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.GetFamilyNodesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.GetFamilyNodesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
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
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional sint32 descendant_levels = 2;
 * @return {number}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional bool include_siblings = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.GetFamilyNodesRequest.prototype.setIncludeSiblings = function(value) {
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
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.displayName = 'proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canModifyFamilyHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply;
  return proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanModifyFamilyHierarchy(value);
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
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanModifyFamilyHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_modify_family_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.prototype.getCanModifyFamilyHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyReply.prototype.setCanModifyFamilyHierarchy = function(value) {
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
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.displayName = 'proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest;
  return proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest}
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.CanModifyFamilyHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AddRootFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AddRootFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AddRootFamilyReply.displayName = 'proto.dlkit.proto.relationship.AddRootFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AddRootFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AddRootFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AddRootFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddRootFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.AddRootFamilyReply}
 */
proto.dlkit.proto.relationship.AddRootFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AddRootFamilyReply;
  return proto.dlkit.proto.relationship.AddRootFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AddRootFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AddRootFamilyReply}
 */
proto.dlkit.proto.relationship.AddRootFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.AddRootFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AddRootFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AddRootFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddRootFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AddRootFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AddRootFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AddRootFamilyRequest.displayName = 'proto.dlkit.proto.relationship.AddRootFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AddRootFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AddRootFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.AddRootFamilyRequest}
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AddRootFamilyRequest;
  return proto.dlkit.proto.relationship.AddRootFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AddRootFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AddRootFamilyRequest}
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.AddRootFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AddRootFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AddRootFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AddRootFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.AddRootFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AddRootFamilyRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.RemoveRootFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RemoveRootFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RemoveRootFamilyReply.displayName = 'proto.dlkit.proto.relationship.RemoveRootFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RemoveRootFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RemoveRootFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveRootFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RemoveRootFamilyReply}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RemoveRootFamilyReply;
  return proto.dlkit.proto.relationship.RemoveRootFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RemoveRootFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RemoveRootFamilyReply}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RemoveRootFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RemoveRootFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RemoveRootFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveRootFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RemoveRootFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RemoveRootFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RemoveRootFamilyRequest.displayName = 'proto.dlkit.proto.relationship.RemoveRootFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RemoveRootFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RemoveRootFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.RemoveRootFamilyRequest}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RemoveRootFamilyRequest;
  return proto.dlkit.proto.relationship.RemoveRootFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RemoveRootFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RemoveRootFamilyRequest}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RemoveRootFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RemoveRootFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.RemoveRootFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.RemoveRootFamilyRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.AddChildFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AddChildFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AddChildFamilyReply.displayName = 'proto.dlkit.proto.relationship.AddChildFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AddChildFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AddChildFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AddChildFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddChildFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.AddChildFamilyReply}
 */
proto.dlkit.proto.relationship.AddChildFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AddChildFamilyReply;
  return proto.dlkit.proto.relationship.AddChildFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AddChildFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AddChildFamilyReply}
 */
proto.dlkit.proto.relationship.AddChildFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.AddChildFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AddChildFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AddChildFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddChildFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.AddChildFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.AddChildFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.AddChildFamilyRequest.displayName = 'proto.dlkit.proto.relationship.AddChildFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.AddChildFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.AddChildFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    childId: (f = msg.getChildId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.AddChildFamilyRequest}
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.AddChildFamilyRequest;
  return proto.dlkit.proto.relationship.AddChildFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.AddChildFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.AddChildFamilyRequest}
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.AddChildFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.AddChildFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getChildId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFamilyId();
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
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.hasChildId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.AddChildFamilyRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.RemoveChildFamilyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RemoveChildFamilyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RemoveChildFamilyReply.displayName = 'proto.dlkit.proto.relationship.RemoveChildFamilyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RemoveChildFamilyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamilyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamilyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamilyReply}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RemoveChildFamilyReply;
  return proto.dlkit.proto.relationship.RemoveChildFamilyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamilyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamilyReply}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RemoveChildFamilyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RemoveChildFamilyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamilyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamilyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RemoveChildFamilyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RemoveChildFamilyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RemoveChildFamilyRequest.displayName = 'proto.dlkit.proto.relationship.RemoveChildFamilyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RemoveChildFamilyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamilyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    childId: (f = msg.getChildId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamilyRequest}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RemoveChildFamilyRequest;
  return proto.dlkit.proto.relationship.RemoveChildFamilyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamilyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamilyRequest}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RemoveChildFamilyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamilyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getChildId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFamilyId();
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
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.hasChildId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.RemoveChildFamilyRequest.prototype.hasFamilyId = function() {
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
proto.dlkit.proto.relationship.RemoveChildFamiliesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RemoveChildFamiliesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RemoveChildFamiliesReply.displayName = 'proto.dlkit.proto.relationship.RemoveChildFamiliesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RemoveChildFamiliesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamiliesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamiliesReply}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RemoveChildFamiliesReply;
  return proto.dlkit.proto.relationship.RemoveChildFamiliesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamiliesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamiliesReply}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.relationship.RemoveChildFamiliesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RemoveChildFamiliesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamiliesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.relationship.RemoveChildFamiliesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.displayName = 'proto.dlkit.proto.relationship.RemoveChildFamiliesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamiliesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    familyId: (f = msg.getFamilyId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamiliesRequest}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.relationship.RemoveChildFamiliesRequest;
  return proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamiliesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.relationship.RemoveChildFamiliesRequest}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFamilyId(value);
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
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.relationship.RemoveChildFamiliesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFamilyId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id family_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.prototype.getFamilyId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.prototype.setFamilyId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.prototype.clearFamilyId = function() {
  this.setFamilyId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.relationship.RemoveChildFamiliesRequest.prototype.hasFamilyId = function() {
  return jspb.Message.getField(this, 1) != null;
};


goog.object.extend(exports, proto.dlkit.proto.relationship);
